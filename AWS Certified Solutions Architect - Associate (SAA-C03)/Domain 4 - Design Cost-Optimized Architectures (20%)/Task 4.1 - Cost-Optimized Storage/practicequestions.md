# Task 4.1 - Cost-Optimized Storage - Practice Questions

> **Domain 4 - Design Cost-Optimized Architectures (20%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **15 multiple-choice (single answer)** followed by **3 multiple-response (select 2+)**. Total **18**.


**Topic order in this file:** S3 Storage Classes & Lifecycle → EBS Volumes & Snapshots → Data Migration & Transfer → EFS, FSx & Shared File Storage → S3 Security, Access & Durability → Cost Management & Optimization Tools → Secrets, Parameters & Credentials → Elastic Beanstalk & Deployment


---


# Section A - Multiple Choice (one correct answer)


## S3 Storage Classes & Lifecycle


**Q1.** A media company stores 400 TB of finished video masters in Amazon S3 Standard. The files are downloaded roughly twice a year, but when they are requested the editing team needs them within minutes. The company wants the lowest possible storage cost that still meets this requirement. Which storage class should the solutions architect recommend?

- **A.** S3 Glacier Flexible Retrieval using Bulk retrieval
- **B.** S3 Glacier Instant Retrieval
- **C.** S3 Standard-Infrequent Access
- **D.** S3 Glacier Deep Archive


**Q2.** A company has enabled versioning on a 60 TB S3 bucket. Although the application deletes objects regularly, the monthly S3 bill continues to climb. What is the MOST likely cause and the correct remediation?

- **A.** Cross-Region Replication is enabled; disable replication on the destination bucket
- **B.** Noncurrent object versions are being retained indefinitely; add a lifecycle rule with NoncurrentVersionExpiration and ExpiredObjectDeleteMarker actions
- **C.** S3 Standard pricing increased; move the bucket to S3 One Zone-IA
- **D.** The bucket is in the wrong Region; migrate it to a cheaper Region


**Q3.** A new analytics dataset is being uploaded to Amazon S3. The data science team cannot predict how frequently the objects will be read, and management has explicitly said they do not want to risk paying retrieval fees. Which storage class meets these requirements with the lowest administrative effort?

- **A.** S3 Glacier Instant Retrieval
- **B.** S3 Standard with a 30-day lifecycle transition to S3 One Zone-IA
- **C.** S3 Intelligent-Tiering
- **D.** S3 Standard-Infrequent Access


**Q4.** A company must retain 5 PB of regulatory records for 10 years. The records will almost certainly never be read, but if an auditor requests them a 48-hour turnaround is acceptable. Which option is the MOST cost-effective?

- **A.** Store the records on Amazon EBS sc1 volumes attached to a stopped EC2 instance
- **B.** Store the records in S3 Glacier Flexible Retrieval
- **C.** Store the records in S3 Glacier Deep Archive
- **D.** Store the records in S3 One Zone-IA


**Q5.** A data engineering team writes millions of 20 KB sensor files to Amazon S3 each day. A lifecycle rule transitions them to S3 Glacier Deep Archive after 30 days, but the bill did not fall as expected. What is the MOST likely explanation?

- **A.** Objects smaller than the 40 KB minimum billable size for Deep Archive are each billed at 40 KB, and each transition incurs a per-object request charge
- **B.** Lifecycle transitions only apply to objects uploaded after the rule was created
- **C.** Glacier Deep Archive does not support objects under 1 MB, so the transitions silently failed
- **D.** S3 Glacier Deep Archive is more expensive than S3 Standard in most Regions


**Q6.** A solutions architect needs data-driven evidence for when objects in a 90 TB bucket should transition to S3 Standard-IA. Which tool provides per-bucket and per-prefix access pattern analysis with recommended transition ages?

- **A.** S3 Storage Class Analysis
- **B.** S3 Inventory
- **C.** Amazon Macie
- **D.** AWS Compute Optimizer


**Q7.** An application performs large multipart uploads to Amazon S3, but network interruptions frequently abort them. The storage team notices the bucket's billed size is far larger than the sum of the objects listed in the console. What should be done?

- **A.** Switch the bucket to S3 Intelligent-Tiering
- **B.** Enable S3 Versioning to consolidate the partial uploads
- **C.** Add a lifecycle rule with an AbortIncompleteMultipartUpload action after 7 days
- **D.** Enable S3 Transfer Acceleration to prevent upload failures


## EBS Volumes & Snapshots


**Q8.** An operations review finds 350 Amazon EBS gp2 volumes provisioned at 1 TiB each purely so that each volume delivers 3,000 IOPS, even though actual capacity used is under 200 GiB per volume. What change will reduce cost the MOST while preserving performance?

- **A.** Enable Fast Snapshot Restore on all volumes
- **B.** Migrate the volumes to st1 throughput-optimized HDD
- **C.** Migrate the volumes to gp3 and provision 3,000 IOPS independently of capacity, then reduce the allocated size
- **D.** Migrate the volumes to io2 and provision 3,000 IOPS


**Q9.** A company keeps 7 years of monthly EBS snapshots for compliance. The snapshots are never restored except during an annual audit, where a 24-72 hour restore time is acceptable. Which action reduces snapshot storage cost the MOST?

- **A.** Convert the snapshots into AMIs
- **B.** Move the old snapshots to the EBS Snapshot Archive tier
- **C.** Enable Fast Snapshot Restore on the archived snapshots
- **D.** Copy the snapshots to a second Region for redundancy


## Data Migration & Transfer


**Q10.** A company runs an on-premises tape backup library and wants to eliminate the cost of tape media, tape drives and offsite vaulting while continuing to use its existing backup software unchanged. Which AWS service should it use?

- **A.** AWS Storage Gateway - Tape Gateway
- **B.** AWS Storage Gateway - Volume Gateway in stored mode
- **C.** AWS DataSync
- **D.** AWS Backup


## EFS, FSx & Shared File Storage


**Q11.** An Amazon EFS file system holds 45 TB of engineering data, but monitoring shows only about 3 TB is accessed in any given month. The team wants to cut cost without changing the mount points or application code. What should the solutions architect do?

- **A.** Recreate the file system using EFS One Zone and copy the data across
- **B.** Migrate all of the data to Amazon S3 Glacier Deep Archive
- **C.** Change the throughput mode from Elastic to Provisioned
- **D.** Enable EFS lifecycle management to transition files not accessed for 30 days to the EFS Infrequent Access and Archive storage classes


## S3 Security, Access & Durability


**Q12.** A research organisation publishes a 300 TB open dataset in Amazon S3. Thousands of external universities download subsets of it, and the data transfer charges have become unsustainable. The organisation wants consumers to bear the cost of their own downloads. What should it configure?

- **A.** Serve the dataset through Amazon CloudFront with a restrictive price class
- **B.** Move the dataset to S3 One Zone-IA
- **C.** Enable S3 Transfer Acceleration on the bucket
- **D.** Enable Requester Pays on the bucket


## Cost Management & Optimization Tools


**Q13.** A company with 40 AWS accounts wants a single view of S3 usage and activity across the organisation, including recommendations such as which buckets lack lifecycle rules or have excessive noncurrent versions. Which service provides this?

- **A.** AWS Trusted Advisor
- **B.** AWS Cost Explorer
- **C.** Amazon S3 Storage Lens
- **D.** Amazon S3 Inventory


## Secrets, Parameters & Credentials


**Q14.** Without _____, you must either create multiple AWS accounts-each with its own billing and subscriptions to AWS products-or your employees must share the security credentials of a single AWS account.

- **A.** Amazon Glacier
- **B.** Amazon RDS
- **C.** Amazon EMR
- **D.** Amazon IAM


## Elastic Beanstalk & Deployment


**Q15.** Your company runs an Amazon Elastic Compute Cloud (Amazon EC2) instance periodically to perform a batch processing job on a large and growing filesystem. At the end of the batch job, you shut down the Amazon EC2 instance to save money but need to persist the filesystem on the Amazon EC2 instance from the previous batch runs. What AWS Cloud service can you leverage to meet these requirements?

- **A.** Amazon DynamoDB
- **B.** Amazon Elastic Block Store (Amazon EBS)
- **C.** AWS CloudFormation
- **D.** Amazon Glacier


# Section B - Multiple Response (select all that apply)


## S3 Storage Classes & Lifecycle


**Q16.** A solutions architect is designing a lifecycle policy for application log files in Amazon S3. Logs are queried heavily for 30 days, occasionally for the next 11 months, and must then be retained for 6 more years for compliance before deletion. Which TWO configurations are the most cost-effective parts of this policy? (Select 2.) **(Select 2.)**

- **A.** Transition objects to S3 One Zone-IA after 1 day
- **B.** Transition objects to S3 Standard-Infrequent Access after 30 days
- **C.** Transition objects to S3 Glacier Instant Retrieval after 7 days
- **D.** Expire objects after 90 days
- **E.** Transition objects to S3 Glacier Deep Archive after 365 days


## EBS Volumes & Snapshots


**Q17.** An audit of a production account reveals significant storage waste. Which TWO findings represent charges the company is paying for resources that deliver no value? (Select 2.) **(Select 2.)**

- **A.** S3 objects stored in S3 Intelligent-Tiering Frequent Access tier
- **B.** Elastic IP addresses that are allocated but not associated with a running resource
- **C.** EBS snapshots used as the source for the current AMI
- **D.** EBS volumes in the available state that are not attached to any instance
- **E.** gp3 volumes running at 40% of their provisioned IOPS


## Data Migration & Transfer


**Q18.** A company is migrating 600 TB of archival data from an on-premises NAS to AWS. The site has a 200 Mbps internet link shared with production traffic, and the migration must complete within one month. Which TWO actions together form the most cost-effective and feasible approach? (Select 2.) **(Select 2.)**

- **A.** Use AWS DataSync over the existing internet link to transfer all 600 TB
- **B.** Order multiple AWS Snowball Edge Storage Optimized devices to transfer the bulk of the data
- **C.** Provision a 10 Gbps AWS Direct Connect link for the one-month migration
- **D.** Apply an S3 lifecycle rule to move the ingested data to S3 Glacier Deep Archive
- **E.** Enable S3 Transfer Acceleration and upload over the internet link


---


# Answer Key & Explanations


**Q1. B**  
_S3 Storage Classes & Lifecycle_  
S3 Glacier Instant Retrieval is designed for archive data that is accessed about once a quarter and still requires millisecond retrieval. It is roughly 68% cheaper than S3 Standard. Deep Archive and Glacier Flexible Retrieval cannot return objects in minutes at their cheapest tiers, and Standard-IA is more expensive than Glacier Instant Retrieval for data touched only twice a year.

**Q2. B**  
_S3 Storage Classes & Lifecycle_  
In a versioned bucket a DELETE only creates a delete marker, so every previous version keeps billing. Lifecycle rules using NoncurrentVersionExpiration remove old versions and ExpiredObjectDeleteMarker cleans up orphaned delete markers. S3 Storage Lens will confirm how much of the bucket is noncurrent versions.

**Q3. C**  
_S3 Storage Classes & Lifecycle_  
S3 Intelligent-Tiering automatically moves objects between frequent, infrequent and archive instant access tiers based on observed access patterns, and charges no retrieval fees for the automatic tiers. It only adds a small per-object monitoring charge, making it the standard answer for unknown or changing access patterns.

**Q4. C**  
_S3 Storage Classes & Lifecycle_  
S3 Glacier Deep Archive is the lowest-cost AWS storage, designed for data retained 7-10 years and retrieved rarely, with Standard retrieval in 12 hours and Bulk in 48 hours. It has a 180-day minimum storage duration, which is irrelevant for a 10-year retention requirement.

**Q5. A**  
_S3 Storage Classes & Lifecycle_  
Archive classes carry a minimum billable object size (40 KB for Glacier Flexible Retrieval and Deep Archive, 128 KB for IA and Glacier Instant Retrieval) plus a per-object transition request charge. For very small objects these can exceed the storage savings. Aggregating the files into larger objects before archiving solves it.

**Q6. A**  
_S3 Storage Classes & Lifecycle_  
S3 Storage Class Analysis observes access patterns on a bucket, prefix or tag filter and reports how much data is infrequently accessed, recommending an appropriate age for lifecycle transitions. S3 Inventory lists objects and metadata but does not analyse access patterns.

**Q7. C**  
_S3 Storage Classes & Lifecycle_  
Incomplete multipart uploads leave orphaned parts that are billed indefinitely and do not appear in the object listing. An AbortIncompleteMultipartUpload lifecycle action deletes parts from uploads that were never completed, typically after 7 days.

**Q8. C**  
_EBS Volumes & Snapshots_  
gp3 decouples IOPS and throughput from capacity: every gp3 volume includes 3,000 IOPS and 125 MB/s baseline regardless of size, and gp3 is about 20% cheaper per GB than gp2. This removes the need to over-provision capacity purely to obtain IOPS. io2 is far more expensive and st1 cannot deliver 3,000 IOPS.

**Q9. B**  
_EBS Volumes & Snapshots_  
EBS Snapshot Archive stores rarely-needed snapshots up to 75% cheaper than standard snapshot storage, with a 90-day minimum retention and a 24-72 hour restore time, which fits an annual audit. Fast Snapshot Restore and cross-Region copies both increase cost.

**Q10. A**  
_Data Migration & Transfer_  
Tape Gateway presents a virtual tape library over iSCSI VTL so existing backup applications continue to write 'tapes', while the data is stored in Amazon S3 and can be archived to S3 Glacier Flexible Retrieval or Deep Archive. This removes physical tape hardware and offsite storage costs with no change to backup software.

**Q11. D**  
_EFS, FSx & Shared File Storage_  
EFS lifecycle management transparently moves files that have not been accessed for a configured period into the IA and Archive storage classes, saving up to about 92% for cold data, while keeping the same file system, mount targets and paths. Files move back transparently on access if that option is enabled.

**Q12. D**  
_S3 Security, Access & Durability_  
With Requester Pays enabled, the requester rather than the bucket owner pays for requests and data transfer out. Requesters must be authenticated AWS principals and must include the request-payer header. This is the standard pattern for large shared or open datasets.

**Q13. C**  
_Cost Management & Optimization Tools_  
S3 Storage Lens delivers organisation-wide visibility into object storage usage and activity trends, with built-in cost-efficiency recommendations. It integrates with AWS Organizations to aggregate metrics across all accounts.

**Q14. D**  
_Secrets, Parameters & Credentials_  
Without IAM, however, you must either create multiple AWS accounts—each with its own billing and subscriptions to AWS products—or your employees must share the security credentials of a single AWS account. Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html

**Q15. B**  
_Elastic Beanstalk & Deployment_  
Amazon EBS provides persistent block-level storage volumes for use with Amazon EC2 instances on the AWS Cloud. Amazon DynamoDB, Amazon Glacier, and AWS CloudFormation do not provide persistent block-level storage for Amazon EC2 instances. Amazon DynamoDB provides managed NoSQL databases. Amazon Glacier provides low- cost archival storage. AWS CloudFormation gives developers and systems administrators an easy way to create and manage a collection of related AWS resources.

**Q16. B, E**  
_S3 Storage Classes & Lifecycle_  
Standard-IA is appropriate once the heavy query period ends at 30 days (it also satisfies the 30-day minimum before an IA transition is allowed). After the occasional-access year, Glacier Deep Archive is the cheapest home for the remaining six years of compliance retention. Expiring at 90 days would violate the retention requirement.

**Q17. B, D**  
_EBS Volumes & Snapshots_  
Unattached EBS volumes continue to bill at full price, and allocated-but-unassociated Elastic IP addresses carry an hourly charge. AWS Trusted Advisor flags both. Snapshots backing a current AMI are required, under-utilised provisioned IOPS is a rightsizing opportunity rather than pure waste, and Intelligent-Tiering frequent-access objects are correctly placed.

**Q18. B, D**  
_Data Migration & Transfer_  
600 TB over a shared 200 Mbps link would take well over a year, so Snowball Edge devices are the only feasible option in the timeframe. Once the archival data lands in S3, a lifecycle rule to Glacier Deep Archive minimises ongoing storage cost. Provisioning Direct Connect takes weeks to months and is not justified for a one-off migration.
