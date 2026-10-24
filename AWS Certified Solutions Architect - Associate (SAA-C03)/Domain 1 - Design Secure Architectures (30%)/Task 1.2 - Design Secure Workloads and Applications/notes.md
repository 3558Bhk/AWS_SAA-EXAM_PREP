# Task 1.2 — Design Secure Workloads and Applications

> This task is about the **network and application layers**: how you build a VPC that segments traffic, how you keep application secrets out of code, how you defend against attacks coming from outside AWS, and how you connect securely to on-premises networks.

---

# 1. VPC Fundamentals

## 1.1 What a VPC is

A **Virtual Private Cloud** is a logically isolated section of the AWS network, dedicated to your account, in **one Region**. Inside it you define your own IP address range, subnets, route tables, and gateways. A VPC **spans all Availability Zones in its Region**, which is why you can place subnets in different AZs within the same VPC.

Every account comes with a **default VPC** in each Region (`172.31.0.0/16`) with a public subnet per AZ, an internet gateway, and a default security group. Default VPCs are convenient but not appropriate for production — the subnets are all public and the CIDR may clash with on-premises ranges.

## 1.2 CIDR planning

- IPv4 CIDR block size must be between **/16 (65,536 addresses) and /28 (16 addresses)**.
- The CIDR **cannot be changed after creation**, but you can **add up to four secondary CIDR blocks** later (they must not overlap and must follow RFC 1918 rules relative to the primary).
- **Never overlap** with on-premises ranges or with VPCs you may later peer with — VPC peering and Transit Gateway both forbid overlapping CIDRs. This is the single most common long-term networking mistake.
- Recommended practice: allocate from a central plan (RFC 1918 space: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), one non-overlapping block per VPC, with room to grow. **AWS VPC IP Address Manager (IPAM)** automates this allocation and tracking across accounts and Regions.

## 1.3 Subnets

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

## 1.4 Gateways

- **Internet Gateway (IGW)** — a horizontally scaled, redundant, highly available VPC component that allows communication between the VPC and the internet. One per VPC. It performs 1:1 NAT between the instance's private IP and its public/Elastic IP. For an instance to reach the internet it needs: a public or Elastic IP, a route `0.0.0.0/0 → igw-xxxx`, and permissive SG/NACL rules.
- **NAT Gateway** — a managed service that lets instances in **private** subnets initiate **outbound** connections to the internet (and to other VPC-external services) while preventing the internet from initiating inbound connections.
  - Lives **in a public subnet**, requires an **Elastic IP**, and is an **AZ-scoped resource**.
  - Scales automatically from 5 Gbps to **100 Gbps**.
  - Charged **per hour plus per GB processed** — a well-known cost trap.
  - For high availability, deploy **one NAT gateway per AZ** and point each AZ's private route table at its local NAT gateway. A single NAT gateway is both a single point of failure and a source of cross-AZ data charges.
  - **Security groups cannot be attached** to a NAT gateway; control traffic with NACLs and with the SGs of the instances behind it.
- **NAT Instance (legacy)** — an EC2 instance performing NAT. Cheaper at very low volume and supports port forwarding and acting as a bastion, but **you** manage patching, HA, and scaling, and you must **disable the source/destination check** on the instance.
- **Egress-only Internet Gateway** — the IPv6 equivalent of a NAT gateway: outbound-only. IPv6 addresses are always globally routable, so this is how you prevent inbound IPv6 connections.

## 1.5 Route tables

- Each subnet is associated with exactly one route table (the VPC's **main** route table by default).
- The `local` route covering the VPC CIDR is always present and cannot be removed or overridden — this is what makes all subnets in a VPC able to talk to each other by default.
- **Longest-prefix match wins**: a route for `10.0.5.0/24` beats `0.0.0.0/0`.
- Targets can be: IGW, NAT gateway, egress-only IGW, virtual private gateway, transit gateway, peering connection, network interface, gateway endpoint (via prefix list), or local.
- Best practice: a separate route table per subnet tier per AZ, so you can point each AZ at its own NAT gateway.

---

# 2. Security Groups vs Network ACLs

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

## 2.1 Why statefulness matters

With a **security group**, if you allow inbound TCP 443, the response packets going back out are automatically permitted regardless of outbound rules. With a **NACL**, you must add an outbound rule allowing the **ephemeral port range** (1024–65535) or responses will be dropped. The symptom — "requests go out but nothing comes back" or "connections hang" — is the classic NACL question.

## 2.2 Security group referencing

Instead of hardcoding CIDRs, reference another security group as the source:

- `sg-web` allows inbound 443 from `0.0.0.0/0`
- `sg-app` allows inbound 8080 **from `sg-web`**
- `sg-db` allows inbound 3306 **from `sg-app`**

This "SG chaining" survives auto scaling, IP changes, and AZ moves, and is the least-privilege pattern the exam expects. A security group can also reference **itself**, which is how cluster members (e.g., Elasticsearch nodes) talk to each other.

## 2.3 When to use a NACL

Because security groups cannot deny, NACLs are the answer whenever the requirement is to **block** something specific:
- Block a known malicious IP or CIDR from an entire subnet
- Add a coarse subnet-level guardrail that individual teams cannot remove by editing an SG
- Enforce one-way rules at a tier boundary

For Layer 7 blocking (a bad user agent, a URI pattern, a country), use **AWS WAF** instead.

---

# 3. Network Segmentation Strategy

## 3.1 The three-tier reference design

Repeat all three tiers in **at least two (ideally three) Availability Zones**:

**Public subnets** — internet-facing load balancers (ALB/NLB), NAT gateways, and (if you still use them) bastion hosts. Nothing that holds data.

**Private application subnets** — EC2 instances, ECS tasks, EKS nodes, Lambda ENIs. No route to the IGW; outbound via NAT gateway; `sg-app` accepts traffic only from the load balancer's security group.

**Private data subnets** — RDS, Aurora, ElastiCache, OpenSearch. Often with a route table that has **no `0.0.0.0/0` route at all**, so these instances cannot reach the internet even outbound. DB subnet groups must span multiple AZs for Multi-AZ deployments.

Additional segmentation ideas that appear in scenarios:
- A separate **management/shared services VPC** or subnet for monitoring and directory services.
- A dedicated **egress VPC** with centralized NAT and firewalling, reached via Transit Gateway.
- Separate VPCs (or accounts) per environment rather than per-subnet separation, when isolation requirements are strict.

## 3.2 VPC Flow Logs

Flow Logs capture **metadata about IP traffic** (not payloads) at the VPC, subnet, or ENI level.

- Fields include source/destination IP and port, protocol, packets, bytes, start/end time, action (**ACCEPT / REJECT**), and log status. Custom formats can add `vpc-id`, `subnet-id`, `instance-id`, `tcp-flags`, `pkt-srcaddr`, and `flow-direction`.
- Destinations: **CloudWatch Logs**, **S3**, or **Kinesis Data Firehose**.
- Uses: troubleshooting "why is this blocked" (look for REJECT), detecting port scans, feeding GuardDuty, and compliance evidence.
- **They do not capture packet contents.** For full packet capture use **VPC Traffic Mirroring**, which copies traffic from an ENI to a monitoring appliance.
- Some traffic is never logged: Amazon DNS server traffic, Windows license activation, instance metadata (`169.254.169.254`), DHCP, and traffic to the reserved VPC router address.

## 3.3 Diagnostic tools

- **VPC Reachability Analyzer** — performs static configuration analysis between a source and destination and tells you whether a path exists; if not, it names the blocking component (security group, NACL, route table).
- **Network Access Analyzer** — evaluates whether unintended network paths exist (e.g., "can anything in a private subnet reach the internet?").
- **VPC Network Access Analyzer / Flow Logs + Athena** for larger investigations.

---

# 4. VPC Endpoints and Private Service Access

## 4.1 The problem they solve

By default, calling `s3.ap-south-1.amazonaws.com` from a private subnet goes out through the NAT gateway to the public internet (even though it stays on AWS's network edge). That means: NAT data-processing charges, a dependency on internet routing, and traffic that leaves your VPC boundary — which some compliance regimes forbid.

**VPC endpoints** let you reach AWS services using private IP addresses, with no IGW, no NAT, and no public IPs.

## 4.2 The three endpoint types

| Type | How it works | Services | Cost |
|---|---|---|---|
| **Gateway endpoint** | Adds a **route table entry** pointing a managed **prefix list** at the endpoint | **Amazon S3 and DynamoDB only** | **Free** |
| **Interface endpoint (AWS PrivateLink)** | Creates an **ENI with a private IP** in each chosen subnet; DNS resolves the service name to that private IP | Most AWS services, partner SaaS, and your own services | Hourly per ENI per AZ + per-GB processed |
| **Gateway Load Balancer endpoint** | Routes traffic to a fleet of third-party virtual appliances using GENEVE | Firewalls, IDS/IPS | Hourly + per-GB |

**Gateway endpoint details:** region-specific, cannot be accessed from on-premises (over DX/VPN) directly, and are controlled by an **endpoint policy** plus route table association. Because they are free, "use a gateway endpoint for S3" is almost always the right answer when the question mentions S3 traffic and cost or privacy.

**Interface endpoint details:** supports **private DNS** (so the standard service hostname resolves privately), works from on-premises over Direct Connect/VPN, can be restricted with **security groups** on the endpoint ENI, and supports endpoint policies.

## 4.3 Locking resources to an endpoint

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

## 4.4 AWS PrivateLink for your own services

If you operate a service and want other VPCs (yours or customers') to consume it privately:
1. Put the service behind a **Network Load Balancer** (or GWLB).
2. Create a **VPC endpoint service** and allowlist the consumer principals.
3. Consumers create **interface endpoints** to your service.

Benefits: no VPC peering, **overlapping CIDRs are irrelevant** (traffic is NAT'd through the endpoint), the connection is **one-way** (consumer → provider), and nothing is exposed to the internet. This is the standard SaaS-on-AWS pattern and a frequent exam answer.

---

# 5. Threats From Outside AWS, and the Services That Stop Them

## 5.1 Distributed Denial of Service

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

## 5.2 Application-layer attacks and AWS WAF

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

## 5.3 AWS Network Firewall

A managed, stateful network firewall and intrusion prevention system deployed **inside your VPC** at a dedicated firewall subnet per AZ. It supports:
- **Stateless rules** (5-tuple filtering, fast path)
- **Stateful rules** using **Suricata-compatible** IPS signatures
- **Domain name filtering** for egress (allow only `*.example.com`, block everything else)
- Managed threat signature rule groups
- Centralized deployment with Transit Gateway for inspection of inter-VPC and egress traffic

Choose it when a question demands **deep packet inspection, IPS, or egress FQDN filtering** across a VPC — something security groups and NACLs cannot do.

## 5.4 Route 53 Resolver DNS Firewall

Filters **outbound DNS queries** from your VPC against domain allow/deny lists, including AWS-managed lists of known malicious domains. Useful against data exfiltration over DNS and malware command-and-control.

## 5.5 AWS Firewall Manager

A central policy manager that enforces security configuration **across all accounts in an AWS Organization**:
- AWS WAF web ACLs and rule groups
- Shield Advanced protections
- Security group policies (audit and enforce common rules, find unused/redundant groups)
- Network Firewall and DNS Firewall policies

Crucially, it applies policies to **existing and newly created resources automatically**. When a question says "ensure consistent rules across dozens of accounts, including new ALBs created in the future," the answer is **Firewall Manager**.

## 5.6 Detection and posture services

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

# 6. Application Configuration and Credentials Security

## 6.1 The rule

Credentials and configuration must never be hardcoded in source code, baked into AMIs or container images, committed to Git, or passed as plaintext environment variables that end up in logs. Instead, the application is given an **IAM role**, and it uses that role to fetch secrets at runtime from a managed store.

## 6.2 AWS Secrets Manager vs SSM Parameter Store

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

## 6.3 Eliminating passwords entirely

- **IAM database authentication** (RDS MySQL/PostgreSQL and Aurora): the application calls `generate-db-auth-token` using its IAM role and uses that token as the password. Tokens are valid for **15 minutes**, and there is no stored secret at all. Note the connection limit considerations (roughly 200 new connections/second).
- **IAM roles for all AWS service calls** — never an access key.
- **Amazon RDS Proxy** can retrieve credentials from Secrets Manager and enforce IAM authentication centrally.

## 6.4 Other configuration hygiene

- **Lambda environment variables** are encrypted at rest with KMS; for sensitive values use Secrets Manager/Parameter Store or at minimum a customer managed key with encryption helpers.
- **ECS/EKS**: inject secrets via the task definition's `secrets` block (pulled from Secrets Manager or Parameter Store) rather than `environment`.
- **AWS AppConfig** for safe, validated configuration deployment with rollback.
- Scan repositories for leaked credentials (git-secrets, CodeGuru, Amazon CodeWhisperer security scans) and rotate anything exposed.

---

# 7. Secure Application Access

## 7.1 Authenticating users to applications

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

## 7.2 Administrative access to instances

Ranked from best to worst for the exam:

1. **AWS Systems Manager Session Manager** — browser or CLI shell with **no inbound ports, no bastion host, no SSH keys, no public IPs**. Requires the SSM agent (pre-installed on Amazon Linux, Ubuntu, Windows AMIs), an instance role with `AmazonSSMManagedInstanceCore`, and connectivity to SSM endpoints (via NAT or **interface endpoints** for `ssm`, `ssmmessages`, `ec2messages`). Sessions can be **logged to S3/CloudWatch**, and access is controlled with IAM. This is the modern correct answer.
2. **EC2 Instance Connect / Instance Connect Endpoint** — push a temporary SSH key or tunnel SSH/RDP without public IPs.
3. **Bastion host** — a hardened instance in a public subnet with an SG restricted to the corporate CIDR; all admin traffic hops through it. Still appears in scenarios, but if Session Manager is an option it usually wins on "no inbound ports / least operational overhead."

---

# 8. Securing External Network Connections

## 8.1 AWS Site-to-Site VPN

- IPsec tunnels between your **customer gateway** (on-prem device) and a **virtual private gateway** (attached to a VPC) or a **transit gateway**.
- Each connection provides **two tunnels** terminating in different AZs for redundancy; each tunnel supports roughly **1.25 Gbps**. With Transit Gateway you can use **ECMP** across multiple tunnels to aggregate bandwidth.
- **Encrypted by default** (IPsec), runs over the public internet, so latency and jitter vary.
- Deployable in **minutes**, and inexpensive (hourly connection charge plus data transfer).
- Supports static routing or **BGP** dynamic routing.
- **AWS Client VPN** is the separate, OpenVPN-based service for individual remote users connecting into a VPC, with authentication via Active Directory, SAML, or certificates.

## 8.2 AWS Direct Connect

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

## 8.3 Choosing between them

| Requirement | Answer |
|---|---|
| Encrypted hybrid link, quick, low cost | **Site-to-Site VPN** |
| Consistent high bandwidth, predictable latency, large sustained transfers | **Direct Connect** |
| Private link **and** encryption in transit required | **IPsec VPN running over Direct Connect** (or MACsec on supported DX ports) |
| Direct Connect with resilient failover on a budget | **DX + VPN backup** |
| Many VPCs and multiple on-prem sites | **Transit Gateway** + DX Gateway and/or VPN attachments |
| Individual remote employees | **AWS Client VPN** |

---

# 9. Ports and Protocols Reference

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

# 10. Worked Scenarios

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

# 11. Quick Decision Table

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
