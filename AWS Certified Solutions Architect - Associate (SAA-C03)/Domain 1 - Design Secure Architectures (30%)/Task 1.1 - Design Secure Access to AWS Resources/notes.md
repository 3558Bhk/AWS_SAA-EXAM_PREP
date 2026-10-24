# Task 1.1 — Design Secure Access to AWS Resources

> **Weight:** Domain 1 is 30% of the exam and Task 1.1 is the most heavily tested single task in SAA-C03. Expect 8–12 questions touching IAM, roles, multi-account governance, and federation.
>
> **The one principle that answers most questions:** *identities should receive temporary, least-privilege credentials through roles, and permissions should be layered so that the narrowest boundary wins.*

---

# 1. The AWS Shared Responsibility Model

## 1.1 What the model actually says

AWS splits accountability at the line where the virtualization layer meets the customer's workload.

- **AWS is responsible for "security OF the cloud."** This is everything AWS operates: the physical data centers (badge access, guards, biometric locks), power and cooling, the server hardware, the storage media and its secure decommissioning, the networking fabric between racks and between AZs, the hypervisor, and the software that runs AWS's own managed services.
- **The customer is responsible for "security IN the cloud."** This is everything the customer configures and puts into the service: the data itself, who is allowed to touch it, how it is encrypted, the guest operating system on an EC2 instance, firewall rules, application code, and identity management.

The exam phrases this as a question about a specific service and asks which party handles a specific duty. The trick is that the dividing line **moves depending on the service model**.

## 1.2 How the line shifts by service model

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

## 1.3 Responsibilities that are *always* the customer's

No matter which service you use, these never transfer to AWS:
1. **Your data** — its content, its classification, and its retention.
2. **Identity and access management** — who has credentials and what those credentials may do.
3. **Account-level configuration** — MFA on root, password policy, enabled Regions.
4. **Deciding whether to encrypt** and managing key policies (even when AWS supplies the key material).

## 1.4 Shared controls

Some controls are shared, meaning both parties do a version of the same thing at different layers:
- **Patch management** — AWS patches the infrastructure and managed service software; you patch guest OS and applications.
- **Configuration management** — AWS configures its infrastructure devices; you configure your OS, databases, and applications.
- **Awareness and training** — AWS trains AWS employees; you train yours.

## 1.5 Exam patterns

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

# 2. AWS Global Infrastructure (from a security and access angle)

## 2.1 Regions

A **Region** is a separate geographic area containing multiple isolated data center clusters — for example `ap-south-1` (Mumbai), `us-east-1` (N. Virginia), `eu-west-1` (Ireland).

Key properties that matter for secure design:
- **Regions are isolated from each other by default.** Data you put in a Region stays in that Region unless you take an explicit action to move it (enabling cross-Region replication, copying a snapshot, creating a cross-Region read replica, using a global service). This is the foundation of **data residency** compliance: if regulation says data must remain in India, you place resources in `ap-south-1` and use an SCP to deny other Regions.
- **Some Regions are opt-in** (newer Regions like Hong Kong, Bahrain, Milan). They must be explicitly enabled in account settings, and credentials from STS global endpoints may not work there unless you use the Regional endpoint or enable global STS tokens for all Regions.
- **Region selection criteria**: compliance/data residency first, then latency to users, then service availability (not every service exists in every Region), then price (prices differ per Region).

## 2.2 Availability Zones

An **Availability Zone** is one or more discrete data centers within a Region, each with redundant power, networking, and connectivity, housed in separate facilities.

- AZs are **physically separated** — typically tens of kilometres apart — so that a fire, flood, or power event affects only one.
- They are connected by **dedicated, redundant, low-latency metro fibre**, giving single-digit-millisecond (usually < 1–2 ms) round-trip latency. That is fast enough for **synchronous replication**, which is exactly how RDS Multi-AZ and Aurora work.
- **AZ names are randomized per account.** Your `us-east-1a` is probably not the same physical AZ as another account's `us-east-1a`. AWS does this to balance load across AZs. When you must correlate AZs between accounts (for example when sharing subnets via RAM, or minimizing cross-AZ traffic in a multi-account architecture), use the **AZ ID** (`use1-az1`), which *is* consistent across accounts.
- Most Regions have 3 or more AZs; a few have 6.

## 2.3 Other infrastructure elements

- **Local Zones** — an extension of a Region placed in a large metro area, giving single-digit-millisecond latency for things like media production, gaming, and remote workstations. You extend a VPC into a Local Zone with a subnet.
- **Wavelength Zones** — AWS infrastructure embedded inside telecom providers' 5G networks for ultra-low-latency mobile applications.
- **AWS Outposts** — physical AWS racks installed in your own data center, running a subset of AWS services locally. Used for strict data residency or when an application must sit next to on-prem systems.
- **Edge locations and Regional edge caches** — hundreds of points of presence worldwide used by CloudFront, Route 53, AWS Shield, AWS WAF, Global Accelerator, and S3 Transfer Acceleration. **DDoS absorption happens here**, far from your origin.

## 2.4 Global vs Regional services

This distinction appears in security questions constantly.

**Global (one namespace, no Region selector):**
IAM, AWS Organizations, Route 53, CloudFront, AWS WAF when attached to CloudFront, AWS Shield, Billing, Trusted Advisor, and the S3 *namespace* (bucket names are globally unique, though each bucket's data lives in one Region).

**Regional (resources exist independently in each Region):**
EC2, VPC, EBS, RDS, Lambda, DynamoDB, SQS, SNS, CloudWatch, CloudTrail trails (unless you make them multi-Region), **KMS keys**, **ACM certificates**, Secrets Manager secrets, and Service Quotas.

Two consequences you will be tested on:
1. **A KMS key cannot be used in another Region.** To decrypt a cross-Region replicated object, the destination Region needs its own key, or you use a **multi-Region key**.
2. **An ACM certificate for CloudFront must be requested in `us-east-1`**, because CloudFront is a global service whose control plane lives there. For an ALB, the certificate must exist in the ALB's own Region.

---

# 3. IAM — Identities and Principals

## 3.1 Authentication vs authorization

IAM performs two distinct jobs, and the exam often tests whether you can tell them apart:
- **Authentication** — proving who you are. For a human: username + password (+ MFA). For code: an access key ID and secret, or a signed request using temporary credentials.
- **Authorization** — deciding whether the authenticated principal may perform the requested action on the requested resource. This is the policy evaluation engine.

Every API request to AWS is signed (Signature Version 4) and carries an identity. IAM evaluates the request against all applicable policies and returns allow or deny.

## 3.2 Anatomy of an ARN

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

## 3.3 The root user

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

## 3.4 IAM users

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

## 3.5 IAM groups

A group is a container for users that lets you attach policies once and apply them to many users. Important constraints:
- **Groups cannot be nested** (no group inside a group).
- **A group is not a principal.** You cannot put a group ARN in the `Principal` element of a resource-based policy, and a group cannot assume a role.
- Users can belong to multiple groups (up to 10 by default); their effective permissions are the union of all attached policies.

## 3.6 IAM roles — the centrepiece

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

## 3.7 The credential provider chain

When an SDK or the CLI runs, it looks for credentials in this order (simplified, and worth knowing because it explains "why is my app still using the old keys?"):
1. Command-line options / explicit parameters in code
2. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`)
3. Shared credentials file (`~/.aws/credentials`)
4. Shared config file (`~/.aws/config`), including assumed-role profiles
5. Container credentials (ECS task role endpoint)
6. **Instance profile credentials from IMDS**

So if an instance has a role but someone also left static keys in `~/.aws/credentials`, the static keys win — a frequent real-world and exam gotcha.

---

# 4. Policies and the Authorization Model

## 4.1 The six policy types

| Type | Attached to | Grants? | Key purpose |
|---|---|---|---|
| **Identity-based policy** | IAM user, group, or role | Yes | What this identity may do |
| **Resource-based policy** | The resource itself | Yes | Who may access this resource; **has a `Principal` element** |
| **Permissions boundary** | A user or role | **No** | Hard ceiling on the identity's maximum permissions |
| **Service Control Policy (SCP)** | Org root, OU, or account | **No** | Hard ceiling on everything in the member account |
| **Session policy** | Passed inline during `AssumeRole` | **No** (narrows) | Further restricts a specific session |
| **Access control list (ACL)** | S3 objects/buckets (legacy) | Yes | Legacy cross-account object grants |

Identity-based policies come in three flavours: **AWS managed** (maintained by AWS, e.g., `ReadOnlyAccess`, `AmazonS3FullAccess`), **customer managed** (your reusable policies — the recommended default), and **inline** (embedded in a single identity, deleted with it; use only when a strict 1:1 relationship is required).

## 4.2 Policy JSON element by element

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

## 4.3 Condition operators and keys

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

## 4.4 Policy evaluation logic — the complete flow

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

### Same-account vs cross-account

- **Same account:** identity policy **OR** resource policy is enough. If a bucket policy allows your role, you don't strictly need an S3 statement in the role's policy (though most teams add both).
- **Cross-account:** you need **BOTH**. Account A's identity policy must allow the action, **and** Account B's resource policy (or role trust policy) must allow the principal from Account A. This "both sides must agree" rule is tested repeatedly.
- **Exception worth knowing:** KMS key policies are authoritative — the key policy must grant access, and it can delegate to IAM in the same account using the `"AWS": "arn:aws:iam::<acct>:root"` principal with `kms:*`. Without that delegation statement, IAM policies alone cannot grant key use.

## 4.5 Permissions boundaries in practice

A boundary doesn't grant anything; it caps what an identity can ever be granted. The classic use case is **delegated administration**: you want developers to create roles for their own applications without being able to create an admin role.

Implementation pattern:
1. Create a customer managed policy, e.g., `DeveloperBoundary`, allowing only S3, DynamoDB, Lambda, and CloudWatch.
2. Grant developers `iam:CreateRole` and `iam:AttachRolePolicy` **with a condition** requiring `iam:PermissionsBoundary` to equal the ARN of `DeveloperBoundary`.
3. Deny `iam:DeleteRolePermissionsBoundary` and `iam:PutRolePermissionsBoundary` changes.

Now any role a developer creates is permanently capped by the boundary, even if they attach `AdministratorAccess` to it.

## 4.6 RBAC vs ABAC

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

# 5. AWS STS, Role Switching and Cross-Account Access

## 5.1 What STS returns

AWS Security Token Service issues **temporary credentials** consisting of three parts: an access key ID, a secret access key, and a **session token** (the presence of the session token is what distinguishes temporary from long-term credentials). They expire automatically, which is why they are inherently safer than IAM user keys.

Duration rules:
- Default session: **1 hour**.
- Maximum: set by the role's **maximum session duration** setting, which can be 1–12 hours. The caller can request up to that maximum with `DurationSeconds`.
- **Role chaining** (using one assumed role to assume another) is **capped at 1 hour** and cannot be extended.
- `GetSessionToken` for IAM users: 15 minutes to 36 hours (default 12); for root, maximum 1 hour.

## 5.2 The STS API surface

| API | Used for |
|---|---|
| `AssumeRole` | Cross-account access and same-account role switching by IAM principals |
| `AssumeRoleWithSAML` | Enterprise federation from AD FS / any SAML 2.0 IdP |
| `AssumeRoleWithWebIdentity` | OIDC federation — Cognito identity pools, Google/Facebook/Apple, **EKS IRSA**, GitHub Actions OIDC |
| `GetSessionToken` | Temporary credentials for an IAM user, typically to satisfy an MFA condition |
| `GetFederationToken` | Temporary credentials for a federated user from a proxy application |
| `GetCallerIdentity` | "Who am I?" — no permissions required, great for troubleshooting |

## 5.3 Setting up cross-account access (the canonical pattern)

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

## 5.4 External ID and the confused deputy problem

When a **third-party SaaS vendor** (monitoring, cost analytics, backup) needs access to your account, a naive cross-account role creates a risk: the vendor's system holds many customers' role ARNs, and an attacker who learns your role ARN could trick the vendor into assuming *your* role while acting for *their* account. This is the **confused deputy** problem.

The fix is `sts:ExternalId`: the vendor generates a unique secret per customer, you place it in the trust policy as a condition, and the vendor must pass it on every `AssumeRole` call.

```json
"Condition": { "StringEquals": { "sts:ExternalId": "a7f3c9e1-unique-per-customer" } }
```

**Exam cue:** "third-party", "vendor", "partner needs access to your account" → **cross-account role with ExternalId**.

## 5.5 `iam:PassRole` and privilege escalation

When you launch an EC2 instance with an instance profile, or create a Lambda function with an execution role, you are "passing" a role to a service. That requires the `iam:PassRole` permission. If a user has broad `iam:PassRole` on `*` plus `ec2:RunInstances`, they can launch an instance with an administrator role attached and effectively become an administrator. **Always scope PassRole** to specific role ARNs and add a `iam:PassedToService` condition.

## 5.6 IAM Roles Anywhere

For servers and workloads **outside AWS** that need AWS credentials without IAM user keys, IAM Roles Anywhere lets you use X.509 certificates from your own certificate authority (registered as a trust anchor) to obtain temporary credentials. This is the modern answer to "our on-premises application needs to call AWS APIs securely without long-lived keys."

---

# 6. Federation and Identity Services

## 6.1 Why federate

If your organization already maintains identities in Active Directory, Okta, Entra ID (Azure AD), or another IdP, recreating those users in IAM means duplicated accounts, duplicated offboarding, and inconsistent MFA. Federation lets the IdP remain the single source of truth while AWS issues short-lived credentials mapped to roles.

## 6.2 AWS IAM Identity Center (successor to AWS SSO)

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

## 6.3 Classic SAML 2.0 federation with IAM (pre-Identity Center)

Still examinable and still used where Identity Center isn't deployed:

1. Create a **SAML identity provider** object in IAM, uploading the IdP's metadata XML.
2. Create IAM roles whose trust policy trusts that provider with `sts:AssumeRoleWithSAML` and a condition on `SAML:aud`.
3. The IdP's SAML assertion includes attributes (`https://aws.amazon.com/SAML/Attributes/Role`) listing the role ARN and provider ARN.
4. The user hits the IdP, authenticates, is redirected to the AWS sign-in endpoint with the assertion, and STS returns temporary credentials for the chosen role.

The main drawback versus Identity Center: you must create and maintain the provider object and roles in **every account**.

## 6.4 AWS Directory Service options

| Option | What it is | Use when |
|---|---|---|
| **AWS Managed Microsoft AD** | A real Microsoft AD (Standard or Enterprise) running in your VPC, managed by AWS | You need full AD features in AWS, want to support AD-aware workloads (FSx for Windows, RDS for SQL Server, EC2 domain join), and/or want a **trust relationship** with on-prem AD |
| **AD Connector** | A proxy that forwards authentication requests to your on-premises AD | You want AWS services to use on-prem AD **without storing any directory data in AWS** |
| **Simple AD** | Samba-based, lightweight, Linux-friendly | Small, simple directory needs; **no trusts, no MFA, limited features** |

## 6.5 Amazon Cognito — customer/app identities

Cognito is for **application end users**, not employees. Two distinct components:
- **User pool** — a user directory providing sign-up, sign-in, password policies, MFA, email/phone verification, a hosted UI, and federation with social IdPs (Google, Facebook, Apple) and enterprise IdPs (SAML/OIDC). It returns **JWTs** (ID token, access token, refresh token). ALB and API Gateway can validate these tokens natively.
- **Identity pool (federated identities)** — exchanges a token (from a user pool or a social IdP) for **temporary AWS credentials** via STS, mapped to an IAM role. Supports authenticated and unauthenticated (guest) roles, and role selection based on token claims.

Classic pattern: a mobile app authenticates against a user pool, passes the token to an identity pool, and receives credentials scoped by a policy using `${cognito-identity.amazonaws.com:sub}` so each user can only read/write their own S3 prefix or DynamoDB rows.

> **Remember the split: workforce → IAM Identity Center; customers/app users → Cognito; servers/services → IAM roles.**

## 6.6 OIDC federation for workloads

- **EKS IRSA (IAM Roles for Service Accounts)** — the cluster's OIDC provider is registered in IAM so individual Kubernetes service accounts map to IAM roles, giving pod-level least privilege.
- **GitHub Actions / GitLab CI** — register the provider's OIDC endpoint and let pipelines assume a role with no stored AWS keys. This is the modern answer for "our CI/CD stores AWS access keys as secrets — how do we fix it?"

---

# 7. Multi-Account Strategy

## 7.1 Why multiple accounts

An AWS account is the strongest isolation boundary available. Reasons to use many:
- **Blast radius containment** — a compromise or runaway process in dev cannot touch prod.
- **Security/compliance scoping** — keep PCI or HIPAA workloads in dedicated accounts so audits are narrower.
- **Billing separation** — per-team or per-product cost attribution without relying solely on tags.
- **Service quota isolation** — quotas are per account per Region, so one team can't exhaust another's limits.
- **Simpler IAM** — permissions in a small single-purpose account are far easier to keep least privilege.

Typical structure: Management (payer) account; Security OU with Log Archive and Audit/Security Tooling accounts; Infrastructure OU with Network and Shared Services accounts; Workloads OU split into Prod and Non-Prod; a Sandbox OU with tight SCPs and budgets; a Suspended OU with a deny-all SCP for decommissioned accounts.

## 7.2 AWS Organizations

- **Management (payer) account** sits at the root; it creates/invites **member accounts** and owns consolidated billing.
- **Organizational Units (OUs)** group accounts into a hierarchy (nesting up to 5 levels deep). Policies attached to an OU are inherited by all accounts beneath it.
- **Feature sets:** *Consolidated billing only* (just billing) or **All features** (required for SCPs and most governance features).
- **Policy types** you can enable: **Service control policies**, **tag policies** (enforce tag key casing/allowed values), **backup policies** (org-wide AWS Backup plans), **AI services opt-out policies**, and **chat applications policies**.
- **Delegated administrator** — you can nominate a member account to administer a service org-wide (GuardDuty, Security Hub, Config, Macie, IAM Access Analyzer, Backup), so the management account isn't used for daily operations.
- **Consolidated billing benefits:** one bill; **volume pricing tiers aggregate across accounts** (so combined S3 usage reaches cheaper tiers sooner); **unused RIs and Savings Plans are shared** across accounts by default (can be disabled per account).

## 7.3 Service Control Policies in depth

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

## 7.4 AWS Control Tower

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

## 7.5 AWS Resource Access Manager (RAM)

RAM shares resources across accounts in an organization without duplicating them or building peering meshes. Commonly shared: **VPC subnets** (VPC sharing — a central network account owns the VPC, workload accounts deploy into its subnets), **Transit Gateways**, **Route 53 Resolver rules**, **License Manager configurations**, **Aurora DB clusters**, and **Image Builder components**.

## 7.6 Organization-wide security services

- **Organization CloudTrail trail** — created in the management account, automatically applies to all member accounts (current and future), delivering to one S3 bucket in the Log Archive account. Enable **log file validation**, SSE-KMS encryption, and **S3 Object Lock** on the bucket so logs are tamper-evident and immutable.
- **AWS Config aggregator** — multi-account, multi-Region view of configuration and compliance.
- **Security Hub** with a delegated administrator — single pane of findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, plus CIS/PCI/AWS FSBP standards.
- **GuardDuty / Macie / Inspector** all support delegated administration and auto-enrollment of new accounts.

---

# 8. Resource-Based Policies — When and Why

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

# 9. Troubleshooting "Access Denied" — a repeatable method

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

# 10. Worked Scenarios

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

# 11. Quick Decision Table

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

# 12. Memory Hooks

- "**Explicit Deny beats everything**; implicit deny is the default; nothing is allowed until something allows it."
- "**SCPs and boundaries limit; policies grant.** Effective = intersection of ceilings ∩ union of grants."
- "**Roles, not keys. Temporary, not permanent.**"
- "**Cross-account means both sides must say yes.**"
- "**Workforce → Identity Center. Customers → Cognito. Compute → roles. Partners → role + ExternalId.**"
- "**Bucket ARN lists, object ARN gets.**"
- "**If you can list but not download, suspect KMS.**"
