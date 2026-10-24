# Task 2.1 — Design Scalable and Loosely Coupled Architectures

> This task is about **how components talk to each other** and **how each one grows independently**. The recurring exam theme: a synchronous, tightly coupled design is failing under load or cascading failures — replace it with queues, events, load balancers, auto scaling, caching, and managed services.

---

# 1. Scaling Concepts

## 1.1 Vertical vs horizontal scaling

**Vertical scaling (scale up)** means replacing a resource with a bigger one — `t3.medium` → `m6i.4xlarge`, or `db.r6g.large` → `db.r6g.8xlarge`.
- *Advantages:* no application changes, no distributed-systems complexity, works for software that cannot be clustered.
- *Disadvantages:* there is always a ceiling (the largest instance type); it usually requires a **stop/start or failover**, so there is downtime; and a single large instance is a single point of failure. You also pay for peak capacity continuously.
- *Where it is still the right answer:* the **writer node of a relational database**, legacy monoliths, and licensed software priced per node.

**Horizontal scaling (scale out)** means adding more instances of the same component behind a load balancer or a queue.
- *Advantages:* effectively unlimited, each unit is small and cheap, failures remove only a fraction of capacity, and you can scale in to save money.
- *Prerequisite:* the component must be **stateless**, or state must be externalized.
- *This is the cloud-native default and the expected exam answer* whenever the question mentions growth, elasticity, or availability.

**Elasticity** is the ability to add and remove capacity automatically in response to demand; **scalability** is the ability to grow at all. AWS questions that say "handle unpredictable spikes without over-provisioning" are asking for **elasticity** (Auto Scaling, serverless, on-demand capacity).

## 1.2 Stateless design

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

## 1.3 Loose coupling

Two components are **tightly coupled** when one calls the other synchronously and directly, and must know its address, be available at the same moment, and process at the same speed. One slow or failed component then stalls or breaks the whole chain.

**Loose coupling** inserts a well-defined interface between them — a load balancer, a queue, a topic, an event bus, or an API — so that:
- Producers don't need to know how many consumers exist or where they are
- A consumer outage buffers work instead of losing it
- Each side scales on its own signal
- Components can be deployed, upgraded, and replaced independently

---

# 2. Load Balancing with Elastic Load Balancing

## 2.1 The four load balancer types

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

## 2.2 Target groups, listeners and rules

- A **listener** watches a port/protocol; **rules** evaluate conditions in priority order and route to a **target group**.
- Example microservice routing on one ALB: `/api/orders/*` → orders-tg, `/api/users/*` → users-tg, `Host: admin.example.com` → admin-tg, everything else → a fixed 404 response. One ALB can therefore serve many services, which is also a cost optimization.
- **Weighted target groups** enable blue/green and canary deployments (e.g., 95% to v1, 5% to v2).
- **Health checks** per target group (protocol, path, interval, timeout, healthy/unhealthy thresholds, matcher codes). Unhealthy targets are removed from rotation; the ASG can then replace them if the ASG health check type is **ELB**.
- **Deregistration delay (connection draining)** — default **300 seconds** — lets in-flight requests finish before a target is removed.
- **Slow start** gradually ramps traffic to newly registered targets so caches and JITs warm up.

## 2.3 Cross-zone load balancing

- **ALB: enabled by default and free.** Every node can send traffic to targets in any AZ, so an uneven number of targets per AZ is still balanced evenly.
- **NLB: disabled by default**, and enabling it incurs **inter-AZ data transfer charges**. Without it, each NLB node sends only to targets in its own AZ.

## 2.4 TLS and security

- Terminate TLS at the load balancer with an **ACM certificate** (ALB certs in the ALB's Region).
- **SNI** lets one listener host many certificates.
- Use **security group chaining**: the ALB's SG allows 443 from the internet; the instance SG allows the app port **from the ALB's SG only**.
- Attach **AWS WAF** to the ALB for L7 protection; NLBs cannot have WAF.

---

# 3. Auto Scaling

## 3.1 EC2 Auto Scaling groups

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

## 3.2 Scaling policies

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

## 3.3 Application Auto Scaling

Beyond EC2, AWS Auto Scaling / Application Auto Scaling can scale: **ECS services**, **DynamoDB** table and index capacity, **Aurora Replicas**, **Lambda provisioned concurrency**, Spot Fleet, EMR clusters, SageMaker endpoints, Comprehend, Keyspaces, Neptune, and more.

---

# 4. Decoupling: Queues, Topics, Events and Workflows

## 4.1 Amazon SQS

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

## 4.2 Amazon SNS

A fully managed **push-based publish/subscribe** service. A publisher sends one message to a **topic**, and SNS delivers a copy to **every subscriber**.

- **Subscriber types:** SQS queues, Lambda functions, HTTP/HTTPS endpoints, email, SMS, mobile push (APNs/FCM), Kinesis Data Firehose, and AWS Event Fork Pipelines.
- **Fan-out pattern** — the canonical loose-coupling design: one event → an SNS topic → **multiple SQS queues**, each owned by a different consumer. Each consumer gets its own durable copy, retries independently, and has its own DLQ. If one consumer is down, its queue buffers.
- **Message filtering** — subscription filter policies evaluate message attributes (or body) so each subscriber receives only relevant messages.
- **FIFO topics** pair with FIFO queues for ordered fan-out.
- Supports **message archiving/replay**, delivery retries with backoff, and DLQs on subscriptions.

## 4.3 Amazon EventBridge

A **serverless event bus** that routes events based on their content.

- **Buses:** the default bus (AWS service events), **custom buses** (your applications), and **partner buses** (SaaS providers such as Zendesk, Datadog, Shopify).
- **Rules** match an **event pattern** (JSON matching on any field) and send the event to up to 5 **targets** — Lambda, SQS, SNS, Step Functions, ECS tasks, Kinesis, API destinations (external HTTP endpoints), another event bus, and more.
- **Schema registry and discovery** generate code bindings for event structures.
- **Archive and replay** — store events and replay them later, which is invaluable for recovery and testing.
- **EventBridge Scheduler** — a managed cron/rate scheduler at scale (replacing CloudWatch Events rules for scheduling).
- **EventBridge Pipes** — point-to-point integration with filtering and enrichment between a source and target.
- Cross-account and cross-Region event delivery.

**SNS vs EventBridge:** SNS is optimized for very high-throughput, low-latency fan-out and for mobile/SMS/email endpoints. EventBridge is optimized for **content-based routing, AWS and SaaS event sources, schedules, archive/replay, and many heterogeneous targets**. If the question mentions reacting to AWS service state changes, third-party SaaS events, or filtering on event content, choose **EventBridge**.

## 4.4 Amazon MQ

Managed **Apache ActiveMQ** and **RabbitMQ**. Choose it only when an existing application uses **industry-standard messaging protocols** — **AMQP, MQTT, STOMP, JMS, OpenWire** — and must be migrated without rewriting the messaging layer. For anything new, SQS/SNS are cheaper, simpler, and scale better.

## 4.5 AWS Step Functions

Serverless **workflow orchestration** using state machines defined in Amazon States Language.

- **State types:** Task (invoke Lambda, ECS, Batch, SNS, DynamoDB, and 200+ AWS APIs directly), **Choice** (branching), **Parallel**, **Map** (iterate over a collection, including distributed map for very large datasets), Wait, Pass, Succeed, Fail.
- **Built-in error handling:** `Retry` with exponential backoff and jitter, and `Catch` for fallback paths — this removes huge amounts of boilerplate code.
- **Callback pattern (`waitForTaskToken`)** pauses a workflow until an external system or a human responds — this is how approval steps are implemented.
- **Standard workflows:** up to **1 year** duration, **exactly-once** execution, full execution history, visual console. For long-running, auditable business processes.
- **Express workflows:** up to **5 minutes**, **at-least-once**, very high event rate, much cheaper. For streaming ingestion and high-volume short tasks.

**Exam cue:** "coordinate multiple Lambda functions," "retry logic and error handling without writing code," "visualize the process," "a human approval step" → **Step Functions**.

## 4.6 Choosing the right integration service

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

# 5. Amazon API Gateway

## 5.1 API types

| | **REST API** | **HTTP API** | **WebSocket API** |
|---|---|---|---|
| Cost | Higher | **Up to ~71% cheaper** | Per message/connection |
| Latency | Low | **Lower** | — |
| Features | Full set: request/response transformation (VTL), **caching**, **API keys and usage plans**, request validation, WAF, private endpoints, canary deployments, AWS X-Ray | Core proxying, **JWT authorizers**, CORS, simpler config | Bidirectional, persistent connections |
| Use | Feature-rich public APIs, legacy integrations | Simple, low-latency proxies to Lambda/HTTP | Chat, live dashboards, notifications |

## 5.2 Key capabilities

- **Integrations:** Lambda (proxy and non-proxy), any HTTP backend, **direct AWS service integrations** (put straight into SQS, Kinesis, DynamoDB, or Step Functions without a Lambda "glue" function), private integrations to an NLB/ALB via VPC Link.
- **Authorization:** IAM (SigV4), Cognito user pool authorizer, **Lambda authorizer** (token or request based, with result caching), resource policies, and **mTLS**.
- **API keys + usage plans** provide **throttling and quotas per client** — note they are a metering and rate-limiting tool, **not authentication**.
- **Throttling:** account-level default ~10,000 requests/second with a 5,000 burst, plus per-stage and per-method limits. Requests beyond the limit receive **429 Too Many Requests**.
- **Caching:** 0.5 GB to 237 GB per stage, TTL up to 1 hour (default 300 s), with per-method cache settings and cache invalidation headers. Reduces backend load and latency.
- **Stages and canary releases:** deploy to `dev`/`prod` stages; a canary sends a percentage of traffic to a new deployment.
- **Private APIs** are reachable only through **interface VPC endpoints**, controlled by a resource policy.
- **Timeout:** the integration timeout is **29 seconds** (treat this as the exam number). Anything longer must be asynchronous — return `202 Accepted` and process via SQS/Step Functions, with the client polling or receiving a notification.

---

# 6. Serverless and Containers

## 6.1 AWS Lambda

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

## 6.2 Containers on AWS

- **Amazon ECS** — AWS's own orchestrator. Concepts: **task definition** (the blueprint: image, CPU/memory, ports, IAM role, logging), **task** (a running instance of it), **service** (maintains N tasks and integrates with an ALB), **cluster**. Launch types:
  - **EC2** — you own and pay for the instances; more control, supports GPU/special instance types, can use **Spot** and bin-packing for cost efficiency.
  - **Fargate** — serverless; you specify vCPU/memory per task and AWS runs it; no instances to patch or scale.
- **Amazon EKS** — managed Kubernetes control plane. Choose when you need Kubernetes APIs, Helm, operators, or portability between clouds/on-prem. Nodes can be self-managed, managed node groups, **Karpenter**-provisioned, or **Fargate profiles**.
- **AWS Fargate** — the serverless compute engine behind ECS/EKS; billed per vCPU-second and GB-second with a 1-minute minimum. **Fargate Spot** offers up to 70% savings for interruption-tolerant tasks.
- **Amazon ECR** — private registry with image scanning (basic and enhanced via Inspector), lifecycle policies, immutable tags, and cross-Region replication.
- **AWS App Runner** — point it at a container image or source repository and get a scaled, load-balanced HTTPS service with the least configuration of any option.

**Security in containers:** use **task roles** (per task, least privilege) rather than instance roles; use the **`awsvpc` network mode** so each task gets its own ENI and security group; pull secrets from Secrets Manager via the task definition; scan images in ECR.

**Migrating to containers:** **AWS App2Container** converts existing Java and .NET applications into container images with generated ECS/EKS deployment artifacts. For pure lift-and-shift to EC2, **AWS Application Migration Service (MGN)** is the tool.

## 6.3 Choosing compute

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

# 7. Multi-Tier and Microservice Patterns

## 7.1 Classic three-tier web architecture

```
Route 53  →  CloudFront (+ WAF)  →  ALB (public subnets, 2–3 AZs)
                                      ↓
                        Auto Scaling group of app servers (private subnets)
                                      ↓
      RDS Multi-AZ / Aurora (private DB subnets)  +  ElastiCache  +  S3
```
Static assets live in S3 behind CloudFront; sessions live in ElastiCache or DynamoDB; secrets in Secrets Manager; outbound access via NAT gateways; AWS service access via VPC endpoints.

## 7.2 Event-driven serverless architecture

```
Client → API Gateway → Lambda → SQS → worker (Lambda/Fargate) → DynamoDB
                          ↓
                    EventBridge → other services
                          ↓
                 Step Functions (orchestration)
```
Characteristics: no servers, pay-per-use, each stage scales independently, failures isolated by queues and DLQs.

## 7.3 Microservice design principles

- **Single responsibility** and **independent deployability**
- **A data store per service** — no shared database tables between services
- **Stateless services** so they scale horizontally
- **Asynchronous communication** wherever a synchronous response is not strictly needed
- **Idempotent consumers** — because at-least-once delivery means duplicates will happen
- **Retries with exponential backoff and jitter**, plus **circuit breakers** so a failing dependency doesn't exhaust your threads
- **Graceful degradation** — serve cached or partial results rather than failing entirely
- **Service discovery** — **AWS Cloud Map** / **ECS Service Connect**, or an ALB per service
- **Observability** — structured logs, metrics, and **X-Ray** tracing across service boundaries

## 7.4 The "fan-out + buffer" pattern (worth memorizing)

S3 upload → **SNS topic** → three **SQS queues** → three independent consumers (thumbnailer, indexer, notifier). Each consumer scales on its own queue depth, retries independently, and has its own DLQ. This single diagram answers a surprising number of exam questions.

---

# 8. Caching and Edge Acceleration

## 8.1 Layers of caching

| Layer | Service / technique | Typical gain |
|---|---|---|
| Browser/client | `Cache-Control`, ETags | Eliminates requests entirely |
| Edge CDN | **CloudFront** (static + dynamic, Origin Shield) | Latency and origin offload |
| API | **API Gateway cache** | Fewer backend invocations |
| Application / session / query | **ElastiCache (Redis/Valkey or Memcached)** | Microsecond reads |
| NoSQL | **DynamoDB DAX** | Microsecond reads, reduced RCU |
| Relational read scaling | **Read replicas** | Offloads the primary |
| DNS | Route 53 TTL | Fewer lookups |

## 8.2 Caching strategies

- **Lazy loading (cache-aside)** — on a miss, read from the database and populate the cache. Only requested data is cached, and a cache failure is survivable. Downsides: a cache miss costs three round trips, and data can become stale.
- **Write-through** — write to the cache on every database write. Data is always fresh and reads are fast, but writes are slower and the cache fills with data that may never be read.
- **TTL-based expiry** — bound staleness; usually combined with the strategies above.
- Typical production answer: **lazy loading + write-through for hot keys + TTL**.

## 8.3 Read replicas

Use when the workload is **read-heavy**, for reporting/analytics offload, or to provide low-latency reads in another Region. Replication is **asynchronous**, so replicas are **eventually consistent** — never use them when the application requires read-after-write consistency. RDS supports up to 5 replicas per source; **Aurora supports 15** with typically sub-10 ms lag. Replicas can be **promoted** to standalone databases (a manual DR action).

## 8.4 Edge acceleration

- **Amazon CloudFront** — caches at 600+ points of presence, terminates TLS at the edge, supports **Origin Shield** (an extra regional caching layer), origin failover groups, signed URLs/cookies, field-level encryption, and edge compute (**CloudFront Functions** for light header/URL work, **Lambda@Edge** for heavier logic).
- **AWS Global Accelerator** — two **static anycast IP addresses**; client traffic enters the AWS backbone at the nearest edge and is routed to the healthiest endpoint, with **failover in seconds independent of DNS TTLs**. Supports **TCP and UDP**, so it is the choice for gaming, VoIP, MQTT/IoT, and any non-HTTP protocol, or when clients cache DNS badly.

---

# 9. Storage Types in Scalable Designs

| Type | Services | Characteristics | Typical use |
|---|---|---|---|
| **Object** | S3, S3 Glacier | Flat namespace, HTTP API, virtually unlimited, rich metadata, no partial in-place update | Static assets, data lake, backups, media, logs |
| **File** | EFS (NFS/Linux), FSx for Windows (SMB), FSx for Lustre (HPC), FSx ONTAP/OpenZFS | Shared, concurrent access with POSIX/SMB semantics | Shared content, home directories, lift-and-shift, HPC |
| **Block** | EBS (single AZ; Multi-Attach on io1/io2), Instance store (ephemeral) | Raw devices, lowest latency, filesystem on top | Boot volumes, databases, transactional workloads |

Design rule: **put shared state in S3 or EFS, never on an instance's local disk**, so the fleet can scale and instances remain disposable.

---

# 10. Worked Scenarios

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

# 11. Quick Decision Table

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
