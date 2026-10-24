# Task 4.2 — Design Cost-Optimized Compute Solutions

> Compute is usually the largest line on an AWS bill. Four levers produce nearly all the savings: **the right purchasing model**, **the right size**, **the right amount of running time**, and **the right compute service**. The exam tests all four.

---

# 1. EC2 Purchasing Options

## 1.1 The full set

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

## 1.2 Savings Plans in detail

| Type | Flexibility | Discount |
|---|---|---|
| **Compute Savings Plans** | **Maximum** — applies across **EC2 (any instance family, size, OS, tenancy, Region)**, **Fargate**, and **Lambda** | Up to **66%** |
| **EC2 Instance Savings Plans** | Locked to an **instance family in a Region**, but flexible on size, OS, and AZ | Up to **72%** |
| **SageMaker Savings Plans** | SageMaker usage | Up to 64% |

You commit to spending a given **dollar amount per hour** for 1 or 3 years. Usage up to that amount is billed at the discounted rate; usage beyond it is billed On-Demand. Payment options: **All Upfront** (biggest discount) > **Partial Upfront** > **No Upfront**.

**Savings Plans vs Reserved Instances:** Savings Plans are simpler and more flexible and are generally the modern recommendation. RIs retain two advantages: **Standard RIs can be sold on the Reserved Instance Marketplace**, and **zonal RIs provide a capacity reservation**. RIs are still the only commitment model for **RDS, Redshift, ElastiCache, OpenSearch, and DynamoDB** — Savings Plans do not cover those services.

**RI types:** **Standard** (up to 72%, can change AZ/size within a family, **can be sold**) and **Convertible** (up to 66%, can be **exchanged** for a different family/OS/tenancy, cannot be sold). **Scope:** *regional* RIs give AZ flexibility and instance-size flexibility within a family; *zonal* RIs give a capacity reservation in one AZ but no flexibility.

**Organization-wide:** with **consolidated billing**, unused RI and Savings Plan benefits are **shared across all accounts** in the organization by default (can be disabled per account). This is a significant and frequently tested cost advantage of AWS Organizations.

## 1.3 Spot Instances in depth

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

## 1.4 Choosing the purchasing model

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

# 2. Rightsizing and Elasticity

## 2.1 Rightsizing

Over-provisioning is the most common source of waste. Typical findings: instances averaging 5% CPU, volumes four times larger than needed, and Lambda functions with 3 GB of memory doing trivial work.

- **AWS Compute Optimizer** analyzes CloudWatch metrics and recommends specific instance types/sizes for **EC2, Auto Scaling groups, EBS volumes, Lambda functions, ECS on Fargate, and RDS**, including projected savings and performance risk.
- **Cost Explorer rightsizing recommendations** identify idle and underutilized instances.
- **Trusted Advisor** flags **low-utilization EC2 instances, idle load balancers, unassociated Elastic IPs, underutilized EBS volumes, and idle RDS instances**.
- Remember that memory is **not** a default CloudWatch metric — install the **CloudWatch agent** so rightsizing decisions account for memory.
- Moving down one instance size halves the cost; moving to a newer generation usually improves price/performance at no effort.

## 2.2 Turn things off

- **Non-production environments running 24/7** are a classic waste. Dev/test used 40 hours a week costs 76% less if stopped outside those hours. Automate with **EventBridge Scheduler + Lambda**, **Systems Manager Automation**, **Instance Scheduler on AWS**, or ASG **scheduled scaling to zero**.
- Stopped EC2 instances cost nothing for compute, but **EBS volumes and Elastic IPs still bill**.
- Terminate orphaned resources: unattached volumes, old snapshots, unused load balancers, idle NAT gateways, unused Elastic IPs, forgotten dev stacks. **AWS Config rules** and tagging-based cleanup automation enforce this.

## 2.3 Auto Scaling as a cost control

Auto Scaling is as much a cost tool as a performance tool — **scaling in** is where the savings are.

- Set a realistic **minimum** so you aren't paying for idle headroom.
- Use **target tracking** on the metric that actually drives load so the fleet shrinks promptly.
- **Scheduled scaling** for predictable patterns (scale to 2 at night, 20 at 9 a.m.).
- **Predictive scaling** avoids over-provisioning "just in case."
- **Mixed instances with Spot** cuts the marginal cost of each additional instance.
- Watch **cooldowns** — overly long cooldowns delay scale-in and cost money.

## 2.4 Graviton

Moving to **AWS Graviton (ARM)** instances typically yields **up to 40% better price/performance** with lower energy use. Available for EC2, Lambda (`arm64`), Fargate, RDS, Aurora, ElastiCache, OpenSearch, EMR, and more. Interpreted and JIT languages usually need only a redeploy; compiled code needs recompiling. Combine Graviton with a Savings Plan and the savings stack.

---

# 3. Choosing a Cheaper Compute Model

## 3.1 Serverless vs always-on

Lambda and Fargate charge only while code runs. For **intermittent, spiky, or low-duty-cycle** workloads this is dramatically cheaper than an always-on EC2 instance — a function invoked 100,000 times a month for 200 ms each may cost cents, where the smallest EC2 instance costs several dollars.

The crossover point matters: at **sustained high utilization**, EC2 (especially with Savings Plans or Spot) becomes cheaper per unit of compute than Lambda. The exam usually frames it clearly — "runs a few times per hour" → serverless; "runs continuously at 70% CPU" → EC2 with a commitment.

## 3.2 Lambda cost model and tuning

Cost = **(GB-seconds) × price + per-request charge** (plus ephemeral storage above 512 MB and provisioned concurrency if enabled).

- Because **CPU scales with memory**, raising memory often **lowers** total cost: a function taking 10 s at 512 MB might take 2 s at 1,024 MB — half the GB-seconds and five times faster. Use **AWS Lambda Power Tuning** to find the optimum empirically.
- Use **`arm64` (Graviton)** for ~20% lower price per GB-second.
- Trim deployment packages and move initialization outside the handler so warm invocations reuse it.
- **Provisioned concurrency costs money even when idle** — use it only where cold-start latency genuinely matters, and auto-scale it on a schedule.
- Avoid functions that **sleep or poll** waiting on something; use Step Functions `Wait` states or event-driven triggers instead of paying for idle execution time.
- Batch records (SQS/Kinesis batch size) to reduce invocation count.

## 3.3 Containers

- **Fargate** removes instance management and bills per vCPU-second/GB-second with a 1-minute minimum — cheaper for bursty or low-density workloads, and it avoids paying for unused EC2 capacity.
- **ECS/EKS on EC2** is cheaper at high, steady utilization because you can **bin-pack** many tasks onto each instance and use **Spot** and Savings Plans. The trade-off is that you manage, patch, and scale the instances.
- **Fargate Spot** gives up to 70% off for interruption-tolerant tasks.
- **Right-size task CPU/memory requests** — over-requesting wastes cluster capacity invisibly.
- **Karpenter** (EKS) provisions right-sized nodes just-in-time and consolidates workloads onto fewer nodes, often producing large savings versus the Cluster Autoscaler.
- Use **Graviton** task/node architectures.

## 3.4 Managed services instead of self-managed

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

## 3.5 Batch and HPC

- **AWS Batch** with a **Spot** compute environment and array jobs is the canonical answer for "run thousands of restartable jobs as cheaply as possible."
- **EMR** with **task nodes on Spot** and **transient clusters** (terminate when the job finishes, with data in S3 via EMRFS) avoids paying for idle clusters.
- Queue-driven worker fleets on Spot, scaled on queue depth, scale to zero when idle.

---

# 4. Licensing Costs

- **License Included** AMIs (Windows, SQL Server) bundle the license into the hourly rate — simple, no compliance overhead, good for variable usage.
- **BYOL** on **Dedicated Hosts** is usually cheaper for large, steady Windows/Oracle/SQL Server estates licensed per physical core, and gives visibility of sockets and cores for compliance.
- **AWS License Manager** tracks license usage against entitlements across accounts and can block launches that would breach a limit.
- Consider **open-source alternatives**: migrating SQL Server → **Aurora PostgreSQL with Babelfish**, or Oracle → Aurora via **SCT + DMS**, eliminates licence fees entirely. The **Windows → Linux** move for .NET Core applications is another standard saving.
- **Optimize CPU options** — reduce the number of vCPUs on an instance (keeping the memory) when licensing is **per core**, so you pay for fewer licensed cores while retaining a large memory footprint.

---

# 5. Governance: Keeping Costs Down Over Time

- **Tagging strategy** — mandatory tags (`CostCenter`, `Project`, `Environment`, `Owner`) enforced by **tag policies** (Organizations), **SCPs**, or **AWS Config rules**, and **activated as cost allocation tags** in the Billing console (only effective from activation onward).
- **Cost Categories** group accounts, tags, and services into business dimensions for reporting.
- **AWS Budgets with Budget Actions** can automatically apply a restrictive IAM policy, stop EC2/RDS instances, or attach an SCP when a threshold is breached.
- **SCPs** can restrict expensive resources — for example, deny launching instance families larger than a set size, deny Regions you don't operate in, or deny creating Dedicated Hosts.
- **Service Catalog** publishes pre-approved, right-sized, tagged product templates so teams can self-serve without over-provisioning.
- **Cost Anomaly Detection** for unexpected spikes; **Compute Optimizer** reviewed monthly; **Trusted Advisor** checks acted on regularly.
- **Consolidated billing** for volume discounts and shared commitment benefits.
- **Showback/chargeback** with the CUR in Athena/QuickSight, or **AWS Billing Conductor** for custom rates.

---

# 6. Worked Scenarios

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

# 7. Quick Decision Table

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
