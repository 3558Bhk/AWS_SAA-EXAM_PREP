# SAA-C03 Full-Length Mock Exam — 65 Questions

**Time limit: 130 minutes. Passing target: 52/65 (80%) — aim higher than the real 72% to leave margin.**

Domain weighting of this mock: D1 Security 20 · D2 Resilience 17 · D3 Performance 16 · D4 Cost 12.
Do not look at the answer key until you finish. Mark questions you guessed — review those even if you got them right.

---

## Questions

**1.** A company needs its EC2 application to retrieve a database password that rotates every 30 days without code redeployments. What should be used?
A. Store the password in the AMI
B. AWS Secrets Manager with automatic rotation, accessed via an IAM role
C. An encrypted S3 object with public read
D. An environment variable set at launch

**2.** Which policy type sets the maximum permissions an IAM role can ever have, without granting anything?
A. Resource-based policy
B. Permissions boundary
C. Trust policy
D. Session token

**3.** A solutions architect must block a specific IP range from reaching all instances in a subnet. What should be used?
A. Security group deny rule
B. Network ACL inbound deny rule
C. IAM policy
D. Route table entry

**4.** A company must prevent all member accounts from launching resources outside two approved Regions. What is MOST efficient?
A. IAM policies attached to every user
B. An SCP denying actions when `aws:RequestedRegion` is not in the approved list
C. AWS Config rules
D. CloudTrail alarms

**5.** Which two are the customer's responsibility for an application on Amazon EC2? (Choose TWO)
A. Patching the guest operating system
B. Securing the hypervisor
C. Configuring security group rules
D. Maintaining data center physical security
E. Replacing failed hardware

**6.** An application in a private subnet must call the AWS KMS API without traversing the internet. What should be created?
A. NAT gateway
B. Interface VPC endpoint for KMS
C. Gateway VPC endpoint for KMS
D. Internet gateway

**7.** A company wants 600 employees in its corporate Active Directory to access 18 AWS accounts with temporary credentials and no IAM users. What should be used?
A. AWS IAM Identity Center with AD as the identity source
B. IAM users synchronized by a script
C. Amazon Cognito identity pools
D. Access keys distributed by email

**8.** Which S3 configuration guarantees that objects cannot be deleted by anyone, including the root user, for 5 years?
A. Versioning with MFA Delete
B. Object Lock in governance mode
C. Object Lock in compliance mode
D. A restrictive bucket policy

**9.** An EC2 instance must be administered by operators with no SSH keys, no bastion host, and no inbound ports open. What should be used?
A. AWS Systems Manager Session Manager
B. EC2 key pairs over port 22 restricted by SG
C. AWS Client VPN with SSH
D. A NAT gateway

**10.** Which AWS service continuously analyzes CloudTrail, VPC Flow Logs, and DNS logs to detect threats?
A. Amazon Macie
B. Amazon GuardDuty
C. AWS Config
D. AWS Trusted Advisor

**11.** An existing unencrypted EBS volume must be encrypted. What is the correct sequence?
A. Enable encryption on the volume in place
B. Snapshot the volume, copy the snapshot with encryption enabled, create a new volume from the encrypted copy
C. Detach and reattach the volume with encryption
D. Use AWS Backup to encrypt in place

**12.** Which condition key restricts S3 bucket access to principals within the company's AWS Organization?
A. `aws:SourceIp`
B. `aws:PrincipalOrgID`
C. `s3:x-amz-acl`
D. `aws:SecureTransport`

**13.** A web application must be protected from SQL injection and have rate limiting per client IP. What should be deployed?
A. AWS Shield Standard
B. AWS WAF on the Application Load Balancer
C. Network ACLs
D. Amazon Inspector

**14.** A company requires that keys never be accessible to AWS and must meet FIPS 140-2 Level 3. What should be used?
A. AWS KMS AWS managed keys
B. AWS CloudHSM
C. S3 SSE-S3
D. Secrets Manager

**15.** Which two actions improve root user security? (Choose TWO)
A. Enable MFA on the root user
B. Create root access keys for automation
C. Delete any existing root access keys
D. Use root for daily administration
E. Share root credentials with the ops team

**16.** A third-party analytics vendor requires read access to your S3 data. What is the MOST secure approach?
A. Make the bucket public
B. Create an IAM user and share the access keys
C. Create a cross-account IAM role with an ExternalId condition in the trust policy
D. Send presigned URLs daily by email

**17.** Which service discovers and classifies sensitive data such as credit card numbers stored in Amazon S3?
A. Amazon Macie
B. Amazon GuardDuty
C. AWS Security Hub
D. Amazon Detective

**18.** An architecture requires all traffic to a bucket to use TLS. Which bucket policy element enforces this?
A. Deny when `aws:SecureTransport` is false
B. Allow when `s3:x-amz-server-side-encryption` is present
C. Deny when `aws:PrincipalOrgID` is absent
D. Allow only HTTPS in the NACL

**19.** Which service automates the creation of a secure multi-account landing zone with a log archive account and preventive guardrails?
A. AWS Organizations
B. AWS Control Tower
C. AWS Service Catalog
D. AWS Config

**20.** A company must centrally manage, encrypt, and retain backups for EBS, RDS, DynamoDB, and EFS across 12 accounts with cross-Region copies. What should be used?
A. AWS Backup with organization backup policies
B. Custom Lambda scripts
C. Data Lifecycle Manager only
D. S3 Cross-Region Replication

**21.** A web tier must survive the failure of an entire Availability Zone. Which design is correct?
A. One large instance with an Elastic IP
B. An Auto Scaling group spanning three AZs behind an Application Load Balancer
C. Two instances in the same AZ behind an ALB
D. A cluster placement group in one AZ

**22.** An ecommerce platform must process orders exactly once and in order per customer. Which service should be used?
A. SQS standard queue
B. SQS FIFO queue with the customer ID as the message group ID
C. SNS standard topic
D. EventBridge

**23.** Which DR strategy keeps data replicated continuously and a minimal core running, with application servers started only during failover?
A. Backup and restore
B. Pilot light
C. Warm standby
D. Multi-site active-active

**24.** A stateful legacy application cannot be modified and stores sessions locally. What enables it to run behind a load balancer?
A. Sticky sessions on the ALB
B. Disabling health checks
C. Using an NLB only
D. Cross-zone load balancing

**25.** Which Route 53 configuration sends all traffic to a primary Region and automatically switches to a standby Region if the primary endpoint fails?
A. Weighted routing
B. Failover routing with health checks
C. Geolocation routing
D. Simple routing

**26.** An application invokes a chain of Lambda functions with conditional logic and needs built-in retries and visual tracking. What should be used?
A. AWS Step Functions
B. Amazon SQS
C. Amazon EventBridge rules
D. AWS Batch

**27.** Which configuration gives the fastest automatic failover for a relational database within one Region?
A. Read replica with manual promotion
B. RDS Multi-AZ (or Multi-AZ DB cluster)
C. Daily snapshots
D. Cross-Region replica

**28.** An image upload must trigger four independent downstream services, each able to retry on its own. What design is BEST?
A. S3 event → SNS topic → four SQS queues → four consumers
B. S3 event → one Lambda calling all four services
C. S3 event → one SQS queue → one consumer
D. Cron job polling the bucket

**29.** A fleet of workers processes an SQS queue. What metric should drive Auto Scaling?
A. CPUUtilization only
B. ApproximateNumberOfMessagesVisible / backlog per instance
C. NetworkOut
D. DiskReadOps

**30.** Which design removes a single point of failure for outbound internet access in a three-AZ VPC?
A. One NAT gateway in one AZ
B. One NAT gateway per AZ with AZ-local routes
C. An internet gateway per subnet
D. A NAT instance in a private subnet

**31.** An application must continue processing if an entire Region fails, with a NoSQL datastore writable in both Regions. What should be used?
A. DynamoDB global tables
B. DynamoDB with PITR
C. RDS Multi-AZ
D. ElastiCache replication groups

**32.** Which feature allows an Auto Scaling group to gradually replace all instances with a new AMI while maintaining a minimum healthy percentage?
A. Instance refresh
B. Lifecycle hooks
C. Scheduled scaling
D. Warm pools

**33.** What is the PRIMARY benefit of immutable infrastructure?
A. Lower storage costs
B. Elimination of configuration drift and simple rollback by redeploying a previous image
C. Faster network throughput
D. Reduced IAM complexity

**34.** A standby DR environment must scale to full production capacity during failover. What must be checked in advance?
A. Service quotas in the DR Region
B. The AZ names match
C. That CloudFront is enabled
D. That Reserved Instances are purchased in the primary Region

**35.** Which service provides a service map and latency breakdown across microservices?
A. AWS X-Ray
B. VPC Flow Logs
C. AWS Config
D. CloudTrail

**36.** Which two statements describe Amazon Aurora? (Choose TWO)
A. Storage is replicated six ways across three Availability Zones
B. It supports up to 5 read replicas
C. It supports up to 15 read replicas with typically sub-10 ms lag
D. Storage must be pre-provisioned and cannot grow
E. It is only compatible with Oracle

**37.** Thousands of EC2 instances need a shared, elastic POSIX file system accessible across AZs. Which service?
A. Amazon EBS
B. Amazon EFS
C. Amazon S3
D. Instance store

**38.** A data warehouse workload needs high sequential throughput at the lowest block-storage cost. Which EBS type?
A. gp3
B. io2
C. st1
D. sc1

**39.** Which S3 feature allows SQL filtering of a single object server-side to reduce data returned?
A. S3 Select
B. S3 Batch Operations
C. S3 Inventory
D. S3 Storage Lens

**40.** An application needs microsecond read latency for a DynamoDB table with minimal code change. What should be added?
A. ElastiCache for Memcached
B. DynamoDB Accelerator (DAX)
C. A global secondary index
D. Read replicas

**41.** Which compute option is BEST for an unpredictable workload with thousands of short executions per day and long idle periods?
A. A reserved m6i.xlarge instance
B. AWS Lambda
C. ECS on EC2 with minimum 2 instances
D. Dedicated Hosts

**42.** A memory-intensive in-memory analytics engine requires 1 TB of RAM. Which instance family?
A. C family
B. R or X family
C. T family
D. D family

**43.** Which combination provides the lowest inter-node network latency for a tightly coupled HPC job?
A. Spread placement group across three AZs
B. Cluster placement group with EFA-enabled instances
C. Instances in separate VPCs with peering
D. Partition placement group across Regions

**44.** A company must connect 35 VPCs and two data centers with transitive routing and central route management. What should be used?
A. VPC peering mesh
B. AWS Transit Gateway
C. AWS PrivateLink
D. Multiple internet gateways

**45.** Which service delivers streaming data to Amazon S3 in Parquet format with no shard management?
A. Amazon Kinesis Data Streams
B. Amazon Data Firehose
C. Amazon MSK
D. Amazon SQS

**46.** Which service provides serverless SQL queries directly against data in Amazon S3?
A. Amazon Athena
B. Amazon Redshift provisioned
C. Amazon RDS
D. Amazon EMR

**47.** A Kinesis stream shows throttling on one shard while others are idle. What is the cause?
A. Retention period too long
B. A poorly chosen, low-cardinality partition key
C. Too few consumers
D. Enhanced fan-out enabled

**48.** Which service converts CSV data in a data lake to Parquet and populates a central metadata catalog?
A. AWS Glue
B. Amazon QuickSight
C. AWS DataSync
D. Amazon Comprehend

**49.** Which network service should be used for a global application over UDP requiring two static IP addresses?
A. Amazon CloudFront
B. AWS Global Accelerator
C. Route 53 weighted routing
D. Application Load Balancer

**50.** An Aurora cluster must serve read-only analytics queries across all replicas automatically. Which endpoint should the application use?
A. Writer endpoint
B. Reader endpoint
C. Instance endpoint
D. VPC endpoint

**51.** A steady production workload will run for three years and the company wants maximum savings with flexibility to change instance families and Regions. What should be purchased?
A. Standard Reserved Instances
B. Compute Savings Plan
C. Spot Instances
D. On-Demand Capacity Reservations

**52.** Batch jobs run nightly, are fault tolerant, and can be restarted. Which purchasing option is cheapest?
A. On-Demand
B. Spot Instances
C. Dedicated Hosts
D. Convertible RIs

**53.** Objects are hot for 30 days, cold afterwards, and must be retained 7 years with 12-hour retrieval acceptable. What is cheapest?
A. S3 Standard for all 7 years
B. Lifecycle: Standard → Standard-IA at 30 days → Glacier Deep Archive at 90 days → expire at 7 years
C. S3 Intelligent-Tiering only
D. S3 One Zone-IA for all 7 years

**54.** Private instances transfer 80 TB/month to S3 through a NAT gateway. What reduces cost MOST?
A. A second NAT gateway
B. An S3 gateway VPC endpoint
C. S3 Transfer Acceleration
D. Moving instances to public subnets

**55.** Which tool provides resource-level, hourly cost data suitable for Athena analysis?
A. AWS Cost and Usage Report
B. AWS Budgets
C. AWS Pricing Calculator
D. Trusted Advisor

**56.** A relational database is used a few hours per week and idle otherwise. Which option is cheapest?
A. Aurora Serverless v2
B. RDS Multi-AZ with reserved instances
C. A large provisioned Aurora cluster
D. Redshift

**57.** Which two actions reduce S3 costs for a versioned bucket with heavy multipart uploads? (Choose TWO)
A. Lifecycle rule to expire noncurrent versions
B. Lifecycle rule to abort incomplete multipart uploads
C. Enable Transfer Acceleration
D. Enable Cross-Region Replication
E. Disable encryption

**58.** Fifteen low-traffic applications each use a dedicated ALB. What reduces cost?
A. Consolidate behind one ALB using host/path-based routing
B. Replace each ALB with an NLB
C. Enable cross-zone load balancing
D. Add CloudFront to each

**59.** Which migration removes commercial database licensing costs with minimal application code change for a SQL Server app?
A. Babelfish for Aurora PostgreSQL via SCT and DMS
B. Lift and shift to EC2 with SQL Server
C. Amazon DynamoDB
D. Amazon Neptune

**60.** A company has 20 unattached Elastic IP addresses. What should be done?
A. Release them, since idle public IPv4 addresses are billed hourly
B. Keep them; they are free when unattached
C. Attach them to the NAT gateway
D. Convert them to private IPs

**61.** Which option reduces DynamoDB costs for a steady, predictable workload?
A. On-demand capacity
B. Provisioned capacity with auto scaling plus reserved capacity
C. Global tables in three Regions
D. Larger item sizes

**62.** Which two increase a CloudFront cache hit ratio and reduce origin cost? (Choose TWO)
A. Remove unnecessary cookies and query strings from the cache key
B. Increase TTLs for static content
C. Forward all headers to the origin
D. Set TTL to zero
E. Disable compression

**63.** A workload has a predictable baseline of 30 instances and unpredictable peaks to 90. What is the MOST cost-effective strategy?
A. 90 Reserved Instances
B. Savings Plans for the 30-instance baseline plus On-Demand/Spot for peaks
C. All On-Demand
D. All Spot

**64.** Which service gives ML-based right-sizing recommendations for EC2, EBS, Lambda, and Fargate?
A. AWS Compute Optimizer
B. AWS Config
C. Amazon Inspector
D. AWS Systems Manager

**65.** A dev/test environment currently mirrors production, including Multi-AZ RDS, and runs 24/7. What is the MOST appropriate optimization?
A. Single-AZ RDS, burstable instances, and scheduled shutdown outside working hours
B. Purchase 3-year All Upfront RIs for dev
C. Move dev to Dedicated Hosts
D. Keep it identical for parity

---
---

# Answer Key

| # | Ans | # | Ans | # | Ans | # | Ans | # | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 14 | B | 27 | B | 40 | B | 53 | B |
| 2 | B | 15 | A,C | 28 | A | 41 | B | 54 | B |
| 3 | B | 16 | C | 29 | B | 42 | B | 55 | A |
| 4 | B | 17 | A | 30 | B | 43 | B | 56 | A |
| 5 | A,C | 18 | A | 31 | A | 44 | B | 57 | A,B |
| 6 | B | 19 | B | 32 | A | 45 | B | 58 | A |
| 7 | A | 20 | A | 33 | B | 46 | A | 59 | A |
| 8 | C | 21 | B | 34 | A | 47 | B | 60 | A |
| 9 | A | 22 | B | 35 | A | 48 | A | 61 | B |
| 10 | B | 23 | B | 36 | A,C | 49 | B | 62 | A,B |
| 11 | B | 24 | A | 37 | B | 50 | B | 63 | B |
| 12 | B | 25 | B | 38 | C | 51 | B | 64 | A |
| 13 | B | 26 | A | 39 | A | 52 | B | 65 | A |

---

# Explanations (condensed)

1. **B** — Secrets Manager rotates natively; the role grants retrieval without stored credentials.
2. **B** — Permissions boundaries cap maximum permissions and never grant.
3. **B** — Only NACLs support deny rules at subnet level.
4. **B** — SCPs enforce Region restrictions org-wide in one place.
5. **A,C** — Guest OS and security group configuration are customer responsibilities in IaaS.
6. **B** — KMS requires an interface endpoint; only S3 and DynamoDB use gateway endpoints.
7. **A** — Identity Center federates an existing directory across many accounts with temporary credentials.
8. **C** — Compliance mode is immutable even for root.
9. **A** — Session Manager needs no inbound ports, keys, or bastion.
10. **B** — GuardDuty is the managed threat-detection service.
11. **B** — Encryption cannot be applied in place; snapshot → encrypted copy → new volume.
12. **B** — `aws:PrincipalOrgID` matches all principals in the organization.
13. **B** — WAF provides SQLi managed rules and rate-based rules.
14. **B** — CloudHSM is single-tenant FIPS 140-2 Level 3 hardware you alone control.
15. **A,C** — Enable MFA and remove root access keys.
16. **C** — Cross-account role with ExternalId prevents the confused deputy problem.
17. **A** — Macie classifies sensitive data in S3.
18. **A** — Deny on `aws:SecureTransport = false` enforces TLS.
19. **B** — Control Tower builds the landing zone with Log Archive/Audit accounts and guardrails.
20. **A** — AWS Backup supports all those services, cross-Region copy, and org policies.
21. **B** — Multi-AZ ASG behind an ALB survives AZ loss.
22. **B** — FIFO with a per-customer message group gives ordering plus exactly-once.
23. **B** — Pilot light keeps data replicated and a minimal core running.
24. **A** — Sticky sessions accommodate local session state.
25. **B** — Failover routing with health checks is active-passive DNS.
26. **A** — Step Functions provides orchestration, retries, and visual workflows.
27. **B** — Multi-AZ provides automatic failover within a Region.
28. **A** — SNS fan-out to dedicated SQS queues gives independent retries and DLQs.
29. **B** — Queue backlog is the true demand signal for workers.
30. **B** — NAT gateways are AZ-scoped; one per AZ removes the SPOF and cross-AZ fees.
31. **A** — DynamoDB global tables are multi-Region and multi-active.
32. **A** — Instance refresh performs rolling replacement with a healthy-percentage guardrail.
33. **B** — Immutability eliminates drift and makes rollback a redeploy.
34. **A** — Quotas are per-Region; verify before relying on failover scaling.
35. **A** — X-Ray provides distributed tracing and service maps.
36. **A,C** — Aurora stores 6 copies across 3 AZs and supports 15 low-lag replicas.
37. **B** — EFS is the elastic, multi-AZ, shared POSIX file system.
38. **C** — st1 is throughput-optimized HDD for sequential big-data workloads.
39. **A** — S3 Select filters a single object with SQL server-side.
40. **B** — DAX is API-compatible and delivers microsecond reads.
41. **B** — Lambda costs nothing when idle and scales automatically.
42. **B** — R/X families are memory optimized.
43. **B** — Cluster placement group plus EFA gives the lowest latency.
44. **B** — Transit Gateway provides transitive hub-and-spoke routing at scale.
45. **B** — Firehose is serverless and converts records to Parquet.
46. **A** — Athena queries S3 with serverless SQL.
47. **B** — A low-cardinality partition key creates a hot shard.
48. **A** — Glue performs the ETL and maintains the Data Catalog.
49. **B** — Global Accelerator supports UDP and static anycast IPs.
50. **B** — The reader endpoint load-balances across Aurora Replicas.
51. **B** — Compute Savings Plans maximize flexibility at up to 66% savings.
52. **B** — Interruptible batch is the Spot use case.
53. **B** — Lifecycle tiering to Deep Archive is cheapest for a known pattern.
54. **B** — S3 gateway endpoints are free and bypass NAT processing charges.
55. **A** — The CUR is the granular, Athena-queryable billing dataset.
56. **A** — Aurora Serverless v2 avoids paying for idle capacity.
57. **A,B** — Noncurrent versions and abandoned multipart parts are billed but invisible in listings.
58. **A** — One ALB with routing rules removes 14 hourly charges.
59. **A** — Babelfish lets Aurora PostgreSQL accept T-SQL, minimizing rewrite.
60. **A** — Idle public IPv4 addresses are billed hourly.
61. **B** — Provisioned plus auto scaling and reserved capacity is cheapest for predictable load.
62. **A,B** — Narrower cache keys and longer TTLs raise hit ratio.
63. **B** — Commit to the baseline only; cover peaks with On-Demand/Spot.
64. **A** — Compute Optimizer gives ML right-sizing recommendations.
65. **A** — Non-production does not need production-grade availability or 24/7 runtime.

---

## Scoring Guide

| Score | Meaning |
|---|---|
| 58–65 (89%+) | Comfortably ready — book the exam |
| 52–57 (80–88%) | Ready; review your wrong answers and the relevant notes.md |
| 45–51 (69–78%) | Borderline — study the two weakest domains for a week and retake |
| < 45 | Re-read all 14 notes files and redo the per-task question sets first |

**Per-domain breakdown:** Q1–20 = Domain 1 · Q21–37 = Domain 2 · Q38–50 = Domain 3 · Q51–65 = Domain 4.
Score each block separately — any block below 70% is where your study time should go.
