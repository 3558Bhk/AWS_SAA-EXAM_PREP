# AWS — Cloud Engineer Interview Master Notes (4–6 Years Experience)

> **Covers:** Cloud Engineer · Senior DevOps Engineer · SRE · Platform Engineer · Solutions Architect (Associate/Professional) interview scope for AWS.
> **Structure for every topic:** Definition → Important Points → **Use cases & comparisons** → Edge Cases & Gotchas → Interview Q&A (Basic / Medium / Hard-Scenario) → **Production troubleshooting** for the high-frequency services.
> **Six-part standard used for service-depth topics:** Definition → Important Points → Use cases & comparisons → Edge cases & gotchas → Interview Q&A → Production troubleshooting (commands, expected output, root cause, mitigation, prevention).
> **Two Basic + two Intermediate + three Scenario questions** is the target density per service; where a topic shows three questions they are Basic / Medium / Hard-Scenario.
> **Legend:** ★★★ = asked in almost every 4-year interview · ★★ = common follow-up · ★ = senior/architect depth.
> **Accuracy note:** Default quotas, instance types, supported features and regional availability change. Numbers here reflect the state at the time of writing (Oct 2026). Verify against the AWS docs and the Service Quotas console before an interview or a production decision.

---

<details>
<summary><strong>Table of contents</strong> (click to expand)</summary>


**PART 1 — GLOBAL INFRASTRUCTURE & FUNDAMENTALS**

- [1.1 AWS Regions ★★★](#11-aws-regions)
- [1.2 Availability Zones (AZs) ★★★](#12-availability-zones-azs)
- [1.3 AWS Data Centers & Physical Infrastructure ★](#13-aws-data-centers-physical-infrastructure)
- [1.4 Edge Network, Local Zones, Wavelength, Outposts ★★](#14-edge-network-local-zones-wavelength-outposts)
- [1.5 AWS Shared Responsibility Model ★★★](#15-aws-shared-responsibility-model)
- [1.6 AWS Well-Architected Framework ★★★](#16-aws-well-architected-framework)
- [1.7 AWS Organizations, SCPs, Control Tower & Multi-Account ★★★](#17-aws-organizations-scps-control-tower-multi-account)
- [1.8 Migration Strategies — the 7 Rs ★★](#18-migration-strategies-the-7-rs)
- [1.9 IP Subnetting & AWS Reserved IP Addresses ★★★](#19-ip-subnetting-aws-reserved-ip-addresses)
- [1.10 Quotas, Service Limits & Support Plans ★★](#110-quotas-service-limits-support-plans)

**PART 2 — NETWORKING**

- [2.1 VPC Fundamentals & Design ★★★](#21-vpc-fundamentals-design)
- [2.2 Internet Gateway, NAT Gateway & NAT Instance ★★★](#22-internet-gateway-nat-gateway-nat-instance)
- [2.3 VPC Endpoints & AWS PrivateLink ★★★](#23-vpc-endpoints-aws-privatelink)
- [2.4 VPC Peering ★★★](#24-vpc-peering)
- [2.5 AWS Transit Gateway ★★★](#25-aws-transit-gateway)
- [2.6 Site-to-Site VPN & Direct Connect ★★★](#26-site-to-site-vpn-direct-connect)
- [2.7 Security Groups vs Network ACLs ★★★](#27-security-groups-vs-network-acls)
- [2.8 Application Load Balancer (ALB) ★★★](#28-application-load-balancer-alb)
- [2.9 Network Load Balancer (NLB) ★★★](#29-network-load-balancer-nlb)
- [2.10 Route 53 ★★★](#210-route-53)
- [2.11 CloudFront ★★★](#211-cloudfront)
- [2.12 AWS WAF & Shield ★★](#212-aws-waf-shield)
- [2.13 AWS Network Firewall & VPC Traffic Inspection ★★](#213-aws-network-firewall-vpc-traffic-inspection)
- [2.14 AWS Global Accelerator ★★](#214-aws-global-accelerator)
- [2.15 VPC Flow Logs, Reachability Analyzer & Network Troubleshooting ★★](#215-vpc-flow-logs-reachability-analyzer-network-troubleshooting)
- [2.16 VPC Lattice, Verified Access & DNS Exfiltration Controls ★★](#216-vpc-lattice-verified-access-dns-exfiltration-controls)

**PART 3 — COMPUTE**

- [3.1 Amazon EC2 — Instances & Families ★★★](#31-amazon-ec2-instances-families)
- [3.2 EC2 Purchasing Options, Spot, RIs & Savings Plans ★★★](#32-ec2-purchasing-options-spot-ris-savings-plans)
- [3.3 Amazon EBS — Types, Snapshots & Performance ★★★](#33-amazon-ebs-types-snapshots-performance)
- [3.4 Instance Store & EFS & FSx ★★](#34-instance-store-efs-fsx)
- [3.5 ECS & Fargate ★★★](#35-ecs-fargate)
- [3.6 Amazon EKS ★★★](#36-amazon-eks)
- [3.7 AWS Lambda ★★★](#37-aws-lambda)
- [3.8 API Gateway ★★★](#38-api-gateway)
- [3.9 AWS Batch, Step Functions & Event-Driven Orchestration ★★](#39-aws-batch-step-functions-event-driven-orchestration)
- [3.10 Elastic Beanstalk & App Runner (awareness) ★](#310-elastic-beanstalk-app-runner-awareness)
- [3.11 AWS Systems Manager (SSM) ★★★](#311-aws-systems-manager-ssm)

**PART 4 — STORAGE**

- [4.1 Amazon S3 — Fundamentals ★★★](#41-amazon-s3-fundamentals)
- [4.2 S3 Storage Classes & Lifecycle ★★★](#42-s3-storage-classes-lifecycle)
- [4.3 S3 Security Deep Dive ★★★](#43-s3-security-deep-dive)
- [4.4 Amazon EBS vs EFS vs S3 vs FSx — Choosing Storage ★★](#44-amazon-ebs-vs-efs-vs-s3-vs-fsx-choosing-storage)
- [4.5 Amazon S3 Access Points, Multi-Region Access Points & Transfer ★★](#45-amazon-s3-access-points-multi-region-access-points-transfer)

**PART 5 — DATABASES**

- [5.1 Amazon RDS — Engines & Operations ★★★](#51-amazon-rds-engines-operations)
- [5.2 RDS Multi-AZ vs Read Replicas vs Multi-AZ DB Cluster ★★★](#52-rds-multi-az-vs-read-replicas-vs-multi-az-db-cluster)
- [5.3 Amazon Aurora ★★★](#53-amazon-aurora)
- [5.4 Amazon DynamoDB — Keys, Capacity & Hot Partitions ★★★](#54-amazon-dynamodb-keys-capacity-hot-partitions)
- [5.5 ElastiCache (Redis / Memcached) ★★★](#55-elasticache-redis-memcached)
- [5.6 Amazon OpenSearch, Redshift & Athena ★★](#56-amazon-opensearch-redshift-athena)
- [5.7 Database Selection Matrix ★★★](#57-database-selection-matrix)

**PART 6 — IDENTITY & SECURITY**

- [6.1 IAM — Users, Roles, Policies ★★★](#61-iam-users-roles-policies)
- [6.2 IAM Policy Evaluation Workbook ★★★](#62-iam-policy-evaluation-workbook)
- [6.3 AWS KMS ★★★](#63-aws-kms)
- [6.4 AWS Secrets Manager & SSM Parameter Store ★★★](#64-aws-secrets-manager-ssm-parameter-store)
- [6.5 AWS CloudTrail ★★★](#65-aws-cloudtrail)
- [6.6 Amazon GuardDuty, Security Hub, Inspector, Macie & Config ★★★](#66-amazon-guardduty-security-hub-inspector-macie-config)
- [6.7 ACM & Certificate Management ★★](#67-acm-certificate-management)
- [6.8 Amazon Cognito ★★](#68-amazon-cognito)
- [6.9 AWS Shield, WAF, Firewall Manager & Security Baseline ★★](#69-aws-shield-waf-firewall-manager-security-baseline)

**PART 7 — INTEGRATION & MESSAGING**

- [7.1 Amazon SQS ★★★](#71-amazon-sqs)
- [7.2 Amazon SNS ★★★](#72-amazon-sns)
- [7.3 Amazon EventBridge ★★★](#73-amazon-eventbridge)
- [7.4 Amazon Kinesis & MSK ★★](#74-amazon-kinesis-msk)
- [7.5 Messaging Selection Matrix ★★](#75-messaging-selection-matrix)

**PART 8 — AUTO SCALING & ELASTICITY**

- [8.1 Auto Scaling Groups ★★★](#81-auto-scaling-groups)
- [8.2 Scaling Strategies Beyond EC2 ★★](#82-scaling-strategies-beyond-ec2)

**PART 9 — MONITORING, LOGGING & OPERATIONS**

- [9.1 Amazon CloudWatch — Metrics, Alarms, Dashboards ★★★](#91-amazon-cloudwatch-metrics-alarms-dashboards)
- [9.2 CloudWatch Logs, Application Signals & X-Ray ★★](#92-cloudwatch-logs-application-signals-x-ray)
- [9.3 AWS Health, Trusted Advisor, Incident Response & Runbooks ★★](#93-aws-health-trusted-advisor-incident-response-runbooks)

**PART 10 — IaC & DEVOPS ON AWS**

- [10.1 AWS CloudFormation ★★★](#101-aws-cloudformation)
- [10.2 Terraform on AWS ★★★](#102-terraform-on-aws)
- [10.3 CI/CD on AWS ★★★](#103-cicd-on-aws)
- [10.4 Containers & Registries — ECR ★★](#104-containers-registries-ecr)

**PART 11 — DISASTER RECOVERY, RELIABILITY & COST**

- [11.1 DR Strategies (Backup & Restore → Pilot Light → Warm Standby → Multi-Site) ★★★](#111-dr-strategies-backup-restore-pilot-light-warm-standby-multi-site)
- [11.2 Reliability Patterns — Retries, Circuit Breakers, Idempotency, Bulkheads ★★★](#112-reliability-patterns-retries-circuit-breakers-idempotency-bulkheads)
- [11.3 AWS Cost Optimization ★★★](#113-aws-cost-optimization)
- [11.4 Tagging, FinOps & Governance ★★](#114-tagging-finops-governance)
- [11.5 AWS Backup & Restore Testing ★★★](#115-aws-backup-restore-testing)
- [11.6 Cross-Account Automation, Conformance Packs & Audit Trails ★★](#116-cross-account-automation-conformance-packs-audit-trails)

**PART 12 — PRODUCTION TROUBLESHOOTING PLAYBOOKS (15 SCENARIOS)**

- [12.1 EC2 is running but SSH/SSM access fails](#121-ec2-is-running-but-sshssm-access-fails)
- [12.2 Private EC2 cannot reach the internet](#122-private-ec2-cannot-reach-the-internet)
- [12.3 ALB returns intermittent 502 / 503 / 504](#123-alb-returns-intermittent-502-503-504)
- [12.4 ASG does not launch instances during peak traffic](#124-asg-does-not-launch-instances-during-peak-traffic)
- [12.5 Cross-VPC connectivity fails through Transit Gateway](#125-cross-vpc-connectivity-fails-through-transit-gateway)
- [12.6 S3 returns AccessDenied despite an IAM Allow](#126-s3-returns-accessdenied-despite-an-iam-allow)
- [12.7 RDS CPU reaches 95% and application latency increases](#127-rds-cpu-reaches-95-and-application-latency-increases)
- [12.8 EKS pods remain Pending or in ImagePullBackOff](#128-eks-pods-remain-pending-or-in-imagepullbackoff)
- [12.9 Terraform apply fails on state locking or drift](#129-terraform-apply-fails-on-state-locking-or-drift)
- [12.10 A deployment causes a production outage](#1210-a-deployment-causes-a-production-outage)
- [12.11 CloudWatch alarms are not triggering correctly](#1211-cloudwatch-alarms-are-not-triggering-correctly)
- [12.12 The AWS bill unexpectedly increases by 40%](#1212-the-aws-bill-unexpectedly-increases-by-40)
- [12.13 A production AZ fails and applications must recover](#1213-a-production-az-fails-and-applications-must-recover)
- [12.14 A cross-Region DR failover is required](#1214-a-cross-region-dr-failover-is-required)
- [12.15 A compromised IAM access key is detected](#1215-a-compromised-iam-access-key-is-detected)

**PART 13 — SENIOR SCENARIO DRILLS (60–90 second verbal set)**


**PART 14 — RAPID REVISION**

- [14.1 One-line differences you must not fumble](#141-one-line-differences-you-must-not-fumble)
- [14.2 Numbers worth memorising (verify before quoting)](#142-numbers-worth-memorising-verify-before-quoting)
- [14.3 Final 60-second self-test](#143-final-60-second-self-test)
- [14.4 Command cheat sheet — what to run, and what "good" looks like](#144-command-cheat-sheet-what-to-run-and-what-good-looks-like)

</details>



---

## How to use these notes (revision sprint — 6–8 focused hours/day)

| Day | Topics | Practical outcome |
| --- | --- | --- |
| 1 | AWS fundamentals, VPC, routing, hybrid connectivity | Design **and troubleshoot** a three-AZ VPC |
| 2 | IAM, KMS, Organizations, WAF, security services | Diagnose a policy denial and a security incident from evidence |
| 3 | EC2, ASG, ALB, S3, EBS, EFS | Deploy and troubleshoot a highly available application |
| 4 | RDS, Aurora, DynamoDB, Lambda, SQS/SNS/EventBridge | Explain scaling, replication and failure recovery |
| 5 | CloudWatch, CloudTrail, Config, AWS Backup, DR | Investigate an incident and design recovery to a stated RTO/RPO |
| 6 | Terraform, CI/CD, ECS/EKS, cost | Deploy a complete application via IaC; explain a bill spike |
| 7 | Architecture scenarios, mock interviews, behavioural | Two technical mocks and a written weak-area list |

> This is a **revision sprint**, not a from-scratch course. Read → say it out loud → do a lab for anything you cannot demonstrate.

**Where to spend the hours (4-year target balance)**

| Area | Share | Why |
| --- | --- | --- |
| Production troubleshooting & scenarios | **35%** | This is what separates 4 years from 2 — "what failed, how did you prove it" |
| Architecture & design decisions | **25%** | Trade-offs, alternatives, failure modes |
| Hands-on AWS / Terraform / automation | **20%** | Evidence beats definitions in a senior loop |
| Definitions & service internals | **15%** | Necessary, but not the differentiator |
| Behavioural & project ownership | **5%** | STAR stories with metrics and ownership |

**The question that decides a 4-year interview:**
> "What failed, how did you prove the root cause, how did you restore service safely, and what did you change to prevent recurrence?"

**Production scenario checklist — mark each only when you can give a 30-second diagnosis framework, three first commands, a realistic root cause, a safe mitigation and a permanent fix:**

- [ ] 1. EC2 is running but SSH/SSM access fails
- [ ] 2. Private EC2 cannot reach the internet
- [ ] 3. ALB returns intermittent 502 / 503 / 504
- [ ] 4. ASG does not launch instances during peak traffic
- [ ] 5. Cross-VPC connectivity fails through Transit Gateway
- [ ] 6. S3 returns AccessDenied despite an IAM Allow
- [ ] 7. RDS CPU reaches 95% and application latency increases
- [ ] 8. EKS pods remain Pending or in ImagePullBackOff
- [ ] 9. Terraform apply fails on state locking or drift
- [ ] 10. A deployment causes a production outage
- [ ] 11. CloudWatch alarms are not triggering correctly
- [ ] 12. The AWS bill unexpectedly increases by 40%
- [ ] 13. A production AZ fails and applications must recover
- [ ] 14. A cross-Region DR failover is required
- [ ] 15. A compromised IAM access key is detected

> Answers for all 15 are in **Part 12 — Production Troubleshooting Playbooks**.

**The 5-stage answer framework (use for every scenario question):**
1. **Impact** — who/what is affected, scope, business impact.
2. **Telemetry** — metrics, logs, traces, health checks, recent changes.
3. **Isolate** — network → compute → storage → identity → app → dependency.
4. **Mitigate safely** — rollback, failover, scale, traffic shift, config fix.
5. **Prevent recurrence** — RCA, guardrails, alarms, automation, test.

**The 6 questions behind every AWS service question at this level:**
Why this service → how is it configured → how is it secured → how does it fail → how do you monitor it → how do you recover it.

---

# PART 1 — GLOBAL INFRASTRUCTURE & FUNDAMENTALS

## 1.1 AWS Regions ★★★

**Definition:** An AWS Region is a geographically separate area containing multiple isolated Availability Zones where AWS deploys cloud infrastructure and services.

**Important Points**
- Region codes: `us-east-1`, `ap-south-1` (Mumbai), `ap-south-2` (Hyderabad), `eu-west-1`.
- Most Regions have 3 AZs; some have more (verify the current count per Region).
- Regions provide geographic isolation for compliance, data residency, latency and disaster recovery.
- Regional resources: VPC, subnets, EC2, EBS, RDS, regional load balancers, most caches.
- Global resources/services: IAM, Route 53 (global hosted zones), CloudFront, Global Accelerator, Organizations, WAF (global scope for CloudFront), billing.
- Cross-Region replication is always explicit (S3 CRR, RDS cross-Region replicas, DynamoDB Global Tables, EBS snapshots copy, backups copy).
- Pricing differs per Region (e.g., Mumbai vs `us-east-1`), and so do service availability, instance families and quotas.
- Use case: Primary workload in `ap-south-1`, DR in `ap-south-2`, chosen for latency + residency, not merely because it is "near".

**Edge Cases & Gotchas**
- Multi-AZ is **not** Region-failure protection.
- A service can be "available in the Region" but a specific instance family, GPU type, or feature may not be.
- S3 bucket names are globally unique within a partition (`aws`, `aws-cn`, `aws-us-gov`), but the data lives in the bucket's Region.
- Cross-Region data transfer is billed in most cases; architecture decisions change the bill.
- Service-linked roles, KMS keys, and ACM certificates are Region-scoped — a DR Region needs its own.
- Console default Region ≠ resource Region; many "resource not found" incidents are wrong-Region mistakes.

**Interview Questions**
- **Basic — What is an AWS Region?** → A geographically isolated AWS infrastructure location containing multiple Availability Zones. Resources such as VPCs, EC2 and RDS are created inside a chosen Region.
- **Medium — How do you choose a Region for an enterprise application?** → Evaluate: data residency/compliance, latency to users, service and instance availability, pricing, existing Direct Connect/latency from on-prem, DR requirements, and proximity to other dependent systems. Then validate with a proof of concept.
- **Hard/Scenario — The primary Region becomes unavailable. Does Multi-AZ restore the application?** → No. Multi-AZ survives an AZ failure. Region loss requires a cross-Region DR design: replicated data (S3 CRR / Aurora Global DB / DynamoDB Global Tables / snapshot copies), pre-built or infrastructure-as-code secondary capacity, and a traffic failover mechanism (Route 53 failover, Global Accelerator, CloudFront origin groups). State the RTO/RPO you designed for.

## 1.2 Availability Zones (AZs) ★★★

**Definition:** An Availability Zone is one or more physically separate data centers within a Region, with independent power, cooling and networking, connected to other AZs by low-latency private links.

**Important Points**
- An AZ is a **failure domain**; a Region is a **geographic boundary**.
- An EC2 instance runs in exactly one AZ. A subnet belongs to exactly one AZ.
- An ALB/NLB spans multiple AZs (subnets you attach), and cross-zone load balancing determines distribution.
- RDS Multi-AZ keeps a standby in a different AZ; Aurora replicates 6 ways across 3 AZs.
- AZ names (`us-east-1a`) are **mapped per account**; AZ IDs (`use1-az1`) identify the same physical zone across accounts. Cross-account architecture should compare AZ IDs.
- Use case: Application servers in 3 AZs behind an ALB; database Multi-AZ; NAT Gateway per AZ.

**Edge Cases & Gotchas**
- Many instances in one AZ = zero AZ fault tolerance.
- Cross-AZ traffic is charged in many paths (EC2↔EC2, ALB to targets, NAT Gateway, VPC endpoints). Chatty cross-AZ designs quietly cost money.
- Cross-zone load balancing is on by default for ALB and off by default for NLB (cost and distribution implications).
- Regional services still have zonal dependencies underneath (e.g., EKS nodes, ENIs, NAT gateways).
- Capacity: a single AZ can be out of capacity for a specific instance type even if the Region is not.

**Interview Questions**
- **Basic — Region vs AZ?** → A Region is a geographic area; an AZ is an isolated infrastructure location (one or more data centers) inside it.
- **Medium — Can an EC2 instance span multiple AZs?** → No. You achieve AZ tolerance with multiple instances in multiple AZs behind a load balancer, plus a data tier that replicates.
- **Hard/Scenario — AZ `ap-south-1a` fails and the app goes down, even though you have 4 servers.** → All 4 are evidently in that AZ. Fix: ASG across ≥3 AZs, ALB with subnets in all AZs, health checks, database Multi-AZ, and a capacity check that the "desired" count actually distributes (ASG does per-AZ balancing, but removal/spot behaviours can skew it).

## 1.3 AWS Data Centers & Physical Infrastructure ★

**Definition:** AWS data centers are the physical facilities housing servers, storage, networking equipment and supporting infrastructure; one or more of them form an Availability Zone.

**Important Points**
- Multiple data centers can constitute an AZ; AWS designs them with independent power, cooling, networking and fire suppression.
- AWS owns physical security, hardware lifecycle, host patching and the hypervisor layer — customers have no physical access.
- **Nitro System** offloads virtualisation, networking and storage to dedicated hardware, improving performance, isolation and security (and enabling features like ENA, NVMe and confidential computing options).
- Hardware redundancy is engineered within AZs; AZs are engineered for independence within a Region.
- Customers select a **Region and AZ** (or let the platform choose), never an individual data center or rack.
- Dedicated Hosts and Dedicated Instances provide hardware-level isolation for licensing/compliance, still without physical access.
- Use case: compliance evidence comes from AWS certifications/audit reports (SOC, ISO, PCI), not from customer inspection of a facility.

**Edge Cases & Gotchas**
- A hardware failure is usually invisible: AWS retires/migrates hosts, instance status checks fire, and auto-recovery or ASG replacement handles it — only if you designed for replacement.
- AWS-controlled redundancy never replaces **application-level** backup/DR: an EBS volume is replicated within its AZ but not across Regions.
- Dedicated Hosts do not make a workload more available — they only change tenancy and licensing.
- Physical security certifications do not make your workload compliant; you still own access control, encryption and logging evidence.
- Host maintenance events (instance retirement, reboot events) are notified via AWS Health and EventBridge — subscribe to them.

**Interview Questions**
- **Basic — Who manages physical security of AWS data centers?** → AWS. Customers have no physical access; compliance relies on AWS audit reports plus customer configuration controls.
- **Medium — Can a customer choose which data center hosts an instance?** → No. Customers choose a Region and, where applicable, an AZ; AWS places the instance within that AZ.
- **Hard/Scenario — A hardware host fails. Does EC2 recover automatically?** → Not guaranteed. Depending on configuration, an instance may be stopped/retired or recovered via auto-recovery or ASG replacement. The robust design is stateless instances behind a load balancer with health checks, an ASG across AZs, and data on replicated/persistent storage.

## 1.4 Edge Network, Local Zones, Wavelength, Outposts ★★

**Definition:** AWS extends beyond Regions through a global edge network (CloudFront PoPs and Route 53 Resolver endpoints), Local Zones (compute close to metros), Wavelength (compute inside telecom 5G networks) and Outposts (AWS hardware in your data center).

**Important Points**
- **Edge locations / PoPs:** used by CloudFront, Route 53, Global Accelerator, Shield and WAF — CDN caching and DDoS absorption points.
- **Regional edge caches:** larger mid-tier caches between PoPs and origins.
- **Local Zones:** a Zone extension of a parent Region for single-digit-millisecond latency in a metro; inherits the parent Region for many services.
- **Wavelength:** AWS infrastructure inside carrier networks for ultra-low-latency 5G/edge use cases.
- **Outposts:** racks/servers installed on-premises, managed by AWS, connected to a parent Region; for data residency, low latency, or local processing.
- Use case: CloudFront for global static delivery; Local Zone for a Mumbai latency-sensitive trading UI; Outpost for a factory-floor app that must stay on-prem.

**Edge Cases & Gotchas**
- Local Zones have limited instance types and per-service availability; not every service works there.
- Outposts still need reliable connectivity to the parent Region for control plane operations; plan for disconnected scenarios.
- CloudFront is a CDN — it does not replace application-level global load balancing (that is Global Accelerator).
- Edge services do not fix a slow origin or a non-replicated database.

**Interview Questions**
- **Basic — What is an edge location?** → A globally distributed point of presence used by CloudFront/Route 53/Global Accelerator/WAF to serve and protect traffic close to users.
- **Medium — CloudFront vs Global Accelerator vs Local Zone?** → CloudFront caches HTTP(S) content at the edge; Global Accelerator optimises TCP/UDP paths to regional endpoints using anycast IPs; Local Zones place compute capacity near a metro.
- **Hard/Scenario — A trading app needs <10 ms latency for Mumbai users and data must stay in India.** → Design in `ap-south-1` with a Local Zone in the relevant metro if the service is supported; keep data in-Region; verify service support in Local Zones and the DR path.

## 1.5 AWS Shared Responsibility Model ★★★

**Definition:** The Shared Responsibility Model divides security duties: AWS is responsible for security **of** the cloud (physical, infrastructure, managed service layers), the customer for security **in** the cloud (data, identities, configuration, guest OS, application).

**Important Points**

| Responsibility | AWS | Customer |
| --- | --- | --- |
| Physical facilities, hardware, hypervisor | ✔ | — |
| Managed service engine patching (RDS engine, **managed** Lambda runtimes) | ✔ | — |
| Lambda **container images / custom runtimes / dependencies** | — | ✔ |
| EC2 guest OS, middleware, app patching | — | ✔ |
| IAM users/roles/policies, MFA | — | ✔ |
| Data classification, encryption choices, key policies | ✔ (tools) | ✔ (decisions) |
| Security group/NACL/bucket policy configuration | — | ✔ |
| Network traffic protection (TLS, encryption in transit) | ✔ (capability) | ✔ (configuration) |
| Compliance validation of *your workload* | — | ✔ |

- Responsibility shifts by model: IaaS (EC2), PaaS (RDS/Lambda), SaaS (WorkMail/Chime).
- Encryption: AWS provides the mechanism; the customer chooses whether to enable it, which key, and who can use the key.
- **Shared controls** exist (patch management, configuration management, awareness): AWS patches infrastructure, customer patches guest/app.
- **Lambda runtime patching is not universal.** For AWS-managed runtimes (Python, Node.js, Java, .NET, Go, Ruby) AWS publishes and patches runtime updates, but **you** own the runtime version you pin, its deprecation deadlines, your libraries/layers and any container image base. For container-image functions and custom runtimes, the base image and all patching are yours. Say "depends on runtime type and configuration" — a blanket "AWS patches Lambda" is imprecise.

**Edge Cases & Gotchas**
- A public S3 bucket from a bad bucket policy is a **customer** issue — do not blame AWS in an interview.
- "Managed" does not mean "secure by default" (RDS still needs private subnets, SG rules, credential rotation).
- AWS-managed encryption keys are convenient but limit cross-account/control flexibility; compliance often demands CMKs.
- Confusing *logging enabled by AWS* with *log review by customer* is a common audit finding.

**Interview Questions**
- **Basic — Security of the cloud vs in the cloud?** → AWS secures infrastructure it operates; the customer secures workloads, identity, configurations and data.
- **Medium — Who patches what for EC2, RDS and Lambda?** → EC2: customer patches guest OS, middleware and app. RDS: AWS patches the engine and underlying OS; the customer owns configuration, parameter groups, credentials, network exposure and major-version upgrade decisions. Lambda: for **AWS-managed runtimes** AWS provides patched runtime versions, but the customer owns runtime version pinning/deprecation deadlines, dependencies, layers and configuration; for **container images and custom runtimes** the customer owns the base image and patching entirely.
- **Hard/Scenario — A production S3 bucket is public and leaks data. Who is responsible, and what do you do first?** → Customer configuration responsibility. First: containment (apply Block Public Access, remove the offending policy/ACL, rotate exposed credentials). Then: CloudTrail + S3 server access logs to scope access, notify per incident process, add SCP/Config rules/policy guardrails, and enable Access Analyzer.

## 1.6 AWS Well-Architected Framework ★★★

**Definition:** A set of architectural best practices across six pillars used to evaluate and improve cloud workloads systematically.

**Important Points**
- **Six pillars:** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.
- Each pillar has design principles and questions in the Well-Architected Tool; **lenses** (Serverless, SaaS, IoT, Financial Services, etc.) tailor the questions.
- **Reliability** covers foundations, workload architecture, change management, failure management (backup, DR, chaos).
- **Operational Excellence** covers runbooks, IaC, small reversible changes, anticipating failure, learning from events.
- Reviews produce **high-risk issues (HRIs)** and a remediation plan; they are not audits — they are conversations.
- Use case: pre-launch review of a new platform; quarterly review of a production workload; due diligence for migrations.

**Edge Cases & Gotchas**
- "Doing a WA review" without fixing HRIs is theatre; interviewers probe for outcomes.
- The framework is **vendor-agnostic guidance**, not a checklist you can "pass".
- Cost Optimization is not "spend less" — it is "deliver the same business value for less", including not paying for idle resources.
- Sustainability is new and rarely deep-dived at 4 yrs, but knowing the pillar exists matters.

**Interview Questions**
- **Basic — Name the pillars.** → Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.
- **Medium — How would you run a Well-Architected review?** → Identify workload and owners, gather architecture and metrics, run the WA Tool with pillar questions, agree on HRIs, assign owners and dates, track remediation, re-review after major change.
- **Hard/Scenario — A team wants to skip the review "because the go-live is next week".** → Do a **targeted** review of the highest-risk areas (security exposure, backup/DR, single points of failure, quotas, alarms). Document accepted risks. Ship with guardrails, and schedule a full review after launch.

## 1.7 AWS Organizations, SCPs, Control Tower & Multi-Account ★★★

**Definition:** AWS Organizations centrally manages multiple AWS accounts with consolidated billing and policy guardrails; Control Tower automates a secure multi-account landing zone.

**Important Points**
- Structure: **Root → Organizational Units (OUs) → accounts**.
- **Consolidated billing:** one payer, volume discounts aggregated, one place for cost visibility (CUR, Cost Explorer).
- **Service Control Policies (SCPs):** JSON guardrails that define the **maximum** permissions for accounts in an OU. SCPs **filter**, they never grant. They do not apply to the management account or to service-linked roles.
- Common SCPs: deny regions outside approved list, deny leaving the organization, deny disabling CloudTrail/GuardDuty, deny root user actions, require IMDSv2, deny public S3 ACLs, protect security services.
- **RAM (Resource Access Manager):** share subnets, TGW, resolver rules, license configs across accounts.
- **Control Tower:** baseline landing zone with OUs, guardrails (preventive via SCPs, detective via Config), Account Factory (Service Catalog), dashboard, and drift detection.
- Typical OU design: `Security` (log archive, audit), `Infrastructure` (network, shared services), `Workloads/Prod`, `Workloads/NonProd`, `Sandbox`, `Suspended`.
- Why multi-account: blast-radius isolation, clean billing, separate quotas, environment segregation, simpler IAM boundaries, regulatory separation.

**Edge Cases & Gotchas**
- SCP changes **can take time to propagate**; do not assume instant effect.
- SCPs don't affect the management account's own restrictions the same way — do not run workloads in the management account.
- A `Deny *` SCP can lock out your own operators (including the ability to detach it) — test on a sandbox OU first and keep a break-glass path.
- Guardrails consume service quotas (Config rules, CloudTrail trails) and cost money.
- Centralized logging account needs cross-account log delivery permissions and bucket policies — a common failure point.
- **Cross-account access** is not automatic; you need role trust policies + `sts:AssumeRole` permission on the calling side.

**Interview Questions**
- **Basic — What is an SCP?** → An Organizations policy that sets the maximum available permissions for member accounts; it restricts but cannot grant.
- **Medium — Why use multiple AWS accounts instead of multiple VPCs?** → Stronger isolation (blast radius, IAM, quotas, billing, compliance), independent guardrails, clearer ownership. VPCs isolate networks, not permissions or quotas.
- **Hard/Scenario — Finance wants one bill and Security wants isolation. Design the account structure.** → Organizations with consolidated billing for one invoice, OUs by function/environment, dedicated security/log-archive/shared-network accounts, SCP guardrails, Control Tower for baseline, cost allocation via tags and CUR/ABP, and cross-account roles for access.

## 1.8 Migration Strategies — the 7 Rs ★★

**Definition:** Frameworks describing how existing workloads are moved/transformed to AWS: Rehost, Replatform, Repurchase, Refactor, Retire, Retain, Relocate.

**Important Points**

| Strategy | Change level | Example | Notes |
| --- | --- | --- | --- |
| Rehost (lift & shift) | Minimal | VMware VM → EC2 via AWS MGN (Application Migration Service) | Fastest migration, no modernisation |
| Replatform (lift, tinker, shift) | Moderate | Self-managed MySQL → RDS/Aurora | Managed benefits, small code/config change |
| Repurchase (drop & shop) | Replace | Self-hosted CRM → SaaS | Licence and integration work |
| Refactor / re-architect | High | Monolith → microservices on ECS/Lambda | Highest benefit, highest risk/cost |
| Retire | Remove | Unused app | Free win — audit first |
| Retain | No move | Mainframe/latency-critical | Revisit later |
| Relocate | Hypervisor-level | VMware Cloud on AWS | Fast, large-scale, minimal change |

- Tools: **AWS MGN** (server rehost), **AWS DMS + SCT** (database migration, schema conversion, CDC for near-zero downtime cutover), **DataSync** (file/NFS/SMB transfer), **Snowball** (large offline data), **Migration Hub** (tracking).
- Migrations run in waves by dependency and business priority; you build a **migration factory** (repeatable landing zone + runbooks).

**Edge Cases & Gotchas**
- Lift-and-shift carries over technical debt and often *increases* cost (no right-sizing, no elasticity design).
- DMS CDC requires attention to replication lag, LOB handling, DDL changes and cutover sequencing.
- Hard-coded IPs, hostnames, licence servers, AD dependencies and legacy auth break migrations.
- Migration cutovers need a tested rollback plan and a freeze window.
- Rehosting without right-sizing wastes months of savings; measure utilisation before choosing instance types.

**Interview Questions**
- **Basic — What is lift-and-shift?** → Moving an application with minimal changes (e.g., MGN to EC2).
- **Medium — Replatform vs refactor?** → Replatform adopts a managed service with limited change (MySQL → RDS); refactor redesigns the application (monolith → serverless/microservices).
- **Hard/Scenario — A legacy Java app with an on-prem MySQL must move in 6 weeks with minimal downtime.** → Rehost the app with MGN to EC2 (or containerise later), replatform the DB with DMS (full load + CDC), test in a staging VPC with identical SG/DNS, cut over in a low-traffic window with a rollback to on-prem, then optimise (right-size, RDS Multi-AZ) after stabilisation.

## 1.9 IP Subnetting & AWS Reserved IP Addresses ★★★

**Definition:** CIDR notation divides an address space into subnets; AWS VPC subnets use CIDR blocks and reserve five IPv4 addresses per subnet.

**Important Points**
- Usable IPv4 = 2^(32 − prefix) − 5 (AWS VPC subnets).
- VPC IPv4 block: /16 (65,536) down to /28; a subnet: /16 to /28. Five addresses are reserved:
  - `.0` network address
  - `.1` VPC router (default gateway)
  - `.2` DNS (Route 53 Resolver)
  - `.3` future use
  - last address of the subnet — reserved by AWS (VPCs do not support broadcast, so nothing can use it)
- Example `/24`: 256 total → **251 usable**.
- Example `/28`: 16 total → **11 usable**.
- Subnet CIDRs in a VPC must not overlap; peering/TGW/VPN need non-overlapping ranges end-to-end.
- Plan for growth: leave gaps between AZ blocks and environment blocks; reserve /16s per environment/Region in an IPAM plan.
- **AWS VPC IPAM** helps plan and allocate non-overlapping pools across accounts/Regions.
- IPv6: VPC gets a /56, subnets a /64; IPv6 addresses are global but private by routing; no NAT for IPv6 (egress-only IGW for outbound-only).

**Typical /16 plan**

```
10.20.0.0/16  prod-ap-south-1
 ├── 10.20.0.0/20    AZ-a  public
 ├── 10.20.16.0/20   AZ-a  private-app
 ├── 10.20.32.0/20   AZ-a  private-db
 ├── 10.20.48.0/20   AZ-b  public     (+16 each block)
 └── ...             reserve half the /16 for growth
```

**Edge Cases & Gotchas**
- `/28` looks fine until you add a NAT Gateway, ALB ENIs, EKS pods and endpoints — 11 usable addresses disappear fast.
- EKS with the VPC CNI assigns **pod IPs from subnets**; large pod counts need large subnets or prefix delegation/CNI custom networking.
- Cross-account VPCs often accidentally pick the same RFC1918 ranges and can never be peered.
- The `.2` address is not a per-subnet DNS server VM; it is the resolver endpoint.
- No broadcast/multicast in VPCs (multicast is a separate feature).
- Overlapping CIDRs are the #1 reason a TGW migration stalls — audit before you build.

**Interview Questions**
- **Basic — Usable IPs in an AWS /24?** → 251.
- **Medium — Why five reserved addresses?** → Network address, VPC router, DNS resolver (`.2`), `.3` held for future use, and the final address of the subnet, which AWS reserves because VPCs do not support broadcast.
- **Hard/Scenario — EKS nodes have CPU free but pods won't schedule.** → Suspect subnet IP exhaustion / ENI limits: check available IPs per subnet (`aws ec2 describe-subnets`), CNI logs, `kubectl describe pod` events, node `max-pods`, and consider prefix delegation, secondary CIDR/custom networking, or larger subnets.

## 1.10 Quotas, Service Limits & Support Plans ★★

**Definition:** AWS enforces service quotas (soft limits you can raise, hard limits you cannot) and offers tiered support plans.

**Important Points**
- Quotas are per Region/account for most services; some are global (e.g., VPCs per Region is regional, IAM entities have their own limits).
- Common ones to know conceptually: VPCs per Region, subnets per VPC, security groups and rules, EIPs, NAT gateways, ALB/NLB per Region, EC2 vCPUs per instance family, RDS instances, Lambda concurrency (default 1,000), API rate limits, TGW attachments, S3 request rates per prefix.
- Raise via **Service Quotas console** or a support case; some are auto-approved.
- **Support plans:** Basic (billing/account only), Developer (business hours, 1 primary contact), Business (24×7, production down guidance, full Trusted Advisor checks, TAM pool), Enterprise On-Ramp / Enterprise (TAM, faster SLAs, Well-Architected reviews, incident management).
- **Trusted Advisor** checks: cost, security, fault tolerance, performance, service limits (full checks need Business+).
- **AWS Health Dashboard** / EventBridge health events for planned changes and incidents.

**Edge Cases & Gotchas**
- Quota exhaustion is a classic production failure: autoscaling silently stuck, Lambda throttling at 1,000 concurrency, EIP limit hit during DR.
- Account-level quotas are not shared across accounts — a multi-account design has per-account ceilings.
- Throttling from APIs requires **exponential backoff with jitter** (AWS SDKs support retries, but tune them).
- Raising quotas takes time — pre-raise for launch and DR Regions.
- Support plan level determines how fast you get help during an incident; interviewers like candidates who mention this.
- **Treat every number and every support-plan description in these notes as "verify before quoting".** Default quotas, response-time targets and plan inclusions change; the authoritative source is the Service Quotas console, the AWS Support plan page and current pricing documentation. In an interview, say "the default is around X — I'd confirm it in Service Quotas" rather than asserting a stale figure.

**Interview Questions**
- **Basic — Difference between a soft and hard limit?** → Soft quotas can be increased via Service Quotas/support; hard limits are fixed by architecture and cannot be raised.
- **Medium — How do you prepare for a big launch from a quotas perspective?** → Inventory required quotas per service/Region, pre-request increases (including DR Region), load-test to detect throttling, add CloudWatch alarms on usage, and document fallback behaviour.
- **Hard/Scenario — Auto Scaling isn't launching instances during a traffic spike and there are no obvious errors.** → Check ASG activity history for quota/capacity errors, EC2 vCPU quotas, subnet IP availability, launch template errors, IAM/PassRole, and AZ capacity. Also verify max capacity and suspended processes.

---

# PART 2 — NETWORKING

## 2.1 VPC Fundamentals & Design ★★★

**Definition:** A Virtual Private Cloud is a logically isolated virtual network in a Region, with its own IP ranges, subnets, route tables, gateways and security controls.

**Important Points**
- Components: CIDR block(s), subnets (one AZ each), route tables, internet gateway (IGW), NAT gateway, egress-only IGW (IPv6), VPC endpoints, security groups, NACLs, DHCP option sets, flow logs.
- **Public subnet** = subnet whose route table has `0.0.0.0/0 → IGW`. **Private subnet** = no direct IGW route, egress via NAT/endpoints.
- Route tables: most specific (longest prefix) route wins; local route always exists for the VPC CIDR.
- A subnet can be associated with only one route table; multiple subnets can share one.
- Default VPC: auto-created, all subnets public — not appropriate for production.
- Peering attachment and TGW attachments are not "gateways" in route tables in the same way — routes point at the attachment.
- Design pattern: 3 tiers × 3 AZs, NAT per AZ, endpoints for S3/DynamoDB (gateway) and interface endpoints for other services, centralised egress in a shared-services VPC for larger estates.
- **Secondary CIDR blocks:** a VPC can have additional IPv4 CIDR associations (subject to limits). This is the standard fix for IP exhaustion and the enabler for **EKS custom networking** (pods in a dedicated secondary range). Secondary CIDRs cannot overlap existing VPC/peered/on-prem ranges; routes must cover them, and **you cannot remove a secondary CIDR while resources still use it**.
- **IPv6 / dual-stack:** assign a /56 IPv6 block to the VPC and /64s to subnets; addresses are globally routable but reachable only if the route table and SGs allow it. **Egress-only Internet Gateway** provides outbound-only IPv6 (there is no NAT for IPv6). IPv6-only subnets suit large EKS pod/IP demands; dual-stack applications must be tested for libraries that still assume IPv4.
- **VPC sharing (AWS RAM):** share subnets from a **owner** account to participant accounts within an Organization. Participants launch resources into shared subnets but cannot modify them; security groups can be shared so participants reference central SGs. Great for centralised network teams; watch quotas (participants cannot see the VPC's other resources) and change control.
- Use case: Public ALB in public subnets, app in private subnets, RDS in isolated DB subnets with no internet route.

**Edge Cases & Gotchas**
- One NAT Gateway shared by 3 AZs saves money but creates cross-AZ cost, a cross-AZ dependency, and an AZ failure blast radius.
- Deleting an IGW or route breaks the public subnet instantly — guard with change control.
- Security group referencing across VPCs requires peering/TGW and works only for SG-referencing rules in supported paths.
- CIDR overlap blocks peering/TGW/VPN entirely — no NAT trick fixes it (you need PrivateLink or a proxy).
- Subnet-level NACLs plus SG rules plus OS firewalls: three layers where a typo can silently drop traffic.
- VPC flow logs do not capture packet payloads or all traffic types (e.g., some instance metadata traffic); they are not real-time.
- Secondary CIDR mistakes are hard to unwind: overlapping ranges, missing routes and EKS ENIConfig left pointing at the wrong subnet cause silent blackholes.
- IPv6 changes the security model: no NAT, no egress-only protection unless you use an egress-only IGW, and SGs/NACLs must actually have IPv6 rules (an IPv4-only rule set silently drops IPv6).
- VPC sharing moves control away from the workload team — a participant cannot add a CIDR, change a route table or delete a subnet, so escalations go through the network owner.

**Interview Questions**
- **Basic — What makes a subnet public?** → Its associated route table has a route to an Internet Gateway, plus the resource needs a public IP and permissive SG/NACL.
- **Medium — Design a VPC for a 3-tier app with 3 AZs.** → /16 VPC; per AZ: public /24 (ALB, NAT), private-app /20, private-data /20; IGW, one NAT per AZ, S3 gateway endpoint, interface endpoints for secrets/monitoring, SGs by tier reference, NACLs default-allow, flow logs to S3/CloudWatch.
- **Hard/Scenario — EC2 in a private subnet cannot reach the internet.** → Check: route table has `0.0.0.0/0 → NAT GW`; NAT gateway is in a public subnet with an IGW route and an EIP; SG outbound allows traffic; NACLs allow ephemeral return traffic; subnet has no conflicting more-specific route; DNS resolution works; instance has no public IP requirement for NAT. Then confirm from inside with `curl -v` and `traceroute`.

## 2.2 Internet Gateway, NAT Gateway & NAT Instance ★★★

**Definition:** An IGW enables bidirectional internet connectivity for resources with public IPv4 addresses; a NAT Gateway performs source NAT so private-subnet resources can initiate outbound internet connections.

**Important Points**
- IGW: horizontally scaled, managed, highly available **per AZ view but logically per VPC**; no bandwidth limit to manage; requires public IP/EIP on the instance.
- **NAT Gateway — public:** associated with an Elastic IP (or EIP pool) in a public subnet; provides internet egress. **NAT Gateway — private:** no public IP; used to translate private addresses for **VPC-to-VPC, VPC-to-on-prem and overlapping-CIDR** destinations that would otherwise require a redesign. Choose the type by destination, not by habit.
- **Zonal vs regional deployment:** the classic NAT Gateway is **zonal** — one per AZ, with the subnet's route table pointing at that AZ's gateway. AWS has introduced region-level/expanded availability behaviour for NAT Gateway in some Regions (a gateway can be associated with subnets across AZs and remain available if an AZ fails) — **verify current support and behaviour for your Region** rather than assuming single-AZ failure. The safe interview answer: "classically zonal — deploy one per AZ for AZ independence; newer regional behaviour exists and should be verified before relying on it."
- NAT Gateway supports TCP/UDP/ICMP, not inbound initiated connections.
- NAT instance: an EC2 doing NAT — cheaper at tiny scale, but you own HA, scaling, patching, and it needs `source/destination check` disabled.
- **Connection tracking and port exhaustion:** each public IP provides a finite pool of simultaneous connections (roughly 64,000 ports per destination endpoint, per protocol). Thousands of short-lived connections to one external endpoint — health checks, API polling, log shipping, high-churn microservices — can exhaust the pool. Symptoms are intermittent `connection timeout`/`cannot assign requested address` while the gateway looks "healthy". Fixes: fewer public IPs per destination via connection pooling/keep-alive, a public IP prefix or more EIPs, spread destinations, or an NLB/PrivateLink path for AWS services.
- **Metrics that matter:** `ActiveConnectionCount`, `ConnectionAttemptCount`, `ConnectionEstablishedCount`, `PacketsDropCount`, `ErrorPortAllocation` (SNAT port allocation failures), `IdleTimeoutCount`, plus `BytesOutToDestination` for cost. Alarm on `ErrorPortAllocation` — it is the precise signal for port exhaustion.
- **NAT Gateway can't be used for VPC-to-VPC or on-prem traffic** with private IPs unless it is a **Private NAT Gateway** in a supported design — do not try to use it as a router.
- Use S3/DynamoDB **gateway endpoints** to avoid paying NAT data-processing charges for those workloads.
- VPC endpoints + PrivateLink replace NAT for most AWS service access.

**Edge Cases & Gotchas**
- NAT Gateway data-processing ($/GB) is a top-5 surprise AWS bill item, especially with ECR pulls from private subnets.
- One NAT per AZ is best practice; cross-AZ NAT = cost + AZ coupling.
- A NAT Gateway in a subnet whose route table loses its IGW route breaks all egress in dependent subnets.
- No security groups on NAT Gateway; you control traffic with SGs/NACLs on the instances and endpoint policies.
- NAT Gateway does not "preserve" client IP — the target sees the NAT EIP.
- Private NAT Gateway exists for overlapping-CIDR/on-prem egress scenarios (verify feature and Region support).
- A NAT Gateway cannot be resized — add EIPs (up to the per-gateway limit) or add gateways. Throughput scales with gateway capacity, but a single gateway can still be a bottleneck for extreme workloads.
- `ErrorPortAllocation` rising is the cleanest evidence of SNAT exhaustion; capture it before adding IPs blindly.

**Interview Questions**
- **Basic — IGW vs NAT Gateway?** → IGW allows inbound and outbound connectivity for public resources; NAT allows outbound-only internet access for private resources using an EIP.
- **Medium — Why put a NAT Gateway per AZ?** → AZ independence (no cross-AZ dependency or data charges), availability during an AZ failure, and simpler troubleshooting.
- **Hard/Scenario — ECR image pulls are slow and the NAT bill is huge.** → Add **interface VPC endpoints** for ECR API/DKR, S3 gateway endpoint (layers live in S3), CloudWatch Logs, and Secrets Manager; enable image caching on nodes; consider registry mirrors; verify SG/NACL rules on endpoint ENIs and endpoint policies.

## 2.3 VPC Endpoints & AWS PrivateLink ★★★

**Definition:** VPC endpoints let private-subnet resources reach supported AWS services (and PrivateLink services) without traversing the internet or NAT.

**Important Points**
- **Gateway endpoints** (free): S3 and DynamoDB only. Added to route tables; no SG, no ENI. Endpoint policies apply. Do **not** support access from on-prem or other VPCs directly.
- **Interface endpoints** (PrivateLink, billed hourly + per GB): an ENI with a private IP in your subnet; supports SGs; enables private DNS; works from on-prem/peered networks when DNS + routing are correct.
- **Gateway Load Balancer endpoints** for third-party appliances.
- **Endpoint policies** restrict which resources/actions the endpoint can be used for (defence in depth vs a compromised instance).
- **PrivateLink** exposes *your* service to other VPCs/accounts via Network Load Balancer + endpoint service, without peering or overlapping-CIDR problems.
- Service names: `com.amazonaws.ap-south-1.s3`, `...execute-api`, `...ecr.dkr`, `...secretsmanager`.
- Use case: fully private EKS with no NAT: interface endpoints for ECR, S3 gateway, logs, STS, EC2, and Secrets Manager.

**Edge Cases & Gotchas**
- **Private DNS** on an interface endpoint changes resolution for the whole VPC (for that service) — by design, but surprising.
- Gateway endpoints cannot be used from on-prem; hybrid access requires interface endpoints, TGW + PrivateLink, or a proxy.
- Endpoint ENIs consume subnet IPs and have per-AZ hourly costs.
- Endpoint policies with `Resource: "*"` are common and weaken the control.
- Some services have regional endpoint differences and not all services support every endpoint type.
- CloudTrail data events for endpoint usage may require extra configuration; flow logs on endpoint ENIs are useful for troubleshooting.
- **Endpoint DNS troubleshooting (the #1 private-endpoint failure):**
  - `dig +short s3.ap-south-1.amazonaws.com` / `getent hosts <service>` should return the **private** ENI IPs when private DNS is enabled.
  - If it returns public IPs: private DNS not enabled, or the VPC has `enableDnsSupport`/`enableDnsHostnames` disabled, or a custom DHCP option set points DNS somewhere that doesn't forward to the Amazon-provided resolver (`169.254.169.253`/VPC+2).
  - Check the endpoint's state (`available`), its subnets/AZs, SG ingress on 443 **from the client SG**, and NACLs.
  - On-prem/hybrid clients need Route 53 Resolver inbound endpoints plus forwarding — interface-endpoint private DNS only affects VPCs with the setting enabled.
- **Endpoint policy vs IAM policy** — two independent gates, both must allow:
  - **IAM policy** answers "may this principal call this API?"
  - **Endpoint policy** answers "may this endpoint be used for this resource/action?" Even a full-admin IAM role is denied if the endpoint policy excludes the bucket/queue/table. A common hardening pattern is an endpoint policy restricted to specific resource ARNs plus `aws:PrincipalOrgID`.
- **Hybrid access:** gateway endpoints are unreachable from on-prem; interface endpoints are reachable over VPN/DX once DNS resolves privately and routes to the endpoint ENIs exist.

**Interview Questions**
- **Basic — Gateway vs interface endpoint?** → Gateway endpoints (S3/DynamoDB) are route-table targets and free; interface endpoints are ENIs with private IPs, support SGs, cost hourly and per GB, and enable PrivateLink.
- **Medium — When would you use PrivateLink instead of VPC peering?** → When you need one-way service access at scale, have overlapping CIDRs, want to avoid managing routes/firewalls between many VPCs, or need to expose a SaaS service to customers.
- **Hard/Scenario — A Lambda in a VPC must read S3 without a NAT Gateway.** → Add an S3 **gateway endpoint** to the Lambda subnet's route table (cheapest), keep the Lambda role policy least-privilege, and verify the endpoint policy allows the bucket. If the Lambda must also call Secrets Manager/CloudWatch, add interface endpoints.

## 2.4 VPC Peering ★★★

**Definition:** A private one-to-one network connection between two VPCs that lets resources communicate using private IPs.

**Important Points**
- Same or different Region, same or different account, same or different Organizations (with RAM/acceptance).
- Requires routes in **both** VPCs; no transitive routing.
- CIDRs must not overlap.
- Works across AZs; traffic stays on the AWS backbone but cross-AZ/cross-Region charges may apply.
- Peering does not provide IGW/NAT sharing; you cannot route through a peer to reach the internet.
- Security groups/NACLs still govern traffic; SG referencing across peers is supported.
- DNS: enable "DNS resolution" for private hosted zone sharing across peers where required.
- Use case: app VPC ↔ shared DB VPC; two-team VPCs needing private connectivity.

**Edge Cases & Gotchas**
- The classic: A↔B and B↔C does **not** give A↔C.
- Full mesh grows as n(n−1)/2 — 10 VPCs = 45 peerings; 50 VPCs = 1,225. TGW time.
- Cross-Region peering still requires correct routes and SG rules in both Regions; latency is real.
- Route table limits (routes per table) can be reached in large meshes.
- Deleting a peering leaves dangling routes that blackhole traffic.
- DNS resolution is not automatically enabled — private hostnames can still fail.
- Peering has no route-table segmentation, security-admin or central inspection — every pair is a flat trust relationship once NSGs allow it.
- Peering connections cannot be tagged for cost allocation of the data-transfer charges in the same way as other resources; cross-Region data transfer is billed to the requesting side's account.

**Interview Questions**
- **Basic — What is VPC peering?** → A private, one-to-one connection between two VPCs using private IPs.
- **Medium — Is peering transitive?** → No. Each pair needs its own peering and routes (or a transit solution).
- **Hard/Scenario — A↔B and B↔C are peered, but A cannot reach C. Options?** → VPC peering is **non-transitive and cannot be made transitive by inserting an appliance**: a firewall/NVA in B does not turn peering into a transit network, and "just add routes" does not create reachability. Supported options are (1) a **direct A–C peering**, or (2) a **routed architecture** — Transit Gateway (or a Cloud WAN/Virtual WAN equivalent) — with B (or a dedicated inspection VPC) attached as a routing/inspection hop. State clearly that TGW is the correct answer once the mesh grows; do not imply peering plus an NVA equals transit.

## 2.5 AWS Transit Gateway ★★★

**Definition:** A regional hub-and-spoke router that connects many VPCs, VPNs, Direct Connect gateways and peered TGWs through a central routing layer.

**Important Points**
- Attachments: VPC, VPN, Direct Connect gateway, TGW peering, Connect.
- **TGW route tables** (one or more per TGW) with association + propagation; segment routing by OU/environment is the standard design (prod, non-prod, shared, inspection).
- **Segmentation design:** separate TGW route tables per segment (`prod`, `non-prod`, `shared-services`, `inspection`, `hybrid`) with explicit association + propagation — never one default route table for everything. A segment's route table determines which attachments can reach which prefixes.
- **Blackhole routes** enable deliberate traffic dropping (e.g., quarantine VPC, or blocking a prefix during an incident). Monitored via the `PacketDropCountBlackhole` metric.
- **Appliance mode** keeps a flow pinned to the same AZ's appliance ENI so stateful inspection sees both directions — required for firewalls/NVAs, at a cost of AZ affinity.
- **TGW Flow Logs** (where supported) record attachment-level flow metadata; together with VPC flow logs they distinguish "never reached TGW" from "reached TGW and was dropped" — the fastest way to localise a blackhole.
- TGW peering connects Regions (not transitive by default — you must configure routes and, for multi-hop, attach to a central TGW).
- Costs: hourly per attachment + per GB data processed; cross-AZ data charges.
- Use case: 20+ VPCs, shared services, hybrid via Direct Connect gateway, centralised inspection.

**Edge Cases & Gotchas**
- TGW route tables and VPC route tables are **two separate layers** — both must be right.
- Associations vs propagations confusion is the #1 exam/interview trap: *associate* a VPC attachment with a route table to say "this attachment uses this table"; *propagate* to advertise routes into a table.
- Overlapping CIDRs cannot be fixed by TGW.
- TGW does not inspect traffic — you need Network Firewall/GWLB/NVA in an inspection VPC.
- Attachment quotas and route limits per table matter at scale.
- Data processing charges can exceed the peering alternative for low-volume, stable topologies.
- Segmentation mistakes can expose prod to non-prod — use separate route tables per segment and explicit propagation.
- Attachment-level **route propagation does not imply reachability**: the destination VPC's own route table must point back at the TGW.
- Appliance mode does not fix an NVA that lacks IP forwarding or whose SG blocks return traffic.
- TGW route table limits (routes per table, attachments, associations) are reachable in mature estates — monitor and split segments before you hit them.

**Interview Questions**
- **Basic — What is Transit Gateway?** → A managed regional hub that connects VPCs and hybrid networks with centralized routing.
- **Medium — TGW vs VPC peering?** → Peering for a small number of simple 1:1 connections; TGW for many VPCs needing centralised routing, segmentation and hybrid connectivity.
- **Hard/Scenario — Two VPCs attached to the same TGW cannot communicate. Debug it.** → Check attachment state (`available`), TGW route table association for each attachment, propagation of each VPC CIDR into the peer's route table, VPC route table entries pointing to the TGW, overlapping CIDRs, SG/NACL rules, and whether appliance mode is needed. Then use VPC flow logs + TGW metrics (`BytesIn/Out`, `PacketDropCountBlackhole`).

## 2.6 Site-to-Site VPN & Direct Connect ★★★

**Definition:** Hybrid connectivity options: Site-to-Site VPN is an encrypted IPsec tunnel over the internet; Direct Connect (DX) is a dedicated private physical connection into AWS.

**Important Points**

| | Site-to-Site VPN | Direct Connect |
| --- | --- | --- |
| Path | Public internet, IPsec encrypted | Dedicated private circuit / partner-hosted connection |
| Bandwidth | Up to ~1.25 Gbps per tunnel (verify) | 50 Mbps–100 Gbps (dedicated/hosted), LAG for more |
| Latency/jitter | Variable | Predictable, consistent |
| Setup time | Minutes | Weeks–months (cross-connect, carrier) |
| Encryption | IPsec built-in | Not encrypted by default (MACsec or VPN over DX possible) |
| Cost | Low | Port hours + partner/cross-connect |
| Use case | Quick DR link, low/medium volume | Production hybrid, large data transfer, latency-sensitive |

- VPN: two tunnels per connection for redundancy; can terminate on a VGW (single VPC) or a **Transit Gateway** (many VPCs).
- DX: **virtual interfaces** — private VIF (VPC via VGW/DXGW), transit VIF (to TGW/DX gateway), public VIF (AWS public services). BGP peering, route filtering, and DX Gateway for multi-Region.
- **BGP path selection** is what actually decides DX vs VPN: prefer the path with the best **AS-path length**, then `local-preference`/MED as your edge devices apply them. Common patterns: AS-path prepending to make VPN a standby, longer prefixes advertised over DX only, and explicit `inbound`/`outbound` route filters on the VIF. Longest-prefix match in the VPC route table still wins over BGP preference — a /24 via VPN beats a /16 via DX for that /24.
- **BFD** (where the customer gateway/device supports it) gives sub-second failure detection on DX/VPN paths instead of waiting for BGP hold timers; verify both ends support it before claiming fast failover.
- **Tunnel health:** a VPN connection shows both tunnels `UP` while traffic still fails — check tunnel status metrics (`TunnelState`, `TunnelDataIn/Out`), IKE/IPsec proposal mismatch, pre-shared key mismatch, and whether the on-prem device's interesting-traffic ACLs cover the subnet.
- **Asymmetric routing** breaks stateful inspection and NAT: outbound via DX, return via VPN (or vice versa) gets dropped. Prove it with flow logs/traceroute on both directions and pin the path with BGP attributes, or use a single active path with a tested standby.
- **Failover testing** is the only proof: shut one tunnel/circuit or withdraw a BGP advertisement in a change window, confirm traffic shifts within the expected time, and measure the actual outage. Test both directions (AWS → on-prem and on-prem → AWS).
- **Resilience models:** DX plus internet VPN backup; dual DX on diverse paths/devices; dual-homed with two carriers; DX **SiteLink** for multi-site topologies; **Global Reach** to connect DX locations via AWS.
- Route preference: BGP attributes on the DX/VPN side and longest-prefix on the VPC side. Typically DX preferred over VPN by AS-path/prefix.
- Use case: 10 Gbps DX from Mumbai for production; VPN as backup; TGW as the hybrid hub.

**Edge Cases & Gotchas**
- A single DX connection is **not** highly available — carrier or location failure takes you down.
- VGW-based VPN has limits; many VPCs → TGW VPN attachments.
- Asymmetric routing across DX + VPN breaks stateful firewalls.
- DX does not encrypt traffic — compliance may require MACsec or VPN over DX.
- BGP misconfiguration (wrong ASN, missing route filters, no summary routes) shows up as "tunnel up, no traffic".
- MTU: DX 1500 (9001 jumbo with support), VPN ~1400 — fragmentation issues appear with large packets.
- On-prem DNS/AD resolution over hybrid links requires Route 53 Resolver endpoints and correct forwarding.
- MTU mismatches on VPN (~1400) vs DX (1500/9001) produce "works for small requests, hangs on large uploads" symptoms — check TCP MSS clamping and PMTUD.
- DX gateway associations and allowed prefixes must be correct for propagation; a VIF that is `up` can still advertise nothing useful.

**Interview Questions**
- **Basic — VPN vs Direct Connect?** → VPN is encrypted over the internet, quick to set up; DX is a dedicated private circuit with predictable performance and higher setup effort.
- **Medium — How do you make hybrid connectivity highly available?** → Redundant DX connections on diverse paths/devices + VPN backup, BGP with path preference, TGW for central termination, and tested failover. Document RTO/RPO and test regularly.
- **Hard/Scenario — After a DX cutover, traffic to AWS is slower and some flows drop.** → Check BGP: which routes being advertised/received, AS-path prepending, prefix lengths (longest match wins), DX vs VPN preference; verify VIF type and VLAN; check appliance mode/asymmetric routing through the firewall; confirm MTU and TCP MSS on both sides.

## 2.7 Security Groups vs Network ACLs ★★★

**Definition:** Security Groups are stateful virtual firewalls on ENIs; NACLs are stateless allow/deny lists applied at the subnet boundary.

**Important Points**

| Feature | Security Group | Network ACL |
| --- | --- | --- |
| Scope | ENI/resource | Subnet |
| Statefulness | Stateful (return traffic auto-allowed) | Stateless (must allow both directions) |
| Rule types | Allow only | Allow and deny |
| Evaluation | All rules aggregated | Numbered order, first match |
| Applies to | Inbound/outbound per ENI | Inbound/outbound per subnet |
| References | CIDR, SG, prefix list | CIDR only (plus numbered rules) |
| Default | Deny all inbound, allow all outbound | Default NACL allow all |

- SGs are the primary control; NACLs are a coarse subnet guardrail (often left default-allow).
- SG referencing (`sg-xxxx`) enables tier-to-tier rules without hardcoded CIDRs — the cleanest pattern.
- NACLs are useful for explicit deny of known-bad CIDRs and for isolating subnets at a coarse level.
- Ephemeral ports: client-side source ports usually 1024–65535 — NACL outbound must permit them.
- Use case: SG chain `alb-sg → app-sg` on 8080, `app-sg → db-sg` on 3306; default NACLs; explicit deny of a malicious CIDR at the subnet NACL.

**Edge Cases & Gotchas**
- A NACL allowing 443 inbound but denying outbound ephemeral ports = timeouts that look like app failures.
- SGs cannot explicitly deny — for deny you need NACL, Network Firewall, or WAF (L7).
- Default SG is permissive and shared; don't leave resources in it.
- Rule changes to SGs apply to new connections immediately but existing connections can persist.
- SG limits: rules per SG, SGs per ENI (verify); prefix lists help keep rules tidy.
- Changing an SG on a live cluster can silently cut health checks.

**Interview Questions**
- **Basic — Which is stateful?** → Security Groups.
- **Medium — How do you deny a specific IP?** → Not with SG allow rules — use a NACL deny rule, AWS Network Firewall, or WAF for HTTP(S).
- **Hard/Scenario — Clients time out on 443 even though the SG allows it.** → Verify NACL inbound 443 + outbound ephemeral; route tables and IGW/NAT path; the app is listening (`ss -lntp`); OS firewall (firewalld/ufw/nftables); target group health; ALB SG vs instance SG; return path; and finally packet capture (VPC Traffic Mirroring/Reachability Analyzer). **Reachability Analyzer** is the fastest tool here.

## 2.8 Application Load Balancer (ALB) ★★★

**Definition:** A managed Layer 7 load balancer that routes HTTP/HTTPS (and gRPC/WebSocket) traffic using host, path, header, method and query rules to target groups.

**Important Points**
- Listeners (port/protocol) → rules → target groups → targets (instance, IP, Lambda, ALB).
- Routing: host-based, path-based, weighted target groups (canary), redirect, fixed response, authentication (OIDC/Cognito).
- Features: HTTP/2, WebSocket, TLS termination with ACM, SNI, WAF integration, access logs (S3), sticky sessions, slow start, gRPC, mutual TLS (verify).
- Health checks per target group (path, port, interval, thresholds, matcher).
- Cross-zone load balancing **enabled by default**; nodes per AZ scale automatically.
- Idle timeout default 60s (adjustable), keep-alive to targets, deregistration delay (default 300s) for graceful drain.
- **TLS policies** are chosen per listener (e.g., `ELBSecurityPolicy-TLS13-1-2-2021-06` for TLS 1.2/1.3 only). Weak/legacy policies are an audit finding; pin a modern policy and test old clients explicitly.
- **Mutual TLS (mTLS):** supported on ALB with a trust store (ACM Private CA or imported CA bundle) — `verify` mode enforces client certs, `passthrough` forwards them for app-level validation. Choose verify for B2B APIs; passthrough when the backend needs the certificate identity.
- **Access logs** (S3, JSON, optional gzip) are essential for 5xx forensics — fields include `target_status_code`, `target_group_arn`, `request_processing_time`, `target_processing_time`, `error_reason`. Enable them on day one; they cost almost nothing relative to their diagnostic value.
- **Connection draining / deregistration delay** applies per target group; graceful shutdown in the app must be shorter than the delay or in-flight requests are cut.
- **Cost model — LCUs:** pay hourly + **Load Capacity Units** (new connections/sec, active connections/min, processed bytes, rule evaluations — whichever is highest). HTTPS adds TLS cost; rule count matters. A tiny app with 40 listener rules can cost more than the traffic implies.
- **Target health reason codes** in `describe-target-health` (`Target.ResponseCodeMismatch`, `Target.Timeout`, `Target.FailedHealthChecks`, `Target.NotInService`, `Elb.RegistrationInProgress`, `Target.InvalidState`) tell you *why*, not just *unhealthy* — always quote the reason in an interview answer.
- Use case: `/api/*` → API service, `/static/*` → another service, host-based routing for `app.example.com` vs `admin.example.com`.

**Edge Cases & Gotchas**
- **503** = no healthy targets / no registered targets / SG mismatch / wrong port / app not ready. **502** = target returned garbage/reset. **504** = target timed out (app slow, SG, or idle timeout mismatch).
- Health check path returning 200 on a static page while the app is broken — check deep health endpoints.
- ALB is regional; it cannot fail over across Regions (use Route 53/CloudFront/Global Accelerator).
- No static IPs (use NLB or Global Accelerator).
- HTTPS at ALB does not automatically encrypt ALB→target; configure HTTPS on the target group if needed.
- Too-low deregistration delay kills in-flight requests during deploys; too high slows deploys.
- ALB target SG must allow traffic **from the ALB SG**, not the client CIDR.
- Idle timeout shorter than the app's keep-alive produces sporadic 502/504s under load — align ALB idle timeout with backend keep-alive (backend keep-alive should generally be *longer*).
- Listener rule limits and rule evaluations affect LCU cost and latency; deep path routing belongs in the app or a gateway.
- mTLS failures surface as TLS handshake errors, not 4xx/5xx — check the trust store, CA chain and client certificate expiry.
- Access logs are not real-time (minutes of delay) — use CloudWatch metrics for alerting and logs for forensics.

**Interview Questions**
- **Basic — OSI layer?** → Layer 7.
- **Basic — What is a target group?** → A logical set of targets (instances, IPs, Lambda, another ALB) with its own health check and attributes that listener rules forward to.
- **Medium — How does path-based routing work?** → Listener rules evaluate in priority order; the first match forwards to the associated target group.
- **Medium — When are sticky sessions appropriate, and when are they a smell?** → Appropriate for legacy stateful apps that cannot externalise session state; a smell when they hide a scaling/session design problem, because they unbalance load and break during scale-in and AZ failure. Prefer externalised state (Redis/DynamoDB) and stateless targets.
- **Hard/Scenario — ALB returns intermittent 503s during deployments.** → Check target group health during rollout, registration/deregistration delay, readiness probe/grace period, app startup time, `UnHealthyHostCount` and `TargetResponseTime` metrics, and whether new instances pass health checks before old ones drain. Fix with slow start, proper deregistration delay, and rolling deployment with health-based gates.

## 2.9 Network Load Balancer (NLB) ★★★

**Definition:** A Layer 4 load balancer for TCP/UDP/TLS with extreme performance, static IPs per AZ and source-IP preservation.

**Important Points**
- Handles millions of connections per second with ultra-low latency (verify current numbers).
- Static IP per AZ; can attach Elastic IPs for internet-facing NLBs → good for partner allowlists.
- Preserves client source IP to targets (when targets are instances/IPs and not using proxy protocol v2 in some paths).
- TLS termination supported; also TCP pass-through.
- Cross-zone load balancing **off by default** (cost/distribution implications; enabling incurs cross-AZ charges).
- Health checks: TCP, HTTP, HTTPS.
- Can front an ALB as a target (static IP + L7 features), useful for IP-restricted requirements.
- Use case: high-throughput TCP service, MQTT broker, gaming, RADIUS, static-IP requirement for third parties.

**Edge Cases & Gotchas**
- No path/host routing — do not use NLB where you need HTTP-aware rules.
- Source IP preservation changes with target type (IP vs instance) and proxy protocol settings.
- Connection draining for TCP relies on deregistration delay; long-lived connections can outlive the target.
- Cross-zone disabled means uneven distribution if AZ capacities differ.
- Security groups on NLB are supported now, but the "security group on target" model is different from ALB; verify.
- TLS termination at NLB means certificates and SNI must be configured per listener.
- **Cost model — NLCUs:** hourly + Network Load Capacity Units (new flows/sec, active flows/min, processed bytes). TCP keep-alives reduce new-flow cost; chatty short-lived connections inflate it.
- **Target health reasons** are the same family as ALB; for `Tcp` health checks a `Connection refused` almost always means the app isn't listening on that port/IP family, not an SG problem if the SG allows it.
- Enabling cross-zone load balancing changes the data-transfer bill and improves distribution — decide explicitly and document it.

**Production Troubleshooting**
```bash
# Why is a target unhealthy? Ask for the reason code, not just the state
aws elbv2 describe-target-health --target-group-arn <tg-arn> \
  --query 'TargetHealthDescriptions[].[Target.Id,Target.Port,TargetHealth.State,TargetHealth.Reason,TargetHealth.Description]' --output table

# Is the NLB seeing unhealthy targets? (metric confirms scope: one target vs all)
aws cloudwatch get-metric-statistics --namespace AWS/NetworkELB \
  --metric-name UnHealthyHostCount --dimensions Name=LoadBalancer,Value=app/<nlb-name> \
  --start-time $(date -u -d'-1 hour' +%FT%TZ) --end-time $(date -u +%FT%TZ) \
  --period 60 --statistics Average
```
Expected/interpretation: `Target.FailedHealthChecks` or `Target.Timeout` with a specific IP means the probe path/port is wrong or the app is not listening — check `ss -lntp` on that host and the **target** SG. `Elb.RegistrationInProgress` means wait, not fix. All targets unhealthy at once points at a shared cause: SG on the NLB, subnet/NACL change, or a bad deployment.

**Interview Questions**
- **Basic — OSI layer?** → Layer 4.
- **Medium — When NLB over ALB?** → TCP/UDP, static IP requirement, extreme throughput/latency, or non-HTTP protocols.
- **Hard/Scenario — A partner requires fixed IPs and the app needs host-based routing. Design it.** → NLB with Elastic IPs in front, ALB as the NLB target group, ALB performs L7 routing. Alternatively Global Accelerator (static anycast IPs) in front of ALB.

## 2.10 Route 53 ★★★

**Definition:** AWS's managed DNS service: public and private hosted zones, domain registration, health checks and multiple routing policies.

**Important Points**
- Record types: A, AAAA, CNAME, MX, TXT, NS, SOA, CAA, **Alias** (A/AAAA to AWS resources: ALB, CloudFront, S3 website, NLB, API Gateway).
- **Alias vs CNAME:** alias is free to query, works at zone apex, resolves to AWS resource; CNAME cannot be used at apex and is billed.
- **Routing policies:** Simple, Weighted, Latency, Failover (primary/secondary), Geolocation, Geoproximity (+ bias), Multivalue answer.
- **Health checks:** endpoint (HTTP/HTTPS/TCP), calculated, CloudWatch alarm-based. Can evaluate `StringMatch`, status codes, latency.
- **Private hosted zones:** internal DNS for VPCs; associate with multiple VPCs; hybrid resolution via **Route 53 Resolver** inbound/outbound endpoints + forwarding rules.
- **DNSSEC** signing is supported for public hosted zones (verify current support/Regions) — it protects against spoofing but adds key-rotation and DS-record operational work.
- **Split-horizon DNS:** a public zone and a private zone with the **same name** give internal clients internal answers and external clients public answers. Powerful for internal-only endpoints, and dangerous when the private zone is not linked to a VPC — clients then silently get public IPs.
- **Route 53 Resolver endpoints (hybrid DNS):** **inbound** endpoints let on-premises resolvers query Route 53 private zones (via VPN/DX); **outbound** endpoints + **Resolver rules** forward specific domains from AWS to on-prem DNS. Rules can be shared across accounts with RAM. This is the standard hybrid DNS pattern and the fix for "private zone works in the VPC but not on-prem".
- **Route 53 Resolver DNS Firewall:** domain allow/deny lists applied to outbound DNS from VPCs and Resolver endpoints — blocks known-malicious domains and constrains DNS-based data exfiltration. It is separate from security groups and from Network Firewall domain rules.
- TTL vs alias: alias inherits the target's behaviour; failover speed depends on TTL and client caching.
- Use case: `api.example.com` alias to ALB; weighted 10/90 canary across two ALBs; failover to `ap-south-2`; private `db.internal` zone.

**Edge Cases & Gotchas**
- DNS failover is not instant — TTL, resolver caching and client caching determine actual failover time.
- Route 53 health checks can only reach public endpoints; for private resources use CloudWatch alarm-based health checks.
- A failover record flips DNS, but existing TCP connections continue to the old IP.
- Private hosted zone association is per VPC; forgetting a VPC causes "record not found" in that VPC.
- Overlapping private zones with the same name across accounts → resolver chooses based on association; ambiguity causes incidents.
- Registrar lock/transfer issues — keep domain contacts and MFA under control.
- Route 53 Resolver is the recursive resolver; **DNS Firewall** is a policy layer on top of it. Different products — do not use the names interchangeably.
- Split-horizon zones with the same name in two accounts cause ambiguous answers; the result depends on which VPC is associated.
- Outbound Resolver rules that match too broadly can blackhole all external DNS — test with `dig` and check rule ordering.
- Health checks that depend on a full page render (login, DB) cause failover on dependency blips; use a shallow readiness endpoint plus separate deep alarms.

**Interview Questions**
- **Basic — Why alias over CNAME?** → Works at the zone apex, no query charge, and resolves dynamically to AWS resource IPs.
- **Basic — What is the difference between a public and a private hosted zone?** → A public zone answers internet resolvers for a domain you own; a private zone answers only from associated VPCs and is used for internal names and split-horizon DNS.
- **Medium — How does a failover routing policy work?** → Primary and secondary records, each optionally health-checked; when the primary is unhealthy Route 53 answers with the secondary — subject to TTL, resolver/client caching and connection reuse. Pair it with application-level retry and a readiness-based health check.
- **Medium — How do you health-check a private resource that the internet cannot reach?** → Route 53 endpoint health checks require a publicly reachable endpoint, so for private targets use a **CloudWatch alarm-based health check** driven by a metric that reflects the resource's health.
- **Hard/Scenario — Multi-Region active-passive with 30-second RTO on DNS failover. Is that realistic?** → **DNS alone cannot promise 30 seconds.** Route 53 changes the *answer*, but resolvers and clients cache it (TTL), existing TCP/HTTP connections keep using the old IPs, and the standby Region must already have capacity, credentials, certificates, DNS records and replicated data. A 30-second RTO requires: a proxied/anycast entry point (Global Accelerator or CloudFront) rather than pure DNS, health checks that reflect real readiness, a **warm** secondary (pre-scaled compute, database that can be promoted within RPO), and tested application/data recovery — then measured in a drill. Say explicitly that RTO is dominated by data failover and application readiness, not by DNS.

## 2.11 CloudFront ★★★

**Definition:** AWS's global CDN: caches and serves HTTP(S) content from edge locations, with TLS, compression, WAF, signed URLs and origin shielding.

**Important Points**
- **Origins:** S3 (with OAC), ALB, EC2, API Gateway, custom origins; **origin groups** for failover.
- **Behaviours:** path-pattern based; cache policies, origin request policies, TTLs (min/default/max), compression, allowed methods, viewer protocol policy.
- **Security:** ACM certificate in `us-east-1` for CloudFront, WAF (scope CLOUDFRONT), **Origin Access Control (OAC)** (replaces legacy OAI), signed URLs/cookies for private content, geo-restriction, Shield Standard.
- **Cache-key design is the performance lever:** the cache key comes from the cache policy (query strings, headers, cookies) — **fewer components = higher hit rate**. Put auth in a header the origin validates but CloudFront does not cache on, allow-list and normalise query parameters, and never cache on `User-Agent`.
- **OAC (Origin Access Control):** signs CloudFront→S3 requests so the bucket stays private. OAI is legacy; use OAC, including for SSE-KMS buckets. For ALB/custom origins, restrict the origin SG to the CloudFront managed prefix list (or require a shared-secret header) so the origin isn't reachable directly.
- **Signed URLs vs signed cookies:** signed URLs for a single object (downloads, media); signed cookies for many objects (HLS segments, subscriber sites). Both use a trusted key group; short expiries limit blast radius.
- **Origin failover:** an **origin group** with primary + secondary and failover criteria (e.g., 500–504) keeps serving during an origin outage. Health checks must hit a real readiness path — a static 200 page defeats the purpose.
- **Cache invalidation** (`/*`) is billed per path; prefer versioned filenames.
- **Origin Shield** adds a caching layer to reduce origin load.
- **Lambda@Edge / CloudFront Functions** for lightweight request/response manipulation.
- Use case: static site on S3 + API on ALB with caching for GETs, global low-latency delivery.

**Edge Cases & Gotchas**
- Cache misses on API endpoints cause origin overload; use appropriate cache policies and TTLs.
- Cookies/headers in the cache key fragment the cache and reduce hit rate.
- CloudFront does not cache `POST` by default; do not expect API acceleration without architecture changes.
- Signed URLs expire; clock skew and long TTLs cause 403s.
- WAF is regional for ALB and global for CloudFront — attaching to the wrong scope leaves the origin exposed.
- Leaving the S3 origin publicly accessible bypasses CloudFront controls (OAC + Block Public Access).
- ACM certificates must be in `us-east-1` for CloudFront, regardless of workload Region.
- Origin failover does not copy data — a second origin in another Region only helps if the application and its data are actually available there.
- Header/behaviour issues are hard to debug from a warm cache: reproduce with a cache-busting query string and inspect the `x-cache` and `x-amz-cf-id` response headers.
- Geo-restriction and WAF are edge controls; direct-to-origin traffic bypasses both.

**Interview Questions**
- **Basic — What is CloudFront?** → A global CDN that caches content at edge locations and delivers it over AWS's network with TLS/WAF.
- **Medium — CloudFront vs Global Accelerator?** → CloudFront caches HTTP(S) content at the edge; Global Accelerator optimises TCP/UDP to regional endpoints using static anycast IPs and no caching.
- **Hard/Scenario — Static assets have a 20% cache hit rate and origin CPU is high.** → Inspect cache keys (cookies/headers/query strings), TTLs, compression, vary behaviour, and whether requests are unique per user. Normalise query strings, move auth out of cookies for static paths, add Origin Shield, and pre-warm/version assets.

## 2.12 AWS WAF & Shield ★★

**Definition:** AWS WAF is a Layer 7 web application firewall for CloudFront, ALB, API Gateway and AppSync; Shield provides DDoS protection (Standard automatic, Advanced paid).

**Important Points**
- Web ACLs contain rules with priorities; actions: Allow, Block, Count, CAPTCHA, Challenge.
- Rule types: AWS managed rule groups (Core, Known Bad Inputs, SQLi, IP reputation, Bot Control), custom rules, **rate-based rules**, geo match, IP sets, regex/string match, label-based logic.
- **Shield Standard** is automatic for all AWS customers (L3/L4 DDoS); **Shield Advanced** adds enhanced detection, DDoS Response Team, cost protection, and advanced reporting.
- WAF logging to CloudWatch Logs/S3/Firehose is essential for tuning.
- Rate-based rules protect against brute force and scraper bursts; thresholds must be tuned per endpoint.
- Use case: block OWASP-top-10 patterns, rate-limit `/login`, geo-block non-supported countries.

**Edge Cases & Gotchas**
- Managed rule groups block legitimate traffic — start in **Count** mode, observe, then Block.
- WAF inspects per request; encrypted payload inspection requires terminating TLS at the edge.
- Rate-based rules count per IP per window; NATed corporate traffic can trigger false positives.
- WAF adds latency (usually small) and cost per request/rule.
- Blocking at WAF doesn't protect the ALB from direct-to-IP attacks — restrict the origin to CloudFront IPs/SG or use private origins.
- Regional vs global scope mistakes are common.

**Interview Questions**
- **Basic — Shield Standard vs Advanced?** → Standard is free automatic L3/L4 protection; Advanced adds SRT access, cost protection, enhanced detection, and more.
- **Medium — How do you safely enable AWS managed WAF rules?** → Deploy in Count, analyse sampled requests/logs for a period, tune exclusions, then switch to Block with alarms.
- **Hard/Scenario — During a credential-stuffing attack, legitimate users are also getting blocked.** → Add scoped rate-based rules per login path, use Bot Control with targeted challenge/CAPTCHA instead of blanket blocks, allowlist known partners, monitor WAF logs, and layer application-level controls (MFA, account lockout, breached-password checks).

## 2.13 AWS Network Firewall & VPC Traffic Inspection ★★

**Definition:** A managed stateful network firewall/VPC IDS-IPS service for centralised inspection of VPC traffic.

**Important Points**
- Deployed into a dedicated **inspection VPC** per AZ with a firewall endpoint; routes from TGW/spokes are steered through it.
- **Stateless rule groups** (fast, 5-tuple) and **stateful rule groups** (Suricata-compatible, domain lists, allow/deny).
- Supports **domain-based egress filtering**, IPS signatures, TLS inspection (verify), and logging to S3/CloudWatch/Firehose.
- Use with TGW **appliance mode** for symmetric flows.
- **VPC Traffic Mirroring** can copy traffic to appliances/analytics without inline inspection; **Reachability Analyzer** models paths without sending packets.

**Edge Cases & Gotchas**
- Asymmetric routing breaks stateful inspection — appliance mode/ENI attachment is essential.
- Firewall endpoints are AZ-scoped: one per AZ or lose resilience.
- Cost scales with endpoints + data processed; centralising all traffic can be expensive.
- Not a WAF — it is L3/L4 with some L7 domain filtering, not HTTP request inspection.

**Interview Questions**
- **Basic — Network Firewall vs SG/NACL?** → SG/NACL are distributed, local controls; Network Firewall is centralised stateful inspection with IDS/IPS and domain filtering.
- **Medium — How do you centralise egress inspection across 20 VPCs?** → TGW with segmented route tables + inspection VPC with Network Firewall endpoints per AZ; spokes default route to TGW; firewall returns traffic; appliance mode enabled; logs centralised.
- **Hard/Scenario — After centralising egress, some apps break.** → Check asymmetric routing, missing return routes in the inspection VPC, domain allow-lists (including CDN/API domains and IP-literal traffic), port/protocol rules, TLS SNI-based rules vs IP-based, and firewall logs; roll back specific spokes while fixing.

## 2.14 AWS Global Accelerator ★★

**Definition:** A global service providing two static anycast IPv4 addresses and routing TCP/UDP traffic over the AWS global network to healthy regional endpoints.

**Important Points**
- Standard accelerator: TCP/UDP, 2 static anycast IPs (plus optional IPv6 dual-stack).
- Endpoints: ALB, NLB, EC2, Elastic IP, and (with custom routing) VPC subnet endpoints.
- Health checks per endpoint group; **traffic dials** (percentage per Region) and endpoint weights.
- **Client affinity** options; custom routing accelerator for deterministic endpoint selection.
- Bypasses much of the public internet; improves path stability and latency, not caching.
- Use case: global API with Mumbai/Singapore/Frankfurt endpoints, static IPs for allowlisting, fast regional failover.

**Edge Cases & Gotchas**
- Not a CDN — no caching.
- Health checks must reflect app readiness, or traffic shifts to a broken Region.
- Does not replicate data/state; database replication is your job.
- Accelerator endpoints must be in supported resource types and Regions (verify).
- Costs: hourly + data transfer premium (DT-Premium) — can be significant.
- Endpoint weights/dials are easy to misconfigure during failover tests.

**Interview Questions**
- **Basic — What is Global Accelerator?** → A global anycast routing service with static IPs that sends TCP/UDP traffic over the AWS network to healthy regional endpoints.
- **Medium — Global Accelerator vs CloudFront?** → Accelerator is a network-path optimiser for TCP/UDP with static IPs; CloudFront is a caching CDN for HTTP(S).
- **Hard/Scenario — Two Regions, active-passive, need <1 minute regional failover with fixed IPs.** → Global Accelerator with endpoint groups in both Regions, health checks on an app-level readiness endpoint, traffic dial 100/0 or weights, and pre-provisioned secondary capacity. Validate with game-day failover; verify data replication and DNS for internal dependencies.

## 2.15 VPC Flow Logs, Reachability Analyzer & Network Troubleshooting ★★

**Definition:** VPC Flow Logs capture IP traffic metadata at VPC/subnet/ENI level; Reachability Analyzer models connectivity between two resources without sending packets.

**Important Points**
- Flow log fields: srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start/end, action (ACCEPT/REJECT), log-status. Custom formats add vpc-id, subnet-id, instance-id, tcp-flags, pkt-srcaddr.
- Destinations: CloudWatch Logs, S3 (cheaper at volume, query with Athena), Firehose.
- Aggregation levels: VPC, subnet, ENI. **Do not** enable at VPC and ENI simultaneously thinking you get more data — you get duplicates.
- Flow logs don't capture: packets to the instance metadata service, DHCP/Windows licence traffic, some NTP/DNS traffic from the VPC resolver, or payloads.
- **Reachability Analyzer:** source → destination path analysis with component-level verdict (SG, NACL, route table, etc.).
- **Network Access Analyzer**, **Traffic Mirroring**, **CloudWatch Internet Monitor** (verify), **VPC IP Address Manager** complete the toolbox.
- Use case: prove a SG is blocking traffic in minutes instead of guessing.

**Edge Cases & Gotchas**
- REJECT entries only appear when the packet reaches a component that logs it; absence of logs isn't proof.
- Flow logs can be delayed minutes; not a real-time security tool.
- High-volume flow logs are expensive — sample or filter to REJECT, and expire in S3.
- ENIs are replaced on some events (instance stop/start) — filter on resource ID, not ENI ID.
- Logging does not capture application errors; pair with CloudWatch/ALB logs.

**Interview Questions**
- **Basic — What do VPC Flow Logs show?** → Metadata about accepted/rejected IP flows, not packet contents.
- **Medium — How do you diagnose "no traffic is reaching my instance"?** → Reachability Analyzer first (path + blocking component), then flow logs (REJECT at which hop), then SG/NACL/route checks, then OS-level tools.
- **Hard/Scenario — Intermittent connection resets between two services in different VPCs.** → Check for MTU/fragmentation, NAT/stateful firewall idle timeouts, asymmetric routes, SG rule churn, target health/draining, and retransmissions in flow logs/TCP metrics. Correlate timestamps with deployments and scaling events.

---

## 2.16 VPC Lattice, Verified Access & DNS Exfiltration Controls ★★

**Definition:** VPC Lattice is an application-layer service network that connects VPCs and accounts at the service level (listeners, target groups, auth policies); AWS Verified Access provides identity-aware, zero-trust access to private applications without a VPN.

**Important Points**
- **VPC Lattice:** define a **service** (listener + target group of IPs/ALBs/NLBs/Lambda), attach it to a **service network**, associate VPCs, and apply **auth policies** (IAM SigV4) at the service/network level. Security groups on the service control client access.
- Lattice solves the "many VPCs need to call one service" problem without a TGW/peering mesh, and it works across **overlapping CIDRs** because it is service-oriented rather than route-oriented.
- Traffic can be observed with **VPC Lattice access logs** and used for per-service authorisation — closer to a service mesh than to routing.
- **Verified Access:** evaluates **identity (IdP) + device posture (MDM/EDR)** per request and proxies to private applications behind an internal ALB/NLB. Replaces the traditional client VPN for workforce access with per-app, per-request policy.
- **DNS-based exfiltration controls:** Route 53 Resolver **DNS Firewall** (allow/deny lists, `BLOCK`/`ALERT` actions), plus **Network Firewall** domain lists for egress. Attacker tooling commonly tunnels data over DNS — outbound 53 to the internet should be denied or proxied, not left open.
- Use case: 30 spoke VPCs call a shared payments service through Lattice with IAM auth; vendors reach an internal admin app via Verified Access with device posture; DNS Firewall blocks known-bad domains and logs everything else.

**Edge Cases & Gotchas**
- Lattice is a connectivity/authorisation layer — it does not replace L4 firewalling, NACLs or inspection for all traffic.
- Auth policies are easy to over-grant (`Principal: *` with `Allow`) — treat them like IAM and review them.
- Lattice adds per-hour and per-GB cost; model it against TGW attachments for small estates.
- Verified Access requires identity provider and device-trust configuration — a broken IdP claim blocks all access, so keep a break-glass path.
- DNS Firewall only sees DNS queries through the Resolver; **hard-coded IPs, DoH/DoT to external resolvers and direct-to-IP traffic bypass it**. Combine with Network Firewall/SG egress rules that deny 53/853 to the internet.
- DNS Firewall is not a data-loss prevention product — it raises the cost of one exfiltration technique.

**Interview Questions**
- **Basic — What problem does VPC Lattice solve?** → Service-to-service connectivity and authorisation across many VPCs/accounts without building peering or TGW routing meshes, including across overlapping CIDRs.
- **Medium — Verified Access vs a client VPN?** → A VPN grants network-level access to a VPC; Verified Access grants per-application access evaluated per request against identity and device posture, with no broad network path.
- **Hard/Scenario — Security asks how you would stop data exfiltration over DNS.** → Deny or proxy outbound 53/853 to the internet at the SG/firewall layer, enable Route 53 Resolver DNS Firewall with allow-lists for business domains, log and alert on blocked queries, and monitor volume anomalies. Acknowledge the limits (DoH, IP-literal traffic) and pair it with egress Network Firewall and DLP controls.

---

# PART 3 — COMPUTE

## 3.1 Amazon EC2 — Instances & Families ★★★

**Definition:** Elastic Compute Cloud provides resizable virtual servers on AWS-managed physical hosts, with full OS control.

**Important Points**
- **Families:** general purpose (M, T), compute optimised (C), memory optimised (R, X, z), storage optimised (I, D, H), accelerated (P, G, Inferentia/Trainium), and specialised (Mac, HPC).
- **Naming:** `m6i.2xlarge` = family `m`, generation `6`, attributes (`i` Intel, `a` AMD, `g` Graviton, `n` network-optimised, `d` local NVMe), size `2xlarge`.
- **Burstable T-family:** CPU credits (baseline + burst); `T3/T4g` have **unlimited mode** option that bills surplus credits — a classic surprise bill.
- **AMIs:** Region-scoped golden images (versioned, encrypted, hardened); can be shared/copied; AMI ID differs per Region.
- **User data:** runs once at first boot via cloud-init on common Linux AMIs; used for bootstrap, not configuration management. Base64-encoded, max 16 KB.
- **Instance metadata:** IMDSv1 (legacy), **IMDSv2 (session-token, enforce it)**; optionally IMDSv2-only with hop limit 1 and RequireTokens.
- **Instance profile:** delivers temporary IAM role credentials via IMDS — never put access keys on instances.
- **Placement groups:** cluster (low latency, same rack — HPC), spread (distinct hardware, max 7 per AZ per group), partition (Hadoop/Kafka/Cassandra, isolated racks).
- **Status checks:** system (AWS hardware) vs instance (your OS/network). Auto Recovery moves an instance to healthy hardware keeping instance ID; stop/start re-hosts it.
- **Hibernation:** saves RAM to EBS root, restores on start; supported on limited instance types/AMIs.
- **EC2 Instance Connect / SSM Session Manager** for access without SSH keys or public IPs.
- **Tenancy:** shared (default), dedicated instance, dedicated host (BYOL, hardware visibility).
- Use case: lift-and-shift app servers, custom kernel/licence workloads, GPU inference, self-managed databases.

**Edge Cases & Gotchas**
- Stopping an instance may change the public IPv4; private IPv4 persists (unless re-created). Attach an EIP for stable addresses.
- Instance-store data is lost on stop/terminate; EBS root persists.
- T-family performance cliffs when credits are exhausted — `CPUCreditBalance` alarm is mandatory.
- Instance type availability is AZ-specific (and newer GPU types can be scarce); use capacity reservations for critical launches.
- An instance in a private subnet with no NAT/endpoint cannot reach package repositories — bootstrap fails silently.
- Nitro instances require the NVMe/EBS drivers in the AMI; old on-prem AMIs may not boot.
- Instance retirement/stop-start events exist (scheduled maintenance) — handle via health checks and ASG replacement.
- Enforcing IMDSv2 breaks legacy agents; enforce with SCP/launch template.

**Interview Questions**
- **Basic — What is an AMI?** → A template containing the OS, software and configuration for launching instances; regional and versioned.
- **Basic — What is an instance profile?** → A container for an IAM role that lets the EC2 instance obtain rotating temporary credentials through the instance metadata service — no static keys on the host.
- **Medium — Stop vs terminate?** → Stop shuts down and releases compute but keeps EBS and private IPs (public IP may change); terminate destroys the instance and attached EBS according to `DeleteOnTermination`.
- **Medium — How does IMDSv2 differ from IMDSv1, and why enforce it?** → IMDSv2 requires a `PUT` to obtain a session token before requests and supports a hop limit, which blocks most SSRF-based credential theft. Enforce it with launch templates (`HttpTokens: required`), an account default, and an SCP/Config rule so a compromised app cannot fetch credentials via a simple GET.
- **Hard/Scenario — An instance is at 100% CPU and unresponsive.** → Confirm with CloudWatch + `top`/`pidstat`/`htop`; check for runaway processes, retry storms, unbounded JVM GC, noisy neighbours (if co-located), CPU credits (burstable), and disk I/O wait. Mitigate by scaling out/up, restarting with validation, and fixing the code path. Add alarms and load tests.

**Production Troubleshooting — "instance is running but unreachable"**
```bash
# 1. Is it really healthy? system vs instance status (AWS-side vs OS/guest-side)
aws ec2 describe-instance-status --instance-ids i-0abc --include-all-instances \
  --query 'InstanceStatuses[0].[InstanceState.Name,SystemStatus.Status,InstanceStatus.Status,InstanceStatus.Details]' --output json

# 2. Does the network path actually exist? (models SG, NACL, route table, no packets sent)
aws ec2 create-network-insights-path --source <sg-or-eni-or-instance-id> \
  --destination <ip-or-eni> --protocol tcp --destination-port 22
aws ec2 start-network-insights-analysis --network-insights-path-id nip-0abc \
  --query 'NetworkInsightsAnalysisId' --output text

# 3. Has traffic arrived and been accepted/rejected?
aws logs filter-log-events --log-group-name /aws/vpc/flowlogs \
  --filter-pattern "REJECT" --start-time $(( ($(date +%s)-3600)*1000 ))
```
Interpretation: `SystemStatus=ok` + `InstanceStatus=impaired` → guest OS problem (disk full, kernel, fstab) → use **serial console / SSM Run Command**, not SSH. Both `ok` but no flow-log entries → traffic never reaches the ENI (route/SG/NACL/peer). Flow-log **REJECT** identifies the blocking layer. `Network Insights` names the exact blocking component, which is what you quote as the root cause.

## 3.2 EC2 Purchasing Options, Spot, RIs & Savings Plans ★★★

**Definition:** AWS offers On-Demand, Spot, Reserved Instances (Standard/Convertible), Savings Plans (Compute/EC2 Instance), and Dedicated options to trade flexibility for discount.

**Important Points**

| Option | Commitment | Discount | Flexibility | Notes |
| --- | --- | --- | --- | --- |
| On-Demand | None | Baseline | Full | Predictable, short-term |
| Savings Plans (Compute) | 1 or 3 yr, $/hr | Up to ~66% | Any instance family/Region/size (for eligible compute incl. Lambda/Fargate) | Best default for dynamic fleets |
| Savings Plans (EC2 Instance) | 1 or 3 yr | Up to ~72% | Family + Region locked | Better discount, less flexible |
| Reserved Instances | 1 or 3 yr | Up to ~72% | Standard less flexible; Convertible exchangeable | Some RIs can be sold on the RI Marketplace (verify) |
| Spot | None (2-min notice) | Up to ~90% | Interruptible | Capacity by spare pool; use for stateless/batch |
| Dedicated Hosts/Instances | Depends | Varies | — | Compliance/BYOL |

- **Spot best practices:** diversified instance types and AZs, capacity-optimised allocation strategy, Spot Fleet/ASG, **capacity rebalance**, checkpointing, graceful interruption handling (2-minute warning via IMDS/EventBridge), avoid stateful single-instance workloads.
- **Savings Plans apply per account/family of usage**; use Cost Explorer's recommendations with a conservative commitment — you pay for the commitment even if unused.
- Spot pricing changes gradually; interruptions depend on pool supply, not price alone.
- **RIs and Savings Plans** can be shared across accounts in an Organization (RI sharing/Savings Plans apply org-wide by default).
- Use case: web fleet on Savings Plans + Spot for batch/CI runners + On-Demand for DR spiky capacity.

**Edge Cases & Gotchas**
- Committing to 3-year RI/Savings Plans on an architecture that will change (Graviton migration!) locks in savings you can't use.
- Spot interruption does not always look like a stop — instances can be terminated, stopped or hibernated depending on config.
- Spot capacity is not guaranteed at a given time; critical capacity needs on-demand/reserved.
- Underutilised RIs = pure loss; monitor coverage and utilisation.
- Discounts and credits confuse cost reporting — tag, and use Cost Categories/ABP.
- Mixing Graviton and x86 changes Savings Plan flexibility only if using Compute SPs.

**Interview Questions**
- **Basic — How do you save money on steady-state EC2?** → Savings Plans/RIs for the baseline, right-sizing, Graviton where supported, Spot for fault-tolerant work, and autoscaling for variable load.
- **Medium — Spot vs On-Demand?** → Spot is spare capacity at a large discount with interruption risk; use for stateless, retryable, checkpointed workloads only.
- **Hard/Scenario — A batch platform must be 60% cheaper in 6 months without breaking SLAs.** → Profile utilisation, right-size, move suitable jobs to Graviton, buy Compute Savings Plans for the on-demand baseline, use Spot with diversified pools + checkpointing for batch, add a Spot interruption handler, and set budgets/anomaly detection. Track coverage/utilisation monthly.

## 3.3 Amazon EBS — Types, Snapshots & Performance ★★★

**Definition:** Elastic Block Store provides persistent, AZ-scoped block volumes for EC2 with snapshots to S3-backed storage.

**Important Points**

| Type | Media | Use case | Notes |
| --- | --- | --- | --- |
| gp3 | SSD | Default general purpose | 3,000 IOPS + 125 MiB/s baseline, independently provisionable up to high limits |
| gp2 | SSD | Legacy general purpose | IOPS tied to size (3 IOPS/GiB), burst bucket |
| io2 Block Express | SSD | Critical databases | Highest provisioned IOPS + durability, Multi-Attach eligible |
| io1 | SSD | Legacy provisioned | — |
| st1 | HDD | Throughput-heavy sequential (Kafka, logs) | Cannot be boot volume |
| sc1 | HDD | Cold/archive | Cannot be boot volume |

- **EBS is AZ-scoped**: to move, snapshot → copy to another Region → create volume in an AZ.
- **Snapshots are incremental**, stored in S3-managed infrastructure, encrypted snapshots stay encrypted; can be shared/copied across accounts/Regions (with KMS permissions).
- **Encryption**: default-on at account level is best practice; KMS CMKs, per-volume encryption.
- **Multi-Attach** (io1/io2) across instances in the *same AZ* requires a cluster-aware filesystem (GFS2/OCFS2) — otherwise corruption.
- **Performance:** IOPS vs throughput vs latency; EBS-optimised instances have dedicated bandwidth; gp3 lets you tune IOPS/throughput independently of size.
- **RAID in EBS** is generally not recommended for redundancy (EBS already replicates within AZ); striping (RAID 0) is used for higher aggregate throughput.
- **Snapshots & Data Lifecycle Manager (DLM)** for scheduled, retention-based backups; **AWS Backup** for centralised policies.
- **Fast Snapshot Restore (FSR)** to eliminate initial-volume latency (costly).
- Use case: gp3 for app servers; io2 for high-IOPS databases; snapshots nightly + cross-Region copies for DR.

**Edge Cases & Gotchas**
- Grow the volume → the **partition/filesystem must also be grown** (`growpart`, `resize2fs`/`xfs_growfs`).
- Can only grow volumes, never shrink them (size is not reduced; build a new smaller volume).
- An instance's EBS bandwidth cap can bottleneck even a very fast volume.
- Small I/O sizes and low queue depth cap achieved IOPS regardless of provisioning.
- `DeleteOnTermination` default true for root volumes, false for data volumes — verify explicitly.
- Snapshots are crash-consistent, not application-consistent unless you quiesce/freeze the filesystem or use VSS/application tooling.
- Multi-Attach without cluster FS = corruption, 100% of the time.
- AZ failure: EBS volumes are unavailable; snapshots can be restored to another AZ.
- gp2→gp3 migration is easy but doesn't automatically peak performance without tuning.

**Interview Questions**
- **Basic — EBS vs S3?** → EBS is block storage attached to one EC2 in an AZ; S3 is object storage over HTTP APIs, replicated across AZs.
- **Basic — What does gp3 give you over gp2?** → gp3 has a fixed baseline (3,000 IOPS, 125 MiB/s) with IOPS and throughput provisioned independently of volume size, so you do not have to over-provision capacity to get performance.
- **Medium — Why gp3 over gp2?** → Independent IOPS/throughput provisioning and better price/performance, no need to over-provision capacity for IOPS.
- **Medium — Crash-consistent vs application-consistent snapshots?** → A snapshot captures the block device as of that moment (crash-consistent) — like pulling the power. Application-consistent snapshots require quiescing the filesystem/app (VSS on Windows, freeze scripts on Linux) so the restored volume has a clean transaction state.
- **Hard/Scenario — After increasing a volume from 100 GiB to 200 GiB, `df` still shows 100 GiB.** → The block device grew; the partition and filesystem did not. Check `lsblk`, `growpart /dev/xvda 1`, then `resize2fs` or `xfs_growfs`. Verify with `df -h`. If an LVM layer exists, extend the PV/LV too.

## 3.4 Instance Store & EFS & FSx ★★

**Definition:** Instance store is ephemeral NVMe/SSD attached to the host; EFS is managed elastic NFS for Linux; FSx provides managed Windows/Lustre/NetApp/OpenZFS filesystems.

**Important Points**
- **Instance store:** highest IOPS/lowest latency; data lost on stop/terminate/host failure. Used for cache, scratch, temp DB.
- **EFS:** regional, multi-AZ NFSv4 shared filesystem; **performance modes** (General Purpose, Max I/O — verify current modes), **throughput modes** (Bursting, Provisioned, Elastic); **storage classes** (Standard, Infrequent Access, Archive) with lifecycle policies; security groups + IAM + access points + POSIX permissions.
- **EFS mount targets** are per-AZ ENIs — create one per AZ for HA, and mount via DNS.
- **FSx for Windows File Server:** SMB, AD integration, DFS, shadow copies.
- **FSx for Lustre:** HPC/ML, linked to S3 as a data repository.
- **FSx for NetApp ONTAP / OpenZFS:** NFS/SMB/iSCSI with snapshots/replication features.
- Use case: shared app content on EFS; ML training data on FSx Lustre; Windows user home drives on FSx for Windows.

**Edge Cases & Gotchas**
- EFS is not suitable for latency-sensitive databases or heavy small-file workloads.
- Bursting throughput is tied to stored size — small filesystems get low throughput; use Elastic/Provisioned.
- EFS is Linux-only; Windows needs FSx for Windows.
- Mount targets in only one AZ double cross-AZ data charges and create an AZ dependency.
- Instance store is *not* a backup solution — anything important must be replicated.
- FSx for Lustre performance scales with filesystem size; undersizing throttles.
- NFS v4.1 locking and many small files can trip up poorly-designed apps; EFS has higher latency than local disk.

**Interview Questions**
- **Basic — Instance store vs EBS?** → Instance store is ephemeral and host-attached; EBS is persistent and network-attached, survives stops.
- **Medium — When EFS over EBS?** → When multiple Linux instances/AZs need to share the same files (web content, lift-and-shift apps needing NFS). Not for databases.
- **Hard/Scenario — A lift-and-shift app needs a shared uploads directory across 6 app servers in 3 AZs.** → EFS with mount targets in each AZ, Security Groups referencing the app SG, access points per app, lifecycle policy to IA, and application retry logic for NFS latency. Consider S3 for new architectures (presigned URLs) instead of shared FS.

## 3.5 ECS & Fargate ★★★

**Definition:** Elastic Container Service is AWS's managed container orchestrator; Fargate is serverless compute for containers, removing node management.

**Important Points**
- **Task definition:** image, CPU/memory, ports, env vars, secrets (Secrets Manager/SSM via `valueFrom`), volumes, log config, task role (app permissions) vs **execution role** (pull image, write logs).
- **Launch types:** EC2 (you manage capacity, cheaper at scale, GPU/daemon control) vs Fargate (no nodes, per-task billing, simpler).
- **Services:** desired count, deployment types, load balancer attachment, service discovery, autoscaling (target tracking on CPU/memory/ALB request count/queue depth), deployment circuit breaker + rollback, health checks, blue/green with CodeDeploy.
- **Capacity providers:** Fargate, Fargate Spot, EC2 ASGs with managed scaling.
- **Task networking:** `awsvpc` gives each task its own ENI/IP (required for Fargate) — subnet IP planning matters.
- **Sidecars/init containers** for logging/proxies; **EBS/EFS volumes** for persistence (Fargate supports EFS).
- **Bottlerocket** as a hardened node OS; **ECS Exec** for debugging without SSH.
- Use case: microservices on Fargate with ALB, autoscaling, and Secrets Manager injection.

**Edge Cases & Gotchas**
- Task vs service role confusion (execution role cannot grant the app permissions).
- Fargate task size CPU/memory combinations are limited — invalid combos fail validation.
- `awsvpc` ENI density limits how many tasks fit on an EC2 node and consumes subnet IPs.
- Graceful shutdown requires `stopTimeout` + SIGTERM handling; otherwise in-flight requests drop.
- Log driver misconfiguration silently loses logs.
- Image pull from a private registry needs permissions (execution role) and NAT/VPC endpoints.
- Fargate Spot can reclaim tasks — handle interruptions.
- Sticky sessions/WebSockets with ALB need idle timeouts aligned.

**Interview Questions**
- **Basic — ECS task definition vs service?** → The task definition is the blueprint (image/CPU/memory/config); the service keeps a desired count running and integrates with load balancers/autoscaling.
- **Medium — ECS on EC2 vs Fargate?** → EC2: control over instances, lower cost at high, steady density, GPU/daemons; Fargate: no node ops, per-task billing, simpler scaling, higher unit cost.
- **Hard/Scenario — Tasks keep restarting every few minutes.** → `describe-services` events, stopped task reasons (OOMKilled 137, health-check failures, image pull errors, missing secrets), memory/cpu sizing, ALB health check path/port, app logs, and IAM permissions. Add deployment circuit breaker and alarms on task restarts.

## 3.6 Amazon EKS ★★★

**Definition:** Elastic Kubernetes Service is a managed Kubernetes control plane on AWS; you choose managed node groups, self-managed nodes, or Fargate for data-plane capacity.

**Important Points**
- **Control plane** is managed (multi-AZ, patched); you own the data plane, add-ons, and workload configuration.
- **Node options:** managed node groups (ASG-backed, easier upgrades), self-managed (full control), Fargate profiles (no nodes), Karpenter (just-in-time provisioning, best for consolidation/cost — verify current maturity).
- **Networking:** VPC CNI assigns pod IPs from subnets (secondary IPs/ENIs); **prefix delegation** raises pod density; **custom networking** uses a secondary CIDR. CIDR exhaustion is the #1 EKS networking bug.
- **IAM:** cluster IAM role; node IAM role; **IRSA** (IAM Roles for Service Accounts via OIDC) — now **EKS Pod Identity** as the newer simpler option (verify availability). Avoid node-role over-permissioning.
- **Access:** EKS API auth via IAM + `aws-auth` ConfigMap (legacy) / access entries (newer); RBAC inside the cluster.
- **Ingress/exposure:** ALB Ingress Controller, AWS Load Balancer Controller, NLB, Gateway API. **CNI/CSI add-ons** for VPC networking and EBS.
- **Storage:** EBS CSI driver (RWO volumes), EFS CSI (RWX), FSx.
- **Autoscaling:** HPA (pods), VPA (sizing), Cluster Autoscaler / Karpenter (nodes), KEDA (event-driven).
- **Upgrades:** control plane version then node groups; add-ons have version compatibility matrices; **blue/green node groups** for zero-downtime.
- **Observability/security:** CloudWatch Container Insights, ADOT/OpenTelemetry, Falco/GuardDuty EKS Runtime Monitoring, Pod Security Standards, network policies (requires CNI support).
- Use case: standardised microservices platform with IRSA-based least privilege and Karpenter cost control.

**Edge Cases & Gotchas**
- Subnet IP exhaustion → pods Pending; fix with prefix delegation, larger subnets, custom networking, or fewer pods per node.
- IRSA trust policy mistakes (wrong OIDC provider/audience/subject) cause `AccessDenied` even with correct IAM policy.
- Upgrading control plane before node/add-on compatibility can break workloads (deprecated APIs removed).
- Cluster AutoScaler doesn't scale down with local storage/PodDisruptionBudget issues and often mis-scales with heterogeneous instance types; Karpenter handles this better.
- CoreDNS/CoreDNS-node issues cause cluster-wide DNS failures — monitor CoreDNS replicas and IP capacity.
- Node security groups vs cluster security group confusion; the cluster SG is attached to ENIs.
- Pod security: privileged pods and hostPath mounts = node compromise.
- EKS costs: control plane hourly per cluster — many small clusters add up; use one cluster per env/team boundary, not per app.

**Interview Questions**
- **Basic — What does EKS manage vs you?** → AWS manages the control plane (API server, etcd, patching, HA); you manage nodes/Fargate, workloads, IAM/RBAC, networking, add-ons, and upgrades orchestration.
- **Basic — Managed node group vs Fargate profile?** → A managed node group gives you EC2 capacity with AWS handling node lifecycle/upgrades; a Fargate profile runs pods without nodes and without node-level control, at a higher per-pod cost and with no DaemonSets or privileged pods.
- **Medium — How do pods get IAM permissions?** → Preferred: IRSA (service account annotated with an IAM role via OIDC trust) or EKS Pod Identity. Avoid granting permissions to the node role, which every pod inherits.
- **Medium — Why is granting permissions to the node role an anti-pattern?** → Every pod on the node inherits those credentials, so one compromised pod has the union of all permissions. Use IRSA or EKS Pod Identity so each service account gets a scoped role and the node role stays minimal (ECR pull, CNI, logs).
- **Hard/Scenario — After a deploy, pods are Pending with "failed to assign an IP address".** → Subnet CIDR exhaustion or ENI/IP limits on nodes. Check free IPs per subnet, `max-pods` per node, VPC CNI logs, and add prefix delegation/secondary CIDR or scale node types. Long-term: plan /20+ private subnets per AZ and monitor `ipamd` metrics.

**Production Troubleshooting — errors, throttles and timeouts**
```bash
# Recent errors and duration percentiles for one function
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Errors \
  --dimensions Name=FunctionName,Value=order-processor \
  --start-time $(date -u -d'-1 hour' +%FT%TZ) --end-time $(date -u +%FT%TZ) \
  --period 300 --statistics Sum

# Is it throttling, or failing? (Throttles vs Errors vs ConcurrentExecutions)
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Throttles \
  --dimensions Name=FunctionName,Value=order-processor \
  --start-time $(date -u -d'-1 hour' +%FT%TZ) --end-time $(date -u +%FT%TZ) \
  --period 300 --statistics Sum

# What actually happened in one invocation?
aws logs filter-log-events --log-group-name /aws/lambda/order-processor \
  --start-time $(( ($(date +%s)-3600)*1000 )) --filter-pattern "ERROR Task timed out" | head -50
```
Interpretation: `Throttles > 0` with `ConcurrentExecutions` pinned at the account/reserved limit → concurrency problem (raise limits, add reserved/provisioned concurrency, or decouple with SQS). `Errors > 0` with `Duration ≈ timeout` → downstream slowness; check `Duration` p99 and the dependency's own metrics. `Duration` near zero with errors → handler exception, read the stack trace. Missing logs entirely → execution-role/log-permission or VPC endpoint issue.

## 3.7 AWS Lambda ★★★

**Definition:** Serverless event-driven compute that runs functions on demand, scaling automatically, with no server management.

**Important Points**
- **Execution model:** cold start vs warm start; invocation types (synchronous RequestResponse, asynchronous Event with internal retries, poll-based for SQS/Kinesis/DynamoDB Streams).
- **Limits to know conceptually:** 15-minute timeout, 10 GB memory/CPU sizing (CPU scales with memory), `/tmp` ephemeral storage configurable (512 MB–10 GB), 1,000 default concurrency (regional, can be raised), deployment package size limits, 4 KB synchronous payload / 256 KB async (verify).
- **Concurrency:** reserved concurrency (guarantee + cap for a function), **provisioned concurrency** (pre-warmed, removes cold starts, costs), unreserved pool shared across functions.
- **VPC:** Lambda in a VPC uses ENIs (Hyperplane-managed now); needs NAT/endpoints for internet/AWS APIs; cold starts worse with VPC (much improved but still).
- **Triggers:** API Gateway, ALB, S3 events, SQS/SNS, EventBridge, DynamoDB/Kinesis streams, Cognito, Step Functions, CloudFront (Lambda@Edge).
- **Destinations & DLQ:** on-failure destinations (SQS/SNS/EventBridge/Lambda) for async; DLQ for older patterns; retry semantics differ by source.
- **Packaging:** zip vs container images (up to 10 GB); layers for shared deps.
- **Power tools:** SnapStart (Java, verify), Graviton (arm64) for price/performance, ARM/custom runtimes, Lambda extensions.
- **Security:** execution role least privilege, env var encryption with KMS, secrets from Secrets Manager/SSM (cache and refresh), no hardcoded credentials.
- Use case: event processing (S3 upload → thumbnail), scheduled jobs, light APIs, glue code between services.

**Edge Cases & Gotchas**
- Lambda is not for long-running jobs or steady high-throughput workloads — cost and 15-min limit bite.
- Throttling under spikes: unreserved concurrency shared pool; provisioned concurrency or reserved needed for critical paths.
- Retries cause **duplicate processing** — design idempotent handlers (this is the classic interview probe).
- Async invocations retry twice then go to DLQ/destination; SQS pollers batch + partial batch failures need `ReportBatchItemFailures`.
- VPC Lambda without endpoints/NAT fails to call AWS APIs.
- Cold starts: large packages, VPC, init work outside the handler, and many dependencies increase latency. Mitigate with provisioned concurrency, SnapStart, smaller packages, lazy init.
- Env var size limit (4 KB total) — use Secrets Manager for large config.
- Recursive invocations (Lambda → S3 → Lambda) can loop and cost thousands of dollars — always guard with idempotency/state checks.
- `context.getRemainingTimeInMillis()` — handle timeouts gracefully.

**Interview Questions**
- **Basic — What is Lambda?** → Serverless, event-driven compute that runs code on demand with automatic scaling and pay-per-invocation billing.
- **Basic — What is a cold start?** → The first invocation on a new execution environment, which includes initialising the runtime and your handler (plus VPC ENI attachment for VPC functions), adding latency; later invocations on the same environment are warm.
- **Medium — Reserved vs provisioned concurrency?** → Reserved guarantees and caps concurrency for a function; provisioned pre-initialises environments to eliminate cold starts (and costs while idle).
- **Medium — How do synchronous and asynchronous invocations retry differently?** → Synchronous callers (API Gateway, ALB) get the error and must retry themselves; asynchronous events retry automatically (twice by default) before going to a DLQ or on-failure destination. Design handlers to be idempotent because retries are guaranteed somewhere.
- **Hard/Scenario — An S3 event triggers a Lambda that occasionally processes the same object twice.** → S3 events are at-least-once. Make the function idempotent (check a DynamoDB processed-events table keyed by object key+ETag+version), use conditional writes, and add a DLQ/destination. Also verify retries aren't amplified by client retries.

**Production Troubleshooting — 4xx/5xx and latency**
```bash
# Error breakdown by status code for a stage (5-min buckets)
aws cloudwatch get-metric-statistics --namespace AWS/ApiGateway --metric-name 5XXError \
  --dimensions Name=ApiName,Value=orders-api Name=Stage,Value=prod \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) \
  --period 300 --statistics Sum

# Integration latency vs total latency — separates API GW from the backend
aws cloudwatch get-metric-statistics --namespace AWS/ApiGateway --metric-name IntegrationLatency \
  --dimensions Name=ApiName,Value=orders-api Name=Stage,Value=prod \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) \
  --period 300 --statistics Average
```
Interpretation: `Latency` high but `IntegrationLatency` low → throttle/cache/edge issue at the gateway. `5XXError` with `IntegrationLatency` spiking → backend timeout (remember the 29 s hard limit). `429` → usage plan/stage throttle or Lambda concurrency. `502` to a Lambda proxy → malformed response shape or an unhandled crash.

## 3.8 API Gateway ★★★

**Definition:** A managed API front door offering REST, HTTP and WebSocket APIs with auth, throttling, caching, request validation and usage plans.

**Important Points**
- **REST API** (full features: caching, usage plans, API keys, WAF, request validation, transformations) vs **HTTP API** (cheaper/faster, JWT auth, simpler) vs **WebSocket API**.
- **Integrations:** Lambda proxy, HTTP proxy, AWS service (direct integration, e.g., SQS, DynamoDB), mock, VPC Link (private integration to NLB/ALB).
- **Auth:** IAM (SigV4), Cognito user pools, Lambda authorizers (token/request), JWT authorizers (HTTP API), mutual TLS (verify).
- **Throttling:** account-level 10,000 RPS default with per-API/usage-plan/stage limits; burst limits; 429 responses; use with Lambda reserved concurrency.
- **Caching:** stage-level cache (billed by size), TTL, invalidation.
- **Endpoint types:** edge-optimised (CloudFront), regional, private (via interface endpoint + resource policy).
- **Stages** for environments; canary deployments; usage plans + API keys for partner quotas.
- **Observability:** access logs (JSON), execution logs, X-Ray/ADOT tracing, CloudWatch metrics (4XXError, 5XXError, Latency, IntegrationLatency, CacheHitCount).
- Use case: REST API in front of Lambda with Cognito auth, throttling and WAF.

**Edge Cases & Gotchas**
- **Timeout is 29 s maximum** (integration timeout) — long jobs must be async (SQS/Step Functions) and return a job ID.
- 4XX/5XX errors: distinguish client (`400`, `403`, `429`) from integration (`502` bad gateway, `504` timeout).
- Lambda proxy integration requires the correct response shape; a malformed response = `502`.
- Throttling at API Gateway (429) vs Lambda (concurrency) vs downstream DB — different fixes.
- API keys are not authentication — they are identification/rate-limit tokens.
- Caching can serve stale data after a deploy; invalidate or version the cache key.
- WebSocket APIs need connection state managed in DynamoDB.
- Payload size limits (10 MB REST) — use S3 presigned URLs for large files.

**Interview Questions**
- **Basic — REST vs HTTP API?** → HTTP API is cheaper/faster with JWT auth and simpler features; REST API has caching, usage plans, request validation, WAF and richer integration options.
- **Medium — How do you protect a public API?** → WAF + throttling/usage plans + auth (Cognito/IAM/Lambda authorizer) + least-privilege Lambda role + input validation + access logging + alarms on 4XX/5XX/latency.
- **Hard/Scenario — A client reports random 429s at 300 requests/minute.** → Check stage/usage-plan throttles, account limits, Lambda reserved concurrency, downstream limits (DynamoDB throttle, RDS connections), and retry storms with no backoff. Fix by raising limits deliberately, adding client backoff+jitter, and queueing non-urgent writes.

## 3.9 AWS Batch, Step Functions & Event-Driven Orchestration ★★

**Definition:** AWS Batch runs containerised batch jobs with managed queues/compute; Step Functions orchestrates distributed workflows as state machines; EventBridge routes events between services.

**Important Points**
- **Batch:** compute environments (EC2/Spot/Fargate), job queues, job definitions; array jobs; retries; good for ETL, rendering, simulation.
- **Step Functions:** Standard (long-running, exactly-once, history limits) vs Express (high volume, at-least-once); states: Task, Choice, Parallel, Map (incl. Distributed Map), Wait, Retry/Catch; integrates with 200+ services; error handling and human approval patterns.
- **EventBridge:** event bus, rules with pattern matching, targets, schedules (cron), schema registry, partner/SaaS sources, cross-account routing, archive/replay.
- **Event-driven patterns:** choreography (events) vs orchestration (state machine); outbox pattern; saga with compensating transactions.
- Use case: nightly ETL with Step Functions Map over S3 partitions; EventBridge fan-out from an order service.

**Edge Cases & Gotchas**
- Step Functions Standard has execution history/state size limits — large payloads should be stored in S3 and passed by reference.
- Express workflows don't support all state types/integrations.
- EventBridge is **at-least-once** and ordering is not guaranteed — consumers must be idempotent.
- Rule pattern mismatches fail silently (no target invoked) — use CloudWatch metrics `FailedInvocations` and DLQs.
- EventBridge schedules use UTC; DST surprises for local-time jobs.
- Batch Spot interruptions need retry strategies and checkpointing.

**Interview Questions**
- **Basic — Orchestration vs choreography?** → Orchestration centralises flow in a coordinator (Step Functions); choreography lets services react to events (EventBridge) with no central controller.
- **Medium — When Step Functions over Lambda chaining?** → Multi-step, long-running, retryable workflows with visibility, error handling and human approvals; you avoid fragile chained Lambdas and 15-min limits.
- **Hard/Scenario — A 40-step data pipeline must resume after failures without reprocessing everything.** → Step Functions with per-step retry/catch, checkpointing to DynamoDB/S3, idempotent tasks, Map for parallel partitions, and a DLQ for unrecoverable items. Track execution history for auditability.

## 3.10 Elastic Beanstalk & App Runner (awareness) ★

**Definition:** Elastic Beanstalk is a PaaS that deploys applications onto managed EC2/ASG/ELB stacks; App Runner runs containerised web apps without infrastructure management.

**Important Points**
- Beanstalk: application versions, environments, platforms, deployment policies (all-at-once, rolling, rolling with additional batch, immutable, blue/green via separate env + CNAME swap), `.ebextensions` for config.
- You still own the underlying resources and can customise them; Beanstalk is a convenience layer, not magic.
- App Runner: source (image/ECR or code), autoscaling, TLS, VPC connector for private resources (verify current capabilities).
- Use case: legacy PaaS-style deployments in Beanstalk; simple containerised APIs on App Runner.

**Edge Cases & Gotchas**
- Beanstalk environments drift; teams forget the underlying ASG/ELB settings.
- Immutable deployments are safer but slower and can hit instance/AZ capacity.
- Beanstalk is not "serverless" — you pay for EC2/ELB.
- App Runner regions/features are limited compared with ECS/EKS; check VPC and custom-domain support.

**Interview Questions**
- **Basic — What is Elastic Beanstalk?** → A PaaS layer that provisions and manages the AWS resources needed to run your application.
- **Medium — Why do many teams move off Beanstalk?** → Limited flexibility/IaC friendliness vs ECS/EKS; hidden resource management; containerisation offers better portability.
- **Hard/Scenario — You must ship a legacy Tomcat app quickly with minimal ops.** → Beanstalk with immutable/blue-green deployments, RDS outside the environment for lifecycle independence, ELB + autoscaling, and later a re-platform plan.

---

## 3.11 AWS Systems Manager (SSM) ★★★

**Definition:** Systems Manager is the operations plane for AWS and hybrid servers: inventory, patching, remote command execution, secure shell access, parameter storage, automation and session auditing.

**Important Points**
- **Session Manager:** browser/CLI shell into EC2/on-prem/ECS-exec without opening inbound ports, a bastion or an SSH key. Requires the SSM agent, an instance profile with `AmazonSSMManagedInstanceCore`, and **outbound** connectivity to SSM endpoints (NAT or `ssm`, `ssmmessages`, `ec2messages` interface endpoints). Sessions can be logged to S3/CloudWatch with KMS encryption — a strong audit story and the modern answer to "how do you access production?"
- **Run Command:** execute scripts at scale (`AWS-RunShellScript`, `AWS-RunPowerShellScript`) with rate/concurrency controls, output to S3/CloudWatch, and no SSH — the correct tool for fleet-wide fixes.
- **Patch Manager:** patch baselines + maintenance windows; scan and install, with compliance reporting. Alternative to rebuilding AMIs, suitable for pets/long-lived fleets; immutable-image pipelines are often preferred for cattle.
- **Parameter Store:** hierarchical configuration and `SecureString` secrets (KMS), Standard vs Advanced tiers, no native rotation (use Secrets Manager for that).
- **Automation documents:** runbooks as code (restart a service, snapshot a volume, remediate a Config finding). Frequently the remediation target for EventBridge/Config/Security Hub.
- **Inventory, State Manager (associations), Fleet Manager, Distributor, OpsCenter/Incidents** round out the suite.
- **Hybrid/Arc-like:** **hybrid activations** register on-prem servers as managed nodes; `ssm-user` and port forwarding (`AWS-StartPortForwardingSession`) give DB access without exposing ports.
- Use case: no inbound 22/3389 anywhere; all admin access via Session Manager with session logging, patching in a Sunday window, and Config-driven auto-remediation through Automation runbooks.

**Edge Cases & Gotchas**
- "Instance not showing in Fleet Manager" is almost always: agent missing/stopped, no instance profile, no route to SSM endpoints, or an endpoint policy/SG blocking `ssmmessages`. Prove it from the instance (`systemctl status amazon-ssm-agent`, `curl` to `https://ssm.<region>.amazonaws.com`).
- Session Manager through a **private subnet with no NAT and no endpoints** silently fails — add the three interface endpoints.
- Run Command concurrency/error thresholds: a `50%` error threshold can stop a fleet-wide change halfway, leaving partial state.
- Patch Manager reboots disrupt workloads if not coordinated with load balancers/ASGs (use maintenance windows + health checks).
- Parameter Store has throughput limits per account/Region; high-frequency `GetParameter` calls need caching (or Secrets Manager with caching).
- Session logging is not on by default — enable it in preferences; without it you have access but no audit trail.

**Interview Questions**
- **Basic — What is Session Manager and why use it?** → A managed shell into instances through the SSM control plane with no inbound ports, no SSH keys and optional full session logging.
- **Medium — Session Manager vs bastion host?** → A bastion is a jump server you patch, expose and audit; Session Manager removes the public entry point and provides IAM-controlled, logged sessions per instance.
- **Hard/Scenario — A private instance cannot be reached with Session Manager.** → Check the agent status on the host, the instance profile (`AmazonSSMManagedInstanceCore`), `ssm`/`ssmmessages`/`ec2messages` endpoints or NAT path, SG/NACL egress on 443, and the endpoint policy. Then confirm the instance appears as a managed node in Fleet Manager before retrying the session.

---

# PART 4 — STORAGE

## 4.1 Amazon S3 — Fundamentals ★★★

**Definition:** S3 is object storage providing 11 nines of durability, bucket/key addressing and HTTP APIs for unlimited-scale data.

**Important Points**
- **Buckets are regional**, names globally unique per partition; **keys** are flat (prefix is not a directory).
- **Strong read-after-write consistency** for new PUTs, overwrites, deletes and LIST since Dec 2020.
- **Versioning:** protects against overwrite/delete (delete marker); required for replication and Object Lock.
- **Lifecycle:** transition between classes, expire objects/versions, abort incomplete multipart uploads.
- **Replication:** CRR/SRR, requires versioning; replication is **asynchronous**; supports replication of existing objects (batch replication) and delete-marker replication options.
- **Event notifications:** to SQS/SNS/Lambda/EventBridge.
- **Static website hosting**, **Transfer Acceleration**, **Requester Pays**, **Object Lambda** (verify), **Multipart Upload** (needed >5 GB, up to 5 TB object).
- **Access points** for per-app/team policies; **Access Analyzer** to find external access.
- **Logging:** server access logs (target bucket) + CloudTrail **data events** (per-object; volume cost).
- **Security:** Block Public Access (account + bucket), bucket policies, IAM, ACLs disabled by default (Object Ownership), encryption (SSE-S3 / SSE-KMS / DSSE-KMS / SSE-C), TLS-only bucket policies, MFA delete.
- Use case: data lake (with Athena/Glue), backups, static sites, media, log archive.

**Edge Cases & Gotchas**
- Versioning + lifecycle is essential; without it versioned buckets grow forever.
- DeleteObject without a version ID just adds a delete marker; recovering requires listing versions.
- SSE-KMS adds key permissions to the access path and has request-rate/cost considerations; **Bucket Keys** reduce KMS costs.
- Cross-account replication needs policies on source, destination and the KMS key.
- S3 is not a filesystem: no rename (copy+delete), no partial overwrite in place, no POSIX locks.
- Prefixes no longer need randomisation for performance (S3 auto-scales), but extreme hot prefixes can still hit limits.
- Event notifications are at-least-once — consumers must be idempotent.
- Public access is blocked by account-level BPA even if a bucket policy grants public read — this frustrates migration teams.

**Interview Questions**
- **Basic — Is S3 strongly consistent?** → Yes, for new object PUTs, overwrites, deletes and LIST operations since December 2020.
- **Basic — What happens when you delete an object in a versioned bucket without a version ID?** → S3 adds a **delete marker** rather than removing data; the object appears deleted, and removing the delete marker restores it.
- **Medium — How do you recover an overwritten object?** → With versioning enabled, get the previous version ID and copy/retrieve it; without versioning, restore from backup/replication (if any).
- **Medium — How do you enforce TLS-only access?** → A bucket policy with an explicit `Deny` on `s3:*` where `aws:SecureTransport` is `false` (plus disabling insecure endpoints at the SDK/client layer). The deny also catches internal clients that fall back to HTTP.
- **Hard/Scenario — A bucket is receiving 50k PUTs/second and costs are spiking.** → Review request patterns and key design; enable S3 Storage Lens/metrics; consider batching/compaction, lower-cost classes for cold data, lifecycle to expire intermediate objects, and avoid expensive LIST-heavy code. Check KMS request costs if using SSE-KMS with Bucket Keys.

**Production Troubleshooting — AccessDenied and slow/expensive access**
```bash
# Who am I, and what does the policy actually evaluate to?
aws sts get-caller-identity
aws s3api get-bucket-policy --bucket my-bucket | jq '.Policy' | sed 's/\\n/\n/g'
aws s3api get-public-access-block --bucket my-bucket        # is a BPA overriding intent?
aws s3api get-object-attributes --bucket my-bucket --key path/file --object-attributes ObjectSize,StorageClass

# Did the request even reach S3? (data events must be enabled)
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=GetObject \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --max-results 5
```
Interpretation: `AccessDenied` with a valid identity policy → check bucket policy explicit deny, **KMS `kms:Decrypt`**, SCP/boundary, VPC endpoint policy, and Object Ownership/ACL interaction in that order. A **403 on a private-endpoint-only bucket** is usually a DNS/endpoint-policy problem, not IAM. `StorageClass=DEEP_ARCHIVE` explains multi-hour latency and retrieval cost immediately.

## 4.2 S3 Storage Classes & Lifecycle ★★★

**Definition:** Storage classes trade retrieval cost/latency for storage cost; lifecycle rules automate transitions and expiry.

**Important Points**

| Class | Access pattern | Retrieval | Notes |
| --- | --- | --- | --- |
| S3 Standard | Frequent | Instant | Default; 3+ AZs |
| S3 Intelligent-Tiering | Unpredictable/changing | Instant | Auto-moves between tiers; small monitoring fee; no retrieval fee |
| Standard-IA | Infrequent, rapid access | Instant | Retrieval fee, 30-day min duration, min object size charge |
| One Zone-IA | Infrequent, re-creatable | Instant | Single AZ — not for primary data |
| Glacier Instant Retrieval | Archive, ms access | Instant | 90-day min duration |
| Glacier Flexible Retrieval | Archive | Minutes–hours | 90-day min |
| Glacier Deep Archive | Long-term archive | ~12 h | 180-day min; lowest cost |
| Express One Zone | Latency-sensitive, high throughput | Instant | Single AZ, directory bucket; not for durability-critical data |

- Lifecycle rule components: filter (prefix/tag/size), transitions (days since creation), expiration, noncurrent version transitions/expiration, abort incomplete MPU.
- Transitions must respect minimum storage durations or you pay early-deletion charges.
- **S3 Storage Lens** for org-wide storage metrics; **Inventory** for object-level reporting; **Batch Operations** for bulk actions.
- Use case: logs → Standard → IA at 30 d → Glacier IR at 90 d → Deep Archive at 365 d → expire at 7 y.

**Edge Cases & Gotchas**
- Small objects (<128 KB) in IA classes cost more per object overhead than they save.
- Frequent retrieval from archive classes can cost more than Standard.
- Lifecycle transitions take time (hours to a day); they are not immediate.
- Minimum-duration charges make "transition then delete in 10 days" expensive.
- Deep Archive retrieval can take 12+ hours — check application expectations.
- Intelligent-Tiering doesn't move objects smaller than 128 KB; use lifecycle prefixes for those.
- One Zone-IA/Express One Zone are not AZ-resilient — read the availability model.

**Interview Questions**
- **Basic — Cheapest class for yearly compliance archives?** → Glacier Deep Archive (with retrieval time and minimum-duration implications).
- **Medium — When Intelligent-Tiering?** → Unknown or changing access patterns; it removes the guessing while avoiding retrieval fees.
- **Hard/Scenario — A team wants to cut S3 cost by 70% without breaking apps.** → Analyse Storage Lens/Inventory by prefix/age/size; add lifecycle transitions for cold data; delete incomplete MPUs and noncurrent versions; dedupe; consider Bucket Keys for KMS cost; review request patterns (LIST storms) and move small-object workloads accordingly. Validate retrieval SLAs for each class before transitioning.

## 4.3 S3 Security Deep Dive ★★★

**Definition:** S3 access control combines identity policies, bucket policies, ACLs (legacy), Block Public Access, access points, and encryption.

**Important Points**
- **Evaluation:** explicit deny > allow in either identity or resource policy > implicit deny. Same-account: identity policy allows suffice. **Cross-account: both sides must allow** (unless the resource policy grants to the principal and identity also allows — both required for most cases).
- **Block Public Access** at account and bucket level: blocks public policies and ACLs, ignores new/existing public grants — leave ON unless you truly host a public site.
- **Object Ownership:** ACLs disabled (bucket owner enforced) is now the default for new buckets — simplifies ownership.
- **Access points:** per-application policies without editing one giant bucket policy; VPC-restricted access points.
- **Presigned URLs:** temporary, shareable URLs signed by the signer's credentials; expiry limited (max 7 days with sigv4/IAM credentials).
- **Encryption:** SSE-S3 (AES-256, automatic), SSE-KMS (audit + key control; watch request costs/limits), DSSE-KMS, SSE-C (customer keys). Default encryption is on for new buckets.
- **TLS enforcement:** deny `aws:SecureTransport: false`.
- **VPC endpoint policies:** restrict bucket access to a specific VPC/endpoint.
- **Cross-account patterns:** bucket policy with `aws:PrincipalOrgID` condition to allow only your Organization.
- Use case: app uploads via presigned PUT, reads via CloudFront OAC, private bucket, KMS-encrypted, blocked public, VPC-endpoint-restricted.

**Edge Cases & Gotchas**
- A bucket policy alone doesn't help if the identity policy denies or SCP blocks.
- KMS key policy is a **separate** permission gate — `s3:GetObject` without `kms:Decrypt` = AccessDenied.
- Presigned URLs inherit the signer's permissions — if the signer can delete, an uploader might too.
- `s3:*` on `Resource: *` in a CI role is a breach waiting to happen.
- Bucket owner and object owner differ after cross-account uploads if ACLs are enabled.
- CloudFront OAC requires both bucket policy and correct signing; a common misconfiguration is leaving the bucket public.
- Region/endpoint mismatch (calling a bucket in the wrong Region) produces confusing redirect errors.

**Interview Questions**
- **Basic — How do you make a bucket private but readable by an app?** → Block Public Access on, IAM role with least-privilege `s3:GetObject` on the specific prefix, bucket policy denying non-TLS, KMS key policy allowing the role, private endpoint or NAT for access.
- **Medium — Cross-account S3 access fails; why?** → Cross-account needs both the caller's identity policy (allow s3:GetObject) and the bucket policy granting the caller's principal (or role), plus KMS key policy if encrypted, and no SCP/endpoint-policy deny.
- **Hard/Scenario — Security wants proof that no bucket is public.** → Enable account-level Block Public Access via SCP/Org policy, run Access Analyzer for external/public access, use Config rules + Security Hub controls, AWS Trusted Advisor checks, and scheduled `s3api get-bucket-policy-status` audits; remediate with automation (EventBridge → Lambda).

## 4.4 Amazon EBS vs EFS vs S3 vs FSx — Choosing Storage ★★

**Definition:** AWS storage splits into block (EBS), file (EFS/FSx), and object (S3) with different access semantics, durability and cost.

**Important Points**

| Need | Service | Why |
| --- | --- | --- |
| Single EC2 OS/data disk | EBS gp3 | Block device, low latency |
| High-IOPS database volume | EBS io2 Block Express | Provisioned IOPS + durability |
| Shared Linux filesystem across AZs | EFS | Managed NFS, elastic |
| Windows SMB shares | FSx for Windows | AD integration, SMB |
| HPC/ML scratch linked to S3 | FSx for Lustre | High throughput |
| Web assets, backups, data lake | S3 | Durable, cheap, serverless access |
| Ephemeral cache | Instance store | Fastest local disk |

**Edge Cases & Gotchas**
- Databases on EFS/NFS = latency and locking problems.
- S3 "mount" tools (s3fs, mountpoint-s3) are not POSIX filesystems for write-heavy workloads; Mountpoint for S3 is read-oriented (verify current semantics).
- EBS Multi-Attach needs a cluster filesystem.
- Restoring from S3 backups for a database needs a restore process, not a mount.

**Interview Questions**
- **Basic — Which storage for a shared Linux upload directory?** → EFS (or S3 with presigned URLs for modern apps).
- **Medium — Why not run a database on EFS?** → NFS latency, locking/consistency semantics, and throughput characteristics are unsuitable; use EBS with the right IOPS or a managed DB.
- **Hard/Scenario — An ML team needs 100 TB of training data accessible at high throughput.** → Store the source of truth in S3; use FSx for Lustre with S3 integration for high-performance training; cache hot data locally; use S3 Intelligent-Tiering for cost.

## 4.5 Amazon S3 Access Points, Multi-Region Access Points & Transfer ★★

**Definition:** Access Points provide named network endpoints with distinct policies for a bucket; Multi-Region Access Points route S3 requests across buckets in multiple Regions; Transfer Family provides SFTP/FTPS/FTP into S3/EFS.

**Important Points**
- Access point names/aliases are used in the `s3://` ARN or alias; policies per access point keep bucket policies sane.
- **MRAP** routes to the lowest-latency bucket and can fail over; great for active-active reads; requires replication.
- **AWS Transfer Family:** managed SFTP/FTPS/AS2 endpoints backed by S3/EFS; authenticating via service-managed, AD, or custom identity provider.
- **DataSync** for scheduled NFS/SMB/S3/HDFS transfers with verification and bandwidth control.
- **Snowball/Snowcone** for petabyte transfers where the network is the bottleneck.
- Use case: partner SFTP landing zone into S3 with Lambda processing; MRAP for global read access.

**Edge Cases & Gotchas**
- MRAP has different endpoint semantics and not every S3 feature is available; check failover behaviour and replication lag.
- Transfer Family costs are per endpoint hour + data; not cheap for tiny volumes.
- DataSync needs agents/IAM roles and network paths; verification stages matter for compliance.
- Snowball has a minimum practical data volume to be cost-effective.

**Interview Questions**
- **Basic — What is an S3 access point?** → A named endpoint with its own policy for accessing a bucket, simplifying multi-application access control.
- **Medium — How do you give vendors a file-drop interface without giving AWS credentials?** → Transfer Family SFTP endpoint with a scoped IAM role/access point, or presigned S3 URLs; both avoid distributing long-lived credentials.
- **Hard/Scenario — 300 TB must move to S3 within a month over a 200 Mbps link.** → Calculate throughput (200 Mbps ≈ 2 TB/day ≈ 60 TB/month minus overhead), so the network cannot meet the deadline — use Snowball devices in parallel, then DataSync for incremental changes; verify chain of custody and checksums.

---

# PART 5 — DATABASES

## 5.1 Amazon RDS — Engines & Operations ★★★

**Definition:** RDS is a managed relational database service for MySQL, MariaDB, PostgreSQL, Oracle, SQL Server (and Db2) that automates provisioning, patching, backups and HA.

**Important Points**
- **Automated backups:** daily snapshot + transaction logs → **point-in-time recovery** within the retention window (1–35 days).
- **Manual snapshots** persist beyond deletion (until you delete them); **DB snapshot copy** across Regions.
- **Maintenance windows** for engine patching; **minor version auto-upgrade** settings.
- **Parameter groups** (engine settings) and **option groups** (engine features, e.g., Oracle options, SQL Server TDE).
- **Subnet groups** define which subnets (AZs) RDS can use; **private subnets only** in production.
- **RDS Proxy:** connection pooling, multiplexing, IAM auth, faster failover — essential for Lambda/serverless connection storms.
- **Performance Insights** for wait-event analysis; Enhanced Monitoring for OS metrics.
- **Storage autoscaling**, gp3/io1/io2 storage, encryption at rest via KMS, TLS in transit.
- **Custom endpoints** for replicas; **Blue/Green deployments** for major-version upgrades with managed switchover (verify engine support).
- Use case: Multi-AZ MySQL for OLTP, read replicas for reporting, RDS Proxy for a serverless API.

**Edge Cases & Gotchas**
- Replication lag on read replicas → stale reads; do not read-after-write from a replica.
- Failover is not instant: DNS update + app reconnection (typically tens of seconds to a couple of minutes). Applications need retry/reconnect logic and short connection timeouts.
- Max connections are tied to instance class; connection storms (Lambda, containers) exhaust them — use RDS Proxy or a pooler.
- Storage full = instance becomes read-only/unavailable; enable storage autoscaling and alarms.
- Auto minor version upgrade can surprise you in production — test in staging, control windows.
- Automated backups are retained only for the retention period; deleting the instance can delete backups unless you take a final snapshot.
- Encryption cannot be enabled on an existing unencrypted instance in place — snapshot → copy with encryption → restore (or blue/green).
- Long-running transactions block DDL and vacuum; watch for bloat and lock waits.

**Interview Questions**
- **Basic — What does RDS manage for you?** → Provisioning, patching, backups/PITR, Multi-AZ failover, monitoring integration, and storage management.
- **Basic — What is point-in-time recovery?** → Continuous transaction-log archiving plus daily snapshots lets you restore to any second within the retention window (1–35 days), into a **new** instance.
- **Medium — How do you get near-zero-downtime minor upgrades?** → Multi-AZ with a maintenance window, tested in staging, using blue/green or replica promotion, with app retry logic and a rollback plan.
- **Medium — What problem does RDS Proxy solve?** → Connection multiplexing and pooling between many short-lived clients (Lambda/containers) and a database with a limited connection count, plus IAM auth and faster failover handling.
- **Hard/Scenario — A serverless API causes "too many connections" errors.** → Add RDS Proxy (pooling/multiplexing) or a pooler, reduce connection churn, tune max_connections by instance class, set short-lived connections with proper closing, and add alarms on `DatabaseConnections`.

**Production Troubleshooting — latency, connections and failover**
```bash
# Where is the time going? Performance Insights style evidence first
aws rds describe-db-instances --db-instance-identifier prod-db \
  --query 'DBInstances[0].[DBInstanceStatus,MultiAZ,AvailabilityZone,ReadReplicaDBInstanceIdentifiers,EnhancedMonitoringResourceArn]' --output json

# Connection saturation and CPU (the two most common "database is slow" causes)
aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name DatabaseConnections \
  --dimensions Name=DBInstanceIdentifier,Value=prod-db \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 60 --statistics Average
aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name CPUUtilization \
  --dimensions Name=DBInstanceIdentifier,Value=prod-db \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 60 --statistics Average

# Replica lag (is the read path the problem?), and recent failover/maintenance events
aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name ReplicaLag \
  --dimensions Name=DBInstanceIdentifier,Value=prod-db-read-1 \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 60 --statistics Maximum
aws rds describe-events --source-identifier prod-db --source-type db-instance --duration 1440
```
Interpretation: `DatabaseConnections` at the instance-class ceiling → connection storms (add RDS Proxy / pooling, reduce pool size per pod). CPU high **and** `ReadIOPS`/`WriteIOPS` at the volume limit → instance/volume bottleneck, not a query problem. `ReplicaLag` high → stale reads and an unhealthy DR replica. `describe-events` shows failovers/maintenance that explain a latency cliff at a timestamp you can correlate with app errors.

## 5.2 RDS Multi-AZ vs Read Replicas vs Multi-AZ DB Cluster ★★★

**Definition:** Three distinct availability/scaling architectures: Multi-AZ DB instance (synchronous standby), Read Replicas (asynchronous copies, readable), Multi-AZ DB cluster (writer + two readable instances across 3 AZs).

**Important Points**

| Feature | Multi-AZ DB instance | Read Replica | Multi-AZ DB cluster |
| --- | --- | --- | --- |
| Purpose | HA | Read scaling | HA + readable standbys |
| Replication | Synchronous (block-level to standby) | Asynchronous (engine-level) | Semi-synchronous to 2 readable secondaries |
| Failover | Automatic | Not automatic | Automatic, faster failover |
| Reads from standby | No | Yes | Yes (2 readers) |
| Cross-Region | No (same Region) | Yes (supported engines) | Same-Region AZs |
| Cost | 2× instance | Per replica | ~3× instances |

- **Failover triggers:** AZ outage, instance failure, storage failure, patching, manual reboot with failover.
- **RDS events** (EventBridge) and `ReplicaLag` metric are the metrics to alarm on.
- **Promoting a replica** is a manual, one-way action that breaks replication.
- Use case: Multi-AZ for production OLTP; 2 replicas for reporting; Aurora Global DB when cross-Region is needed.

**Edge Cases & Gotchas**
- A traditional Multi-AZ standby is **not readable** — a classic interview trap.
- Read replicas are not backups; they replicate mistakes (DROP TABLE included) quickly.
- Failover causes connection drops — connection strings must not be pinned to an IP.
- Cascading replicas reduce primary load but increase lag.
- Cross-Region replicas add latency and cost (data transfer) and are asynchronous.
- Multi-AZ does not protect against Region failure.
- Replicas can be promoted accidentally — control IAM permissions.

**Interview Questions**
- **Basic — Multi-AZ vs Read Replica?** → Multi-AZ is HA with synchronous replication and automatic failover; Read Replicas are asynchronous, readable copies for scaling reads.
- **Medium — Can you read from a Multi-AZ standby?** → Not for a Multi-AZ DB instance. Multi-AZ DB clusters provide readable instances.
- **Hard/Scenario — After a write, the app reads stale data from a replica.** → Route read-after-write to the primary (session stickiness or a consistency flag), use replica lag metrics to gate replica reads, or restructure the flow (e.g., read from primary for X seconds after a user write).

## 5.3 Amazon Aurora ★★★

**Definition:** Aurora is a MySQL/PostgreSQL-compatible engine with a distributed, log-structured storage layer replicated across 3 AZs, plus serverless and global options.

**Important Points**
- **Storage:** 6 copies of 10 GB segments across 3 AZs; auto-grows to large sizes; you pay for storage used, not provisioned (except I/O-optimised — verify).
- **Endpoints:** writer, reader, custom; readers share a reader endpoint for load balancing.
- **Failover:** typically fast (tens of seconds); Aurora fast failover is a documented design feature.
- **Aurora Serverless v2:** capacity in ACUs, scales in fine increments; good for variable/unpredictable workloads; not for zero-cost idle like v1 was.
- **Aurora Global Database:** cross-Region replication with low lag (typically under a second), secondary Region readable, planned/forced failover (RPO can be near-zero for managed failover, non-zero on unplanned).
- **Backtrack** (MySQL-compatible, verify) to rewind the cluster without restore.
- **Performance Insights / Enhanced Monitoring / slow query log** are essential.
- **Parallel Query** (verify), **Aurora Machine Learning**, **zero-downtime patching**.
- **Cloning** for fast copy-on-write dev/test environments.
- Use case: high-throughput OLTP needing cross-AZ durability and fast failover; Global DB for multi-Region reads/DR.

**Edge Cases & Gotchas**
- Aurora is not "just MySQL": engine differences, parameter differences, and some features/locks behave differently.
- Global Database failover requires detaching secondaries (or managed planned failover) and repointing apps; DNS/endpoint handling matters.
- Replica lag is small but nonzero — read-your-writes still needs the writer endpoint.
- Serverless v2 minimum ACUs still cost money; scaling is not instantaneous for sudden 100× spikes.
- Storage costs grow with the high-water mark until you defragment/rebuild.
- Aurora limits on connections and temp tables differ from MySQL — tune parameters.
- Backtrack is not a substitute for backups.

**Interview Questions**
- **Basic — What makes Aurora different from RDS MySQL?** → Distributed log-structured storage replicated 6× across 3 AZs, faster failover, read replicas with low lag, global databases, serverless, and higher default performance.
- **Medium — Aurora vs RDS Multi-AZ?** → Aurora offers better durability/failover and replication performance at higher cost/complexity; RDS Multi-AZ is simpler and cheaper for modest workloads.
- **Hard/Scenario — A global app needs reads in three Regions and <1 min RTO.** → Aurora Global Database with a primary writer, secondaries in each Region (read locally), Route 53/Global Accelerator for traffic, managed planned failover for drills, and documented unplanned failover with RPO expectations.

## 5.4 Amazon DynamoDB — Keys, Capacity & Hot Partitions ★★★

**Definition:** DynamoDB is a fully managed, serverless NoSQL key-value/document database with single-digit-millisecond latency at any scale.

**Important Points**
- **Primary key:** partition key only, or partition key + sort key. The partition key is hashed to a partition; the sort key orders items within it.
- **Capacity modes:** on-demand (pay per request, scales automatically) vs provisioned (RCU/WCU with auto scaling; cheaper at steady, predictable load).
- **Item size limit: 400 KB.**
- **Indexes:** GSI (different partition key, eventually consistent, own capacity) and LSI (same partition key, different sort key, strongly consistent possible, created at table creation only).
- **Read consistency:** strongly consistent reads available on the table and LSIs; GSIs are **eventually consistent only**.
- **Streams** for CDC → Lambda/Kinesis; **Global Tables** for multi-Region active-active (MREC, last-writer-wins by default; verify multi-Region strong consistency options).
- **Transactions:** TransactWriteItems/TransactGetItems across up to 100 items, 2× cost.
- **TTL** for automatic expiry; **DAX** for microsecond read caching; **DynamoDB Accelerator** reduces hot-read pressure.
- **Adaptive capacity + burst capacity** absorb short spikes; **on-demand** handles unknown traffic.
- **Partition throughput:** per-partition limits apply (3,000 RCU / 1,000 WCU per partition — verify), so key design determines scale.
- Use case: sessions, carts, IoT state, leaderboards, idempotency tables, event metadata.

**Edge Cases & Gotchas**
- **Hot partition:** an `ACTIVE` status or a single big tenant concentrates traffic on one partition → throttling even with capacity to spare.
- GSI backpressure: if a GSI's write capacity is exhausted, writes to the **table** are throttled.
- Scans are expensive and slow — prefer Query with a good key design; use parallel scan sparingly.
- `ConsistentRead=true` costs 2× and isn't available on GSIs.
- Global Tables conflict resolution is last-writer-wins unless you implement custom reconciliation.
- On-demand still has per-table and account throughput limits — sudden 10× spikes can throttle.
- Empty partitions split/merge over time; capacity isn't instantly balanced after a hot key is fixed.
- Transactions are not a free replacement for good key design.
- Backups: PITR must be enabled explicitly; on-demand backups for long retention.

**Interview Questions**
- **Basic — Composite primary key?** → Partition key + sort key; partition key spreads data, sort key orders items within a partition and enables range queries.
- **Basic — How is capacity measured?** → One RCU = one strongly consistent read per second of an item up to 4 KB (eventually consistent reads cost half); one WCU = one write per second of an item up to 1 KB. Item size rounds up, so a 5 KB read costs 2 RCUs.
- **Medium — What causes throttling at low utilisation?** → Hot partitions/hot keys, GSI capacity mismatch, uneven access patterns, and per-partition limits. Check `ThrottledRequests`, `OnlineIndexThrottleEvents`, and CloudWatch Contributor Insights.
- **Medium — What happens when a GSI runs out of write capacity?** → Writes to the **base table** are throttled until the index catches up — index capacity is not isolated from table throughput, which is why GSI design and capacity must be sized together.
- **Hard/Scenario — A single enterprise tenant generates 70% of writes and throttles.** → Detect the hot key with Contributor Insights; apply **write sharding** (e.g., `tenant#<random 0..N>` as the partition key with scatter-gather reads), cache hot reads in DAX/ElastiCache, move large-tenant data to its own table/shard, and use on-demand mode during sharding rollout. Preserve query patterns with carefully designed GSIs.

**Production Troubleshooting — cache misses and evictions**
```bash
aws cloudwatch get-metric-statistics --namespace AWS/ElastiCache --metric-name CacheMissRate \
  --dimensions Name=CacheClusterId,Value=session-cache \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 300 --statistics Average
aws cloudwatch get-metric-statistics --namespace AWS/ElastiCache --metric-name Evictions \
  --dimensions Name=CacheClusterId,Value=session-cache \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 300 --statistics Sum
aws cloudwatch get-metric-statistics --namespace AWS/ElastiCache --metric-name CurrConnections \
  --dimensions Name=CacheClusterId,Value=session-cache \
  --start-time $(date -u -d'-2 hours' +%FT%TZ) --end-time $(date -u +%FT%TZ) --period 300 --statistics Maximum
```
Interpretation: rising `Evictions` + `BytesUsedForCache` at `maxmemory` → undersized or a leaked key pattern; the cache is silently dropping data. `CurrConnections` at the node limit → clients not pooling connections (very common with serverless). Miss rate spiking *and* DB CPU spiking together is the stampede signature — mitigate with locks/coalescing and warm-up, not just a bigger node.

## 5.5 ElastiCache (Redis / Memcached) ★★★

**Definition:** Managed in-memory caching: Redis (data structures, persistence, replication, pub/sub) and Memcached (simple, multi-threaded, non-persistent).

**Important Points**
- **Patterns:** cache-aside (lazy loading), write-through, write-behind, read-through; TTLs to bound staleness.
- **Redis features:** replication groups, Multi-AZ with automatic failover, cluster mode (sharding), persistence (AOF/RDB), pub/sub, streams, Lua scripting, sorted sets, transactions.
- **Memcached:** horizontally scaled, no persistence/replication, simplest multi-threaded option.
- **Security:** VPC-only, SGs, in-transit encryption (TLS), at-rest encryption, AUTH token/RBAC (Redis 6+), IAM auth (verify).
- **Scaling:** vertical (node type), horizontal (cluster mode shards/replicas), read replicas.
- **Serverless** option exists (ElastiCache Serverless — verify current features).
- **Metrics:** CPU, `EngineCPUUtilization`, evictions, `CurrConnections`, cache hit/miss, replication lag, `BytesUsedForCache`.
- Use case: session store, product catalogue cache, rate limiting counters, leaderboards.

**Edge Cases & Gotchas**
- **Evictions**: `maxmemory-policy` (`allkeys-lru`, `volatile-lru`) — a misconfigured policy silently drops keys and causes DB stampedes.
- Cache stampede/thundering herd after a flush or failover — use request coalescing/locks and jittered TTLs.
- Redis is single-threaded per shard for command execution; one huge key or O(N) command (`KEYS`, big `SMEMBERS`) stalls the shard.
- Cluster mode changes the client (multi-key ops need hash tags).
- Failover causes brief unavailability and possible data loss (depending on persistence mode).
- Never store the only copy of data in a cache.
- Cache invalidation strategy is the hard part — document it.

**Interview Questions**
- **Basic — Redis vs Memcached?** → Redis has persistence, replication, data structures and cluster mode; Memcached is a simple, multi-threaded, ephemeral cache.
- **Medium — How do you prevent a cache stampede?** → TTL jitter, request coalescing/locking, stale-while-revalidate, pre-warming, and keeping the DB protected with connection limits/timeouts.
- **Hard/Scenario — After a Redis failover, the database gets overwhelmed.** → The cache went cold and all traffic hit the DB. Mitigate immediately with rate limiting/queueing and read replicas; permanently: replicated cluster with Multi-AZ, warm-up strategy, cache-aside with locks, circuit breakers, and DB capacity headroom.

## 5.6 Amazon OpenSearch, Redshift & Athena ★★

**Definition:** OpenSearch is managed search/analytics on a Lucene-based engine; Redshift is a managed columnar data warehouse; Athena is serverless SQL over S3 (Presto/Trino-based).

**Important Points**
- **OpenSearch:** indexes, mapping, shards/replicas, snapshots, UltraWarm/cold storage tiers, fine-grained access control, VPC or public with auth; used for log analytics and full-text search.
- **Redshift:** columnar, MPP, distribution keys/styles, sort keys, compression encodings, **Redshift Spectrum** for S3, concurrency scaling, RA3 (separate compute/storage), serverless option, Materialized views.
- **Athena:** query S3 with SQL, pay per TB scanned; use **partitioning + Parquet/ORC + compression** to cut cost dramatically; federated queries; CTAS/INSERT INTO for ETL.
- **AWS Glue** catalog/ETL and **Lake Formation** for permissions around the S3 data lake.
- Use case: OpenSearch for application search and log analytics; Redshift for BI/warehouse; Athena for ad-hoc lake queries.

**Edge Cases & Gotchas**
- Athena costs explode with `SELECT *` on uncompressed CSV — partition and columnarise.
- Redshift distribution key mistakes cause data skew/redistribution and slow queries.
- OpenSearch shard sizing (target ~10–50 GB/shard) and too many shards hurt performance.
- OpenSearch is not a primary database.
- VACUUM/ANALYZE and sort-key maintenance matter for Redshift performance.

**Interview Questions**
- **Basic — Athena vs Redshift?** → Athena is serverless, pay-per-scan, ad-hoc over S3; Redshift is a provisioned/serverless warehouse with persistent optimisation for repeated BI workloads.
- **Medium — How do you reduce Athena cost?** → Convert to Parquet/ORC with compression, partition by common filters (date/tenant), avoid `SELECT *`, use CTAS for aggregates, and set per-query data limits.
- **Hard/Scenario — A BI team's Redshift dashboard is slow at month-end.** → Examine WLM/concurrency scaling, sort/distribution keys, statistics (ANALYZE/VACUUM), materialized views, result caching, and query patterns. Move heavy ETL off peak, use Spectrum for cold data, and consider RA3/serverless scaling.

## 5.7 Database Selection Matrix ★★★

**Definition:** A service-selection framework mapping access patterns, consistency and scale requirements to the right AWS database, rather than defaulting to one engine.

**Important Points**
- Choose from **access patterns and consistency requirements first**, engine familiarity second.
- Relational fits joins, multi-entity transactions and reporting; NoSQL fits known key-based access at scale; warehouses fit analytics; search engines fit text/facets; streams fit ordered replay.
- Most production estates use 3–4 database types, not one. Polyglot persistence is normal but increases operational cost — justify each engine.
- Migrating engines later is expensive; validate the access-pattern fit with a prototype and a load test.

| Requirement | Choose | Notes |
| --- | --- | --- |
| OLTP, relational, modest scale | RDS Multi-AZ | Simple, predictable |
| High-throughput relational, fast failover | Aurora | Distributed storage, Global DB |
| Global relational active-passive | Aurora Global Database | Low-lag cross-Region |
| Key-value at massive scale | DynamoDB | Design key access patterns first |
| Multi-Region active-active NoSQL | DynamoDB Global Tables | Conflict resolution plan needed |
| Read cache | ElastiCache Redis | TTL/invalidation design |
| Data warehouse / BI | Redshift | Columnar, MPP |
| Ad-hoc S3 queries | Athena | Partition + columnar |
| Search / log analytics | OpenSearch | Shard sizing |
| Graph | Neptune | — |
| Time series | Timestream (verify) | IoT/metrics |
| Ledger/audit | QLDB (verify availability) | Immutable history |
| Document/JSON with Mongo API | DocumentDB | Compatibility caveats |

**Edge Cases & Gotchas**
- Picking a database before documenting access patterns is the most expensive architectural mistake in this list — DynamoDB key design cannot be fixed later without migration.
- Polyglot persistence multiplies backup, monitoring, IAM and on-call complexity; consolidate where the benefit is marginal.
- "We might need joins later" pushes teams to relational for data that is fundamentally key-value — measure before over-engineering.
- Serverless NoSQL is not automatically cheaper: scan-heavy access patterns and on-demand pricing can exceed a small RDS instance.
- Compliance and residency requirements can eliminate an engine choice regardless of technical fit.

**Interview Questions**
- **Basic — When DynamoDB over RDS?** → Known access patterns, extreme scale, predictable key-value/document operations, no complex joins, and serverless ops.
- **Medium — When Aurora over DynamoDB?** → Relational integrity, joins, transactions across entities, and SQL reporting are more important than per-request scale.
- **Hard/Scenario — Design storage for an order system with 5k TPS writes and reporting.** → DynamoDB for orders with a well-designed key (tenant + order ID) and GSIs for status/date queries; DynamoDB Streams → analytics pipeline; Athena/Redshift for reporting; idempotency table; PITR + on-demand backups; TTL for transient records. Or Aurora if joins/ACID across many entities dominate — justify with access patterns.

---

# PART 6 — IDENTITY & SECURITY

## 6.1 IAM — Users, Roles, Policies ★★★

**Definition:** IAM controls authentication and authorization for AWS APIs through identities (users, roles, groups), policies, and AWS STS temporary credentials.

**Important Points**
- **Identities:** root user (lock it away, MFA, no access keys), IAM users (long-term credentials, legacy), groups, roles (assumed with STS temporary credentials), federated identities.
- **Policy types:** identity-based (managed/inline), resource-based (S3, SQS, Lambda, KMS, etc.), **permissions boundaries**, **SCPs**, **session policies**, ACLs (legacy).
- **Structure:** `Version`, `Statement[]` with `Effect`, `Action`, `Resource`, `Principal` (resource policies only), `Condition`.
- **Evaluation logic:** explicit **Deny always wins** → then SCP/boundary filter → then identity or resource allow → implicit deny by default.
- **Roles:** two policies — **trust policy** (who can assume) and **permissions policy** (what it can do). Cross-account access needs `sts:AssumeRole` on the caller side and a trust policy on the target side.
- **Instance profiles / IRSA / task roles** deliver credentials to compute without static keys.
- **IAM Access Analyzer:** identifies resources shared externally, validates policies, generates least-privilege policies from CloudTrail.
- **Identity Center (SSO):** federated workforce access with permission sets across accounts — the modern replacement for IAM users.
- **Conditions** worth knowing: `aws:SourceIp`, `aws:PrincipalOrgID`, `aws:SourceVpce`, `aws:MultiFactorAuthPresent`, `aws:RequestTag`, `aws:PrincipalTag`, `s3:prefix`, `aws:SecureTransport`.
- **Best practices:** no long-lived keys, MFA everywhere, least privilege, permission boundaries for delegated admin, rotate, monitor with CloudTrail, prefer roles over users.

**Edge Cases & Gotchas**
- "IAM policy allows S3 but access is denied" — check SCP, boundary, session policy, bucket policy, KMS key policy, VPC endpoint policy, and the right Region/ARN.
- Policy propagation is not instantaneous (usually seconds, but can take longer) — retries after a change.
- `iam:PassRole` is required for services launching resources with a role (EC2, Lambda, ECS, Glue) — forgetting it is a classic failure.
- `Resource: "*"` with wildcard actions is privilege escalation; also watch `iam:CreatePolicyVersion`, `iam:AttachRolePolicy`, `sts:AssumeRole` chains.
- Root user cannot be restricted by SCPs in the same way — never use it for daily work.
- Access key leakage in Git is the most common breach vector — use git-secrets/Secret Scanning + immediate key deactivation.
- Managed policy updates by AWS can change your effective permissions.
- Cross-account resource policy grants do not grant identity-policy permissions automatically in all service cases — understand per-service semantics.

**Interview Questions**
- **Basic — User vs role?** → A user is a long-lived identity with credentials; a role is assumed temporarily via STS with short-lived credentials and is the preferred mechanism for workloads and cross-account access.
- **Basic — What is a trust policy?** → The resource-based policy attached to a role that states **who** may assume it (principals, accounts, federated providers, conditions). It says nothing about what the role can do after assumption.
- **Medium — Inline vs managed policy?** → Inline is embedded in one identity (tightly coupled, hard to audit/reuse); managed is a standalone reusable document with versioning.
- **Medium — When do you use a permissions boundary?** → In delegated administration: you let a team create roles, but the boundary caps those roles so they cannot exceed a defined maximum — preventing privilege escalation while keeping ownership with the team.
- **Hard/Scenario — A role has `s3:GetObject` on the bucket but still gets AccessDenied.** → Check explicit deny (SCP/boundary/session/bucket policy), object ARN vs bucket ARN, KMS `kms:Decrypt` if SSE-KMS, VPC endpoint policy, bucket policy requiring a different principal, `aws:SecureTransport`, and whether the call uses the right role/credentials (`aws sts get-caller-identity`).

**Production Troubleshooting — proving why a call was denied**
```bash
# 1. Which identity is actually being used? (wrong role is the most common cause)
aws sts get-caller-identity

# 2. Simulate the exact action before arguing about policy JSON
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::111122223333:role/app-task \
  --action-names s3:GetObject --resource-arns arn:aws:s3:::my-bucket/path/file.json \
  --query 'EvaluationResults[0].[EvalDecision,EvalDecisionDetails,MatchedStatements]' --output json

# 3. Find the denying statement in CloudTrail (errorCode + errorMessage identify the block type)
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=GetObject \
  --start-time $(date -u -d'-1 hour' +%FT%TZ) --max-results 10 \
  --query 'Events[].CloudTrailEvent' --output text | jq -r '.errorCode // empty' | sort | uniq -c
```
Interpretation: `AccessDenied` → no allow reached (identity policy, resource policy, boundary, SCP). `AccessDeniedException`/KMS errors → check `kms:Decrypt` on the **object's** key. `explicitDeny=true` in the simulation output → quote the `MatchedStatements` service (SCP vs bucket policy vs boundary) — that is your root cause sentence. Simulation does **not** evaluate resource policies by default, so pair it with the bucket policy check.

## 6.2 IAM Policy Evaluation Workbook ★★★

**Definition:** A decision model for combining identity policies, resource policies, SCPs, permission boundaries, session policies and explicit denies — practised against concrete scenarios.

**Important Points**
- Order of reasoning: **explicit deny → SCP filter → permissions boundary/session policy filter → identity or resource allow → implicit deny**.
- Same-account requests can be allowed by an identity policy alone; cross-account requests generally need both an identity-side allow and a resource-based allow.
- A boundary or SCP can only reduce permissions — neither grants anything.
- KMS key policies are a separate gate for encrypted resources; the S3/SQS/Lambda policy allow is not sufficient on its own.
- VPC endpoint policies filter traffic on the network path and can deny requests that IAM allows.

**Edge Cases & Gotchas**
- An AWS-managed policy update can silently change effective permissions.
- Deny in a resource policy applies even to the account root principal unless explicitly excepted.
- `aws:PrincipalOrgID` conditions are how you safely allow an entire Organization without listing accounts.

**Scenario answers to practise out loud:**

| # | Setup | Result | Why |
| --- | --- | --- | --- |
| 1 | Identity allows `s3:*`; SCP denies `s3:DeleteObject` | Delete denied, other actions allowed | Explicit deny in SCP wins |
| 2 | Boundary allows only `s3:GetObject`; identity allows `s3:*` | Only GetObject allowed | Effective = intersection |
| 3 | Identity allows `s3:GetObject`; bucket policy denies principal | Denied | Resource-based explicit deny |
| 4 | Same account, identity allows; bucket policy has no statement for role | Allowed | Same-account identity allow suffices |
| 5 | Cross-account, identity allows; no bucket policy for caller | Denied | Cross-account requires resource-side permission |
| 6 | Identity allows `kms:Decrypt` on key A; object encrypted with key B | Denied | Wrong key |
| 7 | Role trust policy allows account A; user in account B has `sts:AssumeRole` | Denied | Trust policy must include B or the calling role |

**Interview Questions**
- **Basic — Does an SCP grant permissions?** → No; SCPs only filter the maximum permissions available in member accounts.
- **Medium — Does a permissions boundary grant permissions?** → No; it caps what identity policies can grant.
- **Hard/Scenario — A developer has AdministratorAccess but cannot create a VPC.** → An SCP at the OU level is likely denying `ec2:CreateVpc`, or a permissions boundary caps the role. Check `aws organizations list-policies-for-target`, the role's boundary, and CloudTrail `AccessDenied` event details.

## 6.3 AWS KMS ★★★

**Definition:** Key Management Service is a managed, FIPS 140-validated (verify level per feature) key service that creates and controls encryption keys integrated across AWS services.

**Important Points**
- **Key types:** AWS-owned (no control, invisible), AWS-managed (`aws/service-name`, automatic rotation, no key policy control), **customer managed keys (CMKs)** — full control, key policy, rotation, grants, cross-account use.
- **Key material origin:** KMS-generated, imported, or custom key store (CloudHSM).
- **Symmetric vs asymmetric**; **envelope encryption** — KMS encrypts a data key; the data key encrypts data locally (this is how S3/EBS encryption works).
- **Key policy** is the primary access control; IAM policies are secondary (unless the key policy delegates to IAM with `Enable IAM policies`).
- **Grants** for temporary, scoped access (used by services); **encryption context** for additional authenticated data and policy conditions.
- **Automatic rotation** (annual, optional for CMKs) rotates the *backing key*, not the key ID/ARN.
- **Multi-Region keys** for cross-Region encryption (DR; verify supported services).
- **Quotas:** per-account KMS request rate — exceeded quotas show as `ThrottlingException`; use **Bucket Keys** for S3 and data key caching for high-volume apps.
- **CloudHSM** when you need dedicated hardware and single-tenant key control; **KMS external key stores** to keep key material on-prem.
- Use case: encrypt EBS/S3/RDS with customer-managed keys, control cross-account decryption, audit key usage in CloudTrail.

**Edge Cases & Gotchas**
- Deleting a KMS key has a 7–30 day waiting period and is effectively permanent — data encrypted with it becomes unrecoverable.
- Key policy mistakes lock out services or accounts, and KMS is hard to "admin-fix" because key policies are the source of truth.
- `kms:Decrypt` is needed in addition to `s3:GetObject`; also `kms:GenerateDataKey` for writes.
- Cross-account encrypted data requires both key policies and grants/IAM on both sides.
- KMS request throttling can slow EBS/S3 workloads at high volume — bucket keys/data key caching.
- AWS-managed keys cannot be used cross-account or have their policies adjusted.
- Encryption at rest does not protect against a compromised principal that can decrypt — IAM is the real boundary.

**Interview Questions**
- **Basic — What is envelope encryption?** → KMS encrypts a data key; the data key encrypts the data. You store the encrypted data key with the data, reducing KMS calls and enabling rotation.
- **Medium — AWS-managed vs customer-managed keys?** → AWS-managed are automatic and convenient but not customisable or cross-account; CMKs allow key policy control, rotation, auditing and cross-account access.
- **Hard/Scenario — Encrypted S3 objects are unreadable after a cross-account role change.** → Verify the KMS key policy still grants the reading principal (or its account) `kms:Decrypt`, check for grants that were revoked, confirm the key is still enabled, and check encryption context conditions. Cross-account requires both the bucket policy and the key policy.

## 6.4 AWS Secrets Manager & SSM Parameter Store ★★★

**Definition:** Secrets Manager stores and rotates secrets with fine-grained access; Parameter Store stores configuration and (optionally encrypted) parameters hierarchically.

**Important Points**
- **Secrets Manager:** secrets with versions/stages (`AWSCURRENT`, `AWSPENDING`), **automatic rotation** via Lambda (native support for RDS/Aurora/Redshift/DocumentDB), cross-account access via resource policies, VPC endpoints, KMS encryption, replica secrets in multiple Regions.
- **Parameter Store:** Standard (free, 4 KB) vs Advanced (paid, 8 KB, policies, higher throughput); String/StringList/SecureString; hierarchy `/app/env/db/password`; **no native rotation** (you build it).
- Access via IAM; encryption via KMS; audit via CloudTrail.
- **Caching:** SDKs/agents cache; the **AWS Secrets Manager Agent** caches locally; do not call the API per request (throttling + latency + cost).
- Use case: DB credentials with 30-day rotation; feature flags and config in Parameter Store; third-party API keys in Secrets Manager.

**Edge Cases & Gotchas**
- Secrets Manager costs per secret per month + per 10k API calls — hundreds of secrets add up; Parameter Store Standard is free for config.
- Rotation Lambda failures leave `AWSPENDING` secrets; alarm on rotation failures.
- A rotated DB password breaks apps that cached it without refresh logic.
- Deleting a secret has a recovery window (7–30 days); beware of recreating the same name.
- Env-var injection (ECS/Lambda) fetches at start — long-running tasks need refresh strategy.
- Secret sprawl: plaintext env vars in CI logs, .env files in repos.

**Interview Questions**
- **Basic — Secrets Manager vs Parameter Store?** → Secrets Manager adds native rotation, versioning stages, cross-account resource policies and replication; Parameter Store is a cheaper hierarchical config store with SecureString and no built-in rotation.
- **Medium — How does rotation work for RDS?** → A rotation Lambda uses the `AWSPENDING` secret, changes the password via the RDS API/DB, tests it, then promotes it to `AWSCURRENT`. Apps must fetch/cache and handle both versions during the transition.
- **Hard/Scenario — After enabling rotation, some pods fail authentication.** → Pods cached the old credential. Use the Secrets Manager agent/sidecar or a refresh-aware client with retry on auth failure, allow overlap (two valid passwords briefly), and stagger rotation. Check rotation Lambda logs and the secret's version stages.

## 6.5 AWS CloudTrail ★★★

**Definition:** CloudTrail records AWS API activity (management events, and optionally data/insight events) for auditing and security investigation.

**Important Points**
- **Trails:** single-Region or all-Region; deliver to S3 (with optional log file validation), CloudWatch Logs, EventBridge. **Organization trail** covers all accounts.
- **Event types:** management events (control plane — free tier of one trail), **data events** (S3 object-level, Lambda invokes — volume-priced), **insight events** (anomalous API call rates/error rates).
- **90-day Event history** in the console per Region; long-term retention requires S3.
- **Integrity:** log file validation (digest files), S3 Object Lock/versioning + MFA delete for tamper resistance.
- **Detection:** EventBridge rules on CloudTrail (e.g., root login, IAM policy change, SG ingress 0.0.0.0/0, CloudTrail stopped) → SNS/Lambda/Security Hub.
- **Investigation:** filter by `eventSource`, `eventName`, `userIdentity.arn`, `sourceIPAddress`, `errorCode`, `requestParameters`.
- Use case: "who deleted the bucket?", compliance evidence, detecting privilege escalation.

**Edge Cases & Gotchas**
- Data events are **not on by default** — no S3 object-level audit until you enable them.
- A trail deleting/stopping is a common attacker step — alarm on `StopLogging`/`DeleteTrail` and protect the trail bucket with an SCP.
- CloudTrail does not capture the request body for all services (some request parameters are omitted/sensitive).
- Deliveries are batched (up to ~15 min in some cases) — not real-time.
- CloudTrail covers the control plane, not OS-level activity (use GuardDuty/agents/host logs).
- Cross-account aggregation needs an Organization trail to be practical.

**Interview Questions**
- **Basic — What does CloudTrail log?** → AWS API calls: who, what, when, from where, and the result — the control-plane audit trail.
- **Medium — Management vs data events?** → Management events are control-plane operations (CreateBucket, RunInstances); data events are high-volume data-plane operations (GetObject, PutObject) that must be explicitly enabled and cost more.
- **Hard/Scenario — An S3 object was deleted last month. How do you investigate?** → Search CloudTrail data events (if enabled) in Athena over the S3 log bucket for `DeleteObject` by `userIdentity` and `sourceIPAddress`; correlate with CloudWatch/ALB logs and IAM changes. If data events weren't enabled, you can only see bucket-level/bucket policy changes — which is the lesson to document.

## 6.6 Amazon GuardDuty, Security Hub, Inspector, Macie & Config ★★★

**Definition:** A suite of managed security services: threat detection (GuardDuty), posture/aggregation (Security Hub), vulnerability scanning (Inspector), sensitive-data discovery (Macie), and resource compliance rules (Config).

**Important Points**
- **GuardDuty:** analyses VPC Flow Logs, DNS logs, CloudTrail, EKS audit logs, S3 data events, malware protection; findings like cryptomining, credential exfiltration, unusual API from unusual location. Multi-account via Organizations.
- **Security Hub:** aggregates findings (GuardDuty, Inspector, Macie, Config, partner tools) against standards (CIS, PCI DSS, AWS Foundational Security Best Practices); automated remediation via EventBridge.
- **Inspector:** continuous vulnerability scanning of EC2, ECR images and Lambda code; CVSS-based findings.
- **Macie:** ML-based discovery/classification of sensitive data in S3 (PII, credentials) + bucket policy findings.
- **AWS Config:** records resource configuration changes, evaluates **Config rules** (managed/custom) for compliance, tracks resource history and relationships; **conformance packs**; auto-remediation with SSM Automation.
- **AWS Audit Manager** for evidence collection against frameworks (awareness).
- Use case: an SCP-protected security account aggregating findings across the Organization with auto-remediation for public buckets and open SGs.

**Edge Cases & Gotchas**
- GuardDuty is a detector, not a blocker — you need response automation (EventBridge → Lambda → isolate instance via SG change).
- Findings volume can overwhelm teams without triage/severity routing and suppression rules.
- Inspector agentless vs agent-based coverage differences (verify).
- Macie costs scale with S3 data scanned — scope buckets/prefixes sensibly.
- Config costs by configuration items recorded + rule evaluations; large accounts can be expensive.
- Aggregation requires proper Organizations delegation and cross-Region settings — easy to misconfigure.
- Security Hub findings don't fix anything by themselves.

**Interview Questions**
- **Basic — GuardDuty vs Config?** → GuardDuty detects threats/anomalous behaviour; Config tracks configuration state and evaluates rules for compliance.
- **Medium — How would you auto-remediate an EC2 instance with GuardDuty malware findings?** → EventBridge rule on the finding → Lambda: isolate via a quarantine SG (deny all except forensic access), snapshot EBS for evidence, disable instance profile, notify, then human-guided cleanup.
- **Hard/Scenario — Security wants continuous CIS compliance evidence across 40 accounts.** → Security Hub with CIS standard enabled at the Organization level, Config conformance pack, delegated admin account, automated remediation for high-severity controls, daily compliance report via EventBridge + SNS, and exception register for accepted risks.

## 6.7 ACM & Certificate Management ★★

**Definition:** AWS Certificate Manager provisions, manages and renews public/private TLS certificates for integrated services.

**Important Points**
- Public certificates are **free**, auto-renewed (DNS validation strongly preferred over email — email validation does not auto-renew reliably).
- **Regional binding:** ALB/NLB/API Gateway need the cert in the same Region; **CloudFront requires `us-east-1`**.
- **Private CA** (ACM PCA) issues private certificates for internal mTLS/service mesh.
- Cannot export public ACM certificates (use a private CA or third-party cert for export needs).
- Integrates with ALB/NLB, CloudFront, API Gateway, Elastic Beanstalk, App Runner, and more (verify per service).
- Validation methods: DNS (CNAME) or email; DNS validation supports wildcards and multi-domain SANs.
- Use case: ALB HTTPS with auto-renewed ACM cert; internal service mTLS with private CA.

**Edge Cases & Gotchas**
- A cert in the wrong Region (CloudFront needs `us-east-1`) fails silently at attach time.
- Email-validated certs expire if the approval mailbox changes — prefer DNS.
- Certificate expiry for non-ACM certs (imported or third-party) still needs monitoring — imported certs do not auto-renew.
- Deleting a DNS validation record breaks renewal later.
- Wildcard certs save money but not for multi-level subdomains.
- TLS policy configuration matters for compliance (minimum TLS version/ciphers).

**Interview Questions**
- **Basic — How are ACM public certs renewed?** → Automatically if they are in use and validated (DNS validation recommended); otherwise renewal fails and must be re-issued.
- **Medium — Which Region for a CloudFront certificate?** → `us-east-1`, regardless of origin Region.
- **Hard/Scenario — 200 ALBs use a wildcard cert that fails to renew.** → Check validation records (deleted/changed DNS), whether the cert is attached and in use, CA/DNS zone ownership, and CloudTrail for changes. Move to DNS validation, add expiry alarms via CloudWatch/EventBridge (`ACM Certificate Expiration` events), and keep the renewal CNAMEs immutable in IaC.

## 6.8 Amazon Cognito ★★

**Definition:** Cognito provides user sign-up/sign-in (User Pools) and temporary AWS credentials for authenticated users (Identity Pools).

**Important Points**
- **User Pools:** hosted UI, MFA, social/OIDC/SAML federation, password policies, groups, custom attributes, Lambda triggers (pre/post auth, pre sign-up), token (JWT) issuance.
- **Identity Pools:** exchange tokens for AWS credentials with an IAM role, scoped by rules.
- **Tokens:** ID token (identity claims), access token (scopes/groups), refresh token; JWT validation at API Gateway/ALB/backend.
- Limits: user pool quotas, group/attribute constraints; token lifetimes configurable.
- Use case: mobile/web app login with MFA, JWT authorizer at API Gateway, least-privilege S3 access per user via Identity Pool.

**Edge Cases & Gotchas**
- User Pools are for authentication, not authorization logic — enforce role/permission checks at the API.
- Deleting a user pool deletes users irrecoverably; export/plan.
- Custom attributes cannot be changed easily after creation (immutable in practice).
- Refresh token revocation and global sign-out behaviour must be designed.
- Identity Pool role selection with per-user data requires careful IAM policy conditions (`sub` claim, leading-key strategies).
- Cognito quotas/rate limits on auth operations can throttle large bursts of logins.

**Interview Questions**
- **Basic — User Pool vs Identity Pool?** → User Pool authenticates users and returns JWTs; Identity Pool exchanges those tokens for temporary AWS credentials via IAM roles.
- **Medium — How do you secure an API with Cognito?** → Validate the JWT (issuer, audience, expiry, signature) at API Gateway (Cognito authorizer) or the backend, map groups/scopes to authorization, use short-lived access tokens and refresh tokens.
- **Hard/Scenario — Users must only read their own S3 prefix.** → Identity Pool with an IAM policy using `${cognito-identity.amazonaws.com:sub}` in the resource path (`s3:prefix` and `s3:LeadingKeys` for DynamoDB), plus bucket policy that does not allow cross-prefix access. Never trust a client-supplied user ID.

## 6.9 AWS Shield, WAF, Firewall Manager & Security Baseline ★★

**Definition:** A layered edge security baseline: Shield (DDoS), WAF (L7 filtering), Firewall Manager (org-wide policy), plus the account baseline (CloudTrail, Config, GuardDuty, BPA, SCPs, IAM hygiene).

**Important Points**
- **Baseline checklist for any new account:**
  - Root: MFA, no access keys, unlikely-to-guess email alias.
  - CloudTrail organization trail + S3 log archive (Object Lock), Config recorder, GuardDuty, Security Hub, Inspector, Macie (if S3 with PII).
  - S3 Block Public Access at account level, EBS default encryption, IMDSv2 enforcement.
  - IAM: Identity Center for humans, roles for workloads, no long-lived keys, password policy, permission boundaries for delegated admins.
  - Network: no 0.0.0.0/0 on 22/3389, VPC flow logs, Network Firewall for central egress if required.
  - SCP guardrails for region allow-list, security service protection, root action denial.
  - Budgets + Cost Anomaly Detection.
- **Firewall Manager** centrally enforces WAF rules, Shield Advanced, SG policies and Network Firewall policies across accounts.
- **Shield Advanced** includes DDoS cost protection, SRT access and proactive engagement for high-risk events.
- Use case: onboarding a new account from a Control Tower baseline in minutes, verified by Security Hub compliance.

**Interview Questions**
- **Basic — What blocks a DDoS at L3/4 vs L7?** → Shield (Standard automatic, Advanced enhanced) handles volumetric L3/L4; WAF rate-based and bot rules handle L7.
- **Medium — How do you ensure every ALB in the org has a WAF?** → Firewall Manager WAF policy scoped to the Organization with auto-remediation for non-compliant resources.
- **Hard/Scenario — A new account was created by a developer and is missing all security controls.** → Control Tower Account Factory/landing-zone automation prevents this; otherwise use Config-aggregator + Security Hub to detect drift, apply baseline via StackSets, and add SCPs/guardrails so manual accounts cannot be created without baseline.

**Edge Cases & Gotchas**
- Shield Standard is automatic but limited; volumetric L7 attacks need WAF rules and rate limits, not just Shield.
- WAF managed rules in Block mode from day one cause false positives that look like outages — always start in Count.
- Firewall Manager policies only apply to resources it can see; resources in unsupported configurations or Regions are silently unprotected.
- Baseline drift is the norm: a new service that requires a public endpoint quietly bypasses the "no public access" intent — exceptions need an owner and expiry.
- Security tooling that pages nobody is security theatre; every high-severity detector needs an owner, a runbook and an SLA.

---

# PART 7 — INTEGRATION & MESSAGING

## 7.1 Amazon SQS ★★★

**Definition:** SQS is a fully managed message queue for decoupling producers and consumers, offering Standard and FIFO queues.

**Important Points**
- **Standard:** at-least-once, best-effort ordering, nearly unlimited throughput.
- **FIFO:** exactly-once processing per message group with ordering, **message group IDs**, deduplication IDs, limited throughput (higher with high-throughput mode/batching — verify).
- **Visibility timeout:** the message is hidden while a consumer processes it; if not deleted in time it becomes visible again → duplicate processing if the work takes longer.
- **Long polling** (up to 20 s) reduces empty receives and cost; **short polling** returns immediately.
- **Dead-letter queue (DLQ):** `maxReceiveCount` then move to DLQ — essential for poison messages.
- **Retention** default 4 days, max 14 days; **message size** up to 256 KB (claim-check larger payloads in S3).
- **SQS + Lambda:** event source mapping, batch size, partial batch failure reporting, scaling based on queue depth.
- **KMS encryption, SSE**, VPC endpoints, IAM policies, queue-level resource policies.
- **Delay queues** and per-message timers.
- Use case: order processing decoupling, buffering writes during spikes, DLQs for async consumers.

**Edge Cases & Gotchas**
- Visibility timeout shorter than processing time = duplicates. Set to ~6× average processing time and extend via heartbeat for long jobs.
- Standard queues guarantee **at-least-once**, so idempotency is mandatory.
- FIFO throughput is per message group; a single group serialises and can bottleneck (hot group).
- A DLQ without alarms is a silent data-loss path — alarm on `ApproximateNumberOfMessagesVisible`.
- Not deleting the message after processing causes redelivery after visibility timeout.
- Consumers polling with too few threads/throttled Lambda concurrency leave a growing backlog.
- SQS is not a stream — no replay, no ordering guarantee for Standard.
- Encryption does not prevent a misconfigured policy from allowing anonymous access.

**Interview Questions**
- **Basic — SQS Standard vs FIFO?** → Standard: at-least-once, high throughput, no strict ordering; FIFO: exactly-once (dedup) and ordering per message group with lower throughput.
- **Medium — What is a visibility timeout?** → The period a received message is hidden from other consumers. If the consumer doesn't delete it in time, it's redelivered.
- **Hard/Scenario — The queue backlog is growing and consumers are idle.** → Check Lambda concurrency/unreserved limits, batch size, function duration, and errors (throttling in DLQ); verify consumer scaling and queue depth alarms. If Lambda is throttled by downstream, add reserved concurrency/backoff and possibly move to EC2/ECS consumers with controlled concurrency.

## 7.2 Amazon SNS ★★★

**Definition:** SNS is a pub/sub messaging service delivering messages to many subscribers (SQS, Lambda, HTTP/S, email, SMS, mobile push) with fan-out.

**Important Points**
- **Topics** (Standard and FIFO), **subscriptions** with filter policies, delivery retry policies, DLQs for failed deliveries.
- **Fan-out pattern:** SNS topic → many SQS queues (each with its own consumer and DLQ) — the canonical decoupling design.
- Message filtering by attributes avoids sending irrelevant messages to subscribers.
- **SNS FIFO** for ordered fan-out to SQS FIFO.
- **Mobile push** via platform applications; **SMS** with per-number costs.
- Encryption with KMS, access policies, VPC endpoints.
- Use case: one "order placed" event → billing queue, email queue, analytics queue.

**Edge Cases & Gotchas**
- SNS is push-based and fire-and-forget: a failed HTTP subscription without a DLQ loses the message.
- Email/SMS subscriptions must be confirmed; email delivery is best-effort and not for critical flows.
- SNS cannot buffer for a slow consumer — use SQS in between.
- Message size limit (256 KB) — store large payloads elsewhere.
- Cross-account subscriptions need topic policy permissions and (for encrypted topics) KMS grants.

**Interview Questions**
- **Basic — SNS vs SQS?** → SNS is pub/sub push to many subscribers; SQS is a pull-based queue for one consumer group.
- **Medium — Why fan-out with SNS → multiple SQS?** → Each consumer gets its own durable queue, independent retry/DLQ/throughput, avoiding a single shared-consumer bottleneck.
- **Hard/Scenario — A downstream team misses events occasionally.** → If they use an HTTP subscription, add a DLQ + retry policy; better, move them to an SQS subscription with a DLQ and alarms. Confirm subscription filter policies aren't dropping messages, and check SNS delivery failure metrics.

## 7.3 Amazon EventBridge ★★★

**Definition:** A serverless event bus that routes events between AWS services, your applications and SaaS partners based on content-based rules.

**Important Points**
- **Event buses:** default (AWS service events), custom, partner. Rules match on event pattern → targets (Lambda, SQS, SNS, Step Functions, API Gateway, Kinesis, another bus).
- **Schedules** (cron/rate) for time-based invocation — replaces classic CloudWatch Events rules.
- **Schema registry + discovery**, **archive and replay** for up to 90 days (verify).
- **Cross-account** event buses and **resource-based policies** enable centralised event routing.
- **Pipes** for point-to-point integrations with filtering/enrichment (verify).
- Delivery: at-least-once, no ordering guarantee (use FIFO SNS/SQS or sequencing keys for ordering needs).
- Use case: react to EC2 state changes, S3 events (via EventBridge), GuardDuty findings, or custom domain events.

**Edge Cases & Gotchas**
- Pattern matching errors fail silently — no target invoked, no error. Always add DLQ + `FailedInvocations` alarm.
- EventBridge is not a queue: no backpressure; bursts can throttle targets.
- Ordering is not guaranteed — design idempotent, order-agnostic handlers or use FIFO downstream.
- Schedules are UTC and run in the Region of the rule.
- Cross-account routing requires policies on both buses and often KMS (for encrypted buses).
- Cost per event can exceed SQS for very high volume.

**Interview Questions**
- **Basic — EventBridge vs SNS?** → EventBridge does content-based routing/filtering across many event sources with schemas and replay; SNS is simpler pub/sub fan-out.
- **Medium — How do you ensure no events are lost?** → DLQ on the rule target, retries with backoff, archive/replay for reprocessing, alarms on `FailedInvocations`, and idempotent consumers.
- **Hard/Scenario — Teams keep missing events from a custom bus.** → Inspect rule patterns against actual event JSON (CloudWatch Logs/`TestEventPattern`), confirm the rule is enabled and the target permission exists, check target DLQ and failed invocations, and add archive+replay for recovery.

## 7.4 Amazon Kinesis & MSK ★★

**Definition:** Kinesis Data Streams is a managed real-time streaming service (shards, ordered records, replay); MSK is managed Apache Kafka.

**Important Points**
- **Kinesis Data Streams:** shards with capacity limits (writes/reads per shard — verify), partition keys, sequence numbers, retention 24 h–365 d, **on-demand** vs provisioned mode, enhanced fan-out for multiple consumers, KCL for processing.
- **Kinesis Data Firehose:** managed delivery to S3/Redshift/OpenSearch/Splunk with buffering, compression, transformation (Lambda), no replay.
- **Kinesis Data Analytics (Managed Flink):** SQL/Flink streaming analytics (verify naming).
- **MSK:** Kafka-compatible, brokers across AZs, IAM auth/SASL, MSK Connect, tiered storage (verify), MSK Serverless.
- **Hot shard problem** = same as DynamoDB hot partition: poor partition key distribution.
- Use case: clickstream ingestion, IoT telemetry, log pipelines, CDC into a lake.

**Edge Cases & Gotchas**
- Kinesis ordering is per shard; too few shards limits throughput; resharding is operationally heavy.
- Repeated partition key values create hot shards.
- Firehose does not support replay — if you need reprocessing, land raw data in S3 and use Streams.
- Consumer lag (KCL `MillisBehindLatest`) is the key metric — alarm on it.
- MSK requires Kafka expertise: topic sizing, partitions, rebalancing, broker storage, and upgrades.
- Kinesis record size limit 1 MB (verify).

**Interview Questions**
- **Basic — Kinesis vs SQS?** → Kinesis is an ordered, replayable stream with multiple consumers per shard; SQS is a queue where a message is consumed and deleted.
- **Medium — Kinesis Data Streams vs Firehose?** → Streams for custom real-time processing with replay; Firehose for managed delivery/loading to destinations.
- **Hard/Scenario — Consumers are falling behind on a 20-shard stream.** → Check `MillisBehindLatest`, per-shard throughput limits, hot shards (uneven partition keys), consumer parallelism (one KCL worker per shard, enhanced fan-out limits), and processing time per record. Fix with resharding/on-demand mode, better partition keys, parallel processing, and batching.

## 7.5 Messaging Selection Matrix ★★

**Definition:** A selection framework for AWS messaging and eventing services based on delivery semantics, ordering, replay and fan-out requirements.

**Important Points**
- Ask four questions: **one consumer or many? ordering required? replay needed? synchronous or asynchronous?**
- Queues (SQS) decouple producers from consumers and provide buffering; pub/sub (SNS) duplicates a message to many subscribers; an event bus (EventBridge) routes by content with schemas and archive/replay; streams (Kinesis/MSK) retain an ordered log for multiple independent consumers.
- Every asynchronous hop needs a **DLQ + alarm** and an **idempotent consumer**.
- Prefer the simplest service that meets the requirement — SNS/SQS before EventBridge, EventBridge before Kinesis.

| Need | Service | Key reason |
| --- | --- | --- |
| Simple decoupling queue | SQS Standard | Cheap, durable, at-least-once |
| Strict ordering + dedup | SQS FIFO | Message groups |
| One-to-many notify | SNS | Fan-out, multiple protocols |
| Content-based routing, many sources | EventBridge | Rules, schemas, replay |
| Ordered fan-out | SNS FIFO → SQS FIFO | Ordering across subscribers |
| High-volume stream, replay | Kinesis / MSK | Shards/partitions, retention |
| Delivery to S3/Redshift | Firehose | Managed batching/transform |
| Long-running workflow | Step Functions | Orchestration + retries |
| Request/response API | API Gateway + Lambda | Sync contract |

**Edge Cases & Gotchas**
- Every asynchronous hop needs a DLQ and an alarm — a queue without DLQ monitoring is a silent data-loss path.
- At-least-once delivery is the default everywhere: consumers must be idempotent.
- Choosing a stream when a queue would do adds shard management, checkpointing and cost for no benefit.
- FIFO queues scale per message group: one hot group serialises and becomes the bottleneck.
- Event-driven choreography without a trace of the end-to-end flow is very hard to debug — propagate correlation IDs.

**Question — When would you choose Kafka (MSK) over Kinesis?** → Existing Kafka ecosystem/tooling, very high throughput with many consumers, fine-grained retention/compaction control, or multi-protocol compatibility. Kinesis wins on operational simplicity and AWS-native integration.

**Interview Questions**
- **Basic — Name the four core messaging patterns and one service each.** → Queue (SQS), pub/sub (SNS), event routing (EventBridge), streaming (Kinesis/MSK).
- **Medium — SNS fan-out vs EventBridge rules?** → SNS pushes to subscribers with simple filter policies; EventBridge matches rich event content across many sources, supports schemas, archives and replay.
- **Hard/Scenario — An order event must reach billing, email and analytics, and analytics is often down.** → SNS topic (or EventBridge bus) fanning out to three SQS queues with independent DLQs and consumers, so a slow/down analytics consumer never affects billing or email; add idempotent consumers and queue-depth alarms.


---

# PART 8 — AUTO SCALING & ELASTICITY

## 8.1 Auto Scaling Groups ★★★

**Definition:** An ASG maintains a desired number of EC2 instances across AZs and adjusts capacity according to policies and health checks.

**Important Points**
- **Min/Desired/Max** capacity; launch template (or mixed instances policy with multiple instance types + Spot allocation strategies).
- **Health checks:** EC2 (instance status) and **ELB** (target group health) — enable ELB checks for apps behind a load balancer.
- **Health check grace period** and lifecycle hooks (pending:wait, terminating:wait) for bootstrap and graceful drain.
- **Scaling policies:** target tracking (recommended — CPU, ALB request count per target, SQS backlog per instance), step scaling, simple scaling, scheduled scaling, **predictive scaling** (ML-based for recurring patterns).
- **Cooldowns / warmup**: default cooldown and target-tracking warmup prevent thrash.
- **Instance refresh** for rolling replacement of instances with a new launch template; **warm pools** for pre-initialised capacity.
- **Capacity rebalance** for Spot: proactively replaces instances at elevated interruption risk.
- **Termination policies** and AZ rebalancing behaviour.
- **Suspended processes** can silently stop scaling (AddToLoadBalancer, AlarmNotification, Launch, Terminate, HealthCheck, ReplaceUnhealthy).
- Use case: web fleet 3–30 instances across 3 AZs on target tracking at 60% CPU.

**Edge Cases & Gotchas**
- **"CPU is high but no scale-out"** checklist: max capacity, suspended processes, scaling policy/alarm state, cooldown/warmup, quotas (vCPU), subnet IP exhaustion, launch template errors (AMI/instance type/key pair/SG), AZ capacity, and IAM permission issues.
- Aggressive scale-in causes flapping — use longer stabilisation windows and target tracking's built-in warmup.
- Bootstrapping from user data slows readiness — use golden AMIs/containers + warm pools.
- ASG replaces unhealthy instances — if your app fails health checks during deploys, you get rolling outages.
- Spot-only ASGs can lose all capacity in a bad pool.
- Cross-AZ data transfer costs grow with chatty cross-AZ scaling.
- ASG lifecycle hooks without heartbeats leave instances stuck in waiting states.

**Interview Questions**
- **Basic — What are min/desired/max?** → The lower bound, the target count and the upper bound; the ASG tries to maintain desired while respecting min/max.
- **Medium — Target tracking vs step scaling?** → Target tracking maintains a metric near a target automatically; step scaling adjusts by increments based on alarm thresholds and is better for non-linear responses.
- **Hard/Scenario — During a sale, scaling lags 5 minutes and users see errors.** → Pre-scale with scheduled scaling before the event, use target tracking on request count per target (leading indicator) rather than CPU (lagging), lower warmup, use warm pools/golden AMIs, and verify quotas. Add predictive scaling for recurring traffic.

**Production Troubleshooting — "the ASG isn't scaling"**
```bash
# 1. Why did the last scaling activities fail? (the single most useful command)
aws autoscaling describe-scaling-activities --auto-scaling-group-name web-asg \
  --max-items 10 --query 'Activities[].[StartTime,StatusCode,StatusMessage,Cause]' --output table

# 2. Is the alarm driving it in ALARM state, with data?
aws cloudwatch describe-alarms --alarm-name-prefix web-asg \
  --query 'MetricAlarms[].[AlarmName,StateValue,StateReason,Threshold]' --output table

# 3. Account-level blockers: vCPU quota, subnet IPs, suspended processes
aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A   # Standard On-Demand vCPUs
aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-0abc \
  --query 'Subnets[].[SubnetId,AvailabilityZone,AvailableIpAddressCount]' --output table
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names web-asg \
  --query 'AutoScalingGroups[0][SuspendedProcesses,MaxSize,DesiredCapacity,Instances[].AvailabilityZone]'
```
Interpretation: `StatusCode=Failed` with `StatusMessage` naming a quota (`VcpuLimitExceeded`), capacity, or launch-template error is the root cause — quote it. All `Successful` but count not rising → alarm not in ALARM, cooldown/warmup still active, or max capacity reached. `AvailableIpAddressCount` low in one AZ → instance launches in that subnet fail even though others succeed.

## 8.2 Scaling Strategies Beyond EC2 ★★

**Definition:** Elasticity options across compute models — ECS service autoscaling, EKS HPA/Cluster Autoscaler/Karpenter, Lambda concurrency, DynamoDB on-demand, Aurora Serverless v2.

**Important Points**
- **ECS:** target tracking on CPU/memory/request count/queue depth; capacity providers with managed scaling; Fargate vs EC2 provider strategies.
- **EKS:** HPA (metrics-server/custom metrics), VPA, Cluster Autoscaler, **Karpenter** (fast, bin-packing, spot-aware), KEDA (event-driven).
- **Lambda:** reserved/provisioned concurrency, concurrency scaling is automatic but bounded by limits.
- **DynamoDB:** on-demand or auto scaling; pre-warm for known spikes.
- **Aurora Serverless v2:** ACU range, scales in seconds (not instant).
- **Multi-dimensional scaling** and queue-depth-based scaling are the senior-level answers (scale on the metric that leads user impact).
- Use case: SQS-driven worker fleet scaling on backlog per instance.

**Edge Cases & Gotchas**
- Scaling on CPU fails for I/O-bound or queue-driven workloads — CPU stays low while latency grows.
- HPA without resource requests misbehaves (targets % of request); missing requests = unpredictable scaling.
- Cluster Autoscaler needs the pending pod's requests to be satisfiable by an available instance type — heterogeneous/ARM nodes can block scaling.
- Scale-in without connection draining drops requests.
- Provisioned concurrency costs money even when idle.

**Interview Questions**
- **Basic — What metric should drive scaling?** → A metric that leads user impact (queue depth, request rate per target, latency) rather than a lagging one (CPU after saturation).
- **Medium — HPA vs Cluster Autoscaler?** → HPA scales pod replicas; Cluster Autoscaler/Karpenter scales nodes to fit pending pods.
- **Hard/Scenario — Pods are pending with "0/20 nodes available: insufficient cpu" but node CPU is 40%.** → Pod requests are too large for the remaining allocatable capacity (or nodes have daemonsets/system reservations). Right-size requests, enable a node autoscaler/Karpenter, add instance types, and review taints/tolerations, affinity and topology spread constraints.

---

# PART 9 — MONITORING, LOGGING & OPERATIONS

## 9.1 Amazon CloudWatch — Metrics, Alarms, Dashboards ★★★

**Definition:** CloudWatch is AWS's observability service for metrics, logs, alarms, dashboards and automated actions.

**Important Points**
- **Metrics:** namespace, dimensions, resolution (standard 1 min, **high resolution 1 s**), retention (1 min for 15 days → 1 h for 455 days; verify).
- **Alarms:** metric alarms (static or **anomaly detection band**), composite alarms (AND/OR of alarms), actions (SNS, ASG, EC2 actions, SSM).
- **Missing data treatment:** `missing`, `notBreaching`, `breaching`, `ignore` — wrong choice causes alarms that never fire or always fire.
- **Custom metrics:** `PutMetricData` (watch cardinality and cost), embedded metric format (EMF), CloudWatch agent.
- **Dashboards** across accounts/Regions; **metrics insights** queries; **cross-account observability**.
- **CloudWatch Logs:** log groups, retention (default never expire — set it!), metric filters, subscription filters, Logs Insights query language, export to S3.
- **CloudWatch Logs Insights:** query syntax `fields | filter | stats | sort | limit`; use for quick incident triage.
- **EventBridge/CloudWatch Events** for scheduled tasks and AWS state-change reactions.
- *Critical alarms to have for any EC2/ALB stack:* CPU, status check failures, `UnHealthyHostCount`, `TargetResponseTime`, `5XXError`, `RequestCount`, disk/`mem` (agent), and application-specific error rates.
- Use case: alarm on ALB 5XX > 1% for 2 datapoints in 5 minutes → SNS → on-call.

**Edge Cases & Gotchas**
- Default **memory and disk metrics don't exist** without the CloudWatch agent (this is a favorite interview trap).
- `Average` vs `p99` statistics: CPU average hides saturation spikes; use percentiles for latency.
- Alarm `InsufficientData` states cause silent alerting gaps — alarm on that too, or use appropriate missing-data treatment.
- High-cardinality custom dimensions make metrics expensive and slow.
- Logs Insights is not a full analytics engine — extremely large scans are slow/expensive.
- Cross-account dashboards/alarms need explicit sharing configuration.
- CloudWatch Logs retention defaults to "never expire" — unbounded cost.
- Alarm actions can recur (StateUpdate/OK actions) — design notification flow deliberately.

**Interview Questions**
- **Basic — How do you monitor EC2 memory?** → Install the CloudWatch agent to publish `mem_used_percent` as a custom metric (it is not a hypervisor-visible metric).
- **Basic — Standard vs high-resolution metrics?** → Standard metrics are 1-minute granularity; high-resolution custom metrics support sub-minute data (down to 1 second) and can drive faster alarms, at a higher cost.
- **Medium — Metric alarm vs composite alarm?** → A metric alarm triggers on a metric condition; a composite alarm combines alarm states with AND/OR logic to reduce noise and express multi-signal conditions.
- **Medium — What does an alarm in `INSUFFICIENT_DATA` mean?** → The alarm has no data that satisfies its evaluation periods — the metric isn't publishing, the dimensions are wrong, or the resource is new. Treat it as an unknown state and alarm on it; do not assume it means healthy.
- **Hard/Scenario — The dashboard shows normal CPU for all instances while users report slowness.** → Look at latency percentiles (p95/p99), ALB `TargetResponseTime`, request count, downstream dependency times (DB `ReadLatency`, cache miss rate), GC/thread pool saturation, disk I/O, and network. CPU average hides brief saturation and queueing — use p99 and saturation metrics.

## 9.2 CloudWatch Logs, Application Signals & X-Ray ★★

**Definition:** CloudWatch Logs centralises application/system logs; **X-Ray** provides distributed tracing; CloudWatch Application Signals/ADOT provide service-level SLO views.

**Important Points**
- **Structured JSON logs** are essential for filtering/querying — log the request ID, trace ID, user/tenant, status, latency.
- **Correlation:** propagate a correlation/trace ID through API Gateway → Lambda → downstream services; X-Ray does this automatically when instrumented.
- **X-Ray:** traces, segments, subsegments, service map, annotations/indexed metadata, sampling rules; SDK/daemon/OpenTelemetry (ADOT) options.
- **Log routing:** subscription filters → Kinesis/Firehose → S3/OpenSearch for long-term analytics.
- **Retention and cost:** set retention per log group, avoid logging PII/secrets, sample debug logs, control verbosity in production.
- **Container logs:** awslogs/FireLens drivers; EKS uses Fluent Bit/CloudWatch agent add-on.
- Use case: a 500 ms p99 regression traced to a slow DynamoDB call in X-Ray's service map.

**Edge Cases & Gotchas**
- X-Ray sampling means not every request is traced — good for cost, bad for rare bugs (adjust sampling rules).
- Logs often become the biggest observability cost — no retention policy = compounding charges.
- Unstructured logs make alerts brittle; use metric filters on structured fields.
- Missing trace propagation through async hops (SQS/EventBridge) breaks end-to-end tracing unless you propagate headers manually.
- Logging secrets/PII creates a compliance incident — redact at the SDK/agent layer.

**Interview Questions**
- **Basic — What is X-Ray?** → A distributed tracing service that shows request paths and latency across services, including downstream AWS calls.
- **Medium — How do you trace a request across Lambda → SQS → Lambda?** → Propagate the trace header (`X-Amzn-Trace-Id`/trace context) into message attributes, instrument both functions, and stitch in X-Ray; or use OpenTelemetry with a collector for vendor-neutral tracing.
- **Hard/Scenario — p99 latency degrades only for 2% of requests.** → Use percentile alarms, trace sampling tuned to capture slow requests, per-dependency latency (`TargetResponseTime`, DB `ReadLatency`, downstream API), and correlate by instance/tenant. Aggregate averages will never reveal this.

## 9.3 AWS Health, Trusted Advisor, Incident Response & Runbooks ★★

**Definition:** AWS Health notifies on service events affecting your resources; Trusted Advisor provides best-practice checks; SRE practice ties this into incident response and runbooks.

**Important Points**
- **AWS Health Dashboard:** account-specific events (scheduled maintenance, service degradation); integrate with EventBridge for automation; Organizational view for multi-account.
- **Trusted Advisor:** cost optimization, security, fault tolerance, performance, service limits; full checks need Business+ support.
- **Incident management:** severity levels, on-call rotation, comms templates, timelines, blameless postmortems, action items with owners.
- **Runbooks:** documented steps for common alerts; automated where possible (SSM Automation/Systems Manager documents).
- **Game days / chaos engineering:** AWS Fault Injection Service (FIS) for controlled failure experiments (AZ failure, instance termination, latency injection) — verify features.
- Use case: monthly game day terminating a random ASG instance and testing alarm→runbook→recovery.

**Edge Cases & Gotchas**
- AWS Health events can be resource-specific for paid support plans only (verify current behaviour).
- Alerts without runbooks create MTTR chaos; runbooks without testing rot.
- Postmortems that blame people prevent learning.
- Chaos testing in production requires blast-radius controls and business approval.

**Interview Questions**
- **Basic — What is a runbook?** → A documented, repeatable procedure for handling a specific operational event.
- **Medium — How do you reduce MTTR?** → Actionable alerts tied to runbooks, correlation IDs/tracing, dashboards, automated remediation for known-safe fixes, and regular game days.
- **Hard/Scenario — A repeated incident takes 40 minutes to diagnose each time.** → Convert the diagnosis into a decision tree, add the missing metric/log/alert, automate the safe first steps, add a runbook link to the alert, and track MTTR after changes.

---

# PART 10 — IaC & DEVOPS ON AWS

## 10.1 AWS CloudFormation ★★★

**Definition:** CloudFormation is AWS's native Infrastructure as Code service: declarative templates that create and manage stacks of resources with dependency ordering and rollback.

**Important Points**
- **Template anatomy:** `AWSTemplateFormatVersion`, `Description`, `Parameters`, `Mappings`, `Conditions`, `Resources` (required), `Outputs`, `Metadata`, `Transform` (macros/SAM).
- **Stack operations:** create/update/delete, **change sets** (preview changes), **rollback on failure**, **drift detection**, stack policies, termination protection.
- **Nested stacks** and **cross-stack references** (`Export`/`ImportValue`) — exports are immutable while referenced.
- **StackSets** deploy one template across many accounts/Regions (Organizations integration) — the standard for baselines.
- **DeletionPolicy** (`Retain`/`Snapshot`/`Delete`), **UpdateReplacePolicy**, `DependsOn`, `CreationPolicy`/`UpdatePolicy` (ASG rolling updates), `WaitCondition`.
- **Custom resources** and **Lambda-backed resources** for gaps.
- **SAM** for serverless (transforms to CloudFormation); **CDK** synthesises CloudFormation from real programming languages (TypeScript/Python/Java/C#/Go).
- **Modules, Registry, Hooks** (verify), and **`cfn-lint`/`cfn-guard`** for policy checks.
- Use case: standardised VPC/account baseline as StackSets; app stacks per environment in pipelines.

**Edge Cases & Gotchas**
- Failed updates roll back, but resources created before failure can leave orphans depending on policies.
- Changing a property that requires replacement **deletes and recreates** the resource (data loss risk on RDS!). Read the change set for "Replacement: True".
- Exports cannot be modified/deleted while imported — cross-stack coupling causes deployment deadlocks.
- Stack drift means someone changed resources manually; reconcile, don't ignore.
- Large templates have size limits — use nested stacks or modules.
- Secrets in parameters appear in stack metadata/history — use Secrets Manager dynamic references (`{{resolve:secretsmanager:...}}`).
- Deleting a stack deletes everything it owns — termination protection and DeletionPolicy are mandatory in production.
- Rollback of a bad stack update can be slow (resource-by-resource); plan the change set carefully.

**Interview Questions**
- **Basic — What is a CloudFormation stack?** → A named collection of AWS resources managed together as a single unit from a template.
- **Medium — How do you avoid accidental data loss on update?** → Review change sets for replacement, set `DeletionPolicy: Snapshot/Retain` on stateful resources, use termination protection, keep databases in their own stack, and test in non-prod first.
- **Hard/Scenario — 60 accounts need a new guardrail (VPC flow logs + Config + a new SCP). How?** → StackSets with service-managed permissions at the Organization/OU level for the resources, an Organizations policy update for the SCP (via IaC provider or API), canary to a pilot OU, then percentage-based rollout with automatic rollback on failure.

## 10.2 Terraform on AWS ★★★

**Definition:** Terraform is an open-source/enterprise IaC tool using HCL and a state file to plan and apply changes across providers, including AWS.

**Important Points**
- **Core workflow:** `init` → `plan` → `apply`; `fmt`/`validate`/`lint` in CI.
- **State:** the source of truth mapping resources to real IDs; store remotely in **S3 + DynamoDB lock** (or Terraform Cloud) with encryption and versioning. **Never commit state** — it contains secrets.
- **Modules** for reuse (VPC, EKS, IAM baseline); registry modules + version pinning.
- **Workspaces** vs separate state per environment — separate state per env/account is safer.
- **Providers** (AWS, Kubernetes, Helm), provider version pinning, `data` sources for lookups.
- **Drift:** `terraform plan` in CI to detect out-of-band changes; `terraform state` commands for surgical fixes (use carefully).
- `import` for adopting existing resources; `moved` blocks to refactor without recreating; `prevent_destroy` lifecycle.
- **Terragrunt/Atlantis/Spacelift/Env0** for DRY multi-account orchestration and PR-based applies (know at least one).
- Secrets: never in `.tf`/tfvars committed to git; use `aws_secretsmanager_secret_version` data source or external secret injection at apply time (and remember they land in state).
- Use case: multi-account landing zone with per-env state buckets, modules, OIDC-authenticated CI applies.

**Edge Cases & Gotchas**
- **State locking** missing → concurrent applies corrupt state. Always use DynamoDB locking.
- State file contains plaintext secrets — bucket access must be restricted and audited.
- `terraform destroy` in production with no `prevent_destroy` = disaster.
- Import doesn't generate configuration — you must write matching config or the next plan destroys/replaces.
- Provider upgrades can change resource schemas; pin versions and read upgrade guides.
- Plan/apply drift between CI and laptop runs causes "it worked in the pipeline" mysteries — enforce pipeline-only applies.
- Circular dependencies between modules are a design smell.
- Long-lived access keys in CI are an anti-pattern — use OIDC federation to an IAM role.

**Interview Questions**
- **Basic — What is Terraform state and why does it matter?** → A mapping of declared resources to real infrastructure, needed to plan diffs; it must be remote, locked, encrypted and access-controlled.
- **Basic — What does `terraform plan` actually do?** → Refreshes state against real infrastructure, computes a diff against the desired configuration, and shows create/update/replace/destroy actions without changing anything.
- **Medium — How do you manage multiple environments?** → Separate state per account/environment, shared versioned modules, environment-specific tfvars/roots, and a pipeline with plan-on-PR and apply-on-merge.
- **Medium — Secrets always end up in Terraform state. How do you handle that?** → Assume state contains plaintext: encrypt the backend, restrict access tightly, avoid writing secrets from Terraform where possible (read at runtime from Secrets Manager/SSM by the app), mark variables sensitive, and rotate anything that was ever written to state.
- **Hard/Scenario — A colleague changed an SG in the console; Terraform now wants to revert it.** → Confirm the drift is intentional; if yes, update the code to match (or import/refresh), plan and apply so state is authoritative. Then prevent drift with SCPs/read-only console access for prod and a scheduled drift-detection pipeline.

**Production Troubleshooting — Terraform apply failures**
```bash
# 1. Who holds the state lock? (DynamoDB lock table)
aws dynamodb get-item --table-name terraform-locks \
  --key '{"LockID":{"S":"my-state-bucket/prod/terraform.tfstate"}}' --consistent-read

# 2. What does the plan actually want to change, and what is drift vs intended?
terraform plan -detailed-exitcode -out=tfplan   # 0 = no changes, 2 = changes, 1 = error
terraform show -json tfplan | jq '.resource_changes[] | select(.change.actions|index("delete") or index("replace")) | .address'

# 3. Which attributes force replacement? (prevents accidental data loss)
terraform plan | grep -E "must be replaced|forces replacement" -A2
```
Interpretation: `LockID` present with an old `Info` → a run died mid-apply; confirm no process is active, then `terraform force-unlock <id>` **after** checking the remote state is intact. Plan shows unexpected `replace` on stateful resources (RDS, EBS, EC2) → stop, add `lifecycle { prevent_destroy }`, and move the resource into its own state. Drift-only `update` actions → someone changed the console; decide policy-first (revert or codify), then apply.

## 10.3 CI/CD on AWS ★★★

**Definition:** A pipeline that builds, tests, scans, deploys and verifies application changes using AWS-native (CodeCommit/CodeBuild/CodeDeploy/CodePipeline) or third-party tools (GitHub Actions, GitLab CI, Jenkins).

**Important Points**
- **Stages:** source → build/test → security scan (SAST/SCA/container scan) → artifact store → deploy to dev → integration tests → approval → prod deploy (blue/green/canary) → smoke tests → notify.
- **CodeBuild:** buildspec phases (`install`, `pre_build`, `build`, `post_build`), artifacts, caching, VPC builds; CodeDeploy: EC2/ECS/Lambda deployment strategies (in-place, blue/green, canary, linear) with hooks and alarms; CodePipeline: stages/actions/approvals.
- **Artifact management:** versioned images in ECR (scan on push, immutable tags), build once/deploy everywhere.
- **Deployment strategies:** rolling, blue/green, canary with automatic rollback on CloudWatch alarm.
- **Auth for CI:** GitHub Actions OIDC → IAM role; no long-lived keys.
- **Environment promotion:** same artifact through envs; config via SSM/Secrets Manager/env vars.
- **IaC in the pipeline:** plan on PR, approval, apply on merge; separate pipeline for infrastructure.
- Use case: PR → tests + `terraform plan` → merge → build image → deploy dev → e2e → manual approval → canary 10% prod → auto-rollback on 5XX alarm.

**Edge Cases & Gotchas**
- Deploying different artifacts to different environments breaks reproducibility.
- No automated rollback = long MTTR; canary/blue-green with alarm-based rollback is the fix.
- Long-lived AWS keys in CI are a top breach vector — use OIDC.
- Pipelines that can't be re-run from any stage cause manual fumbling during incidents.
- Missing database migrations step causes deploy/runtime failures — version migrations and run them safely (expand/contract).
- Secrets leaked in build logs — mask variables and avoid `echo`.
- CodePipeline artifact buckets need encryption and restricted access.
- "It passed CI" ≠ tested; missing integration/e2e coverage shows up in prod.

**Interview Questions**
- **Basic — Blue/green vs canary?** → Blue/green switches all traffic to a new identical environment after validation; canary shifts a small percentage first and increases based on health.
- **Medium — How do you authenticate GitHub Actions to AWS securely?** → OIDC identity provider + IAM role trust restricted to the repo/branch, short-lived credentials, no static keys.
- **Hard/Scenario — A prod deploy causes a 5% error-rate increase that nobody notices for an hour.** → Add deployment-time alarms on 5XX/latency, canary/blue-green with automated rollback gates, smoke tests, and mandatory post-deploy observation windows. Also add deploy markers to dashboards so correlation is instant.

## 10.4 Containers & Registries — ECR ★★

**Definition:** ECR is a managed container image registry with scanning, replication and IAM-based access.

**Important Points**
- Private and public (ECR Public/Gallery) repositories; **image scanning** (basic vs enhanced/Inspector), **immutable tags**, lifecycle policies to expire untagged images.
- **Cross-Region/cross-account replication** for multi-Region deployments; **pull-through cache** for upstream registries (verify).
- Access from ECS/EKS/Lambda uses IAM; from outside AWS use a token (`aws ecr get-login-password`).
- Private access requires NAT or interface VPC endpoints (`ecr.api`, `ecr.dkr`, plus S3 gateway for layers).
- Image signing (Notation/Cosign via Signer — verify) and admission control in EKS.
- Use case: CI pushes immutable SHA-tagged images, EKS pulls via VPC endpoints, lifecycle expires old images.

**Edge Cases & Gotchas**
- ECR pulls through NAT are a top NAT cost driver — use endpoints.
- Untagged images accumulate cost — lifecycle policies are mandatory.
- Mutable tags (`latest`) break reproducibility and rollbacks.
- Cross-account pulls need repository policies and (for encrypted repos) KMS permissions.
- Scan-on-push basic scanning may miss OS-level CVEs unless enhanced scanning is enabled.

**Interview Questions**
- **Basic — How does EKS pull from a private ECR repo?** → Node/task IAM role with ECR permissions, ECR interface endpoints (or NAT), and image URIs; no docker login needed on EKS/ECS.
- **Medium — Why immutable tags?** → Guarantees the tag always points to the same image, enabling reliable rollbacks and audits.
- **Hard/Scenario — Deployments sometimes pull an old image.** → Mutable tags were reused. Enforce immutable tags, deploy by digest/SHA, and ensure the deployment spec references the new digest; verify with `describe-images` timestamps.

---

# PART 11 — DISASTER RECOVERY, RELIABILITY & COST

## 11.1 DR Strategies (Backup & Restore → Pilot Light → Warm Standby → Multi-Site) ★★★

**Definition:** Four DR patterns trading cost against RTO/RPO: Backup & Restore, Pilot Light, Warm Standby, Multi-Site (active-active).

**Important Points**

| Strategy | What runs in DR Region | RTO | RPO | Relative cost |
| --- | --- | --- | --- | --- |
| Backup & Restore | Nothing; restore from backups/snapshots | Hours | Hours (backup interval) | $ |
| Pilot Light | Core data replicated + minimal infra (VPC, IAM, DB replica) | Tens of minutes–hours | Minutes | $$ |
| Warm Standby | Scaled-down full stack always running | Minutes | Seconds–minutes | $$$ |
| Multi-Site active-active | Full capacity in 2+ Regions serving traffic | Near-zero (seconds) | Near-zero (sync/quasi-sync) | $$$$ |

- **Key enablers:** IaC to rebuild infrastructure, AMIs/images replicated, data replication (Aurora Global DB, DynamoDB Global Tables, S3 CRR, RDS cross-Region replicas), Route 53 failover/Global Accelerator, pre-raised quotas in DR Region.
- **RTO/RPO are business decisions** — get them in writing from stakeholders; the architecture follows.
- **Testing:** planned DR drills, `TestFailover`-style exercises, chaos engineering (FIS), and recording actual measured RTO.
- **Runbooks + ownership:** who declares a disaster, who runs the failover, how apps reconnect.
- Use case: regulated fintech → warm standby in `ap-south-2` with Aurora Global DB, Route 53 failover, pre-baked AMIs, quarterly drills.

**Edge Cases & Gotchas**
- Untested DR is fiction — quota limits, missing AMIs, IAM roles, ACM certs, and DNS records are the usual surprises.
- DR Region lacks service availability for a specific instance family or feature.
- Data replication lag > RPO means real data loss on unplanned failover.
- Cross-Region data transfer and duplicate capacity can double the bill — budget it explicitly.
- Secrets/KMS keys are Region-scoped; replicate keys and secrets.
- Failover works, failback may not — plan and test the return path.
- DNS TTL and client caching extend real RTO beyond the design on paper.

**Interview Questions**
- **Basic — What is pilot light?** → Minimal core infrastructure and replicated data run in the DR Region; you scale up the rest during failover.
- **Medium — Warm standby vs multi-site?** → Warm standby runs a scaled-down but complete stack and scales on failover; multi-site runs full capacity in multiple Regions with active traffic.
- **Hard/Scenario — RTO 15 minutes, RPO 5 minutes, for a 3-tier app. Which strategy and how do you prove it?** → Warm standby (or active-passive with hot DB replica): pre-provisioned capacity, Aurora Global DB / cross-Region replicas with lag alarms, Route 53 failover or Global Accelerator, IaC rebuild for edge cases, automated runbook. Prove with quarterly game days measuring actual RTO/RPO, and fix gaps found each time.

## 11.2 Reliability Patterns — Retries, Circuit Breakers, Idempotency, Bulkheads ★★★

**Definition:** Application-level resilience patterns that prevent partial failures from becoming outages.

**Important Points**
- **Timeout:** every network call needs one; no timeout = thread exhaustion.
- **Retry with exponential backoff + jitter:** retries transient errors only; cap attempts; avoid retrying non-idempotent calls blindly.
- **Circuit breaker:** after N failures, fail fast for a cooldown, then half-open probe.
- **Bulkhead:** isolate pools/threads/connections per dependency so one slow dependency doesn't consume all capacity.
- **Idempotency keys:** safe retries for payments/orders; store processed keys with TTL.
- **Graceful degradation:** serve cached/stale data, disable non-critical features, queue instead of failing.
- **Backpressure & load shedding:** bounded queues, 429/503 with Retry-After, admission control.
- **Chaos engineering:** inject latency/failure in a controlled way to validate.
- AWS specifics: SDK retry modes (`standard`/`adaptive`), DynamoDB conditional writes for idempotency, SQS DLQ, ALB/Route 53 health checks, Aurora/RDS retry logic.
- Use case: payment service with idempotency keys, circuit breakers per PSP, and bounded thread pools per downstream.

**Edge Cases & Gotchas**
- Retry storms amplify outages (all clients retry simultaneously) — jitter is not optional.
- Retrying non-idempotent POSTs creates duplicate charges/orders.
- Retry + no circuit breaker + no timeout = cascading failure.
- Health checks that depend on downstream services cause mass unhealthy states during a downstream blip.
- Deep dependency chains multiply availability: 5 services at 99.9% ≈ 99.5% combined.

**Interview Questions**
- **Basic — Why is idempotency important?** → Distributed systems retry; idempotent handlers guarantee a retried request doesn't create duplicate side effects.
- **Medium — What does a circuit breaker protect?** → The caller and the failing dependency from overload — it fails fast and recovers gradually instead of piling up requests.
- **Hard/Scenario — One slow downstream service takes the whole API down.** → Add per-dependency timeouts and bulkheads, circuit breakers to fail fast, caching/fallback responses, and async processing where possible. Then load-test to prove isolation.

## 11.3 AWS Cost Optimization ★★★

**Definition:** A continuous practice of matching spend to business value: right-sizing, pricing models, storage lifecycle, architecture efficiency, and visibility/governance.

**Important Points**
- **Visibility:** Cost Explorer, Cost and Usage Report (CUR) → Athena/QuickSight, **Cost Anomaly Detection**, **Budgets with alerts**, tagging strategy (env, owner, cost-centre, project), Cost Categories, **Application/Account-Based Cost Reporting (ABP)** for shared costs.
- **Compute:** right-sizing (Compute Optimizer), Savings Plans/RIs for baseline, Spot for fault-tolerant, Graviton, autoscaling, scheduled shutdown of non-prod, containerisation density, Lambda memory tuning (AWS Lambda Power Tuning).
- **Storage:** S3 lifecycle/Intelligent-Tiering, delete incomplete MPUs/old snapshots/AMIs, gp2→gp3, EBS right-sizing, snapshot retention via DLM/AWS Backup policies, EFS IA lifecycle.
- **Network:** NAT Gateway data processing, cross-AZ traffic, inter-Region transfer, CloudFront/endpoints to avoid egress, VPC endpoints instead of NAT.
- **Observability:** log retention, sampling, metric cardinality, third-party per-host pricing.
- **Common hidden costs:** idle load balancers, unattached EIPs/volumes, old AMIs/snapshots, dev environments running 24/7, non-prod NAT, unoptimised data transfer, CloudWatch logs never expiring.
- **Governance:** SCPs restricting expensive instance families/Regions, budgets enforced by automation, tagging policies via Config/Tag Policies.
- Use case: FinOps review reducing 30% by right-sizing + Savings Plans + S3 lifecycle + shutting down non-prod nights/weekends.

**Edge Cases & Gotchas**
- Cost optimization can break reliability if you cut capacity without headroom — always keep N+1 and test.
- Savings Plans are commitments: buying against a shrinking baseline wastes money.
- Deleting "unused" resources without checking ownership causes incidents — trace via CloudTrail/tags first.
- Data transfer is often underestimated: cross-AZ chatter, NAT, egress to internet.
- Aggressive log retention removal can breach compliance.
- Showback without accountability produces no behaviour change — pair with owners and targets.

**Interview Questions**
- **Basic — Name three quick cost wins.** → Right-size/or stop idle resources, delete unattached EBS/EIPs and old snapshots, move eligible workloads to Spot/Savings Plans and S3 to lifecycle classes.
- **Medium — How do you attribute costs in a multi-account org?** → Accounts per workload/env + tagging standards + Cost Categories + CUR/Athena + ABP for shared costs + monthly showback per team.
- **Hard/Scenario — The bill grew 40% in a month with no traffic change.** → Cost Explorer by service/Region/account, then Cost Anomaly Detection and CUR queries; check for data transfer (NAT/cross-AZ), new log volumes, snapshot growth, an autoscaling loop, a forgotten DR Region, and KMS/observability request spikes. Fix, then add budgets/alarms and a guardrail.

## 11.4 Tagging, FinOps & Governance ★★

**Definition:** A tagging and governance framework makes cost, ownership, compliance and automation possible across accounts.

**Important Points**
- Required tags: `Environment`, `Owner`, `CostCenter`, `Project/Application`, `DataClassification`, `ManagedBy` (terraform/cfn).
- Enforce with **Tag Policies** (Organizations), **Config rules** (`required-tags`), **SCPs** denying creation without tags (via `aws:RequestTag` conditions), and auto-tagging in IaC modules.
- Distinguish **cost allocation tags** (activated in billing) from resource tags; activation is not retroactive for historical reports.
- **Resource Groups / Resource Groups Tagging API** for grouping; tag-based automation (stop non-prod at night).
- **AWS Backup** tag-based policies; **DLM** for snapshots.
- Use case: SCP requires `Environment` and `Owner` on EC2/RDS/S3; a Lambda tags untagged resources and notifies owners.

**Interview Questions**
- **Basic — Difference between a tag and a cost allocation tag?** → All tags exist on resources; only tags activated as cost allocation tags appear in billing/Cost Explorer.
- **Medium — How do you enforce tagging?** → Tag policies + Config required-tags rules + SCP deny on create without required tags + IaC modules that always set them; report compliance weekly.
- **Hard/Scenario — Finance cannot allocate 25% of the bill.** → Identify untaggable/shared services (NAT, TGW, support, shared logging), allocate via ABP or a documented split model, backfill tags, and enforce going forward. Never chase perfect attribution for shared infrastructure — define a defensible allocation rule.

---

## 11.5 AWS Backup & Restore Testing ★★★

**Definition:** AWS Backup centralises backup policies, vaults, retention and cross-Region/cross-account copies across many services, and can verify restores.

**Important Points**
- **Supported resources:** EBS, EC2, RDS/Aurora, DynamoDB, EFS, FSx, S3 (where supported), Storage Gateway, DocumentDB/Neptune, and more (verify per service/Region).
- **Components:** backup **plan** (schedule + lifecycle + copy actions) → **vault** (with **vault lock** in compliance mode for WORM) → **backup selection** (tags or resources) → **jobs** → **recovery points**.
- **Cross-Region and cross-account copies** are first-class: copy to a DR Region and to a **separate security account** so a compromised production account cannot delete backups.
- **Vault Lock (compliance mode)** makes recovery points immutable for a retention period — the answer to ransomware and insider deletion. Governance mode is reversible by privileged users; compliance mode is not.
- **Legal hold** freezes recovery points independent of retention.
- **Restore testing** (where supported) automates periodic restores and validates them — the difference between "we have backups" and "we can recover".
- **Audit Manager / Backup Audit Manager** produce compliance reports (backup frequency, retention, minimum retention, cross-Region copy).
- Point-in-time recovery (RDS/DynamoDB/Aurora continuous backup) complements snapshot-based plans; choose by RPO.
- Use case: tag-based plan covering all production resources, nightly snapshots with 35-day retention, monthly copies to a DR Region, quarterly copies to a security account with vault lock, and a monthly automated restore test.

**Edge Cases & Gotchas**
- **A successful backup job is not proof of recoverability** — untested restores routinely fail on missing IAM roles, KMS key permissions in the DR account, or capacity.
- Cross-account copies require the vault's access policy, KMS key policy and, for encrypted resources, a key usable in the destination account.
- Vault Lock in compliance mode cannot be undone — plan retention carefully; you will pay for the retention you locked in.
- Backup frequency defines RPO; a daily backup means up to 24 hours of data loss. Say the number out loud when asked about RPO.
- S3 backup coverage and semantics differ from replication (versioning + replication is often the better S3 DR mechanism — verify current capabilities).
- Some services require specific resource configurations (e.g., encryption keys, cluster state) for a restore to be usable.
- Backups do not protect against logical corruption that occurs before the snapshot — you need multiple recovery points plus PITR where available.

**Interview Questions**
- **Basic — What does AWS Backup add over per-service snapshots?** → Central policies, cross-service coverage, cross-Region and cross-account copies, vault lock, and audit reporting in one place.
- **Medium — How do you protect backups from ransomware or an insider in the production account?** → Copy to a separate security account with restricted access, enable Vault Lock in compliance mode, use least-privilege KMS keys that production cannot delete, enable MFA delete on the vault's S3 backing where applicable, and monitor with CloudTrail/GuardDuty.
- **Hard/Scenario — Prove you can recover a production RDS instance to 4 hours ago in a DR Region.** → Restore a recovery point or PITR into the DR Region, verify KMS key access in the target account, bring up the app against it, validate data integrity and connection strings, and record the measured time. Automate this as a scheduled restore test so the answer is evidence, not opinion.

## 11.6 Cross-Account Automation, Conformance Packs & Audit Trails ★★

**Definition:** The tooling that makes a multi-account estate consistent and auditable: StackSets, Organizations policies, Config conformance packs/aggregators, and centralised logs.

**Important Points**
- **CloudFormation StackSets** with Organizations integration deploy one template across accounts/OUs/Regions. Use **service-managed permissions**, **canary deployments** to a pilot OU, and **automatic deployment** for new accounts.
- **Config conformance packs** bundle Config rules + remediation into a deployable YAML template; **organization conformance packs** apply to every account in the Organization and report compliance centrally.
- **Config aggregators** (single account or organization aggregator) give one compliance view across accounts/Regions; **advanced queries** answer questions like "which RDS instances are public?" across the estate.
- **Centralised logging:** an Organizations CloudTrail trail to a log-archive account with S3 Object Lock, plus central CloudWatch Logs and VPC flow logs. Protect the trail with an SCP that denies `StopLogging`/`DeleteTrail`.
- **Incident audit trail pattern:** every automated remediation writes to CloudTrail + a ticket; every human break-glass action is via a PIM-like/assumed role with session logging; retain evidence per the compliance period.
- **EventBridge cross-account** rules route findings (GuardDuty, Security Hub, Config) to a central responder account that runs SSM Automation.
- Use case: an SCP blocks public S3; Config conformance pack detects drift; EventBridge triggers an SSM Automation document that remediates and logs; Security Hub tracks the finding to closure.

**Edge Cases & Gotchas**
- StackSets fail partially — one account's quota/permission error leaves an OU inconsistent; use failure tolerance and operation preferences deliberately.
- Conformance packs evaluate periodically and can lag; they do not prevent deployment (that is Policy-as-code/SCPs + pre-deploy checks).
- Remediation runbooks need permissions in **every** target account — an over-scoped automation role is a bigger risk than the finding.
- Aggregators only see accounts/Regions that are authorised; a missing Region is a blind spot, not "compliant".
- Log-archive accounts need their own guardrails: if an attacker can delete the trail and the bucket, your audit trail is gone.
- Evidence must be exportable for auditors — automate a scheduled export, not a scramble at audit time.

**Interview Questions**
- **Basic — What is a Config conformance pack?** → A packaged set of Config rules (and optional remediation) deployed as a unit to assess a defined compliance framework.
- **Medium — How do you keep 50 accounts consistent after a new guardrail is approved?** → SCP where the control is a permission boundary; StackSets for resources; organization conformance packs for detection; canary to a pilot OU; automated remediation; and a compliance dashboard from the aggregator.
- **Hard/Scenario — An auditor asks for proof that no production S3 bucket was public last quarter.** → Show organisation-wide CloudTrail (object/bucket policy changes), Config history for `s3-bucket-public-read-prohibited` with timestamps, Security Hub findings and remediation records, plus the SCP that prevents it. Point out that Config history + CloudTrail is the evidence chain, and restore-test/backup logs cover the data side.

---

# PART 12 — PRODUCTION TROUBLESHOOTING PLAYBOOKS (15 SCENARIOS)

> **How to answer any of these in an interview (60–90 seconds):**
> 1. **30-second diagnosis framework** — the layers you would check, in order, and *why that order*.
> 2. **Three first commands** — the evidence you would gather before touching anything.
> 3. **Likely root cause** — stated as a hypothesis with the evidence that confirms it.
> 4. **Safe mitigation** — restore service without destroying the evidence or making it worse.
> 5. **Permanent fix** — the change that prevents recurrence (guardrail, alarm, automation, design).
>
> Never start with "I'd restart it". Start with "I'd prove which layer is failing."

## 12.1 EC2 is running but SSH/SSM access fails

- **Framework:** Is the instance healthy (AWS-side or guest-side)? → Is there a network path (SG/NACL/route/peering)? → Is the OS accepting (sshd listening, firewall, disk full, fstab)? → Is access configured (key pair, IAM role for SSM, agent)?
- **First commands:** `aws ec2 describe-instance-status --include-all-instances --instance-ids i-xxx` · `aws ec2 create-network-insights-path … / start-network-insights-analysis` · `aws ssm describe-instance-information` (is it a managed node?)
- **Root cause:** `SystemStatus=ok` + `InstanceStatus=impaired` → guest OS (full disk, broken `/etc/fstab`, kernel panic, sshd down). All green but no flow-log entries → network path (SG removed, NACL change, route gone, or a new peering). Instance missing from SSM → no instance profile or no route to SSM endpoints.
- **Safe mitigation:** use **serial console** or **SSM Run Command** to fix the guest (do not terminate yet — you lose the evidence); restore the SG rule/route via change control; if the host is degraded, stop/start (same instance ID) or replace via ASG.
- **Permanent fix:** no inbound 22 at all — SSM Session Manager with logging; user-data/AMI health checks that fail loudly; alarms on `StatusCheckFailed_Instance` and disk usage; immutable images so a broken box is replaced, not nursed.

## 12.2 Private EC2 cannot reach the internet

- **Framework:** route (`0.0.0.0/0` to NAT?) → NAT gateway placement/health (public subnet, IGW route, EIP) → SG egress → NACL (inbound ephemeral!) → DNS resolution → is it an *internet* destination or an AWS API call that should use an endpoint?
- **First commands:** `aws ec2 describe-route-tables --filters Name=vpc-id,Values=vpc-x` · `aws ec2 create-network-insights-path --source i-xxx --destination 8.8.8.8 --protocol tcp --destination-port 443` + `start-network-insights-analysis` · `aws logs filter-log-events --log-group-name /aws/vpc/flowlogs --filter-pattern REJECT`
- **Root cause:** most often a missing/incorrect NAT route, a NAT gateway in a subnet without an IGW route, or an egress SG/NACL change. With private-link-friendly designs, the "internet" destination is actually an AWS API that should go through an endpoint.
- **Safe mitigation:** restore the route or SG rule; if NAT is impaired, fail over to the NAT gateway in another AZ (or add one); never open the instance to the internet as a fix.
- **Permanent fix:** per-AZ NAT, S3/DynamoDB gateway endpoints plus interface endpoints for the APIs actually used, alarms on NAT `ErrorPortAllocation`/throughput, and a route-table conformance check in CI/IaC.

## 12.3 ALB returns intermittent 502 / 503 / 504

- **Framework:** 503 = no healthy targets (health check, registration, SG, capacity) · 502 = target returned an invalid response/reset (app crash, protocol mismatch, header too large) · 504 = target exceeded the idle/response timeout (slow app, DB, or timeout mismatch).
- **First commands:** `aws elbv2 describe-target-health --target-group-arn <tg>` (read the **reason code**) · query `UnHealthyHostCount`, `TargetResponseTime`, `HTTPCode_Target_5XX_Count` · read ALB access logs filtered by `error_reason`.
- **Root cause:** flapping health checks during deployments; deregistration delay shorter than slow requests; app keep-alive shorter than the ALB idle timeout; one bad target in a group; connection pool exhaustion in the app.
- **Safe mitigation:** remove/drain the bad target, extend deregistration delay, align idle/keep-alive timeouts, increase capacity or roll back the last deployment.
- **Permanent fix:** health-check path that proves readiness (not a static page), slow start, rolling/blue-green deploys with alarms and auto-rollback, timeout budget agreed between ALB → app → DB, and a `5XX > threshold` alarm wired to the deploy pipeline gate.

## 12.4 ASG does not launch instances during peak traffic

- **Framework:** is the alarm/scale-out action correct? → is the ASG blocked (max size, suspended processes, cooldown/warmup)? → account limits (vCPU quotas)? → capacity/placement (AZ capacity, subnet IPs)? → launch template errors (AMI, instance type, key pair, SG, IAM/PassRole)?
- **First commands:** `aws autoscaling describe-scaling-activities --auto-scaling-group-name asg --max-items 10` · `aws service-quotas get-service-quota …` + `aws ec2 describe-subnets` (free IPs) · `aws cloudwatch describe-alarms --alarm-name-prefix …`
- **Root cause:** `StatusCode=Failed` with `VcpuLimitExceeded` or an instance-type/AZ capacity error is the usual answer; otherwise the policy never triggered (metric not in ALARM, cooldown, max capacity).
- **Safe mitigation:** raise max capacity/cooldown, request quota increase, spread across more instance types/AZs (mixed instances policy), free subnet IPs — then verify with a load test.
- **Permanent fix:** pre-raised quotas for peak + DR Regions, target tracking on a **leading** metric (requests per target, queue depth), warm pools or pre-scaling for known events, and an alarm on `GroupInServiceInstances` vs desired.

## 12.5 Cross-VPC connectivity fails through Transit Gateway

- **Framework:** attachment state → TGW route table association → prefix propagation into the right table → **VPC** route table pointing at the TGW → overlapping CIDRs → SG/NACL → appliance mode/asymmetry if inspecting.
- **First commands:** `aws ec2 describe-transit-gateway-attachments` · `aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id tgw-rtb-x --filters Name=state,Values=active` · `aws ec2 describe-route-tables` for the source subnet, plus `PacketDropCountBlackhole` metrics.
- **Root cause:** the two classic mistakes — the attachment is associated with a route table that lacks the peer's prefix, or the destination VPC has no return route to the TGW. Overlapping CIDRs and a missing `Allow` SG rule are next.
- **Safe mitigation:** add the missing propagation/route; isolate to the affected segment route table; avoid changing the shared table during an incident.
- **Permanent fix:** explicit per-segment route tables, IaC-managed routes with drift detection, TGW flow logs enabled, blackhole alarms, and a connectivity test suite (Reachability Analyzer paths) run after every network change.

## 12.6 S3 returns AccessDenied despite an IAM Allow

- **Framework:** which principal? → identity policy → **bucket policy explicit deny** → SCP/boundary/session policy → **KMS key policy (`kms:Decrypt`)** → VPC endpoint policy → Object Ownership/ACL → wrong bucket/Region/ARN.
- **First commands:** `aws sts get-caller-identity` · `aws iam simulate-principal-policy --policy-source-arn … --action-names s3:GetObject --resource-arns …` · `aws cloudtrail lookup-events` for the `errorCode`/`errorMessage`, plus `aws s3api get-bucket-policy`/`get-public-access-block`.
- **Root cause:** encrypted object without `kms:Decrypt` on the correct key; a bucket policy deny (often `aws:SecureTransport` or a VPC-endpoint condition the client doesn't satisfy); a restriction on a role the app isn't actually using.
- **Safe mitigation:** grant the narrow missing permission (KMS decrypt on that key, or fix the condition), or route the request through the required VPC endpoint.
- **Permanent fix:** least-privilege policies as code, Access Analyzer validation in CI, `simulate-principal-policy` in the pipeline for critical paths, and alarms on spikes of `AccessDenied` in CloudTrail.

## 12.7 RDS CPU reaches 95% and application latency increases

- **Framework:** is it the database or the application waiting on it? → CPU vs IOPS vs connections vs locks → top SQL (Performance Insights) → recent change (deploy, index, traffic, parameter group) → read/write split and replica lag.
- **First commands:** Performance Insights top wait events / top SQL · `aws cloudwatch get-metric-statistics` for `CPUUtilization`, `DatabaseConnections`, `ReadIOPS`/`WriteIOPS`, `ReplicaLag` · `aws rds describe-events --source-identifier db --duration 1440`.
- **Root cause:** missing index or a plan regression after a deploy; connection storm from a new autoscaling event; long transactions/locks; a reporting query moved onto the primary; an undersized instance for current IOPS.
- **Safe mitigation:** kill/limit the offending query or session, add the missing index in a low-traffic window, route reporting to a replica, raise instance class/IOPS as a temporary measure, scale out the app with backoff.
- **Permanent fix:** Performance Insights alarms, connection pooling/RDS Proxy, query review in CI (plan checks), read replicas with routing discipline, and capacity headroom sized from p95 not average.

## 12.8 EKS pods remain Pending or in ImagePullBackOff

- **Framework:** `Pending` → scheduling (CPU/memory requests, taints/affinity, topology spread, PVC zone, **subnet IP exhaustion with VPC CNI**). `ImagePullBackOff` → image name/tag, registry auth (IRSA/node role `ecr:GetAuthorizationToken`+`BatchGetImage`), network path to ECR (NAT or endpoints), image platform (arm64 vs amd64).
- **First commands:** `kubectl describe pod <pod>` (read `Events` and `Status.Reason`) · `kubectl get nodes -o wide` + `describe node` for allocatable/taints · `aws ec2 describe-subnets` for free IPs + `kubectl logs -n kube-system -l k8s-app=aws-node`.
- **Root cause:** requests too large for remaining allocatable capacity; a PVC bound to another AZ; subnet CIDR exhaustion (`failed to assign an IP address`); missing IRSA trust for the registry; architecture mismatch (Graviton nodes, x86 image).
- **Safe mitigation:** right-size requests, add capacity/node pool in the right AZ, free IPs (terminate stale pods, add secondary CIDR/prefix delegation), fix the image digest/arch, restore the role's ECR permissions.
- **Permanent fix:** planned subnet sizing or CNI custom networking/prefix delegation, PodDisruptionBudgets and topology spread, admission policies that require resource requests, image scanning/signing, and alarms on `ipamd` IP availability and pending pods.

## 12.9 Terraform apply fails on state locking or drift

- **Framework:** who holds the lock and is the process alive? → is the remote state intact? → what does the plan actually change (drift vs intended)? → did someone change the console?
- **First commands:** `aws dynamodb get-item --table-name terraform-locks --key '{"LockID":{"S":"…"}}' --consistent-read` · `terraform plan -detailed-exitcode` · `terraform show -json tfplan | jq '.resource_changes[]'` filtered to replace/delete.
- **Root cause:** a killed CI job leaving a stale lock; manual console changes (drift); a provider/schema change forcing replacement; a workspace/backend pointed at the wrong state.
- **Safe mitigation:** confirm no active run, then `terraform force-unlock`; for drift, decide to codify or revert — never apply a plan containing an unexpected `replace` on stateful resources.
- **Permanent fix:** pipeline-only applies with a single concurrency lock per environment, `prevent_destroy` on stateful resources and separate state for them, scheduled drift detection, and backend state with versioning + restricted write access.

## 12.10 A deployment causes a production outage

- **Framework:** correlate the error onset with the deploy marker → was it the code, config, schema, or infrastructure? → is rollback safe (backward-compatible schema?) → blast radius (all traffic or a subset)?
- **First commands:** check deploy marker on dashboards/alarms and the ALB `5xx` rate · `aws elbv2 describe-target-health` · application logs/APM around the deploy timestamp, plus the pipeline's last changeset.
- **Root cause:** a schema migration incompatible with the previous version; a config/secret change; capacity reduction; a failed canary that passed because health checks were shallow.
- **Safe mitigation:** roll back the artifact (slot swap back / previous task definition / previous image digest) or shift traffic to the previous version; if the DB changed, roll forward with a compatibility patch rather than reverting data.
- **Permanent fix:** expand/contract migrations, blue-green or canary with automatic rollback on alarms, deploy markers on dashboards, feature flags, and a post-incident action item that adds the missing test.

## 12.11 CloudWatch alarms are not triggering correctly

- **Framework:** is the metric publishing (namespace, dimensions, Region)? → is the alarm state history showing evaluation at all? → threshold/statistic/period logic → missing-data treatment → is someone suppressing it (alert processing/suppression, SNS filter, action group limits)?
- **First commands:** `aws cloudwatch describe-alarm-history --alarm-name <name> --history-item-type StateUpdate` · `aws cloudwatch get-metric-statistics --namespace … --metric-name … --dimensions …` · `aws cloudwatch get-metric-data` for the exact expression, plus SNS/action-group delivery logs.
- **Root cause:** wrong dimension (e.g., `TargetGroup` vs `LoadBalancer`), alerting on `Average` when spikes are short, `InsufficientData` treated as OK, memory/disk metrics that require the CloudWatch agent, or a notification layer that dropped the message.
- **Safe mitigation:** fix the dimension/statistic and re-test with a synthetic breach; for missing guest metrics, deploy the agent; check SNS subscriptions and endpoint health.
- **Permanent fix:** alarm-as-code with tests, alarms on `InsufficientData`, composite alarms to cut noise, periodic alert drills, and a runbook link embedded in every alarm description.

## 12.12 The AWS bill unexpectedly increases by 40%

- **Framework:** which service/meter/account/Region grew? → new workload or a change in behaviour? → data transfer vs requests vs storage → orphaned/idle resources → commitments/expiry.
- **First commands:** Cost Explorer grouped by service → then by usage type and account · `aws ce get-cost-and-usage` for the month vs prior · Cost Anomaly Detection / CUR query in Athena for the top usage type.
- **Root cause:** NAT Gateway data processing (ECR pulls, cross-AZ chatter), forgotten non-prod/DR capacity, snapshots/versions never expiring, KMS/request charges from a new feature, an autoscaling loop, or a Savings Plan/RI expiring.
- **Safe mitigation:** stop the bleeding first (fix the loop, delete orphaned volumes/IPs, expire broken lifecycle), then optimise deliberately — never delete resources you cannot attribute to an owner.
- **Permanent fix:** budgets + anomaly alerts, mandatory cost-allocation tags enforced by policy, Storage Lens/lifecycle for S3, endpoint adoption for NAT-heavy paths, monthly FinOps review with owners.

## 12.13 A production AZ fails and applications must recover

- **Framework:** is the failure really AZ-scoped? → are all tiers spread (compute, DB, cache, NAT, endpoints, load balancer subnets)? → is the control plane degraded (DNS/API) or only data plane? → what is the single-AZ dependency?
- **First commands:** `aws ec2 describe-instance-status` filtered by AZ + ASG/AZ health · CloudWatch `UnHealthyHostCount` per AZ and ALB `HealthyHostCount` per target AZ · RDS events + Multi-AZ state.
- **Root cause:** one dependency pinned to the failed AZ — a NAT gateway, a single ElastiCache node, an MSK broker, an EFS mount target, a zone-pinned EBS volume, or an ASG that never rebalanced.
- **Safe mitigation:** remove the failed AZ's targets from rotation, let the ASG replace instances, fail the DB over (Multi-AZ does this automatically), and shift traffic to healthy AZs.
- **Permanent fix:** 3-AZ designs for every tier, per-AZ NAT/endpoints, zone-aware autoscaling, and quarterly AZ-failure game days that prove recovery time.

## 12.14 A cross-Region DR failover is required

- **Framework:** declare the disaster and RTO clock → is the DR Region's data caught up (RPO)? → is infrastructure and identity present (IaC, AMIs, KMS, certs, quotas)? → is DNS/traffic ready to switch? → can the app start with its dependencies?
- **First commands:** check replication (`aws rds describe-db-instances --query 'DBInstances[].ReadReplicaSourceDBInstanceIdentifier'`, Aurora Global DB status, `ReplicaLag`) · `aws ec2 describe-images --owners self --region <dr>` + quota checks · Route 53/Global Accelerator health and record state.
- **Root cause:** the DR Region usually fails on a missing dependency — KMS key or secrets not replicated, AMI absent, quota not raised, IAM roles missing, or data behind RPO.
- **Safe mitigation:** promote the database, start the pre-built/IaC stack, switch the routing policy, validate a smoke transaction, then communicate RTO/RPO achieved.
- **Permanent fix:** DR as code that is deployed continuously, quarterly failover drills with measured RTO, replication-lag alarms, pre-raised quotas, and a written failback procedure.

## 12.15 A compromised IAM access key is detected

- **Framework:** contain → determine scope → assess impact → revoke → rebuild → prevent. Never "rotate and hope".
- **First commands:** `aws iam update-access-key --access-key-id AKIA… --status Inactive` · `aws cloudtrail lookup-events --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIA…` (or Athena over the org trail) · `aws iam generate-credential-report` / Access Analyzer to find other standing credentials.
- **Root cause:** long-lived keys in code/CI or a leaked `.env`/log; the exposure path matters as much as the key.
- **Safe mitigation:** deactivate (not delete) the key, revoke sessions for the associated role/user, isolate resources it touched (e.g., change an SG to quarantine), snapshot evidence, and notify security per policy.
- **Permanent fix:** eliminate long-lived keys — roles for workloads, OIDC federation for CI, Secrets Manager for third parties; MFA + `aws:MultiFactorAuthPresent` conditions; GuardDuty + CloudTrail anomaly alarms; GitHub secret scanning and pre-commit hooks; quarterly credential reviews.

---

---

# PART 13 — SENIOR SCENARIO DRILLS (60–90 second verbal set)

> Cover the answer, say it out loud in 60–90 seconds, then compare. These mirror the "production scenarios" section of your original notes but with deeper expected answers.

**1. EC2 in a private subnet cannot reach the internet.**
Route table → NAT Gateway (public subnet, IGW route, EIP) → SG outbound → NACL both directions → DNS → missing/more-specific route. Use Reachability Analyzer + flow logs to prove which hop drops it.

**2. One AZ fails and the app goes down despite "Multi-AZ".**
Check whether all instances/ENIs/NAT/DB really span AZs; ALB subnets per AZ; ASG AZ balance; RDS Multi-AZ; NAT per AZ; and whether a hard dependency (ElastiCache node, MSK broker, a single-AZ EFS mount target) is single-AZ.

**3. RDS primary fails mid-transaction.**
Multi-AZ failover moves the standby to primary; existing connections drop and DNS updates — the app must retry/reconnect. Data committed pre-failure survives; uncommitted transactions roll back. Verify `ReplicaLag`, RDS events, app retry logic, and whether the app uses a proxy.

**4. IAM allows S3 access but requests get AccessDenied.**
SCP → permissions boundary → session policy → bucket policy explicit deny → KMS key policy (`kms:Decrypt`) → VPC endpoint policy → wrong ARN/Region → wrong role being used. CloudTrail `AccessDenied` events name the denying policy type.

**5. DynamoDB throttles despite high provisioned capacity.**
Hot partition/hot key, GSI capacity mismatch (backpressure to the table), on-demand per-table limits, burst absorption exhausted, or a scan-heavy access pattern. Contributor Insights identifies the key; shard, cache, or rekey.

**6. ALB 503 during a deployment.**
No healthy targets: readiness checks, grace periods, deregistration delay, target registration timing, SG rules, app startup time. Fix with health-check-based gating, slow start and rolling deployments.

**7. Lambda times out calling RDS at peak.**
Connection exhaustion (use RDS Proxy), VPC/NAT issues, connection setup cost outside the handler, low memory (CPU scales with memory), and downstream saturation. Cache connections in a global scope.

**8. EKS pods Pending after scaling.**
Subnet IP exhaustion, ENI/max-pods limits, insufficient allocatable CPU/memory, taints/affinity, PVC scheduling (EBS is AZ-scoped!), and cluster autoscaler not matching instance types.

**9. A developer's leaked access key is found in Git.**
Immediate deactivation/rotation, CloudTrail review of key usage, IAM Access Analyzer, revoke sessions (`sts`/console), assess what was accessed, notify security, enable GitHub secret scanning + pre-commit hooks, move to OIDC/roles.

**10. S3 costs doubled this month.**
Request volume (LIST storms, small-object churn), KMS request charges, incomplete multipart uploads, noncurrent versions, wrong storage class for access pattern, replication of cold data, and log-bucket growth. Storage Lens + Inventory + Cost Explorer by usage type.

**11. A multi-account Organization wants centralized egress with inspection.**
Shared-services/inspection VPC, TGW segmented route tables, Network Firewall per AZ, spokes with default route to TGW, appliance mode for symmetry, central logs, and an allow-list model. Roll out canary-first.

**12. Terraform wants to destroy a production RDS instance.**
Change set/plan shows replacement (e.g., changed identifier or engine property). Never apply blind: `lifecycle { prevent_destroy }`, state inspection, restore from snapshot if it already happened, and separate stateful resources into their own stack.

**13. Cross-Region DR drill reveals the secondary Region cannot launch the app.**
Quotas not raised, AMIs/images not replicated, IAM roles/KMS keys/secrets missing, ACM certs not present, SG rules referencing missing resources, instance family unavailable, and DNS not switched. Codify the DR environment in IaC and drill quarterly.

**14. A public S3 bucket leaked data.**
Contain (Block Public Access), remove the policy, rotate credentials if exposed, use Access Analyzer/CloudTrail/S3 access logs to scope, notify per policy, add Config rules + SCP + automated remediation.

**15. The NAT Gateway bill is larger than the compute bill.**
ECR pulls, S3/DynamoDB traffic, cross-AZ calls, and log shipping through NAT. Add gateway/interface endpoints, cache images, co-locate chatty services, and review egress patterns.

---

# PART 14 — RAPID REVISION

## 14.1 One-line differences you must not fumble

| Question | Sharp answer |
| --- | --- |
| SG vs NACL | SG = stateful, ENI-level, allow-only, all rules apply. NACL = stateless, subnet-level, allow+deny, numbered order |
| ALB vs NLB | L7 vs L4; ALB path/host routing; NLB static IPs, ultra-low latency, TCP/UDP |
| ALB vs API Gateway | ALB is a load balancer with basic L7 routing; API Gateway adds auth, throttling, usage plans, caching, stages |
| CloudFront vs Global Accelerator | Caching CDN (HTTP) vs network-path acceleration with static anycast IPs (TCP/UDP) |
| VPC peering vs TGW | 1:1 non-transitive vs hub with centralised routing/segmentation |
| Gateway vs interface endpoint | Free, route-table, S3/DynamoDB only vs ENI + SG + PrivateLink, hourly cost |
| IGW vs NAT | Bidirectional for public IPs vs outbound-only SNAT with EIP |
| Multi-AZ vs Read Replica | Sync HA failover vs async readable scaling |
| Aurora vs RDS | Distributed 6-copy storage + fast failover + Global DB vs simpler managed relational |
| DynamoDB GSI vs LSI | Different PK, eventually consistent, add anytime vs same PK, can be strongly consistent, create-time only |
| SQS vs SNS vs EventBridge vs Kinesis | Queue vs pub/sub vs content-routing bus vs ordered replayable stream |
| EBS vs EFS vs S3 | Block/one AZ vs NFS/multi-AZ vs object/regional |
| Spot vs On-Demand | Spare capacity, 2-min interruption, up to ~90% cheaper vs guaranteed but full price |
| Secrets Manager vs Parameter Store | Rotation + versioning + cross-account vs cheaper hierarchical config |
| CloudTrail vs CloudWatch vs Config | API audit trail vs metrics/logs/alarms vs configuration history/compliance |
| GuardDuty vs Inspector vs Macie | Threat detection vs vulnerability scanning vs sensitive-data discovery |
| User vs Role | Long-term identity credentials vs temporary assumed credentials |
| SCP vs IAM policy vs boundary | Max permissions filter vs granted permissions vs cap on granted permissions |
| Blue/green vs canary | Full switch after validation vs gradual percentage shift |
| RTO vs RPO | Time to restore vs acceptable data loss |

## 14.2 Numbers worth memorising (verify before quoting)

| Item | Value |
| --- | --- |
| S3 durability | 11 nines |
| S3 object max size / single PUT | 5 TB / 5 GB (multipart above) |
| DynamoDB item size | 400 KB |
| Lambda max timeout / memory | 15 min / up to 10 GB |
| Lambda default concurrency | 1,000 per Region |
| API Gateway integration timeout | 29 s |
| SQS message size / retention | 256 KB / 4 days default, 14 max |
| SNS/SQS max message | 256 KB |
| EBS gp3 baseline | 3,000 IOPS, 125 MiB/s |
| VPC IPv4 reserved per subnet | 5 |
| ALB idle timeout default | 60 s |
| ALB/NLB deregistration delay default | 300 s |
| RDS automated backup retention | 1–35 days |
| CloudTrail Event history | 90 days |
| ACM CloudFront cert Region | us-east-1 |
| RDS failover | Typically ~60–120 s (varies) |
| NAT Gateway cost model | Hourly + per GB processed |
| KMS key deletion window | 7–30 days |

## 14.3 Final 60-second self-test

1. Draw a 3-AZ VPC with a public ALB, private app tier, Multi-AZ DB, NAT per AZ, S3 endpoint — with routes and SGs.
2. Explain an AccessDenied for encrypted cross-account S3 in under 60 s.
3. Choose a database for 10k TPS order writes plus BI reporting, and defend it.
4. Explain Multi-AZ vs read replicas vs Aurora Global DB in one breath each.
5. Name the four DR strategies with RTO/RPO/cost.
6. List the checks for "ASG not scaling".
7. List the checks for "ALB 503".
8. List five cost leaks you would hunt for on day one.
9. Explain warm standby vs pilot light with a real example.
10. Explain how you would prove a security finding was remediated.

## 14.4 Command cheat sheet — what to run, and what "good" looks like

> Copy these into your lab. In an interview, naming the command **and** the expected output is what proves hands-on experience.

| Question you are answering | Command | What a healthy result looks like |
| --- | --- | --- |
| Who am I / which role? | `aws sts get-caller-identity` | Expected account + assumed-role ARN, not a user with a static key |
| Is the instance healthy? | `aws ec2 describe-instance-status --include-all-instances` | `SystemStatus: ok` and `InstanceStatus: ok` |
| Why is traffic blocked? | `aws ec2 start-network-insights-analysis` (Reachability Analyzer) | `NetworkPathFound: true`; on failure, a named blocking component (SG/NACL/route) |
| What traffic hit the ENI? | VPC flow logs in CloudWatch Logs Insights | `ACCEPT` for expected flows; `REJECT` pinpoints the blocking layer |
| Why is a target unhealthy? | `aws elbv2 describe-target-health --target-group-arn …` | `State: healthy`; otherwise read `Reason` (`Target.Timeout`, `ResponseCodeMismatch`) |
| Is the ASG being blocked? | `aws autoscaling describe-scaling-activities` | `StatusCode: Successful`; a `Failed` event names the quota/capacity cause |
| Do I have quota left? | `aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A` | Used < quota, with headroom for peak |
| Are subnet IPs available? | `aws ec2 describe-subnets --query 'Subnets[].[SubnetId,AvailableIpAddressCount]'` | Hundreds free in app subnets; low double digits is a warning |
| Is my IAM allow effective? | `aws iam simulate-principal-policy …` | `allowed`; `implicitDeny`/`explicitDeny` tells you which layer blocked it |
| Who changed it? | `aws cloudtrail lookup-events --lookup-attributes …` | An event with `userIdentity`, `sourceIPAddress`, `eventTime` you can attribute |
| Is the DB the bottleneck? | Performance Insights top waits + `DatabaseConnections`, `ReplicaLag` | CPU < 70%, connections below class limit, replica lag near zero |
| Are pods schedulable? | `kubectl describe pod` → `Events`, `kubectl describe node` → allocatable | `Scheduled` and `Running`; `FailedScheduling` names the constraint |
| Why can't it pull the image? | `kubectl describe pod` → `Failed to pull image`, `aws ec2 describe-subnets` | Image digest resolves, IPs available, `AcrPull`/ECR permissions present |
| Is Terraform safe to apply? | `terraform plan -detailed-exitcode` (0/2/1) | 0 = no drift; 2 = intended changes only, no unexpected `replace` |
| Is the cache healthy? | ElastiCache `Evictions`, `CacheMissRate`, `CurrConnections` | Evictions ~0, miss rate stable, connections below node limit |
| Will the alarm fire? | `aws cloudwatch describe-alarm-history --history-item-type StateUpdate` | A prior `OK → ALARM` transition proves the rule works |
| What is costing money? | Cost Explorer grouped by usage type + CUR in Athena | Top usage types attributed to a tagged owner |
| Can I actually recover? | AWS Backup restore test / `aws rds restore-db-instance-to-point-in-time` | A restored instance you connected to and validated, with measured time |


> **Verification note:** re-check current quotas, limits, supported features and pricing in the AWS documentation and Service Quotas console before interviews or production design. New capabilities (Pod Identity, Karpenter maturity, KMS/ACM features, new instance families) evolve quickly.

---

**Sources to keep open:** AWS Documentation (docs.aws.amazon.com) · AWS Well-Architected Framework · AWS Prescriptive Guidance (DR, multi-account) · Service Quotas console · AWS Pricing Calculator · This Is My Architecture videos.
