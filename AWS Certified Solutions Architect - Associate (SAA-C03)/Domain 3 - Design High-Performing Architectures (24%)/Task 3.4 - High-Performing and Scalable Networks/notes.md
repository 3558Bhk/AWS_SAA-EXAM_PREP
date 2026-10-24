# Task 3.4 — Determine High-Performing and/or Scalable Network Architectures

> Networking questions in the exam are usually about **latency** (get the user closer / get traffic onto the AWS backbone), **bandwidth** (choose the right link and instance), or **topology at scale** (how do 200 VPCs and five data centres connect without a mess of peering).

---

# 1. VPC Networking Foundations

## 1.1 Building blocks

- A **VPC** is a logically isolated virtual network in one Region, defined by a CIDR block (**/16 to /28**). You can add up to four secondary CIDRs.
- **Subnets** are AZ-scoped slices of the VPC CIDR. A subnet is **public** if its route table has a route to an **internet gateway**; otherwise it is private. **This routing fact — not a checkbox — is what makes a subnet public.**
- AWS reserves **5 IP addresses per subnet**: network address, VPC router, DNS, future use, and broadcast. A `/24` therefore yields 251 usable addresses.
- **Route tables** are evaluated **most-specific-prefix-first**; the local route for the VPC CIDR always wins and cannot be removed.
- **Elastic network interfaces (ENIs)** carry private IPs, security groups, and (optionally) public/Elastic IPs. The number of ENIs and IPs per instance is limited by instance type — a factor when running many containers in `awsvpc` mode.

## 1.2 Internet and egress paths

| Component | Direction | Notes |
|---|---|---|
| **Internet gateway (IGW)** | Inbound + outbound, IPv4/IPv6 | Horizontally scaled, no bandwidth constraint |
| **NAT gateway** | **Outbound only**, IPv4 | Managed, AZ-scoped, scales **5 → 100 Gbps**, 55,000 simultaneous connections per unique destination. Deploy **one per AZ** for resilience and to avoid cross-AZ data charges |
| **NAT instance** | Outbound only | Self-managed EC2; bandwidth limited by instance type; must **disable source/destination check**. Legacy |
| **Egress-only internet gateway** | Outbound only, **IPv6** | IPv6 addresses are globally routable, so this is the IPv6 equivalent of NAT for egress-only |

## 1.3 IP addressing and planning

- Plan **non-overlapping CIDRs** across all VPCs and on-premises networks — overlapping ranges block peering, Transit Gateway routing, and VPN.
- Leave room for growth; subnets cannot be resized after creation.
- **Amazon VPC IP Address Manager (IPAM)** plans, tracks, allocates, and audits CIDRs across accounts and Regions — the answer for "manage IP space at organization scale."
- **IPv6** addresses in AWS are all public; use an egress-only IGW for outbound-only, and note that **security groups and NACLs need explicit IPv6 rules**.

## 1.4 DNS in the VPC

- **Amazon-provided DNS** at the VPC base + 2 (and `169.254.169.253`), controlled by `enableDnsSupport` and `enableDnsHostnames`.
- **Route 53 Resolver endpoints**: **inbound** endpoints let on-premises resolvers query Route 53 private hosted zones; **outbound** endpoints plus **forwarding rules** let VPC resources resolve on-premises domains. Together they give hybrid DNS.
- **Private hosted zones** serve internal names to associated VPCs.
- **Route 53 Resolver DNS Firewall** blocks queries to malicious or unapproved domains.

---

# 2. Connecting VPCs and Accounts

## 2.1 VPC peering

A one-to-one, private connection between two VPCs (same or different account, same or different Region).

- Uses AWS's private network; **no single point of failure and no bandwidth bottleneck**.
- **Not transitive** — if A peers with B and B peers with C, A cannot reach C. This is the defining limitation.
- CIDRs **must not overlap**.
- Each side must update route tables and security groups (you can reference a security group across a peering connection within the same Region).
- Scaling problem: a full mesh of *n* VPCs needs **n(n−1)/2** connections — 10 VPCs need 45 peerings. This is why Transit Gateway exists.

## 2.2 AWS Transit Gateway

A **regional network hub** that connects VPCs, VPN connections, Direct Connect gateways, and other Transit Gateways in a hub-and-spoke topology.

- Scales to **thousands of VPC attachments**, with up to **50 Gbps per VPC attachment** (and up to 100 Gbps aggregate per flow set with ECMP across multiple VPN tunnels).
- **Transit Gateway route tables** allow segmentation — for example, a "production" route table and a "development" route table so the two environments can each reach shared services but not each other.
- **Transit Gateway peering** connects TGWs across Regions over the AWS backbone (encrypted), enabling a global network.
- **Multicast** support, and **Connect attachments** for SD-WAN appliances using GRE.
- Share the TGW across accounts with **AWS RAM**.
- Billed per attachment-hour plus data processed.

**Exam cue:** "connect many VPCs and on-premises networks with centralized routing" or "VPC peering doesn't scale / isn't transitive" → **Transit Gateway**.

## 2.3 AWS PrivateLink and VPC endpoints

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

## 2.4 AWS Resource Access Manager (RAM)

Share resources across accounts without duplicating them: **subnets (VPC sharing)**, Transit Gateways, Route 53 Resolver rules, License Manager configurations, Aurora clusters, and more. **VPC sharing** lets many accounts deploy into subnets of one centrally managed VPC — reducing IP sprawl and the number of VPCs to interconnect.

## 2.5 AWS Cloud WAN

A managed **global** wide-area network: define a network policy centrally and AWS builds and manages the connectivity between Regions, VPCs, and on-premises locations, with segmentation and a unified dashboard. Think "Transit Gateway, but global and policy-driven."

---

# 3. Hybrid Connectivity

## 3.1 Site-to-Site VPN

An IPsec tunnel between your customer gateway and an AWS **virtual private gateway (VGW)** or Transit Gateway.

- Each connection provides **two tunnels in different AZs** for redundancy — configure both.
- Throughput: up to **1.25 Gbps per tunnel**; aggregate more with **ECMP over multiple connections to a Transit Gateway**.
- Runs over the **public internet**, so latency and jitter are variable.
- Quick to set up (minutes to hours), low cost, encrypted by default.
- Routing: static or **BGP** (dynamic, with failover).
- **AWS Client VPN** is the separate, OpenVPN-based service for individual remote users.

## 3.2 AWS Direct Connect (DX)

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

## 3.3 Choosing a hybrid link

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

# 4. Edge Services for Performance

## 4.1 Amazon CloudFront

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

## 4.2 AWS Global Accelerator

Provides **two static anycast IP addresses** advertised from AWS edge locations worldwide. Client traffic enters the **AWS global backbone at the nearest edge** and is routed to the optimal healthy endpoint.

- Improves performance by **up to 60%** by bypassing congested internet paths.
- Works at **layer 4** with **TCP and UDP** — so it supports gaming, VoIP, IoT/MQTT, and any non-HTTP protocol that CloudFront cannot.
- **Health checks with failover in seconds**, independent of DNS TTL caching.
- **Traffic dials** (percentage per endpoint group/Region) and **endpoint weights** for gradual migration and blue/green.
- **Client affinity** options to pin a client to one endpoint.
- Endpoints can be ALBs, NLBs, EC2 instances, or Elastic IPs.

## 4.3 CloudFront vs Global Accelerator

| | **CloudFront** | **Global Accelerator** |
|---|---|---|
| Layer | 7 (HTTP/HTTPS) | 4 (TCP/UDP) |
| Caches content | **Yes** | No |
| Static IPs | No (DNS name) | **Yes, two anycast IPs** |
| Non-HTTP protocols | No | **Yes** |
| Failover speed | Origin group failover | **Seconds, no DNS dependency** |
| Best for | Websites, APIs, media, static assets | Gaming, VoIP, IoT, non-HTTP, static-IP requirements, fast regional failover |

They can be combined: Global Accelerator in front of regional ALBs, CloudFront for cacheable content.

## 4.4 Route 53 for performance

- **Latency-based routing** sends each user to the Region with the lowest measured latency for them.
- **Geolocation** and **geoproximity** (with bias) route by location, for compliance or gradual load shifting.
- **Alias records** are free to query, work at the zone apex, and track AWS resource IP changes automatically.
- **Multivalue answer** returns up to 8 healthy records for simple client-side distribution.
- Lower **TTLs** speed up failover at the cost of more queries — and remember that client-side DNS caching often ignores TTLs, which is the argument for Global Accelerator.

## 4.5 S3 Transfer Acceleration and Multi-Region Access Points

- **Transfer Acceleration** routes uploads/downloads through the nearest **CloudFront edge** and over the AWS backbone to the bucket — valuable for geographically distant clients uploading large objects.
- **S3 Multi-Region Access Points** give a single global endpoint that automatically routes to the lowest-latency bucket among several Regions, with failover.

---

# 5. Instance and Protocol-Level Performance

- **Enhanced networking (ENA)** — up to **100 Gbps**, lower latency and jitter; enabled by default on modern instances.
- **ENA Express (SRD)** — improves single-flow bandwidth and tail latency between supported instances.
- **Elastic Fabric Adapter (EFA)** — OS-bypass networking for MPI/NCCL in HPC and distributed ML; only meaningful inside a **cluster placement group**.
- **Instance bandwidth scales with size** — a network-bound workload may need a bigger or `n`-suffixed instance.
- **Placement groups:** cluster (lowest latency, one AZ), spread (distinct hardware, max 7/AZ), partition (rack-isolated groups for distributed systems).
- **Jumbo frames (MTU 9001)** work within a VPC and over Direct Connect; traffic to the internet, over most VPN, or across some gateways is limited to 1500 bytes.
- **Multiple ENIs / IP addresses** can increase aggregate throughput for some workloads and are required for high container density in `awsvpc` mode.

---

# 6. Load Balancer Selection for Performance

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

# 7. Monitoring and Troubleshooting Network Performance

- **VPC Flow Logs** — capture accepted/rejected traffic metadata at the VPC, subnet, or ENI level, delivered to CloudWatch Logs, S3, or Kinesis Firehose. They show **source, destination, ports, bytes, packets, and action** — ideal for diagnosing blocked traffic and traffic volumes. They do **not** capture packet payloads, and they miss some traffic (Amazon DNS, instance metadata, license activation, DHCP, Windows activation).
- **VPC Traffic Mirroring** — copies actual packets from an ENI to a monitoring appliance for deep packet inspection.
- **Reachability Analyzer** — static configuration analysis between two endpoints; tells you *which* component (route table, NACL, security group) blocks a path, without sending packets.
- **Network Access Analyzer** — verifies that network access matches your intent (e.g., "no path from the internet to database subnets").
- **CloudWatch Internet Monitor** — measures internet performance and availability affecting your users.
- **CloudWatch Network Monitor** — monitors hybrid network performance between on-premises and AWS.
- **Transit Gateway Network Manager** — visualize and monitor a global network.
- Key metrics: `ProcessedBytes` and `ActiveFlowCount` on NAT gateways and load balancers, `TargetResponseTime`, `SurgeQueueLength`/`RejectedConnectionCount`, EC2 `NetworkIn/Out` and the ENA driver's `bw_in_allowance_exceeded` / `pps_allowance_exceeded` counters (which reveal that you've hit instance network limits).

---

# 8. Worked Scenarios

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

# 9. Quick Decision Table

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
