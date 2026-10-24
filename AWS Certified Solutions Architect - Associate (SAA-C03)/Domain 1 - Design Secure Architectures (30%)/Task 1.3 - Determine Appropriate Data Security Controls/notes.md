# Task 1.3 — Determine Appropriate Data Security Controls

> This task covers **encryption (at rest and in transit), key management, data classification and governance, retention, and backup/recovery**. The recurring exam themes are: which encryption option fits, how to retrofit encryption onto existing resources, how to make data immutable, and how to centralize backups.

---

# 1. Encryption Fundamentals

## 1.1 At rest vs in transit

- **Encryption at rest** protects data sitting on disk — in S3, EBS, EFS, FSx, RDS, DynamoDB, Redshift, snapshots, and backups. It defends against physical media theft and against someone obtaining the underlying storage.
- **Encryption in transit** protects data moving over a network — TLS/SSL for HTTPS and database connections, IPsec for VPNs, and SSH. It defends against interception and man-in-the-middle attacks.

A complete design uses both, plus access control. Encryption is **not** a substitute for IAM: if a principal is allowed to call `s3:GetObject` and `kms:Decrypt`, encryption is transparent to them.

## 1.2 Symmetric vs asymmetric

- **Symmetric** — one key encrypts and decrypts (AES-256). Fast, and the default for every AWS service integration. A symmetric KMS key never leaves KMS in plaintext.
- **Asymmetric** — a mathematically linked public/private key pair (RSA or ECC). KMS supports asymmetric keys for **encrypt/decrypt** (when a party outside AWS must encrypt without calling KMS) and for **sign/verify** (digital signatures). The public key can be downloaded and distributed; the private key never leaves KMS.

## 1.3 Envelope encryption — the central concept

KMS will only directly encrypt payloads up to **4 KB**. Real data is much larger, so AWS services use **envelope encryption**:

1. The service calls **`GenerateDataKey`** against a KMS key (also called the CMK, or root key).
2. KMS returns **two** things: a **plaintext data key** and an **encrypted copy of that data key** (encrypted under the KMS key).
3. The service encrypts your data locally with the plaintext data key (AES-256), then **discards the plaintext key from memory**.
4. The **encrypted data key is stored alongside the ciphertext**.
5. To decrypt, the service sends the encrypted data key to KMS (`Decrypt`), gets the plaintext key back, decrypts the data, and discards the key again.

Why this matters:
- Large objects never traverse the KMS API — only small keys do.
- You get a single point of control: **deleting or disabling the KMS key makes every object encrypted under it undecryptable**, which is the "crypto-shredding" answer for data destruction requirements.
- Every `Decrypt` call is **logged in CloudTrail**, giving you an audit trail of data access.
- KMS request volume (and cost) scales with the number of operations — mitigated by **data key caching** and, for S3, by **S3 Bucket Keys**.

---

# 2. AWS KMS in Depth

## 2.1 What KMS is

A managed service for creating and controlling cryptographic keys, backed by **FIPS 140-2 validated hardware security modules**. Key material **never leaves KMS unencrypted**, KMS is integrated with virtually every AWS service, and **every key usage is recorded in CloudTrail**.

**KMS keys are Regional.** A key created in `ap-south-1` cannot decrypt data in `us-east-1`. To work across Regions you either re-encrypt with a destination-Region key (what S3 replication does automatically if configured) or create a **multi-Region key** — a primary key plus related replicas sharing the same key material and key ID suffix, so ciphertext from one Region can be decrypted in another.

## 2.2 Key types

| Type | Managed by | Rotation | Visible / controllable | Cost |
|---|---|---|---|---|
| **AWS owned keys** | AWS, shared across many accounts | AWS-controlled | Not visible in your account, no policy control | Free |
| **AWS managed keys** (`aws/s3`, `aws/ebs`, `aws/rds`) | AWS, one per service per account | **Automatic, every year, cannot be disabled** | Visible; **key policy cannot be edited** | Free (pay per API call) |
| **Customer managed keys (CMK)** | You | **Optional automatic rotation**, default yearly, configurable 90–2,560 days | Full control: key policy, grants, aliases, enable/disable, schedule deletion, tags | ~$1/month per key + API calls |
| **Imported key material (BYOK)** | You import 256-bit material | **Manual only** (import new material into a new key) | You can delete the material immediately, and set an expiry | Same as CMK |
| **Custom key store (CloudHSM-backed)** | You, in a dedicated CloudHSM cluster | Manual | Full control, single-tenant HSMs | CMK cost + CloudHSM cost |
| **External key store (XKS)** | Key material held **outside AWS** in your own HSM/key manager | You | Full control, highest separation | Highest complexity |

**When the exam wants a CMK:** whenever the requirement mentions auditing key usage, controlling who can use the key, rotating on your own schedule, sharing a key cross-account, or disabling/deleting a key. AWS managed keys cannot do any of those.

## 2.3 Key rotation — what actually changes

- **Automatic rotation of a customer managed key** creates **new backing key material** on schedule while keeping the **same key ID, ARN, and alias**. AWS retains all previous backing keys so old ciphertext still decrypts. Your applications need no changes and nothing has to be re-encrypted. New encrypt operations use the newest material.
- **AWS managed keys** rotate automatically every year; you cannot turn it off or change the period.
- **Imported key material cannot be automatically rotated** — you must import new material (into a new key) and re-encrypt or re-point an alias.
- **Manual rotation** = create a brand-new key and update the **alias** to point at it. Old data still requires the old key, so keep it enabled.
- **On-demand rotation** is also supported for CMKs.

## 2.4 Key policies, grants and IAM

Every KMS key has a **key policy**, and it is **mandatory and authoritative**. Unlike S3, where an IAM policy alone can grant access, **IAM policies cannot grant access to a KMS key unless the key policy delegates to IAM**:

```json
{
  "Sid": "EnableIAMUserPermissions",
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
  "Action": "kms:*",
  "Resource": "*"
}
```

This statement (created by default) means "IAM policies in this account may be used to control this key."

**Grants** are a second mechanism: temporary, programmatic, fine-grained permissions typically created by AWS services on your behalf (for example, when EBS needs ongoing access to decrypt a volume). They support `CreateGrant`, `RetireGrant`, and `RevokeGrant`, and are preferred over editing policies for short-lived delegation.

**Important KMS actions:** `kms:Encrypt`, `kms:Decrypt`, `kms:ReEncrypt*`, `kms:GenerateDataKey*`, `kms:DescribeKey`, `kms:CreateGrant`, `kms:ScheduleKeyDeletion`.

**Condition keys:**
- **`kms:ViaService`** — the key can only be used through a named service endpoint, e.g., `"kms:ViaService": "s3.ap-south-1.amazonaws.com"`. This prevents someone using the key directly through the KMS API.
- **`kms:EncryptionContext:<key>`** — the encryption context is additional authenticated data (AAD) supplied at encrypt time; it is **not secret** but is **logged in CloudTrail** and must match exactly at decrypt time. Great for binding a ciphertext to a specific tenant or purpose.
- `kms:CallerAccount`, `kms:GrantIsForAWSResource`.

**Cross-account key use:** the key policy in the owning account must allow the external principal, **and** the external account's IAM policy must allow the KMS actions. This "both sides" rule mirrors general cross-account behaviour.

## 2.5 Key deletion and disabling

- You cannot delete a KMS key immediately. You **schedule deletion** with a waiting period of **7 to 30 days** (default 30). During that window the key is unusable but recoverable.
- **Disabling** a key is instant and reversible — the better choice if you just need to stop usage temporarily.
- Deleting a key permanently destroys all data encrypted under it. Use `kms:ScheduleKeyDeletion` deliberately and consider an SCP denying it.

## 2.6 Quotas and cost control

KMS enforces a shared per-Region quota on cryptographic operations (on the order of 5,500 to 50,000 requests per second depending on Region and operation type). High-volume workloads can hit `ThrottlingException`. Mitigations:
- **S3 Bucket Keys** — a bucket-level data key is generated and reused for many objects, cutting KMS requests (and cost) by **up to 99%**. Enable this whenever a bucket uses SSE-KMS at scale.
- **Data key caching** in the AWS Encryption SDK.
- Request a quota increase.

## 2.7 AWS CloudHSM

A **single-tenant, dedicated hardware security module** cluster in your VPC, validated to **FIPS 140-2 Level 3**. You control the HSM users and keys; **AWS has no access to your key material** and cannot recover it if you lose credentials.

Use CloudHSM when:
- A regulation requires single-tenant, customer-controlled HSMs or FIPS 140-2 Level 3
- You need PKCS#11, JCE, or Microsoft CNG/KSP interfaces
- You are offloading SSL/TLS processing or running a private certificate authority
- You need Oracle TDE or SQL Server TDE with keys you alone hold
- You want a **KMS custom key store** (KMS front end, CloudHSM key storage)

Trade-offs: you manage clustering, backups, and users; it is far more expensive than KMS; and it is not natively integrated with most AWS services except through KMS custom key stores.

---

# 3. Encryption by Service — the details that get tested

## 3.1 Amazon S3

**Server-side encryption options:**

| Option | Key management | Notes |
|---|---|---|
| **SSE-S3** (AES-256) | AWS-managed, fully transparent | **Applied by default to all new objects**; free; no audit trail per object |
| **SSE-KMS** | KMS key (AWS managed `aws/s3` or your CMK) | CloudTrail audit of key usage, key policy control, **KMS request charges** (mitigate with Bucket Keys) |
| **DSSE-KMS** | Two independent layers of KMS encryption | For workloads with dual-layer regulatory requirements |
| **SSE-C** | **Customer-provided key sent with every request** | AWS encrypts/decrypts but **stores no key**; **HTTPS is mandatory**; you must manage and supply the key, and losing it means losing the data |
| **Client-side encryption** | You encrypt before upload (S3 Encryption Client, KMS or your own key) | AWS never sees plaintext |

**Enforcing encryption:** set **default bucket encryption** (so unspecified uploads get encrypted), and add a **bucket policy that denies PutObject** when the `s3:x-amz-server-side-encryption` header is missing or not the required value. To force a specific key, also condition on `s3:x-amz-server-side-encryption-aws-kms-key-id`.

**Enforcing TLS:**
```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::bucket", "arn:aws:s3:::bucket/*"],
  "Condition": { "Bool": { "aws:SecureTransport": "false" } }
}
```

**Other S3 data-protection controls:**
- **S3 Block Public Access** — four settings available at the **account** and **bucket** level that override any bucket policy or ACL granting public access. This is the first answer to "prevent accidental public exposure," and account-level is the stronger control.
- **Object Ownership = Bucket owner enforced** — disables ACLs entirely so access is governed only by policies. Recommended for all new buckets.
- **Versioning** — keeps every version of an object; deletes insert a **delete marker** rather than destroying data. Required for replication and Object Lock.
- **MFA Delete** — requires an MFA code to permanently delete an object version or to change the versioning state. Can only be enabled by the **root user** via CLI/API.
- **S3 Object Lock (WORM)** — prevents object versions from being deleted or overwritten for a retention period or indefinitely under a legal hold. Requires versioning, and must be enabled at bucket creation (or via support for existing buckets).
  - **Governance mode** — users with the special permission `s3:BypassGovernanceRetention` can shorten or remove the lock. Use for internal policy enforcement.
  - **Compliance mode** — **nobody**, including the root user and AWS, can shorten retention or delete the version until it expires. Use for regulatory requirements (SEC 17a-4, FINRA).
  - **Legal hold** — indefinite, independent of a retention period, removable by a user with the right permission.
- **S3 Glacier Vault Lock** — the equivalent WORM control for Glacier vaults, locked with a policy that becomes immutable after validation.
- **Access points** and **Multi-Region Access Points** — per-application hostnames with their own policies, simplifying access control on a shared bucket.
- **Presigned URLs** — grant temporary access to a specific object using the signer's permissions, with an expiry.

## 3.2 Amazon EBS

- Encryption uses **KMS with AES-256**, is transparent to the instance, and has a negligible performance impact.
- When a volume is encrypted, so are: **data at rest on the volume, data in transit between the instance and the volume, all snapshots of it, and all volumes created from those snapshots**.
- **You cannot encrypt an existing unencrypted volume in place, and you cannot remove encryption.** The workflow is: **create a snapshot → copy the snapshot with encryption enabled (choosing a key) → create a new volume (or AMI) from the encrypted copy → attach it**.
- **EBS encryption by default** can be enabled per account per Region, so every new volume and snapshot is encrypted automatically.
- **Sharing encrypted snapshots across accounts** requires a **customer managed key** (AWS managed keys cannot be shared); you share both the snapshot and the key. **Encrypted snapshots can never be made public.**
- Root volumes can be encrypted at launch, and AMIs can be copied with encryption to produce encrypted-by-default images.

## 3.3 Amazon EFS and FSx

- **EFS**: encryption at rest uses KMS and **can only be enabled at file system creation**; encryption in transit uses **TLS via the EFS mount helper** (`-o tls`). Access control combines **IAM** (file system policy), **EFS Access Points** (enforce a POSIX user/group and root directory per application), security groups, and POSIX permissions. A file system policy can enforce `elasticfilesystem:ClientRootAccess` restrictions and require TLS with `aws:SecureTransport`.
- **FSx for Windows File Server**: encrypted at rest with KMS by default; in transit with **SMB Kerberos session encryption**. Integrates with Active Directory for authentication and NTFS ACLs.
- **FSx for Lustre**: encryption at rest by default; in-transit encryption supported on specific instance types in the same VPC.
- **FSx for NetApp ONTAP / OpenZFS**: KMS at rest, plus their native protocol encryption.

## 3.4 Amazon RDS and Aurora

- Encryption at rest uses **KMS** and **must be enabled when the DB instance/cluster is created**. To encrypt an existing unencrypted database: **snapshot → copy the snapshot with encryption → restore from the encrypted snapshot** (then cut over).
- Once encrypted: automated backups, snapshots, read replicas, and (for Aurora) the cluster volume are all encrypted. **You cannot have an encrypted replica of an unencrypted primary, or vice versa.**
- **Encryption in transit**: RDS provides a CA bundle; clients connect with TLS. You can force it: PostgreSQL parameter `rds.force_ssl=1`, MySQL `require_secure_transport=ON`, SQL Server `rds.force_ssl`.
- **Transparent Data Encryption (TDE)** is additionally available for Oracle and SQL Server via option groups, optionally backed by CloudHSM.
- **IAM database authentication** removes stored passwords (15-minute tokens) for MySQL, PostgreSQL, and Aurora.
- **Performance Insights** data and logs can also be encrypted with KMS.

## 3.5 DynamoDB, and other services

- **DynamoDB is encrypted at rest by default** — you choose an AWS owned key (default, free), an AWS managed key, or a customer managed key. Encryption cannot be disabled.
- Fine-grained access control uses IAM conditions such as **`dynamodb:LeadingKeys`** (restrict a user to items whose partition key matches their identity) and `dynamodb:Attributes` with a projection expression for column-level control.
- **Amazon Redshift** — cluster encryption with KMS or HSM, chosen at creation; encrypted in transit with TLS.
- **SQS, SNS, Kinesis, EventBridge** — SSE with KMS, optional.
- **Amazon EBS-backed AMIs, EMR, SageMaker, Glue, Athena results, CloudWatch Logs** — all support KMS encryption.
- **AWS CloudTrail** — logs are SSE-S3 encrypted by default; use **SSE-KMS** plus **log file validation** (digest files) to make tampering detectable. Store in a dedicated Log Archive account with **Object Lock**.
- **Lambda** — environment variables encrypted with KMS at rest; use a CMK plus encryption helpers for sensitive values.

---

# 4. Encryption in Transit and AWS Certificate Manager

## 4.1 ACM essentials

- **ACM issues free public TLS/SSL certificates** for use with integrated services: **Elastic Load Balancing (ALB/NLB), CloudFront, API Gateway, App Runner, Amplify, Elastic Beanstalk, and AWS-managed endpoints**.
- **Validation methods:**
  - **DNS validation (recommended)** — you add a CNAME record; ACM can then **renew the certificate automatically and indefinitely** as long as the record stays in place. With Route 53 ACM can create the record for you.
  - **Email validation** — sent to domain contacts; renewal requires manual action, so it is fragile.
- **Certificates are Regional.** An ALB needs the certificate in the ALB's Region. **CloudFront requires the certificate in `us-east-1`** regardless of where your origin lives.
- **Public ACM certificates cannot be exported.** You cannot install them on an EC2 instance or an on-premises server. For those cases use:
  - **AWS Private CA (ACM Private CA)** — issues private certificates you *can* export, for internal services, IoT devices, containers, and EC2
  - Import a third-party certificate into ACM (then **you** are responsible for renewal — imported certificates are **not** auto-renewed)
- **SNI (Server Name Indication)** allows one ALB or CloudFront distribution to serve many certificates/domains.
- **Monitoring expiry**: ACM emits `Days to Expiry` CloudWatch metrics and EventBridge events; the AWS Config rule **`acm-certificate-expiration-check`** flags certificates nearing expiry. This matters mainly for imported certificates.

## 4.2 Where to terminate TLS

- **At CloudFront** — closest to the user, best performance; CloudFront can then re-encrypt to the origin (HTTPS only is the secure setting).
- **At the ALB** — common; the ALB holds the ACM certificate, and you can optionally re-encrypt to targets.
- **At the instance (end-to-end encryption)** — required when regulation forbids plaintext anywhere; use an **NLB with TCP passthrough** or an ALB with HTTPS targets, and install certificates on instances (from Private CA or imported).

---

# 5. Data Classification, Governance and Compliance

## 5.1 Classification

Classification is the process of labelling data by sensitivity (e.g., Public, Internal, Confidential, Restricted) so that controls can be applied consistently.

- **Amazon Macie** automates discovery in **S3**: it inventories buckets (public access, encryption status, sharing) and runs sensitive data discovery jobs using managed identifiers (names, addresses, credit cards, passports, AWS keys, medical identifiers) and **custom data identifiers** (your own regex). Findings go to Security Hub and EventBridge for automated response.
- **Tagging** turns classification into an enforceable control: tag resources `Classification=Confidential`, then use **ABAC** conditions (`aws:ResourceTag`) to restrict access, and **tag policies** in Organizations to keep tag keys/values consistent.
- **AWS Glue Data Catalog + Lake Formation** classify and govern structured data in a data lake, with **column-, row-, and cell-level permissions** — the right answer when a question asks for fine-grained analytics access control.

## 5.2 Governance tooling

- **AWS Config** — continuous configuration recording plus managed rules such as `s3-bucket-server-side-encryption-enabled`, `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `rds-storage-encrypted`, `iam-user-mfa-enabled`, `acm-certificate-expiration-check`. Rules can trigger **automatic remediation** via SSM Automation documents. **Conformance packs** bundle rules into a compliance framework and can be deployed org-wide.
- **AWS Organizations policies** — SCPs to deny unencrypted actions, tag policies, backup policies.
- **AWS Artifact** — self-service portal for AWS's own compliance reports (SOC 1/2/3, PCI DSS AoC, ISO certifications) and agreements (including the **HIPAA BAA** and GDPR DPA). The answer when an auditor asks for AWS's certifications.
- **AWS Audit Manager** — continuously collects evidence from your environment and maps it to prebuilt frameworks (HIPAA, PCI DSS v3.2.1, GDPR, SOC 2, CIS), producing assessment reports. The answer when the requirement is evidence collection about **your** workloads.
- **AWS Security Hub** — compliance standards scoring and finding aggregation.

## 5.3 Common compliance mappings

| Requirement | Typical AWS implementation |
|---|---|
| **HIPAA** | Use HIPAA-eligible services, sign the **BAA** via Artifact, encrypt PHI at rest (KMS) and in transit (TLS), enable CloudTrail, restrict access with IAM, log and monitor |
| **PCI DSS** | Network segmentation (separate VPC/account for the CDE), WAF, encryption, key management with KMS/CloudHSM, CloudTrail + Config, quarterly scanning (Inspector) |
| **GDPR** | Choose EU Regions for residency, encrypt, implement deletion workflows (lifecycle rules, crypto-shredding), DPA via Artifact, Macie for discovery |
| **Data residency** | Region selection + **SCP restricting `aws:RequestedRegion`**, avoid global replication, Outposts/Local Zones if on-soil infrastructure is required |
| **Immutable audit records** | S3 **Object Lock compliance mode** or Glacier Vault Lock, CloudTrail log file validation, separate Log Archive account |

---

# 6. Backups, Replication and Recovery

## 6.1 AWS Backup

A centralized, policy-driven backup service covering **EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, Storage Gateway, S3, DocumentDB, Neptune, Redshift, Timestream, and VMware workloads**.

Core concepts:
- **Backup plan** — rules defining frequency (cron), backup window, **lifecycle** (transition to **cold storage** after N days, with a 90-day minimum in cold, and expiry), and copy actions.
- **Backup vault** — the destination; encrypted with KMS, with a vault access policy.
- **AWS Backup Vault Lock** — WORM for backups. **Governance mode** allows privileged users to make changes; **Compliance mode** is immutable — once the cooling-off period passes, **no one, including the root user or AWS Support, can delete recovery points or shorten retention**.
- **Resource assignment by tag** — "back up everything tagged `Backup=Daily`," so new resources are covered automatically.
- **Cross-Region and cross-account copy** — essential for DR and for protecting against account compromise.
- **Organization backup policies** — enforce plans across all accounts from the management account.
- **Restore testing** — scheduled automated restore validation.

The exam answer for *"centralize, automate, and enforce backups across multiple services and accounts with retention and compliance"* is **AWS Backup**.

## 6.2 Service-native mechanisms

**Amazon S3**
- **Versioning** protects against overwrite and accidental delete.
- **Replication**: **SRR** (same-Region, for log aggregation or sovereignty) and **CRR** (cross-Region, for DR and latency). Requirements: versioning on **both** buckets, an IAM role for S3 to assume, and (for cross-account) a destination bucket policy. Replication can change **storage class** and **ownership**, and can replicate delete markers if configured.
- **Replication only applies to objects written after it is enabled** — use **S3 Batch Replication** to backfill existing objects. This is a very common exam detail.
- **S3 Replication Time Control (RTC)** adds a **15-minute SLA** and replication metrics.
- **Lifecycle rules** for transitions and expirations, including noncurrent versions.

**Amazon EBS**
- **Snapshots** are incremental, stored durably in S3 (in an AWS-managed account), and can be copied cross-Region and cross-account.
- Automate with **Amazon Data Lifecycle Manager (DLM)** or AWS Backup.
- **Fast Snapshot Restore** pre-warms snapshots so restored volumes deliver full performance immediately.
- **Recycle Bin** retains deleted snapshots and AMIs for a configurable period so accidental deletions can be undone.
- **EBS Snapshot Archive** stores rarely needed snapshots at up to 75% lower cost (90-day minimum, 24–72 hour restore).

**Amazon RDS / Aurora**
- **Automated backups**: retention **0–35 days**, enabling **point-in-time recovery** to any second within the window (typically to within ~5 minutes of now). Stored in S3; deleting the instance can delete them unless you take a final snapshot.
- **Manual snapshots** persist until explicitly deleted and can be copied/shared (encrypted snapshots need a CMK to be shared).
- **Cross-Region automated backup replication** for RDS.
- **Aurora** continuously backs up to S3 with no performance impact, supports PITR, **Backtrack** (Aurora MySQL — rewind the cluster in place in seconds without a restore), and **fast database cloning** (copy-on-write).

**Amazon DynamoDB**
- **Point-in-time recovery (PITR)** — continuous backups with restore to any second in the last **35 days**.
- **On-demand backups** — full backups retained until deleted, with no performance impact.
- **Global tables** for multi-Region redundancy (not a substitute for backups — a bad write replicates).

**EFS / FSx** — AWS Backup integration, EFS **Replication** for cross-Region copies, FSx automatic daily backups and Multi-AZ options.

## 6.3 Retention and lifecycle

**S3 Lifecycle** supports two action types:
- **Transition** between storage classes (Standard → Standard-IA → Intelligent-Tiering → Glacier Instant Retrieval → Glacier Flexible Retrieval → Deep Archive)
- **Expiration** — delete current versions, delete **noncurrent versions** after N days, **remove expired delete markers**, and **abort incomplete multipart uploads** (a frequently forgotten source of invisible cost)

**Minimum storage durations to remember:** Standard-IA and One Zone-IA **30 days**; Glacier Instant Retrieval **90 days**; Glacier Flexible Retrieval **90 days**; Deep Archive **180 days**. Deleting earlier incurs a prorated early-deletion charge. Objects must also be at least 30 days old before transitioning from Standard to Standard-IA.

**Retention principle for the exam:** align retention to the stated compliance requirement, use lifecycle automation rather than scripts, and use Object Lock/Vault Lock only where immutability is genuinely required (because you then *cannot* delete early to save money).

---

# 7. Worked Scenarios

**Scenario 1 — "Financial records must be immutable for 7 years; not even an administrator may delete them."**
S3 with versioning + **Object Lock in compliance mode** with a 7-year retention period, in a dedicated account, with a lifecycle rule transitioning to Glacier Deep Archive for cost. Governance mode would be wrong because it can be bypassed.

**Scenario 2 — "Encrypt an existing production RDS database with minimal data loss."**
Take a snapshot → copy the snapshot specifying a KMS key → restore a new instance from the encrypted copy → use DMS or a short maintenance window to cut over. Encryption cannot be toggled on an existing instance.

**Scenario 3 — "Our SSE-KMS bucket is throttling and KMS costs are high."**
Enable **S3 Bucket Keys** to reduce KMS calls by up to 99%; consider data key caching for custom applications; request a quota increase if still needed.

**Scenario 4 — "We must prove exactly who decrypted customer data and when."**
Use a **customer managed KMS key** with **encryption context**, and review **CloudTrail** `Decrypt` events. AWS owned/managed keys do not give you the same control.

**Scenario 5 — "A departing engineer must no longer be able to read archived data, and we must guarantee the data is unrecoverable."**
Crypto-shredding: **schedule deletion of the KMS key** (7–30 day window) so all ciphertext encrypted under it becomes permanently undecryptable.

**Scenario 6 — "Backups must be protected even if the production account is compromised."**
AWS Backup with **cross-account copy** into an isolated backup account, **Vault Lock in compliance mode**, and an SCP preventing deletion. For S3, add CRR to a bucket in another account with Object Lock.

**Scenario 7 — "Our CloudFront distribution needs a custom domain certificate."**
Request a public certificate in **ACM in us-east-1** with **DNS validation** so it auto-renews, then attach it to the distribution.

**Scenario 8 — "Developers keep creating unencrypted EBS volumes."**
Turn on **EBS encryption by default** in each Region, add an SCP denying `ec2:CreateVolume` when `ec2:Encrypted` is false, and add the Config rule `encrypted-volumes` with remediation for detection.

---

# 8. Quick Decision Table

| Requirement | Answer |
|---|---|
| Full control and audit of keys | **Customer managed KMS key** + CloudTrail |
| Keys must be single-tenant, FIPS 140-2 Level 3, AWS has no access | **AWS CloudHSM** (or KMS custom key store) |
| Keys must stay outside AWS entirely | **KMS External Key Store (XKS)** |
| Yearly key rotation with no application change | **Automatic rotation on a CMK** |
| Encrypt data > 4 KB with KMS | **Envelope encryption (`GenerateDataKey`)** |
| Encrypt an existing unencrypted RDS/EBS | **Snapshot → copy with encryption → restore** |
| Share an encrypted snapshot cross-account | **Customer managed key** shared with the other account |
| Guarantee all uploads are encrypted | Default bucket encryption **+ Deny bucket policy on the SSE header** |
| Force HTTPS to a bucket | **Deny when `aws:SecureTransport` is false** |
| Prevent accidental public buckets | **S3 Block Public Access (account level)** |
| Immutable records for a regulator | **S3 Object Lock, compliance mode** (or Glacier Vault Lock) |
| Prevent accidental version deletion | **Versioning + MFA Delete** |
| Restrict a key to one service | **`kms:ViaService` condition** |
| Bind ciphertext to a tenant and log it | **Encryption context** |
| Free, auto-renewing public TLS certificate | **ACM with DNS validation** (us-east-1 for CloudFront) |
| TLS certificate installed on EC2 | **AWS Private CA** or an imported certificate |
| Discover PII in S3 | **Amazon Macie** |
| Column/row-level control over a data lake | **AWS Lake Formation** |
| Row-level control in DynamoDB | **`dynamodb:LeadingKeys` condition** |
| Centralized, policy-based, cross-account backups | **AWS Backup + Vault Lock + cross-account copy** |
| Immutable backups | **AWS Backup Vault Lock, compliance mode** |
| Restore a database to a point 2 hours ago | **Automated backups / PITR** |
| Replicate existing S3 objects to a new destination | **S3 Batch Replication** |
| 15-minute replication SLA | **S3 Replication Time Control** |
| Auditor wants AWS's SOC 2 report | **AWS Artifact** |
| Continuous evidence collection for our workloads | **AWS Audit Manager** |
| Detect and auto-fix unencrypted resources | **AWS Config rules + SSM remediation** |
