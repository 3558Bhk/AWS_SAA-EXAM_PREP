# Task 2.2 — Design Highly Available and/or Fault-Tolerant Architectures

> This task is about **surviving failure**: of an instance, an Availability Zone, a Region, or a dependency. You must be able to map a stated **RTO/RPO and budget** to the right architecture, and to spot single points of failure in a described design.

---

# 1. Core Definitions

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

# 2. Identifying and Removing Single Points of Failure

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

# 3. Compute and Infrastructure Resilience

## 3.1 Multi-AZ with Auto Scaling and ELB

The foundational HA pattern:
- An **ALB/NLB** with subnets in at least two (preferably three) AZs
- An **Auto Scaling group** whose subnets span those AZs, with `min` at least equal to the number of AZs so the loss of one AZ leaves capacity
- **`HealthCheckType = ELB`** so application-level failures cause replacement
- Enough headroom (the **"N+1" rule**) that losing one AZ's capacity doesn't overload the rest — with three AZs you need ~50% spare per AZ to survive one AZ loss without degradation

## 3.2 Instance-level recovery

- **EC2 Auto Recovery** — a CloudWatch alarm on `StatusCheckFailed_System` triggers recovery, which migrates the instance to new underlying hardware **keeping the same instance ID, private IP, Elastic IP, and EBS volumes**. Useful for single-instance legacy workloads that cannot be clustered. (Modern instance types have this built in by default.)
- **ASG replacement** — the ASG terminates and launches a fresh instance; the IP changes, so the workload must be stateless or behind a load balancer.
- **EC2 hibernation** preserves RAM state to the root EBS volume — a cost/startup optimization rather than an HA feature.

## 3.3 Placement groups

| Strategy | Behaviour | Effect on resilience |
|---|---|---|
| **Cluster** | Packs instances close together in **one AZ** for lowest latency and highest throughput | **Reduces** resilience — one AZ, correlated hardware |
| **Spread** | Places each instance on **distinct underlying hardware** (racks); max **7 instances per AZ per group** | **Maximizes** resilience for a small set of critical instances |
| **Partition** | Divides instances into partitions, each on a separate rack set; up to 7 partitions per AZ | For large distributed systems (HDFS, Cassandra, Kafka) that are rack-aware |

## 3.4 Immutable infrastructure and deployments

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

# 4. Data Resilience

## 4.1 Amazon S3

- **99.999999999% durability** and data stored redundantly across **at least three AZs** (except **One Zone-IA** and **Express One Zone**, which use a single AZ).
- **Strong read-after-write consistency** for all operations.
- **Versioning** protects against overwrite and deletion (a delete creates a delete marker).
- **Replication** — SRR and CRR — for DR, latency, and compliance. Requires versioning on both ends; **only replicates objects written after it is enabled** (use **Batch Replication** for existing objects); **RTC** provides a 15-minute SLA.
- **Object Lock** for immutability; **MFA Delete** for extra protection.

## 4.2 Amazon EBS

- An EBS volume is **replicated within a single Availability Zone only**. It is not multi-AZ. If the AZ fails, the volume is unavailable.
- Resilience comes from **snapshots**, which are incremental and stored durably (in S3, in an AWS-managed account), and can be **copied cross-Region and cross-account**.
- Automate with **Amazon Data Lifecycle Manager** or **AWS Backup**; speed up restores with **Fast Snapshot Restore**; protect against accidental deletion with **Recycle Bin**.

## 4.3 Amazon RDS

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

## 4.4 Amazon Aurora

- The storage layer keeps **six copies of your data across three Availability Zones** and is self-healing (continuously scanning for and repairing errors). Aurora can tolerate the loss of **two copies without affecting writes** and **three copies without affecting reads**.
- Storage grows automatically in 10 GB increments up to **128 TiB** and is shared by all instances in the cluster.
- Up to **15 Aurora Replicas**, replica lag typically **under 10 ms**. On primary failure Aurora **fails over to a replica, usually in under 30 seconds**, using failover priority tiers. With no replica, Aurora recreates the primary (slower).
- **Endpoints:** writer (cluster) endpoint, **reader endpoint** (load-balances across replicas), custom endpoints, and instance endpoints.
- **Aurora Global Database** — one primary Region plus up to **five secondary Regions**, replicated at the storage layer with typical lag **under one second**. Provides **RPO ≈ 1 second and RTO under 1 minute** for cross-Region failover, plus local low-latency reads. This is the standard answer for global relational DR.
- **Backtrack** (Aurora MySQL) rewinds the cluster in place to a prior point in seconds, without restoring a snapshot — excellent for undoing a bad deployment or an accidental `DELETE`.
- **Fast database cloning** creates a copy-on-write clone in minutes for testing.

## 4.5 Amazon DynamoDB

- Data is automatically replicated across **three Availability Zones** in a Region; there is no "enable Multi-AZ" option.
- **Global tables** provide multi-Region, **multi-active** replication with last-writer-wins conflict resolution — read and write in any Region, with typically sub-second replication.
- **Point-in-time recovery** gives continuous backups with restore to any second in the last **35 days**; **on-demand backups** are retained until deleted.
- **DynamoDB Streams** can feed cross-Region or cross-system replication and event-driven recovery logic.

## 4.6 EFS and FSx

- **EFS Standard** stores data redundantly across multiple AZs in the Region; **EFS One Zone** is cheaper but single-AZ. **EFS Replication** maintains a cross-Region copy with an RPO measured in minutes.
- **FSx for Windows File Server** offers a **Multi-AZ** deployment with automatic failover; **FSx for Lustre** persists durability by linking to an S3 bucket as the system of record (scratch file systems are explicitly non-replicated).

---

# 5. Route 53, Health Checks and Failover

## 5.1 Health checks

Route 53 supports three types:
- **Endpoint health checks** — Route 53 checkers around the world probe an IP or domain over HTTP/HTTPS/TCP, optionally matching a string in the response body.
- **Calculated health checks** — combine multiple child checks with AND/OR/NOT logic ("healthy if at least 2 of 3 children are healthy").
- **CloudWatch alarm health checks** — treat an alarm state as health, which lets you base DNS failover on any metric (including private resources Route 53 cannot reach directly).

Health checks can also send **SNS notifications** and are what make failover routing work.

## 5.2 Routing policies

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

## 5.3 Alias records and TTL

- **Alias records** point to AWS resources (ALB/NLB, CloudFront, S3 website endpoints, API Gateway, Global Accelerator, another Route 53 record). They are **free to query**, can be used at the **zone apex** (`example.com`), and automatically track the target's IP changes. A **CNAME cannot be used at the zone apex**.
- **TTL** governs how long resolvers cache a record. Lower TTLs (60 seconds or less) make DNS failover faster but increase query volume. Note that many clients and some JVMs cache DNS beyond the TTL, which is exactly why **Global Accelerator** (which fails over at the network layer) is preferred when seconds matter.

## 5.4 Global Accelerator vs CloudFront for availability

- **Global Accelerator** provides two **static anycast IPs**, routes traffic into the AWS backbone at the nearest edge, continuously health-checks endpoints, and **fails over within seconds without any DNS change**. It supports **TCP and UDP** and any protocol. Use it for gaming, VoIP, IoT, financial feeds, or when clients cache DNS.
- **CloudFront** is an HTTP/S CDN. It improves availability by caching (serving from cache during origin problems), supports **origin groups** for automatic origin failover, and absorbs DDoS at the edge.

---

# 6. Disaster Recovery Strategies

The four strategies, in increasing cost and decreasing RTO/RPO:

| Strategy | RPO | RTO | What is running in the DR Region | Relative cost |
|---|---|---|---|---|
| **Backup & restore** | Hours | **Hours to a day** | Nothing but backups/snapshots | **$** |
| **Pilot light** | Minutes | **Tens of minutes** | Core data continuously replicated (e.g., a database replica); servers configured but **switched off / not provisioned** | **$$** |
| **Warm standby** | Seconds–minutes | **Minutes** | A **fully functional but scaled-down** copy of the whole stack, always running | **$$$** |
| **Multi-site active/active** | Near zero | **Near zero** | Full production capacity live in both Regions, serving traffic | **$$$$** |

## 6.1 Backup and restore
Take regular backups (AWS Backup, snapshots, S3 CRR) and copy them to the DR Region. After a disaster, rebuild infrastructure from **infrastructure as code** and restore data. Cheapest, slowest. Suitable for non-critical workloads and for the long tail of systems.

## 6.2 Pilot light
The "always-on" part is the **data**: a cross-Region read replica, DynamoDB global table, or continuously replicated storage. Application servers exist as AMIs/templates but are not running. On failover you scale up compute, promote the database, and repoint DNS. Significantly faster than restore, much cheaper than warm standby.

## 6.3 Warm standby
A complete, smaller copy of production runs continuously in the DR Region — perhaps one instance per tier rather than ten. It can serve traffic immediately (possibly degraded) and is scaled up during failover. The key advantage over pilot light is that the system is already *proven working*.

## 6.4 Multi-site active/active
Both Regions serve live traffic (Route 53 latency or weighted routing, or Global Accelerator). Requires multi-Region data strategies such as **DynamoDB global tables** or **Aurora Global Database** (with write forwarding) and careful handling of conflicts, idempotency, and consistency. Highest cost and complexity, near-zero RTO/RPO.

## 6.5 Supporting services

- **AWS Elastic Disaster Recovery (AWS DRS)** — continuous **block-level replication** of on-premises or cloud servers into a low-cost staging area in AWS; launches fully provisioned instances on failover. RPO in **seconds**, RTO in **minutes**. The answer for "replicate physical/virtual servers for DR without re-architecting."
- **AWS Backup** — cross-Region and cross-account copies, Vault Lock, organization policies.
- **AWS Application Migration Service (MGN)** — the equivalent tool for migrations.
- **CloudFormation / CDK / Terraform** — recreate the environment deterministically, which is what makes backup-and-restore and pilot light viable.
- **AWS Resilience Hub** — assess an application against defined RTO/RPO targets, score it, and get remediation recommendations.
- **AWS Fault Injection Service (FIS)** — run controlled chaos experiments (terminate instances, inject latency, fail an AZ) to validate that the design really is resilient.

## 6.6 The service-quota trap
Service quotas are **per account, per Region**. A DR Region that has never run production may have **default limits** far below what a failover requires — EC2 vCPU limits, Elastic IPs, NAT gateways, RDS instances. **Raise quotas in the DR Region in advance** and periodically test. This is a favourite exam detail.

---

# 7. Resilience Patterns

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

# 8. Making Legacy and Unmodifiable Applications Resilient

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

# 9. Observability for Resilience

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

# 10. Worked Scenarios

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

# 11. Quick Decision Table

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
