# Task 3.2 — Design High-Performing and Elastic Compute Solutions

> Two skills are tested here: **choosing the right compute service and instance type for a workload**, and **making that compute scale correctly** (on the right metric, at the right speed, with the right elasticity).

---

# 1. EC2 Instance Families

## 1.1 Reading an instance name

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

## 1.2 The families

| Family | Prefixes | Optimized for | Representative workloads |
|---|---|---|---|
| **General purpose** | **T** (burstable), **M**, Mac | Balanced CPU : memory (roughly 1 vCPU : 4 GiB) | Web servers, small/medium databases, microservices, dev/test, code repositories |
| **Compute optimized** | **C** | High CPU per dollar (1 vCPU : 2 GiB) | Batch processing, **media transcoding**, high-performance web servers, scientific modelling, ad serving, gaming servers, HPC |
| **Memory optimized** | **R**, **X**, **z1d**, **u-** (High Memory) | Large memory per vCPU (1 vCPU : 8–32+ GiB) | In-memory databases, **SAP HANA**, large caches (Redis), real-time big data analytics, Electronic Design Automation |
| **Storage optimized** | **I** (NVMe IOPS), **D** (dense HDD), **H** (HDD throughput) | Very high local disk IOPS or throughput | NoSQL (Cassandra, ScyllaDB, MongoDB), Elasticsearch/OpenSearch, data warehousing, distributed file systems, transactional databases needing local storage |
| **Accelerated computing** | **P** (GPU training), **G** (GPU inference/graphics), **Inf** (Inferentia), **Trn** (Trainium), **F** (FPGA), **VT** (video transcode) | Hardware acceleration | ML training and inference, graphics workstations, genomics, video processing |
| **HPC optimized** | **Hpc** | Tightly coupled HPC with high network bandwidth | CFD, weather simulation, molecular dynamics |

## 1.3 Burstable (T) instances — a frequent exam trap

T-family instances provide a **baseline** level of CPU and accumulate **CPU credits** when running below it; credits are spent when bursting above baseline.

- When credits are exhausted in **Standard mode**, performance is **throttled to the baseline** — which looks like a mysterious, severe slowdown after hours of healthy operation. This is a classic scenario question.
- **Unlimited mode** (default for T3/T3a/T4g) allows sustained bursting and charges a surcharge for credits used beyond what is earned.
- T instances are ideal for workloads with **low average CPU and occasional spikes** (small websites, dev environments, microservices), and wrong for sustained CPU-heavy work — use **C** or **M** instead.

## 1.4 AWS Graviton

Graviton (currently Graviton2/3/4, the `g` suffix) are AWS-designed ARM processors delivering **up to ~40% better price/performance** than comparable x86 instances, with lower power consumption.

- Works with most Linux distributions and open-source software; applications written in interpreted or JIT languages (Python, Java, Node.js, Go, .NET Core, PHP, Ruby) usually need only a rebuild/redeploy. Compiled C/C++ needs recompilation.
- Available for EC2, **Lambda (arm64)**, **Fargate**, RDS, Aurora, ElastiCache, OpenSearch, EMR, and more.
- **Exam cue:** "improve performance and reduce cost for a Linux workload" → **Graviton**.

## 1.5 Networking performance features

- **Enhanced networking (ENA)** — SR-IOV based, up to **100 Gbps** on supported instances, with lower latency and jitter than the older virtualized NIC. Enabled by default on modern AMIs/instances.
- **ENA Express** (Scalable Reliable Datagram) — reduces tail latency and increases single-flow bandwidth.
- **Elastic Fabric Adapter (EFA)** — adds **OS-bypass** so HPC and ML frameworks (MPI, NCCL) can communicate directly with the network hardware, dramatically lowering latency for tightly coupled jobs. Only available on specific instance types and only useful within a **cluster placement group**.
- **Placement groups:**
  - **Cluster** — all instances in one AZ, physically close; lowest latency and highest per-flow throughput (up to 100 Gbps). Reduces availability.
  - **Spread** — each instance on distinct hardware, max 7 per AZ per group; best for small critical fleets.
  - **Partition** — groups of racks isolated from each other; for large distributed systems like HDFS, Cassandra, Kafka.
- **Instance network bandwidth scales with instance size.** A network-bound workload may need a larger or `n`-suffixed instance even if CPU is idle.
- **Jumbo frames (MTU 9001)** work inside a VPC and over Direct Connect, but not over the internet or most VPN paths.

## 1.6 Tenancy options

- **Shared (default)** — your instances share hardware with other customers.
- **Dedicated Instances** — hardware dedicated to your account, but instances may move between hosts.
- **Dedicated Hosts** — a specific physical server allocated to you, with visibility of sockets and cores. Required for **BYOL licensing** tied to physical cores (Windows Server, SQL Server, Oracle) and for some compliance regimes.

---

# 2. Scaling EC2

## 2.1 Auto Scaling group essentials

An ASG maintains capacity between **min**, **desired**, and **max** across multiple AZs, replacing unhealthy instances and integrating with load balancers.

- Use **launch templates** (versioned; required for mixed instances, Spot, and newer features).
- **Set `HealthCheckType = ELB`** so application-level failures trigger replacement, with a sensible **health check grace period**.
- **Lifecycle hooks** pause instances during launch or terminate to allow bootstrapping or draining.
- **Warm pools** keep pre-initialized instances stopped, so scale-out is near-instant for applications with long boot or warm-up times.
- **Instance refresh** performs controlled rolling replacement when the launch template changes.
- **Mixed instances policy** — specify several instance types and an On-Demand/Spot split, with allocation strategies (`price-capacity-optimized` is the modern recommendation) and **capacity rebalancing** for Spot.

## 2.2 Scaling policies and choosing the right metric

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

## 2.3 Application Auto Scaling

The same engine scales other resources: **ECS services**, **DynamoDB** tables and GSIs, **Aurora Replicas**, **Lambda provisioned concurrency**, Spot Fleet, EMR, SageMaker endpoints, AppStream, Comprehend, Keyspaces, and Neptune.

---

# 3. Serverless Compute

## 3.1 AWS Lambda performance tuning

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

## 3.2 AWS Fargate

Serverless compute for containers on ECS and EKS. You declare vCPU and memory per task (from 0.25 vCPU/0.5 GB up to 16 vCPU/120 GB, plus configurable ephemeral storage up to 200 GB), and AWS runs it with no instances to patch, scale, or secure.

- Billed per vCPU-second and GB-second with a one-minute minimum.
- **Fargate Spot** offers up to 70% savings for interruption-tolerant tasks.
- Supports **Graviton (arm64)** for better price/performance.
- Each task gets its own kernel-level isolation and its own ENI (`awsvpc` mode), which is also a security advantage.

Trade-offs vs ECS on EC2: Fargate has no GPU support, no access to the host, and can be more expensive at very high steady utilization, where bin-packed EC2 (especially with Spot) wins.

---

# 4. Containers at Scale

- **Amazon ECS** — services maintain a desired task count; **service auto scaling** (via Application Auto Scaling) reacts to CPU, memory, or **`ALBRequestCountPerTarget`**. **Capacity providers** connect the service to either Fargate/Fargate Spot or an EC2 Auto Scaling group with **managed scaling** (which scales the instance fleet to fit pending tasks).
- **Amazon EKS** — managed Kubernetes control plane across multiple AZs. Node scaling via **managed node groups** with the **Cluster Autoscaler**, or **Karpenter** (which provisions right-sized nodes just-in-time and consolidates workloads — significantly faster and more efficient). Pod scaling via the **Horizontal Pod Autoscaler** (and VPA for vertical). **Fargate profiles** run pods serverlessly.
- **Amazon ECR** for images, with lifecycle policies and replication.
- Performance considerations: right-size task CPU/memory requests (over-requesting wastes capacity, under-requesting throttles), use **awsvpc** networking, place tasks across AZs, and use **Service Connect / Cloud Map** for service discovery.

---

# 5. Batch and Big Data Compute

- **AWS Batch** — fully managed batch scheduling. You define **job definitions**, submit jobs to **job queues** with priorities, and Batch provisions a **compute environment** (EC2 On-Demand, **Spot**, or Fargate) sized to the queue. Supports **array jobs** (thousands of similar tasks), **job dependencies**, and automatic retry. The answer for *"run thousands of queued jobs cost-effectively with no scheduler to manage."*
- **Amazon EMR** — managed Hadoop ecosystem (Spark, Hive, Presto/Trino, HBase, Flink). Uses **instance fleets or groups** with master, core (HDFS), and **task nodes (ideal for Spot)**. Variants: EMR on EC2, **EMR on EKS**, and **EMR Serverless**. Use for petabyte-scale distributed processing and when you need specific framework versions or deep tuning.
- **AWS ParallelCluster** — open-source tool for provisioning traditional HPC clusters (Slurm) on AWS.
- **Choosing:** short event-driven work → **Lambda**; many long-running queued jobs → **Batch**; distributed data-processing frameworks → **EMR**; tightly coupled MPI simulations → **HPC instances + cluster placement group + EFA** (often via ParallelCluster).

---

# 6. Edge and Distributed Compute

- **CloudFront Functions** — ultra-lightweight JavaScript at the edge (sub-millisecond, ~1 ms CPU budget) for header manipulation, URL rewrites, redirects, and simple auth checks. Runs at all edge locations, highest scale, lowest cost.
- **Lambda@Edge** — full Node.js/Python functions running at **regional edge caches**, with more memory, longer execution, and network access. Use for heavier logic: origin selection, A/B testing with external calls, image resizing, authorization against an external service.
- **AWS Outposts** — AWS-managed racks on-premises running EC2, EBS, S3, ECS/EKS, RDS locally. For latency-sensitive on-prem integration or data residency.
- **AWS Local Zones** — extend a Region into a metro area for single-digit-millisecond latency (media rendering, gaming, remote desktops).
- **AWS Wavelength** — compute inside 5G carrier networks for mobile edge applications.
- **AWS IoT Greengrass** — run Lambda functions and ML inference on edge devices.
- **AWS Global Accelerator** — not compute, but it reduces the network component of latency by moving traffic onto the AWS backbone at the nearest edge.

---

# 7. Decoupling So Components Scale Independently

A tightly coupled synchronous chain forces every tier to scale together and makes the slowest component the bottleneck for everything. Insert the right integration point:

- **Queue (SQS)** between a fast producer and a slow consumer, scaling workers on **backlog depth**
- **Stream (Kinesis)** when multiple consumers need the same ordered data
- **Topic/bus (SNS/EventBridge)** when one event must trigger several independent reactions
- **Load balancer** between stateless tiers
- **Cache (ElastiCache/DAX/CloudFront)** in front of expensive reads
- **Step Functions** to coordinate long-running multi-step work without holding a connection open

Each component then scales on **its own signal** — requests per target for the web tier, queue depth for workers, RCU/WCU for DynamoDB, replica count for the database read layer.

---

# 8. Worked Scenarios

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

# 9. Quick Decision Table

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
