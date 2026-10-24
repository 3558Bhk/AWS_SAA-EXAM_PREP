# AWS Certified Solutions Architect – Associate (SAA-C03)
## Complete Consolidated Study Notes

> Every task-level `notes.md` in this study pack, merged into one continuous document.
> Use the per-task folders for focused study and practice questions; use this file for
> linear reading, search, printing, or final revision.

---

## Exam at a Glance

| Item | Detail |
|---|---|
| **Exam code** | SAA-C03 |
| **Questions** | 65 (50 scored + 15 unscored) |
| **Duration** | 130 minutes |
| **Passing score** | 720 / 1000 (scaled, compensatory) |
| **Question types** | Multiple choice, multiple response |
| **Cost** | 150 USD |
| **Delivery** | Pearson VUE test centre or online proctored |
| **Validity** | 3 years |

## Domain Weighting

| Domain | Weight | Approx. scored questions |
|---|---|---|
| Domain 1 — Design Secure Architectures | **30%** | ~15 |
| Domain 2 — Design Resilient Architectures | **26%** | ~13 |
| Domain 3 — Design High-Performing Architectures | **24%** | ~12 |
| Domain 4 — Design Cost-Optimized Architectures | **20%** | ~10 |

---

## Table of Contents

- [Domain 1 — Design Secure Architectures (30%)](#domain-1--design-secure-architectures-30)
  - [Task 1.1 — Design Secure Access to AWS Resources](#task-11--design-secure-access-to-aws-resources)
  - [Task 1.2 — Design Secure Workloads and Applications](#task-12--design-secure-workloads-and-applications)
  - [Task 1.3 — Determine Appropriate Data Security Controls](#task-13--determine-appropriate-data-security-controls)
- [Domain 2 — Design Resilient Architectures (26%)](#domain-2--design-resilient-architectures-26)
  - [Task 2.1 — Design Scalable and Loosely Coupled Architectures](#task-21--design-scalable-and-loosely-coupled-architectures)
  - [Task 2.2 — Design Highly Available and/or Fault-Tolerant Architectures](#task-22--design-highly-available-andor-fault-tolerant-architectures)
- [Domain 3 — Design High-Performing Architectures (24%)](#domain-3--design-high-performing-architectures-24)
  - [Task 3.1 — Determine High-Performing and/or Scalable Storage Solutions](#task-31--determine-high-performing-andor-scalable-storage-solutions)
  - [Task 3.2 — Design High-Performing and Elastic Compute Solutions](#task-32--design-high-performing-and-elastic-compute-solutions)
  - [Task 3.3 — Determine High-Performing Database Solutions](#task-33--determine-high-performing-database-solutions)
  - [Task 3.4 — Determine High-Performing and/or Scalable Network Architectures](#task-34--determine-high-performing-andor-scalable-network-architectures)
  - [Task 3.5 — Determine High-Performing Data Ingestion and Transformation Solutions](#task-35--determine-high-performing-data-ingestion-and-transformation-solutions)
- [Domain 4 — Design Cost-Optimized Architectures (20%)](#domain-4--design-cost-optimized-architectures-20)
  - [Task 4.1 — Design Cost-Optimized Storage Solutions](#task-41--design-cost-optimized-storage-solutions)
  - [Task 4.2 — Design Cost-Optimized Compute Solutions](#task-42--design-cost-optimized-compute-solutions)
  - [Task 4.3 — Design Cost-Optimized Database Solutions](#task-43--design-cost-optimized-database-solutions)
  - [Task 4.4 — Design Cost-Optimized Network Architectures](#task-44--design-cost-optimized-network-architectures)
- [Appendix A — Service Cheat Sheet by Category](#appendix-a--service-cheat-sheet-by-category)
- [Appendix B — Numbers and Limits to Memorize](#appendix-b--numbers-and-limits-to-memorize)
- [Appendix C — Keyword to Service Decoder](#appendix-c--keyword-to-service-decoder)
- [Appendix D — Top 25 Distractors and Traps](#appendix-d--top-25-distractors-and-traps)
- [Final Study Flow](#final-study-flow)

---


# Domain 1 — Design Secure Architectures (30%)


## Task 1.1 — Design Secure Access to AWS Resources

> **Weight:** Domain 1 is 30% of the exam and Task 1.1 is the most heavily tested single task in SAA-C03. Expect 8–12 questions touching IAM, roles, multi-account governance, and federation.
>
> **The one principle that answers most questions:** *identities should receive temporary, least-privilege credentials through roles, and permissions should be layered so that the narrowest boundary wins.*

---

## 1. The AWS Shared Responsibility Model

### 1.1 What the model actually says

AWS splits accountability at the line where the virtualization layer meets the customer's workload.

- **AWS is responsible for "security OF the cloud."** This is everything AWS operates: the physical data centers (badge access, guards, biometric locks), power and cooling, the server hardware, the storage media and its secure decommissioning, the networking fabric between racks and between AZs, the hypervisor, and the software that runs AWS's own managed services.
- **The customer is responsible for "security IN the cloud."** This is everything the customer configures and puts into the service: the data itself, who is allowed to touch it, how it is encrypted, the guest operating system on an EC2 instance, firewall rules, application code, and identity management.

The exam phrases this as a question about a specific service and asks which party handles a specific duty. The trick is that the dividing line **moves depending on the service model**.

### 1.2 How the line shifts by service model

**Infrastructure as a Service (EC2, EBS, VPC)** — this is the maximum customer responsibility. AWS gives you a virtual machine and a network; everything from the operating system upward is yours:
- You patch the guest OS and kernel.
- You install and patch application software and runtime libraries.
- You configure security groups, NACLs, and route tables.
- You manage SSH keys, local user accounts, host-based firewalls, and antivirus.
- You decide on and implement encryption for EBS volumes and data in transit.

**Platform / managed services (RDS, ElastiCache, Elastic Beanstalk, EMR)** — AWS takes over the operating system and the engine software:
- AWS patches the underlying OS and the database engine (during your chosen maintenance window).
- AWS handles automated backups, failover orchestration, and hardware replacement.
- **You still own**: database user accounts and grants, security group rules controlling who can reach port 3306, parameter group settings, whether encryption is enabled, and all the data.

Elastic Beanstalk is an interesting middle case: AWS manages the platform, but because the application runs on EC2 instances *in your account*, you remain responsible for the application code and for applying platform updates when AWS publishes them.

**Abstracted / serverless services (S3, DynamoDB, Lambda, SQS)** — AWS operates essentially the whole stack:
- AWS runs the servers, patches everything, and manages availability and durability.
- **You still own**: data classification, IAM and resource policies, encryption choices (SSE-S3 vs SSE-KMS vs client-side), versioning and lifecycle settings, Block Public Access, and in Lambda's case your function code and its dependencies.

### 1.3 Responsibilities that are *always* the customer's

No matter which service you use, these never transfer to AWS:
1. **Your data** — its content, its classification, and its retention.
2. **Identity and access management** — who has credentials and what those credentials may do.
3. **Account-level configuration** — MFA on root, password policy, enabled Regions.
4. **Deciding whether to encrypt** and managing key policies (even when AWS supplies the key material).

### 1.4 Shared controls

Some controls are shared, meaning both parties do a version of the same thing at different layers:
- **Patch management** — AWS patches the infrastructure and managed service software; you patch guest OS and applications.
- **Configuration management** — AWS configures its infrastructure devices; you configure your OS, databases, and applications.
- **Awareness and training** — AWS trains AWS employees; you train yours.

### 1.5 Exam patterns

| Question | Answer |
|---|---|
| Who patches the OS of an RDS instance? | **AWS** |
| Who patches the OS of an EC2 instance running MySQL? | **Customer** |
| Who is responsible for the security group rules on an RDS instance? | **Customer** |
| Who physically destroys failed disks? | **AWS** |
| Who configures S3 bucket policies? | **Customer** |
| Who manages the hypervisor? | **AWS** |
| Who encrypts data in transit to an application? | **Customer** (AWS supplies the tooling: ACM, TLS endpoints) |
| Who is responsible for availability of a single-AZ workload? | **Customer** — AWS provides multiple AZs; using them is your design choice |

---

## 2. AWS Global Infrastructure (from a security and access angle)

### 2.1 Regions

A **Region** is a separate geographic area containing multiple isolated data center clusters — for example `ap-south-1` (Mumbai), `us-east-1` (N. Virginia), `eu-west-1` (Ireland).

Key properties that matter for secure design:
- **Regions are isolated from each other by default.** Data you put in a Region stays in that Region unless you take an explicit action to move it (enabling cross-Region replication, copying a snapshot, creating a cross-Region read replica, using a global service). This is the foundation of **data residency** compliance: if regulation says data must remain in India, you place resources in `ap-south-1` and use an SCP to deny other Regions.
- **Some Regions are opt-in** (newer Regions like Hong Kong, Bahrain, Milan). They must be explicitly enabled in account settings, and credentials from STS global endpoints may not work there unless you use the Regional endpoint or enable global STS tokens for all Regions.
- **Region selection criteria**: compliance/data residency first, then latency to users, then service availability (not every service exists in every Region), then price (prices differ per Region).

### 2.2 Availability Zones

An **Availability Zone** is one or more discrete data centers within a Region, each with redundant power, networking, and connectivity, housed in separate facilities.

- AZs are **physically separated** — typically tens of kilometres apart — so that a fire, flood, or power event affects only one.
- They are connected by **dedicated, redundant, low-latency metro fibre**, giving single-digit-millisecond (usually < 1–2 ms) round-trip latency. That is fast enough for **synchronous replication**, which is exactly how RDS Multi-AZ and Aurora work.
- **AZ names are randomized per account.** Your `us-east-1a` is probably not the same physical AZ as another account's `us-east-1a`. AWS does this to balance load across AZs. When you must correlate AZs between accounts (for example when sharing subnets via RAM, or minimizing cross-AZ traffic in a multi-account architecture), use the **AZ ID** (`use1-az1`), which *is* consistent across accounts.
- Most Regions have 3 or more AZs; a few have 6.

### 2.3 Other infrastructure elements

- **Local Zones** — an extension of a Region placed in a large metro area, giving single-digit-millisecond latency for things like media production, gaming, and remote workstations. You extend a VPC into a Local Zone with a subnet.
- **Wavelength Zones** — AWS infrastructure embedded inside telecom providers' 5G networks for ultra-low-latency mobile applications.
- **AWS Outposts** — physical AWS racks installed in your own data center, running a subset of AWS services locally. Used for strict data residency or when an application must sit next to on-prem systems.
- **Edge locations and Regional edge caches** — hundreds of points of presence worldwide used by CloudFront, Route 53, AWS Shield, AWS WAF, Global Accelerator, and S3 Transfer Acceleration. **DDoS absorption happens here**, far from your origin.

### 2.4 Global vs Regional services

This distinction appears in security questions constantly.

**Global (one namespace, no Region selector):**
IAM, AWS Organizations, Route 53, CloudFront, AWS WAF when attached to CloudFront, AWS Shield, Billing, Trusted Advisor, and the S3 *namespace* (bucket names are globally unique, though each bucket's data lives in one Region).

**Regional (resources exist independently in each Region):**
EC2, VPC, EBS, RDS, Lambda, DynamoDB, SQS, SNS, CloudWatch, CloudTrail trails (unless you make them multi-Region), **KMS keys**, **ACM certificates**, Secrets Manager secrets, and Service Quotas.

Two consequences you will be tested on:
1. **A KMS key cannot be used in another Region.** To decrypt a cross-Region replicated object, the destination Region needs its own key, or you use a **multi-Region key**.
2. **An ACM certificate for CloudFront must be requested in `us-east-1`**, because CloudFront is a global service whose control plane lives there. For an ALB, the certificate must exist in the ALB's own Region.

---

## 3. IAM — Identities and Principals

### 3.1 Authentication vs authorization

IAM performs two distinct jobs, and the exam often tests whether you can tell them apart:
- **Authentication** — proving who you are. For a human: username + password (+ MFA). For code: an access key ID and secret, or a signed request using temporary credentials.
- **Authorization** — deciding whether the authenticated principal may perform the requested action on the requested resource. This is the policy evaluation engine.

Every API request to AWS is signed (Signature Version 4) and carries an identity. IAM evaluates the request against all applicable policies and returns allow or deny.

### 3.2 Anatomy of an ARN

Amazon Resource Names identify resources in policies. You should be able to read one:

```
arn:aws:s3:::my-bucket/reports/2026/q1.csv
arn:aws:iam::111122223333:role/AppServerRole
arn:aws:ec2:ap-south-1:111122223333:instance/i-0abc123
arn:aws:kms:ap-south-1:111122223333:key/1234abcd-...
```

Format: `arn:partition:service:region:account-id:resource`

- **partition** — `aws` (standard), `aws-cn` (China), `aws-us-gov` (GovCloud).
- **region / account-id are empty for S3 and IAM**: S3 bucket names are global, and IAM is a global service (though IAM ARNs do carry the account ID).
- Wildcards are allowed: `arn:aws:s3:::my-bucket/*` means every object in the bucket. Note that `arn:aws:s3:::my-bucket` (no `/*`) refers to the **bucket itself** — needed for `s3:ListBucket` — while `arn:aws:s3:::my-bucket/*` refers to the **objects** — needed for `s3:GetObject`. Mixing these up is a classic cause of "access denied" and a favourite distractor.

### 3.3 The root user

The root user is created when the account is created and is identified by the account's email address. It has **complete, unrestricted access** to everything in the account and **cannot be limited by IAM policies**. The only thing that can constrain it is a Service Control Policy from an AWS Organization — and even then, certain actions cannot be blocked.

**Mandatory best practices:**
1. **Enable MFA on root.** For high-value accounts use a hardware MFA device rather than a phone app, and store it in a safe. AWS now also supports multiple MFA devices per root user (up to 8), which removes the single-device risk.
2. **Do not create root access keys.** If any exist, delete them. There is essentially no legitimate reason for programmatic root access.
3. **Use a role-based email alias** (e.g., `aws-root-prod@company.com`) that goes to a distribution list, not an individual's mailbox, so the account isn't lost when someone leaves.
4. **Create an administrative identity for daily work** — an IAM Identity Center user with an AdministratorAccess permission set, or an IAM user/role with the `AdministratorAccess` policy — and lock the root credentials away.
5. **Set a strong password and enable account recovery contacts.**

**Tasks that genuinely require root** (memorize the main ones):
- Changing the account name, root email address, or root password
- Changing or cancelling the AWS Support plan
- **Closing the AWS account**
- Restoring IAM user permissions after an administrator has locked everyone out
- Registering as a seller in the Reserved Instance Marketplace
- **Enabling MFA Delete on an S3 bucket** (and the root user must generate the request)
- Editing or deleting an S3 bucket policy that includes an invalid VPC ID or explicit deny that locks everyone out
- Requesting removal of the PTR record for EC2 reverse DNS (email deliverability)
- Signing up for GovCloud and some billing-related changes

### 3.4 IAM users

An IAM user is a **long-term identity** with permanent credentials. A user can have:
- A **console password** (optional), governed by the account password policy
- Up to **two access keys** (access key ID + secret access key) — two so you can rotate without downtime: create the second, deploy it, verify, then delete the first
- MFA devices
- SSH keys for CodeCommit and certificates for some services

**When are IAM users still appropriate?**
Increasingly rarely. The modern guidance is:
- Humans → **IAM Identity Center** (federated, temporary credentials)
- Applications on AWS → **IAM roles** attached to the compute
- Applications outside AWS → **IAM Roles Anywhere** (X.509 certificate-based) or IAM Identity Center
- IAM users remain acceptable for legacy systems that cannot federate, for service accounts in simple accounts, and for emergency "break-glass" access

**Credential hygiene tooling:**
- **IAM credential report** — a downloadable CSV listing every user in the account with password age, MFA status, access key age and last-used date. This is the answer whenever a question asks for a single report on user credential state.
- **Access Advisor / service last accessed data** — shows which services an identity (user, group, role, or even an OU) has actually called and when. Use it to strip unused permissions and move toward least privilege.
- **IAM Access Analyzer** — three capabilities worth knowing:
  - *External access findings*: identifies resources (S3 buckets, KMS keys, IAM roles, Lambda functions, SQS queues, Secrets Manager secrets, EFS file systems, ECR repositories, RDS snapshots) that can be accessed by a principal outside your account/organization. Uses automated reasoning, not log analysis, so it finds theoretical access even if nobody has used it.
  - *Policy validation*: checks policies against grammar and best practices.
  - *Policy generation*: reads CloudTrail history and generates a least-privilege policy based on what was actually used.

### 3.5 IAM groups

A group is a container for users that lets you attach policies once and apply them to many users. Important constraints:
- **Groups cannot be nested** (no group inside a group).
- **A group is not a principal.** You cannot put a group ARN in the `Principal` element of a resource-based policy, and a group cannot assume a role.
- Users can belong to multiple groups (up to 10 by default); their effective permissions are the union of all attached policies.

### 3.6 IAM roles — the centrepiece

A role is an identity with a permissions policy but **no long-term credentials**. Instead, a trusted entity *assumes* the role and receives **temporary security credentials** from STS.

Every role has two policies:
1. **Trust policy (assume role policy)** — a resource-based policy on the role that answers *"who is allowed to assume me?"* Its `Principal` can be an AWS account, an IAM user or role, an AWS service (`ec2.amazonaws.com`, `lambda.amazonaws.com`), a SAML provider, or an OIDC provider.
2. **Permissions policy** — one or more identity-based policies answering *"what can the assumed session do?"*

**Common role types:**

| Role type | Trusted principal | Example |
|---|---|---|
| **EC2 instance role** (via instance profile) | `ec2.amazonaws.com` | Application on EC2 reads from S3 |
| **Lambda execution role** | `lambda.amazonaws.com` | Function writes to DynamoDB and CloudWatch Logs |
| **ECS task role** | `ecs-tasks.amazonaws.com` | Per-task least privilege (preferred over instance role) |
| **ECS task execution role** | `ecs-tasks.amazonaws.com` | Pulls images from ECR, writes logs — infrastructure-level, not app-level |
| **Cross-account role** | Another account's ID or role ARN | Auditor in the security account reads logs in prod |
| **Service role** | The service principal | CodeDeploy, CloudFormation, Config acting on your behalf |
| **Service-linked role** | Predefined and locked | Auto Scaling, Elastic Beanstalk; cannot be edited and cannot be deleted while in use |
| **Federated role** | SAML or OIDC provider ARN | ADFS or Okta users, EKS pods (IRSA), GitHub Actions |

**Instance profiles:** an EC2 instance cannot be given a role directly — it is given an *instance profile*, which is a container holding exactly one role. The console creates this automatically; CLI/CloudFormation users must create it explicitly. This is a detail that appears in troubleshooting-flavoured questions.

**How an EC2 instance actually gets credentials:** the AWS SDK on the instance queries the **Instance Metadata Service** at `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>`, which returns temporary credentials that AWS rotates automatically well before expiry. The application never stores a secret.

**IMDSv1 vs IMDSv2:** IMDSv1 is a simple request/response, which means a **Server-Side Request Forgery (SSRF)** vulnerability in your web application can be abused to read instance credentials. **IMDSv2 is session-oriented**: the caller must first `PUT` to obtain a token, then supply that token on subsequent requests, and the response hop limit defaults to 1 so containers and proxies can't accidentally relay it. **Enforcing IMDSv2 is the standard exam answer to "an SSRF flaw leaked our instance credentials."**

### 3.7 The credential provider chain

When an SDK or the CLI runs, it looks for credentials in this order (simplified, and worth knowing because it explains "why is my app still using the old keys?"):
1. Command-line options / explicit parameters in code
2. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`)
3. Shared credentials file (`~/.aws/credentials`)
4. Shared config file (`~/.aws/config`), including assumed-role profiles
5. Container credentials (ECS task role endpoint)
6. **Instance profile credentials from IMDS**

So if an instance has a role but someone also left static keys in `~/.aws/credentials`, the static keys win — a frequent real-world and exam gotcha.

---

## 4. Policies and the Authorization Model

### 4.1 The six policy types

| Type | Attached to | Grants? | Key purpose |
|---|---|---|---|
| **Identity-based policy** | IAM user, group, or role | Yes | What this identity may do |
| **Resource-based policy** | The resource itself | Yes | Who may access this resource; **has a `Principal` element** |
| **Permissions boundary** | A user or role | **No** | Hard ceiling on the identity's maximum permissions |
| **Service Control Policy (SCP)** | Org root, OU, or account | **No** | Hard ceiling on everything in the member account |
| **Session policy** | Passed inline during `AssumeRole` | **No** (narrows) | Further restricts a specific session |
| **Access control list (ACL)** | S3 objects/buckets (legacy) | Yes | Legacy cross-account object grants |

Identity-based policies come in three flavours: **AWS managed** (maintained by AWS, e.g., `ReadOnlyAccess`, `AmazonS3FullAccess`), **customer managed** (your reusable policies — the recommended default), and **inline** (embedded in a single identity, deleted with it; use only when a strict 1:1 relationship is required).

### 4.2 Policy JSON element by element

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTeamPrefixReadWithMFAFromOffice",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/AnalystRole" },
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::reports-bucket/team-a/*",
      "Condition": {
        "Bool": { "aws:MultiFactorAuthPresent": "true" },
        "IpAddress": { "aws:SourceIp": ["203.0.113.0/24"] },
        "StringEquals": { "aws:PrincipalOrgID": "o-abc1234567" }
      }
    }
  ]
}
```

- **`Version`** — always `"2012-10-17"`. The older `2008-10-17` does not support policy variables. This is a real exam detail.
- **`Sid`** — optional statement identifier, useful for readability and for targeting a statement.
- **`Effect`** — `Allow` or `Deny`.
- **`Principal`** — **only valid in resource-based policies and role trust policies.** Can be `"AWS"`, `"Service"`, `"Federated"`, or `"*"`. Putting `Principal` in an identity-based policy is invalid.
- **`Action` / `NotAction`** — service-prefixed actions (`s3:GetObject`, `ec2:RunInstances`), wildcards allowed (`s3:Get*`). `NotAction` means "everything except these," which is powerful and dangerous.
- **`Resource` / `NotResource`** — ARNs the statement applies to.
- **`Condition`** — optional constraints; **all conditions in a block must be true (AND)**, while multiple values for the same key are **OR**.

**Policy variables** let one policy serve many users:
```json
"Resource": "arn:aws:s3:::user-data/${aws:username}/*"
```
Other variables: `${aws:userid}`, `${aws:PrincipalTag/Department}`, `${cognito-identity.amazonaws.com:sub}` (used to scope S3 prefixes per mobile user).

### 4.3 Condition operators and keys

**Operators you should recognize:**
`StringEquals`, `StringNotEquals`, `StringLike` (wildcards), `ArnEquals`, `ArnLike`, `Bool`, `NumericLessThan`, `DateGreaterThan`, `IpAddress`, `NotIpAddress`, `Null` (tests whether a key exists), and the set operators `ForAllValues:` / `ForAnyValue:` for multi-valued keys. Appending **`IfExists`** (e.g., `StringEqualsIfExists`) makes the condition pass when the key is absent — useful for services that don't always send the key.

**High-value global condition keys:**

| Key | Meaning / use |
|---|---|
| `aws:PrincipalOrgID` | Caller belongs to your AWS Organization — far cleaner than listing account IDs |
| `aws:PrincipalOrgPaths` | Caller is in a specific OU path |
| `aws:PrincipalArn` / `aws:PrincipalAccount` | Exact caller identity |
| `aws:PrincipalTag/<key>` | Tag on the calling identity — the basis of ABAC |
| `aws:ResourceTag/<key>` | Tag on the target resource |
| `aws:RequestTag/<key>` | Tag being applied in this request (enforce tagging at creation) |
| `aws:TagKeys` | Which tag keys are present in the request |
| `aws:MultiFactorAuthPresent` / `aws:MultiFactorAuthAge` | Force MFA, or require recent MFA |
| `aws:SourceIp` | Caller's public IP — **does not work through a VPC endpoint** |
| `aws:SourceVpc` / `aws:SourceVpce` | Restrict access to a VPC or specific endpoint — the correct replacement for SourceIp in private architectures |
| `aws:SecureTransport` | Whether TLS was used — deny when `false` |
| `aws:RequestedRegion` | Which Region the request targets — the standard Region-restriction SCP |
| `aws:CurrentTime` / `aws:EpochTime` | Time-bounded access |
| `aws:ViaAWSService` | Whether another AWS service is making the call on your behalf |
| `sts:ExternalId` | Third-party cross-account protection |
| `iam:PermissionsBoundary` | Require that created roles carry a specific boundary |

**Service-specific examples:** `s3:x-amz-server-side-encryption` (force SSE on upload), `s3:x-amz-server-side-encryption-aws-kms-key-id` (force a *specific* key), `s3:prefix` (restrict listing to a folder), `ec2:InstanceType` (restrict instance sizes), `kms:ViaService` (key usable only through a named service), `dynamodb:LeadingKeys` (row-level access per user).

### 4.4 Policy evaluation logic — the complete flow

This is the single most important mechanic in Domain 1. For every request, IAM evaluates in this order:

1. **Collect all applicable policies**: SCPs, resource-based policies, identity-based policies, permissions boundaries, session policies.
2. **Explicit Deny check.** If *any* applicable policy contains a matching `Deny`, the request is **denied immediately**. Nothing can override an explicit deny.
3. **SCP check** (only for accounts inside an Organization). If an SCP does not allow the action, it is denied — regardless of IAM policy. SCPs do not apply to the management account or to service-linked roles.
4. **Resource-based policy check.** If a resource-based policy explicitly allows the principal, that can be sufficient **within the same account** (and for some services it grants access even without an identity policy).
5. **Identity-based policy check.** Must allow, unless a resource-based policy already granted access in the same account.
6. **Permissions boundary check.** If a boundary is attached, the action must be allowed by both the boundary and the identity policy.
7. **Session policy check.** If the session was created with an inline session policy, the action must also be allowed there.
8. **Default: implicit deny.** If nothing explicitly allows the action, it is denied.

**The mental model:** effective permissions are the **intersection** of every "ceiling" (SCP, boundary, session policy) with the **union** of the grants (identity policy, resource policy) — and any explicit Deny wipes everything out.

#### Same-account vs cross-account

- **Same account:** identity policy **OR** resource policy is enough. If a bucket policy allows your role, you don't strictly need an S3 statement in the role's policy (though most teams add both).
- **Cross-account:** you need **BOTH**. Account A's identity policy must allow the action, **and** Account B's resource policy (or role trust policy) must allow the principal from Account A. This "both sides must agree" rule is tested repeatedly.
- **Exception worth knowing:** KMS key policies are authoritative — the key policy must grant access, and it can delegate to IAM in the same account using the `"AWS": "arn:aws:iam::<acct>:root"` principal with `kms:*`. Without that delegation statement, IAM policies alone cannot grant key use.

### 4.5 Permissions boundaries in practice

A boundary doesn't grant anything; it caps what an identity can ever be granted. The classic use case is **delegated administration**: you want developers to create roles for their own applications without being able to create an admin role.

Implementation pattern:
1. Create a customer managed policy, e.g., `DeveloperBoundary`, allowing only S3, DynamoDB, Lambda, and CloudWatch.
2. Grant developers `iam:CreateRole` and `iam:AttachRolePolicy` **with a condition** requiring `iam:PermissionsBoundary` to equal the ARN of `DeveloperBoundary`.
3. Deny `iam:DeleteRolePermissionsBoundary` and `iam:PutRolePermissionsBoundary` changes.

Now any role a developer creates is permanently capped by the boundary, even if they attach `AdministratorAccess` to it.

### 4.6 RBAC vs ABAC

**Role-based access control (RBAC)** defines a policy per job function: `DataEngineerPolicy`, `QAPolicy`, `BillingReadOnly`. It is simple and explicit, but the number of policies grows with every new team, project, or environment, and each new project means editing or creating policies.

**Attribute-based access control (ABAC)** makes the decision by comparing **tags on the principal** with **tags on the resource**:

```json
{
  "Effect": "Allow",
  "Action": ["ec2:StartInstances", "ec2:StopInstances"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
    }
  }
}
```

One policy now covers every current and future project: tag the user/role with `Project=Atlas` and tag the resources `Project=Atlas`, and access matches automatically. Pair it with a condition on `aws:RequestTag/Project` so new resources must be tagged correctly at creation.

**Exam trigger:** any question saying *"new teams/projects are added frequently and we want to minimize the number of policies / policy maintenance overhead"* is pointing at **ABAC**.

---

## 5. AWS STS, Role Switching and Cross-Account Access

### 5.1 What STS returns

AWS Security Token Service issues **temporary credentials** consisting of three parts: an access key ID, a secret access key, and a **session token** (the presence of the session token is what distinguishes temporary from long-term credentials). They expire automatically, which is why they are inherently safer than IAM user keys.

Duration rules:
- Default session: **1 hour**.
- Maximum: set by the role's **maximum session duration** setting, which can be 1–12 hours. The caller can request up to that maximum with `DurationSeconds`.
- **Role chaining** (using one assumed role to assume another) is **capped at 1 hour** and cannot be extended.
- `GetSessionToken` for IAM users: 15 minutes to 36 hours (default 12); for root, maximum 1 hour.

### 5.2 The STS API surface

| API | Used for |
|---|---|
| `AssumeRole` | Cross-account access and same-account role switching by IAM principals |
| `AssumeRoleWithSAML` | Enterprise federation from AD FS / any SAML 2.0 IdP |
| `AssumeRoleWithWebIdentity` | OIDC federation — Cognito identity pools, Google/Facebook/Apple, **EKS IRSA**, GitHub Actions OIDC |
| `GetSessionToken` | Temporary credentials for an IAM user, typically to satisfy an MFA condition |
| `GetFederationToken` | Temporary credentials for a federated user from a proxy application |
| `GetCallerIdentity` | "Who am I?" — no permissions required, great for troubleshooting |

### 5.3 Setting up cross-account access (the canonical pattern)

Scenario: developers in the **Dev account (111111111111)** need read access to an S3 bucket in the **Prod account (222222222222)**.

**Step 1 — In Prod, create the role with a trust policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::111111111111:root" },
    "Action": "sts:AssumeRole",
    "Condition": { "Bool": { "aws:MultiFactorAuthPresent": "true" } }
  }]
}
```
Using `:root` here means "any principal in account 111111111111 that is *also* granted sts:AssumeRole by its own IAM policy" — it delegates the decision to the Dev account's administrators. To be stricter, name a specific role ARN instead.

**Step 2 — In Prod, attach a least-privilege permissions policy** to the role (e.g., `s3:GetObject` and `s3:ListBucket` on one bucket).

**Step 3 — In Dev, allow the developers to assume it:**
```json
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::222222222222:role/ProdReadOnly"
}
```

**Step 4 — Use it.** In the console, "Switch Role." In the CLI, define a profile with `role_arn` and `source_profile`, and the CLI calls `AssumeRole` transparently.

> Whenever a question describes sharing credentials, copying access keys between accounts, or creating duplicate IAM users in each account, the correct answer is almost always **"create a cross-account IAM role and assume it."**

### 5.4 External ID and the confused deputy problem

When a **third-party SaaS vendor** (monitoring, cost analytics, backup) needs access to your account, a naive cross-account role creates a risk: the vendor's system holds many customers' role ARNs, and an attacker who learns your role ARN could trick the vendor into assuming *your* role while acting for *their* account. This is the **confused deputy** problem.

The fix is `sts:ExternalId`: the vendor generates a unique secret per customer, you place it in the trust policy as a condition, and the vendor must pass it on every `AssumeRole` call.

```json
"Condition": { "StringEquals": { "sts:ExternalId": "a7f3c9e1-unique-per-customer" } }
```

**Exam cue:** "third-party", "vendor", "partner needs access to your account" → **cross-account role with ExternalId**.

### 5.5 `iam:PassRole` and privilege escalation

When you launch an EC2 instance with an instance profile, or create a Lambda function with an execution role, you are "passing" a role to a service. That requires the `iam:PassRole` permission. If a user has broad `iam:PassRole` on `*` plus `ec2:RunInstances`, they can launch an instance with an administrator role attached and effectively become an administrator. **Always scope PassRole** to specific role ARNs and add a `iam:PassedToService` condition.

### 5.6 IAM Roles Anywhere

For servers and workloads **outside AWS** that need AWS credentials without IAM user keys, IAM Roles Anywhere lets you use X.509 certificates from your own certificate authority (registered as a trust anchor) to obtain temporary credentials. This is the modern answer to "our on-premises application needs to call AWS APIs securely without long-lived keys."

---

## 6. Federation and Identity Services

### 6.1 Why federate

If your organization already maintains identities in Active Directory, Okta, Entra ID (Azure AD), or another IdP, recreating those users in IAM means duplicated accounts, duplicated offboarding, and inconsistent MFA. Federation lets the IdP remain the single source of truth while AWS issues short-lived credentials mapped to roles.

### 6.2 AWS IAM Identity Center (successor to AWS SSO)

This is the recommended way to manage **workforce** access in 2024+ and the expected answer on most multi-account human-access questions.

**Architecture:**
- Enabled in the **management account** of an AWS Organization (administration can be delegated to a member account).
- **Identity source** — choose one:
  - *Identity Center directory* (built in; good for small organizations with no existing IdP)
  - *Active Directory* — via **AWS Managed Microsoft AD** or **AD Connector** to on-premises AD
  - *External identity provider* — any SAML 2.0 IdP (Okta, Entra ID, Ping, OneLogin), typically with **SCIM** for automatic user/group provisioning and deprovisioning
- **Permission sets** — reusable bundles of policies (AWS managed, customer managed, inline, plus an optional permissions boundary). When you assign a permission set to a group for an account, Identity Center **provisions an IAM role into that account** automatically and keeps it in sync.
- **Assignments** — map (group) × (permission set) × (account). One assignment can cover an entire OU's worth of accounts.
- **Access portal** — a single URL where users sign in once and see every account and role they can use, plus SAML-integrated business applications. Users can also get short-lived CLI credentials (`aws sso login`) or use IAM Identity Center support in the SDKs.

**Why it wins exam questions:** no IAM users to create, no credentials to rotate, centralized assignment across hundreds of accounts, uses the existing corporate directory, and access is removed instantly when the user is disabled in the IdP.

### 6.3 Classic SAML 2.0 federation with IAM (pre-Identity Center)

Still examinable and still used where Identity Center isn't deployed:

1. Create a **SAML identity provider** object in IAM, uploading the IdP's metadata XML.
2. Create IAM roles whose trust policy trusts that provider with `sts:AssumeRoleWithSAML` and a condition on `SAML:aud`.
3. The IdP's SAML assertion includes attributes (`https://aws.amazon.com/SAML/Attributes/Role`) listing the role ARN and provider ARN.
4. The user hits the IdP, authenticates, is redirected to the AWS sign-in endpoint with the assertion, and STS returns temporary credentials for the chosen role.

The main drawback versus Identity Center: you must create and maintain the provider object and roles in **every account**.

### 6.4 AWS Directory Service options

| Option | What it is | Use when |
|---|---|---|
| **AWS Managed Microsoft AD** | A real Microsoft AD (Standard or Enterprise) running in your VPC, managed by AWS | You need full AD features in AWS, want to support AD-aware workloads (FSx for Windows, RDS for SQL Server, EC2 domain join), and/or want a **trust relationship** with on-prem AD |
| **AD Connector** | A proxy that forwards authentication requests to your on-premises AD | You want AWS services to use on-prem AD **without storing any directory data in AWS** |
| **Simple AD** | Samba-based, lightweight, Linux-friendly | Small, simple directory needs; **no trusts, no MFA, limited features** |

### 6.5 Amazon Cognito — customer/app identities

Cognito is for **application end users**, not employees. Two distinct components:
- **User pool** — a user directory providing sign-up, sign-in, password policies, MFA, email/phone verification, a hosted UI, and federation with social IdPs (Google, Facebook, Apple) and enterprise IdPs (SAML/OIDC). It returns **JWTs** (ID token, access token, refresh token). ALB and API Gateway can validate these tokens natively.
- **Identity pool (federated identities)** — exchanges a token (from a user pool or a social IdP) for **temporary AWS credentials** via STS, mapped to an IAM role. Supports authenticated and unauthenticated (guest) roles, and role selection based on token claims.

Classic pattern: a mobile app authenticates against a user pool, passes the token to an identity pool, and receives credentials scoped by a policy using `${cognito-identity.amazonaws.com:sub}` so each user can only read/write their own S3 prefix or DynamoDB rows.

> **Remember the split: workforce → IAM Identity Center; customers/app users → Cognito; servers/services → IAM roles.**

### 6.6 OIDC federation for workloads

- **EKS IRSA (IAM Roles for Service Accounts)** — the cluster's OIDC provider is registered in IAM so individual Kubernetes service accounts map to IAM roles, giving pod-level least privilege.
- **GitHub Actions / GitLab CI** — register the provider's OIDC endpoint and let pipelines assume a role with no stored AWS keys. This is the modern answer for "our CI/CD stores AWS access keys as secrets — how do we fix it?"

---

## 7. Multi-Account Strategy

### 7.1 Why multiple accounts

An AWS account is the strongest isolation boundary available. Reasons to use many:
- **Blast radius containment** — a compromise or runaway process in dev cannot touch prod.
- **Security/compliance scoping** — keep PCI or HIPAA workloads in dedicated accounts so audits are narrower.
- **Billing separation** — per-team or per-product cost attribution without relying solely on tags.
- **Service quota isolation** — quotas are per account per Region, so one team can't exhaust another's limits.
- **Simpler IAM** — permissions in a small single-purpose account are far easier to keep least privilege.

Typical structure: Management (payer) account; Security OU with Log Archive and Audit/Security Tooling accounts; Infrastructure OU with Network and Shared Services accounts; Workloads OU split into Prod and Non-Prod; a Sandbox OU with tight SCPs and budgets; a Suspended OU with a deny-all SCP for decommissioned accounts.

### 7.2 AWS Organizations

- **Management (payer) account** sits at the root; it creates/invites **member accounts** and owns consolidated billing.
- **Organizational Units (OUs)** group accounts into a hierarchy (nesting up to 5 levels deep). Policies attached to an OU are inherited by all accounts beneath it.
- **Feature sets:** *Consolidated billing only* (just billing) or **All features** (required for SCPs and most governance features).
- **Policy types** you can enable: **Service control policies**, **tag policies** (enforce tag key casing/allowed values), **backup policies** (org-wide AWS Backup plans), **AI services opt-out policies**, and **chat applications policies**.
- **Delegated administrator** — you can nominate a member account to administer a service org-wide (GuardDuty, Security Hub, Config, Macie, IAM Access Analyzer, Backup), so the management account isn't used for daily operations.
- **Consolidated billing benefits:** one bill; **volume pricing tiers aggregate across accounts** (so combined S3 usage reaches cheaper tiers sooner); **unused RIs and Savings Plans are shared** across accounts by default (can be disabled per account).

### 7.3 Service Control Policies in depth

**What they are:** filters that define the **maximum available permissions** for principals in member accounts. They never grant anything — a principal still needs an IAM allow.

**Where they apply:** root, OU, or individual account, and they are **inherited down the tree**. The effective SCP for an account is the intersection of every SCP along its path from the root.

**What they do NOT affect:**
- The **management account** (even if you attach an SCP to it — this is why you should run no workloads there)
- **Service-linked roles**
- Anything outside the Organization

**Two strategies:**
- **Deny list (most common):** leave the default `FullAWSAccess` policy attached and add policies containing only `Deny` statements. Easy to operate; new services are automatically allowed.
- **Allow list:** detach `FullAWSAccess` and explicitly allow only approved services. Very tight, but high maintenance — every new service needs a policy change.

**SCPs you should recognize:**

Restrict Regions (allowing global services to still function):
```json
{
  "Effect": "Deny",
  "NotAction": ["iam:*", "organizations:*", "route53:*", "cloudfront:*",
                "support:*", "budgets:*", "waf:*"],
  "Resource": "*",
  "Condition": {
    "StringNotEquals": { "aws:RequestedRegion": ["ap-south-1", "us-east-1"] }
  }
}
```

Other common guardrails: deny `organizations:LeaveOrganization`; deny disabling CloudTrail, GuardDuty, Config, or Security Hub; deny deletion of specific log buckets; deny root user actions (`"Condition": {"StringLike": {"aws:PrincipalArn": "arn:aws:iam::*:root"}}`); deny creating IAM users (forcing Identity Center); deny disabling default EBS encryption; require a permissions boundary on new roles; deny expensive instance families in sandbox OUs.

### 7.4 AWS Control Tower

Control Tower builds and governs a **landing zone** — a pre-configured, well-architected multi-account environment — with far less effort than assembling Organizations + CloudTrail + Config + SCPs by hand.

**What it sets up:**
- An organization with a **Security OU** containing a **Log Archive account** (centralized CloudTrail and Config logs, usually with restrictive policies) and an **Audit/Security account** (cross-account read access and notifications), plus a **Sandbox OU**.
- Org-wide **CloudTrail** and **AWS Config** with centralized S3 delivery.
- **Account Factory** — a Service Catalog product for provisioning new accounts with pre-set baselines, network configuration, and IAM Identity Center access.
- **IAM Identity Center** configured with default permission sets.
- A **dashboard** for compliance status across accounts.

**Controls (formerly guardrails)** come in three enforcement types:
- **Preventive** — implemented as **SCPs**; stop the action from happening at all (e.g., "disallow deletion of log archive").
- **Detective** — implemented as **AWS Config rules**; report non-compliance after the fact (e.g., "detect public read access on S3 buckets").
- **Proactive** — implemented as **CloudFormation hooks**; block non-compliant resources before they are provisioned.

They are also graded as **Mandatory**, **Strongly recommended**, and **Elective**.

**Exam cue:** "set up a secure, compliant, multi-account environment quickly with minimal operational effort / best practices built in" → **Control Tower**. If the question is only about restricting permissions in an existing org → **SCPs**. If it's about sharing resources → **RAM**.

### 7.5 AWS Resource Access Manager (RAM)

RAM shares resources across accounts in an organization without duplicating them or building peering meshes. Commonly shared: **VPC subnets** (VPC sharing — a central network account owns the VPC, workload accounts deploy into its subnets), **Transit Gateways**, **Route 53 Resolver rules**, **License Manager configurations**, **Aurora DB clusters**, and **Image Builder components**.

### 7.6 Organization-wide security services

- **Organization CloudTrail trail** — created in the management account, automatically applies to all member accounts (current and future), delivering to one S3 bucket in the Log Archive account. Enable **log file validation**, SSE-KMS encryption, and **S3 Object Lock** on the bucket so logs are tamper-evident and immutable.
- **AWS Config aggregator** — multi-account, multi-Region view of configuration and compliance.
- **Security Hub** with a delegated administrator — single pane of findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, plus CIS/PCI/AWS FSBP standards.
- **GuardDuty / Macie / Inspector** all support delegated administration and auto-enrollment of new accounts.

---

## 8. Resource-Based Policies — When and Why

Resource-based policies live on the resource and contain a `Principal`. They are the mechanism for cross-account access and for letting AWS services invoke things.

| Service | Policy name | Typical use |
|---|---|---|
| **S3** | Bucket policy (and access point policy) | Cross-account access, force TLS, force encryption, restrict to a VPC endpoint, allow CloudFront OAC |
| **KMS** | **Key policy (always present and authoritative)** | Who may use/manage the key; must delegate to IAM explicitly |
| **SQS** | Queue policy | Let S3, SNS, or EventBridge send messages; cross-account consumers |
| **SNS** | Topic policy | Let CloudWatch alarms, S3, or another account publish |
| **Lambda** | Function resource policy | Let API Gateway, S3, EventBridge, or ALB invoke the function |
| **Secrets Manager** | Secret policy | Cross-account secret retrieval |
| **ECR** | Repository policy | Let other accounts pull images |
| **EFS** | File system policy | Enforce encryption in transit, restrict to specific roles |
| **API Gateway** | Resource policy | Restrict by source VPC endpoint, IP, or account |
| **VPC endpoints** | Endpoint policy | Limit which buckets/services can be reached through the endpoint |
| **OpenSearch, Glacier, EventBridge buses, CodeArtifact** | Resource policy | Cross-account and service access |

**Rule of thumb:** use a **resource policy** when the caller is in another account or is an AWS service; use an **identity policy** for your own principals.

---

## 9. Troubleshooting "Access Denied" — a repeatable method

The exam sometimes presents a scenario where access fails despite an apparently correct policy. Work through this list:

1. **Is there an explicit Deny?** Check SCPs, the identity policy, the resource policy, and any permissions boundary.
2. **Is an SCP blocking it?** Especially Region restrictions and service denials.
3. **Cross-account?** Confirm both sides allow it.
4. **Is the ARN right?** Bucket vs object ARN (`bucket` vs `bucket/*`), missing wildcard, wrong Region/account.
5. **Is a condition failing?** MFA not present, request not over TLS, source IP evaluated as the NAT/endpoint address, missing required tag.
6. **Is it KMS?** Access to an encrypted S3 object requires `kms:Decrypt` on the key *and* a key policy that permits the principal. "I can list the bucket but not download the object" is almost always KMS.
7. **Is it a permissions boundary** silently capping the identity?
8. **Is the role's trust policy correct**, and does the caller have `sts:AssumeRole`?
9. **Is `iam:PassRole` missing** when launching a resource with a role?
10. **Which credentials are actually in use?** Run `aws sts get-caller-identity`; the credential provider chain may be picking up stale static keys.

---

## 10. Worked Scenarios

**Scenario 1 — "Our EC2 app stores access keys in a config file."**
Replace with an IAM role attached via instance profile; enforce IMDSv2; delete the keys; add an SCP or Config rule to detect long-lived keys. Secrets Manager is for *application* secrets (database passwords), not for AWS credentials.

**Scenario 2 — "500 employees, 20 accounts, corporate Okta, no duplicate identities."**
IAM Identity Center with Okta as the external SAML identity source and SCIM provisioning; define permission sets (`AdministratorAccess`, `PowerUserAccess`, `ReadOnlyAccess`, plus custom ones) and assign them to Okta groups across OUs.

**Scenario 3 — "A partner SaaS tool needs read access to CloudWatch metrics."**
Cross-account role in your account trusting the vendor's account, with `sts:ExternalId` required and a least-privilege read-only policy. No IAM user, no shared keys.

**Scenario 4 — "Developers must be able to create roles but never grant admin."**
Permissions boundary policy + a condition on `iam:CreateRole` requiring that boundary + deny on modifying/removing boundaries.

**Scenario 5 — "Ensure no account can turn off CloudTrail or operate outside two Regions."**
Two SCPs applied at the organization root: one denying `cloudtrail:StopLogging` and `cloudtrail:DeleteTrail`, one denying all non-global actions when `aws:RequestedRegion` is outside the approved list. Remember the management account is exempt.

**Scenario 6 — "A mobile game needs per-user access to S3 objects."**
Cognito user pool for sign-in (with Google federation), identity pool to issue AWS credentials, and an IAM role whose policy restricts `arn:aws:s3:::game-bucket/${cognito-identity.amazonaws.com:sub}/*`.

**Scenario 7 — "Auditors need read-only access across 40 accounts, no identities per account."**
IAM Identity Center with a `ReadOnlyAccess` (or `SecurityAudit`) permission set assigned to the auditors group across the organization's OUs. An SCP cannot grant this.

---

## 11. Quick Decision Table

| Requirement | Answer |
|---|---|
| App on EC2 needs S3 access | IAM role via instance profile |
| App on EKS pod needs least-privilege AWS access | **IRSA** (OIDC federation) |
| CI/CD pipeline outside AWS | OIDC provider + role (no stored keys) |
| On-prem server needs AWS credentials | **IAM Roles Anywhere** or Identity Center |
| Third-party SaaS vendor access | Cross-account role + **ExternalId** |
| Employees using corporate AD/Okta | **IAM Identity Center** with external IdP |
| Mobile/web customers sign in | **Cognito** user pool + identity pool |
| Restrict all accounts to approved Regions | **SCP** with `aws:RequestedRegion` |
| Cap the maximum permissions of a role | **Permissions boundary** |
| Limit a single temporary session further | **Session policy** |
| Find resources shared outside the org | **IAM Access Analyzer** |
| Find permissions nobody uses | **Access Advisor / last accessed data** |
| One report of all users, MFA, key age | **IAM credential report** |
| Audit who did what and when | **CloudTrail** (org trail into Log Archive account) |
| Build a secure multi-account baseline fast | **AWS Control Tower** |
| Share subnets/TGW across accounts | **AWS RAM** |
| Scale permissions as projects grow | **ABAC with tags** |
| Protect instance credentials from SSRF | **IMDSv2** |
| Prevent accidental privilege escalation via services | Scope **`iam:PassRole`** |

---

## 12. Memory Hooks

- "**Explicit Deny beats everything**; implicit deny is the default; nothing is allowed until something allows it."
- "**SCPs and boundaries limit; policies grant.** Effective = intersection of ceilings ∩ union of grants."
- "**Roles, not keys. Temporary, not permanent.**"
- "**Cross-account means both sides must say yes.**"
- "**Workforce → Identity Center. Customers → Cognito. Compute → roles. Partners → role + ExternalId.**"
- "**Bucket ARN lists, object ARN gets.**"
- "**If you can list but not download, suspect KMS.**"

---

## Task 1.2 — Design Secure Workloads and Applications

> This task is about the **network and application layers**: how you build a VPC that segments traffic, how you keep application secrets out of code, how you defend against attacks coming from outside AWS, and how you connect securely to on-premises networks.

---

## 1. VPC Fundamentals

### 1.1 What a VPC is

A **Virtual Private Cloud** is a logically isolated section of the AWS network, dedicated to your account, in **one Region**. Inside it you define your own IP address range, subnets, route tables, and gateways. A VPC **spans all Availability Zones in its Region**, which is why you can place subnets in different AZs within the same VPC.

Every account comes with a **default VPC** in each Region (`172.31.0.0/16`) with a public subnet per AZ, an internet gateway, and a default security group. Default VPCs are convenient but not appropriate for production — the subnets are all public and the CIDR may clash with on-premises ranges.

### 1.2 CIDR planning

- IPv4 CIDR block size must be between **/16 (65,536 addresses) and /28 (16 addresses)**.
- The CIDR **cannot be changed after creation**, but you can **add up to four secondary CIDR blocks** later (they must not overlap and must follow RFC 1918 rules relative to the primary).
- **Never overlap** with on-premises ranges or with VPCs you may later peer with — VPC peering and Transit Gateway both forbid overlapping CIDRs. This is the single most common long-term networking mistake.
- Recommended practice: allocate from a central plan (RFC 1918 space: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), one non-overlapping block per VPC, with room to grow. **AWS VPC IP Address Manager (IPAM)** automates this allocation and tracking across accounts and Regions.

### 1.3 Subnets

A **subnet** is a CIDR slice of the VPC bound to exactly **one Availability Zone**. Subnets never span AZs.

**AWS reserves five IP addresses in every subnet:**

| Address (in a 10.0.1.0/24) | Purpose |
|---|---|
| 10.0.1.0 | Network address |
| 10.0.1.1 | VPC router |
| 10.0.1.2 | **DNS (Amazon-provided, VPC base + 2)** |
| 10.0.1.3 | Reserved for future use |
| 10.0.1.255 | Network broadcast (not supported, but reserved) |

So a `/24` gives **251 usable addresses**, not 256. A `/28` gives 11. Expect a calculation question.

**Public vs private is a routing property, not a setting.** A subnet is *public* if its route table has a route to an **internet gateway**. There is no checkbox called "public." A subnet with `Auto-assign public IPv4` enabled but no IGW route is still private.

### 1.4 Gateways

- **Internet Gateway (IGW)** — a horizontally scaled, redundant, highly available VPC component that allows communication between the VPC and the internet. One per VPC. It performs 1:1 NAT between the instance's private IP and its public/Elastic IP. For an instance to reach the internet it needs: a public or Elastic IP, a route `0.0.0.0/0 → igw-xxxx`, and permissive SG/NACL rules.
- **NAT Gateway** — a managed service that lets instances in **private** subnets initiate **outbound** connections to the internet (and to other VPC-external services) while preventing the internet from initiating inbound connections.
  - Lives **in a public subnet**, requires an **Elastic IP**, and is an **AZ-scoped resource**.
  - Scales automatically from 5 Gbps to **100 Gbps**.
  - Charged **per hour plus per GB processed** — a well-known cost trap.
  - For high availability, deploy **one NAT gateway per AZ** and point each AZ's private route table at its local NAT gateway. A single NAT gateway is both a single point of failure and a source of cross-AZ data charges.
  - **Security groups cannot be attached** to a NAT gateway; control traffic with NACLs and with the SGs of the instances behind it.
- **NAT Instance (legacy)** — an EC2 instance performing NAT. Cheaper at very low volume and supports port forwarding and acting as a bastion, but **you** manage patching, HA, and scaling, and you must **disable the source/destination check** on the instance.
- **Egress-only Internet Gateway** — the IPv6 equivalent of a NAT gateway: outbound-only. IPv6 addresses are always globally routable, so this is how you prevent inbound IPv6 connections.

### 1.5 Route tables

- Each subnet is associated with exactly one route table (the VPC's **main** route table by default).
- The `local` route covering the VPC CIDR is always present and cannot be removed or overridden — this is what makes all subnets in a VPC able to talk to each other by default.
- **Longest-prefix match wins**: a route for `10.0.5.0/24` beats `0.0.0.0/0`.
- Targets can be: IGW, NAT gateway, egress-only IGW, virtual private gateway, transit gateway, peering connection, network interface, gateway endpoint (via prefix list), or local.
- Best practice: a separate route table per subnet tier per AZ, so you can point each AZ at its own NAT gateway.

---

## 2. Security Groups vs Network ACLs

This comparison is guaranteed to appear.

| Property | **Security Group** | **Network ACL** |
|---|---|---|
| Applies at | **ENI / instance level** | **Subnet level** |
| State | **Stateful** — return traffic is automatically allowed | **Stateless** — return traffic must be explicitly allowed |
| Rule types | **Allow only** | **Allow and Deny** |
| Evaluation | All rules evaluated; if any allows, traffic passes | **Rules processed in number order, lowest first; first match wins** |
| Default behaviour | Default SG allows all inbound *from members of the same SG* and all outbound. A newly created SG denies all inbound, allows all outbound | Default NACL allows all inbound and outbound. A **newly created custom NACL denies everything** until you add rules |
| Source/destination | CIDR, another **security group**, or a prefix list | CIDR only |
| Quantity | Up to 5 SGs per ENI (adjustable) | One NACL per subnet, many subnets per NACL |

### 2.1 Why statefulness matters

With a **security group**, if you allow inbound TCP 443, the response packets going back out are automatically permitted regardless of outbound rules. With a **NACL**, you must add an outbound rule allowing the **ephemeral port range** (1024–65535) or responses will be dropped. The symptom — "requests go out but nothing comes back" or "connections hang" — is the classic NACL question.

### 2.2 Security group referencing

Instead of hardcoding CIDRs, reference another security group as the source:

- `sg-web` allows inbound 443 from `0.0.0.0/0`
- `sg-app` allows inbound 8080 **from `sg-web`**
- `sg-db` allows inbound 3306 **from `sg-app`**

This "SG chaining" survives auto scaling, IP changes, and AZ moves, and is the least-privilege pattern the exam expects. A security group can also reference **itself**, which is how cluster members (e.g., Elasticsearch nodes) talk to each other.

### 2.3 When to use a NACL

Because security groups cannot deny, NACLs are the answer whenever the requirement is to **block** something specific:
- Block a known malicious IP or CIDR from an entire subnet
- Add a coarse subnet-level guardrail that individual teams cannot remove by editing an SG
- Enforce one-way rules at a tier boundary

For Layer 7 blocking (a bad user agent, a URI pattern, a country), use **AWS WAF** instead.

---

## 3. Network Segmentation Strategy

### 3.1 The three-tier reference design

Repeat all three tiers in **at least two (ideally three) Availability Zones**:

**Public subnets** — internet-facing load balancers (ALB/NLB), NAT gateways, and (if you still use them) bastion hosts. Nothing that holds data.

**Private application subnets** — EC2 instances, ECS tasks, EKS nodes, Lambda ENIs. No route to the IGW; outbound via NAT gateway; `sg-app` accepts traffic only from the load balancer's security group.

**Private data subnets** — RDS, Aurora, ElastiCache, OpenSearch. Often with a route table that has **no `0.0.0.0/0` route at all**, so these instances cannot reach the internet even outbound. DB subnet groups must span multiple AZs for Multi-AZ deployments.

Additional segmentation ideas that appear in scenarios:
- A separate **management/shared services VPC** or subnet for monitoring and directory services.
- A dedicated **egress VPC** with centralized NAT and firewalling, reached via Transit Gateway.
- Separate VPCs (or accounts) per environment rather than per-subnet separation, when isolation requirements are strict.

### 3.2 VPC Flow Logs

Flow Logs capture **metadata about IP traffic** (not payloads) at the VPC, subnet, or ENI level.

- Fields include source/destination IP and port, protocol, packets, bytes, start/end time, action (**ACCEPT / REJECT**), and log status. Custom formats can add `vpc-id`, `subnet-id`, `instance-id`, `tcp-flags`, `pkt-srcaddr`, and `flow-direction`.
- Destinations: **CloudWatch Logs**, **S3**, or **Kinesis Data Firehose**.
- Uses: troubleshooting "why is this blocked" (look for REJECT), detecting port scans, feeding GuardDuty, and compliance evidence.
- **They do not capture packet contents.** For full packet capture use **VPC Traffic Mirroring**, which copies traffic from an ENI to a monitoring appliance.
- Some traffic is never logged: Amazon DNS server traffic, Windows license activation, instance metadata (`169.254.169.254`), DHCP, and traffic to the reserved VPC router address.

### 3.3 Diagnostic tools

- **VPC Reachability Analyzer** — performs static configuration analysis between a source and destination and tells you whether a path exists; if not, it names the blocking component (security group, NACL, route table).
- **Network Access Analyzer** — evaluates whether unintended network paths exist (e.g., "can anything in a private subnet reach the internet?").
- **VPC Network Access Analyzer / Flow Logs + Athena** for larger investigations.

---

## 4. VPC Endpoints and Private Service Access

### 4.1 The problem they solve

By default, calling `s3.ap-south-1.amazonaws.com` from a private subnet goes out through the NAT gateway to the public internet (even though it stays on AWS's network edge). That means: NAT data-processing charges, a dependency on internet routing, and traffic that leaves your VPC boundary — which some compliance regimes forbid.

**VPC endpoints** let you reach AWS services using private IP addresses, with no IGW, no NAT, and no public IPs.

### 4.2 The three endpoint types

| Type | How it works | Services | Cost |
|---|---|---|---|
| **Gateway endpoint** | Adds a **route table entry** pointing a managed **prefix list** at the endpoint | **Amazon S3 and DynamoDB only** | **Free** |
| **Interface endpoint (AWS PrivateLink)** | Creates an **ENI with a private IP** in each chosen subnet; DNS resolves the service name to that private IP | Most AWS services, partner SaaS, and your own services | Hourly per ENI per AZ + per-GB processed |
| **Gateway Load Balancer endpoint** | Routes traffic to a fleet of third-party virtual appliances using GENEVE | Firewalls, IDS/IPS | Hourly + per-GB |

**Gateway endpoint details:** region-specific, cannot be accessed from on-premises (over DX/VPN) directly, and are controlled by an **endpoint policy** plus route table association. Because they are free, "use a gateway endpoint for S3" is almost always the right answer when the question mentions S3 traffic and cost or privacy.

**Interface endpoint details:** supports **private DNS** (so the standard service hostname resolves privately), works from on-premises over Direct Connect/VPN, can be restricted with **security groups** on the endpoint ENI, and supports endpoint policies.

### 4.3 Locking resources to an endpoint

You can require that a bucket is only reachable through a specific endpoint:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::secure-bucket", "arn:aws:s3:::secure-bucket/*"],
  "Condition": { "StringNotEquals": { "aws:SourceVpce": "vpce-0a1b2c3d" } }
}
```

Note the use of `aws:SourceVpce` rather than `aws:SourceIp` — **IP-based conditions do not work for endpoint traffic**.

### 4.4 AWS PrivateLink for your own services

If you operate a service and want other VPCs (yours or customers') to consume it privately:
1. Put the service behind a **Network Load Balancer** (or GWLB).
2. Create a **VPC endpoint service** and allowlist the consumer principals.
3. Consumers create **interface endpoints** to your service.

Benefits: no VPC peering, **overlapping CIDRs are irrelevant** (traffic is NAT'd through the endpoint), the connection is **one-way** (consumer → provider), and nothing is exposed to the internet. This is the standard SaaS-on-AWS pattern and a frequent exam answer.

---

## 5. Threats From Outside AWS, and the Services That Stop Them

### 5.1 Distributed Denial of Service

**AWS Shield Standard** — automatically enabled for every customer at no cost. Defends against common network and transport layer (L3/L4) attacks such as SYN floods, UDP reflection, and amplification attacks, with always-on detection and inline mitigation at the edge.

**AWS Shield Advanced** — paid (US$3,000/month per organization, plus data transfer), and adds:
- Enhanced detection and mitigation for larger and more sophisticated attacks, including application-layer (L7) attacks when combined with WAF
- **24/7 access to the Shield Response Team (SRT)**, who can write mitigations on your behalf during an event
- **Cost protection**: credits for scaling charges (EC2, ELB, CloudFront, Route 53, Global Accelerator) incurred because of a DDoS attack
- Protection for CloudFront, Route 53, ALB/NLB/Elastic IPs, and Global Accelerator
- **AWS WAF included at no additional cost** on protected resources, plus Firewall Manager integration
- Detailed attack diagnostics and near-real-time visibility

**Architectural defences that matter as much as the service choice:**
- Put **CloudFront and Route 53** in front — they absorb and disperse traffic at hundreds of edge locations.
- Keep origins private: restrict the origin's security group to the **CloudFront managed prefix list**, or use **Origin Access Control** for S3.
- Use **Auto Scaling** so the application can absorb surges.
- Use **AWS WAF rate-based rules** to throttle abusive IPs.
- Reduce the attack surface: no unnecessary public IPs, no open ports, API Gateway throttling.

### 5.2 Application-layer attacks and AWS WAF

**AWS WAF** is a Layer 7 web application firewall. It can be associated with:
**CloudFront, Application Load Balancer, API Gateway (REST), AppSync, Cognito user pools, App Runner, and AWS Verified Access.**
It **cannot** be attached to a Network Load Balancer or directly to an EC2 instance — a common distractor.

**Building blocks:**
- A **Web ACL** contains ordered **rules**; each rule has a **statement** and an **action**.
- **Statements**: IP set match, geographic match, string/regex match on URI, header, body, query string or cookies, size constraint, **SQL injection match**, **cross-site scripting match**, label match, and **rate-based** (count requests per 5-minute window per IP or per custom key).
- **Actions**: Allow, Block, **Count** (test mode), **CAPTCHA**, and **Challenge** (silent browser check).
- **AWS Managed Rule Groups**: Core rule set (OWASP-style), Known bad inputs, SQL database, Linux/Windows/PHP/WordPress, IP reputation, Anonymous IP list, **Bot Control**, and **Account Takeover Prevention / Account Creation Fraud Prevention**.
- **Logging** to CloudWatch Logs, S3, or Firehose, with field redaction.

**Mapping attacks to services:**

| Threat | Control |
|---|---|
| SQL injection, XSS | **AWS WAF** (managed rule groups + custom rules) |
| HTTP floods / scraping | **WAF rate-based rules**, CAPTCHA, Bot Control |
| Volumetric L3/L4 DDoS | **Shield** (Standard automatically; Advanced for large/targeted) |
| Malicious IP at network layer | **NACL deny** or WAF IP set |
| Compromised credentials, crypto-mining, port scanning | **GuardDuty** (detection) |
| Vulnerable OS packages / container images | **Amazon Inspector** |
| Exposed sensitive data in S3 | **Amazon Macie** |
| Malware on EBS volumes | **GuardDuty Malware Protection** |
| Outbound traffic to disallowed domains | **Network Firewall** or **Route 53 Resolver DNS Firewall** |

### 5.3 AWS Network Firewall

A managed, stateful network firewall and intrusion prevention system deployed **inside your VPC** at a dedicated firewall subnet per AZ. It supports:
- **Stateless rules** (5-tuple filtering, fast path)
- **Stateful rules** using **Suricata-compatible** IPS signatures
- **Domain name filtering** for egress (allow only `*.example.com`, block everything else)
- Managed threat signature rule groups
- Centralized deployment with Transit Gateway for inspection of inter-VPC and egress traffic

Choose it when a question demands **deep packet inspection, IPS, or egress FQDN filtering** across a VPC — something security groups and NACLs cannot do.

### 5.4 Route 53 Resolver DNS Firewall

Filters **outbound DNS queries** from your VPC against domain allow/deny lists, including AWS-managed lists of known malicious domains. Useful against data exfiltration over DNS and malware command-and-control.

### 5.5 AWS Firewall Manager

A central policy manager that enforces security configuration **across all accounts in an AWS Organization**:
- AWS WAF web ACLs and rule groups
- Shield Advanced protections
- Security group policies (audit and enforce common rules, find unused/redundant groups)
- Network Firewall and DNS Firewall policies

Crucially, it applies policies to **existing and newly created resources automatically**. When a question says "ensure consistent rules across dozens of accounts, including new ALBs created in the future," the answer is **Firewall Manager**.

### 5.6 Detection and posture services

| Service | What it does | Data sources / scope |
|---|---|---|
| **Amazon GuardDuty** | Continuous intelligent **threat detection**; agentless | CloudTrail management and S3 data events, VPC Flow Logs, DNS logs, plus optional EKS audit logs, RDS login activity, Lambda network activity, and EBS malware scanning |
| **Amazon Macie** | Discovers and classifies **sensitive data in S3** (PII, PHI, credentials, financial data) using ML and pattern matching | S3 buckets; reports to Security Hub/EventBridge |
| **Amazon Inspector** | Automated **vulnerability management** — CVEs and network reachability | EC2 (via SSM agent), **ECR container images**, and **Lambda functions** |
| **AWS Security Hub** | Aggregates and normalizes findings; runs **security standards** (CIS, PCI DSS, AWS Foundational Security Best Practices) | All of the above plus partner products; org-wide with a delegated admin |
| **Amazon Detective** | Builds a behaviour graph to investigate the root cause of a finding | CloudTrail, VPC Flow Logs, GuardDuty findings |
| **AWS Config** | Records configuration state and evaluates **compliance rules**, with auto-remediation via SSM documents | All supported resources; aggregators for org-wide view |
| **AWS CloudTrail** | Records API calls: who, what, when, from where | Management events (free, 90-day history), data events, Insights |
| **AWS Audit Manager** | Collects evidence continuously and maps it to frameworks (PCI, HIPAA, SOC 2, GDPR) | Across services |

---

## 6. Application Configuration and Credentials Security

### 6.1 The rule

Credentials and configuration must never be hardcoded in source code, baked into AMIs or container images, committed to Git, or passed as plaintext environment variables that end up in logs. Instead, the application is given an **IAM role**, and it uses that role to fetch secrets at runtime from a managed store.

### 6.2 AWS Secrets Manager vs SSM Parameter Store

| Feature | **Secrets Manager** | **SSM Parameter Store** |
|---|---|---|
| Price | Per secret per month + API calls | **Standard tier free** (10,000 params); advanced tier paid |
| **Automatic rotation** | **Yes** — built-in Lambda rotation for RDS, Aurora, Redshift, DocumentDB; custom Lambda for anything else | **No native rotation** (you can build it with EventBridge + Lambda) |
| Cross-account access | Yes, via a **resource policy** on the secret | No resource policy |
| Encryption | KMS (always) | **SecureString** type with KMS |
| Generate random passwords | **Yes** (`GetRandomPassword`) | No |
| Size limit | 64 KB | 4 KB standard / 8 KB advanced |
| Versioning / staging labels | Yes (AWSCURRENT, AWSPREVIOUS, AWSPENDING) | Version history |
| Hierarchy / path queries | Limited | **Yes** (`/app/prod/db/...`, `GetParametersByPath`) |
| Best for | Database credentials, API keys, anything needing rotation or cross-account sharing | Configuration values, feature flags, non-sensitive settings, simple secrets on a budget |

**Rotation strategies in Secrets Manager:**
- **Single user** — the rotation Lambda changes the password of one database user. Brief window where in-flight connections may use the old password.
- **Alternating users** — two users are maintained and rotated alternately, so there is always a valid credential. Recommended for zero-downtime rotation.

### 6.3 Eliminating passwords entirely

- **IAM database authentication** (RDS MySQL/PostgreSQL and Aurora): the application calls `generate-db-auth-token` using its IAM role and uses that token as the password. Tokens are valid for **15 minutes**, and there is no stored secret at all. Note the connection limit considerations (roughly 200 new connections/second).
- **IAM roles for all AWS service calls** — never an access key.
- **Amazon RDS Proxy** can retrieve credentials from Secrets Manager and enforce IAM authentication centrally.

### 6.4 Other configuration hygiene

- **Lambda environment variables** are encrypted at rest with KMS; for sensitive values use Secrets Manager/Parameter Store or at minimum a customer managed key with encryption helpers.
- **ECS/EKS**: inject secrets via the task definition's `secrets` block (pulled from Secrets Manager or Parameter Store) rather than `environment`.
- **AWS AppConfig** for safe, validated configuration deployment with rollback.
- Scan repositories for leaked credentials (git-secrets, CodeGuru, Amazon CodeWhisperer security scans) and rotate anything exposed.

---

## 7. Secure Application Access

### 7.1 Authenticating users to applications

- **Amazon Cognito user pools** — full identity provider for your app: sign-up, sign-in, MFA, password policies, hosted UI, social and enterprise federation; issues JWTs.
- **ALB built-in authentication** — the load balancer itself can require authentication via **Cognito** or any **OIDC** provider before forwarding to targets. Zero application code.
- **API Gateway authorization options**:
  - **IAM (SigV4)** — for internal/service-to-service calls
  - **Cognito user pool authorizer** — validates the JWT
  - **Lambda authorizer** — custom logic (token-based or request-based), with caching
  - **Resource policy** — restrict by account, IP, or VPC endpoint
  - **Mutual TLS (mTLS)** — client certificate authentication
  - **API keys + usage plans** — throttling and quota, **not** an authentication mechanism (a common trap)
- **AWS Verified Access** — zero-trust access to internal applications without a VPN, evaluating identity and device posture on every request.
- **AWS Verified Permissions** — externalized fine-grained authorization using Cedar policies.

### 7.2 Administrative access to instances

Ranked from best to worst for the exam:

1. **AWS Systems Manager Session Manager** — browser or CLI shell with **no inbound ports, no bastion host, no SSH keys, no public IPs**. Requires the SSM agent (pre-installed on Amazon Linux, Ubuntu, Windows AMIs), an instance role with `AmazonSSMManagedInstanceCore`, and connectivity to SSM endpoints (via NAT or **interface endpoints** for `ssm`, `ssmmessages`, `ec2messages`). Sessions can be **logged to S3/CloudWatch**, and access is controlled with IAM. This is the modern correct answer.
2. **EC2 Instance Connect / Instance Connect Endpoint** — push a temporary SSH key or tunnel SSH/RDP without public IPs.
3. **Bastion host** — a hardened instance in a public subnet with an SG restricted to the corporate CIDR; all admin traffic hops through it. Still appears in scenarios, but if Session Manager is an option it usually wins on "no inbound ports / least operational overhead."

---

## 8. Securing External Network Connections

### 8.1 AWS Site-to-Site VPN

- IPsec tunnels between your **customer gateway** (on-prem device) and a **virtual private gateway** (attached to a VPC) or a **transit gateway**.
- Each connection provides **two tunnels** terminating in different AZs for redundancy; each tunnel supports roughly **1.25 Gbps**. With Transit Gateway you can use **ECMP** across multiple tunnels to aggregate bandwidth.
- **Encrypted by default** (IPsec), runs over the public internet, so latency and jitter vary.
- Deployable in **minutes**, and inexpensive (hourly connection charge plus data transfer).
- Supports static routing or **BGP** dynamic routing.
- **AWS Client VPN** is the separate, OpenVPN-based service for individual remote users connecting into a VPC, with authentication via Active Directory, SAML, or certificates.

### 8.2 AWS Direct Connect

- A **dedicated private network connection** from your data center or colocation facility into an AWS Direct Connect location.
- Port speeds from **50 Mbps to 100 Gbps** (hosted connections for sub-1 Gbps; dedicated for 1/10/100 Gbps).
- Benefits: **consistent, predictable latency**, higher and more reliable throughput, and **lower per-GB data transfer costs** than internet egress.
- Drawbacks: takes **weeks to months** to provision, costs a fixed port fee, and — critically — **is not encrypted by default**. Direct Connect provides privacy (your traffic is not on the public internet) but not cryptographic confidentiality.
- **Virtual interfaces (VIFs):**
  - **Private VIF** → reach VPC resources via VGW or Direct Connect gateway
  - **Public VIF** → reach AWS public endpoints (S3, DynamoDB) over the private link
  - **Transit VIF** → connect to a Transit Gateway via a Direct Connect gateway
- **Direct Connect Gateway** lets one connection reach VPCs in **multiple Regions and accounts**.
- **Resiliency options:** two connections at one location (development/standard), two connections at **two different locations** (high resilience), or four connections across two locations (maximum resilience). A **Site-to-Site VPN as a backup** is the cheap resilience option.

### 8.3 Choosing between them

| Requirement | Answer |
|---|---|
| Encrypted hybrid link, quick, low cost | **Site-to-Site VPN** |
| Consistent high bandwidth, predictable latency, large sustained transfers | **Direct Connect** |
| Private link **and** encryption in transit required | **IPsec VPN running over Direct Connect** (or MACsec on supported DX ports) |
| Direct Connect with resilient failover on a budget | **DX + VPN backup** |
| Many VPCs and multiple on-prem sites | **Transit Gateway** + DX Gateway and/or VPN attachments |
| Individual remote employees | **AWS Client VPN** |

---

## 9. Ports and Protocols Reference

| Port | Protocol / service |
|---|---|
| 22 | SSH, SFTP |
| 25 | SMTP (outbound restricted by default on EC2) |
| 53 | DNS (TCP and UDP) |
| 80 / 443 | HTTP / HTTPS |
| 123 | NTP |
| 389 / 636 | LDAP / LDAPS |
| 445 | SMB (FSx for Windows) |
| 1433 | Microsoft SQL Server |
| 1521 | Oracle |
| 2049 | NFS (EFS) |
| 3306 | MySQL, MariaDB, Aurora MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL, Aurora PostgreSQL |
| 5439 | Amazon Redshift |
| 6379 | Redis / Valkey |
| 11211 | Memcached |
| 27017 | MongoDB / DocumentDB |
| 1024–65535 | Ephemeral ports (needed in NACL rules) |

---

## 10. Worked Scenarios

**Scenario 1 — "Instances in private subnets must download OS patches."**
NAT gateway in a public subnet per AZ, with each private route table pointing `0.0.0.0/0` at its local NAT gateway. If the patches come from S3 (e.g., a repository mirror), add an **S3 gateway endpoint** to cut both cost and exposure.

**Scenario 2 — "We're being hit by SQL injection attempts through our ALB."**
Attach an **AWS WAF web ACL** to the ALB with the **SQL database managed rule group** and the core rule set; start rules in **Count** mode to measure false positives, then switch to Block. Add a **rate-based rule** for abusive clients.

**Scenario 3 — "A single IP address is scanning our subnet."**
Add an inbound **NACL Deny** rule with a low rule number for that CIDR. (SGs cannot deny.) For HTTP-layer blocking, a WAF IP set is also valid.

**Scenario 4 — "Lambda functions in a VPC need Secrets Manager and KMS but must not touch the internet."**
Create **interface VPC endpoints** for `secretsmanager` and `kms` in the function's subnets, with security groups allowing 443 from the Lambda ENIs. No NAT gateway required.

**Scenario 5 — "Operators need shell access to instances in private subnets; auditors need session recordings."**
**SSM Session Manager** with an instance profile granting `AmazonSSMManagedInstanceCore`, session logging to S3/CloudWatch, and IAM policies restricting who can start sessions on which instances (using tags).

**Scenario 6 — "Partner must consume our internal API; their VPC uses the same CIDR as ours."**
**AWS PrivateLink**: NLB in front of the service, a VPC endpoint service, and an interface endpoint in the partner's VPC. Overlapping CIDRs are irrelevant.

**Scenario 7 — "Regulator requires that traffic to AWS never crosses the public internet and is encrypted."**
**Direct Connect** for the private path plus an **IPsec VPN over the DX** (or MACsec) for encryption; use **public VIF or interface endpoints** for AWS service access.

**Scenario 8 — "We must enforce the same WAF rules on every ALB in 40 accounts, including ones created next month."**
**AWS Firewall Manager** policy at the organization level.

---

## 11. Quick Decision Table

| Requirement | Answer |
|---|---|
| Block one malicious IP for a whole subnet | **NACL deny rule** |
| Filter SQLi/XSS/bots/geo at Layer 7 | **AWS WAF** |
| Absorb a large volumetric DDoS with expert support | **Shield Advanced** |
| Deep packet inspection and egress domain filtering | **AWS Network Firewall** |
| Block malicious DNS lookups | **Route 53 Resolver DNS Firewall** |
| Same security policies across many accounts | **AWS Firewall Manager** |
| Private subnet instances need internet for updates | **NAT gateway (one per AZ)** |
| Private access to S3/DynamoDB | **Gateway VPC endpoint (free)** |
| Private access to KMS/Secrets Manager/SSM/ECR | **Interface endpoint (PrivateLink)** |
| Expose your service to other VPCs privately | **PrivateLink endpoint service behind an NLB** |
| Shell access with no open ports or keys | **SSM Session Manager** |
| Rotate database credentials automatically | **Secrets Manager** |
| Store non-secret configuration cheaply | **SSM Parameter Store (standard tier)** |
| Remove database passwords entirely | **IAM database authentication** |
| Detect compromised instances / unusual API calls | **GuardDuty** |
| Find PII stored in S3 | **Macie** |
| Scan EC2 and container images for CVEs | **Inspector** |
| Single view of all security findings | **Security Hub** |
| Investigate the root cause of a finding | **Detective** |
| Record whether traffic was accepted or rejected | **VPC Flow Logs** |
| Determine why a connection fails | **Reachability Analyzer** |
| Capture full packets for forensic analysis | **VPC Traffic Mirroring** |
| Encrypted hybrid link quickly | **Site-to-Site VPN** |
| Consistent high-bandwidth hybrid link | **Direct Connect** |
| Private hybrid link that must also be encrypted | **VPN over Direct Connect** |
| Remote employees need VPC access | **AWS Client VPN** |

---

## Task 1.3 — Determine Appropriate Data Security Controls

> This task covers **encryption (at rest and in transit), key management, data classification and governance, retention, and backup/recovery**. The recurring exam themes are: which encryption option fits, how to retrofit encryption onto existing resources, how to make data immutable, and how to centralize backups.

---

## 1. Encryption Fundamentals

### 1.1 At rest vs in transit

- **Encryption at rest** protects data sitting on disk — in S3, EBS, EFS, FSx, RDS, DynamoDB, Redshift, snapshots, and backups. It defends against physical media theft and against someone obtaining the underlying storage.
- **Encryption in transit** protects data moving over a network — TLS/SSL for HTTPS and database connections, IPsec for VPNs, and SSH. It defends against interception and man-in-the-middle attacks.

A complete design uses both, plus access control. Encryption is **not** a substitute for IAM: if a principal is allowed to call `s3:GetObject` and `kms:Decrypt`, encryption is transparent to them.

### 1.2 Symmetric vs asymmetric

- **Symmetric** — one key encrypts and decrypts (AES-256). Fast, and the default for every AWS service integration. A symmetric KMS key never leaves KMS in plaintext.
- **Asymmetric** — a mathematically linked public/private key pair (RSA or ECC). KMS supports asymmetric keys for **encrypt/decrypt** (when a party outside AWS must encrypt without calling KMS) and for **sign/verify** (digital signatures). The public key can be downloaded and distributed; the private key never leaves KMS.

### 1.3 Envelope encryption — the central concept

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

## 2. AWS KMS in Depth

### 2.1 What KMS is

A managed service for creating and controlling cryptographic keys, backed by **FIPS 140-2 validated hardware security modules**. Key material **never leaves KMS unencrypted**, KMS is integrated with virtually every AWS service, and **every key usage is recorded in CloudTrail**.

**KMS keys are Regional.** A key created in `ap-south-1` cannot decrypt data in `us-east-1`. To work across Regions you either re-encrypt with a destination-Region key (what S3 replication does automatically if configured) or create a **multi-Region key** — a primary key plus related replicas sharing the same key material and key ID suffix, so ciphertext from one Region can be decrypted in another.

### 2.2 Key types

| Type | Managed by | Rotation | Visible / controllable | Cost |
|---|---|---|---|---|
| **AWS owned keys** | AWS, shared across many accounts | AWS-controlled | Not visible in your account, no policy control | Free |
| **AWS managed keys** (`aws/s3`, `aws/ebs`, `aws/rds`) | AWS, one per service per account | **Automatic, every year, cannot be disabled** | Visible; **key policy cannot be edited** | Free (pay per API call) |
| **Customer managed keys (CMK)** | You | **Optional automatic rotation**, default yearly, configurable 90–2,560 days | Full control: key policy, grants, aliases, enable/disable, schedule deletion, tags | ~$1/month per key + API calls |
| **Imported key material (BYOK)** | You import 256-bit material | **Manual only** (import new material into a new key) | You can delete the material immediately, and set an expiry | Same as CMK |
| **Custom key store (CloudHSM-backed)** | You, in a dedicated CloudHSM cluster | Manual | Full control, single-tenant HSMs | CMK cost + CloudHSM cost |
| **External key store (XKS)** | Key material held **outside AWS** in your own HSM/key manager | You | Full control, highest separation | Highest complexity |

**When the exam wants a CMK:** whenever the requirement mentions auditing key usage, controlling who can use the key, rotating on your own schedule, sharing a key cross-account, or disabling/deleting a key. AWS managed keys cannot do any of those.

### 2.3 Key rotation — what actually changes

- **Automatic rotation of a customer managed key** creates **new backing key material** on schedule while keeping the **same key ID, ARN, and alias**. AWS retains all previous backing keys so old ciphertext still decrypts. Your applications need no changes and nothing has to be re-encrypted. New encrypt operations use the newest material.
- **AWS managed keys** rotate automatically every year; you cannot turn it off or change the period.
- **Imported key material cannot be automatically rotated** — you must import new material (into a new key) and re-encrypt or re-point an alias.
- **Manual rotation** = create a brand-new key and update the **alias** to point at it. Old data still requires the old key, so keep it enabled.
- **On-demand rotation** is also supported for CMKs.

### 2.4 Key policies, grants and IAM

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

### 2.5 Key deletion and disabling

- You cannot delete a KMS key immediately. You **schedule deletion** with a waiting period of **7 to 30 days** (default 30). During that window the key is unusable but recoverable.
- **Disabling** a key is instant and reversible — the better choice if you just need to stop usage temporarily.
- Deleting a key permanently destroys all data encrypted under it. Use `kms:ScheduleKeyDeletion` deliberately and consider an SCP denying it.

### 2.6 Quotas and cost control

KMS enforces a shared per-Region quota on cryptographic operations (on the order of 5,500 to 50,000 requests per second depending on Region and operation type). High-volume workloads can hit `ThrottlingException`. Mitigations:
- **S3 Bucket Keys** — a bucket-level data key is generated and reused for many objects, cutting KMS requests (and cost) by **up to 99%**. Enable this whenever a bucket uses SSE-KMS at scale.
- **Data key caching** in the AWS Encryption SDK.
- Request a quota increase.

### 2.7 AWS CloudHSM

A **single-tenant, dedicated hardware security module** cluster in your VPC, validated to **FIPS 140-2 Level 3**. You control the HSM users and keys; **AWS has no access to your key material** and cannot recover it if you lose credentials.

Use CloudHSM when:
- A regulation requires single-tenant, customer-controlled HSMs or FIPS 140-2 Level 3
- You need PKCS#11, JCE, or Microsoft CNG/KSP interfaces
- You are offloading SSL/TLS processing or running a private certificate authority
- You need Oracle TDE or SQL Server TDE with keys you alone hold
- You want a **KMS custom key store** (KMS front end, CloudHSM key storage)

Trade-offs: you manage clustering, backups, and users; it is far more expensive than KMS; and it is not natively integrated with most AWS services except through KMS custom key stores.

---

## 3. Encryption by Service — the details that get tested

### 3.1 Amazon S3

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

### 3.2 Amazon EBS

- Encryption uses **KMS with AES-256**, is transparent to the instance, and has a negligible performance impact.
- When a volume is encrypted, so are: **data at rest on the volume, data in transit between the instance and the volume, all snapshots of it, and all volumes created from those snapshots**.
- **You cannot encrypt an existing unencrypted volume in place, and you cannot remove encryption.** The workflow is: **create a snapshot → copy the snapshot with encryption enabled (choosing a key) → create a new volume (or AMI) from the encrypted copy → attach it**.
- **EBS encryption by default** can be enabled per account per Region, so every new volume and snapshot is encrypted automatically.
- **Sharing encrypted snapshots across accounts** requires a **customer managed key** (AWS managed keys cannot be shared); you share both the snapshot and the key. **Encrypted snapshots can never be made public.**
- Root volumes can be encrypted at launch, and AMIs can be copied with encryption to produce encrypted-by-default images.

### 3.3 Amazon EFS and FSx

- **EFS**: encryption at rest uses KMS and **can only be enabled at file system creation**; encryption in transit uses **TLS via the EFS mount helper** (`-o tls`). Access control combines **IAM** (file system policy), **EFS Access Points** (enforce a POSIX user/group and root directory per application), security groups, and POSIX permissions. A file system policy can enforce `elasticfilesystem:ClientRootAccess` restrictions and require TLS with `aws:SecureTransport`.
- **FSx for Windows File Server**: encrypted at rest with KMS by default; in transit with **SMB Kerberos session encryption**. Integrates with Active Directory for authentication and NTFS ACLs.
- **FSx for Lustre**: encryption at rest by default; in-transit encryption supported on specific instance types in the same VPC.
- **FSx for NetApp ONTAP / OpenZFS**: KMS at rest, plus their native protocol encryption.

### 3.4 Amazon RDS and Aurora

- Encryption at rest uses **KMS** and **must be enabled when the DB instance/cluster is created**. To encrypt an existing unencrypted database: **snapshot → copy the snapshot with encryption → restore from the encrypted snapshot** (then cut over).
- Once encrypted: automated backups, snapshots, read replicas, and (for Aurora) the cluster volume are all encrypted. **You cannot have an encrypted replica of an unencrypted primary, or vice versa.**
- **Encryption in transit**: RDS provides a CA bundle; clients connect with TLS. You can force it: PostgreSQL parameter `rds.force_ssl=1`, MySQL `require_secure_transport=ON`, SQL Server `rds.force_ssl`.
- **Transparent Data Encryption (TDE)** is additionally available for Oracle and SQL Server via option groups, optionally backed by CloudHSM.
- **IAM database authentication** removes stored passwords (15-minute tokens) for MySQL, PostgreSQL, and Aurora.
- **Performance Insights** data and logs can also be encrypted with KMS.

### 3.5 DynamoDB, and other services

- **DynamoDB is encrypted at rest by default** — you choose an AWS owned key (default, free), an AWS managed key, or a customer managed key. Encryption cannot be disabled.
- Fine-grained access control uses IAM conditions such as **`dynamodb:LeadingKeys`** (restrict a user to items whose partition key matches their identity) and `dynamodb:Attributes` with a projection expression for column-level control.
- **Amazon Redshift** — cluster encryption with KMS or HSM, chosen at creation; encrypted in transit with TLS.
- **SQS, SNS, Kinesis, EventBridge** — SSE with KMS, optional.
- **Amazon EBS-backed AMIs, EMR, SageMaker, Glue, Athena results, CloudWatch Logs** — all support KMS encryption.
- **AWS CloudTrail** — logs are SSE-S3 encrypted by default; use **SSE-KMS** plus **log file validation** (digest files) to make tampering detectable. Store in a dedicated Log Archive account with **Object Lock**.
- **Lambda** — environment variables encrypted with KMS at rest; use a CMK plus encryption helpers for sensitive values.

---

## 4. Encryption in Transit and AWS Certificate Manager

### 4.1 ACM essentials

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

### 4.2 Where to terminate TLS

- **At CloudFront** — closest to the user, best performance; CloudFront can then re-encrypt to the origin (HTTPS only is the secure setting).
- **At the ALB** — common; the ALB holds the ACM certificate, and you can optionally re-encrypt to targets.
- **At the instance (end-to-end encryption)** — required when regulation forbids plaintext anywhere; use an **NLB with TCP passthrough** or an ALB with HTTPS targets, and install certificates on instances (from Private CA or imported).

---

## 5. Data Classification, Governance and Compliance

### 5.1 Classification

Classification is the process of labelling data by sensitivity (e.g., Public, Internal, Confidential, Restricted) so that controls can be applied consistently.

- **Amazon Macie** automates discovery in **S3**: it inventories buckets (public access, encryption status, sharing) and runs sensitive data discovery jobs using managed identifiers (names, addresses, credit cards, passports, AWS keys, medical identifiers) and **custom data identifiers** (your own regex). Findings go to Security Hub and EventBridge for automated response.
- **Tagging** turns classification into an enforceable control: tag resources `Classification=Confidential`, then use **ABAC** conditions (`aws:ResourceTag`) to restrict access, and **tag policies** in Organizations to keep tag keys/values consistent.
- **AWS Glue Data Catalog + Lake Formation** classify and govern structured data in a data lake, with **column-, row-, and cell-level permissions** — the right answer when a question asks for fine-grained analytics access control.

### 5.2 Governance tooling

- **AWS Config** — continuous configuration recording plus managed rules such as `s3-bucket-server-side-encryption-enabled`, `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `rds-storage-encrypted`, `iam-user-mfa-enabled`, `acm-certificate-expiration-check`. Rules can trigger **automatic remediation** via SSM Automation documents. **Conformance packs** bundle rules into a compliance framework and can be deployed org-wide.
- **AWS Organizations policies** — SCPs to deny unencrypted actions, tag policies, backup policies.
- **AWS Artifact** — self-service portal for AWS's own compliance reports (SOC 1/2/3, PCI DSS AoC, ISO certifications) and agreements (including the **HIPAA BAA** and GDPR DPA). The answer when an auditor asks for AWS's certifications.
- **AWS Audit Manager** — continuously collects evidence from your environment and maps it to prebuilt frameworks (HIPAA, PCI DSS v3.2.1, GDPR, SOC 2, CIS), producing assessment reports. The answer when the requirement is evidence collection about **your** workloads.
- **AWS Security Hub** — compliance standards scoring and finding aggregation.

### 5.3 Common compliance mappings

| Requirement | Typical AWS implementation |
|---|---|
| **HIPAA** | Use HIPAA-eligible services, sign the **BAA** via Artifact, encrypt PHI at rest (KMS) and in transit (TLS), enable CloudTrail, restrict access with IAM, log and monitor |
| **PCI DSS** | Network segmentation (separate VPC/account for the CDE), WAF, encryption, key management with KMS/CloudHSM, CloudTrail + Config, quarterly scanning (Inspector) |
| **GDPR** | Choose EU Regions for residency, encrypt, implement deletion workflows (lifecycle rules, crypto-shredding), DPA via Artifact, Macie for discovery |
| **Data residency** | Region selection + **SCP restricting `aws:RequestedRegion`**, avoid global replication, Outposts/Local Zones if on-soil infrastructure is required |
| **Immutable audit records** | S3 **Object Lock compliance mode** or Glacier Vault Lock, CloudTrail log file validation, separate Log Archive account |

---

## 6. Backups, Replication and Recovery

### 6.1 AWS Backup

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

### 6.2 Service-native mechanisms

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

### 6.3 Retention and lifecycle

**S3 Lifecycle** supports two action types:
- **Transition** between storage classes (Standard → Standard-IA → Intelligent-Tiering → Glacier Instant Retrieval → Glacier Flexible Retrieval → Deep Archive)
- **Expiration** — delete current versions, delete **noncurrent versions** after N days, **remove expired delete markers**, and **abort incomplete multipart uploads** (a frequently forgotten source of invisible cost)

**Minimum storage durations to remember:** Standard-IA and One Zone-IA **30 days**; Glacier Instant Retrieval **90 days**; Glacier Flexible Retrieval **90 days**; Deep Archive **180 days**. Deleting earlier incurs a prorated early-deletion charge. Objects must also be at least 30 days old before transitioning from Standard to Standard-IA.

**Retention principle for the exam:** align retention to the stated compliance requirement, use lifecycle automation rather than scripts, and use Object Lock/Vault Lock only where immutability is genuinely required (because you then *cannot* delete early to save money).

---

## 7. Worked Scenarios

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

## 8. Quick Decision Table

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

---

# Domain 2 — Design Resilient Architectures (26%)


## Task 2.1 — Design Scalable and Loosely Coupled Architectures

> This task is about **how components talk to each other** and **how each one grows independently**. The recurring exam theme: a synchronous, tightly coupled design is failing under load or cascading failures — replace it with queues, events, load balancers, auto scaling, caching, and managed services.

---

## 1. Scaling Concepts

### 1.1 Vertical vs horizontal scaling

**Vertical scaling (scale up)** means replacing a resource with a bigger one — `t3.medium` → `m6i.4xlarge`, or `db.r6g.large` → `db.r6g.8xlarge`.
- *Advantages:* no application changes, no distributed-systems complexity, works for software that cannot be clustered.
- *Disadvantages:* there is always a ceiling (the largest instance type); it usually requires a **stop/start or failover**, so there is downtime; and a single large instance is a single point of failure. You also pay for peak capacity continuously.
- *Where it is still the right answer:* the **writer node of a relational database**, legacy monoliths, and licensed software priced per node.

**Horizontal scaling (scale out)** means adding more instances of the same component behind a load balancer or a queue.
- *Advantages:* effectively unlimited, each unit is small and cheap, failures remove only a fraction of capacity, and you can scale in to save money.
- *Prerequisite:* the component must be **stateless**, or state must be externalized.
- *This is the cloud-native default and the expected exam answer* whenever the question mentions growth, elasticity, or availability.

**Elasticity** is the ability to add and remove capacity automatically in response to demand; **scalability** is the ability to grow at all. AWS questions that say "handle unpredictable spikes without over-provisioning" are asking for **elasticity** (Auto Scaling, serverless, on-demand capacity).

### 1.2 Stateless design

A **stateless** component keeps no client-specific data in local memory or on local disk between requests, so any instance can serve any request. To get there:

| State | Where to put it |
|---|---|
| Session data (login, shopping cart) | **ElastiCache for Redis** or **DynamoDB** |
| Uploaded files / user content | **Amazon S3** |
| Shared files needing POSIX semantics | **Amazon EFS** |
| Application configuration | **SSM Parameter Store / AppConfig** |
| Secrets | **Secrets Manager** |
| Long-running job state | **Step Functions**, DynamoDB, or a queue |

**Sticky sessions (session affinity)** on an ALB pin a user to one target using a cookie. They are a *compatibility workaround* for applications that cannot be made stateless — useful but imperfect, because they unbalance the fleet and a target failure still loses the session. If a question says "the application cannot be modified," sticky sessions are acceptable; if it says "design a scalable architecture," externalize the state.

### 1.3 Loose coupling

Two components are **tightly coupled** when one calls the other synchronously and directly, and must know its address, be available at the same moment, and process at the same speed. One slow or failed component then stalls or breaks the whole chain.

**Loose coupling** inserts a well-defined interface between them — a load balancer, a queue, a topic, an event bus, or an API — so that:
- Producers don't need to know how many consumers exist or where they are
- A consumer outage buffers work instead of losing it
- Each side scales on its own signal
- Components can be deployed, upgraded, and replaced independently

---

## 2. Load Balancing with Elastic Load Balancing

### 2.1 The four load balancer types

| | **Application LB (ALB)** | **Network LB (NLB)** | **Gateway LB (GWLB)** | *Classic LB (legacy)* |
|---|---|---|---|---|
| OSI layer | **7** (HTTP, HTTPS, gRPC, WebSocket) | **4** (TCP, UDP, TLS) | **3** (GENEVE on port 6081) | 4 / 7 |
| Routing decisions | Host header, **URL path**, HTTP headers, query string, HTTP method, source IP | Protocol + port only | Transparent bump-in-the-wire | Basic |
| Latency / throughput | Low latency, very high throughput | **Ultra-low latency, millions of requests per second** | n/a | Lower |
| Static IP | No — use the DNS name (or front it with Global Accelerator) | **Yes — one Elastic IP per AZ** | n/a | No |
| Target types | Instance, **IP**, **Lambda** | Instance, IP, **ALB** | Appliance fleet | Instance |
| Preserves client source IP | Via `X-Forwarded-For` header | **Yes, natively** | Yes | Via XFF |
| Notable features | WAF integration, **Cognito/OIDC authentication**, redirects, fixed responses, weighted target groups, slow start, sticky sessions | PrivateLink support, TLS termination, UDP, extreme scale, preserves source IP | Inserts third-party firewalls/IDS | Deprecated |

**Choosing:**
- HTTP/HTTPS microservices with path or host routing → **ALB**
- Non-HTTP protocols, gaming/IoT/UDP, static IPs, extreme performance, or PrivateLink → **NLB**
- Inserting a virtual firewall/IDS appliance fleet transparently → **GWLB**
- Need both: an **ALB registered as a target of an NLB** gives you static IPs plus L7 routing

### 2.2 Target groups, listeners and rules

- A **listener** watches a port/protocol; **rules** evaluate conditions in priority order and route to a **target group**.
- Example microservice routing on one ALB: `/api/orders/*` → orders-tg, `/api/users/*` → users-tg, `Host: admin.example.com` → admin-tg, everything else → a fixed 404 response. One ALB can therefore serve many services, which is also a cost optimization.
- **Weighted target groups** enable blue/green and canary deployments (e.g., 95% to v1, 5% to v2).
- **Health checks** per target group (protocol, path, interval, timeout, healthy/unhealthy thresholds, matcher codes). Unhealthy targets are removed from rotation; the ASG can then replace them if the ASG health check type is **ELB**.
- **Deregistration delay (connection draining)** — default **300 seconds** — lets in-flight requests finish before a target is removed.
- **Slow start** gradually ramps traffic to newly registered targets so caches and JITs warm up.

### 2.3 Cross-zone load balancing

- **ALB: enabled by default and free.** Every node can send traffic to targets in any AZ, so an uneven number of targets per AZ is still balanced evenly.
- **NLB: disabled by default**, and enabling it incurs **inter-AZ data transfer charges**. Without it, each NLB node sends only to targets in its own AZ.

### 2.4 TLS and security

- Terminate TLS at the load balancer with an **ACM certificate** (ALB certs in the ALB's Region).
- **SNI** lets one listener host many certificates.
- Use **security group chaining**: the ALB's SG allows 443 from the internet; the instance SG allows the app port **from the ALB's SG only**.
- Attach **AWS WAF** to the ALB for L7 protection; NLBs cannot have WAF.

---

## 3. Auto Scaling

### 3.1 EC2 Auto Scaling groups

An **ASG** maintains a fleet between a **minimum**, **desired**, and **maximum** capacity, spread across the subnets (AZs) you specify, and replaces unhealthy instances automatically.

**Launch templates** (preferred over the older launch configurations) define the AMI, instance type, key pair, security groups, IAM instance profile, user data, and storage. They are **versioned**, support **mixed instance policies**, and are required for newer features.

**Health checks:**
- **EC2 health checks** (default) only detect instance-level failure — a hung application on a running instance stays "healthy."
- **ELB health checks** evaluate the application endpoint. **Set `HealthCheckType=ELB`** so application failures trigger replacement. This is a very common exam fix.
- A **health check grace period** prevents new instances from being killed before they finish booting.

**Other behaviours worth knowing:**
- The ASG **rebalances across AZs** automatically to keep capacity even.
- **Default termination policy:** the AZ with the most instances → the instance using the oldest launch template/configuration → the one closest to the next billing hour. You can override with custom policies.
- **Lifecycle hooks** pause an instance in `Pending:Wait` (to bootstrap, register with a config system, or pull data) or `Terminating:Wait` (to drain connections, upload logs) until you signal completion or the timeout expires.
- **Warm pools** keep pre-initialized instances in a **stopped** state so scale-out is fast for applications with long boot times.
- **Instance refresh** performs a rolling replacement to adopt a new launch template version, honouring a minimum healthy percentage and optional checkpoints — the safe way to roll out a new AMI.
- **Mixed instances policy** combines multiple instance types and a split of On-Demand and **Spot** capacity, with allocation strategies (`capacity-optimized`, `price-capacity-optimized`) and **capacity rebalancing** to pre-emptively replace Spot instances that are about to be reclaimed.

### 3.2 Scaling policies

| Policy | How it works | When to use |
|---|---|---|
| **Target tracking** | Keep a metric at a target value (e.g., average CPU 50%, `ALBRequestCountPerTarget` 1000) — AWS manages the alarms | **The default recommendation**; simplest and most robust |
| **Step scaling** | CloudWatch alarm breaches trigger different adjustments depending on how far the metric is from the threshold | When you need more aggressive response to larger breaches |
| **Simple scaling** | One adjustment per alarm, with a cooldown | Legacy; avoid |
| **Scheduled scaling** | Change min/max/desired at specific times | Known patterns: business hours, month-end, Black Friday |
| **Predictive scaling** | Machine learning forecasts load from at least 24 hours of history and provisions **ahead** of demand | Recurring daily/weekly cycles, long instance boot times |

Good practice: **predictive or scheduled scaling for the known baseline, target tracking for the unexpected.**

**Choosing the metric matters more than the policy type.** CPU is a poor proxy for a queue worker (which may be I/O bound) or for a memory-bound app. Common correct metrics:
- Web tier → `ALBRequestCountPerTarget` or CPU
- Queue workers → **`ApproximateNumberOfMessagesVisible`**, ideally converted to **backlog per instance** (messages ÷ instances) as a custom metric
- Memory-bound apps → a **custom metric published by the CloudWatch agent** (memory is not a default EC2 metric)

### 3.3 Application Auto Scaling

Beyond EC2, AWS Auto Scaling / Application Auto Scaling can scale: **ECS services**, **DynamoDB** table and index capacity, **Aurora Replicas**, **Lambda provisioned concurrency**, Spot Fleet, EMR clusters, SageMaker endpoints, Comprehend, Keyspaces, Neptune, and more.

---

## 4. Decoupling: Queues, Topics, Events and Workflows

### 4.1 Amazon SQS

A fully managed, **pull-based** message queue. Producers send messages; consumers poll, process, and delete them. The queue acts as a **buffer** that absorbs traffic spikes and isolates failures.

**Queue types:**

| | **Standard** | **FIFO** |
|---|---|---|
| Throughput | Nearly unlimited | 300 TPS (3,000 with batching); much higher with high-throughput mode |
| Ordering | **Best effort** | **Strict, per `MessageGroupId`** |
| Delivery | **At least once** (duplicates possible) | **Exactly once processing** (deduplication within a 5-minute window) |
| Name | any | must end in **`.fifo`** |

**Key settings and behaviours:**
- **Message size** up to **256 KB**; for larger payloads store the body in S3 and send a pointer using the **SQS Extended Client Library**.
- **Retention** 1 minute to **14 days** (default 4 days).
- **Visibility timeout** (default 30 s, max **12 hours**) — after a consumer receives a message it becomes invisible to others. If the consumer doesn't delete it in time, it reappears and may be processed twice. Fix slow processing by increasing the timeout or calling **`ChangeMessageVisibility`** as a heartbeat, **and make consumers idempotent**.
- **Dead-letter queue (DLQ)** — after `maxReceiveCount` failed receives, the message moves to a DLQ so a "poison pill" cannot block the queue. Alarm on DLQ depth; use **DLQ redrive** to reprocess after a fix.
- **Long polling** (`ReceiveMessageWaitTimeSeconds` up to **20 s**) waits for messages instead of returning empty immediately — fewer API calls, lower cost, lower latency than short polling. Essentially always enable it.
- **Delay queues** (up to 15 minutes) and per-message timers.
- **Batching** (`SendMessageBatch`, up to 10 messages) reduces cost.
- Encryption with KMS; access controlled by IAM and a **queue resource policy**.

**Scaling consumers:** put workers in an ASG scaled on `ApproximateNumberOfMessagesVisible` or backlog-per-instance, or use **Lambda with an SQS event source mapping** (which scales concurrency automatically and supports batch size, batch window, and maximum concurrency settings).

### 4.2 Amazon SNS

A fully managed **push-based publish/subscribe** service. A publisher sends one message to a **topic**, and SNS delivers a copy to **every subscriber**.

- **Subscriber types:** SQS queues, Lambda functions, HTTP/HTTPS endpoints, email, SMS, mobile push (APNs/FCM), Kinesis Data Firehose, and AWS Event Fork Pipelines.
- **Fan-out pattern** — the canonical loose-coupling design: one event → an SNS topic → **multiple SQS queues**, each owned by a different consumer. Each consumer gets its own durable copy, retries independently, and has its own DLQ. If one consumer is down, its queue buffers.
- **Message filtering** — subscription filter policies evaluate message attributes (or body) so each subscriber receives only relevant messages.
- **FIFO topics** pair with FIFO queues for ordered fan-out.
- Supports **message archiving/replay**, delivery retries with backoff, and DLQs on subscriptions.

### 4.3 Amazon EventBridge

A **serverless event bus** that routes events based on their content.

- **Buses:** the default bus (AWS service events), **custom buses** (your applications), and **partner buses** (SaaS providers such as Zendesk, Datadog, Shopify).
- **Rules** match an **event pattern** (JSON matching on any field) and send the event to up to 5 **targets** — Lambda, SQS, SNS, Step Functions, ECS tasks, Kinesis, API destinations (external HTTP endpoints), another event bus, and more.
- **Schema registry and discovery** generate code bindings for event structures.
- **Archive and replay** — store events and replay them later, which is invaluable for recovery and testing.
- **EventBridge Scheduler** — a managed cron/rate scheduler at scale (replacing CloudWatch Events rules for scheduling).
- **EventBridge Pipes** — point-to-point integration with filtering and enrichment between a source and target.
- Cross-account and cross-Region event delivery.

**SNS vs EventBridge:** SNS is optimized for very high-throughput, low-latency fan-out and for mobile/SMS/email endpoints. EventBridge is optimized for **content-based routing, AWS and SaaS event sources, schedules, archive/replay, and many heterogeneous targets**. If the question mentions reacting to AWS service state changes, third-party SaaS events, or filtering on event content, choose **EventBridge**.

### 4.4 Amazon MQ

Managed **Apache ActiveMQ** and **RabbitMQ**. Choose it only when an existing application uses **industry-standard messaging protocols** — **AMQP, MQTT, STOMP, JMS, OpenWire** — and must be migrated without rewriting the messaging layer. For anything new, SQS/SNS are cheaper, simpler, and scale better.

### 4.5 AWS Step Functions

Serverless **workflow orchestration** using state machines defined in Amazon States Language.

- **State types:** Task (invoke Lambda, ECS, Batch, SNS, DynamoDB, and 200+ AWS APIs directly), **Choice** (branching), **Parallel**, **Map** (iterate over a collection, including distributed map for very large datasets), Wait, Pass, Succeed, Fail.
- **Built-in error handling:** `Retry` with exponential backoff and jitter, and `Catch` for fallback paths — this removes huge amounts of boilerplate code.
- **Callback pattern (`waitForTaskToken`)** pauses a workflow until an external system or a human responds — this is how approval steps are implemented.
- **Standard workflows:** up to **1 year** duration, **exactly-once** execution, full execution history, visual console. For long-running, auditable business processes.
- **Express workflows:** up to **5 minutes**, **at-least-once**, very high event rate, much cheaper. For streaming ingestion and high-volume short tasks.

**Exam cue:** "coordinate multiple Lambda functions," "retry logic and error handling without writing code," "visualize the process," "a human approval step" → **Step Functions**.

### 4.6 Choosing the right integration service

| Need | Service |
|---|---|
| Buffer work, decouple producer/consumer speeds | **SQS** |
| One event to many independent subscribers | **SNS** (often → SQS queues) |
| Strict ordering and no duplicates | **SQS FIFO** |
| Route by event content; AWS/SaaS events; schedules; replay | **EventBridge** |
| Orchestrate a multi-step process with state | **Step Functions** |
| Keep an existing JMS/AMQP application | **Amazon MQ** |
| High-volume ordered stream with replay and multiple readers | **Kinesis Data Streams** |
| GraphQL API with real-time subscriptions | **AWS AppSync** |

---

## 5. Amazon API Gateway

### 5.1 API types

| | **REST API** | **HTTP API** | **WebSocket API** |
|---|---|---|---|
| Cost | Higher | **Up to ~71% cheaper** | Per message/connection |
| Latency | Low | **Lower** | — |
| Features | Full set: request/response transformation (VTL), **caching**, **API keys and usage plans**, request validation, WAF, private endpoints, canary deployments, AWS X-Ray | Core proxying, **JWT authorizers**, CORS, simpler config | Bidirectional, persistent connections |
| Use | Feature-rich public APIs, legacy integrations | Simple, low-latency proxies to Lambda/HTTP | Chat, live dashboards, notifications |

### 5.2 Key capabilities

- **Integrations:** Lambda (proxy and non-proxy), any HTTP backend, **direct AWS service integrations** (put straight into SQS, Kinesis, DynamoDB, or Step Functions without a Lambda "glue" function), private integrations to an NLB/ALB via VPC Link.
- **Authorization:** IAM (SigV4), Cognito user pool authorizer, **Lambda authorizer** (token or request based, with result caching), resource policies, and **mTLS**.
- **API keys + usage plans** provide **throttling and quotas per client** — note they are a metering and rate-limiting tool, **not authentication**.
- **Throttling:** account-level default ~10,000 requests/second with a 5,000 burst, plus per-stage and per-method limits. Requests beyond the limit receive **429 Too Many Requests**.
- **Caching:** 0.5 GB to 237 GB per stage, TTL up to 1 hour (default 300 s), with per-method cache settings and cache invalidation headers. Reduces backend load and latency.
- **Stages and canary releases:** deploy to `dev`/`prod` stages; a canary sends a percentage of traffic to a new deployment.
- **Private APIs** are reachable only through **interface VPC endpoints**, controlled by a resource policy.
- **Timeout:** the integration timeout is **29 seconds** (treat this as the exam number). Anything longer must be asynchronous — return `202 Accepted` and process via SQS/Step Functions, with the client polling or receiving a notification.

---

## 6. Serverless and Containers

### 6.1 AWS Lambda

**Execution model:** an event triggers a function; AWS provisions an execution environment, runs your handler, and keeps the environment warm for a while to serve subsequent invocations.

**Limits to memorize:**
- **Timeout: 15 minutes maximum**
- **Memory: 128 MB to 10,240 MB**, and **CPU scales proportionally with memory** (at ~1,769 MB you get one full vCPU) — so increasing memory often *reduces* cost by finishing faster
- **`/tmp` ephemeral storage: 512 MB to 10 GB**
- **Payload:** 6 MB synchronous, 256 KB asynchronous
- **Deployment package:** 50 MB zipped / 250 MB unzipped, or a **10 GB container image**
- **Default concurrency: 1,000 per account per Region** (soft limit)

**Concurrency controls:**
- **Reserved concurrency** — guarantees a function a share of the account limit and simultaneously **caps** it (useful to protect a downstream database from being overwhelmed).
- **Provisioned concurrency** — keeps a specified number of environments initialized and warm, eliminating **cold starts** for latency-sensitive APIs. Can be auto-scaled.
- **SnapStart** (Java) — snapshots the initialized runtime so cold starts drop dramatically at no extra cost.

**Networking:** a Lambda function attached to a VPC gets ENIs in your subnets and can reach private resources (RDS, ElastiCache). To reach the internet or public AWS endpoints it needs a **NAT gateway** or **VPC interface endpoints**. Functions not in a VPC use AWS-managed networking and have internet access by default.

**Good fits:** event processing (S3, DynamoDB Streams, Kinesis, SNS/SQS), API backends, scheduled tasks, lightweight ETL, glue between services, infrequent or spiky workloads.
**Poor fits:** jobs longer than 15 minutes, sustained high-CPU workloads (cheaper on EC2/Fargate), applications needing persistent connections or very large local state, and workloads requiring specific OS/kernel control.

### 6.2 Containers on AWS

- **Amazon ECS** — AWS's own orchestrator. Concepts: **task definition** (the blueprint: image, CPU/memory, ports, IAM role, logging), **task** (a running instance of it), **service** (maintains N tasks and integrates with an ALB), **cluster**. Launch types:
  - **EC2** — you own and pay for the instances; more control, supports GPU/special instance types, can use **Spot** and bin-packing for cost efficiency.
  - **Fargate** — serverless; you specify vCPU/memory per task and AWS runs it; no instances to patch or scale.
- **Amazon EKS** — managed Kubernetes control plane. Choose when you need Kubernetes APIs, Helm, operators, or portability between clouds/on-prem. Nodes can be self-managed, managed node groups, **Karpenter**-provisioned, or **Fargate profiles**.
- **AWS Fargate** — the serverless compute engine behind ECS/EKS; billed per vCPU-second and GB-second with a 1-minute minimum. **Fargate Spot** offers up to 70% savings for interruption-tolerant tasks.
- **Amazon ECR** — private registry with image scanning (basic and enhanced via Inspector), lifecycle policies, immutable tags, and cross-Region replication.
- **AWS App Runner** — point it at a container image or source repository and get a scaled, load-balanced HTTPS service with the least configuration of any option.

**Security in containers:** use **task roles** (per task, least privilege) rather than instance roles; use the **`awsvpc` network mode** so each task gets its own ENI and security group; pull secrets from Secrets Manager via the task definition; scan images in ECR.

**Migrating to containers:** **AWS App2Container** converts existing Java and .NET applications into container images with generated ECS/EKS deployment artifacts. For pure lift-and-shift to EC2, **AWS Application Migration Service (MGN)** is the tool.

### 6.3 Choosing compute

| Requirement | Choice |
|---|---|
| Event-driven, short, spiky, no servers | **Lambda** |
| Containerized services, no capacity management | **ECS/EKS on Fargate** |
| Containers with GPUs, special instances, or lowest cost at scale | **ECS/EKS on EC2 (+ Spot)** |
| Kubernetes ecosystem or hybrid portability required | **EKS** |
| Batch jobs with queueing and dependencies | **AWS Batch** |
| Full OS control, legacy software, licensing | **EC2** |
| Simplest path from code/image to a running web service | **App Runner / Elastic Beanstalk** |

---

## 7. Multi-Tier and Microservice Patterns

### 7.1 Classic three-tier web architecture

```
Route 53  →  CloudFront (+ WAF)  →  ALB (public subnets, 2–3 AZs)
                                      ↓
                        Auto Scaling group of app servers (private subnets)
                                      ↓
      RDS Multi-AZ / Aurora (private DB subnets)  +  ElastiCache  +  S3
```
Static assets live in S3 behind CloudFront; sessions live in ElastiCache or DynamoDB; secrets in Secrets Manager; outbound access via NAT gateways; AWS service access via VPC endpoints.

### 7.2 Event-driven serverless architecture

```
Client → API Gateway → Lambda → SQS → worker (Lambda/Fargate) → DynamoDB
                          ↓
                    EventBridge → other services
                          ↓
                 Step Functions (orchestration)
```
Characteristics: no servers, pay-per-use, each stage scales independently, failures isolated by queues and DLQs.

### 7.3 Microservice design principles

- **Single responsibility** and **independent deployability**
- **A data store per service** — no shared database tables between services
- **Stateless services** so they scale horizontally
- **Asynchronous communication** wherever a synchronous response is not strictly needed
- **Idempotent consumers** — because at-least-once delivery means duplicates will happen
- **Retries with exponential backoff and jitter**, plus **circuit breakers** so a failing dependency doesn't exhaust your threads
- **Graceful degradation** — serve cached or partial results rather than failing entirely
- **Service discovery** — **AWS Cloud Map** / **ECS Service Connect**, or an ALB per service
- **Observability** — structured logs, metrics, and **X-Ray** tracing across service boundaries

### 7.4 The "fan-out + buffer" pattern (worth memorizing)

S3 upload → **SNS topic** → three **SQS queues** → three independent consumers (thumbnailer, indexer, notifier). Each consumer scales on its own queue depth, retries independently, and has its own DLQ. This single diagram answers a surprising number of exam questions.

---

## 8. Caching and Edge Acceleration

### 8.1 Layers of caching

| Layer | Service / technique | Typical gain |
|---|---|---|
| Browser/client | `Cache-Control`, ETags | Eliminates requests entirely |
| Edge CDN | **CloudFront** (static + dynamic, Origin Shield) | Latency and origin offload |
| API | **API Gateway cache** | Fewer backend invocations |
| Application / session / query | **ElastiCache (Redis/Valkey or Memcached)** | Microsecond reads |
| NoSQL | **DynamoDB DAX** | Microsecond reads, reduced RCU |
| Relational read scaling | **Read replicas** | Offloads the primary |
| DNS | Route 53 TTL | Fewer lookups |

### 8.2 Caching strategies

- **Lazy loading (cache-aside)** — on a miss, read from the database and populate the cache. Only requested data is cached, and a cache failure is survivable. Downsides: a cache miss costs three round trips, and data can become stale.
- **Write-through** — write to the cache on every database write. Data is always fresh and reads are fast, but writes are slower and the cache fills with data that may never be read.
- **TTL-based expiry** — bound staleness; usually combined with the strategies above.
- Typical production answer: **lazy loading + write-through for hot keys + TTL**.

### 8.3 Read replicas

Use when the workload is **read-heavy**, for reporting/analytics offload, or to provide low-latency reads in another Region. Replication is **asynchronous**, so replicas are **eventually consistent** — never use them when the application requires read-after-write consistency. RDS supports up to 5 replicas per source; **Aurora supports 15** with typically sub-10 ms lag. Replicas can be **promoted** to standalone databases (a manual DR action).

### 8.4 Edge acceleration

- **Amazon CloudFront** — caches at 600+ points of presence, terminates TLS at the edge, supports **Origin Shield** (an extra regional caching layer), origin failover groups, signed URLs/cookies, field-level encryption, and edge compute (**CloudFront Functions** for light header/URL work, **Lambda@Edge** for heavier logic).
- **AWS Global Accelerator** — two **static anycast IP addresses**; client traffic enters the AWS backbone at the nearest edge and is routed to the healthiest endpoint, with **failover in seconds independent of DNS TTLs**. Supports **TCP and UDP**, so it is the choice for gaming, VoIP, MQTT/IoT, and any non-HTTP protocol, or when clients cache DNS badly.

---

## 9. Storage Types in Scalable Designs

| Type | Services | Characteristics | Typical use |
|---|---|---|---|
| **Object** | S3, S3 Glacier | Flat namespace, HTTP API, virtually unlimited, rich metadata, no partial in-place update | Static assets, data lake, backups, media, logs |
| **File** | EFS (NFS/Linux), FSx for Windows (SMB), FSx for Lustre (HPC), FSx ONTAP/OpenZFS | Shared, concurrent access with POSIX/SMB semantics | Shared content, home directories, lift-and-shift, HPC |
| **Block** | EBS (single AZ; Multi-Attach on io1/io2), Instance store (ephemeral) | Raw devices, lowest latency, filesystem on top | Boot volumes, databases, transactional workloads |

Design rule: **put shared state in S3 or EFS, never on an instance's local disk**, so the fleet can scale and instances remain disposable.

---

## 10. Worked Scenarios

**Scenario 1 — "Traffic spikes overwhelm our order-processing backend and requests are dropped."**
Insert an **SQS queue** between the web tier and the workers; scale workers with an ASG on **queue depth**; add a **DLQ**; make processing idempotent. The web tier now returns quickly and nothing is lost.

**Scenario 2 — "Each uploaded file must trigger virus scanning, thumbnailing, and an audit record, independently."**
S3 event → **SNS** → three **SQS** queues → three consumers. Independent scaling, retries, and DLQs.

**Scenario 3 — "Users are logged out whenever we scale in."**
Session state is on local disks. Move it to **ElastiCache for Redis** (or DynamoDB). If the app cannot be changed, enable **ALB sticky sessions** as a stopgap.

**Scenario 4 — "A nightly report job takes 45 minutes and is invoked through API Gateway."**
API Gateway cannot wait (29 s) and Lambda cannot run 45 minutes. Have the API push a job to **SQS** or start a **Step Functions** execution, return **202 Accepted**, and run the work on **Fargate/EC2/AWS Batch**, notifying via SNS on completion.

**Scenario 5 — "We need strict per-customer ordering with no duplicate charges."**
**SQS FIFO** with `MessageGroupId` = customer ID, plus a deduplication ID, plus idempotent consumers.

**Scenario 6 — "Our monolith's single ALB serves ten services and deployments are risky."**
Split into microservices with **ALB path-based routing** to separate target groups, deploy each independently, and use **weighted target groups** for canary releases.

**Scenario 7 — "Backend database is overloaded by repeated identical queries."**
Add **ElastiCache** with lazy loading plus TTL; add **read replicas** for remaining read load; consider **API Gateway caching** and **CloudFront** for the response layer.

---

## 11. Quick Decision Table

| Scenario | Answer |
|---|---|
| Spiky traffic overwhelms a backend | **SQS buffer + ASG on queue depth** |
| One event, several independent consumers | **SNS fan-out to SQS queues** |
| Strict ordering, exactly-once | **SQS FIFO** |
| Route events by content, AWS/SaaS sources, replay | **EventBridge** |
| Multi-step process with retries and approvals | **Step Functions** |
| Migrate a JMS/AMQP application unchanged | **Amazon MQ** |
| Serverless REST API with throttling and auth | **API Gateway + Lambda** |
| Poison-pill messages block the queue | **Dead-letter queue** |
| Messages processed twice | Raise **visibility timeout**, heartbeat, make consumers **idempotent** |
| Empty receives cost too much | **Long polling (20 s)** |
| Session state in a scaled fleet | **ElastiCache for Redis / DynamoDB** |
| Legacy app that cannot be made stateless | **ALB sticky sessions** |
| Route `/api` and `/static` to different services | **ALB path-based routing** |
| Static IP, UDP, or extreme TCP performance | **NLB** |
| Insert a third-party firewall appliance | **Gateway Load Balancer** |
| Global low-latency HTTP content | **CloudFront** |
| Global non-HTTP with instant failover | **Global Accelerator** |
| Scale based on queue backlog | ASG on **ApproximateNumberOfMessagesVisible** |
| Scale on memory | **CloudWatch agent custom metric** |
| App-level failures not detected by the ASG | Set health check type to **ELB** |
| Roll out a new AMI safely | **Instance refresh** |
| Long instance boot times slow scale-out | **Warm pools** (or predictive scaling) |
| Eliminate Lambda cold starts | **Provisioned concurrency / SnapStart** |
| Containers with zero infrastructure management | **Fargate** |

---

## Task 2.2 — Design Highly Available and/or Fault-Tolerant Architectures

> This task is about **surviving failure**: of an instance, an Availability Zone, a Region, or a dependency. You must be able to map a stated **RTO/RPO and budget** to the right architecture, and to spot single points of failure in a described design.

---

## 1. Core Definitions

| Term | Meaning | Example |
|---|---|---|
| **High availability (HA)** | The system remains available through component failure, possibly with a brief interruption | RDS Multi-AZ failing over in 60–120 seconds |
| **Fault tolerance (FT)** | The system continues operating with **no interruption** and no loss of capability | Active-active across three AZs with capacity headroom |
| **Disaster recovery (DR)** | The ability to recover from a large-scale event, typically Regional | Failing over to a second Region |
| **RTO (Recovery Time Objective)** | Maximum acceptable **downtime** | "We can be down 15 minutes" |
| **RPO (Recovery Point Objective)** | Maximum acceptable **data loss**, measured in time | "We can lose at most 5 minutes of transactions" |
| **Durability** | Probability the data survives (S3: 99.999999999%) | Data is not lost |
| **Availability** | Probability the service is reachable (S3 Standard: 99.99%) | Data can be retrieved right now |
| **MTTR / MTBF** | Mean time to repair / between failures | Used to reason about component reliability |

**Important nuance:** durability and availability are different. Data can be perfectly durable but temporarily unavailable. Backups protect durability; Multi-AZ protects availability.

**Availability maths:** components in series multiply their availability (two 99.9% components in series ≈ 99.8%); redundant components in parallel dramatically improve it (two 99% components in parallel ≈ 99.99%). This is why removing single points of failure matters more than making any one component better.

---

## 2. Identifying and Removing Single Points of Failure

A **single point of failure (SPOF)** is any component whose loss takes down the system. Scan every architecture diagram for them.

| SPOF | Remedy |
|---|---|
| One EC2 instance | **Auto Scaling group with min ≥ 2 across ≥ 2 AZs behind an ELB** |
| All resources in one AZ | Subnets and resources in **2–3 AZs** |
| Single NAT gateway | **One NAT gateway per AZ**, AZ-local routes |
| Single database instance | **RDS Multi-AZ** or **Aurora** (6 copies / 3 AZs) |
| Database is also the read workload | **Read replicas** |
| Single Region | Cross-Region replication, **Route 53 failover**, Aurora Global Database, DynamoDB global tables |
| Session state on instance disk | **ElastiCache / DynamoDB** |
| Files on instance disk | **S3 / EFS** |
| One Direct Connect link | **Two DX connections at two locations**, or **DX + VPN backup** |
| One internet connection on-prem | Redundant ISPs or VPN over a second path |
| Manual, hand-built servers | **Infrastructure as code + immutable AMIs** |
| A single monolithic deployment | Decouple into independently deployable services |
| One administrator with the only credentials | Federated access, break-glass procedure |
| Hard-coded IPs and endpoints | DNS, service discovery, load balancer endpoints |

---

## 3. Compute and Infrastructure Resilience

### 3.1 Multi-AZ with Auto Scaling and ELB

The foundational HA pattern:
- An **ALB/NLB** with subnets in at least two (preferably three) AZs
- An **Auto Scaling group** whose subnets span those AZs, with `min` at least equal to the number of AZs so the loss of one AZ leaves capacity
- **`HealthCheckType = ELB`** so application-level failures cause replacement
- Enough headroom (the **"N+1" rule**) that losing one AZ's capacity doesn't overload the rest — with three AZs you need ~50% spare per AZ to survive one AZ loss without degradation

### 3.2 Instance-level recovery

- **EC2 Auto Recovery** — a CloudWatch alarm on `StatusCheckFailed_System` triggers recovery, which migrates the instance to new underlying hardware **keeping the same instance ID, private IP, Elastic IP, and EBS volumes**. Useful for single-instance legacy workloads that cannot be clustered. (Modern instance types have this built in by default.)
- **ASG replacement** — the ASG terminates and launches a fresh instance; the IP changes, so the workload must be stateless or behind a load balancer.
- **EC2 hibernation** preserves RAM state to the root EBS volume — a cost/startup optimization rather than an HA feature.

### 3.3 Placement groups

| Strategy | Behaviour | Effect on resilience |
|---|---|---|
| **Cluster** | Packs instances close together in **one AZ** for lowest latency and highest throughput | **Reduces** resilience — one AZ, correlated hardware |
| **Spread** | Places each instance on **distinct underlying hardware** (racks); max **7 instances per AZ per group** | **Maximizes** resilience for a small set of critical instances |
| **Partition** | Divides instances into partitions, each on a separate rack set; up to 7 partitions per AZ | For large distributed systems (HDFS, Cassandra, Kafka) that are rack-aware |

### 3.4 Immutable infrastructure and deployments

**Immutable infrastructure** means servers are never modified after deployment. To change anything — a patch, a config value, a new application version — you build a **new AMI or container image** and replace the instances.

Benefits: no configuration drift, every environment is reproducible, rollback is simply redeploying the previous image, and testing is meaningful because what you tested is exactly what runs.

Tooling: **EC2 Image Builder** (automated golden AMI pipelines with testing), **CloudFormation/CDK/Terraform** for the infrastructure, **Systems Manager Patch Manager** and **State Manager** for compliance on longer-lived fleets, **AWS Config** for drift detection and automatic remediation.

**Deployment strategies:**

| Strategy | How it works | Trade-off |
|---|---|---|
| **In-place / rolling** | Replace instances in batches | Cheapest; mixed versions live simultaneously |
| **Rolling with additional batch** | Add capacity first, then roll | Maintains full capacity; slightly more cost |
| **Immutable** | Launch a whole new ASG, then switch | Safest in-place option; brief double capacity |
| **Blue/green** | Stand up a complete parallel environment and shift traffic (Route 53 weighted records, ALB target group swap, or CodeDeploy) | Instant rollback; doubles cost during cutover |
| **Canary** | Send a small percentage of traffic to the new version, then ramp | Limits blast radius; needs good metrics |

---

## 4. Data Resilience

### 4.1 Amazon S3

- **99.999999999% durability** and data stored redundantly across **at least three AZs** (except **One Zone-IA** and **Express One Zone**, which use a single AZ).
- **Strong read-after-write consistency** for all operations.
- **Versioning** protects against overwrite and deletion (a delete creates a delete marker).
- **Replication** — SRR and CRR — for DR, latency, and compliance. Requires versioning on both ends; **only replicates objects written after it is enabled** (use **Batch Replication** for existing objects); **RTC** provides a 15-minute SLA.
- **Object Lock** for immutability; **MFA Delete** for extra protection.

### 4.2 Amazon EBS

- An EBS volume is **replicated within a single Availability Zone only**. It is not multi-AZ. If the AZ fails, the volume is unavailable.
- Resilience comes from **snapshots**, which are incremental and stored durably (in S3, in an AWS-managed account), and can be **copied cross-Region and cross-account**.
- Automate with **Amazon Data Lifecycle Manager** or **AWS Backup**; speed up restores with **Fast Snapshot Restore**; protect against accidental deletion with **Recycle Bin**.

### 4.3 Amazon RDS

**Multi-AZ instance deployment:**
- A **synchronous standby replica** in a different AZ. Data is written to both before the write is acknowledged, so **RPO is effectively zero**.
- Failover is **automatic** (typically **60–120 seconds**) and works by changing the DNS CNAME of the endpoint — the application reconnects to the same endpoint name.
- Triggered by AZ failure, instance failure, storage failure, network issues, or an instance class change / OS patching.
- **The standby does not serve reads.** It exists purely for availability. Backups and maintenance are performed on the standby, reducing impact on the primary.

**Multi-AZ DB cluster deployment** (MySQL/PostgreSQL): one writer plus **two readable standbys** in different AZs, semi-synchronous replication, and faster failover (typically **under 35 seconds**).

**Read replicas:**
- **Asynchronous**, so there is replication lag and eventual consistency.
- Up to **5 per source**, can be in the same AZ, another AZ, or **another Region**.
- Can be **promoted** to a standalone writable instance — a manual DR mechanism with an RPO equal to the replication lag.
- Replicas serve read traffic; combining Multi-AZ (availability) with read replicas (performance) is common.

**Backups:** automated backups with **1–35 days** retention enable **point-in-time recovery** (restore to any second in the window, typically to within ~5 minutes of now); manual snapshots persist indefinitely; **cross-Region automated backup replication** for DR.

### 4.4 Amazon Aurora

- The storage layer keeps **six copies of your data across three Availability Zones** and is self-healing (continuously scanning for and repairing errors). Aurora can tolerate the loss of **two copies without affecting writes** and **three copies without affecting reads**.
- Storage grows automatically in 10 GB increments up to **128 TiB** and is shared by all instances in the cluster.
- Up to **15 Aurora Replicas**, replica lag typically **under 10 ms**. On primary failure Aurora **fails over to a replica, usually in under 30 seconds**, using failover priority tiers. With no replica, Aurora recreates the primary (slower).
- **Endpoints:** writer (cluster) endpoint, **reader endpoint** (load-balances across replicas), custom endpoints, and instance endpoints.
- **Aurora Global Database** — one primary Region plus up to **five secondary Regions**, replicated at the storage layer with typical lag **under one second**. Provides **RPO ≈ 1 second and RTO under 1 minute** for cross-Region failover, plus local low-latency reads. This is the standard answer for global relational DR.
- **Backtrack** (Aurora MySQL) rewinds the cluster in place to a prior point in seconds, without restoring a snapshot — excellent for undoing a bad deployment or an accidental `DELETE`.
- **Fast database cloning** creates a copy-on-write clone in minutes for testing.

### 4.5 Amazon DynamoDB

- Data is automatically replicated across **three Availability Zones** in a Region; there is no "enable Multi-AZ" option.
- **Global tables** provide multi-Region, **multi-active** replication with last-writer-wins conflict resolution — read and write in any Region, with typically sub-second replication.
- **Point-in-time recovery** gives continuous backups with restore to any second in the last **35 days**; **on-demand backups** are retained until deleted.
- **DynamoDB Streams** can feed cross-Region or cross-system replication and event-driven recovery logic.

### 4.6 EFS and FSx

- **EFS Standard** stores data redundantly across multiple AZs in the Region; **EFS One Zone** is cheaper but single-AZ. **EFS Replication** maintains a cross-Region copy with an RPO measured in minutes.
- **FSx for Windows File Server** offers a **Multi-AZ** deployment with automatic failover; **FSx for Lustre** persists durability by linking to an S3 bucket as the system of record (scratch file systems are explicitly non-replicated).

---

## 5. Route 53, Health Checks and Failover

### 5.1 Health checks

Route 53 supports three types:
- **Endpoint health checks** — Route 53 checkers around the world probe an IP or domain over HTTP/HTTPS/TCP, optionally matching a string in the response body.
- **Calculated health checks** — combine multiple child checks with AND/OR/NOT logic ("healthy if at least 2 of 3 children are healthy").
- **CloudWatch alarm health checks** — treat an alarm state as health, which lets you base DNS failover on any metric (including private resources Route 53 cannot reach directly).

Health checks can also send **SNS notifications** and are what make failover routing work.

### 5.2 Routing policies

| Policy | Behaviour | Typical use |
|---|---|---|
| **Simple** | One record, no health checks | Single resource |
| **Weighted** | Split traffic by assigned weights | Blue/green, canary, gradual migration, A/B testing |
| **Latency-based** | Route to the Region with the lowest measured latency for that client | Global performance |
| **Failover** | Primary record used while healthy; otherwise the secondary | **Active-passive DR** |
| **Geolocation** | Route by the user's country/continent | Compliance, localization, licensing |
| **Geoproximity** | Route by geographic distance, adjustable with a **bias** | Shifting load between Regions gradually |
| **Multivalue answer** | Returns up to **8 healthy records** at random | Simple client-side load balancing with health awareness |
| **IP-based** | Route by the client's CIDR block | ISP-specific optimizations |

### 5.3 Alias records and TTL

- **Alias records** point to AWS resources (ALB/NLB, CloudFront, S3 website endpoints, API Gateway, Global Accelerator, another Route 53 record). They are **free to query**, can be used at the **zone apex** (`example.com`), and automatically track the target's IP changes. A **CNAME cannot be used at the zone apex**.
- **TTL** governs how long resolvers cache a record. Lower TTLs (60 seconds or less) make DNS failover faster but increase query volume. Note that many clients and some JVMs cache DNS beyond the TTL, which is exactly why **Global Accelerator** (which fails over at the network layer) is preferred when seconds matter.

### 5.4 Global Accelerator vs CloudFront for availability

- **Global Accelerator** provides two **static anycast IPs**, routes traffic into the AWS backbone at the nearest edge, continuously health-checks endpoints, and **fails over within seconds without any DNS change**. It supports **TCP and UDP** and any protocol. Use it for gaming, VoIP, IoT, financial feeds, or when clients cache DNS.
- **CloudFront** is an HTTP/S CDN. It improves availability by caching (serving from cache during origin problems), supports **origin groups** for automatic origin failover, and absorbs DDoS at the edge.

---

## 6. Disaster Recovery Strategies

The four strategies, in increasing cost and decreasing RTO/RPO:

| Strategy | RPO | RTO | What is running in the DR Region | Relative cost |
|---|---|---|---|---|
| **Backup & restore** | Hours | **Hours to a day** | Nothing but backups/snapshots | **$** |
| **Pilot light** | Minutes | **Tens of minutes** | Core data continuously replicated (e.g., a database replica); servers configured but **switched off / not provisioned** | **$$** |
| **Warm standby** | Seconds–minutes | **Minutes** | A **fully functional but scaled-down** copy of the whole stack, always running | **$$$** |
| **Multi-site active/active** | Near zero | **Near zero** | Full production capacity live in both Regions, serving traffic | **$$$$** |

### 6.1 Backup and restore
Take regular backups (AWS Backup, snapshots, S3 CRR) and copy them to the DR Region. After a disaster, rebuild infrastructure from **infrastructure as code** and restore data. Cheapest, slowest. Suitable for non-critical workloads and for the long tail of systems.

### 6.2 Pilot light
The "always-on" part is the **data**: a cross-Region read replica, DynamoDB global table, or continuously replicated storage. Application servers exist as AMIs/templates but are not running. On failover you scale up compute, promote the database, and repoint DNS. Significantly faster than restore, much cheaper than warm standby.

### 6.3 Warm standby
A complete, smaller copy of production runs continuously in the DR Region — perhaps one instance per tier rather than ten. It can serve traffic immediately (possibly degraded) and is scaled up during failover. The key advantage over pilot light is that the system is already *proven working*.

### 6.4 Multi-site active/active
Both Regions serve live traffic (Route 53 latency or weighted routing, or Global Accelerator). Requires multi-Region data strategies such as **DynamoDB global tables** or **Aurora Global Database** (with write forwarding) and careful handling of conflicts, idempotency, and consistency. Highest cost and complexity, near-zero RTO/RPO.

### 6.5 Supporting services

- **AWS Elastic Disaster Recovery (AWS DRS)** — continuous **block-level replication** of on-premises or cloud servers into a low-cost staging area in AWS; launches fully provisioned instances on failover. RPO in **seconds**, RTO in **minutes**. The answer for "replicate physical/virtual servers for DR without re-architecting."
- **AWS Backup** — cross-Region and cross-account copies, Vault Lock, organization policies.
- **AWS Application Migration Service (MGN)** — the equivalent tool for migrations.
- **CloudFormation / CDK / Terraform** — recreate the environment deterministically, which is what makes backup-and-restore and pilot light viable.
- **AWS Resilience Hub** — assess an application against defined RTO/RPO targets, score it, and get remediation recommendations.
- **AWS Fault Injection Service (FIS)** — run controlled chaos experiments (terminate instances, inject latency, fail an AZ) to validate that the design really is resilient.

### 6.6 The service-quota trap
Service quotas are **per account, per Region**. A DR Region that has never run production may have **default limits** far below what a failover requires — EC2 vCPU limits, Elastic IPs, NAT gateways, RDS instances. **Raise quotas in the DR Region in advance** and periodically test. This is a favourite exam detail.

---

## 7. Resilience Patterns

- **Retry with exponential backoff and jitter** — naive immediate retries create a thundering herd that prolongs an outage. AWS SDKs implement this by default; the jitter is what prevents synchronized retry storms.
- **Circuit breaker** — after N consecutive failures, stop calling the dependency for a cooldown period and fail fast (or serve a degraded response), protecting both systems.
- **Timeouts everywhere** — an unbounded wait consumes threads and cascades failure.
- **Bulkheads** — isolate resources per dependency (separate connection pools, separate queues) so one failing dependency cannot exhaust everything.
- **Idempotency** — essential because retries and at-least-once delivery guarantee duplicates.
- **Graceful degradation** — serve cached, partial, or default content rather than an error (e.g., hide the recommendations widget if that service is down).
- **Static stability** — design the failover path so it does **not** require control-plane calls during the event. Pre-provision capacity in all AZs rather than relying on launching new instances mid-incident, because control planes are the most likely thing to be stressed during a large failure.
- **Shuffle sharding** — assign each customer a random subset of workers so one abusive customer cannot affect everyone.
- **Throttling and load shedding** — protect the backend with API Gateway throttling, WAF rate rules, SQS buffering, and reserved concurrency so overload degrades gracefully instead of collapsing.

---

## 8. Making Legacy and Unmodifiable Applications Resilient

The exam frequently constrains you with "the application cannot be modified."

| Legacy constraint | AWS remedy |
|---|---|
| Stores sessions in local memory | **ALB sticky sessions** |
| Writes to a local file path shared by all nodes | **Amazon EFS** (Linux) or **FSx for Windows** (SMB) |
| Hard-coded to a fixed IP address | **NLB with an Elastic IP per AZ**, or **Global Accelerator** static IPs |
| Single server that cannot be clustered | **ASG with min=max=1 across multiple AZs** + EBS/EFS for data, or **EC2 Auto Recovery** |
| Opens far too many database connections | **Amazon RDS Proxy** |
| Depends on a Windows file server | **FSx for Windows File Server** (Multi-AZ) or **Storage Gateway** |
| Uses a specific message broker protocol | **Amazon MQ** |
| Needs a licensed appliance in the path | **Gateway Load Balancer** |
| Cannot handle DB failover gracefully | **RDS Proxy** (reduces failover time by up to 66% and holds client connections during failover) |

**Amazon RDS Proxy in detail:** a fully managed, highly available connection pool that sits between your application and RDS/Aurora. It multiplexes many application connections onto fewer database connections (solving Lambda and container "connection storms"), **reduces failover time by up to 66%** by preserving client connections while re-pointing to the new writer, and supports **IAM authentication** and credential retrieval from **Secrets Manager**.

---

## 9. Observability for Resilience

- **Amazon CloudWatch**
  - **Metrics** — 5-minute basic monitoring, 1-minute detailed monitoring, 1-second **high-resolution** custom metrics. Memory and disk usage require the **CloudWatch agent**.
  - **Alarms** — on metrics, with actions (SNS, Auto Scaling, EC2 recovery). **Composite alarms** reduce noise by combining conditions.
  - **Logs** — centralized logging, **metric filters** to turn log patterns into metrics, **Logs Insights** for queries, subscription filters to stream to Kinesis/Lambda.
  - **Synthetics canaries** — scripted probes that test endpoints and user flows from outside, catching failures before users report them.
  - **RUM** and **Evidently** for real-user monitoring and feature experiments.
  - **Dashboards** and **ServiceLens** for a unified view.
- **AWS X-Ray** — distributed tracing producing a **service map** with latency distributions and error rates per node, so you can identify which microservice is the bottleneck or failing.
- **AWS CloudTrail** — the audit record of API activity, essential for post-incident analysis.
- **AWS Health Dashboard** — AWS-side events affecting your specific resources (plus the public Service Health Dashboard).
- **AWS Resilience Hub** — continuous assessment against RTO/RPO goals.
- **Key metrics to alarm on:** `HealthyHostCount` and `UnHealthyHostCount` (ELB), `TargetResponseTime`, `HTTPCode_ELB_5XX_Count`, `ApproximateAgeOfOldestMessage` (SQS — a superb early warning), DLQ depth, `DatabaseConnections`, replica lag, Lambda `Throttles` and `Errors`, and service quota utilization.

---

## 10. Worked Scenarios

**Scenario 1 — "Single-AZ RDS must survive AZ failure, no application changes allowed."**
Enable **Multi-AZ**. The endpoint name stays the same; failover is automatic via DNS. A read replica would require manual promotion and an endpoint change.

**Scenario 2 — "RPO of about one second and RTO under a minute for a MySQL-compatible database, across Regions."**
**Aurora Global Database.** Cross-Region read replicas have higher and less predictable lag plus manual promotion.

**Scenario 3 — "Lowest-cost DR; the business tolerates several hours of downtime."**
**Backup and restore** — AWS Backup with cross-Region copies, infrastructure defined in CloudFormation, documented and tested restore runbook.

**Scenario 4 — "We need to fail over in minutes but cannot afford a full second environment."**
**Warm standby** (scaled-down full stack) or **pilot light** if only the data must stay live. Pair with Route 53 failover routing and pre-raised service quotas.

**Scenario 5 — "Instances are marked healthy but the application is hung."**
Change the ASG **health check type to ELB** and ensure the target group health check hits a meaningful application endpoint (not just `/`), so hung instances are replaced.

**Scenario 6 — "A UDP-based service must fail over between Regions in seconds."**
**AWS Global Accelerator** — DNS-based failover is too slow and CloudFront does not support UDP.

**Scenario 7 — "Thousands of Lambda functions exhaust the Aurora connection limit during spikes."**
**Amazon RDS Proxy** in front of the cluster, with credentials in Secrets Manager.

**Scenario 8 — "Seven critical instances must never share underlying hardware."**
A **spread placement group** (maximum 7 instances per AZ per group), spread across AZs.

**Scenario 9 — "We must prove our DR plan works."**
Use **AWS Resilience Hub** to assess against RTO/RPO, run **AWS FIS** experiments (AZ failure, instance termination, API latency), and schedule regular game days with **AWS Backup restore testing**.

---

## 11. Quick Decision Table

| Requirement | Answer |
|---|---|
| Survive AZ failure, relational database | **RDS Multi-AZ** |
| Offload read traffic | **Read replicas** |
| Fastest relational failover in-Region | **Multi-AZ DB cluster** or **Aurora** |
| Cross-Region relational DR, RPO ~1 s | **Aurora Global Database** |
| Undo a bad write in Aurora MySQL in seconds | **Backtrack** |
| Multi-Region active-active NoSQL | **DynamoDB global tables** |
| Restore DynamoDB to any second in 35 days | **Point-in-time recovery** |
| Lowest-cost DR, hours acceptable | **Backup & restore** |
| Data live, servers off until needed | **Pilot light** |
| Scaled-down live environment | **Warm standby** |
| Zero downtime, both Regions serving | **Multi-site active/active** |
| Continuous replication of on-prem servers | **AWS Elastic Disaster Recovery** |
| Centralized cross-account, cross-Region backups | **AWS Backup** |
| DNS failover to a standby Region | **Route 53 failover routing + health checks** |
| Static IPs and sub-minute failover for TCP/UDP | **AWS Global Accelerator** |
| Automatic failover between two origins | **CloudFront origin groups** |
| Replace instances without in-place patching | **Immutable deployments / instance refresh** |
| Detect configuration drift | **AWS Config** |
| Find the slow or failing microservice | **AWS X-Ray** |
| Validate resilience assumptions | **AWS FIS** + **Resilience Hub** |
| Guarantee distinct hardware for critical nodes | **Spread placement group** |
| DR Region can't launch enough capacity | **Raise service quotas in advance** |
| Database connection exhaustion | **RDS Proxy** |
| Legacy app needs shared storage across nodes | **EFS / FSx for Windows** |
| Legacy app needs a fixed IP | **NLB with Elastic IPs** |

---

# Domain 3 — Design High-Performing Architectures (24%)


## Task 3.1 — Determine High-Performing and/or Scalable Storage Solutions

> The exam tests whether you can match a workload description to the correct storage service and configuration. Almost every question reduces to three questions: **object, file, or block? how much throughput/IOPS/latency? how is it accessed and by how many clients?**

---

## 1. The Three Storage Types

| | **Object** | **File** | **Block** |
|---|---|---|---|
| Services | S3, S3 Glacier | EFS, FSx (Windows / Lustre / ONTAP / OpenZFS) | EBS, Instance store |
| Access | HTTP(S) API (GET/PUT), flat namespace with key prefixes | NFS / SMB mount, hierarchical directories, POSIX or NTFS permissions | Raw block device, you format it with a file system |
| Concurrency | Massive — any number of clients | Many clients simultaneously | Normally **one instance** (EBS Multi-Attach is the exception) |
| Update semantics | Whole-object replace (no partial in-place writes) | Partial file writes, locking, metadata | Random block-level reads/writes |
| Scale | Effectively unlimited | Petabytes, elastic | Per-volume limit (64 TiB) |
| Typical use | Static assets, backups, data lakes, media, logs | Shared content, home directories, HPC, lift-and-shift | Boot volumes, databases, transactional workloads |

**Decision shortcut:**
- "Many servers need to read/write the same files with normal file-system semantics" → **file (EFS or FSx)**
- "One server needs a fast disk for a database" → **block (EBS)**
- "Store and retrieve lots of unstructured data over HTTP at any scale" → **object (S3)**

---

## 2. Amazon S3 in Depth

### 2.1 Fundamentals

- **Unlimited total capacity.** Individual objects range from **0 bytes to 5 TB**. A single `PUT` can upload up to **5 GB**; above that you must use **multipart upload** (and AWS recommends it above ~100 MB).
- **Durability 99.999999999% (11 nines)** by storing data redundantly across **at least three Availability Zones** (except One Zone classes). Availability for S3 Standard is **99.99%**.
- **Strong read-after-write consistency** for all operations — PUTs, overwrites, deletes, and list operations — at no cost and with no performance penalty.
- Flat namespace: there are no real folders. `reports/2026/q1.csv` is just a key; the console displays it as folders. **Prefixes** matter for performance (see below).

### 2.2 Performance characteristics and how to scale

**Request rates:** S3 supports at least **3,500 PUT/COPY/POST/DELETE** and **5,500 GET/HEAD** requests per second **per partitioned prefix**. There is **no limit on the number of prefixes**, so request capacity scales horizontally: splitting objects across 10 prefixes gives roughly 35,000 writes/second and 55,000 reads/second.

If an application receives `503 Slow Down` responses, the fix is to **spread keys across more prefixes** (for example `logs/01/...` through `logs/20/...`), not to request a quota increase. S3 also auto-partitions over time, but that takes a while to adapt.

**Multipart upload** — splits an object into parts uploaded in parallel:
- Required above 5 GB, recommended above ~100 MB
- **Faster** (parallelism), **more resilient** (retry just a failed part), and **resumable**
- Always add a lifecycle rule to **abort incomplete multipart uploads** after N days, or you pay for orphaned parts forever

**Byte-range fetches** — request specific byte ranges of an object in parallel to speed up downloads, or to read just a header/footer of a large file.

**S3 Transfer Acceleration** — clients upload to the nearest **CloudFront edge location** and the data travels to the bucket over the optimized AWS backbone. Helps when users are geographically distant from the bucket; it costs extra, and AWS provides a speed comparison tool to check whether it actually helps.

**S3 Select** — run simple SQL (`SELECT ... WHERE`) against a **single object** (CSV, JSON, Parquet, optionally GZIP/BZIP2) server-side, returning only matching rows/columns. Dramatically reduces data transferred and client-side processing. For queries across **many** objects, use **Athena** instead.

**S3 Express One Zone** — a high-performance, single-AZ storage class delivering **single-digit-millisecond** (up to 10× faster) access and very high request rates, designed for latency-sensitive analytics and ML workloads. Data is co-located with compute in one AZ, with higher request costs and lower storage cost than Standard.

### 2.3 Storage classes

| Class | First-byte latency | Min duration | Min billable size | AZs | Designed for |
|---|---|---|---|---|---|
| **S3 Standard** | ms | — | — | ≥3 | Frequently accessed, hot data |
| **S3 Intelligent-Tiering** | ms (Frequent / Infrequent / Archive Instant tiers) | — (small monitoring fee per object) | 128 KB for auto-tiering | ≥3 | **Unknown or changing access patterns** |
| **S3 Standard-IA** | ms | **30 days** | 128 KB | ≥3 | Infrequently accessed but needs instant retrieval |
| **S3 One Zone-IA** | ms | **30 days** | 128 KB | **1** | Re-creatable, infrequently accessed |
| **S3 Glacier Instant Retrieval** | **ms** | **90 days** | 128 KB | ≥3 | Archive accessed about once a quarter but needing instant access |
| **S3 Glacier Flexible Retrieval** | Expedited 1–5 min, Standard 3–5 h, Bulk 5–12 h | **90 days** | 40 KB | ≥3 | Archive, occasional retrieval |
| **S3 Glacier Deep Archive** | Standard 12 h, Bulk 48 h | **180 days** | 40 KB | ≥3 | Long-term compliance archive, cheapest |
| **S3 Express One Zone** | **single-digit ms** | — | — | 1 | Latency-critical, high-request workloads |

**Intelligent-Tiering tiers:** Frequent Access → Infrequent Access (after 30 days without access) → Archive Instant Access (after 90 days) → optional Archive Access (90+) and Deep Archive Access (180+). **No retrieval fees** for the automatic tiers, which is why it is the right answer for unpredictable patterns.

### 2.4 Lifecycle management

Lifecycle rules automate transitions and deletions, scoped by prefix, tag, or object size:
- **Transition actions** — move between storage classes as objects age
- **Expiration actions** — delete current versions, delete **noncurrent versions** after N days, remove **expired delete markers**, and **abort incomplete multipart uploads**

Constraints: objects must be at least 30 days old before moving from Standard to Standard-IA, and transitions can only move "down" the tier hierarchy. Use **S3 Storage Class Analysis** or **Storage Lens** to decide the thresholds.

### 2.5 Other capabilities worth knowing

- **Event notifications** → SNS, SQS, Lambda, or **EventBridge** (richer filtering) when objects are created, deleted, restored, or replicated.
- **S3 Access Points** — unique hostnames with their own policies per application; **Object Lambda Access Points** transform data on retrieval (redaction, format conversion) without duplicating it.
- **Multi-Region Access Points** — a single global endpoint that routes to the nearest bucket over the AWS backbone, with automatic failover.
- **S3 Batch Operations** — perform actions (copy, restore, tag, invoke Lambda, replicate) across billions of objects from a manifest or inventory report.
- **S3 Inventory** — scheduled CSV/ORC/Parquet reports of objects and metadata.
- **Storage Lens** — organization-wide usage and activity analytics with cost-optimization recommendations.
- **Requester Pays** — the requester pays for requests and transfer, used for large shared datasets.
- **Static website hosting**, **presigned URLs**, **CORS**.

---

## 3. Amazon EBS

### 3.1 Fundamentals

An EBS volume is a **network-attached block device** that lives in **one Availability Zone** and attaches to an EC2 instance in that AZ. It persists independently of the instance lifecycle (unless `DeleteOnTermination` is set on the root volume).

- Volumes can be **modified live** with **Elastic Volumes**: change size, type, IOPS, and throughput without detaching. You can **increase** size but never decrease it.
- Snapshots are **incremental**, stored durably, and can be copied across Regions and accounts.
- **io1/io2 support Multi-Attach** — the same volume attached to up to **16 instances in the same AZ**, which requires a **cluster-aware file system** (not ext4/XFS) to avoid corruption.

### 3.2 Volume types

| Type | Media | Size range | Max IOPS | Max throughput | Boot volume? | Best for |
|---|---|---|---|---|---|---|
| **gp3** | SSD | 1 GiB – 16 TiB | **16,000** (3,000 baseline, provisioned independently of size) | 1,000 MB/s (125 MB/s baseline) | Yes | **Default general purpose**; ~20% cheaper than gp2 |
| **gp2** | SSD | 1 GiB – 16 TiB | 3 IOPS/GiB (min 100, max 16,000), burst to 3,000 | 250 MB/s | Yes | Legacy general purpose |
| **io1** | SSD | 4 GiB – 16 TiB | 64,000 | 1,000 MB/s | Yes | I/O-intensive, Multi-Attach |
| **io2** | SSD | 4 GiB – 16 TiB | 64,000 (higher durability: 99.999%) | 1,000 MB/s | Yes | Critical databases |
| **io2 Block Express** | SSD | up to **64 TiB** | **256,000** | **4,000 MB/s** | Yes | Largest, most demanding databases (SAP HANA, Oracle) |
| **st1** | HDD | 125 GiB – 16 TiB | 500 | **500 MB/s** | **No** | **Throughput-oriented**: big data, log processing, data warehouses |
| **sc1** | HDD | 125 GiB – 16 TiB | 250 | 250 MB/s | **No** | Coldest data, lowest cost per GB |

**Exam-critical facts:**
- **HDD volumes (st1, sc1) cannot be boot volumes.**
- **gp3 decouples IOPS and throughput from capacity**, so you no longer have to over-provision a large volume just to get IOPS (the classic gp2 problem).
- Reaching high IOPS also requires an **EBS-optimized instance** with sufficient network bandwidth; the instance type can be the bottleneck.
- **IOPS vs throughput:** IOPS matters for small random I/O (databases, transactional workloads); throughput (MB/s) matters for large sequential I/O (log processing, ETL, streaming reads).
- **RAID 0** across multiple EBS volumes can increase aggregate IOPS/throughput beyond a single volume's limit (at the cost of resilience); RAID 1 adds redundancy but EBS is already replicated within the AZ.

### 3.3 Instance store

**Physically attached NVMe SSDs** on the host. Characteristics:
- **Highest possible IOPS and lowest latency** — millions of IOPS on storage-optimized instances, because there is no network hop.
- **Ephemeral:** data is lost when the instance **stops, hibernates, or terminates**, or if the underlying hardware fails. It survives a reboot.
- Cost is included in the instance price (no separate charge).
- Capacity and presence are fixed by the instance type.

Use for: caches, buffers, temporary scratch space, swap, and **replicated** datastores where the cluster provides durability (Cassandra, Scylla, Elasticsearch hot tier, Hadoop HDFS temp).

### 3.4 Snapshots and performance

- Snapshots are incremental: only changed blocks are stored, but each snapshot is independently restorable.
- **Volumes restored from a snapshot are lazily loaded** — the first read of each block fetches from S3, causing elevated latency initially. **Fast Snapshot Restore (FSR)** pre-provisions the volume so it delivers full performance immediately (billed per AZ per snapshot).
- **Data Lifecycle Manager (DLM)** or **AWS Backup** automate snapshot creation, retention, and cross-Region copying.
- **EBS Snapshot Archive** stores rarely needed snapshots up to 75% cheaper (90-day minimum, 24–72 hour restore).

---

## 4. Amazon EFS

### 4.1 What it is

A fully managed, elastic **NFS v4.1** file system for **Linux** workloads. It can be mounted concurrently by **thousands of clients** — EC2 instances across multiple AZs, ECS and EKS containers, **Lambda functions**, and on-premises servers over Direct Connect or VPN.

- **Elastic capacity** — grows and shrinks automatically as files are added and removed, to petabyte scale; you pay only for what you store.
- A **mount target** is created per AZ (an ENI with a private IP); clients mount using the DNS name and are routed to their local AZ's mount target.
- Access is controlled by **security groups**, **POSIX permissions**, an **EFS file system policy** (IAM resource policy), and **EFS Access Points** (which enforce a specific POSIX user/group and root directory per application — ideal for multi-tenant or container use).
- Encryption at rest (KMS, set at creation) and in transit (TLS via the EFS mount helper).

### 4.2 Performance and throughput modes

**Performance modes** (set at creation, cannot be changed):
- **General Purpose** — lowest per-operation latency; the default and correct for almost all workloads including web serving and content management.
- **Max I/O** — higher aggregate throughput and IOPS, at the cost of slightly higher latency per operation. For highly parallelized workloads with thousands of clients (big data, media processing). *(Note: with Elastic throughput, General Purpose now scales very high, so Max I/O is increasingly legacy — but it remains an exam answer for "thousands of clients, maximum aggregate throughput, latency tolerance.")*

**Throughput modes:**
- **Elastic** (recommended default) — automatically scales throughput up and down with demand; pay only for what you use. Best for spiky or unpredictable workloads.
- **Bursting** — baseline throughput scales with the amount of data stored (50 KB/s per GiB) and uses burst credits for peaks. Cheap for large, lightly used file systems; a small file system with heavy I/O will exhaust credits.
- **Provisioned** — you specify a fixed MB/s independent of storage size. For small file systems that need high throughput.

### 4.3 Storage classes and lifecycle

- **EFS Standard** (multi-AZ) and **EFS One Zone** (single AZ, ~47% cheaper, for dev/test or re-creatable data).
- **Infrequent Access (IA)** and **Archive** classes within each, with **lifecycle management** automatically moving files after a period without access (and optionally moving them back on access). Savings of up to ~92% for cold data.

---

## 5. Amazon FSx Family

| Service | Protocol / engine | Key features | Choose when |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB**, NTFS | Active Directory integration, NTFS ACLs, DFS Namespaces, shadow copies (user-restorable previous versions), data deduplication, Multi-AZ, SSD or HDD storage | Windows applications, user home directories, .NET apps, SQL Server file shares, lift-and-shift of Windows file servers |
| **FSx for Lustre** | Lustre (POSIX) | **Sub-millisecond latency, hundreds of GB/s throughput, millions of IOPS**; **S3 integration** — presents an S3 bucket as a file system, lazily loading objects and optionally exporting results back | HPC, machine learning training, genomics, seismic analysis, financial modelling, video rendering |
| **FSx for NetApp ONTAP** | **NFS, SMB, and iSCSI** (multiprotocol) | Snapshots, SnapMirror, FlexClone, deduplication/compression, automatic tiering to capacity pool storage | Migrating existing NetApp estates; needing one file system served over multiple protocols |
| **FSx for OpenZFS** | NFS | ZFS snapshots and clones, very low latency, high IOPS | Migrating Linux/ZFS file servers; needing ZFS features |

**FSx for Lustre deployment options:**
- **Scratch** — temporary, **not replicated**, highest raw performance per dollar; data is lost if a file server fails. For short-lived processing.
- **Persistent** — replicated within an AZ, self-healing, for longer-running workloads. Available in several throughput tiers.

---

## 6. Hybrid Storage and Data Transfer

### 6.1 AWS Storage Gateway

A hybrid appliance (VM, hardware appliance, or EC2 instance) that gives on-premises applications access to AWS storage with a **local cache** for low-latency access to hot data.

| Gateway type | Presents | Stores into | Use case |
|---|---|---|---|
| **S3 File Gateway** | **NFS / SMB** file shares | Objects in **S3** (with lifecycle to Glacier) | On-prem apps that speak file protocols but you want data in S3 |
| **FSx File Gateway** | SMB | **FSx for Windows File Server** | Low-latency on-prem access to FSx shares |
| **Volume Gateway — cached** | **iSCSI block volumes** | Primary data in S3, hot cache on-prem | Extend on-prem storage capacity to the cloud |
| **Volume Gateway — stored** | iSCSI block volumes | Primary data **on-prem**, async backups to S3 as EBS snapshots | Keep low-latency local access, back up to AWS |
| **Tape Gateway (VTL)** | Virtual tape library (iSCSI VTL) | S3 and **Glacier / Deep Archive** | Replace physical tape infrastructure with existing backup software |

### 6.2 AWS DataSync

An online transfer service that moves data **between on-premises storage and AWS**, or **between AWS services**.
- Sources/targets: NFS, SMB, HDFS, self-managed object storage, **S3, EFS, FSx (all flavours)**, and other clouds.
- Up to **10× faster** than open-source tools thanks to a purpose-built protocol with parallelism and compression.
- **Scheduled, incremental, validated** transfers that **preserve metadata** (permissions, timestamps), with built-in encryption in transit.
- Runs via an **agent** on-premises (or agentless for AWS-to-AWS).
- The answer for *"recurring, automated, verified data synchronization."*

### 6.3 AWS Transfer Family

Fully managed **SFTP, FTPS, FTP, and AS2** endpoints that read and write directly to **S3 or EFS**. Authentication via service-managed users, Active Directory, or a custom identity provider. Use when **partners must keep using their existing file-transfer clients**.

### 6.4 AWS Snow Family

Physical devices for **offline bulk transfer** where the network is impractical:
- **Snowcone** — 8 TB HDD / 14 TB SSD, portable and rugged, can also run compute at the edge
- **Snowball Edge Storage Optimized** — ~80 TB usable, the workhorse for bulk migration
- **Snowball Edge Compute Optimized** — fewer TB, more vCPU/GPU, for edge processing
- **Snowmobile** — a shipping container for up to 100 PB (largely historical, but exam-relevant)

**Rule of thumb:** compute `time = data ÷ usable bandwidth`. If transferring over the network would take **more than about a week**, choose Snow. For example, 100 TB over a 1 Gbps link at full utilization is roughly 9 days — and real-world utilization is much lower.

### 6.5 Choosing a transfer method

| Situation | Service |
|---|---|
| One-time bulk move, poor bandwidth | **Snowball Edge** |
| Recurring scheduled sync | **DataSync** |
| Continuous hybrid file access with local cache | **Storage Gateway** |
| Partners uploading with SFTP clients | **Transfer Family** |
| Ongoing high-volume transfer over a private link | **Direct Connect** (+ DataSync) |
| Global users uploading large objects to S3 | **Multipart upload + Transfer Acceleration** |
| Database migration with change capture | **AWS DMS** |

---

## 7. Matching Workloads to Storage — Worked Scenarios

**Scenario 1 — "50 Linux web servers across 3 AZs must share the same content directory, and the dataset grows unpredictably."**
**Amazon EFS** with Elastic throughput. EBS cannot be shared across AZs; S3 is not POSIX; FSx for Windows is SMB.

**Scenario 2 — "A machine-learning training job must read 20 TB from S3 at hundreds of GB/s with sub-millisecond latency."**
**FSx for Lustre** linked to the S3 bucket (scratch deployment if the data is transient), which lazily imports objects and can export results back.

**Scenario 3 — "A PostgreSQL database on EC2 needs a sustained 45,000 IOPS with predictable latency."**
**io2 Block Express** (or io2) on an EBS-optimized instance large enough to support that bandwidth. gp3 tops out at 16,000 IOPS.

**Scenario 4 — "A Hadoop cluster needs maximum local throughput for temporary shuffle data."**
**Instance store** on a storage-optimized (I/D/H) instance family — ephemeral is fine because HDFS replicates.

**Scenario 5 — "Nightly log processing scans terabytes sequentially; cost matters."**
**st1 (throughput-optimized HDD)** — cheaper than SSD and designed for large sequential reads.

**Scenario 6 — "We don't know how often this new dataset will be accessed and don't want retrieval surprises."**
**S3 Intelligent-Tiering.**

**Scenario 7 — "Records must be kept 10 years, retrieval within 12 hours is fine."**
**S3 Glacier Deep Archive** via a lifecycle rule.

**Scenario 8 — "Global users complain that uploading 4 GB videos to our Mumbai bucket is slow."**
**Multipart upload** for parallelism plus **S3 Transfer Acceleration** to use the nearest edge.

**Scenario 9 — "Our on-prem application writes to an SMB share; we want the data in AWS without changing the application."**
**S3 File Gateway** (if S3 is the target) or **FSx File Gateway / FSx for Windows** (if a true Windows file system is needed).

**Scenario 10 — "We must migrate 500 TB within a month over a 500 Mbps link shared with production."**
**Snowball Edge** devices — the network path would take many months.

---

## 8. Quick Decision Table

| Requirement | Answer |
|---|---|
| Shared file storage, Linux, multi-AZ, elastic | **Amazon EFS** |
| Shared file storage, Windows, Active Directory, SMB | **FSx for Windows File Server** |
| HPC/ML parallel file system integrated with S3 | **FSx for Lustre** |
| Multiprotocol (NFS + SMB + iSCSI), NetApp features | **FSx for NetApp ONTAP** |
| Single-instance database volume, consistent high IOPS | **io2 / io2 Block Express** |
| General-purpose block storage, best value | **gp3** |
| Highest IOPS, data is disposable | **Instance store** |
| Large sequential throughput, lowest block cost | **st1** |
| Coldest block storage | **sc1** |
| Boot volume | **SSD only (gp3/gp2/io1/io2)** |
| Same volume attached to several instances in one AZ | **io1/io2 Multi-Attach + cluster-aware FS** |
| Unknown/changing access pattern | **S3 Intelligent-Tiering** |
| Infrequent access but instant retrieval needed | **S3 Standard-IA** (or Glacier Instant Retrieval for colder) |
| Re-creatable, infrequent, cheapest resilient option | **S3 One Zone-IA** |
| Deep archive, hours to retrieve | **S3 Glacier Deep Archive** |
| Single-digit-ms object storage for analytics | **S3 Express One Zone** |
| Exceeding 3,500 writes/s in S3 | **Spread keys across more prefixes** |
| Upload a 50 GB object reliably | **Multipart upload** |
| Speed up long-distance uploads | **S3 Transfer Acceleration** |
| Query a subset of one large object | **S3 Select** |
| Query across many objects | **Amazon Athena** |
| Restore a volume with immediate full performance | **Fast Snapshot Restore** |
| Rarely used snapshots, cut cost | **EBS Snapshot Archive** |
| On-prem NFS/SMB backed by S3 | **S3 File Gateway** |
| Replace physical tape backups | **Tape Gateway** |
| Scheduled, validated on-prem → AWS sync | **AWS DataSync** |
| Partners upload via SFTP | **AWS Transfer Family** |
| Petabyte migration with poor bandwidth | **AWS Snowball Edge** |
| Cold EFS data costing too much | **EFS lifecycle management to IA/Archive** |

---

## Task 3.2 — Design High-Performing and Elastic Compute Solutions

> Two skills are tested here: **choosing the right compute service and instance type for a workload**, and **making that compute scale correctly** (on the right metric, at the right speed, with the right elasticity).

---

## 1. EC2 Instance Families

### 1.1 Reading an instance name

`m6gd.2xlarge` decodes as:
- **m** — family (general purpose)
- **6** — generation (higher is newer, usually better price/performance)
- **g** — processor/attribute modifier
- **d** — additional attribute (local NVMe instance store)
- **2xlarge** — size

**Common modifiers:**
| Letter | Meaning |
|---|---|
| **g** | **AWS Graviton (ARM)** processors |
| **a** | AMD EPYC processors |
| **i** | Intel processors (when the default differs) |
| **d** | Local NVMe **instance store** |
| **n** | Network and EBS optimized (higher bandwidth) |
| **e** | Extra storage or memory |
| **z** | High CPU frequency |
| **flex** | Flexible performance (sustained lower baseline, burst) |

### 1.2 The families

| Family | Prefixes | Optimized for | Representative workloads |
|---|---|---|---|
| **General purpose** | **T** (burstable), **M**, Mac | Balanced CPU : memory (roughly 1 vCPU : 4 GiB) | Web servers, small/medium databases, microservices, dev/test, code repositories |
| **Compute optimized** | **C** | High CPU per dollar (1 vCPU : 2 GiB) | Batch processing, **media transcoding**, high-performance web servers, scientific modelling, ad serving, gaming servers, HPC |
| **Memory optimized** | **R**, **X**, **z1d**, **u-** (High Memory) | Large memory per vCPU (1 vCPU : 8–32+ GiB) | In-memory databases, **SAP HANA**, large caches (Redis), real-time big data analytics, Electronic Design Automation |
| **Storage optimized** | **I** (NVMe IOPS), **D** (dense HDD), **H** (HDD throughput) | Very high local disk IOPS or throughput | NoSQL (Cassandra, ScyllaDB, MongoDB), Elasticsearch/OpenSearch, data warehousing, distributed file systems, transactional databases needing local storage |
| **Accelerated computing** | **P** (GPU training), **G** (GPU inference/graphics), **Inf** (Inferentia), **Trn** (Trainium), **F** (FPGA), **VT** (video transcode) | Hardware acceleration | ML training and inference, graphics workstations, genomics, video processing |
| **HPC optimized** | **Hpc** | Tightly coupled HPC with high network bandwidth | CFD, weather simulation, molecular dynamics |

### 1.3 Burstable (T) instances — a frequent exam trap

T-family instances provide a **baseline** level of CPU and accumulate **CPU credits** when running below it; credits are spent when bursting above baseline.

- When credits are exhausted in **Standard mode**, performance is **throttled to the baseline** — which looks like a mysterious, severe slowdown after hours of healthy operation. This is a classic scenario question.
- **Unlimited mode** (default for T3/T3a/T4g) allows sustained bursting and charges a surcharge for credits used beyond what is earned.
- T instances are ideal for workloads with **low average CPU and occasional spikes** (small websites, dev environments, microservices), and wrong for sustained CPU-heavy work — use **C** or **M** instead.

### 1.4 AWS Graviton

Graviton (currently Graviton2/3/4, the `g` suffix) are AWS-designed ARM processors delivering **up to ~40% better price/performance** than comparable x86 instances, with lower power consumption.

- Works with most Linux distributions and open-source software; applications written in interpreted or JIT languages (Python, Java, Node.js, Go, .NET Core, PHP, Ruby) usually need only a rebuild/redeploy. Compiled C/C++ needs recompilation.
- Available for EC2, **Lambda (arm64)**, **Fargate**, RDS, Aurora, ElastiCache, OpenSearch, EMR, and more.
- **Exam cue:** "improve performance and reduce cost for a Linux workload" → **Graviton**.

### 1.5 Networking performance features

- **Enhanced networking (ENA)** — SR-IOV based, up to **100 Gbps** on supported instances, with lower latency and jitter than the older virtualized NIC. Enabled by default on modern AMIs/instances.
- **ENA Express** (Scalable Reliable Datagram) — reduces tail latency and increases single-flow bandwidth.
- **Elastic Fabric Adapter (EFA)** — adds **OS-bypass** so HPC and ML frameworks (MPI, NCCL) can communicate directly with the network hardware, dramatically lowering latency for tightly coupled jobs. Only available on specific instance types and only useful within a **cluster placement group**.
- **Placement groups:**
  - **Cluster** — all instances in one AZ, physically close; lowest latency and highest per-flow throughput (up to 100 Gbps). Reduces availability.
  - **Spread** — each instance on distinct hardware, max 7 per AZ per group; best for small critical fleets.
  - **Partition** — groups of racks isolated from each other; for large distributed systems like HDFS, Cassandra, Kafka.
- **Instance network bandwidth scales with instance size.** A network-bound workload may need a larger or `n`-suffixed instance even if CPU is idle.
- **Jumbo frames (MTU 9001)** work inside a VPC and over Direct Connect, but not over the internet or most VPN paths.

### 1.6 Tenancy options

- **Shared (default)** — your instances share hardware with other customers.
- **Dedicated Instances** — hardware dedicated to your account, but instances may move between hosts.
- **Dedicated Hosts** — a specific physical server allocated to you, with visibility of sockets and cores. Required for **BYOL licensing** tied to physical cores (Windows Server, SQL Server, Oracle) and for some compliance regimes.

---

## 2. Scaling EC2

### 2.1 Auto Scaling group essentials

An ASG maintains capacity between **min**, **desired**, and **max** across multiple AZs, replacing unhealthy instances and integrating with load balancers.

- Use **launch templates** (versioned; required for mixed instances, Spot, and newer features).
- **Set `HealthCheckType = ELB`** so application-level failures trigger replacement, with a sensible **health check grace period**.
- **Lifecycle hooks** pause instances during launch or terminate to allow bootstrapping or draining.
- **Warm pools** keep pre-initialized instances stopped, so scale-out is near-instant for applications with long boot or warm-up times.
- **Instance refresh** performs controlled rolling replacement when the launch template changes.
- **Mixed instances policy** — specify several instance types and an On-Demand/Spot split, with allocation strategies (`price-capacity-optimized` is the modern recommendation) and **capacity rebalancing** for Spot.

### 2.2 Scaling policies and choosing the right metric

| Policy | Description | Use |
|---|---|---|
| **Target tracking** | Maintain a metric at a target value; AWS creates and manages the alarms | Default choice — CPU utilization, `ALBRequestCountPerTarget`, average network I/O, or a custom metric |
| **Step scaling** | Different capacity adjustments depending on the size of the alarm breach | When the response should be proportional to severity |
| **Simple scaling** | One adjustment per alarm with a cooldown | Legacy |
| **Scheduled scaling** | Set min/max/desired at specific times | Predictable daily/weekly/seasonal patterns |
| **Predictive scaling** | ML forecast from ≥24 hours of history, provisioning **before** demand arrives | Recurring cycles plus long instance warm-up |

**Metric selection is the real exam content:**
- Web/API tier → `ALBRequestCountPerTarget` (directly proportional to load) or CPU
- **Queue workers → `ApproximateNumberOfMessagesVisible`**, ideally normalized as **backlog per instance** = messages ÷ running instances, published as a custom metric
- Memory-bound applications → **install the CloudWatch agent** and scale on the custom memory metric (memory is *not* a default EC2 metric; neither is disk usage)
- Connection-bound → `ActiveConnectionCount` or a custom metric

**Cooldowns and warm-up** prevent thrashing: a cooldown blocks further scaling actions until the previous one takes effect; instance warm-up tells target tracking to ignore a new instance's metrics until it is ready.

### 2.3 Application Auto Scaling

The same engine scales other resources: **ECS services**, **DynamoDB** tables and GSIs, **Aurora Replicas**, **Lambda provisioned concurrency**, Spot Fleet, EMR, SageMaker endpoints, AppStream, Comprehend, Keyspaces, and Neptune.

---

## 3. Serverless Compute

### 3.1 AWS Lambda performance tuning

**The memory/CPU relationship is the single most important tuning lever.** Lambda allocates CPU (and network and disk I/O) **proportionally to memory**: at 1,769 MB a function gets the equivalent of one full vCPU; at 10,240 MB roughly six vCPUs. Therefore:

- Increasing memory often **reduces total cost** because the function finishes much faster (cost = GB-seconds × duration + per-request charge). A function taking 10 s at 512 MB that takes 2 s at 1,024 MB costs *less* overall and is five times faster.
- Use **AWS Lambda Power Tuning** (a Step Functions state machine) to empirically find the optimal memory setting.
- Multithreaded code only benefits above ~1,769 MB where multiple vCPUs become available.

**Other limits and levers:**
- Timeout maximum **15 minutes**; `/tmp` from 512 MB to **10 GB**; deployment package 50 MB zipped / 250 MB unzipped, or a **10 GB container image**
- **Cold starts** — the initialization of a new execution environment. Worsened by large packages, heavy static initialization, and (historically) VPC attachment. Mitigations: **provisioned concurrency** (keeps environments warm and initialized), **SnapStart** for Java (snapshot of the initialized runtime, no extra cost), smaller deployment packages, lazy loading of dependencies, and moving initialization outside the handler so it is reused by warm invocations.
- **Concurrency**: default **1,000** per account per Region (soft). **Reserved concurrency** guarantees and caps a function's concurrency (use it to protect a downstream database). **Provisioned concurrency** pre-initializes a set number of environments and can be auto-scaled.
- **Event source mappings** have their own tuning: SQS (batch size up to 10,000, batch window, **maximum concurrency**), Kinesis/DynamoDB Streams (one concurrent invocation per shard by default, raised with the **parallelization factor** up to 10), Kafka.
- **Lambda in a VPC** gets ENIs in your subnets (using Hyperplane ENIs, so scaling is fast) and needs a **NAT gateway or VPC endpoints** for outbound AWS/internet access.

### 3.2 AWS Fargate

Serverless compute for containers on ECS and EKS. You declare vCPU and memory per task (from 0.25 vCPU/0.5 GB up to 16 vCPU/120 GB, plus configurable ephemeral storage up to 200 GB), and AWS runs it with no instances to patch, scale, or secure.

- Billed per vCPU-second and GB-second with a one-minute minimum.
- **Fargate Spot** offers up to 70% savings for interruption-tolerant tasks.
- Supports **Graviton (arm64)** for better price/performance.
- Each task gets its own kernel-level isolation and its own ENI (`awsvpc` mode), which is also a security advantage.

Trade-offs vs ECS on EC2: Fargate has no GPU support, no access to the host, and can be more expensive at very high steady utilization, where bin-packed EC2 (especially with Spot) wins.

---

## 4. Containers at Scale

- **Amazon ECS** — services maintain a desired task count; **service auto scaling** (via Application Auto Scaling) reacts to CPU, memory, or **`ALBRequestCountPerTarget`**. **Capacity providers** connect the service to either Fargate/Fargate Spot or an EC2 Auto Scaling group with **managed scaling** (which scales the instance fleet to fit pending tasks).
- **Amazon EKS** — managed Kubernetes control plane across multiple AZs. Node scaling via **managed node groups** with the **Cluster Autoscaler**, or **Karpenter** (which provisions right-sized nodes just-in-time and consolidates workloads — significantly faster and more efficient). Pod scaling via the **Horizontal Pod Autoscaler** (and VPA for vertical). **Fargate profiles** run pods serverlessly.
- **Amazon ECR** for images, with lifecycle policies and replication.
- Performance considerations: right-size task CPU/memory requests (over-requesting wastes capacity, under-requesting throttles), use **awsvpc** networking, place tasks across AZs, and use **Service Connect / Cloud Map** for service discovery.

---

## 5. Batch and Big Data Compute

- **AWS Batch** — fully managed batch scheduling. You define **job definitions**, submit jobs to **job queues** with priorities, and Batch provisions a **compute environment** (EC2 On-Demand, **Spot**, or Fargate) sized to the queue. Supports **array jobs** (thousands of similar tasks), **job dependencies**, and automatic retry. The answer for *"run thousands of queued jobs cost-effectively with no scheduler to manage."*
- **Amazon EMR** — managed Hadoop ecosystem (Spark, Hive, Presto/Trino, HBase, Flink). Uses **instance fleets or groups** with master, core (HDFS), and **task nodes (ideal for Spot)**. Variants: EMR on EC2, **EMR on EKS**, and **EMR Serverless**. Use for petabyte-scale distributed processing and when you need specific framework versions or deep tuning.
- **AWS ParallelCluster** — open-source tool for provisioning traditional HPC clusters (Slurm) on AWS.
- **Choosing:** short event-driven work → **Lambda**; many long-running queued jobs → **Batch**; distributed data-processing frameworks → **EMR**; tightly coupled MPI simulations → **HPC instances + cluster placement group + EFA** (often via ParallelCluster).

---

## 6. Edge and Distributed Compute

- **CloudFront Functions** — ultra-lightweight JavaScript at the edge (sub-millisecond, ~1 ms CPU budget) for header manipulation, URL rewrites, redirects, and simple auth checks. Runs at all edge locations, highest scale, lowest cost.
- **Lambda@Edge** — full Node.js/Python functions running at **regional edge caches**, with more memory, longer execution, and network access. Use for heavier logic: origin selection, A/B testing with external calls, image resizing, authorization against an external service.
- **AWS Outposts** — AWS-managed racks on-premises running EC2, EBS, S3, ECS/EKS, RDS locally. For latency-sensitive on-prem integration or data residency.
- **AWS Local Zones** — extend a Region into a metro area for single-digit-millisecond latency (media rendering, gaming, remote desktops).
- **AWS Wavelength** — compute inside 5G carrier networks for mobile edge applications.
- **AWS IoT Greengrass** — run Lambda functions and ML inference on edge devices.
- **AWS Global Accelerator** — not compute, but it reduces the network component of latency by moving traffic onto the AWS backbone at the nearest edge.

---

## 7. Decoupling So Components Scale Independently

A tightly coupled synchronous chain forces every tier to scale together and makes the slowest component the bottleneck for everything. Insert the right integration point:

- **Queue (SQS)** between a fast producer and a slow consumer, scaling workers on **backlog depth**
- **Stream (Kinesis)** when multiple consumers need the same ordered data
- **Topic/bus (SNS/EventBridge)** when one event must trigger several independent reactions
- **Load balancer** between stateless tiers
- **Cache (ElastiCache/DAX/CloudFront)** in front of expensive reads
- **Step Functions** to coordinate long-running multi-step work without holding a connection open

Each component then scales on **its own signal** — requests per target for the web tier, queue depth for workers, RCU/WCU for DynamoDB, replica count for the database read layer.

---

## 8. Worked Scenarios

**Scenario 1 — "Video transcoding is CPU-bound and takes too long."**
**Compute optimized (C-family)** instances, parallelized via **AWS Batch** or **Elastic Transcoder/MediaConvert**, optionally on **Spot** for cost. Consider GPU (G-family) if the codec benefits.

**Scenario 2 — "An in-memory analytics engine needs 1 TB of RAM."**
**Memory optimized** — `x2idn`, `r6i.32xlarge`, or the `u-` High Memory family for multi-terabyte SAP HANA.

**Scenario 3 — "A Cassandra cluster needs millions of local IOPS."**
**Storage optimized I-family** with NVMe **instance store**; durability comes from Cassandra's replication.

**Scenario 4 — "Our Lambda function is slow and we want it faster and ideally cheaper."**
Increase **memory** (CPU scales with it), measure with Power Tuning, trim the package, move initialization outside the handler, and consider **arm64/Graviton**.

**Scenario 5 — "API latency spikes after idle periods."**
Cold starts — enable **provisioned concurrency** (or **SnapStart** for Java).

**Scenario 6 — "Workers aren't scaling even though the queue is growing, because CPU stays low."**
Scale on **`ApproximateNumberOfMessagesVisible`** / backlog per instance instead of CPU.

**Scenario 7 — "We need to scale on memory utilization."**
Install the **CloudWatch agent**, publish memory as a custom metric, and use a target tracking policy on it.

**Scenario 8 — "Instances take 12 minutes to boot, so scale-out is too slow during morning peaks."**
**Warm pools** plus **predictive or scheduled scaling** ahead of the known peak.

**Scenario 9 — "A tightly coupled MPI simulation needs the lowest possible inter-node latency."**
**Cluster placement group** + **EFA**-enabled HPC/compute instances in a single AZ.

**Scenario 10 — "Thousands of independent, restartable jobs must run as cheaply as possible."**
**AWS Batch** with a Spot compute environment and array jobs.

---

## 9. Quick Decision Table

| Requirement | Answer |
|---|---|
| Event-driven, short, spiky workload | **AWS Lambda** |
| Containers with no servers to manage | **Fargate (ECS/EKS)** |
| Kubernetes required | **Amazon EKS** |
| Thousands of queued batch jobs | **AWS Batch (+ Spot)** |
| Spark/Hadoop at petabyte scale | **Amazon EMR** |
| CPU-bound processing | **C family (compute optimized)** |
| Large in-memory dataset | **R / X / u- family** |
| Very high local disk IOPS | **I family + instance store** |
| GPU training / inference | **P / Trn** and **G / Inf** |
| Low average CPU with occasional bursts | **T family** (watch credits) |
| Best price/performance on Linux | **Graviton (`g`) instances** |
| BYOL licensing per physical core | **Dedicated Hosts** |
| Lowest inter-node network latency | **Cluster placement group + EFA** |
| Instances must not share hardware | **Spread placement group** |
| Large distributed system, rack awareness | **Partition placement group** |
| Scale a web tier accurately | Target tracking on **`ALBRequestCountPerTarget`** |
| Scale queue workers | Target tracking on **queue backlog per instance** |
| Scale on memory | **CloudWatch agent** custom metric |
| Known daily traffic pattern | **Scheduled** (+ predictive) scaling |
| Long boot times hurt scale-out | **Warm pools** |
| Roll out a new AMI safely | **Instance refresh** |
| Eliminate Lambda cold starts | **Provisioned concurrency** / **SnapStart** |
| Protect a database from Lambda concurrency | **Reserved concurrency** (+ RDS Proxy) |
| Lightweight logic at the edge | **CloudFront Functions** |
| Heavier logic at the edge | **Lambda@Edge** |
| AWS compute inside your data center | **AWS Outposts** |
| Single-digit-ms latency in a specific metro | **AWS Local Zones** |

---

## Task 3.3 — Determine High-Performing Database Solutions

> AWS has a **purpose-built database** for every data shape. The exam gives you a workload description and expects you to pick the right engine, then tune it (caching, read replicas, capacity mode, indexes, connection pooling).

---

## 1. Choosing the Right Database

### 1.1 The purpose-built catalogue

| Database type | AWS service | Data model | Classic use cases |
|---|---|---|---|
| **Relational (OLTP)** | **RDS** (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2), **Aurora** (MySQL/PostgreSQL compatible) | Tables, rows, joins, ACID, SQL | ERP, CRM, finance, e-commerce, any app needing complex queries and transactions |
| **Key-value / document** | **DynamoDB** | Items with attributes, accessed by key | Serverless apps, gaming leaderboards, session stores, IoT, shopping carts, high-scale web |
| **Document** | **DocumentDB** (MongoDB-compatible) | JSON documents, flexible schema | Content management, catalogues, user profiles, MongoDB migrations |
| **In-memory** | **ElastiCache** (Redis/Valkey, Memcached), **MemoryDB** | Key-value in RAM | Caching, session store, leaderboards, pub/sub, rate limiting; MemoryDB adds durability |
| **Graph** | **Neptune** | Nodes and edges (Gremlin, openCypher, SPARQL) | Social networks, fraud detection, recommendation engines, knowledge graphs, network topology |
| **Time series** | **Timestream** | Timestamped measures | IoT telemetry, DevOps metrics, industrial sensors, clickstream |
| **Wide column** | **Keyspaces** (Cassandra-compatible) | Partition/clustering keys, CQL | Cassandra migrations, industrial/fleet data at scale |
| **Ledger** | **QLDB** | Immutable, cryptographically verifiable journal | Audit trails, supply-chain provenance, financial records |
| **Data warehouse (OLAP)** | **Redshift** | Columnar, MPP | BI, dashboards, complex analytical queries over terabytes/petabytes |
| **Search** | **OpenSearch Service** | Inverted index | Full-text search, log analytics, observability |

### 1.2 How to decide

1. **Is the access pattern known and simple (get/put by key) with massive scale?** → **DynamoDB**.
2. **Do you need joins, complex ad-hoc queries, transactions across tables, or existing SQL?** → **RDS/Aurora**.
3. **Is the question analytical (aggregations over huge historical datasets)?** → **Redshift** (or Athena over S3 for ad hoc).
4. **Are relationships themselves the query ("friends of friends who bought X")?** → **Neptune**.
5. **Is it full-text search or log exploration?** → **OpenSearch**.
6. **Is it microsecond-latency reads of hot data?** → **ElastiCache/DAX/MemoryDB**.
7. **Is it append-only timestamped measurements?** → **Timestream**.

**OLTP vs OLAP** is the single most useful distinction: OLTP means many small, fast, concurrent reads/writes of individual records (row-oriented, RDS/Aurora/DynamoDB); OLAP means scanning and aggregating huge numbers of rows across few columns (column-oriented, Redshift).

---

## 2. Amazon RDS

### 2.1 Core concepts

A managed relational database: AWS handles provisioning, OS and engine patching, backups, monitoring, and failover. You remain responsible for schema design, query tuning, indexes, and parameter settings.

- **Instance classes** follow EC2 families: `db.t` (burstable), `db.m` (general), `db.r`/`db.x` (memory optimized). Graviton (`g`) classes give better price/performance.
- **Storage:** gp3 (general purpose SSD), io1/io2 (provisioned IOPS, up to 256,000 with io2 Block Express on supported engines), magnetic (legacy). **Storage autoscaling** grows the volume automatically when free space runs low.
- **Parameter groups** control engine settings (`max_connections`, buffer pool size, query cache, logging); some parameters are static and require a reboot. **Option groups** add engine features (Oracle TDE, SQL Server Audit).
- **Maintenance and backup windows** define when patching and backups occur; with Multi-AZ these are applied to the standby first.

### 2.2 Performance features

**Read replicas** — asynchronous copies that serve read traffic:
- Up to **5 per source** (15 for Aurora), in the same AZ, another AZ, or **another Region**
- **Eventually consistent** — never use when read-after-write consistency is required
- Can be promoted to a standalone database
- Each replica has its own endpoint; the application must be written to route reads to them (or use a proxy/Aurora reader endpoint)

**Multi-AZ** is for availability, not performance — **the standby serves no traffic** in the classic instance deployment. (The newer **Multi-AZ DB cluster** has two *readable* standbys and failover in under 35 seconds.)

**Amazon RDS Proxy** — a managed connection pool that:
- Multiplexes thousands of application connections onto a small number of database connections, solving **connection exhaustion** from Lambda and container fleets
- **Reduces failover time by up to 66%** by holding client connections while re-pointing to the new writer
- Supports **IAM authentication** and **Secrets Manager** credentials, and never exposes database credentials to the application

**Performance Insights** — a visual database load dashboard showing **average active sessions** broken down by wait event, SQL statement, host, and user. This is the tool for answering "which query is causing the load?" Retains 7 days free, up to 2 years paid.

**Enhanced Monitoring** — OS-level metrics (per-process CPU, memory, file system, disk I/O) at up to 1-second granularity, which standard CloudWatch metrics (hypervisor level) cannot provide.

**Other tuning levers:** right-size the instance class; use **gp3 or io2** with adequate IOPS; add indexes; use **connection pooling**; offload reads to replicas; cache in **ElastiCache**; partition large tables; archive cold data to S3.

---

## 3. Amazon Aurora

### 3.1 Architecture

Aurora is a cloud-native reimplementation of MySQL and PostgreSQL that separates compute from a distributed, log-structured storage layer.

- Storage keeps **six copies across three Availability Zones**, is self-healing, and grows automatically in 10 GB increments to **128 TiB**.
- Aurora tolerates the loss of **two copies for writes** and **three copies for reads** with no availability impact.
- Claimed performance: up to **5× MySQL** and **3× PostgreSQL** throughput on the same hardware, achieved largely by sending only redo log records to storage rather than full pages.
- Up to **15 Aurora Replicas** sharing the same storage, so replicas add no write overhead and lag is typically **under 10 ms**. Failover to a replica normally completes in **under 30 seconds**.

### 3.2 Endpoints

- **Cluster (writer) endpoint** — always points to the current primary; follows failover automatically
- **Reader endpoint** — DNS round-robins across all available replicas
- **Custom endpoints** — a subset of instances (e.g., route reporting queries to larger instances)
- **Instance endpoints** — a specific instance, for diagnostics

### 3.3 Aurora features

- **Aurora Serverless v2** — scales **in-place, in fine-grained increments** of Aurora Capacity Units (0.5 ACU steps, from 0.5 to 256 ACUs) in **under a second**, supports read replicas, Multi-AZ, and Global Database, and can be mixed with provisioned instances in one cluster. Ideal for **variable, unpredictable, or intermittent** workloads, dev/test, and multi-tenant SaaS. (v1 scaled by pausing and jumping between capacity points, with a connection interruption — v2 removed that.)
- **Aurora Global Database** — one primary Region and up to **five secondaries**, storage-level replication with typical lag **under one second**, **RPO ≈ 1 s / RTO < 1 min**, plus low-latency local reads and optional **write forwarding** from secondaries.
- **Backtrack** (Aurora MySQL) — rewind the cluster in place to a previous point in seconds without restoring from a snapshot. Perfect for undoing an accidental `DELETE` or a bad deployment.
- **Fast database cloning** — copy-on-write clones created in minutes, using almost no extra storage initially. Ideal for test environments on production-sized data.
- **Aurora Machine Learning** — call SageMaker/Comprehend from SQL.
- **Babelfish for Aurora PostgreSQL** — understands the SQL Server TDS protocol and T-SQL, so SQL Server applications can migrate with minimal code change.
- **Aurora I/O-Optimized** — a cluster configuration with no per-I/O charge; cheaper and more predictable when I/O spend exceeds ~25% of the bill.
- **Zero-ETL integration with Redshift** — near-real-time analytics on Aurora data without building pipelines.

### 3.4 Aurora vs RDS

Choose **Aurora** for higher performance, 15 low-lag replicas, faster failover, auto-scaling storage, Global Database, Backtrack, cloning, and Serverless v2. Choose **RDS** when you need an engine Aurora doesn't offer (Oracle, SQL Server, Db2, MariaDB), when the workload is small and cost-sensitive (a `db.t4g` RDS instance is cheaper than the smallest practical Aurora setup), or when you need specific engine versions/features.

---

## 4. Amazon DynamoDB

### 4.1 Data model and keys

- A **table** holds **items** (rows), each with **attributes**. Items can have different attributes — the schema is flexible apart from the key.
- **Primary key** is either:
  - **Partition key only** (simple) — must be unique
  - **Partition key + sort key** (composite) — the combination must be unique, and items with the same partition key are stored together, sorted by sort key, enabling efficient range queries
- The **partition key is hashed** to decide which physical partition stores the item. **Choosing a high-cardinality, evenly-accessed partition key is the single most important performance decision.** A low-cardinality key (e.g., `status = "active"`) creates a **hot partition** and throttling.
- Item size limit **400 KB** — store large blobs in S3 and keep the pointer in DynamoDB.

### 4.2 Capacity modes

| Mode | How you pay | Best for |
|---|---|---|
| **On-demand** | Per request (read/write request units) | Unpredictable or spiky traffic, new applications, dev/test, infrequent use; **no capacity planning**; instantly accommodates spikes |
| **Provisioned** | Per hour for provisioned **RCU/WCU**, with optional **auto scaling** | Predictable, steady traffic; **cheaper at consistent high utilization**; can be combined with **reserved capacity** for further savings |

**Capacity units:**
- 1 **WCU** = one write of up to **1 KB** per second
- 1 **RCU** = one **strongly consistent** read of up to **4 KB** per second, or **two eventually consistent** reads of up to 4 KB per second
- Transactional reads/writes consume **double**

**Burst capacity** holds up to 5 minutes of unused capacity; **adaptive capacity** automatically shifts throughput toward hot partitions and isolates frequently accessed items, which mitigates but does not eliminate bad key design.

### 4.3 Reads, queries and indexes

- **GetItem** — retrieve one item by full primary key (fastest, cheapest)
- **Query** — retrieve items sharing a partition key, optionally filtered by sort key conditions. **Efficient.**
- **Scan** — reads the **entire table** then filters. **Expensive and slow**; use only for small tables or infrequent full exports. Mitigate with parallel scans and projections, but the real fix is usually a **GSI** so you can `Query` instead.
- **Consistency:** eventually consistent by default (cheaper, lower latency); strongly consistent reads cost double and are not available on GSIs.

**Secondary indexes:**

| | **Local Secondary Index (LSI)** | **Global Secondary Index (GSI)** |
|---|---|---|
| Key | **Same partition key**, different sort key | **Any** partition and sort key |
| When created | **Only at table creation** | Any time, and deletable |
| Limit | 5 per table | 20 per table (soft) |
| Capacity | Shares the table's capacity | **Its own** RCU/WCU |
| Consistency | Supports strongly consistent reads | **Eventually consistent only** |
| Size | 10 GB limit per partition key value | No limit |

**Exam cue:** "query on a non-key attribute" → **GSI**. If a GSI is throttled, it can **throttle writes on the base table** — size GSI capacity appropriately and project only the attributes you need.

### 4.4 DynamoDB Accelerator (DAX)

A fully managed, in-memory cache **purpose-built for DynamoDB**:
- Reduces read latency from single-digit **milliseconds** to **microseconds**
- **API-compatible** — point the DAX client at the cluster; no application rewrite of the data access logic
- Caches both item responses and query/scan results
- Runs inside your VPC as a multi-node cluster
- **Only helps reads**, and is eventually consistent (strongly consistent reads pass through to DynamoDB)

If a question says "microsecond reads for DynamoDB with minimal application changes," the answer is **DAX**, not ElastiCache.

### 4.5 Other DynamoDB capabilities

- **DynamoDB Streams** — an ordered, 24-hour change log of item-level modifications, consumed by Lambda or KCL. Powers event-driven architectures, aggregation, replication, and audit.
- **Global tables** — multi-Region, **multi-active** replication with last-writer-wins conflict resolution, typically sub-second.
- **TTL** — automatically delete expired items at no cost (perfect for sessions, temporary data, and keeping tables small).
- **Point-in-time recovery** (any second in the last 35 days) and on-demand backups.
- **Transactions** — ACID across up to 100 items/multiple tables.
- **Export to S3** (no capacity consumed) for analytics with Athena, and **zero-ETL to Redshift/OpenSearch**.
- **Standard-IA table class** for tables where storage dominates cost over throughput.
- **Fine-grained access control** with `dynamodb:LeadingKeys` so a user can only access items whose partition key matches their identity.

---

## 5. Caching Layers

### 5.1 ElastiCache: Redis/Valkey vs Memcached

| | **Redis / Valkey** | **Memcached** |
|---|---|---|
| Data structures | Strings, lists, sets, sorted sets, hashes, bitmaps, HyperLogLog, streams, geospatial | Simple key-value strings only |
| Persistence | **Yes** (snapshots, AOF) | No |
| Replication / HA | **Replicas + Multi-AZ with automatic failover** | None |
| Scaling | Read replicas; **cluster mode** shards across up to 500 nodes | **Horizontal** — add nodes, client-side sharding |
| Multi-threaded | Mostly single-threaded (Valkey/Redis 7+ improves this) | **Multi-threaded** |
| Extras | Pub/sub, Lua scripting, transactions, **sorted sets for leaderboards**, geospatial queries | Pure, simple, very fast cache |

**Choose Redis** when you need persistence, HA, replication, or rich data structures (leaderboards, rate limiting, pub/sub, session store with failover). **Choose Memcached** for a simple, multi-threaded, horizontally scalable object cache where losing the cache is harmless.

**Amazon MemoryDB for Redis** is a *durable* Redis-compatible **primary database** with multi-AZ transaction-log durability — use it when Redis is the system of record, not just a cache.

### 5.2 Caching strategies

- **Lazy loading (cache-aside)** — check the cache; on a miss, read the database and populate the cache. Only requested data is cached and a cache failure is survivable, but misses cost extra latency and data can go stale.
- **Write-through** — write to the cache whenever you write to the database. Data is never stale and reads are fast, but writes are slower and the cache holds data that may never be read.
- **TTL** — bound staleness regardless of strategy.
- **Write-behind** — buffer writes and flush asynchronously (risk of loss).
- **Typical answer:** lazy loading + TTL, with write-through for hot keys.

**Cache problems to recognize:**
- **Thundering herd / cache stampede** — a popular key expires and thousands of requests hit the database at once. Mitigate with jittered TTLs, request coalescing, or pre-warming.
- **Hot key** — one key receives disproportionate traffic. Mitigate by replicating the key across shards or adding a local in-process cache.
- **Eviction** — when memory fills, Redis applies a maxmemory policy (`allkeys-lru` is common for caches). Watch the `Evictions` metric; rising evictions mean you need a bigger node.

### 5.3 Where caching fits

| Layer | Service |
|---|---|
| Edge/static + dynamic HTTP | **CloudFront** |
| API responses | **API Gateway caching** |
| Application/session/query results | **ElastiCache** |
| DynamoDB reads | **DAX** |
| Relational read scaling | **Read replicas** |
| DNS | Route 53 TTL |

---

## 6. Analytics and Search Data Stores

### 6.1 Amazon Redshift

A petabyte-scale, **columnar, massively parallel processing** data warehouse.

- **Architecture:** a leader node plans queries and distributes work to compute nodes, which are divided into slices. **RA3 nodes** with **managed storage** separate compute from storage (data lives in S3, hot data is cached locally), so you scale each independently.
- **Distribution styles** decide how rows are spread across slices: **KEY** (co-locate rows that join on the same column), **ALL** (replicate a small dimension table to every node to avoid shuffles), **EVEN** (round-robin), **AUTO** (Redshift decides). Bad distribution causes data shuffling and slow joins.
- **Sort keys** (compound or interleaved) let Redshift skip blocks using zone maps, hugely reducing I/O for range-restricted queries.
- **Redshift Spectrum** queries data directly in S3 without loading it, so you keep hot data in the cluster and cold data in the lake.
- **Concurrency Scaling** adds transient clusters automatically during bursts of queries.
- **Materialized views**, **result caching**, **workload management (WLM)** queues, and **AQUA** for acceleration.
- **Redshift Serverless** removes cluster management entirely and bills per RPU-second.
- **Zero-ETL integrations** from Aurora, RDS MySQL, and DynamoDB.

**Redshift is not an OLTP database** — it is poor at single-row lookups and high-frequency small writes.

### 6.2 Athena vs Redshift vs EMR

| | **Athena** | **Redshift** | **EMR** |
|---|---|---|---|
| Model | Serverless SQL over S3 (Presto/Trino) | Provisioned/serverless MPP warehouse | Managed Hadoop/Spark clusters |
| Pay for | **Data scanned** ($5/TB) | Cluster hours or RPU | Cluster hours |
| Best for | Ad-hoc queries, infrequent analysis, log analysis | Repeated complex BI queries, dashboards, joins across large tables | Custom code, ML, non-SQL processing, huge ETL |
| Optimization | **Partition, compress, and convert to Parquet/ORC** | Distribution keys, sort keys, compression | Instance/fleet tuning, Spot task nodes |

### 6.3 Amazon OpenSearch Service

Managed OpenSearch/Elasticsearch for **full-text search** and **log analytics**, with OpenSearch Dashboards for visualization.
- Deploy across 3 AZs with dedicated master nodes for production.
- **UltraWarm** and **Cold storage** tiers back by S3 cut the cost of older indices dramatically.
- **Index State Management** automates rollover and tier transitions.
- **OpenSearch Serverless** for variable workloads.
- Typical pipeline: application/VPC/CloudFront logs → Kinesis Data Firehose / OpenSearch Ingestion → OpenSearch → Dashboards.

---

## 7. Migration and Schema Conversion

- **AWS Database Migration Service (DMS)** — migrates databases with **minimal downtime** using full load plus **change data capture (CDC)**. Supports homogeneous (Oracle→Oracle) and heterogeneous (Oracle→Aurora PostgreSQL) migrations, and targets including S3, Kinesis, OpenSearch, Redshift, and DocumentDB. DMS Serverless removes replication-instance sizing.
- **AWS Schema Conversion Tool (SCT)** — converts schema, stored procedures, and application SQL between different engines; produces an assessment report listing what cannot be converted automatically. Use **SCT + DMS** together for heterogeneous migrations.
- **Babelfish** — lets SQL Server applications talk to Aurora PostgreSQL with little or no code change.
- **AWS DataSync / Snowball** for very large offline data movement feeding a migration.

---

## 8. Worked Scenarios

**Scenario 1 — "Read traffic has grown 10×; writes are unchanged; the RDS primary is saturated."**
Add **read replicas** and route reads to them; add **ElastiCache** for repeated queries. Multi-AZ would not help — the standby serves no traffic.

**Scenario 2 — "We need microsecond reads from DynamoDB without rewriting the data layer."**
**DAX.**

**Scenario 3 — "A DynamoDB table throttles even though provisioned capacity looks adequate overall."**
A **hot partition** from a low-cardinality partition key. Redesign the key (add a suffix/shard, use a high-cardinality attribute), or switch to **on-demand**. Also check whether a GSI is the throttled resource.

**Scenario 4 — "The application queries a non-key attribute and the scan is too slow."**
Create a **GSI** on that attribute and use `Query`.

**Scenario 5 — "Traffic is completely unpredictable and we don't want to manage capacity."**
**DynamoDB on-demand**, or **Aurora Serverless v2** for relational.

**Scenario 6 — "Global users need low-latency reads and writes to the same dataset."**
**DynamoDB global tables** (multi-active), or **Aurora Global Database** with write forwarding for relational.

**Scenario 7 — "Thousands of Lambda functions exhaust database connections."**
**RDS Proxy.**

**Scenario 8 — "Analysts run complex joins across billions of rows and the RDS instance can't cope."**
Move analytics to **Redshift** (or Athena over S3 if queries are ad hoc and infrequent), keeping RDS for OLTP.

**Scenario 9 — "Find all users within three degrees of connection who purchased a product."**
**Amazon Neptune.**

**Scenario 10 — "Migrate an on-prem Oracle database to Aurora PostgreSQL with minimal downtime."**
**SCT** to convert the schema, **DMS** with CDC for the data and ongoing changes, then cut over.

**Scenario 11 — "Session data needs sub-millisecond access and must survive a node failure."**
**ElastiCache for Redis** with Multi-AZ and automatic failover (or **MemoryDB** if it must be durable as a primary store).

**Scenario 12 — "We need to undo an accidental mass delete in Aurora MySQL immediately."**
**Backtrack.**

---

## 9. Quick Decision Table

| Requirement | Answer |
|---|---|
| Relational, managed, standard engines | **Amazon RDS** |
| Relational with high performance, 15 replicas, fast failover | **Amazon Aurora** |
| Relational with unpredictable load, no capacity management | **Aurora Serverless v2** |
| Global relational, RPO ~1 s | **Aurora Global Database** |
| Undo a bad write in seconds (Aurora MySQL) | **Backtrack** |
| Clone production data for test quickly and cheaply | **Aurora fast database cloning** |
| Key-value at any scale, single-digit ms | **DynamoDB** |
| Microsecond DynamoDB reads | **DAX** |
| Query a non-key attribute | **Global Secondary Index** |
| Same partition key, alternate sort key, strong consistency | **Local Secondary Index** (table creation only) |
| Auto-delete expired items | **DynamoDB TTL** |
| React to item changes | **DynamoDB Streams → Lambda** |
| Multi-Region active-active NoSQL | **Global tables** |
| Caching with data structures, persistence, HA | **ElastiCache for Redis** |
| Simple, multi-threaded object cache | **ElastiCache for Memcached** |
| Durable Redis as a primary database | **MemoryDB** |
| MongoDB-compatible | **DocumentDB** |
| Cassandra-compatible | **Keyspaces** |
| Relationship/graph queries | **Neptune** |
| Time-series IoT metrics | **Timestream** |
| Immutable, verifiable audit ledger | **QLDB** |
| Complex BI over terabytes | **Redshift** |
| Ad-hoc SQL over S3, pay per query | **Athena** |
| Query S3 from the warehouse | **Redshift Spectrum** |
| Full-text search / log analytics | **OpenSearch Service** |
| Connection pooling and faster failover | **RDS Proxy** |
| Find the SQL causing database load | **Performance Insights** |
| OS-level DB metrics at 1-second granularity | **Enhanced Monitoring** |
| Migrate with minimal downtime | **DMS (+ SCT for heterogeneous)** |
| Run SQL Server apps on Aurora PostgreSQL | **Babelfish** |

---

## Task 3.4 — Determine High-Performing and/or Scalable Network Architectures

> Networking questions in the exam are usually about **latency** (get the user closer / get traffic onto the AWS backbone), **bandwidth** (choose the right link and instance), or **topology at scale** (how do 200 VPCs and five data centres connect without a mess of peering).

---

## 1. VPC Networking Foundations

### 1.1 Building blocks

- A **VPC** is a logically isolated virtual network in one Region, defined by a CIDR block (**/16 to /28**). You can add up to four secondary CIDRs.
- **Subnets** are AZ-scoped slices of the VPC CIDR. A subnet is **public** if its route table has a route to an **internet gateway**; otherwise it is private. **This routing fact — not a checkbox — is what makes a subnet public.**
- AWS reserves **5 IP addresses per subnet**: network address, VPC router, DNS, future use, and broadcast. A `/24` therefore yields 251 usable addresses.
- **Route tables** are evaluated **most-specific-prefix-first**; the local route for the VPC CIDR always wins and cannot be removed.
- **Elastic network interfaces (ENIs)** carry private IPs, security groups, and (optionally) public/Elastic IPs. The number of ENIs and IPs per instance is limited by instance type — a factor when running many containers in `awsvpc` mode.

### 1.2 Internet and egress paths

| Component | Direction | Notes |
|---|---|---|
| **Internet gateway (IGW)** | Inbound + outbound, IPv4/IPv6 | Horizontally scaled, no bandwidth constraint |
| **NAT gateway** | **Outbound only**, IPv4 | Managed, AZ-scoped, scales **5 → 100 Gbps**, 55,000 simultaneous connections per unique destination. Deploy **one per AZ** for resilience and to avoid cross-AZ data charges |
| **NAT instance** | Outbound only | Self-managed EC2; bandwidth limited by instance type; must **disable source/destination check**. Legacy |
| **Egress-only internet gateway** | Outbound only, **IPv6** | IPv6 addresses are globally routable, so this is the IPv6 equivalent of NAT for egress-only |

### 1.3 IP addressing and planning

- Plan **non-overlapping CIDRs** across all VPCs and on-premises networks — overlapping ranges block peering, Transit Gateway routing, and VPN.
- Leave room for growth; subnets cannot be resized after creation.
- **Amazon VPC IP Address Manager (IPAM)** plans, tracks, allocates, and audits CIDRs across accounts and Regions — the answer for "manage IP space at organization scale."
- **IPv6** addresses in AWS are all public; use an egress-only IGW for outbound-only, and note that **security groups and NACLs need explicit IPv6 rules**.

### 1.4 DNS in the VPC

- **Amazon-provided DNS** at the VPC base + 2 (and `169.254.169.253`), controlled by `enableDnsSupport` and `enableDnsHostnames`.
- **Route 53 Resolver endpoints**: **inbound** endpoints let on-premises resolvers query Route 53 private hosted zones; **outbound** endpoints plus **forwarding rules** let VPC resources resolve on-premises domains. Together they give hybrid DNS.
- **Private hosted zones** serve internal names to associated VPCs.
- **Route 53 Resolver DNS Firewall** blocks queries to malicious or unapproved domains.

---

## 2. Connecting VPCs and Accounts

### 2.1 VPC peering

A one-to-one, private connection between two VPCs (same or different account, same or different Region).

- Uses AWS's private network; **no single point of failure and no bandwidth bottleneck**.
- **Not transitive** — if A peers with B and B peers with C, A cannot reach C. This is the defining limitation.
- CIDRs **must not overlap**.
- Each side must update route tables and security groups (you can reference a security group across a peering connection within the same Region).
- Scaling problem: a full mesh of *n* VPCs needs **n(n−1)/2** connections — 10 VPCs need 45 peerings. This is why Transit Gateway exists.

### 2.2 AWS Transit Gateway

A **regional network hub** that connects VPCs, VPN connections, Direct Connect gateways, and other Transit Gateways in a hub-and-spoke topology.

- Scales to **thousands of VPC attachments**, with up to **50 Gbps per VPC attachment** (and up to 100 Gbps aggregate per flow set with ECMP across multiple VPN tunnels).
- **Transit Gateway route tables** allow segmentation — for example, a "production" route table and a "development" route table so the two environments can each reach shared services but not each other.
- **Transit Gateway peering** connects TGWs across Regions over the AWS backbone (encrypted), enabling a global network.
- **Multicast** support, and **Connect attachments** for SD-WAN appliances using GRE.
- Share the TGW across accounts with **AWS RAM**.
- Billed per attachment-hour plus data processed.

**Exam cue:** "connect many VPCs and on-premises networks with centralized routing" or "VPC peering doesn't scale / isn't transitive" → **Transit Gateway**.

### 2.3 AWS PrivateLink and VPC endpoints

| | **Gateway endpoint** | **Interface endpoint (PrivateLink)** |
|---|---|---|
| Services | **S3 and DynamoDB only** | Most AWS services, your own services, Marketplace services |
| Mechanism | A **route table entry** with a prefix list | An **ENI with a private IP** in your subnet |
| Cost | **Free** | Hourly charge per endpoint per AZ + data processed |
| Scope | Same Region, within the VPC | Can be reached across peering, VPN, Direct Connect, and Transit Gateway |
| DNS | Uses the public service name with a prefix list | Private DNS overrides the service hostname |

- **Gateway Load Balancer endpoints** route traffic to a fleet of third-party security appliances transparently.
- **PrivateLink endpoint services** let you expose your own service (behind an NLB or GWLB) privately to other VPCs/accounts **without peering, without overlapping-CIDR problems, and with one-way access** (consumers reach the provider, not vice versa).
- Policy control: the **`aws:SourceVpce`** condition key restricts an S3 bucket (or other resource) to access only through a specific endpoint.

**Benefits for performance:** traffic stays on the AWS network (lower, more consistent latency), avoids the NAT gateway data-processing charge, and removes the need for internet egress at all.

### 2.4 AWS Resource Access Manager (RAM)

Share resources across accounts without duplicating them: **subnets (VPC sharing)**, Transit Gateways, Route 53 Resolver rules, License Manager configurations, Aurora clusters, and more. **VPC sharing** lets many accounts deploy into subnets of one centrally managed VPC — reducing IP sprawl and the number of VPCs to interconnect.

### 2.5 AWS Cloud WAN

A managed **global** wide-area network: define a network policy centrally and AWS builds and manages the connectivity between Regions, VPCs, and on-premises locations, with segmentation and a unified dashboard. Think "Transit Gateway, but global and policy-driven."

---

## 3. Hybrid Connectivity

### 3.1 Site-to-Site VPN

An IPsec tunnel between your customer gateway and an AWS **virtual private gateway (VGW)** or Transit Gateway.

- Each connection provides **two tunnels in different AZs** for redundancy — configure both.
- Throughput: up to **1.25 Gbps per tunnel**; aggregate more with **ECMP over multiple connections to a Transit Gateway**.
- Runs over the **public internet**, so latency and jitter are variable.
- Quick to set up (minutes to hours), low cost, encrypted by default.
- Routing: static or **BGP** (dynamic, with failover).
- **AWS Client VPN** is the separate, OpenVPN-based service for individual remote users.

### 3.2 AWS Direct Connect (DX)

A **dedicated, private physical connection** from your data centre to AWS through a Direct Connect location.

- **Dedicated connections:** 1, 10, or 100 Gbps physical ports. **Hosted connections** via partners: 50 Mbps to 25 Gbps.
- Benefits: **consistent, predictable latency**, higher and more stable bandwidth, and **reduced data-transfer-out cost** compared with internet egress.
- **Not encrypted by default** — DX provides privacy (it doesn't traverse the internet) but not encryption. For encryption, run an **IPsec VPN over Direct Connect** (or use **MACsec** on supported 10/100 Gbps ports).
- Provisioning takes **weeks to months** (physical cross-connect), which is why a VPN is often used as an interim and then kept as backup.
- **Virtual interfaces (VIFs):**
  - **Private VIF** — reach VPC resources via private IPs (through a VGW or **Direct Connect gateway**)
  - **Public VIF** — reach AWS public endpoints (S3, DynamoDB) over the private link, across all Regions
  - **Transit VIF** — connect to a **Transit Gateway** via a Direct Connect gateway, for many VPCs at once
- **Direct Connect gateway** — a global object that lets one DX connection reach VPCs in **multiple Regions** (not China) and multiple accounts.
- **Link Aggregation Groups (LAG)** bundle multiple connections for more bandwidth and redundancy.

**Resiliency models:** *Development* = one connection; *High resiliency* = two connections at **two different DX locations**; *Maximum resiliency* = two connections at each of two locations, with separate devices. Always consider **VPN as a backup** for a single DX.

### 3.3 Choosing a hybrid link

| Requirement | Answer |
|---|---|
| Needed today, low cost, encryption required | **Site-to-Site VPN** |
| Consistent low latency, high bandwidth, lower egress cost | **Direct Connect** |
| Both — private link with encryption | **VPN over Direct Connect** |
| Many VPCs + on-prem, centralized routing | **Transit Gateway + Transit VIF** |
| VPCs in several Regions over one DX | **Direct Connect gateway** |
| Backup for a DX link | **Site-to-Site VPN failover (BGP)** |
| Individual remote employees | **AWS Client VPN** |

---

## 4. Edge Services for Performance

### 4.1 Amazon CloudFront

A global CDN with **600+ points of presence**. Benefits go far beyond static file caching:

- **Caching** of static *and* dynamic content, with cache policies controlling which headers, cookies, and query strings form the cache key. A tight cache key means a higher hit ratio.
- **TLS terminated at the edge**, so the expensive handshake happens close to the user; the connection to the origin is kept warm and travels the AWS backbone.
- **Origin Shield** — an additional regional caching layer in front of the origin that collapses requests from all edges, dramatically increasing origin offload.
- **Origin groups** for automatic failover between a primary and secondary origin.
- **Compression** (gzip/Brotli) at the edge.
- **HTTP/2 and HTTP/3 (QUIC)** support.
- **Edge compute:** **CloudFront Functions** (sub-millisecond, header/URL manipulation, viewer request/response only) and **Lambda@Edge** (heavier logic, origin request/response too, network access).
- **Security:** AWS WAF integration, AWS Shield Standard always on, **signed URLs and signed cookies** for private content, **Origin Access Control (OAC)** to lock an S3 bucket to CloudFront only, geo-restriction, and field-level encryption.
- **Invalidations** purge cached objects; **versioned object names** (`app.v2.js`) are the better practice.

**Caching best practices:** set long `Cache-Control` max-age for immutable assets, minimize the cache key, forward only the headers you actually vary on, enable Origin Shield for a busy origin, and use `stale-while-revalidate` behaviour to serve during origin problems.

### 4.2 AWS Global Accelerator

Provides **two static anycast IP addresses** advertised from AWS edge locations worldwide. Client traffic enters the **AWS global backbone at the nearest edge** and is routed to the optimal healthy endpoint.

- Improves performance by **up to 60%** by bypassing congested internet paths.
- Works at **layer 4** with **TCP and UDP** — so it supports gaming, VoIP, IoT/MQTT, and any non-HTTP protocol that CloudFront cannot.
- **Health checks with failover in seconds**, independent of DNS TTL caching.
- **Traffic dials** (percentage per endpoint group/Region) and **endpoint weights** for gradual migration and blue/green.
- **Client affinity** options to pin a client to one endpoint.
- Endpoints can be ALBs, NLBs, EC2 instances, or Elastic IPs.

### 4.3 CloudFront vs Global Accelerator

| | **CloudFront** | **Global Accelerator** |
|---|---|---|
| Layer | 7 (HTTP/HTTPS) | 4 (TCP/UDP) |
| Caches content | **Yes** | No |
| Static IPs | No (DNS name) | **Yes, two anycast IPs** |
| Non-HTTP protocols | No | **Yes** |
| Failover speed | Origin group failover | **Seconds, no DNS dependency** |
| Best for | Websites, APIs, media, static assets | Gaming, VoIP, IoT, non-HTTP, static-IP requirements, fast regional failover |

They can be combined: Global Accelerator in front of regional ALBs, CloudFront for cacheable content.

### 4.4 Route 53 for performance

- **Latency-based routing** sends each user to the Region with the lowest measured latency for them.
- **Geolocation** and **geoproximity** (with bias) route by location, for compliance or gradual load shifting.
- **Alias records** are free to query, work at the zone apex, and track AWS resource IP changes automatically.
- **Multivalue answer** returns up to 8 healthy records for simple client-side distribution.
- Lower **TTLs** speed up failover at the cost of more queries — and remember that client-side DNS caching often ignores TTLs, which is the argument for Global Accelerator.

### 4.5 S3 Transfer Acceleration and Multi-Region Access Points

- **Transfer Acceleration** routes uploads/downloads through the nearest **CloudFront edge** and over the AWS backbone to the bucket — valuable for geographically distant clients uploading large objects.
- **S3 Multi-Region Access Points** give a single global endpoint that automatically routes to the lowest-latency bucket among several Regions, with failover.

---

## 5. Instance and Protocol-Level Performance

- **Enhanced networking (ENA)** — up to **100 Gbps**, lower latency and jitter; enabled by default on modern instances.
- **ENA Express (SRD)** — improves single-flow bandwidth and tail latency between supported instances.
- **Elastic Fabric Adapter (EFA)** — OS-bypass networking for MPI/NCCL in HPC and distributed ML; only meaningful inside a **cluster placement group**.
- **Instance bandwidth scales with size** — a network-bound workload may need a bigger or `n`-suffixed instance.
- **Placement groups:** cluster (lowest latency, one AZ), spread (distinct hardware, max 7/AZ), partition (rack-isolated groups for distributed systems).
- **Jumbo frames (MTU 9001)** work within a VPC and over Direct Connect; traffic to the internet, over most VPN, or across some gateways is limited to 1500 bytes.
- **Multiple ENIs / IP addresses** can increase aggregate throughput for some workloads and are required for high container density in `awsvpc` mode.

---

## 6. Load Balancer Selection for Performance

| | **ALB** | **NLB** |
|---|---|---|
| Layer | 7 | **4** |
| Latency | Low | **Ultra-low (~100 µs)** |
| Throughput | Very high | **Millions of requests per second** |
| Static IP | No | **Yes (EIP per AZ)** |
| Protocols | HTTP, HTTPS, gRPC, WebSocket | TCP, UDP, TLS |
| Source IP | `X-Forwarded-For` | **Preserved natively** |
| Routing | Path, host, header, query, method | Port/protocol only |
| Extras | WAF, Cognito auth, redirects, weighted target groups | PrivateLink, extreme scale |

**Cross-zone load balancing** is **on by default and free on ALB**; **off by default on NLB** and billed as inter-AZ traffic when enabled. **Gateway Load Balancer** is for transparently inserting third-party appliances using GENEVE on port 6081.

---

## 7. Monitoring and Troubleshooting Network Performance

- **VPC Flow Logs** — capture accepted/rejected traffic metadata at the VPC, subnet, or ENI level, delivered to CloudWatch Logs, S3, or Kinesis Firehose. They show **source, destination, ports, bytes, packets, and action** — ideal for diagnosing blocked traffic and traffic volumes. They do **not** capture packet payloads, and they miss some traffic (Amazon DNS, instance metadata, license activation, DHCP, Windows activation).
- **VPC Traffic Mirroring** — copies actual packets from an ENI to a monitoring appliance for deep packet inspection.
- **Reachability Analyzer** — static configuration analysis between two endpoints; tells you *which* component (route table, NACL, security group) blocks a path, without sending packets.
- **Network Access Analyzer** — verifies that network access matches your intent (e.g., "no path from the internet to database subnets").
- **CloudWatch Internet Monitor** — measures internet performance and availability affecting your users.
- **CloudWatch Network Monitor** — monitors hybrid network performance between on-premises and AWS.
- **Transit Gateway Network Manager** — visualize and monitor a global network.
- Key metrics: `ProcessedBytes` and `ActiveFlowCount` on NAT gateways and load balancers, `TargetResponseTime`, `SurgeQueueLength`/`RejectedConnectionCount`, EC2 `NetworkIn/Out` and the ENA driver's `bw_in_allowance_exceeded` / `pps_allowance_exceeded` counters (which reveal that you've hit instance network limits).

---

## 8. Worked Scenarios

**Scenario 1 — "Users in Europe and Asia see slow page loads from our us-east-1 web app."**
Put **CloudFront** in front (cache static assets, terminate TLS at the edge, use Origin Shield). For dynamic, consider multi-Region deployment with **Route 53 latency routing** or **Global Accelerator**.

**Scenario 2 — "A UDP-based multiplayer game needs the lowest possible latency and two fixed IPs for firewall whitelisting."**
**AWS Global Accelerator** in front of regional NLBs.

**Scenario 3 — "We have 60 VPCs across 4 accounts and peering has become unmanageable."**
**AWS Transit Gateway** shared via **RAM**, with segmented TGW route tables.

**Scenario 4 — "Our EC2 instances download terabytes from S3 and the NAT gateway cost and throughput are a problem."**
A **gateway VPC endpoint** for S3 — free, no NAT processing charges, traffic stays on the AWS network.

**Scenario 5 — "On-prem analytics needs a consistent 10 Gbps to AWS with predictable latency, and traffic must be encrypted."**
**Direct Connect** (10 Gbps) with an **IPsec VPN over the DX** (or MACsec), plus a backup VPN over the internet.

**Scenario 6 — "A SaaS vendor must expose their service to our VPC without peering or exposing it publicly."**
**AWS PrivateLink** — the vendor publishes an endpoint service behind an NLB; we create an interface endpoint.

**Scenario 7 — "HPC simulation nodes need sub-millisecond inter-node latency."**
**Cluster placement group** + **EFA** + HPC/compute-optimized instances in one AZ.

**Scenario 8 — "Traffic between two instances is being dropped and we can't tell why."**
**Reachability Analyzer** to find the blocking component, then **VPC Flow Logs** to confirm (look for `REJECT` entries — remember a request accepted inbound but rejected outbound points at a **NACL**, since security groups are stateful).

**Scenario 9 — "A single NAT gateway in one AZ is both a bottleneck and a single point of failure."**
Deploy **one NAT gateway per AZ** and point each private subnet's route table at the NAT gateway in its own AZ.

---

## 9. Quick Decision Table

| Requirement | Answer |
|---|---|
| Cache content near users, HTTP/S | **CloudFront** |
| Static anycast IPs, TCP/UDP, fast failover | **Global Accelerator** |
| Route users to the lowest-latency Region | **Route 53 latency-based routing** |
| Connect two VPCs simply | **VPC peering** |
| Connect many VPCs + on-prem centrally | **Transit Gateway** |
| Global, policy-driven WAN | **AWS Cloud WAN** |
| Private access to S3/DynamoDB, free | **Gateway endpoint** |
| Private access to other AWS or partner services | **Interface endpoint (PrivateLink)** |
| Expose your own service privately | **PrivateLink endpoint service (NLB)** |
| Share subnets/TGW across accounts | **AWS RAM** |
| Quick, encrypted hybrid link | **Site-to-Site VPN** |
| Consistent high bandwidth hybrid link | **Direct Connect** |
| Encrypt Direct Connect traffic | **VPN over DX** or **MACsec** |
| One DX reaching VPCs in several Regions | **Direct Connect gateway** |
| DX + many VPCs | **Transit VIF → Transit Gateway** |
| Remote individual users | **Client VPN** |
| Ultra-low latency L4 load balancing, static IP | **NLB** |
| Path/host-based HTTP routing, WAF, auth | **ALB** |
| Insert third-party firewall appliances | **Gateway Load Balancer** |
| Lowest inter-instance latency | **Cluster placement group + EFA** |
| 100 Gbps instance networking | **Enhanced networking (ENA)** on a large/`n` instance |
| Plan and audit CIDRs at scale | **VPC IPAM** |
| See which traffic is allowed/denied | **VPC Flow Logs** |
| Find what blocks a connection | **Reachability Analyzer** |
| Inspect actual packets | **Traffic Mirroring** |
| Resolve on-prem DNS from the VPC | **Route 53 Resolver outbound endpoint + rules** |
| Resolve private hosted zones from on-prem | **Route 53 Resolver inbound endpoint** |
| Speed up long-distance S3 uploads | **S3 Transfer Acceleration** |
| Single global S3 endpoint with failover | **S3 Multi-Region Access Points** |

---

## Task 3.5 — Determine High-Performing Data Ingestion and Transformation Solutions

> This task covers the **data pipeline**: getting data in (batch or streaming), landing it somewhere (usually S3), transforming it, and making it queryable. The recurring exam decisions are **Kinesis vs SQS vs MSK**, **Firehose vs Data Streams**, **Glue vs EMR vs Lambda**, and **Athena vs Redshift**.

---

## 1. Data Pipeline Concepts

### 1.1 The stages

```
SOURCES → INGESTION → STORAGE (raw) → TRANSFORMATION → STORAGE (curated) → ANALYTICS / ML
```

| Stage | Typical AWS services |
|---|---|
| **Ingestion** | Kinesis Data Streams, Data Firehose, MSK, IoT Core, DMS, DataSync, Snowball, Transfer Family, API Gateway, SQS |
| **Raw storage (data lake)** | **Amazon S3**, Lake Formation |
| **Catalog** | **AWS Glue Data Catalog**, Glue crawlers |
| **Transformation** | Glue ETL, Glue DataBrew, EMR, Lambda, Step Functions, Managed Service for Apache Flink, Athena CTAS, Redshift SQL |
| **Curated storage** | S3 (Parquet, partitioned), Redshift, DynamoDB, OpenSearch |
| **Consumption** | Athena, Redshift, QuickSight, OpenSearch Dashboards, SageMaker |
| **Orchestration** | Step Functions, MWAA (Managed Workflows for Apache Airflow), EventBridge, Glue workflows |

### 1.2 Batch vs streaming

| | **Batch** | **Streaming** |
|---|---|---|
| Data arrives | Periodically, in bulk | Continuously, record by record |
| Latency | Minutes to hours | **Milliseconds to seconds** |
| Processing | Over a bounded dataset | Over unbounded data, in windows |
| Services | Glue, EMR, Batch, Lambda, Redshift COPY | Kinesis, MSK, Flink, Lambda |
| Use cases | Nightly reports, daily aggregation, historical reprocessing | Fraud detection, real-time dashboards, clickstream, IoT telemetry, log monitoring |

**Lambda architecture** (speed layer + batch layer) and **Kappa architecture** (one streaming path for everything) are the two canonical designs; AWS pipelines often land streaming data in S3 and then batch-process it, which blends both.

### 1.3 ETL vs ELT

- **ETL** — transform before loading. Classic for warehouses where the target schema is rigid.
- **ELT** — load raw into S3 or Redshift and transform in place with the power of the target engine. More common today because storage is cheap and schema-on-read gives flexibility. Athena and Redshift Spectrum make ELT practical.

---

## 2. Streaming Ingestion

### 2.1 Amazon Kinesis Data Streams

A durable, ordered, replayable stream of records.

**Mechanics:**
- A stream is divided into **shards**. Each shard supports **1 MB/s or 1,000 records/s in**, and **2 MB/s out** (shared across standard consumers).
- A record has a **partition key**, which is hashed to decide the shard. Records with the same partition key go to the same shard and are therefore **ordered within that key**.
- **Retention** is 24 hours by default, extendable to **365 days**, which makes **replay** possible — a key differentiator from SQS, where a message disappears once deleted.
- **Multiple independent consumers** can read the same data simultaneously.

**Capacity modes:**
- **Provisioned** — you manage shard count and can reshard (split/merge). Cheaper at steady, known throughput.
- **On-demand** — scales automatically up to 200 MB/s per stream with no shard management. Better for unpredictable load.

**Consumers:**
- **Standard (shared) consumers** poll and share the 2 MB/s per shard.
- **Enhanced fan-out** gives **each consumer its own 2 MB/s per shard** and pushes data with ~70 ms latency. Use when several consumers need full throughput or low latency.
- **Lambda event source mapping** — by default one concurrent invocation per shard; raise it with the **parallelization factor** (up to 10) for more concurrency while preserving per-partition-key ordering.
- **Kinesis Client Library (KCL)** handles checkpointing and shard rebalancing for custom consumers.

**Producers:** the **Kinesis Producer Library (KPL)** (aggregation and batching for efficiency), the SDK `PutRecords`, the **Kinesis Agent** for log files, and direct integrations from IoT Core, CloudWatch Logs, and EventBridge Pipes.

**Problems and fixes:**
- **`ProvisionedThroughputExceededException`** → a **hot shard** from a skewed partition key, or too few shards. Fix the partition key distribution or add shards.
- **`IteratorAgeMilliseconds` rising** → consumers are falling behind; add consumers/concurrency, use enhanced fan-out, or increase the parallelization factor.

### 2.2 Amazon Data Firehose (formerly Kinesis Data Firehose)

The **fully managed delivery** service: it ingests streaming data and writes it to a destination with **no shard or capacity management**.

- **Destinations:** **S3**, **Redshift** (via S3), **OpenSearch**, Splunk, and HTTP endpoints including partners like Datadog, New Relic, MongoDB.
- **Near real time** — buffered by **size (1–128 MB)** or **time (60–900 seconds)**, so the minimum latency is about **60 seconds**. Firehose is *not* real time; Data Streams is.
- **Built-in transformation** via a Lambda function, **format conversion** to **Parquet or ORC**, compression (GZIP, Snappy, ZIP), and **dynamic partitioning** of S3 prefixes based on record content.
- **No storage/replay** — once delivered, it's gone (failed records go to an S3 error prefix).
- Serverless and auto-scaling; you pay per GB ingested.

**Data Streams vs Firehose — the classic exam pair:**

| | **Kinesis Data Streams** | **Data Firehose** |
|---|---|---|
| Latency | **~200 ms (real time)** | **~60 s minimum (near real time)** |
| Storage/replay | **1–365 days, replayable** | None |
| Scaling | Shards (or on-demand) | **Fully automatic** |
| Consumers | Many custom consumers | Fixed set of destinations |
| Custom processing | Yes, any consumer code | Lambda transform only |
| Management | You manage shards | **Zero** |

Choose **Firehose** when the requirement is "load streaming data into S3/Redshift/OpenSearch with no administration." Choose **Data Streams** when you need **sub-second latency, replay, ordering, or multiple independent consumers**.

### 2.3 Amazon Managed Service for Apache Flink

Formerly Kinesis Data Analytics. Runs **Apache Flink** applications (Java, Scala, Python) or SQL over streaming data for **windowed aggregations, joins across streams, anomaly detection (`RANDOM_CUT_FOREST`), and enrichment** — all in real time, serverless.

Reads from Kinesis Data Streams or MSK; writes to Data Streams, Firehose, Lambda, S3, OpenSearch.

**Exam cue:** "real-time aggregation/analytics on a stream," "compute a moving average over a 5-minute window," "detect anomalies in streaming data."

### 2.4 Amazon MSK (Managed Streaming for Apache Kafka)

Fully managed **Apache Kafka**.

- Choose it when you need **Kafka APIs and ecosystem** — existing Kafka producers/consumers, Kafka Connect, Kafka Streams, Schema Registry — or when migrating an on-premises Kafka cluster.
- **Topics and partitions** instead of shards; message size up to **default 1 MB, configurable higher** (versus Kinesis's hard 1 MB).
- Retention is configurable, including **unlimited with tiered storage**.
- **MSK Serverless** removes broker capacity management.
- More operational knobs and more flexibility than Kinesis, but more to think about.

**Kinesis vs MSK:** Kinesis is simpler, deeply integrated with AWS services, and fully managed with shards; MSK is for Kafka compatibility and portability.

### 2.5 SQS vs Kinesis — a very common confusion

| | **SQS** | **Kinesis Data Streams** |
|---|---|---|
| Model | **Queue** — a message is consumed and deleted | **Stream** — records persist and can be re-read |
| Consumers | Typically one consumer per message | **Many consumers read the same records** |
| Ordering | Standard: best effort; FIFO: per group | **Per shard / partition key** |
| Replay | **No** | **Yes** |
| Scaling | Automatic, unlimited | Shards (or on-demand) |
| Use | Decoupling, work queues, task buffering | Analytics, real-time processing, log/event pipelines, multiple consumers |

"Multiple applications must process the same events" and "we must be able to replay the last 7 days" both point unambiguously to **Kinesis** (or MSK).

### 2.6 AWS IoT Core

Ingests device telemetry over **MQTT, HTTPS, and WebSockets** with device authentication (X.509), a device registry, device shadows, and a **rules engine** that routes messages to Kinesis, Firehose, Lambda, S3, DynamoDB, SNS, or OpenSearch. The front door for IoT pipelines at the scale of millions of devices.

---

## 3. Batch Ingestion and Migration

| Service | Purpose |
|---|---|
| **AWS DMS** | Database migration and **ongoing replication with CDC**; targets include S3, Kinesis, Redshift, OpenSearch, DynamoDB |
| **AWS DataSync** | Scheduled, validated, incremental transfer between on-prem (NFS/SMB/HDFS/object) and S3/EFS/FSx, up to 10× faster than open-source tools |
| **AWS Snow Family** | Offline petabyte-scale transfer when the network would take too long |
| **AWS Transfer Family** | Managed SFTP/FTPS/FTP/AS2 landing directly in S3 or EFS |
| **Storage Gateway** | Continuous hybrid file/volume/tape access backed by S3 |
| **S3 direct upload** | Multipart upload + Transfer Acceleration for large objects from distant clients |
| **Redshift COPY** | Bulk load from S3 in parallel — the correct way to load Redshift (never row-by-row INSERTs) |

---

## 4. Transformation

### 4.1 AWS Glue

A **serverless ETL and data-catalog** service.

- **Glue Data Catalog** — a central metadata repository of databases, tables, schemas, and partitions. It is the metastore used by **Athena, Redshift Spectrum, EMR, and Lake Formation** (and is Hive-metastore compatible).
- **Crawlers** scan S3 (and JDBC sources), **infer schema and partitions**, and populate the catalog on a schedule or trigger.
- **Glue ETL jobs** run **Apache Spark** (Scala/Python) or **Python shell** scripts serverlessly, billed per **DPU-hour** with a 1-minute minimum. **Glue Studio** gives a visual job editor; **job bookmarks** track what has already been processed so incremental runs don't reprocess old data.
- **Glue Streaming ETL** processes Kinesis/Kafka streams with Spark Structured Streaming.
- **Glue DataBrew** — a **visual, no-code** data preparation tool with 250+ built-in transformations, aimed at analysts for cleaning and normalizing data.
- **Glue Data Quality** defines and monitors data-quality rules.
- **Glue workflows and triggers** orchestrate multi-job pipelines.

**Glue vs EMR:** Glue is serverless, quick to start, and ideal for standard ETL and cataloguing. EMR gives you full cluster control, any framework/version, custom libraries, Spot cost optimization, and is better for very large or highly customized processing.

### 4.2 Amazon EMR

Managed Hadoop ecosystem: **Spark, Hive, Presto/Trino, HBase, Flink, Hudi, Iceberg**.

- **Node types:** **master** (coordination), **core** (compute + HDFS — losing them loses data), **task** (compute only — **ideal for Spot instances**).
- **Instance fleets** with mixed types and Spot allocation strategies; **managed scaling** resizes the cluster automatically.
- **EMRFS** lets jobs read/write S3 directly, which decouples storage from compute so clusters can be **transient** (spin up, run the job, terminate) — a major cost pattern.
- Variants: **EMR on EC2**, **EMR on EKS** (run Spark on an existing Kubernetes cluster), **EMR Serverless** (no cluster at all).

### 4.3 Lambda and Step Functions for transformation

- **Lambda** suits lightweight, event-driven transformation: an S3 `ObjectCreated` event triggers a function that validates, converts, enriches, or routes the object. Constrained by the **15-minute timeout**, 10 GB memory, and 10 GB `/tmp`.
- **Step Functions** orchestrates multi-stage pipelines with retries, parallel branches, and **Distributed Map** for fanning out over millions of S3 objects.
- **MWAA (Managed Workflows for Apache Airflow)** is the choice when the team already uses Airflow DAGs or needs complex scheduling and dependency management.

### 4.4 File formats and partitioning — the biggest performance lever

Converting raw CSV/JSON into **columnar, compressed, partitioned** files routinely cuts query time and cost by 90%+.

| Format | Type | Notes |
|---|---|---|
| CSV / JSON | Row, text | Human readable, large, no schema enforcement, slow to query |
| **Parquet** | **Columnar** | Best for analytics; column pruning, predicate pushdown, excellent compression. **The default recommendation.** |
| **ORC** | Columnar | Similar benefits, strong in the Hive ecosystem |
| **Avro** | Row, binary | Good for streaming/write-heavy and schema evolution |

**Compression:** **Snappy** (fast, splittable with Parquet/ORC — the usual choice), **GZIP** (better ratio, not splittable for text), **BZIP2** (splittable, slow), **ZSTD** (good balance).

**Partitioning:** organize S3 keys as `s3://bucket/table/year=2026/month=10/day=23/`. Queries with a `WHERE year=2026 AND month=10` clause then scan only those prefixes — **partition pruning**. Use **Hive-style `key=value`** naming so Athena and Glue detect partitions automatically; run `MSCK REPAIR TABLE` or use **partition projection** for very large partition counts.

**Other optimizations:** avoid many tiny files (compact into 128 MB–1 GB objects), bucket/sort data on common join keys, and use **open table formats** (**Apache Iceberg**, **Hudi**, **Delta Lake**) when you need ACID transactions, row-level updates/deletes, and time travel on a data lake. Athena and EMR both support Iceberg.

---

## 5. Query and Analytics Layer

### 5.1 Amazon Athena

**Serverless, interactive SQL (Trino/Presto) directly over S3** using the Glue Data Catalog.

- **Pay per terabyte scanned** (~$5/TB) — so every optimization that reduces bytes scanned reduces cost proportionally: **columnar formats, compression, partitioning, and selecting only needed columns**.
- **CTAS (`CREATE TABLE AS SELECT`)** converts and repartitions data in place — the standard trick to turn raw CSV into partitioned Parquet.
- **Federated queries** reach other data sources (RDS, DynamoDB, Redshift, CloudWatch, on-prem) through Lambda connectors.
- **Workgroups** separate teams, enforce **per-query and per-workgroup data scan limits**, and track cost.
- **Athena for Apache Spark** runs notebooks serverlessly.
- Best for ad-hoc analysis, log querying, and infrequent reporting. Not for high-concurrency sub-second dashboards — that is Redshift's job.

### 5.2 Amazon Redshift (analytics perspective)

Columnar MPP warehouse for repeated, complex, high-concurrency analytical queries. Key performance items: **distribution style** (KEY/ALL/EVEN/AUTO), **sort keys** and zone maps, **compression encodings**, **COPY** for parallel bulk loads, **Concurrency Scaling**, **materialized views**, **result caching**, **RA3 + managed storage**, **Spectrum** for S3, and **zero-ETL** ingestion from Aurora/RDS/DynamoDB.

**Athena vs Redshift:** Athena if the data lives in S3, queries are ad hoc, and you don't want a cluster. Redshift if you run the same complex queries repeatedly at high concurrency with low latency, and want to join across large curated tables.

### 5.3 Amazon OpenSearch Service

For **full-text search** and **log analytics** with near-real-time ingestion and rich dashboards. Typical pipeline: logs → Firehose (or OpenSearch Ingestion) → OpenSearch → Dashboards. Use **UltraWarm/Cold** tiers and **Index State Management** to control cost as indices age.

### 5.4 Amazon QuickSight

Serverless BI with **SPICE** (an in-memory engine for fast, repeated queries), ML Insights, embedded dashboards, and paginated reports. Connects to Athena, Redshift, RDS, S3, and more.

### 5.5 AWS Lake Formation

Builds and secures a data lake on S3: centralizes **fine-grained permissions** (database, table, **column**, **row**, and cell level) across Athena, Redshift Spectrum, EMR, and Glue, with **tag-based access control** and blueprints for ingestion. The answer to "grant analysts access to some columns but not the PII ones."

### 5.6 Amazon DataZone / Glue Data Quality
DataZone provides business-level data cataloguing, discovery, and governed sharing across an organization; Glue Data Quality monitors rules on datasets. Both appear occasionally in governance-flavoured questions.

---

## 6. Reference Architectures

**Real-time clickstream analytics**
```
Web/app → Kinesis Data Streams → Managed Service for Apache Flink (windowed aggregation)
            ├→ Data Firehose → S3 (Parquet, partitioned) → Athena / Redshift Spectrum
            └→ Lambda → DynamoDB → live dashboard (API Gateway + WebSocket)
```

**Serverless data lake**
```
Sources → (Firehose / DataSync / DMS) → S3 raw
        → Glue crawler → Glue Data Catalog
        → Glue ETL (convert to Parquet, partition) → S3 curated
        → Athena / Redshift Spectrum → QuickSight
        → Lake Formation for fine-grained permissions
```

**IoT telemetry**
```
Devices → IoT Core (MQTT) → Rules engine
        ├→ Kinesis Data Streams → Flink → alerts (SNS)
        ├→ Firehose → S3 → Athena
        └→ Timestream → Grafana / QuickSight
```

**Log analytics**
```
CloudWatch Logs / agents → Firehose → OpenSearch (hot) → Dashboards
                                   └→ S3 (UltraWarm/archive) → Athena
```

**Near-real-time warehouse without ETL**
```
Aurora / RDS MySQL / DynamoDB → zero-ETL integration → Redshift → QuickSight
```

---

## 7. Worked Scenarios

**Scenario 1 — "Stream clickstream data into S3 as Parquet with the least operational overhead."**
**Amazon Data Firehose** with record format conversion to Parquet and dynamic partitioning. No shards to manage.

**Scenario 2 — "Three different teams must each process the same event stream independently, and we need to replay the last week."**
**Kinesis Data Streams** with 7-day retention and **enhanced fan-out** consumers. SQS cannot replay; Firehose has no consumers.

**Scenario 3 — "Athena queries cost too much and take minutes."**
Convert to **Parquet with Snappy**, **partition** by date, compact small files, and select only required columns. Optionally add workgroup scan limits.

**Scenario 4 — "We need a moving 5-minute average and anomaly detection on sensor data in real time."**
**Managed Service for Apache Flink** reading from Kinesis Data Streams.

**Scenario 5 — "Migrate an on-prem Oracle database to Redshift with continuous replication."**
**AWS SCT** for schema plus **DMS with CDC** (optionally landing in S3 and loading with COPY).

**Scenario 6 — "Analysts want to clean and normalize data without writing code."**
**AWS Glue DataBrew.**

**Scenario 7 — "Catalogue our S3 data lake automatically so Athena can query it."**
**Glue crawlers** → **Glue Data Catalog** → Athena.

**Scenario 8 — "Grant the marketing team access to the orders table but hide the credit-card column."**
**AWS Lake Formation** column-level permissions.

**Scenario 9 — "Our Kinesis consumers keep falling behind (IteratorAge climbing)."**
Add shards if writes are throttled, enable **enhanced fan-out**, increase the Lambda **parallelization factor**, or scale out consumers. Check for a hot partition key.

**Scenario 10 — "We already run Kafka on-premises and want to move to AWS with no code changes."**
**Amazon MSK** (or MSK Serverless).

**Scenario 11 — "Nightly Spark job on 50 TB, cost is the priority, job is restartable."**
**Transient EMR cluster** reading from S3 (EMRFS) with **task nodes on Spot**, terminating on completion. Or **EMR Serverless**.

---

## 8. Quick Decision Table

| Requirement | Answer |
|---|---|
| Real-time stream, multiple consumers, replay | **Kinesis Data Streams** |
| Load streaming data to S3/Redshift/OpenSearch, zero admin | **Amazon Data Firehose** |
| Real-time windowed analytics / anomaly detection | **Managed Service for Apache Flink** |
| Kafka compatibility | **Amazon MSK** |
| Decouple producers/consumers, work queue | **Amazon SQS** |
| Millions of IoT devices over MQTT | **AWS IoT Core** |
| Serverless ETL + data catalog | **AWS Glue** |
| Automatically infer schema from S3 | **Glue crawler** |
| No-code visual data prep | **Glue DataBrew** |
| Big Spark/Hadoop clusters, custom frameworks, Spot savings | **Amazon EMR** |
| Lightweight event-driven transform | **Lambda** |
| Orchestrate a multi-step pipeline | **Step Functions** (or **MWAA** for Airflow) |
| Ad-hoc SQL over S3, pay per query | **Amazon Athena** |
| Repeated complex BI at high concurrency | **Amazon Redshift** |
| Query S3 from Redshift | **Redshift Spectrum** |
| Full-text search / log exploration | **OpenSearch Service** |
| Dashboards and BI | **Amazon QuickSight** |
| Column/row-level data lake permissions | **AWS Lake Formation** |
| Reduce Athena cost | **Parquet + Snappy + partitioning** |
| ACID updates/deletes and time travel on S3 | **Apache Iceberg / Hudi** |
| Database migration with CDC | **AWS DMS** |
| Scheduled on-prem → AWS file sync | **AWS DataSync** |
| Petabytes with poor bandwidth | **AWS Snowball Edge** |
| Load Redshift efficiently | **COPY from S3** |
| Analytics on operational data with no pipeline | **Zero-ETL integration** |

---

# Domain 4 — Design Cost-Optimized Architectures (20%)


## Task 4.1 — Design Cost-Optimized Storage Solutions

> Storage cost questions are mostly about **matching the access pattern to the right tier** and **automating the movement between tiers**. You also need to know the cost-management toolkit, because it is referenced across all four Domain 4 tasks.

---

## 1. The AWS Cost-Management Toolkit

These tools appear throughout Domain 4; learn which one answers which question.

| Tool | What it does | The question it answers |
|---|---|---|
| **AWS Cost Explorer** | Visualize and filter up to 12 months of historical cost and usage, with **12-month forecasts**, grouping by service, account, tag, Region; also surfaces **rightsizing recommendations** and RI/Savings Plans recommendations | "Where is our money going, and what will it be next month?" |
| **AWS Budgets** | Set cost, usage, RI/SP utilization or coverage budgets with **alerts** (SNS/email/Chatbot) and **Budget Actions** (apply an IAM policy, stop instances, target an SCP) | "Alert me — or act — before we overspend" |
| **AWS Cost and Usage Report (CUR)** | The most granular billing data (hourly/resource level) delivered to S3 for Athena/Redshift/QuickSight analysis | "I need the raw data for custom chargeback analysis" |
| **AWS Cost Anomaly Detection** | ML-based detection of unusual spend, with alerts | "Tell me when something unexpected starts costing money" |
| **AWS Trusted Advisor** | Checks across cost, performance, security, fault tolerance, service limits — including **idle load balancers, underutilized EBS volumes and instances, unassociated Elastic IPs**. Full checks require Business/Enterprise Support | "What obvious waste can I clean up right now?" |
| **AWS Compute Optimizer** | ML-driven **rightsizing** recommendations for EC2, ASGs, EBS volumes, Lambda functions, ECS on Fargate, and RDS | "Which specific instance type/size should I move to?" |
| **AWS Pricing Calculator** | Model costs **before** deploying | "What will this architecture cost?" |
| **S3 Storage Lens** | Organization-wide S3 usage and activity metrics with cost-efficiency recommendations | "Which buckets and prefixes are wasting money?" |
| **S3 Storage Class Analysis** | Analyzes access patterns per bucket/prefix to recommend lifecycle transition ages | "When should objects move to IA?" |
| **AWS Billing Conductor** | Custom billing views and rates for internal chargeback / resellers | "Show each business unit a customized bill" |
| **Cost Categories & cost allocation tags** | Group costs by team, project, environment; **tags must be activated in the Billing console** and only apply from activation forward | "Split the bill by team" |
| **Consolidated billing (Organizations)** | One bill, **shared volume discounts**, and **shared RI/Savings Plans benefits** across accounts | "Reduce cost across many accounts" |

**Exam cue pairs to memorize:** historical analysis and forecasting → **Cost Explorer**; proactive alerting/action → **Budgets**; granular raw data → **CUR**; unexpected spikes → **Cost Anomaly Detection**; quick waste checks → **Trusted Advisor**; specific resize recommendations → **Compute Optimizer**.

---

## 2. How S3 Billing Actually Works

You pay for several independent dimensions, and the exam often hinges on one of the less obvious ones:

1. **Storage per GB-month** — varies enormously by storage class
2. **Requests** — PUT/COPY/POST/LIST and GET/SELECT, priced per 1,000; **colder classes have higher request costs**
3. **Data transfer OUT to the internet** — the big one; transfer **IN is free**, and transfer to **CloudFront is free**
4. **Retrieval fees** — charged per GB for Standard-IA, One Zone-IA, and all Glacier classes
5. **Early deletion charges** — if you delete before the **minimum storage duration**, you still pay for the full duration
6. **Minimum billable object size** — 128 KB for IA/Glacier Instant, 40 KB for Glacier Flexible/Deep Archive
7. **Management features** — Intelligent-Tiering monitoring fee per object, Inventory, Storage Lens advanced metrics, replication, Object Lambda

**The classic trap:** moving millions of **small** objects to Glacier Deep Archive can *increase* cost, because each object is billed at the 40 KB minimum plus per-object transition request charges. Aggregate small files first.

**The second classic trap:** moving frequently accessed data to IA saves on storage but incurs **retrieval fees** on every access, often costing more overall. IA is for data accessed roughly **less than once a month**.

---

## 3. S3 Storage Classes — Cost View

| Class | Relative storage cost | Retrieval fee | Min duration | Min billable size | AZs | When it's the cheapest correct answer |
|---|---|---|---|---|---|---|
| **S3 Standard** | Baseline (highest) | None | — | — | ≥3 | Frequently accessed, short-lived, or unpredictable *and* latency-critical |
| **Intelligent-Tiering** | Standard rate in the frequent tier, dropping automatically; small **monitoring fee per object** | **None** for automatic tiers | — | 128 KB for auto-tiering | ≥3 | **Unknown or changing access patterns** — the safe default |
| **Standard-IA** | ~45% less than Standard | Per GB | **30 days** | 128 KB | ≥3 | Accessed less than monthly but needs millisecond access |
| **One Zone-IA** | ~20% less than Standard-IA | Per GB | **30 days** | 128 KB | **1** | Re-creatable or secondary copies; accept AZ-loss risk |
| **Glacier Instant Retrieval** | ~68% less than Standard | Per GB (higher) | **90 days** | 128 KB | ≥3 | Archive accessed ~quarterly that still needs **millisecond** retrieval |
| **Glacier Flexible Retrieval** | ~80%+ less | Per GB; Expedited 1–5 min / Standard 3–5 h / **Bulk free 5–12 h** | **90 days** | 40 KB | ≥3 | Archive with occasional, non-urgent retrieval |
| **Glacier Deep Archive** | **Cheapest** (~95% less) | Per GB; Standard 12 h / Bulk 48 h | **180 days** | 40 KB | ≥3 | Long-term compliance retention, rarely if ever retrieved |
| **Express One Zone** | Higher storage, **much lower request cost** | None | — | — | 1 | Very high request rates with low latency; cheaper *per request*, not per GB |

**Decision logic:**
- Accessed daily → **Standard**
- Access pattern unknown or variable → **Intelligent-Tiering**
- Accessed less than monthly, needs instant access → **Standard-IA**
- Easily re-created (thumbnails, transcodes, logs you can regenerate) → **One Zone-IA**
- Accessed a few times a year, instant access required → **Glacier Instant Retrieval**
- Archive, hours acceptable → **Glacier Flexible Retrieval**
- 7–10 year retention, almost never read → **Glacier Deep Archive**

---

## 4. Lifecycle Policies

Lifecycle rules are the automation that makes tiering real. A rule has a **filter** (prefix, tag, object size) and **actions**.

**Transition actions** move objects between classes as they age. Example policy:

```json
{
  "Rules": [{
    "ID": "log-tiering",
    "Status": "Enabled",
    "Filter": { "Prefix": "logs/" },
    "Transitions": [
      { "Days": 30,  "StorageClass": "STANDARD_IA" },
      { "Days": 90,  "StorageClass": "GLACIER_IR" },
      { "Days": 365, "StorageClass": "DEEP_ARCHIVE" }
    ],
    "Expiration": { "Days": 2555 },
    "NoncurrentVersionTransitions": [
      { "NoncurrentDays": 30, "StorageClass": "GLACIER" }
    ],
    "NoncurrentVersionExpiration": { "NoncurrentDays": 365 },
    "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 7 }
  }]
}
```

**Four actions that save money and are frequently forgotten:**
1. **`AbortIncompleteMultipartUpload`** — failed multipart uploads leave orphaned parts you pay for **forever** and which don't appear in the console object list. Always set this (7 days is typical).
2. **`NoncurrentVersionExpiration`** — in a versioned bucket, every overwrite keeps the old version. Without this rule, storage grows without bound.
3. **`ExpiredObjectDeleteMarker`** — clean up delete markers left behind when all versions of an object are gone.
4. **`Expiration`** — actually delete data you are not required to keep. Deleting is the ultimate cost optimization.

**Constraints:** objects must be ≥30 days in Standard before transitioning to Standard-IA or One Zone-IA; transitions only move "down" the hierarchy; there are per-object transition request charges, so transitioning millions of tiny objects may not pay off.

**Deciding thresholds:** use **S3 Storage Class Analysis** (per bucket/prefix access analysis with recommended ages) and **S3 Storage Lens** (organization-wide usage, with recommendations like "enable lifecycle rules on these buckets").

---

## 5. Reducing S3 Data Transfer and Request Costs

- **Transfer IN is free.** **Transfer OUT to the internet is the expensive direction.**
- **S3 → CloudFront is free**, and CloudFront's per-GB egress is cheaper than S3's. **Serving content through CloudFront reduces both transfer cost and origin requests** — a double saving that the exam loves.
- **VPC gateway endpoint for S3 is free** and removes **NAT gateway data-processing charges** (~$0.045/GB) for instances in private subnets pulling from S3. For a workload moving terabytes, this is a very large saving.
- **Same-Region, same-AZ** traffic is cheapest; **cross-AZ traffic costs** in both directions; **cross-Region** costs more.
- **S3 Select / Athena** reduce the volume of data transferred and processed by filtering server-side.
- **Requester Pays** shifts request and transfer costs to the consumer for large shared datasets.
- **Compress** objects and **batch small requests**; request charges on millions of tiny objects can exceed storage charges.
- **Aggregate small files** (e.g., combine log files into larger Parquet objects) to reduce both request count and minimum-size waste.

---

## 6. Cost-Optimizing EBS

| Action | Saving |
|---|---|
| **Migrate gp2 → gp3** | ~20% cheaper per GB, and IOPS/throughput are **decoupled from size**, so you stop over-provisioning capacity just to get IOPS. Usually the single biggest, lowest-risk EBS win. |
| **Delete unattached volumes** | A detached volume bills at full price indefinitely. Trusted Advisor and Compute Optimizer flag these. |
| **Right-size over-provisioned volumes** | Elastic Volumes allows live resize — but **you can only grow**, so plan carefully; otherwise snapshot and restore to a smaller volume. |
| **Use st1/sc1 for throughput/cold data** | HDD is far cheaper per GB than SSD for sequential workloads and archives (not bootable). |
| **Delete old snapshots** | Snapshots are incremental but accumulate. Use **Data Lifecycle Manager** retention policies. |
| **EBS Snapshot Archive** | Up to **75% cheaper** for snapshots kept long term; 90-day minimum, 24–72 h restore. |
| **Avoid unnecessary Fast Snapshot Restore** | FSR is billed per snapshot **per AZ per hour** and is expensive if left enabled. |
| **Set `DeleteOnTermination`** appropriately | Prevents orphaned root volumes. |
| **Use instance store** where data is ephemeral | Included in the instance price — no extra storage charge. |

---

## 7. Cost-Optimizing EFS and FSx

**EFS:**
- **Lifecycle management** moves files not accessed for N days to **Infrequent Access** (up to ~92% cheaper) and then **Archive**, with optional transition back on access. There is a per-GB retrieval fee for IA, so set the transition period sensibly.
- **EFS One Zone** is ~47% cheaper than Standard — appropriate for dev/test and re-creatable data.
- **Throughput mode**: **Elastic** charges for what you use (best for spiky); **Bursting** is cheapest for large, lightly used file systems; **Provisioned** is only worth it for small file systems needing constant high throughput — check whether you are paying for provisioned throughput you don't use.
- Delete stale data; EFS bills for every GB stored.

**FSx:**
- **FSx for Windows**: choose **HDD** storage instead of SSD where latency permits; enable **data deduplication** (often 50–60% savings on user shares); use **Single-AZ** for non-critical workloads.
- **FSx for Lustre**: use **scratch** file systems for transient jobs (cheaper, no replication) and **link to S3** so the durable copy lives in cheap object storage; delete the file system when the job ends.
- **FSx for ONTAP**: automatic tiering to the **capacity pool** moves cold data to much cheaper storage.

---

## 8. Backup, Archive and Data Lifecycle Cost

- **AWS Backup** centralizes policies; the cost lives in the underlying storage, so tune **retention** aggressively and use **cold storage tiers** for long-term recovery points (note the 90-day minimum for cold storage).
- **Over-retention is the most common backup waste.** Keep daily backups for weeks, not years; keep monthly/annual backups in Deep Archive if compliance requires long retention.
- **Cross-Region copies double storage cost and add transfer cost** — do it only for data that truly needs regional DR.
- **S3 Glacier Deep Archive** is the cheapest durable home for compliance archives.
- **Tape Gateway** replaces physical tape libraries with S3/Glacier-backed virtual tapes, eliminating tape hardware and offsite storage costs.
- **S3 Object Lock / Vault Lock** add compliance guarantees without extra storage cost, but note that **locked objects cannot be deleted**, so a mistake in retention settings is expensive and irreversible.

---

## 9. Choosing the Cheapest Correct Storage Service

| Need | Cheapest appropriate option |
|---|---|
| Static website assets | **S3 + CloudFront** (not EC2 web servers) |
| Shared Linux files, mostly cold | **EFS with lifecycle to IA/Archive**, or One Zone |
| Shared Linux files, dev/test | **EFS One Zone** |
| Log archive, 7-year retention | **S3 Glacier Deep Archive** via lifecycle |
| Backups of EC2 volumes | **EBS snapshots + DLM**, archive old ones |
| Large sequential analytics scans on block storage | **st1 HDD** |
| Temporary scratch space | **Instance store** or **FSx for Lustre scratch** |
| Petabyte data lake | **S3** with Parquet + partitioning (cheap storage, cheap queries) |
| On-prem file access with cloud economics | **Storage Gateway** |
| Replace tape infrastructure | **Tape Gateway** |
| Unknown access pattern | **S3 Intelligent-Tiering** |

---

## 10. Worked Scenarios

**Scenario 1 — "Logs are written daily, queried occasionally for 30 days, then kept 7 years for compliance."**
Lifecycle: Standard → **Standard-IA at 30 days** → **Glacier Flexible or Instant at 90 days** → **Deep Archive at 365 days** → expire at 7 years. Compact small log files into larger objects first.

**Scenario 2 — "Our S3 bill keeps growing although we delete objects regularly."**
The bucket is **versioned** — deletes only add delete markers. Add **NoncurrentVersionExpiration** and **ExpiredObjectDeleteMarker** rules, and **AbortIncompleteMultipartUpload**. Confirm with **Storage Lens**.

**Scenario 3 — "Access patterns for a new dataset are unknown and the team fears retrieval fees."**
**S3 Intelligent-Tiering** — automatic tiering with **no retrieval fees** for the automatic access tiers.

**Scenario 4 — "Thumbnails are regenerable and accessed rarely."**
**S3 One Zone-IA** — cheapest resilient-enough option for re-creatable data.

**Scenario 5 — "A large media library is served globally and the S3 data-transfer bill is huge."**
Put **CloudFront** in front: S3→CloudFront transfer is free, CloudFront egress is cheaper, and caching slashes origin requests.

**Scenario 6 — "EC2 instances in private subnets pull 50 TB/month from S3 through a NAT gateway."**
Add a **gateway VPC endpoint for S3** — free, and it eliminates NAT data-processing charges.

**Scenario 7 — "We have 400 gp2 volumes sized at 1 TB purely to get 3,000 IOPS."**
Migrate to **gp3** and provision IOPS independently — smaller volumes, ~20% lower per-GB price, same or better performance.

**Scenario 8 — "Compliance requires 10-year retention of records that will almost certainly never be read."**
**S3 Glacier Deep Archive** with **Object Lock** in compliance mode if immutability is required.

**Scenario 9 — "An EFS file system holds 40 TB, but only 2 TB is touched each month."**
Enable **EFS lifecycle management** to move untouched files to **IA** (and **Archive**), saving up to ~92% on the cold portion.

---

## 11. Quick Decision Table

| Scenario | Answer |
|---|---|
| Unknown or changing access pattern | **S3 Intelligent-Tiering** |
| Infrequent access, instant retrieval | **S3 Standard-IA** |
| Re-creatable, infrequent | **S3 One Zone-IA** |
| Archive, millisecond retrieval needed | **Glacier Instant Retrieval** |
| Archive, hours acceptable | **Glacier Flexible Retrieval** |
| Cheapest long-term archive | **Glacier Deep Archive** |
| Automate tiering and deletion | **S3 Lifecycle policies** |
| Orphaned multipart parts | **AbortIncompleteMultipartUpload rule** |
| Versioned bucket growing forever | **NoncurrentVersionExpiration** |
| Decide transition ages | **S3 Storage Class Analysis** |
| Org-wide S3 waste visibility | **S3 Storage Lens** |
| Cut S3 egress cost | **CloudFront** (free S3→CF transfer) |
| Cut NAT charges for S3 traffic | **Gateway VPC endpoint (free)** |
| Shift data costs to consumers | **Requester Pays** |
| Cheaper general-purpose block storage | **gp3** |
| Cheap sequential block storage | **st1** |
| Long-term snapshot retention | **EBS Snapshot Archive** |
| Automate snapshot retention | **Data Lifecycle Manager** |
| Cold EFS data | **EFS lifecycle to IA/Archive** |
| Dev/test shared file system | **EFS One Zone** |
| Windows shares costing too much | **HDD storage + data deduplication** |
| Transient HPC file system | **FSx for Lustre scratch + S3 link** |
| Replace physical tape | **Tape Gateway** |
| Find idle/unattached resources | **Trusted Advisor** |
| Rightsizing recommendations | **Compute Optimizer** |
| Historical cost analysis and forecast | **Cost Explorer** |
| Alert or act on overspend | **AWS Budgets (+ Budget Actions)** |
| Granular billing data for analysis | **Cost and Usage Report** |
| Detect unexpected spend spikes | **Cost Anomaly Detection** |

---

## Task 4.2 — Design Cost-Optimized Compute Solutions

> Compute is usually the largest line on an AWS bill. Four levers produce nearly all the savings: **the right purchasing model**, **the right size**, **the right amount of running time**, and **the right compute service**. The exam tests all four.

---

## 1. EC2 Purchasing Options

### 1.1 The full set

| Option | Discount vs On-Demand | Commitment | Can be interrupted? | Best for |
|---|---|---|---|---|
| **On-Demand** | Baseline | None | No | Spiky, short-term, unpredictable, first-time workloads, dev/test during work hours |
| **Savings Plans** | Up to **72%** | **1 or 3 years**, a $/hour spend commitment | No | Steady-state usage with flexibility needs |
| **Reserved Instances** | Up to **72%** | 1 or 3 years, specific attributes | No | Steady-state with known instance type/Region |
| **Spot Instances** | Up to **90%** | None | **Yes — 2-minute warning** | Fault-tolerant, stateless, flexible, restartable workloads |
| **Dedicated Instances** | Premium | None or reserved | No | Compliance requiring isolated hardware |
| **Dedicated Hosts** | Premium (can be reserved) | None or 1/3 years | No | **BYOL licensing per physical core/socket**, strict compliance |
| **Capacity Reservations** | **No discount** (pay On-Demand) | None (or combine with SP/RI for discount) | No | **Guarantee capacity** in a specific AZ, e.g., for DR or a known event |

**Key distinction:** a **Capacity Reservation** guarantees *capacity* but gives no discount; a **Savings Plan or RI** gives a *discount* but no capacity guarantee (except a **zonal RI**, which provides both). To get both, buy a Capacity Reservation and cover it with a Savings Plan.

### 1.2 Savings Plans in detail

| Type | Flexibility | Discount |
|---|---|---|
| **Compute Savings Plans** | **Maximum** — applies across **EC2 (any instance family, size, OS, tenancy, Region)**, **Fargate**, and **Lambda** | Up to **66%** |
| **EC2 Instance Savings Plans** | Locked to an **instance family in a Region**, but flexible on size, OS, and AZ | Up to **72%** |
| **SageMaker Savings Plans** | SageMaker usage | Up to 64% |

You commit to spending a given **dollar amount per hour** for 1 or 3 years. Usage up to that amount is billed at the discounted rate; usage beyond it is billed On-Demand. Payment options: **All Upfront** (biggest discount) > **Partial Upfront** > **No Upfront**.

**Savings Plans vs Reserved Instances:** Savings Plans are simpler and more flexible and are generally the modern recommendation. RIs retain two advantages: **Standard RIs can be sold on the Reserved Instance Marketplace**, and **zonal RIs provide a capacity reservation**. RIs are still the only commitment model for **RDS, Redshift, ElastiCache, OpenSearch, and DynamoDB** — Savings Plans do not cover those services.

**RI types:** **Standard** (up to 72%, can change AZ/size within a family, **can be sold**) and **Convertible** (up to 66%, can be **exchanged** for a different family/OS/tenancy, cannot be sold). **Scope:** *regional* RIs give AZ flexibility and instance-size flexibility within a family; *zonal* RIs give a capacity reservation in one AZ but no flexibility.

**Organization-wide:** with **consolidated billing**, unused RI and Savings Plan benefits are **shared across all accounts** in the organization by default (can be disabled per account). This is a significant and frequently tested cost advantage of AWS Organizations.

### 1.3 Spot Instances in depth

Spot uses spare EC2 capacity at up to **90% off**, reclaimed with a **2-minute interruption notice** (delivered through instance metadata and an EventBridge event) when AWS needs the capacity back.

**Suitable workloads:** batch processing, CI/CD build agents, big-data processing (EMR **task nodes**), containerized stateless services, rendering, scientific computing, machine-learning training with checkpointing, and any queue-driven worker fleet.
**Unsuitable:** databases, stateful single-instance applications, anything that cannot tolerate sudden termination, and licensed software with per-launch costs.

**Using Spot well:**
- **Diversify** across many instance types and AZs — capacity for one type may disappear while others remain. Use a **mixed instances policy** in an ASG or an **EC2 Fleet / Spot Fleet**.
- Use the **`price-capacity-optimized`** allocation strategy, which balances low price with low interruption probability (preferred over `lowest-price`, which chases the cheapest pool and gets interrupted most).
- Enable **Capacity Rebalancing** so the ASG proactively launches a replacement when a Spot instance is flagged at elevated risk.
- **Checkpoint** work and make it idempotent; drain connections on the 2-minute warning.
- **Mix On-Demand and Spot** in one ASG: a baseline of On-Demand for guaranteed capacity plus Spot for the elastic portion (e.g., `OnDemandBaseCapacity: 2`, then 20% On-Demand / 80% Spot above the base).
- **Spot Blocks** (defined-duration) are no longer offered to new customers — don't choose them.
- **Fargate Spot** applies the same model to containers (up to 70% off).

### 1.4 Choosing the purchasing model

| Workload | Answer |
|---|---|
| Steady 24/7 baseline | **Compute Savings Plan (3-year, all upfront for max discount)** |
| Steady but will stay on one instance family | **EC2 Instance Savings Plan** or **Standard RI** |
| Unpredictable spikes above the baseline | **On-Demand** |
| Fault-tolerant, interruptible batch | **Spot** |
| Must guarantee capacity in a specific AZ | **On-Demand Capacity Reservation** (+ Savings Plan for the discount) |
| BYOL licensed per physical core | **Dedicated Hosts** |
| Short-lived dev/test during business hours only | **On-Demand + scheduled stop/start** |
| Mixed production fleet | **Savings Plan baseline + Spot for elasticity** |

---

## 2. Rightsizing and Elasticity

### 2.1 Rightsizing

Over-provisioning is the most common source of waste. Typical findings: instances averaging 5% CPU, volumes four times larger than needed, and Lambda functions with 3 GB of memory doing trivial work.

- **AWS Compute Optimizer** analyzes CloudWatch metrics and recommends specific instance types/sizes for **EC2, Auto Scaling groups, EBS volumes, Lambda functions, ECS on Fargate, and RDS**, including projected savings and performance risk.
- **Cost Explorer rightsizing recommendations** identify idle and underutilized instances.
- **Trusted Advisor** flags **low-utilization EC2 instances, idle load balancers, unassociated Elastic IPs, underutilized EBS volumes, and idle RDS instances**.
- Remember that memory is **not** a default CloudWatch metric — install the **CloudWatch agent** so rightsizing decisions account for memory.
- Moving down one instance size halves the cost; moving to a newer generation usually improves price/performance at no effort.

### 2.2 Turn things off

- **Non-production environments running 24/7** are a classic waste. Dev/test used 40 hours a week costs 76% less if stopped outside those hours. Automate with **EventBridge Scheduler + Lambda**, **Systems Manager Automation**, **Instance Scheduler on AWS**, or ASG **scheduled scaling to zero**.
- Stopped EC2 instances cost nothing for compute, but **EBS volumes and Elastic IPs still bill**.
- Terminate orphaned resources: unattached volumes, old snapshots, unused load balancers, idle NAT gateways, unused Elastic IPs, forgotten dev stacks. **AWS Config rules** and tagging-based cleanup automation enforce this.

### 2.3 Auto Scaling as a cost control

Auto Scaling is as much a cost tool as a performance tool — **scaling in** is where the savings are.

- Set a realistic **minimum** so you aren't paying for idle headroom.
- Use **target tracking** on the metric that actually drives load so the fleet shrinks promptly.
- **Scheduled scaling** for predictable patterns (scale to 2 at night, 20 at 9 a.m.).
- **Predictive scaling** avoids over-provisioning "just in case."
- **Mixed instances with Spot** cuts the marginal cost of each additional instance.
- Watch **cooldowns** — overly long cooldowns delay scale-in and cost money.

### 2.4 Graviton

Moving to **AWS Graviton (ARM)** instances typically yields **up to 40% better price/performance** with lower energy use. Available for EC2, Lambda (`arm64`), Fargate, RDS, Aurora, ElastiCache, OpenSearch, EMR, and more. Interpreted and JIT languages usually need only a redeploy; compiled code needs recompiling. Combine Graviton with a Savings Plan and the savings stack.

---

## 3. Choosing a Cheaper Compute Model

### 3.1 Serverless vs always-on

Lambda and Fargate charge only while code runs. For **intermittent, spiky, or low-duty-cycle** workloads this is dramatically cheaper than an always-on EC2 instance — a function invoked 100,000 times a month for 200 ms each may cost cents, where the smallest EC2 instance costs several dollars.

The crossover point matters: at **sustained high utilization**, EC2 (especially with Savings Plans or Spot) becomes cheaper per unit of compute than Lambda. The exam usually frames it clearly — "runs a few times per hour" → serverless; "runs continuously at 70% CPU" → EC2 with a commitment.

### 3.2 Lambda cost model and tuning

Cost = **(GB-seconds) × price + per-request charge** (plus ephemeral storage above 512 MB and provisioned concurrency if enabled).

- Because **CPU scales with memory**, raising memory often **lowers** total cost: a function taking 10 s at 512 MB might take 2 s at 1,024 MB — half the GB-seconds and five times faster. Use **AWS Lambda Power Tuning** to find the optimum empirically.
- Use **`arm64` (Graviton)** for ~20% lower price per GB-second.
- Trim deployment packages and move initialization outside the handler so warm invocations reuse it.
- **Provisioned concurrency costs money even when idle** — use it only where cold-start latency genuinely matters, and auto-scale it on a schedule.
- Avoid functions that **sleep or poll** waiting on something; use Step Functions `Wait` states or event-driven triggers instead of paying for idle execution time.
- Batch records (SQS/Kinesis batch size) to reduce invocation count.

### 3.3 Containers

- **Fargate** removes instance management and bills per vCPU-second/GB-second with a 1-minute minimum — cheaper for bursty or low-density workloads, and it avoids paying for unused EC2 capacity.
- **ECS/EKS on EC2** is cheaper at high, steady utilization because you can **bin-pack** many tasks onto each instance and use **Spot** and Savings Plans. The trade-off is that you manage, patch, and scale the instances.
- **Fargate Spot** gives up to 70% off for interruption-tolerant tasks.
- **Right-size task CPU/memory requests** — over-requesting wastes cluster capacity invisibly.
- **Karpenter** (EKS) provisions right-sized nodes just-in-time and consolidates workloads onto fewer nodes, often producing large savings versus the Cluster Autoscaler.
- Use **Graviton** task/node architectures.

### 3.4 Managed services instead of self-managed

Running software yourself on EC2 means paying for the instances, the storage, the patching effort, and the HA design. Managed equivalents frequently cost less in total:

| Self-managed on EC2 | Managed alternative |
|---|---|
| Web servers hosting static files | **S3 + CloudFront** |
| Self-hosted MySQL/PostgreSQL | **RDS / Aurora / Aurora Serverless v2** |
| Self-hosted Redis/Memcached | **ElastiCache** |
| Self-hosted Kafka | **Amazon MSK** |
| Self-hosted Elasticsearch | **OpenSearch Service** |
| Cron server | **EventBridge Scheduler + Lambda** |
| Self-managed Hadoop | **EMR / EMR Serverless / Glue** |
| NAT instances | **NAT gateway** (or VPC endpoints to avoid it) |
| Self-built CI/CD servers | **CodeBuild / CodePipeline** |
| Self-managed VPN appliances | **Site-to-Site VPN / Client VPN** |

**S3 + CloudFront replacing a web-server fleet** for static content is one of the most frequently correct cost answers on the exam.

### 3.5 Batch and HPC

- **AWS Batch** with a **Spot** compute environment and array jobs is the canonical answer for "run thousands of restartable jobs as cheaply as possible."
- **EMR** with **task nodes on Spot** and **transient clusters** (terminate when the job finishes, with data in S3 via EMRFS) avoids paying for idle clusters.
- Queue-driven worker fleets on Spot, scaled on queue depth, scale to zero when idle.

---

## 4. Licensing Costs

- **License Included** AMIs (Windows, SQL Server) bundle the license into the hourly rate — simple, no compliance overhead, good for variable usage.
- **BYOL** on **Dedicated Hosts** is usually cheaper for large, steady Windows/Oracle/SQL Server estates licensed per physical core, and gives visibility of sockets and cores for compliance.
- **AWS License Manager** tracks license usage against entitlements across accounts and can block launches that would breach a limit.
- Consider **open-source alternatives**: migrating SQL Server → **Aurora PostgreSQL with Babelfish**, or Oracle → Aurora via **SCT + DMS**, eliminates licence fees entirely. The **Windows → Linux** move for .NET Core applications is another standard saving.
- **Optimize CPU options** — reduce the number of vCPUs on an instance (keeping the memory) when licensing is **per core**, so you pay for fewer licensed cores while retaining a large memory footprint.

---

## 5. Governance: Keeping Costs Down Over Time

- **Tagging strategy** — mandatory tags (`CostCenter`, `Project`, `Environment`, `Owner`) enforced by **tag policies** (Organizations), **SCPs**, or **AWS Config rules**, and **activated as cost allocation tags** in the Billing console (only effective from activation onward).
- **Cost Categories** group accounts, tags, and services into business dimensions for reporting.
- **AWS Budgets with Budget Actions** can automatically apply a restrictive IAM policy, stop EC2/RDS instances, or attach an SCP when a threshold is breached.
- **SCPs** can restrict expensive resources — for example, deny launching instance families larger than a set size, deny Regions you don't operate in, or deny creating Dedicated Hosts.
- **Service Catalog** publishes pre-approved, right-sized, tagged product templates so teams can self-serve without over-provisioning.
- **Cost Anomaly Detection** for unexpected spikes; **Compute Optimizer** reviewed monthly; **Trusted Advisor** checks acted on regularly.
- **Consolidated billing** for volume discounts and shared commitment benefits.
- **Showback/chargeback** with the CUR in Athena/QuickSight, or **AWS Billing Conductor** for custom rates.

---

## 6. Worked Scenarios

**Scenario 1 — "We run a steady fleet of 50 m6i instances 24/7 and want maximum savings while keeping flexibility to change instance families."**
**Compute Savings Plan**, 3-year, All Upfront. An EC2 Instance Savings Plan or Standard RI would discount more but lock the family.

**Scenario 2 — "Nightly batch jobs take 6 hours, are checkpointed, and can restart."**
**Spot Instances** via **AWS Batch** or an ASG with a mixed instances policy, diversified across types and AZs with `price-capacity-optimized`.

**Scenario 3 — "Dev and test environments run all week but are only used 9–6 on weekdays."**
**Scheduled stop/start** (EventBridge Scheduler + Lambda, Instance Scheduler, or scheduled scaling) — roughly 70%+ savings. Remember EBS still bills while stopped.

**Scenario 4 — "A web application is idle most of the day with occasional bursts."**
Move to **Lambda + API Gateway** (or Fargate), paying only per request, instead of always-on EC2.

**Scenario 5 — "A Lambda function is invoked millions of times and the bill is high."**
Tune **memory** (often reduces GB-seconds by finishing faster), switch to **arm64/Graviton**, increase batch sizes, shorten the package, and check for idle wait time inside the function.

**Scenario 6 — "A fleet of EC2 web servers only serves static HTML, CSS, JS and images."**
Replace with **S3 static website hosting + CloudFront** — no servers at all.

**Scenario 7 — "We need guaranteed capacity in one AZ for a DR event, at the lowest cost."**
**On-Demand Capacity Reservation** (optionally covered by a Savings Plan for the discount) or a **zonal Reserved Instance**, which provides both discount and capacity.

**Scenario 8 — "We pay a fortune for SQL Server licences on EC2."**
Options: **Dedicated Hosts with BYOL**, **Optimize CPU options** to reduce licensed cores, or migrate to **Aurora PostgreSQL with Babelfish** to remove the licence entirely.

**Scenario 9 — "Teams keep launching oversized instances and nobody notices until the bill arrives."**
**AWS Budgets** with alerts and **Budget Actions**, **SCPs** limiting instance families, **Service Catalog** for approved templates, mandatory **tagging** with tag policies, and **Cost Anomaly Detection**.

**Scenario 10 — "EKS cluster nodes are only 30% utilized."**
Adopt **Karpenter** for just-in-time right-sized nodes and consolidation, right-size pod requests, add **Spot** node pools, and move to **Graviton** instances.

---

## 7. Quick Decision Table

| Scenario | Answer |
|---|---|
| Steady 24/7 compute, want flexibility | **Compute Savings Plan** |
| Steady compute, fixed family, maximum discount | **EC2 Instance Savings Plan / Standard RI** |
| Need to resell a commitment later | **Standard RI (Marketplace)** |
| Need to change instance family mid-term | **Convertible RI / Compute Savings Plan** |
| Fault-tolerant, interruptible | **Spot Instances** |
| Reduce Spot interruptions | **Diversify + `price-capacity-optimized` + capacity rebalancing** |
| Guarantee capacity in an AZ | **Capacity Reservation / zonal RI** |
| BYOL per physical core | **Dedicated Hosts** |
| Reduce licensed cores | **Optimize CPU options** |
| Unpredictable, short-lived workloads | **On-Demand / serverless** |
| Intermittent workload, no servers | **Lambda / Fargate** |
| Containers at high steady density | **ECS/EKS on EC2 + Spot** |
| Containers, bursty, no management | **Fargate (+ Fargate Spot)** |
| Better price/performance on Linux | **Graviton** |
| Dev/test running 24/7 | **Scheduled stop/start** |
| Oversized instances | **Compute Optimizer rightsizing** |
| Idle load balancers, unattached EIPs | **Trusted Advisor** |
| Static website on EC2 | **S3 + CloudFront** |
| Self-managed database/cache/Kafka | **RDS/Aurora, ElastiCache, MSK** |
| Thousands of queued jobs, cheapest | **AWS Batch on Spot** |
| Idle Hadoop cluster | **Transient EMR with Spot task nodes / EMR Serverless** |
| Track spend per team | **Cost allocation tags + Cost Categories** |
| Automatically stop spending at a threshold | **Budgets + Budget Actions** |
| Share discounts across accounts | **Consolidated billing (Organizations)** |
| Prevent expensive resource types | **SCPs / Service Catalog** |

---

## Task 4.3 — Design Cost-Optimized Database Solutions

> Database cost comes from four places: **instance hours**, **storage and I/O**, **backups and snapshots**, and **data transfer**. The exam tests whether you can pick the cheapest *appropriate* engine, size it correctly, commit where usage is steady, and move cold data out of expensive storage.

---

## 1. Where Database Cost Comes From

| Cost dimension | Applies to | How to reduce it |
|---|---|---|
| **Instance hours** | RDS, Aurora provisioned, ElastiCache, Redshift, DocumentDB, Neptune, OpenSearch | Right-size, use Graviton, stop non-prod, commit with Reserved Instances, use serverless for variable load |
| **Storage (GB-month)** | All | Archive cold data to S3, delete unused data, use TTL, choose the right storage type |
| **I/O operations** | Aurora (standard config), RDS with io1/io2, DynamoDB RCU/WCU | Aurora **I/O-Optimized**, caching, efficient queries, right capacity mode |
| **Provisioned throughput** | DynamoDB provisioned | Auto scaling, reserved capacity, or on-demand for spiky load |
| **Backups and snapshots** | All | Shorter retention, delete manual snapshots, export to S3 |
| **Data transfer** | Cross-AZ, cross-Region, internet | Co-locate, avoid unnecessary cross-Region replicas |
| **Licences** | RDS Oracle/SQL Server | BYOL, Optimize CPU options, migrate to open-source engines |

---

## 2. Choosing the Cheapest Appropriate Engine

**The cheapest database is often not a database at all.** Before sizing anything, ask whether the data belongs somewhere cheaper:

| If the data is… | Put it in… |
|---|---|
| Large files or blobs | **S3** (with the pointer in the database) |
| Rarely queried historical records | **S3 + Athena** (pennies per GB vs database storage) |
| Session or temporary state | **DynamoDB with TTL** or **ElastiCache** |
| Logs | **CloudWatch Logs** (with retention set) or **S3 + Athena**, not a relational table |
| Simple key-value lookups at scale | **DynamoDB** rather than an over-provisioned RDS instance |
| Analytics | **Redshift or Athena**, not an oversized OLTP instance |

**Engine selection economics:**
- **DynamoDB on-demand** can be far cheaper than a small always-on RDS instance for low or spiky traffic — and it scales to zero cost when idle.
- **Aurora Serverless v2** suits variable or intermittent relational workloads, scaling in 0.5-ACU increments.
- **RDS on a `db.t4g` burstable Graviton instance** is the cheapest managed relational option for small, bursty workloads.
- **Open-source engines (MySQL, PostgreSQL, MariaDB)** avoid the licence costs of Oracle and SQL Server. **Babelfish** lets SQL Server applications run on Aurora PostgreSQL with minimal change; **SCT + DMS** handles the heavier migrations.
- **Self-managed databases on EC2** are usually *more* expensive in total than RDS once you count instances, storage, backup tooling, HA design, and administration — choose EC2 only when you need OS access or an unsupported engine/version.

---

## 3. Cost-Optimizing RDS and Aurora

### 3.1 Instance sizing and commitments

- **Right-size** with **Compute Optimizer for RDS**, **Performance Insights** (is the load real or is it a bad query?), and CloudWatch metrics. Many production databases run at single-digit CPU.
- **Graviton (`db.*g`) instance classes** give better price/performance at a lower hourly rate — often a 20%+ saving for a version upgrade and a reboot.
- **Burstable `db.t4g`** classes are cheap for dev/test and small workloads, but watch CPU credits for sustained load.
- **Reserved Instances** for RDS: 1 or 3 years, up to **~69%** off. Note that **Savings Plans do not cover RDS** — RIs are the only commitment mechanism (same for ElastiCache, Redshift, OpenSearch, and DynamoDB reserved capacity).
- **Stop non-production databases.** An RDS instance can be stopped for up to **7 days** (it restarts automatically after that), which still saves meaningfully; alternatively snapshot and delete, restoring when needed. Aurora Serverless v2 can scale down to a minimal ACU instead.

### 3.2 Storage and I/O

- **gp3** is the default and cheapest general-purpose RDS storage; use **io1/io2** only when you genuinely need provisioned IOPS, because provisioned IOPS carry a significant premium.
- **Storage autoscaling** avoids over-provisioning up front — but note storage **can only grow**, never shrink, so over-allocating is permanent until you migrate.
- **Aurora I/O-Optimized** removes per-I/O charges for a higher instance/storage rate. It becomes cheaper when **I/O exceeds roughly 25% of the cluster's total spend** — typical of write-heavy or scan-heavy workloads. Aurora **Standard** is cheaper for low-I/O workloads.
- **Aurora storage auto-grows and auto-shrinks**, and you pay only for what is used — unlike RDS, where allocated storage is billed whether used or not.

### 3.3 Multi-AZ and replicas

- **Multi-AZ roughly doubles the instance cost.** It is essential for production, but it is pure waste on dev/test environments — a frequent, easy saving.
- Each **read replica** is a full-priced instance. Add them only when read load genuinely requires it, and consider **ElastiCache** first: a cache node is often cheaper than a replica and removes far more load.
- **Cross-Region read replicas** add instance cost **plus cross-Region data transfer**. Use only where a business requirement (DR or local latency) justifies it.

### 3.4 Backups and snapshots

- **Automated backup storage equal to the database size is free**; beyond that you pay per GB-month. Keep retention to what you actually need (1–35 days).
- **Manual snapshots persist until you delete them** — and they survive the deletion of the database instance. Orphaned manual snapshots are a classic silent cost. Audit and delete them.
- **Export snapshots to S3 in Parquet** for long-term retention at object-storage prices and query them with Athena, instead of paying database-snapshot rates.
- **Cross-Region snapshot copies** double storage cost and add transfer cost.

### 3.5 Other levers

- **Archive cold rows to S3** and query with Athena or Redshift Spectrum; keep the OLTP database small and fast.
- **Caching with ElastiCache** reduces the instance size you need and may let you drop replicas.
- **RDS Proxy** reduces connection overhead so a smaller instance can handle the same application fleet (it does have its own per-vCPU charge, so weigh it).
- **Fix inefficient queries and add indexes** — a missing index is often the real reason someone wants a bigger instance.
- **Licence optimization:** BYOL on Dedicated Hosts, **Optimize CPU options** to reduce licensed cores, or migrate to open source.

---

## 4. Cost-Optimizing DynamoDB

### 4.1 Capacity mode is the biggest decision

| Mode | Billing | Cheapest when |
|---|---|---|
| **On-demand** | Per read/write request unit | Traffic is **spiky, unpredictable, low, or intermittent**; new applications; dev/test. Costs nothing when idle. |
| **Provisioned** | Per hour of provisioned RCU/WCU | Traffic is **steady and predictable** with high utilization — can be ~6–7× cheaper per request than on-demand at consistent load |

Rules of thumb: if average utilization of provisioned capacity would be **below ~15–20%**, on-demand is usually cheaper. If you can keep utilization high with **auto scaling** (target ~70%), provisioned wins. You can switch modes (once every 24 hours).

**Further provisioned savings:** **DynamoDB reserved capacity** (1 or 3 years) gives up to ~77% off provisioned throughput for predictable baselines.

### 4.2 Design choices that cut cost

- **Avoid `Scan`.** A scan reads the entire table and bills for it. Use `Query` with a well-chosen key, or create a **GSI** so you can query instead.
- **Eventually consistent reads cost half** of strongly consistent reads. Use them wherever the application tolerates it.
- **Project only needed attributes** into GSIs — a GSI with `ALL` projection duplicates the whole table's storage and write cost. `KEYS_ONLY` or `INCLUDE` is often enough.
- **Every GSI multiplies write cost** — each write to the base table also writes to each affected index. Delete unused indexes.
- **Keep items small.** WCUs are billed per 1 KB and RCUs per 4 KB, so trimming attribute names and moving blobs to S3 directly reduces consumed capacity.
- **TTL deletes expired items for free** — far cheaper than issuing delete requests, and it keeps storage and scan costs down.
- **DynamoDB Standard-IA table class** cuts storage cost ~60% (with higher request costs) for tables where **storage dominates** — archives, logs, old orders.
- **DAX** reduces read capacity consumption for repeated reads; weigh the cluster cost against RCU savings.
- **Export to S3** for analytics consumes **no read capacity** — never run analytical scans against the live table.
- **Global tables** multiply cost by the number of Regions (plus replication traffic) — use only where multi-Region is required.

---

## 5. Cost-Optimizing Caching and Analytics Stores

**ElastiCache**
- **Reserved nodes** for steady workloads (up to ~55% off).
- **Right-size node types** and use **Graviton** nodes.
- **Redis cluster mode** lets you scale horizontally with smaller nodes rather than one oversized node.
- A cache is often cheaper than additional read replicas or a larger database instance — the saving appears on the *database* line.
- **Data tiering** (r6gd nodes) moves cold data to local NVMe for a much lower cost per GB on large Redis datasets.
- Delete idle dev/test clusters; they bill continuously.

**Amazon Redshift**
- **Reserved nodes** for steady clusters (up to ~75% off).
- **RA3 + managed storage** separates compute and storage, so you stop paying for compute just to hold data.
- **Pause and resume** clusters (or **Redshift Serverless**) for intermittent analytics — Serverless bills per RPU-second with no idle cost.
- **Redshift Spectrum** keeps cold data in S3 and queries it in place, instead of loading everything into the cluster.
- **Concurrency Scaling** earns free credits (one hour per day per cluster), making burst handling cheap.
- **Compression encodings** and good **sort/distribution keys** reduce the storage and compute needed.

**Amazon OpenSearch**
- **UltraWarm** and **Cold storage** tiers (backed by S3) cut the cost of older indices by up to 90%.
- **Index State Management** automates rollover and tier transitions.
- **Reserved Instances** for steady clusters; **OpenSearch Serverless** for variable workloads.
- Set realistic retention — most log data has no value after 30 days in hot storage.

**Amazon Athena**
- Billed at **~$5 per TB scanned**, so cost control *is* scan reduction: **Parquet/ORC, compression, partitioning, selecting fewer columns**, and compacting small files. Use **workgroup data-scan limits** to prevent runaway queries.

---

## 6. Data Lifecycle for Databases

A disciplined lifecycle is often the largest database saving available:

```
Hot (0–90 days)      → RDS/Aurora/DynamoDB      — fast, expensive
Warm (90 days–1 yr)  → S3 Standard / Redshift   — queryable, cheaper
Cold (1–7 years)     → S3 Glacier classes       — archival, cheapest
Expired              → deleted                   — free
```

Mechanisms: **DynamoDB TTL**, scheduled archive jobs writing Parquet to S3, **RDS snapshot export to S3**, **DynamoDB export to S3**, **Redshift unload to S3**, and S3 lifecycle rules moving the archived data onward to Glacier.

---

## 7. Worked Scenarios

**Scenario 1 — "Our RDS database runs 24/7 at 8% CPU with Multi-AZ on a dev account."**
Right-size the instance class (Compute Optimizer), move to **Graviton**, **disable Multi-AZ on dev**, and **stop the instance outside working hours**.

**Scenario 2 — "A DynamoDB table is provisioned at 10,000 RCU/WCU but averages 400."**
Enable **auto scaling** targeting ~70% utilization, or switch to **on-demand** if the pattern is genuinely spiky. Consider **reserved capacity** for the steady baseline.

**Scenario 3 — "A new application has unpredictable traffic and we don't want to plan capacity."**
**DynamoDB on-demand**, or **Aurora Serverless v2** for relational.

**Scenario 4 — "Reporting queries are hammering the production database and someone proposes a bigger instance."**
Add **ElastiCache** for repeated queries and/or a **read replica**, or move analytics to **Redshift/Athena**. Scaling the OLTP instance up is the expensive answer.

**Scenario 5 — "Our Aurora bill shows enormous I/O charges."**
Switch the cluster to **Aurora I/O-Optimized** (worth it above ~25% I/O spend), add caching, and tune queries that scan excessively.

**Scenario 6 — "Seven years of order history sits in RDS but only the last 90 days is queried."**
Archive older rows to **S3 as Parquet**, query with **Athena** (or **Redshift Spectrum**), and shrink the database. Apply S3 lifecycle rules to Glacier afterwards.

**Scenario 7 — "We pay heavily for SQL Server licences on RDS."**
Migrate to **Aurora PostgreSQL with Babelfish** (minimal application change) or use **SCT + DMS**; alternatively BYOL on Dedicated Hosts or **Optimize CPU options**.

**Scenario 8 — "Our OpenSearch cluster keeps 2 years of logs in hot storage."**
Apply **Index State Management** to roll indices into **UltraWarm** then **Cold**, and archive to S3 with a defined retention policy.

**Scenario 9 — "Analytics runs once a week but the Redshift cluster bills continuously."**
**Pause/resume** the cluster, or move to **Redshift Serverless**, or query S3 directly with **Athena**.

**Scenario 10 — "Session data in RDS is causing high write load and cost."**
Move sessions to **DynamoDB with TTL** or **ElastiCache** — cheaper, faster, and self-expiring.

---

## 8. Quick Decision Table

| Scenario | Answer |
|---|---|
| Steady relational workload, 1–3 years | **RDS/Aurora Reserved Instances** (Savings Plans don't cover RDS) |
| Variable relational workload | **Aurora Serverless v2** |
| Small, bursty relational workload | **`db.t4g` Graviton burstable** |
| Better price/performance, same engine | **Graviton DB instance classes** |
| Dev/test database running 24/7 | **Stop it** (up to 7 days) / snapshot and delete; disable Multi-AZ |
| High Aurora I/O charges | **Aurora I/O-Optimized** |
| Spiky or unknown NoSQL traffic | **DynamoDB on-demand** |
| Steady, predictable NoSQL traffic | **DynamoDB provisioned + auto scaling (+ reserved capacity)** |
| Expensive table scans | **GSI + Query**, never `Scan` |
| Halve read cost | **Eventually consistent reads** |
| Storage-heavy, rarely read DynamoDB table | **Standard-IA table class** |
| Expire old items for free | **DynamoDB TTL** |
| Reduce GSI write amplification | **Project only needed attributes / delete unused GSIs** |
| Analytics on DynamoDB without consuming capacity | **Export to S3 + Athena** |
| Repeated identical queries | **ElastiCache** (cheaper than more replicas) |
| Steady cache workload | **ElastiCache reserved nodes** |
| Large Redis dataset, cost-sensitive | **Data tiering (r6gd)** |
| Intermittent analytics | **Redshift pause/resume or Serverless; Athena** |
| Keep cold warehouse data cheap | **Redshift Spectrum / RA3 managed storage** |
| Old log indices costing too much | **OpenSearch UltraWarm / Cold + ISM** |
| Reduce Athena cost | **Parquet + compression + partitioning** |
| Archive cold database rows | **Export to S3 (Parquet) + lifecycle to Glacier** |
| Orphaned manual snapshots | **Audit and delete; export to S3 instead** |
| Oracle/SQL Server licence cost | **Migrate to Aurora (SCT/DMS/Babelfish)** or **BYOL + Optimize CPU** |
| Blobs stored in the database | **Move to S3, keep the pointer** |

---

## Task 4.4 — Design Cost-Optimized Network Architectures

> Network charges are the most invisible part of an AWS bill — there is no "instance" to look at, just a data-transfer line item. The exam tests whether you know **which direction and which path costs money**, and the handful of architectural moves that eliminate most of it.

---

## 1. The AWS Data Transfer Cost Model

### 1.1 The fundamental rules

| Traffic | Cost |
|---|---|
| **Inbound from the internet** | **Free** |
| **Outbound to the internet** | **Charged per GB** (tiered; ~$0.09/GB for the first 10 TB in most Regions) — the most expensive common path |
| **Within the same AZ, using private IPv4 addresses** | **Free** |
| **Within the same AZ, using public IPv4 or Elastic IPs** | **Charged** (~$0.01/GB each way) |
| **Between AZs in the same Region** | **Charged ~$0.01/GB in each direction** (so ~$0.02/GB round trip) |
| **Between Regions** | **Charged**, higher than cross-AZ, varies by Region pair |
| **To/from most AWS services in the same Region over private endpoints** | Usually free or cheap |
| **S3 → CloudFront** | **Free** |
| **CloudFront → internet** | Charged, but **cheaper per GB than EC2/S3 egress**, with volume tiers |
| **Direct Connect data transfer out** | **Significantly cheaper than internet egress** |
| **VPC peering, same Region** | Charged at cross-AZ rates when crossing AZs; **free within the same AZ** |
| **Through a NAT gateway** | **Hourly charge + ~$0.045/GB data processing**, *on top of* any internet egress charge |
| **Through Transit Gateway** | Hourly per attachment + per-GB data processing |
| **Through a load balancer** | Hourly + **LCU/NLCU** charges based on connections, bandwidth, and rules |
| **VPC endpoints (gateway)** | **Free** |
| **VPC endpoints (interface/PrivateLink)** | Hourly per endpoint per AZ + per-GB processing |

### 1.2 The mental model

Ask three questions about any byte:
1. **Does it leave AWS?** Internet egress is the expensive case — reduce it with caching, compression, and CloudFront.
2. **Does it cross an AZ or Region boundary?** If so, can the components be co-located?
3. **Does it pass through a billed middlebox?** NAT gateway, Transit Gateway, interface endpoint, and load balancer all add per-GB processing. Can the path be shortened?

---

## 2. Eliminating NAT Gateway Costs

A NAT gateway costs roughly **$0.045 per hour** plus **$0.045 per GB processed** — and that data-processing charge applies *even when the destination is an AWS service in the same Region*. For a workload pulling terabytes from S3, this is often the single largest surprise on the bill.

**Fixes, in order of impact:**

1. **Gateway VPC endpoints for S3 and DynamoDB** — **completely free**, added as a route table entry. Traffic to S3/DynamoDB bypasses the NAT gateway entirely. If a question mentions private instances downloading large volumes from S3 through NAT, this is the answer.
2. **Interface VPC endpoints (PrivateLink)** for other AWS services (SSM, ECR, Secrets Manager, CloudWatch Logs, KMS, SQS, SNS…). These have an hourly and per-GB cost, but the per-GB rate is lower than NAT processing and they also improve security. Model the break-even: for low-volume services the NAT may be cheaper; for high-volume (ECR image pulls, CloudWatch Logs) endpoints win.
3. **Consolidate NAT gateways** where resilience permits — but note the trade-off: one NAT gateway per AZ costs more in hourly charges yet **avoids cross-AZ data charges** and removes a single point of failure. For high-volume workloads, per-AZ NAT gateways are usually both cheaper and safer; for low-volume dev environments, a single NAT gateway is cheaper.
4. **Remove the need for egress entirely** — use VPC endpoints, host packages in **CodeArtifact/ECR** with endpoints, and bake dependencies into AMIs/container images so instances don't download them at boot.
5. For very small, low-throughput environments, a **NAT instance** on a `t4g.nano` can be cheaper than a NAT gateway — but it is a single point of failure, bandwidth-limited, and you manage it. AWS recommends NAT gateway for anything real.
6. **IPv6 workloads** can use an **egress-only internet gateway**, which has **no hourly or per-GB charge**.

---

## 3. Reducing Internet Egress with CloudFront

CloudFront reduces cost in three distinct ways:

1. **Origin transfer is free** — data from **S3, EC2, ELB, or any AWS origin to CloudFront costs nothing**.
2. **CloudFront's per-GB egress rate is lower** than direct S3 or EC2 egress, and it has volume discount tiers (plus committed-use private pricing at scale).
3. **Caching eliminates origin requests altogether** — fewer S3 GET charges, less load on EC2/ALB (so smaller fleets), and reduced database queries behind them.

**Maximizing the benefit:**
- Raise the **cache hit ratio**: long `Cache-Control` max-age for immutable assets, minimal cache keys (don't forward headers/cookies/query strings you don't vary on), versioned filenames rather than invalidations.
- Enable **Origin Shield** for a busy origin — it collapses requests from all edge locations into one regional layer, further cutting origin requests (it has its own small per-request fee, so it pays off at scale).
- Enable **compression** at the edge (gzip/Brotli) — fewer bytes egressed means a directly lower bill.
- Use **price classes** — restricting CloudFront to cheaper edge locations (e.g., Price Class 100: North America and Europe) lowers cost if you have no users in the most expensive Regions.
- Avoid excessive **invalidations** (the first 1,000 paths per month are free, then charged).

**CloudFront is also the standard answer for "reduce S3 data transfer costs"** and for "reduce the size of our EC2 web fleet."

---

## 4. Co-location: Avoiding Cross-AZ and Cross-Region Charges

- **Same-AZ private IPv4 traffic is free.** Cross-AZ traffic is charged **in both directions**.
- Keep **chatty components in the same AZ** where availability requirements allow — for example, an application server and its cache replica. Balance this against resilience: never sacrifice Multi-AZ for a production database to save transfer cost.
- **ElastiCache**: reading from a replica in another AZ incurs cross-AZ charges. Redis **read-from-replica with AZ affinity** keeps reads local.
- **Load balancers:** **ALB cross-zone load balancing is on by default and free**; **NLB cross-zone is off by default and billed as cross-AZ traffic when enabled**. Enabling it on an NLB processing terabytes is a real cost — weigh it against the uneven distribution it fixes.
- **Kafka/Cassandra/Elasticsearch** style clusters replicate heavily between nodes; spreading them across AZs is necessary for resilience but is a genuine cost line — use rack-aware/AZ-aware configuration to minimize unnecessary cross-AZ replication.
- **Cross-Region replication** (S3 CRR, Aurora Global Database, DynamoDB global tables, cross-Region read replicas) all incur inter-Region transfer. Replicate only what genuinely needs it — for S3, use **replication rules with prefix/tag filters** rather than replicating whole buckets.
- Always use **private IPs / internal DNS** rather than public IPs for internal communication: traffic to a public IP leaves and re-enters the VPC and is charged even within the same AZ.

---

## 5. Choosing Cost-Effective Connectivity

### 5.1 VPC peering vs Transit Gateway

| | **VPC peering** | **Transit Gateway** |
|---|---|---|
| Hourly charge | **None** | Per attachment per hour |
| Data processing | **None** (only cross-AZ/Region transfer rates apply) | **Per GB processed** on top of transfer |
| Scale | n(n−1)/2 connections; not transitive | Thousands of attachments, transitive, centrally routed |

**Cost conclusion:** for a **small number of VPCs with high traffic volume**, peering is cheaper (no hourly or processing fees). For **many VPCs**, Transit Gateway's operational simplicity usually outweighs its per-GB cost — and the management burden of 45+ peerings is its own expense. A common hybrid: Transit Gateway as the general hub, with **direct peering for the few highest-volume VPC pairs**.

### 5.2 VPN vs Direct Connect

- **Site-to-Site VPN** — low hourly cost per connection plus standard internet egress rates. Cheap to start, no commitment, available immediately.
- **Direct Connect** — port-hour charges plus **significantly reduced data-transfer-out rates**. The port cost is fixed, so DX becomes cheaper than VPN above a certain monthly volume (often in the tens of TB). It also provides consistent latency and bandwidth.
- **Break-even thinking:** compute (VPN internet egress $/GB × monthly GB) versus (DX port hours + DX egress $/GB × monthly GB). High, sustained volume favours DX; low or bursty volume favours VPN.
- **Hosted connections** (50 Mbps–25 Gbps via a partner) avoid the cost of a full 1 Gbps port for moderate bandwidth needs.
- Keep a **VPN as a cheap backup** for a single DX rather than buying a second DX, when the budget doesn't allow full redundancy (accepting lower resilience).

### 5.3 PrivateLink vs peering vs Transit Gateway

**PrivateLink (interface endpoints)** charges per endpoint-hour per AZ plus per GB. It is cost-effective when you need **one-way access to a specific service** rather than full network connectivity — and it avoids the overlapping-CIDR problems and broad exposure of peering. For **many consumers reaching one service**, PrivateLink is usually both cheaper and safer than building a mesh.

### 5.4 Load balancers

- **ALB/NLB pricing** = hourly + **LCUs/NLCUs** measured on new connections, active connections, processed bytes, and (ALB) rule evaluations. The highest dimension sets the charge.
- **Consolidate**: one ALB with **host- and path-based routing** can serve dozens of services instead of running one ALB per service — a large and easy saving in microservice environments. The **AWS Load Balancer Controller** with **IngressGroups** does this for EKS.
- **Delete idle load balancers** — Trusted Advisor flags them.
- For pure TCP pass-through at high volume, an **NLB is usually cheaper** than an ALB (fewer processing features).
- Remember that **CloudFront in front of an ALB** reduces the bytes and connections the ALB processes, lowering LCU charges.

---

## 6. Other Network Cost Items

- **Public IPv4 addresses are now charged per hour for every in-use address** (including those attached to running instances, NAT gateways, and load balancers). Reduce the count: use private IPs with a shared NAT gateway or VPC endpoints, front fleets with a single load balancer, and adopt **IPv6** where possible.
- **Unassociated Elastic IPs** are charged — Trusted Advisor flags them, and they are pure waste.
- **VPC Flow Logs** cost money in **ingestion and storage** (CloudWatch Logs or S3). For high-volume VPCs, send them to **S3 in Parquet** rather than CloudWatch Logs, sample or filter (log only rejects, or only specific ENIs), and apply lifecycle rules.
- **Global Accelerator** has a fixed hourly fee plus a per-GB **data transfer premium**. It buys performance and fast failover, not savings — justify it on requirements.
- **Interface endpoints** are billed per AZ: an endpoint in 3 AZs costs 3× the hourly rate. Deploy only in the AZs you actually use.
- **Transit Gateway attachments** bill hourly even when idle — remove attachments for decommissioned VPCs.
- **Route 53**: hosted zone monthly fee plus per-query charges; **alias records to AWS resources are free to query**, so prefer them over CNAMEs pointing at AWS endpoints. Health checks are billed per check (more for non-AWS endpoints and optional features).
- **Data Transfer Out discounts:** the first 100 GB per month of internet egress is free account-wide, and volume tiers reduce the rate at scale.

---

## 7. Monitoring Network Spend

- **Cost Explorer** — filter by **usage type** (`DataTransfer-Out-Bytes`, `NatGateway-Bytes`, `DataTransfer-Regional-Bytes`) and group by service to see exactly which path is costing money.
- **Cost and Usage Report** in Athena — the only way to attribute transfer costs precisely to resources and teams.
- **VPC Flow Logs** — identify the top talkers and unexpected flows driving transfer (and then turn the logs off or sample them, because they cost money too).
- **CloudWatch metrics** — NAT gateway `BytesOutToDestination`/`BytesOutToSource`, ALB `ProcessedBytes`, CloudFront `BytesDownloaded` and **cache hit rate**, interface endpoint bytes processed.
- **Cost Anomaly Detection** catches a sudden transfer spike (often a misconfigured sync job or a cross-Region replication someone enabled).
- **Trusted Advisor** — idle load balancers, unassociated Elastic IPs.

---

## 8. Worked Scenarios

**Scenario 1 — "Private EC2 instances download 80 TB/month from S3 and the NAT gateway bill is enormous."**
Create a **gateway VPC endpoint for S3** — free, and it removes the NAT data-processing charge entirely.

**Scenario 2 — "Our S3 data-transfer-out bill for a global media site is the largest line on the invoice."**
Serve through **CloudFront**: S3→CloudFront transfer is free, CloudFront egress is cheaper, and caching removes most origin requests. Tune the cache hit ratio, enable compression, and consider a **price class**.

**Scenario 3 — "We run 30 ALBs, one per microservice."**
Consolidate onto **one or two ALBs** using host- and path-based routing rules and separate target groups.

**Scenario 4 — "A chatty application tier and its cache sit in different AZs."**
Co-locate them in the same AZ (or use Redis **read-from-replica with AZ affinity**) to avoid cross-AZ charges — provided the availability requirement still allows it.

**Scenario 5 — "We transfer 100 TB/month from on-premises to AWS and back over a VPN."**
Model **Direct Connect**: the reduced egress rate plus predictable performance will almost certainly beat internet egress at that volume. Keep the VPN as a backup path.

**Scenario 6 — "An NLB's cross-zone load balancing was enabled and the bill jumped."**
That traffic is billed as cross-AZ. Decide whether even distribution is worth it; otherwise register comparable target counts per AZ and disable cross-zone.

**Scenario 7 — "We have 8 VPCs and only 2 exchange significant traffic."**
Use **Transit Gateway** for general connectivity but add a **direct VPC peering** between the two high-volume VPCs to avoid TGW per-GB processing.

**Scenario 8 — "Our VPC Flow Logs cost more than the workload."**
Send them to **S3 in Parquet** instead of CloudWatch Logs, reduce the log fields, filter to rejects only, sample, and apply S3 lifecycle rules.

**Scenario 9 — "Our bill now shows charges for public IPv4 addresses we never noticed."**
Audit and release unused Elastic IPs, move instances behind a shared NAT gateway or load balancer, use **VPC endpoints** instead of public endpoints, and adopt **IPv6** where supported.

**Scenario 10 — "Cross-Region replication of our entire S3 bucket is expensive but only some data needs DR."**
Apply **replication rules filtered by prefix or tag** so only the required objects replicate.

---

## 9. Quick Decision Table

| Scenario | Answer |
|---|---|
| Private subnets pulling from S3/DynamoDB | **Gateway VPC endpoint (free)** |
| Private subnets calling other AWS services heavily | **Interface endpoints (PrivateLink)** |
| High internet egress for content | **CloudFront** (free origin transfer, cheaper egress, caching) |
| Reduce CloudFront cost further | **Higher cache hit ratio, compression, Origin Shield, price class** |
| IPv6 outbound only | **Egress-only internet gateway (no data charge)** |
| Many small VPCs, management overhead | **Transit Gateway** |
| Two VPCs, very high traffic | **VPC peering** (no hourly/processing fee) |
| Expose one service to many consumers privately | **PrivateLink** |
| Sustained high-volume hybrid traffic | **Direct Connect** (lower egress rate) |
| Low-volume or temporary hybrid traffic | **Site-to-Site VPN** |
| 30 microservices, 30 load balancers | **Consolidate onto one ALB with routing rules** |
| Idle load balancers / unassociated EIPs | **Delete them (Trusted Advisor)** |
| NLB cross-zone enabled, bill jumped | Cross-AZ charges — **balance targets per AZ or accept the cost** |
| Chatty components in different AZs | **Co-locate in one AZ** where resilience allows |
| Replicating entire buckets cross-Region | **Filter replication by prefix/tag** |
| Expensive VPC Flow Logs | **S3 + Parquet, filter/sample, lifecycle** |
| Charges for public IPv4 addresses | **Release EIPs, share NAT/ALB, use endpoints, adopt IPv6** |
| Find which transfer path costs money | **Cost Explorer by usage type / CUR in Athena** |
| Sudden unexplained transfer spike | **Cost Anomaly Detection + VPC Flow Logs** |
| DNS queries to AWS resources | **Alias records (free queries)** |

---

# Appendix A — Service Cheat Sheet by Category

## Compute
| Service | One-line role |
|---|---|
| **EC2** | Virtual machines; full OS control; families M/T (general), C (CPU), R/X/u (memory), I/D/H (storage), P/G/Inf/Trn (accelerated), Hpc |
| **Lambda** | Event-driven functions; 15-min max, 128 MB–10 GB memory (CPU scales with memory) |
| **ECS** | AWS-native container orchestration; EC2 or Fargate launch types |
| **EKS** | Managed Kubernetes; managed node groups, Karpenter, or Fargate profiles |
| **Fargate** | Serverless compute engine for containers; per-vCPU/GB-second billing |
| **AWS Batch** | Managed batch job queues and compute environments; ideal with Spot |
| **Elastic Beanstalk** | Opinionated PaaS for web apps |
| **App Runner** | Container/source → running HTTPS service with minimal config |
| **Outposts / Local Zones / Wavelength** | AWS compute on-prem, in a metro, or in a 5G network |

## Storage
| Service | One-line role |
|---|---|
| **S3** | Object storage; 11 nines durability; 8 storage classes; lifecycle, versioning, replication |
| **EBS** | Single-AZ block volumes; gp3/gp2 (SSD), io1/io2/Block Express (provisioned IOPS), st1/sc1 (HDD, not bootable) |
| **Instance store** | Ephemeral NVMe on the host; highest IOPS; lost on stop/terminate |
| **EFS** | Elastic multi-AZ NFS for Linux; Elastic/Bursting/Provisioned throughput; IA + Archive tiers |
| **FSx for Windows** | SMB + Active Directory + NTFS ACLs; Multi-AZ |
| **FSx for Lustre** | HPC/ML parallel file system; S3-linked; scratch vs persistent |
| **FSx for ONTAP / OpenZFS** | NetApp / ZFS feature sets; multiprotocol (ONTAP) |
| **Storage Gateway** | Hybrid File (NFS/SMB→S3), Volume (iSCSI), Tape (VTL) with local cache |
| **DataSync / Transfer Family / Snow** | Scheduled sync / managed SFTP / offline petabyte transfer |

## Database
| Service | One-line role |
|---|---|
| **RDS** | Managed relational: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2; Multi-AZ, read replicas |
| **Aurora** | MySQL/PostgreSQL-compatible; 6 copies/3 AZs; 15 replicas; Global Database; Backtrack; Serverless v2 |
| **DynamoDB** | Serverless key-value; on-demand or provisioned; GSI/LSI; DAX; Streams; global tables; TTL |
| **ElastiCache** | Redis/Valkey (structures, persistence, HA) or Memcached (simple, multi-threaded) |
| **MemoryDB** | Durable Redis-compatible primary database |
| **DocumentDB / Keyspaces / Neptune / Timestream / QLDB** | MongoDB / Cassandra / graph / time-series / ledger |
| **Redshift** | Columnar MPP warehouse; RA3 + managed storage; Spectrum; Serverless |
| **OpenSearch** | Search and log analytics; UltraWarm/Cold tiers |
| **RDS Proxy** | Connection pooling; cuts failover time up to 66% |
| **DMS + SCT** | Migration with CDC; schema conversion |

## Networking & Content Delivery
| Service | One-line role |
|---|---|
| **VPC** | Isolated network: subnets, route tables, IGW, NAT GW, egress-only IGW, ENIs |
| **Security groups / NACLs** | Stateful instance firewall / stateless subnet firewall with numbered allow+deny rules |
| **VPC endpoints** | Gateway (S3, DynamoDB — free) and Interface/PrivateLink (ENI, hourly + per-GB) |
| **Transit Gateway** | Regional hub for many VPCs, VPNs, DX; segmented route tables; TGW peering |
| **VPC peering** | 1:1, non-transitive, no hourly or processing fee |
| **Direct Connect** | Dedicated private link; private/public/transit VIFs; DX gateway; not encrypted by default |
| **Site-to-Site VPN / Client VPN** | IPsec tunnels (2 per connection, 1.25 Gbps each) / remote user access |
| **Route 53** | DNS + health checks; simple, weighted, latency, failover, geolocation, geoproximity, multivalue, IP-based; free alias queries |
| **CloudFront** | CDN, 600+ PoPs, OAC, signed URLs/cookies, Origin Shield, origin groups, Functions/Lambda@Edge |
| **Global Accelerator** | Two static anycast IPs, TCP/UDP, AWS backbone, failover in seconds |
| **ELB** | ALB (L7, path/host routing, WAF, Cognito), NLB (L4, static IP, UDP, extreme scale), GWLB (appliance insertion) |

## Security, Identity & Compliance
| Service | One-line role |
|---|---|
| **IAM** | Users, groups, roles, policies; evaluation = explicit deny → SCP → resource policy/allow → boundary |
| **IAM Identity Center** | Workforce SSO with permission sets across accounts |
| **Organizations / SCPs / Control Tower** | Multi-account governance, guardrails, landing zone |
| **STS** | Temporary credentials, AssumeRole, ExternalId, federation |
| **KMS / CloudHSM** | Managed keys and envelope encryption / dedicated FIPS 140-2 Level 3 HSM |
| **Secrets Manager / Parameter Store** | Secrets with rotation / config and SecureString parameters |
| **ACM** | Free public TLS certs with auto-renewal; CloudFront certs must be in us-east-1 |
| **WAF / Shield / Firewall Manager** | L7 rules / DDoS protection (Std free, Adv paid) / central policy management |
| **GuardDuty / Macie / Inspector / Detective / Security Hub** | Threat detection / S3 PII discovery / vulnerability scanning / investigation / aggregated findings |
| **CloudTrail / Config / Audit Manager / Artifact** | API audit / configuration compliance + remediation / audit evidence / AWS compliance reports |
| **Cognito** | User pools (authentication) and identity pools (AWS credentials) |

## Application Integration
| Service | One-line role |
|---|---|
| **SQS** | Pull queue; standard (at-least-once) or FIFO (ordered, exactly-once); DLQ, visibility timeout, long polling |
| **SNS** | Push pub/sub fan-out to SQS, Lambda, HTTP, email, SMS; filter policies |
| **EventBridge** | Content-based event routing, AWS/SaaS sources, scheduler, archive & replay, Pipes |
| **Step Functions** | Workflow orchestration; Standard (1 year, exactly-once) vs Express (5 min, at-least-once) |
| **Amazon MQ** | Managed ActiveMQ/RabbitMQ for AMQP, MQTT, STOMP, JMS, OpenWire |
| **API Gateway** | REST (full features, caching, usage plans), HTTP (cheaper, faster), WebSocket; 29-second timeout |
| **AppSync** | Managed GraphQL with real-time subscriptions |

## Analytics
| Service | One-line role |
|---|---|
| **Kinesis Data Streams** | Real-time, shards, 1–365 day retention, replay, many consumers, enhanced fan-out |
| **Data Firehose** | Zero-admin delivery to S3/Redshift/OpenSearch/Splunk; ~60 s buffer; Parquet conversion |
| **Managed Service for Apache Flink** | Real-time windowed analytics and anomaly detection |
| **MSK** | Managed Apache Kafka (and MSK Serverless) |
| **Glue** | Serverless Spark ETL + Data Catalog + crawlers + DataBrew + job bookmarks |
| **EMR** | Managed Hadoop/Spark/Presto; master/core/task nodes; Spot on task nodes; transient clusters |
| **Athena** | Serverless SQL over S3, ~$5/TB scanned; CTAS; federated queries; workgroup limits |
| **Lake Formation** | Fine-grained (column/row/cell) data lake permissions |
| **QuickSight** | Serverless BI with SPICE |

## Management, Migration & Cost
| Service | One-line role |
|---|---|
| **CloudWatch** | Metrics, alarms, Logs + Insights, Synthetics, RUM, dashboards; agent needed for memory/disk |
| **X-Ray** | Distributed tracing and service maps |
| **Systems Manager** | Session Manager, Patch Manager, Parameter Store, Automation, State Manager, Fleet Manager |
| **CloudFormation / CDK** | Infrastructure as code; StackSets for multi-account/Region |
| **Service Catalog** | Pre-approved, governed product templates |
| **AWS Backup** | Centralized backup policies, Vault Lock, cross-account/Region copies |
| **Elastic Disaster Recovery (DRS)** | Continuous block replication; RPO seconds, RTO minutes |
| **Application Migration Service (MGN)** | Lift-and-shift server migration |
| **Migration Hub / ADS / App2Container** | Track migrations / discover on-prem / containerize Java and .NET apps |
| **Cost Explorer / Budgets / CUR / Anomaly Detection** | Analyze / alert and act / raw data / detect spikes |
| **Compute Optimizer / Trusted Advisor** | Rightsizing recommendations / waste and best-practice checks |
| **Resilience Hub / FIS** | Assess RTO/RPO / chaos experiments |

---

# Appendix B — Numbers and Limits to Memorize

## Exam
| Fact | Value |
|---|---|
| Questions / scored | 65 / 50 (15 unscored) |
| Duration | 130 minutes (~2 min per question) |
| Passing score | 720 / 1000 |
| Validity | 3 years |

## Identity & Security
| Fact | Value |
|---|---|
| IAM policy evaluation | Explicit **Deny** always wins |
| STS session duration | 15 min – 12 h (role chaining capped at 1 h) |
| SCPs | Set the **maximum** permissions; never grant |
| KMS key deletion waiting period | **7–30 days** |
| KMS automatic rotation | Annual (customer-managed keys) |
| Data key size | 256-bit via envelope encryption |
| ACM for CloudFront | Certificate must be in **us-east-1** |
| Secrets Manager | Rotation built in; Parameter Store standard tier is free |

## Networking
| Fact | Value |
|---|---|
| VPC CIDR | /16 to /28 |
| Reserved IPs per subnet | **5** |
| Security groups | **Stateful**, allow rules only |
| NACLs | **Stateless**, allow + deny, evaluated by rule number (lowest first) |
| NAT gateway | 5 → 100 Gbps; one per AZ recommended |
| VPN tunnel | 1.25 Gbps; **2 tunnels per connection** |
| Direct Connect | 1 / 10 / 100 Gbps dedicated; 50 Mbps–25 Gbps hosted |
| ALB deregistration delay | 300 s default |
| ALB cross-zone | On by default, free; **NLB off by default, billed** |
| API Gateway timeout | **29 seconds** |
| Route 53 multivalue | Up to 8 healthy records |
| Gateway endpoints | **S3 and DynamoDB only, free** |

## Compute
| Fact | Value |
|---|---|
| Lambda timeout | **15 minutes** |
| Lambda memory | 128 MB – 10,240 MB (1 vCPU ≈ 1,769 MB) |
| Lambda `/tmp` | 512 MB – 10 GB |
| Lambda payload | 6 MB sync / 256 KB async |
| Lambda default concurrency | 1,000 per account per Region |
| Spot interruption notice | **2 minutes** |
| Savings Plans / RIs | Up to **72%**; Spot up to **90%** |
| Spread placement group | Max **7 instances per AZ** per group |
| EC2 Auto Recovery | Keeps instance ID, private IP, EIP, EBS volumes |

## Storage
| Fact | Value |
|---|---|
| S3 object size | 0 bytes – **5 TB**; single PUT max 5 GB |
| S3 request rate | 3,500 writes / 5,500 reads per second **per prefix** |
| S3 durability / availability | 11 nines / 99.99% (Standard) |
| IA minimum duration / size | 30 days / 128 KB |
| Glacier Instant / Flexible | 90 days minimum |
| Deep Archive | **180 days** minimum; 12 h (Standard) / 48 h (Bulk) retrieval |
| gp3 | 3,000 IOPS & 125 MB/s baseline; up to 16,000 IOPS / 1,000 MB/s |
| io2 Block Express | Up to **256,000 IOPS**, 64 TiB, 4,000 MB/s |
| st1 / sc1 | HDD, **cannot be boot volumes** |
| EBS Multi-Attach | io1/io2, up to **16 instances**, same AZ, cluster-aware FS |
| EFS | Multi-AZ NFS; One Zone ~47% cheaper |

## Database
| Fact | Value |
|---|---|
| RDS automated backups | **1–35 days**, point-in-time recovery |
| RDS read replicas | **5** per source (Aurora 15) |
| RDS Multi-AZ failover | 60–120 s (Multi-AZ DB cluster < 35 s) |
| Aurora storage | 6 copies / 3 AZs, up to **128 TiB**, 10 GB increments |
| Aurora Global Database | Up to 5 secondary Regions; RPO ~1 s, RTO < 1 min |
| DynamoDB item size | **400 KB** |
| 1 WCU / 1 RCU | 1 KB write/s / 4 KB strongly consistent read/s (or 2 eventually consistent) |
| DynamoDB indexes | 5 LSI (creation time only), 20 GSI |
| DynamoDB PITR | 35 days |
| RDS stop duration | Up to **7 days** |

## Integration & Analytics
| Fact | Value |
|---|---|
| SQS message size / retention | 256 KB / 1 min – **14 days** (default 4) |
| SQS visibility timeout | 30 s default, max **12 hours** |
| SQS long polling | Up to **20 seconds** |
| SQS FIFO throughput | 300 TPS (3,000 batched); high-throughput mode higher |
| SNS fan-out | One topic → many subscribers |
| Kinesis shard | **1 MB/s or 1,000 records/s in; 2 MB/s out** |
| Kinesis retention | 24 h default, up to **365 days** |
| Firehose buffer | 1–128 MB or **60–900 seconds** |
| Step Functions | Standard 1 year / Express 5 minutes |
| Athena pricing | ~$5 per TB scanned |

---

# Appendix C — Keyword to Service Decoder

| Phrase in the question | Almost always means |
|---|---|
| "No application changes allowed" | Sticky sessions, EFS/FSx, RDS Proxy, NLB static IP, Multi-AZ |
| "Least operational overhead" / "fully managed" | Serverless or managed service (Lambda, Fargate, Firehose, Aurora Serverless, Glue) |
| "Most cost-effective" + interruptible | **Spot** |
| "Most cost-effective" + steady 24/7 | **Savings Plans / Reserved Instances** |
| "Unpredictable / unknown access pattern" (S3) | **Intelligent-Tiering** |
| "Unpredictable traffic" (DynamoDB) | **On-demand capacity** |
| "Microsecond latency" + DynamoDB | **DAX** |
| "Sub-millisecond" + cache | **ElastiCache** |
| "Must be ordered, no duplicates" | **SQS FIFO** |
| "Multiple consumers, replay the stream" | **Kinesis Data Streams** |
| "Decouple" / "buffer spikes" | **SQS** |
| "One event, several independent actions" | **SNS fan-out** (or EventBridge) |
| "React to AWS service state changes" | **EventBridge** |
| "Coordinate steps with retries / approval" | **Step Functions** |
| "Static IP addresses" | **NLB** or **Global Accelerator** |
| "UDP" / "gaming" / "VoIP" | **NLB / Global Accelerator** |
| "Cache content globally" | **CloudFront** |
| "Route users to the nearest Region" | **Route 53 latency routing** (or Global Accelerator) |
| "Private connectivity to AWS services" | **VPC endpoints / PrivateLink** |
| "Connect hundreds of VPCs" | **Transit Gateway** |
| "Consistent bandwidth to on-premises" | **Direct Connect** |
| "Encrypt Direct Connect" | **VPN over DX** or MACsec |
| "Centrally manage accounts / guardrails" | **Organizations + SCPs / Control Tower** |
| "Temporary credentials" / "cross-account access" | **IAM roles + STS** |
| "Rotate credentials automatically" | **Secrets Manager** |
| "Detect PII in S3" | **Macie** |
| "Detect malicious activity" | **GuardDuty** |
| "Scan for CVEs" | **Inspector** |
| "Who made this API call?" | **CloudTrail** |
| "Is this resource compliant / did it drift?" | **AWS Config** |
| "Block SQL injection / rate limit" | **AWS WAF** |
| "Protect against large DDoS with cost protection" | **Shield Advanced** |
| "Access EC2 without SSH or bastion" | **Session Manager** |
| "RPO near zero across Regions (SQL)" | **Aurora Global Database** |
| "Cheapest DR, hours acceptable" | **Backup & restore** |
| "Scaled-down environment always running" | **Warm standby** |
| "Replicate on-prem servers for DR" | **Elastic Disaster Recovery** |
| "Query S3 with SQL, no infrastructure" | **Athena** |
| "Complex BI at high concurrency" | **Redshift** |
| "Full-text search" | **OpenSearch** |
| "Graph / relationships" | **Neptune** |
| "Immutable audit ledger" | **QLDB** |
| "Petabytes, bad bandwidth" | **Snowball Edge** |
| "Scheduled on-prem → AWS sync" | **DataSync** |
| "Partners use SFTP" | **Transfer Family** |
| "Which instance size should we use?" | **Compute Optimizer** |
| "Alert before we overspend" | **AWS Budgets** |

---

# Appendix D — Top 25 Distractors and Traps

1. **Multi-AZ is not read scaling.** The RDS standby serves no traffic. Read replicas scale reads; Multi-AZ provides availability.
2. **Read replicas are asynchronous.** Never the answer when read-after-write consistency is required.
3. **Security groups are stateful; NACLs are stateless.** If return traffic is blocked, suspect a NACL (you need ephemeral port rules 1024–65535).
4. **Security groups have no deny rules.** "Block a specific malicious IP" → **NACL** or **WAF**, never a security group.
5. **A subnet is public because of a route to an IGW**, not because of a name or checkbox.
6. **NAT gateways are AZ-scoped.** One NAT gateway is a single point of failure and creates cross-AZ charges.
7. **EBS is single-AZ.** It is not a multi-AZ or shared file system; EFS or FSx is.
8. **HDD volumes (st1/sc1) cannot be boot volumes.**
9. **Instance store is ephemeral** — lost on stop, hibernate, or terminate (survives reboot).
10. **S3 is not a file system.** No POSIX semantics, no partial in-place writes.
11. **Glacier minimum durations are real.** Deleting early still costs the full 90/180 days; tiny objects bill at the 40–128 KB minimum.
12. **Lifecycle transitions cost money per object** — moving millions of tiny files to Glacier can increase the bill.
13. **S3 replication only applies to new objects.** Use **Batch Replication** for existing ones; versioning is required on both sides.
14. **ACM certificates for CloudFront must be in us-east-1**, and ACM public certs **cannot be exported**.
15. **KMS keys are Regional.** Cross-Region copies must be re-encrypted with a key in the destination Region (multi-Region keys are the exception).
16. **SCPs do not grant permissions.** They only cap what IAM can allow — and they don't apply to the management account.
17. **An explicit Deny can never be overridden.**
18. **IAM roles, not access keys, for EC2 and Lambda.** Hard-coded credentials are always the wrong answer.
19. **API Gateway times out at 29 seconds.** Long work must be asynchronous (202 + SQS/Step Functions).
20. **Lambda caps at 15 minutes.** Longer jobs → Fargate, Batch, EC2, or Step Functions.
21. **SQS does not fan out and cannot replay.** Multiple independent consumers → **SNS → SQS** or **Kinesis**.
22. **Firehose is near real time (~60 s minimum).** True real time → **Kinesis Data Streams**.
23. **DynamoDB `Scan` reads (and bills for) the whole table.** Use a **GSI** and `Query`.
24. **Enabling NLB cross-zone load balancing costs money** (ALB's is free and on by default).
25. **DR Region service quotas are separate and default-low** — raise them before you need them, and remember Capacity Reservations give capacity but no discount, while Savings Plans give a discount but no capacity.

---

# Final Study Flow

**Week 1 — Domain 1 (Secure, 30%)**
Read Tasks 1.1–1.3 in full. Draw the IAM policy evaluation flow from memory. Build a VPC with public/private subnets, a NAT gateway, security groups, and an S3 gateway endpoint. Do all 60 Domain 1 practice questions and review every explanation, including the ones you got right.

**Week 2 — Domain 2 (Resilient, 26%)**
Read Tasks 2.1–2.2. Memorize the four DR strategies with their RTO/RPO and cost ordering. Build a Multi-AZ ALB + ASG + RDS stack and force a failover. Build an SNS → two SQS → two consumers fan-out. Do the 40 Domain 2 questions.

**Week 3 — Domain 3 (High-Performing, 24%)**
Read Tasks 3.1–3.5. Memorize the storage class and EBS volume tables, and the Kinesis Data Streams vs Firehose vs SQS comparison. Load sample data to S3, convert to partitioned Parquet, and query it with Athena. Do the 100 Domain 3 questions.

**Week 4 — Domain 4 (Cost-Optimized, 20%) and revision**
Read Tasks 4.1–4.4. Memorize the purchasing-model table and the data-transfer cost rules. Explore Cost Explorer, Budgets, Trusted Advisor, and Compute Optimizer in a real account. Do the 80 Domain 4 questions.

Then: sit the **65-question Full-Length Mock Exam** under timed conditions (130 minutes, no notes). Score it and map every wrong answer back to its task folder. Re-read those sections, redo those practice questions, and review `Exam-Day-Cheatsheet.md` the evening before and the morning of the exam.

**Answering strategy in the exam**
1. Read the **last sentence first** — it tells you what is actually being asked.
2. Identify the **constraint keyword**: *most cost-effective*, *least operational overhead*, *highest availability*, *lowest latency*, *minimal changes*. Two options are often both technically correct; the constraint picks the winner.
3. Eliminate options that are **technically impossible** (HDD boot volume, Lambda running 30 minutes, security group deny rule, cross-AZ EBS attach).
4. Eliminate options that **violate best practice** (hard-coded keys, public database subnets, root user, single AZ for production).
5. Prefer **managed and serverless** when the question says least overhead; prefer **purpose-built** services over generic ones.
6. Flag anything taking more than two minutes and come back. Answer every question — there is no penalty for guessing.
