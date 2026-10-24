# SAA-C03 Exam-Day Cheat Sheet

> Read this the night before and the morning of. Nothing new — only what gets tested repeatedly.

---

## 1. The 20 Highest-Yield Rules

1. **Explicit Deny always wins.** Default is implicit deny. Cross-account needs allow on BOTH sides.
2. **Roles, never access keys.** EC2 → instance profile. Lambda → execution role. Third party → role + **ExternalId**.
3. **SCPs limit, they never grant.** They don't affect the management account or service-linked roles.
4. **Security groups:** stateful, allow-only, instance level, can reference other SGs. **NACLs:** stateless, allow+deny, subnet level, numbered, need ephemeral ports.
5. **Multi-AZ = availability. Read replicas = performance.**
6. **S3 and DynamoDB use free gateway endpoints**; everything else uses interface endpoints (PrivateLink).
7. **CloudFront = HTTP caching. Global Accelerator = static anycast IPs, TCP/UDP, instant failover.**
8. **SQS = decouple/buffer. SNS = fan-out. EventBridge = routing/filtering + SaaS. Kinesis = ordered, replayable streams.**
9. **Encryption at rest can't be added in place** to RDS/EBS → snapshot → copy with encryption → restore.
10. **ACM certs for CloudFront must live in us-east-1**; public ACM certs cannot be exported to EC2.
11. **Aurora = 6 copies / 3 AZs, 15 replicas, Global DB ≈ 1 s RPO.**
12. **DynamoDB:** 1 WCU = 1 KB write/s; 1 RCU = 4 KB strongly consistent read/s (or 8 KB eventually consistent).
13. **Lambda:** 15 min max, 128 MB–10 GB memory (CPU scales with memory), 1,000 default concurrency.
14. **Spot = interruptible (2-min warning, 90% off). Savings Plans = flexible commitment (66–72% off).**
15. **S3 minimums:** IA 30 d, Glacier IR/Flexible 90 d, Deep Archive 180 d; 128 KB minimum billable object in IA.
16. **Inbound data transfer is free; cross-AZ, cross-Region, and internet egress are charged.**
17. **NAT Gateway = one per AZ for HA** (hourly + per-GB); replace with VPC endpoints where possible.
18. **GuardDuty = threat detection. Macie = PII in S3. Inspector = CVEs. Security Hub = aggregation. Config = compliance. CloudTrail = who did what.**
19. **IAM Identity Center = workforce SSO across accounts. Cognito = app/customer identities.**
20. **"Least operational overhead" = pick the managed/serverless option.**

---

## 2. Service Picker — One Line Each

**Compute:** EC2 (full control) · Lambda (event, <15 min) · Fargate (containers, no servers) · ECS (AWS-native orchestration) · EKS (Kubernetes) · Batch (queued jobs) · EMR (Spark/Hadoop) · Outposts (on-prem).

**Storage:** S3 (object) · EBS (block, 1 AZ) · Instance store (ephemeral, fastest) · EFS (NFS, Linux, multi-AZ) · FSx Windows (SMB/AD) · FSx Lustre (HPC + S3) · Storage Gateway (hybrid) · Snowball (offline bulk) · DataSync (online sync).

**Database:** RDS (managed relational) · Aurora (high-perf relational) · Aurora Serverless v2 (variable) · DynamoDB (key-value, ms) · DAX (µs cache for DDB) · ElastiCache (µs cache/session) · MemoryDB (durable Redis) · DocumentDB (Mongo) · Keyspaces (Cassandra) · Neptune (graph) · Timestream (time series) · QLDB (ledger) · Redshift (warehouse) · OpenSearch (search/logs).

**Networking:** VPC · IGW/NAT · SG/NACL · Peering (2 VPCs) · TGW (many VPCs, transitive) · PrivateLink (expose one service) · DX (private, high bw) · VPN (quick, encrypted) · Route 53 (DNS + routing policies) · CloudFront · Global Accelerator · ALB/NLB/GWLB.

**Integration:** SQS · SNS · EventBridge · Step Functions · API Gateway · AppSync · Amazon MQ · Kinesis/Firehose/Flink · MSK.

**Security:** IAM · Identity Center · Cognito · Organizations/SCP · Control Tower · KMS · CloudHSM · Secrets Manager · ACM · WAF · Shield · Network Firewall · Firewall Manager · GuardDuty · Macie · Inspector · Security Hub · Detective · Artifact · Audit Manager.

**Analytics:** Athena · Glue (ETL + catalog) · DataBrew · Lake Formation · EMR · QuickSight · Redshift · Data Exchange.

**Management:** CloudWatch · CloudTrail · Config · Systems Manager · Trusted Advisor · Compute Optimizer · Cost Explorer · Budgets · CUR · AWS Backup · Resilience Hub · X-Ray.

---

## 3. Numbers to Memorize

| Item | Value |
|---|---|
| S3 object max | 5 TB (5 GB single PUT, multipart above) |
| S3 request rate | 3,500 writes / 5,500 reads per second **per prefix** |
| S3 durability | 11 nines; Standard availability 99.99% |
| Subnet reserved IPs | 5 per subnet |
| VPC CIDR range | /16 to /28 |
| SQS message size / retention | 256 KB / 14 days max (default 4 days) |
| SQS visibility timeout | 30 s default, 12 h max |
| SQS long polling | up to 20 s |
| SQS FIFO throughput | 300 TPS (3,000 batched); high-throughput mode much higher |
| Kinesis shard | 1 MB/s or 1,000 rec/s in; 2 MB/s out |
| Kinesis retention | 24 h default → 365 days |
| Lambda | 15 min, 10 GB memory, 10 GB /tmp, 1,000 concurrency default |
| API Gateway timeout | 29 seconds (integration) |
| KMS direct encrypt limit | 4 KB (use envelope encryption above) |
| KMS key deletion wait | 7–30 days |
| RDS backup retention | 0–35 days, PITR ~5 min |
| RDS read replicas | 5 (RDS) / 15 (Aurora) |
| Aurora storage | 6 copies, 3 AZs, up to 128 TiB |
| DynamoDB item size | 400 KB; PITR 35 days |
| EBS gp3 | 3,000 IOPS / 125 MB/s baseline, up to 16,000 IOPS |
| EBS io2 Block Express | up to 256,000 IOPS, 64 TiB |
| Spot interruption notice | 2 minutes |
| STS session | 1 h default, up to 12 h (role chaining capped at 1 h) |
| Route 53 multivalue | up to 8 healthy records |
| Direct Connect | 50 Mbps – 100 Gbps |
| VPN tunnel | ~1.25 Gbps per tunnel, 2 tunnels per connection |

---

## 4. Instant Scenario → Answer

| Keyword in question | Answer |
|---|---|
| "decouple", "buffer spikes", "absorb load" | **SQS** |
| "notify multiple systems", "fan-out" | **SNS** (→ SQS queues) |
| "exactly once", "strict order" | **SQS FIFO** |
| "replay", "multiple consumers of a stream" | **Kinesis Data Streams** |
| "no servers", "pay per request", "sporadic" | **Lambda / Fargate / on-demand** |
| "orchestrate steps with retries / approval" | **Step Functions** |
| "global users", "reduce latency", "cache static" | **CloudFront** |
| "static IP", "UDP", "fast failover" | **Global Accelerator** |
| "lowest latency Region" | **Route 53 latency routing** |
| "comply with country rules" | **Route 53 geolocation routing** |
| "shared file system for Linux" | **EFS** |
| "Windows file share with AD" | **FSx for Windows** |
| "HPC file system" | **FSx for Lustre** |
| "unknown access patterns" | **S3 Intelligent-Tiering** |
| "archive, hours to retrieve, cheapest" | **Glacier Deep Archive** |
| "WORM / immutable / cannot be deleted" | **S3 Object Lock compliance mode** |
| "find PII" | **Macie** |
| "detect compromised instance / malicious IP" | **GuardDuty** |
| "CVEs / patch vulnerabilities" | **Inspector** |
| "who deleted it" | **CloudTrail** |
| "configuration compliance / drift" | **AWS Config** |
| "SQL injection / XSS" | **WAF** |
| "large DDoS, 24/7 support, cost protection" | **Shield Advanced** |
| "no inbound ports, no SSH keys, admin access" | **SSM Session Manager** |
| "rotate DB credentials automatically" | **Secrets Manager** |
| "too many DB connections from Lambda" | **RDS Proxy** |
| "microsecond reads" | **ElastiCache / DAX** |
| "cross-Region DB DR, RPO ~1 s" | **Aurora Global Database** |
| "multi-Region active-active NoSQL" | **DynamoDB global tables** |
| "petabyte BI analytics" | **Redshift** |
| "ad-hoc SQL on S3" | **Athena** |
| "CSV to Parquet, serverless ETL" | **Glue** |
| "stream to S3 with no admin" | **Firehose** |
| "migrate DB with minimal downtime" | **DMS (+ SCT if heterogeneous)** |
| "move 100 TB+, limited bandwidth" | **Snowball Edge** |
| "scheduled on-prem → AWS file sync" | **DataSync** |
| "many VPCs, transitive routing" | **Transit Gateway** |
| "overlapping CIDRs, expose one service" | **PrivateLink** |
| "private access to S3 from private subnet" | **Gateway VPC endpoint** |
| "reduce NAT data processing cost" | **VPC endpoints** |
| "steady 3-year workload" | **Savings Plans / RIs** |
| "interruptible batch" | **Spot** |
| "BYOL core-based licensing" | **Dedicated Hosts** |
| "centralize multi-account setup securely" | **Control Tower** |
| "centralize backups across accounts" | **AWS Backup** |
| "consistent WAF rules org-wide" | **Firewall Manager** |

---

## 5. Last 60 Seconds Before You Start
- Time budget: **2 minutes per question**. At question 33 you should have ~65 minutes left.
- Flag anything that takes longer than 2 minutes; there is a review screen.
- Multiple-response questions tell you how many to pick — count them.
- When two answers both "work", pick the one matching the stated optimization (cost / overhead / latency / security).
- Trust your first instinct on IAM and VPC questions; overthinking usually moves you to the wrong answer.

Good luck — you've got this.
