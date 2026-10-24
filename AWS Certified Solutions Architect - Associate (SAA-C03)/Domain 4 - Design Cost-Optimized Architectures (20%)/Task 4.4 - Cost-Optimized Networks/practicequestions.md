# Task 4.4 - Cost-Optimized Networks - Practice Questions

> **Domain 4 - Design Cost-Optimized Architectures (20%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **12 multiple-choice (single answer)** followed by **3 multiple-response (select 2+)**. Total **15**.


**Topic order in this file:** Data Transfer & Network Cost → CloudFront & Edge Delivery → VPC Connectivity: Endpoints, Peering, TGW → Auto Scaling & Elastic Load Balancing → Hybrid Connectivity: Direct Connect & VPN → Monitoring: CloudWatch, CloudTrail & Config → Route 53 & DNS Routing → Cost Management & Optimization Tools


---


# Section A - Multiple Choice (one correct answer)


## Data Transfer & Network Cost


**Q1.** EC2 instances in private subnets download approximately 70 TB of objects from Amazon S3 in the same Region every month. All outbound traffic currently routes through NAT gateways. Which change will reduce cost the MOST?

- **A.** Create an interface VPC endpoint for Amazon S3 in each Availability Zone
- **B.** Replace the NAT gateways with NAT instances on t4g.micro
- **C.** Create a gateway VPC endpoint for Amazon S3 and add it to the private subnets' route tables
- **D.** Enable S3 Transfer Acceleration on the bucket


**Q2.** A solutions architect is reviewing the data transfer charges for a three-tier application. Which of the following traffic flows incurs NO data transfer charge?

- **A.** Data transferred into Amazon EC2 from the internet
- **B.** Data transferred between two EC2 instances in different Availability Zones using private IP addresses
- **C.** Data transferred between two EC2 instances in the same Availability Zone using public IP addresses
- **D.** Data transferred from an EC2 instance to the internet


**Q3.** After enabling cross-zone load balancing on a Network Load Balancer that processes 40 TB per month, a company notices a significant increase in its bill. What is the explanation?

- **A.** With cross-zone load balancing enabled on an NLB, traffic sent to targets in other Availability Zones is billed as inter-AZ data transfer
- **B.** Cross-zone load balancing doubles the number of NLB nodes and therefore the hourly charge
- **C.** Cross-zone load balancing converts the NLB into an Application Load Balancer, which has higher LCU rates
- **D.** Cross-zone load balancing requires a dedicated Elastic IP in every subnet, each of which is billed hourly


**Q4.** A company's AWS bill now shows a recurring charge for public IPv4 addresses. The environment has 200 EC2 instances in private subnets, each with an Elastic IP attached for outbound internet access, plus 40 unassociated Elastic IPs left over from earlier testing. What should the solutions architect do to reduce this charge?

- **A.** Move the instances to a Region where public IPv4 addresses are free
- **B.** Convert all Elastic IPs into static private IP addresses
- **C.** Attach a second Elastic IP to each instance to distribute the charge
- **D.** Release the unassociated Elastic IPs and route outbound traffic from the private instances through shared NAT gateways instead of per-instance Elastic IPs


## CloudFront & Edge Delivery


**Q5.** A global media site serves large video and image files directly from an Amazon S3 bucket. Data transfer out to the internet is now the single largest line item on the AWS bill. Which solution reduces cost the MOST while also improving performance?

- **A.** Enable S3 Transfer Acceleration on the bucket
- **B.** Move the bucket to S3 One Zone-IA
- **C.** Serve the content through Amazon CloudFront with the S3 bucket as the origin
- **D.** Enable Requester Pays on the bucket


**Q6.** A company serves its application exclusively to customers in North America and Europe through Amazon CloudFront. It wants to reduce CloudFront costs without affecting those users. Which configuration change achieves this?

- **A.** Reduce the default TTL on all cache behaviours to zero
- **B.** Configure the distribution to use a CloudFront price class that includes only North America and Europe edge locations
- **C.** Create a separate distribution for each country
- **D.** Disable compression on the distribution


## VPC Connectivity: Endpoints, Peering, TGW


**Q7.** A company connects eight VPCs. Two of these VPCs exchange roughly 90 TB of data per month between them, while the other six exchange only small amounts of management traffic. The company currently routes everything through a Transit Gateway. How can network cost be reduced while keeping centralised routing for the low-volume VPCs?

- **A.** Add an interface VPC endpoint in each of the eight VPCs
- **B.** Replace the Transit Gateway with VPC peering connections between all eight VPCs
- **C.** Move all eight VPCs into a single VPC shared with AWS Resource Access Manager
- **D.** Create a direct VPC peering connection between the two high-volume VPCs and keep the Transit Gateway for the rest


**Q8.** An application in a private subnet makes very heavy use of Amazon ECR to pull container images and writes large volumes of logs to Amazon CloudWatch Logs, all through a NAT gateway. Which change is MOST likely to reduce network cost?

- **A.** Create interface VPC endpoints for Amazon ECR and CloudWatch Logs so the traffic bypasses the NAT gateway
- **B.** Create a gateway VPC endpoint for Amazon ECR
- **C.** Increase the NAT gateway's provisioned bandwidth
- **D.** Move the workload to a public subnet with public IP addresses


## Auto Scaling & Elastic Load Balancing


**Q9.** A microservices platform runs 28 separate Application Load Balancers, one per service, each with very low traffic. The platform team wants to reduce load balancer costs without losing per-service routing. What should they do?

- **A.** Enable cross-zone load balancing on all 28 ALBs
- **B.** Replace the ALBs with Classic Load Balancers
- **C.** Consolidate the services behind a small number of ALBs using host-based and path-based routing rules to separate target groups
- **D.** Replace each ALB with a Network Load Balancer


## Hybrid Connectivity: Direct Connect & VPN


**Q10.** An enterprise transfers about 120 TB per month from its data centre to AWS over a Site-to-Site VPN across the public internet. Network costs are high and performance is inconsistent. Which option will reduce the long-term data transfer cost the MOST?

- **A.** Route the traffic through an interface VPC endpoint
- **B.** Enable AWS Global Accelerator in front of the workload
- **C.** Provision an AWS Direct Connect connection, which offers significantly lower data transfer out rates than internet egress
- **D.** Add a second Site-to-Site VPN connection and use ECMP to increase bandwidth


## Monitoring: CloudWatch, CloudTrail & Config


**Q11.** VPC Flow Logs for a very high-traffic VPC are delivered to Amazon CloudWatch Logs, and the ingestion and storage charges now exceed the cost of the workload being monitored. Which combination of changes reduces logging cost while retaining the ability to investigate traffic?

- **A.** Disable VPC Flow Logs entirely and rely on AWS CloudTrail
- **B.** Increase the flow log aggregation interval to 10 minutes and keep delivering to CloudWatch Logs indefinitely
- **C.** Deliver the flow logs to Amazon S3 in Parquet format, reduce the captured fields, apply sampling, and add an S3 lifecycle policy
- **D.** Enable VPC Traffic Mirroring instead of flow logs


## Route 53 & DNS Routing


**Q12.** A company's Route 53 hosted zone receives billions of DNS queries per month for records that point to an Application Load Balancer and a CloudFront distribution. How can the DNS query charges be reduced?

- **A.** Move the hosted zone to a cheaper AWS Region
- **B.** Use Route 53 alias records to point to the ALB and CloudFront distribution, because alias queries to AWS resources are free
- **C.** Increase the TTL on the CNAME records to 24 hours
- **D.** Replace the hosted zone with a Route 53 Resolver inbound endpoint


# Section B - Multiple Response (select all that apply)


## Data Transfer & Network Cost


**Q13.** A solutions architect is reducing data transfer charges for a workload in a single Region. Which TWO statements about AWS data transfer pricing are correct? (Select 2.) **(Select 2.)**

- **A.** Data transferred between Availability Zones in the same Region is charged in both directions
- **B.** Traffic between EC2 instances in the same Availability Zone is always free regardless of the IP addresses used
- **C.** Data transfer out to the internet is free for the first 10 TB each month
- **D.** Gateway VPC endpoints for Amazon S3 incur a per-GB data processing charge
- **E.** Data transfer from Amazon S3 to Amazon CloudFront is free


## VPC Connectivity: Endpoints, Peering, TGW


**Q14.** A company wants to minimise NAT gateway charges for workloads in private subnets. Which TWO actions will directly reduce those charges? (Select 2.) **(Select 2.)**

- **A.** Attach an Elastic IP to every private instance
- **B.** Deploy a single NAT gateway in one Availability Zone and route all private subnets to it
- **C.** Bake application dependencies into the AMI or container image so instances do not download packages at boot
- **D.** Enable VPC Flow Logs on the NAT gateway's elastic network interface
- **E.** Create gateway VPC endpoints for Amazon S3 and Amazon DynamoDB


## Cost Management & Optimization Tools


**Q15.** A finance team has noticed an unexplained spike in network-related spend and wants to identify the source. Which TWO tools are the most appropriate? (Select 2.) **(Select 2.)**

- **A.** VPC Flow Logs analysed to identify the top talkers generating the traffic
- **B.** Amazon Inspector network reachability findings
- **C.** AWS Compute Optimizer rightsizing recommendations
- **D.** AWS Cost Explorer filtered by usage type, such as NatGateway-Bytes and DataTransfer-Out-Bytes
- **E.** AWS Config conformance packs


---


# Answer Key & Explanations


**Q1. C**  
_Data Transfer & Network Cost_  
Gateway VPC endpoints for S3 and DynamoDB are free and are added as a route table entry, so traffic bypasses the NAT gateway entirely. This removes both the NAT data-processing charge of roughly $0.045 per GB and the associated egress path. At 70 TB per month the saving is very large. Interface endpoints would work but carry hourly and per-GB charges.

**Q2. A**  
_Data Transfer & Network Cost_  
Inbound data transfer from the internet to AWS is free. Cross-AZ traffic is charged in both directions, internet egress is the most expensive common path, and traffic between instances in the same AZ is only free when it uses private IPv4 addresses - using public or Elastic IPs incurs a charge even within one AZ.

**Q3. A**  
_Data Transfer & Network Cost_  
Unlike the ALB, where cross-zone load balancing is enabled by default and free, enabling it on an NLB causes traffic crossing Availability Zones to be charged at standard inter-AZ data transfer rates in both directions. Registering a comparable number of targets in each AZ is an alternative to enabling it.

**Q4. D**  
_Data Transfer & Network Cost_  
AWS charges hourly for every in-use public IPv4 address, and unassociated Elastic IPs are also billed. Removing per-instance Elastic IPs in favour of a shared NAT gateway per Availability Zone, and releasing unused addresses, removes almost all of the charge. Adopting IPv6 with an egress-only internet gateway avoids it entirely.

**Q5. C**  
_CloudFront & Edge Delivery_  
Data transfer from Amazon S3 to CloudFront is free, CloudFront's per-GB egress rate is lower than S3's and is volume-tiered, and caching at the edge eliminates most origin requests. The result is lower transfer cost, lower request cost and lower latency. Transfer Acceleration increases cost, and storage class changes do not affect egress.

**Q6. B**  
_CloudFront & Edge Delivery_  
CloudFront price classes let you exclude the more expensive edge locations in regions where you have no users, lowering the per-GB rate. Disabling compression and reducing TTL both increase cost, because more bytes are transferred and more requests reach the origin.

**Q7. D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Transit Gateway charges per attachment-hour plus a per-GB data processing fee. VPC peering has no hourly or data-processing charge - only standard cross-AZ or cross-Region transfer rates apply. Peering the two highest-volume VPCs directly avoids the per-GB TGW fee on 90 TB while the hub keeps routing simple for the rest.

**Q8. A**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Interface endpoints (PrivateLink) carry an hourly charge per endpoint per AZ plus a per-GB processing fee that is lower than the NAT gateway's per-GB data processing charge, so for high-volume services such as ECR image pulls and CloudWatch Logs they are cheaper as well as more secure. Gateway endpoints only exist for S3 and DynamoDB.

**Q9. C**  
_Auto Scaling & Elastic Load Balancing_  
Each load balancer carries an hourly charge plus LCU charges, so 28 lightly-loaded ALBs waste the fixed hourly component 28 times over. One ALB can route to many target groups using host and path rules, which is both cheaper and simpler to operate. Enabling cross-zone load balancing does not reduce cost.

**Q10. C**  
_Hybrid Connectivity: Direct Connect & VPN_  
Direct Connect replaces internet egress rates with substantially lower DX data transfer out rates and adds a fixed port-hour charge. Above roughly tens of terabytes per month the reduced per-GB rate outweighs the port cost, and it also delivers consistent bandwidth and latency. Additional VPN tunnels still use internet egress pricing.

**Q11. C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Delivering flow logs to S3 in Parquet is far cheaper than CloudWatch Logs ingestion, custom formats let you drop unneeded fields, and lifecycle rules age the data out. CloudTrail records API activity rather than network flows, and Traffic Mirroring captures full packets and is considerably more expensive.

**Q12. B**  
_Route 53 & DNS Routing_  
Route 53 does not charge for queries answered by alias records that point to AWS resources such as ALBs, NLBs, CloudFront distributions, S3 website endpoints and API Gateway. Alias records also work at the zone apex, where CNAMEs are not permitted. Hosted zones are global, not Regional.

**Q13. A, E**  
_Data Transfer & Network Cost_  
S3-to-CloudFront origin transfer is free, which is why fronting S3 with CloudFront reduces egress cost. Cross-AZ traffic is billed at roughly $0.01 per GB in each direction. Only the first 100 GB per month of internet egress is free account-wide, same-AZ traffic is free only over private IPv4 addresses, and gateway endpoints are entirely free.

**Q14. C, E**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Gateway endpoints are free and remove S3 and DynamoDB traffic from the NAT path entirely. Eliminating boot-time package downloads removes another large source of NAT-processed bytes. Consolidating to a single NAT gateway saves hourly charges but introduces cross-AZ data transfer charges and a single point of failure, and flow logs add cost rather than reducing it.

**Q15. A, D**  
_Cost Management & Optimization Tools_  
Cost Explorer's usage-type dimension isolates exactly which transfer path is generating the charge, and VPC Flow Logs identify which resources and flows are responsible. Compute Optimizer addresses instance rightsizing, Inspector assesses security exposure, and Config evaluates resource compliance.
