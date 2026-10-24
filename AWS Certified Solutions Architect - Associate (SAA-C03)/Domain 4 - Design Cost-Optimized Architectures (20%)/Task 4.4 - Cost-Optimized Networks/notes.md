# Task 4.4 — Design Cost-Optimized Network Architectures

> Network charges are the most invisible part of an AWS bill — there is no "instance" to look at, just a data-transfer line item. The exam tests whether you know **which direction and which path costs money**, and the handful of architectural moves that eliminate most of it.

---

# 1. The AWS Data Transfer Cost Model

## 1.1 The fundamental rules

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

## 1.2 The mental model

Ask three questions about any byte:
1. **Does it leave AWS?** Internet egress is the expensive case — reduce it with caching, compression, and CloudFront.
2. **Does it cross an AZ or Region boundary?** If so, can the components be co-located?
3. **Does it pass through a billed middlebox?** NAT gateway, Transit Gateway, interface endpoint, and load balancer all add per-GB processing. Can the path be shortened?

---

# 2. Eliminating NAT Gateway Costs

A NAT gateway costs roughly **$0.045 per hour** plus **$0.045 per GB processed** — and that data-processing charge applies *even when the destination is an AWS service in the same Region*. For a workload pulling terabytes from S3, this is often the single largest surprise on the bill.

**Fixes, in order of impact:**

1. **Gateway VPC endpoints for S3 and DynamoDB** — **completely free**, added as a route table entry. Traffic to S3/DynamoDB bypasses the NAT gateway entirely. If a question mentions private instances downloading large volumes from S3 through NAT, this is the answer.
2. **Interface VPC endpoints (PrivateLink)** for other AWS services (SSM, ECR, Secrets Manager, CloudWatch Logs, KMS, SQS, SNS…). These have an hourly and per-GB cost, but the per-GB rate is lower than NAT processing and they also improve security. Model the break-even: for low-volume services the NAT may be cheaper; for high-volume (ECR image pulls, CloudWatch Logs) endpoints win.
3. **Consolidate NAT gateways** where resilience permits — but note the trade-off: one NAT gateway per AZ costs more in hourly charges yet **avoids cross-AZ data charges** and removes a single point of failure. For high-volume workloads, per-AZ NAT gateways are usually both cheaper and safer; for low-volume dev environments, a single NAT gateway is cheaper.
4. **Remove the need for egress entirely** — use VPC endpoints, host packages in **CodeArtifact/ECR** with endpoints, and bake dependencies into AMIs/container images so instances don't download them at boot.
5. For very small, low-throughput environments, a **NAT instance** on a `t4g.nano` can be cheaper than a NAT gateway — but it is a single point of failure, bandwidth-limited, and you manage it. AWS recommends NAT gateway for anything real.
6. **IPv6 workloads** can use an **egress-only internet gateway**, which has **no hourly or per-GB charge**.

---

# 3. Reducing Internet Egress with CloudFront

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

# 4. Co-location: Avoiding Cross-AZ and Cross-Region Charges

- **Same-AZ private IPv4 traffic is free.** Cross-AZ traffic is charged **in both directions**.
- Keep **chatty components in the same AZ** where availability requirements allow — for example, an application server and its cache replica. Balance this against resilience: never sacrifice Multi-AZ for a production database to save transfer cost.
- **ElastiCache**: reading from a replica in another AZ incurs cross-AZ charges. Redis **read-from-replica with AZ affinity** keeps reads local.
- **Load balancers:** **ALB cross-zone load balancing is on by default and free**; **NLB cross-zone is off by default and billed as cross-AZ traffic when enabled**. Enabling it on an NLB processing terabytes is a real cost — weigh it against the uneven distribution it fixes.
- **Kafka/Cassandra/Elasticsearch** style clusters replicate heavily between nodes; spreading them across AZs is necessary for resilience but is a genuine cost line — use rack-aware/AZ-aware configuration to minimize unnecessary cross-AZ replication.
- **Cross-Region replication** (S3 CRR, Aurora Global Database, DynamoDB global tables, cross-Region read replicas) all incur inter-Region transfer. Replicate only what genuinely needs it — for S3, use **replication rules with prefix/tag filters** rather than replicating whole buckets.
- Always use **private IPs / internal DNS** rather than public IPs for internal communication: traffic to a public IP leaves and re-enters the VPC and is charged even within the same AZ.

---

# 5. Choosing Cost-Effective Connectivity

## 5.1 VPC peering vs Transit Gateway

| | **VPC peering** | **Transit Gateway** |
|---|---|---|
| Hourly charge | **None** | Per attachment per hour |
| Data processing | **None** (only cross-AZ/Region transfer rates apply) | **Per GB processed** on top of transfer |
| Scale | n(n−1)/2 connections; not transitive | Thousands of attachments, transitive, centrally routed |

**Cost conclusion:** for a **small number of VPCs with high traffic volume**, peering is cheaper (no hourly or processing fees). For **many VPCs**, Transit Gateway's operational simplicity usually outweighs its per-GB cost — and the management burden of 45+ peerings is its own expense. A common hybrid: Transit Gateway as the general hub, with **direct peering for the few highest-volume VPC pairs**.

## 5.2 VPN vs Direct Connect

- **Site-to-Site VPN** — low hourly cost per connection plus standard internet egress rates. Cheap to start, no commitment, available immediately.
- **Direct Connect** — port-hour charges plus **significantly reduced data-transfer-out rates**. The port cost is fixed, so DX becomes cheaper than VPN above a certain monthly volume (often in the tens of TB). It also provides consistent latency and bandwidth.
- **Break-even thinking:** compute (VPN internet egress $/GB × monthly GB) versus (DX port hours + DX egress $/GB × monthly GB). High, sustained volume favours DX; low or bursty volume favours VPN.
- **Hosted connections** (50 Mbps–25 Gbps via a partner) avoid the cost of a full 1 Gbps port for moderate bandwidth needs.
- Keep a **VPN as a cheap backup** for a single DX rather than buying a second DX, when the budget doesn't allow full redundancy (accepting lower resilience).

## 5.3 PrivateLink vs peering vs Transit Gateway

**PrivateLink (interface endpoints)** charges per endpoint-hour per AZ plus per GB. It is cost-effective when you need **one-way access to a specific service** rather than full network connectivity — and it avoids the overlapping-CIDR problems and broad exposure of peering. For **many consumers reaching one service**, PrivateLink is usually both cheaper and safer than building a mesh.

## 5.4 Load balancers

- **ALB/NLB pricing** = hourly + **LCUs/NLCUs** measured on new connections, active connections, processed bytes, and (ALB) rule evaluations. The highest dimension sets the charge.
- **Consolidate**: one ALB with **host- and path-based routing** can serve dozens of services instead of running one ALB per service — a large and easy saving in microservice environments. The **AWS Load Balancer Controller** with **IngressGroups** does this for EKS.
- **Delete idle load balancers** — Trusted Advisor flags them.
- For pure TCP pass-through at high volume, an **NLB is usually cheaper** than an ALB (fewer processing features).
- Remember that **CloudFront in front of an ALB** reduces the bytes and connections the ALB processes, lowering LCU charges.

---

# 6. Other Network Cost Items

- **Public IPv4 addresses are now charged per hour for every in-use address** (including those attached to running instances, NAT gateways, and load balancers). Reduce the count: use private IPs with a shared NAT gateway or VPC endpoints, front fleets with a single load balancer, and adopt **IPv6** where possible.
- **Unassociated Elastic IPs** are charged — Trusted Advisor flags them, and they are pure waste.
- **VPC Flow Logs** cost money in **ingestion and storage** (CloudWatch Logs or S3). For high-volume VPCs, send them to **S3 in Parquet** rather than CloudWatch Logs, sample or filter (log only rejects, or only specific ENIs), and apply lifecycle rules.
- **Global Accelerator** has a fixed hourly fee plus a per-GB **data transfer premium**. It buys performance and fast failover, not savings — justify it on requirements.
- **Interface endpoints** are billed per AZ: an endpoint in 3 AZs costs 3× the hourly rate. Deploy only in the AZs you actually use.
- **Transit Gateway attachments** bill hourly even when idle — remove attachments for decommissioned VPCs.
- **Route 53**: hosted zone monthly fee plus per-query charges; **alias records to AWS resources are free to query**, so prefer them over CNAMEs pointing at AWS endpoints. Health checks are billed per check (more for non-AWS endpoints and optional features).
- **Data Transfer Out discounts:** the first 100 GB per month of internet egress is free account-wide, and volume tiers reduce the rate at scale.

---

# 7. Monitoring Network Spend

- **Cost Explorer** — filter by **usage type** (`DataTransfer-Out-Bytes`, `NatGateway-Bytes`, `DataTransfer-Regional-Bytes`) and group by service to see exactly which path is costing money.
- **Cost and Usage Report** in Athena — the only way to attribute transfer costs precisely to resources and teams.
- **VPC Flow Logs** — identify the top talkers and unexpected flows driving transfer (and then turn the logs off or sample them, because they cost money too).
- **CloudWatch metrics** — NAT gateway `BytesOutToDestination`/`BytesOutToSource`, ALB `ProcessedBytes`, CloudFront `BytesDownloaded` and **cache hit rate**, interface endpoint bytes processed.
- **Cost Anomaly Detection** catches a sudden transfer spike (often a misconfigured sync job or a cross-Region replication someone enabled).
- **Trusted Advisor** — idle load balancers, unassociated Elastic IPs.

---

# 8. Worked Scenarios

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

# 9. Quick Decision Table

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
