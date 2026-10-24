# Task 3.1 - High-Performing and Scalable Storage - Practice Questions

> **Domain 3 - Design High-Performing Architectures (24%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **40 multiple-choice (single answer)** followed by **25 multiple-response (select 2+)**. Total **65**.


**Topic order in this file:** S3 Storage Classes & Lifecycle → DynamoDB Design & Capacity → IAM Roles, Policies & Permissions → RDS Multi-AZ, Read Replicas & Aurora → S3 Security, Access & Durability → SQS, SNS & Decoupling → VPC Security Groups & NACLs → EBS Volumes & Snapshots → EC2 Instances, AMIs & Placement → CloudFront & Edge Delivery → High Availability & Fault Tolerance → Data Migration & Transfer → AWS Organizations & Multi-Account → Disaster Recovery, Backup & RTO/RPO → EFS, FSx & Shared File Storage → Monitoring: CloudWatch, CloudTrail & Config → Elastic Beanstalk & Deployment → General Design → Lambda & Serverless Compute


---


# Section A - Multiple Choice (one correct answer)


## S3 Storage Classes & Lifecycle


**Q1.** You have 1 TB of data and want to archive the data that won't be accessed that often. Which is the most suitable Amazon AWS storage solution recommended in this case?

- **A.** ephemeral
- **B.** Glacier
- **C.** CloudFront
- **D.** EBS


**Q2.** Your company runs a web-based application that uses EC2 instances for the web front-end and RDS for the database back-end. The web application writes transaction log files to an S3 bucket and the quantity of files is becoming quite large. You have determined that it is acceptable to retain the most recent 60 days of log files and permanently delete the rest. What can you do to enable this to happen automatically?

- **A.** Use an S3 bucket policy that deletes objects that are more than 60 days old
- **B.** Use an S3 lifecycle policy to move the log files that are more than 60 days old to the GLACIER storage class
- **C.** Write a Ruby script that checks the age of objects and deletes any that are more than 60 days old
- **D.** Use an S3 lifecycle policy with object expiration configured to automatically remove objects that are more than 60 days old


**Q3.** Your company has 100TB of financial records that need to be stored for seven years by law. Experience has shown that any record more than one-year old is unlikely to be accessed. Which of the following storage plans meets these needs in the most cost efficient manner?

- **A.** Store the data on Amazon Simple Storage Service (Amazon S3) with lifecycle policies that change the storage class to Amazon Glacier after one year and delete the object after seven years.
- **B.** Store the data in Amazon Elastic MapReduce (Amazon EMR).
- **C.** Store the data on Amazon Elastic Block Store (Amazon EBS) volumes attached to t2.micro instances.
- **D.** Store the data in Amazon DynamoDB and run daily script to delete data older than seven years.


**Q4.** A customer is leveraging Amazon Simple Storage Service in eu-west-1 to store static content for a web-based property. The customer is storing objects using the Standard Storage class. Where are the customers objects replicated?

- **A.** Multiple facilities in eu-west-1
- **B.** A single facility in eu-west-1
- **C.** A single facility in eu-west-1 and a single facility in eu-central-1
- **D.** A single facility in eu-west-1 and a single facility in us-east-1


## DynamoDB Design & Capacity


**Q5.** What is the maximum write throughput I can provision for a single Dynamic DB table?

- **A.** 100,000 write capacity units
- **B.** 10,000 write capacity units
- **C.** Dynamic DB is designed to scale without limits, but if you go beyond 10,000 you have to contact AWS first.
- **D.** 1,000 write capacity units


## IAM Roles, Policies & Permissions


**Q6.** What is the advantage of read-after-write consistency for S3 buckets?

- **A.** No stale reads for GET requests in a single regions
- **B.** No stale reads for PUT of any new object in all regions
- **C.** Stale reads for PUT requests in some regions
- **D.** Higher throughput for all requests


## RDS Multi-AZ, Read Replicas & Aurora


**Q7.** What does RDS use for database and log storage?

- **A.** Local store
- **B.** EBS
- **C.** Instance store
- **D.** S3
- **E.** SSD


## S3 Security, Access & Durability


**Q8.** When you put objects in Amazon S3, what is the indication that an object was successfully stored?

- **A.** Each S3 account has a special bucket named _s3_logs. Success codes are written to this bucket with a timestamp and checksum.
- **B.** Amazon S3 is engineered for 99.999999999% durability. Therefore there is no need to confirm that data was inserted.
- **C.** A HTTP 200 result code and MD5 checksum, taken together, indicate that the operation was successful.
- **D.** A success code is inserted into the S3 object metadata.


## SQS, SNS & Decoupling


**Q9.** There is expected to be a large increase in write intensive traffic to a website you manage that registers users onto an online learning program. You are concerned about writes to the database being dropped and need to come up with a solution to ensure this does not happen. Which of the solution options below would be the best approach to take?

- **A.** Update the application to write data to an SQS queue and provision additional EC2 instances to process the data and write it to the database
- **B.** Use CloudFront to cache the writes and configure the database as a custom origin
- **C.** Use RDS in a multi-AZ configuration to distribute writes across AZs
- **D.** Update the application to write data to an S3 bucket and provision additional EC2 instances to process the data and write it to the database


## VPC Security Groups & NACLs


**Q10.** Please select the most correct answer regarding the persistence of the Amazon Instance Store

- **A.** The data on an instance store volume persists only during the life of the associated Amazon EC2 instance
- **B.** The data on an instance store volume persists even after associated Amazon EC2 instance is deleted
- **C.** The data on an instance store volume is lost when the security group rule of the associated instance is changed.


## EBS Volumes & Snapshots


**Q11.** You need to create an EBS volume to mount to an existing EC2 instance for an application that will be writing structured data to the volume. The application vendor suggests that the performance of the disk should be up to 3 IOPS per GB. You expect the capacity of the volume to grow to 2TB. Taking into account cost effectiveness, which EBS volume type would you select?

- **A.** Provisioned IOPS (IO1)
- **B.** Cold HDD (SC1)
- **C.** General Purpose (GP2)
- **D.** Throughput Optimized HDD (ST1)


**Q12.** In the 'Detailed' monitoring data available for your Amazon EBS volumes, Provisioned IOPS volumes automatically send _____ minute metrics to Amazon CloudWatch.

- **A.** 1
- **B.** 2
- **C.** 3
- **D.** 5


**Q13.** You are designing the disk configuration for an EC2 instance. The instance needs to support a MapReduce process that requires high throughput for a large dataset with large I/O sizes. You need to provision the most cost-effective storage solution option. What EBS volume type will you select? Wh t EBS l t ill l t?

- **A.** EBS General Purpose SSD
- **B.** EBS General Purpose SSD in a RAID 1 configuration
- **C.** EBS Throughput Optimized HDD
- **D.** EBS Provisioned IOPS SSD


**Q14.** A Provisioned IOPS volume must be at least __________ GB in size

- **A.** 1
- **B.** 20
- **C.** 50
- **D.** 10


**Q15.** You have a workload that requires 1 TB of durable block storage at 1,500 IOPS during normal use. Every night there is an Extract, Transform, Load (ETL) task that requires 3,000 IOPS for 15 minutes. What is the most appropriate volume type for this workload?

- **A.** Use an instance store.
- **B.** Use a general-purpose SSD volume.
- **C.** Use a Provisioned IOPS SSD volume at 3,000 IOPS.
- **D.** Use a magnetic volume.


**Q16.** What steps are required from AWS console to copy an EBS-backed AMI for a database instance cross-region?

- **A.** Create Snapshot of data volume, select Copy, select destination region
- **B.** Create Snapshot of EBS-backed AMI, select Copy Snapshot option, select destination region
- **C.** Select Copy EBS-backed AMI option and destination region
- **D.** Create Snapshot of Instance-store AMI, select Copy AMI option, select destination region
- **E.** Select copy database volume and destination region


**Q17.** When an EC2 EBS-backed (EBS root) instance is stopped, what happens to the data on any ephemeral store volumes?

- **A.** Data is automatically saved in an EBS volume.
- **B.** Data will be deleted and will no longer be accessible.
- **C.** Data is automatically saved as an EBS snapshot.
- **D.** Data is unavailable until the instance is restarted.


**Q18.** What is one key difference between an Amazon EBS-backed and an instance-store backed instance?

- **A.** Amazon EBS-backed instances can be stopped and restarted.
- **B.** Virtual Private Cloud requires EBS backed instances.
- **C.** Auto scaling requires using Amazon EBS-backed instances.
- **D.** Instance-store backed instances can be stopped and restarted.


**Q19.** You are building an automated transcription service in which Amazon EC2 worker instances process an uploaded audio file and generate a text file. You must store both of these files in the same durable storage until the text file is retrieved. You do not know what the storage capacity requirements are. Which storage option is both cost-efficient and scalable?

- **A.** Multiple instance stores
- **B.** A single Amazon S3 bucket
- **C.** Multiple Amazon EBS volume with snapshots
- **D.** A single Amazon Glacier vault


**Q20.** Is it possible to access your EBS snapshots?

- **A.** Yes, through the Amazon S3 APIs.
- **B.** No, EBS snapshots cannot be accessed; they can only be used to create a new EBS volume.
- **C.** Yes, through the Amazon EC2 APIs.
- **D.** EBS doesn't provide snapshots.


**Q21.** A customer has a single 3-TB volume on-premises that is used to hold a large repository of images and print layout files. This repository is growing at 500 GB a year and must be presented as a single logical volume. The customer is becoming increasingly constrained with their local storage capacity and wants an off-site backup of this data, while maintaining low-latency access to their frequently accessed data. Which AWS Storage Gateway configuration meets the customer requirements?

- **A.** Gateway-Stored volumes with snapshots scheduled to Amazon S3
- **B.** Gateway-Cached volumes with snapshots scheduled to Amazon S3
- **C.** Gateway-Virtual Tape Library with snapshots to Amazon S3
- **D.** Gateway-Virtual Tape Library with snapshots to Amazon Glacier


**Q22.** Out of the stripping options available for the EBS volumes, which one has the following disadvantage : 'Doubles the amount of I/O required from the instance to EBS compared to RAID 0, because you're mirroring all writes to a pair of volumes, limiting how much you can stripe.' ?

- **A.** Raid 1
- **B.** Raid
- **C.** Raid 0
- **D.** RAID 1+0 (RAID 10)


**Q23.** Can we attach an EBS volume to more than one EC2 instance at the same time?

- **A.** Only EC2-optimized EBS volumes.
- **B.** Yes.
- **C.** No
- **D.** Only in read mode.


**Q24.** If I want to run a database in an Amazon instance, which is the most recommended Amazon storage option?

- **A.** You can't run a database inside an Amazon instance.
- **B.** Amazon Instance Storage
- **C.** Amazon S3
- **D.** Amazon EBS


## EC2 Instances, AMIs & Placement


**Q25.** What storage type enable permanent attachment of volumes to EC2 instances?

- **A.** RDS
- **B.** S3
- **C.** Instance store
- **D.** TDS
- **E.** EBS


**Q26.** Select the most suitable option. The device name /dev/sda1 (within Amazon EC2) is _______________.

- **A.** Possible for EBS volumes
- **B.** Recommended for EBS volumes
- **C.** Reserved for the root device
- **D.** Recommended for instance store volumes


**Q27.** You launched an EBS-backed EC2 instance into your VPC. A requirement has come up for some high-performance ephemeral storage and so you would like to add an instance-store backed volume. How can you add the new instance store volume?

- **A.** You can specify the instance store volumes for your instance only when you launch an instance
- **B.** You can use a block device mapping to specify additional instance store volumes when you launch your instance, or you can attach additional instance store volumes after your instance is running
- **C.** You must use an Elastic Network Adapter (ENA) to add instance store volumes. First, attach an ENA, and then attach the instance store volume
- **D.** You must shutdown the instance in order to be able to add the instance store volume


**Q28.** A company is deploying a two-tier, highly available web application to AWS. Which service provides durable storage for static content while utilizing lower Overall CPU resources for the web tier?

- **A.** Amazon RDS instance
- **B.** Amazon S3
- **C.** Amazon EC2 instance store
- **D.** Amazon EBS volume


## CloudFront & Edge Delivery


**Q29.** You need to setup a distribution method for some static files. The requests will be mainly GET requests and you are expecting a high volume of GETs often exceeding 2000 per second. The files are currently stored in an S3 bucket. According to AWS best practices, what can you do to optimize performance?

- **A.** Use cross-region replication to spread the load across regions
- **B.** Use S3 Transfer Acceleration
- **C.** Use ElastiCache to cache the content
- **D.** Integrate CloudFront with S3 to cache the content


## High Availability & Fault Tolerance


**Q30.** A new Big Data application you are developing will use hundreds of EC2 instances to write data to a shared file system. The file system must be stored redundantly across multiple AZs within a region and allow the EC2 instances to concurrently access the file system. The required throughput is multiple GB per second. From the options presented which storage solution can deliver these requirements?

- **A.** Amazon EFS
- **B.** Amazon Storage Gateway
- **C.** Amazon S3
- **D.** Amazon EBS using multiple volumes in a RAID 0 configuration


## Data Migration & Transfer


**Q31.** What is the fastest and easiest method for migrating an on-premises VMware virtual machine to the AWS cloud?

- **A.** AWS Storage Gateway
- **B.** Amazon Marketplace
- **C.** EC2 Import/Export
- **D.** AWS Server Migration Service


**Q32.** Your company provides transcoding services for amateur producers to format their short films to a variety of video formats. Which service provides the best option for storing the videos?

- **A.** Amazon Relational Database Service (Amazon RDS)
- **B.** Amazon Simple Storage Service (Amazon S3)
- **C.** AWS Storage Gateway
- **D.** Amazon Glacier


**Q33.** You are designing a web application that stores static assets in an Amazon Simple Storage Service (S3) bucket. You expect this bucket to immediately receive over 150 PUT requests per second. What should you do to ensure optimal performance?

- **A.** Use a predictable naming scheme, such as sequential numbers or date time sequences, in the key names
- **B.** Add a random prefix to the key names.
- **C.** Use multi-part upload.
- **D.** Amazon S3 will automatically manage performance at this scale.


## AWS Organizations & Multi-Account


**Q34.** Government regulations require that your company maintain all correspondence for a period of seven years for compliance reasons. What is the best storage mechanism to keep this data secure in a cost-effective manner?

- **A.** Amazon S3
- **B.** Amazon EBS
- **C.** Amazon EFS
- **D.** Amazon Glacier


**Q35.** What is the maximum single file object size supported with Amazon S3?

- **A.** 1 TB
- **B.** 5 GB
- **C.** 100 GB
- **D.** 5 TB


## Disaster Recovery, Backup & RTO/RPO


**Q36.** What on-premises solution is available from Amazon AWS to minimize latency for all data?

- **A.** S3 bucket
- **B.** Gateway-VTL
- **C.** ElastiCache
- **D.** Gateway-stored volumes
- **E.** EBS
- **F.** Gateway-cached volumes


## EFS, FSx & Shared File Storage


**Q37.** You have been asked to recommend the best AWS storage solution for a client. The client requires a storage solution that provide a mounted file system for a Big Data and Analytics application. The client’s requirements include high throughput, low latency, read- after-write consistency and the ability to burst up to multiple GB/s for short periods of time. Which AWS service can meet this requirement?

- **A.** EFS
- **B.** EBS
- **C.** DynamoDB
- **D.** S3


## Monitoring: CloudWatch, CloudTrail & Config


**Q38.** What is the type of monitoring data (for Amazon EBS volumes) which is available automatically in 5-minute periods at no charge called?

- **A.** Detailed
- **B.** Local
- **C.** Primary
- **D.** Basic


## Elastic Beanstalk & Deployment


**Q39.** You are creating a CloudFormation Stack that will create EC2 instances that will record log files to an S3 bucket. When creating the template which optional section is used to return the name of the S3 bucket?

- **A.** Parameters
- **B.** Resources
- **C.** Mappings
- **D.** Outputs


## General Design


**Q40.** How does AWS uniquely identify S3 objects?

- **A.** Bucket name
- **B.** Object tag
- **C.** Version
- **D.** Key


# Section B - Multiple Response (select all that apply)


## S3 Storage Classes & Lifecycle


**Q41.** Which of the following services natively encrypts data at rest within an AWS region? **(Select 2.)**

- **A.** Amazon DynamoDB
- **B.** Amazon Glacier
- **C.** Amazon Simple Queue Service
- **D.** Amazon CloudFront
- **E.** AWS Storage Gateway


**Q42.** Which statements about Amazon Glacier are true? **(Select 3.)**

- **A.** Amazon Glacier stores data in objects that live in archives.
- **B.** Amazon Glacier archives are identified by user-specified key names.
- **C.** Amazon Glacier can be used as a standalone service and as an Amazon S3 storage class.
- **D.** Amazon Glacier vaults can be locked.
- **E.** Amazon Glacier archives take three to five hours to restore.


**Q43.** What is needed before you can enable cross-region replication on an Amazon Simple Storage Service (Amazon S3) bucket? **(Select 2.)**

- **A.** Create an AWS Identity and Access Management (IAM) policy to allow Amazon S3 to replicate objects on your behalf
- **B.** Enable a lifecycle rule to migrate data to the second region.
- **C.** Enable static website hosting.
- **D.** Enable versioning on the bucket.


**Q44.** A Solutions Architect is designing a data archive strategy using Amazon Glacier. The Architect needs to explain the features of the service to his manager, which statements about Glacier are correct? **(Select 2.)**

- **A.** Retrieval is immediate
- **B.** Uploading archives is synchronous; downloading archives is asynchronous
- **C.** Glacier objects are visible through S3 only
- **D.** The contents of an archive can be modified after uploading


## S3 Security, Access & Durability


**Q45.** Which features can be used to restrict access to Amazon Simple Storage Service (Amazon S3) data? **(Select 3.)**

- **A.** Create a pre-signed URL for an object.
- **B.** Enable static website hosting on the bucket.
- **C.** Use a lifecycle policy.
- **D.** Use an Amazon S3 bucket policy.
- **E.** Use an Amazon S3 Access Control List (ACL) on a bucket or object.


**Q46.** You would like to share some documents with public users accessing an S3 bucket over the Internet. What are two valid methods of granting public read permissions so you can share the documents? **(Select 2.)**

- **A.** Grant public read on all objects using the S3 bucket ACL
- **B.** Share the documents using CloudFront and a static website
- **C.** Grant public read access to the objects when uploading
- **D.** Use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket granting read access to public anonymous users


## DynamoDB Design & Capacity


**Q47.** Which of the following are use cases for Amazon DynamoDB? **(Select 3.)**

- **A.** Storing BLOB data.
- **B.** Storing large amounts of infrequently accessed data.
- **C.** Storing JSON documents.
- **D.** Storing metadata for Amazon S3 objects.
- **E.** Running relational joins and complex updates.
- **F.** Managing web sessions.


## IAM Roles, Policies & Permissions


**Q48.** What security problem is solved by using Cross-Origin Resource Sharing (CORS)? **(Select 2.)**

- **A.** Provide security for third party objects within AWS
- **B.** Enable HTTP requests from within scripts to a different domain
- **C.** Permits sharing objects between AWS services
- **D.** Enable sharing of web-based files between different buckets


## VPC Security Groups & NACLs


**Q49.** In AWS, which security aspects are the customer's responsibility? Choose 4 answers **(Select 4.)**

- **A.** Decommissioning storage devices
- **B.** Security Group and ACL (Access Control List) settings
- **C.** Life-cycle management of IAM credentials
- **D.** Controlling physical access to compute resources
- **E.** Patch management on the EC2 instance's operating system
- **F.** Encryption of EBS (Elastic Block Storage) volumes


## EBS Volumes & Snapshots


**Q50.** You have a workload that requires 15,000 consistent IOPS for data that must be durable. What combination of the following steps do you need? **(Select 2.)**

- **A.** Use a Provisioned IOPS SSD volume.
- **B.** Use an Amazon Elastic Block Store (Amazon EBS)-optimized instance.
- **C.** Use an instance store.
- **D.** Use a magnetic volume.


**Q51.** A customer implemented AWS Storage Gateway with a gateway-cached volume at their main office. An event takes the link between the main and branch office offline. Which methods will enable the branch office to access their data? **(Select 3.)**

- **A.** Make an Amazon Glacier Restore API call to load the files into another Amazon S3 bucket within four to six hours
- **B.** Use a HTTPS GET to the Amazon S3 bucket where the files are located.
- **C.** Launch a new AWS Storage Gateway instance AMI in Amazon EC2, and restore from a gateway snapshot.
- **D.** Restore by implementing a lifecycle policy on the Amazon S3 bucket.
- **E.** Launch an AWS Storage Gateway virtual iSCSI device at the branch office, and restore from a gateway snapshot.
- **F.** Create an Amazon EBS volume from a gateway snapshot, and mount it to an Amazon EC2 instance.


**Q52.** What are characteristics of Amazon S3? **(Select 2.)**

- **A.** S3 offers Provisioned IOPS.
- **B.** S3 allows you to store objects of virtually unlimited size.
- **C.** S3 allows you to store unlimited amounts of data.
- **D.** Objects are directly accessible via a URL.
- **E.** S3 should be used to host a relational database.


**Q53.** Which of the following will occur when an Amazon Elastic Block Store (Amazon EBS)- backed Amazon EC2 instance in an Amazon VPC with an associated EIP is stopped and started? **(Select 2.)**

- **A.** The ENI is detached.
- **B.** All data on instance-store devices will be lost.
- **C.** The EIP will be dissociated from the instance.
- **D.** The underlying host for the instance is changed.
- **E.** All data on Amazon EBS devices will be lost.


**Q54.** What must be done to host a static website in an Amazon Simple Storage Service (Amazon S3) bucket? **(Select 3.)**

- **A.** Make the objects in the bucket world-readable.
- **B.** Create a bucket with the same name as the website.
- **C.** Configure the bucket for static hosting and specify an index and error document.
- **D.** Enable File Transfer Protocol (FTP) on the bucket.
- **E.** Enable HTTP on the bucket.


## EC2 Instances, AMIs & Placement


**Q55.** What is the default behavior for an EC2 instance when terminated? **(Select 2.)**

- **A.** EBS root device volume is automatically deleted when instance terminates
- **B.** EBS data volumes that you attach at launch persist
- **C.** EBS root device volume and additional attached volumes are deleted immediately
- **D.** DeleteOnTermination attribute cannot be modified


**Q56.** Which of the following are true of instance stores? **(Select 2.)**

- **A.** Automatic backups
- **B.** Charge is based on the total amount of storage provisioned.
- **C.** Data is lost when the instance stops.
- **D.** Very high IOPS


## CloudFront & Edge Delivery


**Q57.** You would like to provide some on-demand and live streaming video to your customers. The plan is to provide the users with both the media player and the media files from the AWS cloud. One of the features you need is for the content of the media files to begin playing while the file is still being downloaded. What AWS services can deliver these requirements? **(Select 2.)**

- **A.** Use CloudFront with an RTMP distribution
- **B.** Store the media files in an S3 bucket
- **C.** Use CloudFront with a Web and RTMP distribution
- **D.** Store the media files on an EC2 instance


## Lambda & Serverless Compute


**Q58.** What three statements correctly describe standard Lambda operation? **(Select 3.)**

- **A.** Lambda function is allocated 500 MB ephemeral disk space
- **B.** Lambda stores code in a Glacier vault
- **C.** Lambda stores code in containers
- **D.** Lambda function is allocated 100 MB EBS storage
- **E.** maximum execution time is 300 seconds
- **F.** Lambda stores code in S3


## Monitoring: CloudWatch, CloudTrail & Config


**Q59.** As a SysOps engineer working at Digital Cloud Training, you are constantly trying to improve your processes for collecting log data. Currently you are collecting logs from across your AWS resources using CloudWatch and a combination of standard and custom metrics. You are currently investigating how you can optimize the storage of log files collected by CloudWatch. Which of the following are valid options for storing CloudWatch log files? **(Select 2.)**

- **A.** CloudWatch Logs
- **B.** EBS
- **C.** Splunk
- **D.** EFS


**Q60.** Which of the following are valid statements about Amazon S3? **(Select 2.)**

- **A.** S3 provides read-after-write consistency for any type of PUT or DELETE.
- **B.** S3 provides eventual consistency for overwrite PUTS and DELETES.
- **C.** Consistency is not guaranteed for any type of PUT or DELETE.
- **D.** Partially saved objects are immediately readable with a GET after an overwrite PUT.
- **E.** A successful response to a PUT request only occurs when a complete object is saved.


**Q61.** Amazon Simple Storage Service (Amazon S3) is an eventually consistent storage system. For what kinds of operations is it possible to get stale data as a result of eventual consistency? **(Select 2.)**

- **A.** GET after PUT of a new object
- **B.** DELETE after PUT of new object
- **C.** GET after overwrite PUT (PUT to an existing key)
- **D.** GET or LIST after a DELETE


## AWS Organizations & Multi-Account


**Q62.** What are some of the key characteristics of Amazon Simple Storage Service (Amazon S3)? **(Select 3.)**

- **A.** Objects are world-readable by default.
- **B.** Amazon S3 uses a REST (Representational State Transfer) Application Program Interface (API).
- **C.** You must pre-allocate the storage in a bucket.
- **D.** All objects have a URL.
- **E.** Amazon S3 can store unlimited amounts of data.


## EFS, FSx & Shared File Storage


**Q63.** Which of the following are not appropriates use cases for Amazon Simple Storage Service (Amazon S3)? **(Select 2.)**

- **A.** Storing backups for a relational database
- **B.** Storing a file system mounted to an Amazon Elastic Compute Cloud (Amazon EC2) instance
- **C.** Primary storage for a database
- **D.** Storing web content
- **E.** Storing logs for analytics


## General Design


**Q64.** Amazon Simple Storage Service (S3) bucket policies can restrict access to an Amazon S3 bucket and objects by which of the following? **(Select 3.)**

- **A.** Company name
- **B.** Country of origin
- **C.** IP address range
- **D.** AWS account
- **E.** Objects with a specific prefix


**Q65.** In what ways does Amazon Simple Storage Service (Amazon S3) object storage differ from block and file storage? **(Select 2.)**

- **A.** Amazon S3 stores data in fixed size blocks.
- **B.** Objects are stored in buckets.
- **C.** Objects contain both data and metadata.
- **D.** Objects can be any size.
- **E.** Objects are identified by a numbered address.


---


# Answer Key & Explanations


**Q1. B**  
_S3 Storage Classes & Lifecycle_  
Amazon S3 Glacier and S3 Glacier Deep Archive are a secure, durable, and extremely low-cost Amazon S3 cloud storage classes for data archiving and long-term backup. Refer: https://aws.amazon.com/glacier/

**Q2. D**  
_S3 Storage Classes & Lifecycle_  
Moving logs to Glacier may save cost but the questions requests that the files are permanently deleted Object Expiration allows you to schedule removal of your objects after a defined time period Using Object Expiration rules to schedule periodic removal of objects eliminates the need to build processes to identify objects for deletion and submit delete requests to Amazon S3 References: https://aws.amazon.com/about-aws/whats- new/2011/12/27/amazon-s3-announces-object-expiration/ https://aws.amazon.com/about-aws/whats-new/2011/12/27/amazon-s3-announces-object- expiration/

**Q3. A**  
_S3 Storage Classes & Lifecycle_  
Amazon S3 is the most cost effective storage on AWS, and lifecycle policies are a simple and effective feature to address the business requirements.

**Q4. A**  
_S3 Storage Classes & Lifecycle_  
Refer: https://aws.amazon.com/s3/faqs/

**Q5. C**  
_DynamoDB Design & Capacity_  
Maximum throughput per DynamoDB table is practically unlimited. For information about the limits in place, see Limits in DynamoDB. If you want to request a limit increase, contact Amazon. Refer: https://aws.amazon.com/dynamodb/faqs/

**Q6. C**  
_IAM Roles, Policies & Permissions_  
With this enhancement, Amazon S3 now supports read-after-write consistency in all regions for new objects added to Amazon S3. Read- after-write consistency allows you to retrieve objects immediately after creation in Amazon S3. Refer: https://aws.amazon.com/about-aws/whats- new/2015/08/amazon-s3-introduces-new-usability-enhancements

**Q7. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
DB instances for Amazon RDS for MySQL, MariaDB, PostgreSQL, Oracle, and Microsoft SQL Server use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage. Depending on the amount of storage requested, Amazon RDS automatically stripes across multiple Amazon EBS volumes to enhance performance. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#:~:text=DB%20instances%20for%20Amazon%20RDS,EBS%20volumes%20to%20enhance%20perform

**Q8. C**  
_S3 Security, Access & Durability_  
Refer: https://aws.amazon.com/premiumsupport/knowledge-center/data-integrity-s3/

**Q9. A**  
_SQS, SNS & Decoupling_  
This is a great use case for Amazon Simple Queue Service (Amazon SQS). SQS is a web service that gives you access to message queues that store messages waiting to be processed and offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers. SQS is used for distributed/decoupled applications. In this circumstance SQS will reduce the risk of writes being dropped and it the best option presented RDS in a multi-AZ configuration will not help as writes are only made to the primary database Though writing data to an S3 bucket could potentially work, it is not the best option as SQS is recommended for decoupling application components The CloudFront option is bogus as you cannot configure a database as a custom origin in CloudFront References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-integration/amazon- sqs/

**Q10. C**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q11. C**  
_EBS Volumes & Snapshots_  
SSD, General Purpose (GP2) provides enough IOPS to support this requirement and is the most economical option that does. Using Provisioned IOPS would be more expensive and the other two options do not provide an SLA for IOPS More information on the volume types: - SSD, General Purpose (GP2) provides 3 IOPS per GB up to 16,000 IOPS. Volume size is 1 GB to 16 TB - Provisioned IOPS (Io1) provides the IOPS you assign up to 50 IOPS per GiB and up to 64,000 IOPS per volume. Volume size is 4 GB to 16TB - Throughput Optimized HDD (ST1) provides up to 500 IOPS per volume but does not provide an SLA for IOPS - Cold HDD (SC1) provides up to 250 IOPS per volume but does not provide an SLA for IOPS References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/ https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html?icmpid=docs_ec2_console

**Q12. A**  
_EBS Volumes & Snapshots_  
Data is available automatically in 5-minute periods at no charge. This includes data for the root device volumes for EBS-backed instances. Provisioned IOPS SSD ( io1 ) volumes automatically send one-minute metrics to CloudWatch. ... You can get the data using either the CloudWatch API or the Amazon EC2 console. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html#:~:text=Data%20is%20available%20automatically%20in,volumes%20for%20EBS%2Dbacked%20instances.&text=Provisioned%20IOPS%20SSD%20(%20io1%20)%20volumes,one%2Dminute%20metrics

**Q13. C**  
_EBS Volumes & Snapshots_  
EBS Throughput Optimized HDD is good for the following use cases (and is the most cost-effective option: Frequently accessed, throughput intensive workloads with large datasets and large I/O sizes, such as MapReduce, Kafka, log processing, data warehouse, and ETL workloads Throughput is measured in MB/s, and includes the ability to burst up to 250 MB/s per TB, with a baseline throughput of 40 MB/s per TB and a maximum throughput of 500 MB/s per volume The SSD options are more expensive References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ebs/

**Q14. D**  
_EBS Volumes & Snapshots_  
Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

**Q15. B**  
_EBS Volumes & Snapshots_  
A short period of heavy traffic is exactly the use case for the bursting nature of general-purpose SSD volumes—the rest of the day is more than enough time to build up enough IOPS credits to handle the nightly task. Instance stores are not durable, magnetic volumes cannot provide enough IOPS, and to set up a Provisioned IOPS SSD volume to handle the peak would mean spending money for more IOPS than you need.

**Q16. B**  
_EBS Volumes & Snapshots_  
Search Results Featured snippet from the web Copying an AMI. You can copy an Amazon Machine Image (AMI) within or across AWS Regions using the AWS Management Console, the AWS Command Line Interface or SDKs, or the Amazon EC2 API, all of which support the CopyImage action. You can copy both Amazon EBS-backed AMIs and instance-store-backed AMIs. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html

**Q17. B**  
_EBS Volumes & Snapshots_  
An Amazon EBS-backed instance can be stopped and later restarted without affecting data stored in the attached volumes. There are various instance– and volume-related tasks you can do when an Amazon EBS-backed instance is in a stopped state. For example, you can modify the properties of the instance, change its size, or update the kernel it is using, or you can attach your root volume to a different running instance for debugging or any other purpose. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html

**Q18. A**  
_EBS Volumes & Snapshots_  
For data you want to retain longer, or if you want to encrypt the data, use Amazon Elastic Block Store (Amazon EBS) volumes instead. EBS volumes preserve their data through instance stops and terminations, can be easily backed up with EBS snapshots, can be removed from one instance and reattached to another, and support full-volume encryption. Refer: https://aws.amazon.com/premiumsupport/knowledge-center/instance-store-vs-ebs/

**Q19. B**  
_EBS Volumes & Snapshots_  
Refer: https://aws.amazon.com/s3/

**Q20. C**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q21. D**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q22. D**  
_EBS Volumes & Snapshots_  
RAID 1+0 (RAID 10) doubles the amount of I/O required from the instance to EBS compared to RAID 0, because you're mirroring all writes to a pair of volumes, limiting how much you can stripe. Reference: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/raid-config.html

**Q23. C**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q24. D**  
_EBS Volumes & Snapshots_  
Amazon EBS is the recommended storage option when you run a database on an instance. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html

**Q25. E**  
_EC2 Instances, AMIs & Placement_  
Amazon EBS offers data persistence, dynamic performance adjustments, and the ability to detach and reattach volumes, allowing you to resize clusters for big data analytics engines such as Hadoop and Spark. Refer: https://aws.amazon.com/ebs/?ebs-whats-new.sort- by=item.additionalFields.postDateTime&ebs-whats-new.sort-order=desc

**Q26. C**  
_EC2 Instances, AMIs & Placement_  
HVM AMIs do not support the use of trailing numbers on device names, except for /dev/sda1, which is reserved for the root device, and /dev/sda2. While using /dev/sda2 is possible, we do not recommend using this device mapping with HVM instances. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html

**Q27. A**  
_EC2 Instances, AMIs & Placement_  
You can specify the instance store volumes for your instance only when you launch an instance. You can't attach instance store volumes to an instance after you've launched it You can use a block device mapping to specify additional EBS volumes when you launch your instance, or you can attach additional EBS volumes after your instance is running An Elastic Network Adapter has nothing to do with adding instance store volumes References: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html

**Q28. B**  
_EC2 Instances, AMIs & Placement_  
Amazon Simple Storage Service is storage for the Internet. It is designed to make web-scale computing easier for developers. Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html

**Q29. D**  
_CloudFront & Edge Delivery_  
Amazon S3 automatically scales to high request rates. For example, your application can achieve at least 3,500 PUT/POST/DELETE and 5,500 GET requests per second per prefix in a bucket. There are no limits to the number of prefixes in a bucket If your workload is mainly sending GET requests, in addition to the preceding guidelines, you should consider using Amazon CloudFront for performance optimization. By integrating CloudFront with Amazon S3, you can distribute content to your users with low latency and a high data transfer rate Transfer Acceleration is used to accelerate object uploads to S3 over long distances (latency) Cross-region replication creates a replica copy in another region but should not be used for spreading read requests across regions. There will be 2 S3 endpoints and CRR is not designed for 2 way sync so this would not work well ElastiCache is used for caching database content not S3 content References: https://docs.aws.amazon.com/AmazonS3/latest/dev/request- rate-perf-considerations.html https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

**Q30. A**  
_High Availability & Fault Tolerance_  
Amazon EFS is the best solution as it is the only solution that is a file-level storage solution (not block/object-based), stores data redundantly across multiple AZs within a region and you can concurrently connect up to thousands of EC2 instances to a single filesystem Amazon EBS volumes cannot be accessed by concurrently by multiple instances Amazon S3 is an object store, not a file system Amazon Storage Gateway is a range of products used for on-premises storage management and can be configured to cache data locally, backup data to the cloud and also provides a virtual tape backup solution References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/storage/amazon-efs/

**Q31. D**  
_Data Migration & Transfer_  
AWS Server Migration Service automates the migration of your on-premises VMware vSphere, Microsoft Hyper-V/SCVMM, and Azure virtual machines to the AWS Cloud. AWS SMS incrementally replicates your server VMs as cloud-hosted Amazon Machine Images (AMIs) ready for deployment on Amazon EC2. Refer: https://docs.aws.amazon.com/server-migration-service/latest/userguide/server-migration.html

**Q32. B**  
_Data Migration & Transfer_  
Amazon S3 provides highly durable and available storage for a variety of content. Amazon S3 can be used as a big data object store for all of the videos. Amazon S3’s low cost combined with its design for durability of 99.999999999% and for up to 99.99% availability make it a great storage choice for transcoding services.

**Q33. C**  
_Data Migration & Transfer_  
Multipart upload allows you to upload a single object as a set of parts. Each part is a contiguous portion of the object's data. You can upload these object parts independently and in any order. If transmission of any part fails, you can retransmit that part without affecting other parts. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html#:~:text=Multipart%20upload%20allows%20you%20to,part%20without%20affecting%20other%20parts.

**Q34. D**  
_AWS Organizations & Multi-Account_  
Amazon Glacier enables businesses and organizations to retain data for months, years, or decades, easily and cost effectively. With Amazon Glacier, customers can retain more of their data for future analysis or reference, and they can focus on their business instead of operating and maintaining their storage infrastructure. Customers can also use Amazon Glacier Vault Lock to meet regulatory and compliance archiving requirements.

**Q35. D**  
_AWS Organizations & Multi-Account_  
AWS has raised the limit by three orders of magnitude. Individual Amazon S3 objects can now range in size from 1 byte all the way to 5 terabytes (TB). Now customers can store extremely large files as single objects, which greatly simplifies their storage experience. Amazon S3 does the bookkeeping behind the scenes for our customers, so you can now GET that large object just like you would any other Amazon S3 object. Refer: https://aws.amazon.com/blogs/aws/amazon-s3-object-size-limit/

**Q36. B**  
_Disaster Recovery, Backup & RTO/RPO_  
With cached volumes, you store volume data in AWS, with a small portion of recently accessed data in the cache on-premises. This approach enables low-latency access to your frequently accessed dataset. It also provides seamless access to your entire dataset stored in AWS. By using cached volumes, you can scale your storage resource without having to provision additional hardware. With stored volumes, you store the entire set of volume data on-premises and store periodic point-in-time backups (snapshots) in AWS. In this model, your on-premises storage is primary, delivering low- latency access to your entire dataset. AWS storage is the backup that you can restore in the event of a disaster in your data center. Refer: https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html

**Q37. A**  
_EFS, FSx & Shared File Storage_  
EFS is a fully-managed service that makes it easy to set up and scale file storage in the Amazon Cloud. EFS is good for big data and analytics, media processing workflows, content management, web serving, home directories etc.. EFS uses the NFSv4.1 protocol which is a protocol for mounting file systems (similar to Microsoft’s SMB) EBS is mounted as a block device not a file system S3 is object storage DynamoDB is a fully managed NoSQL database References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

**Q38. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
CloudWatch metrics are statistical data that you can use to view, analyze, and set alarms on the operational behavior of your volumes. The following table describes the types of monitoring data available for your Amazon EBS volumes. Data is available automatically in 5-minute periods at no charge. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html#:~:text=CloudWatch%20metrics%20are%20statistical%20data,for%20your%20Amazon%20EBS%20volumes.&text=Data%20is%20available%20automatica

**Q39. D**  
_Elastic Beanstalk & Deployment_  
The optional Outputs section declares output values that you can import into other stacks (to create cross-stack references), return in response (to describe stack calls), or view on the AWS CloudFormation console. For example, you can output the S3 bucket name for a stack to make the bucket easier to find Template elements include: File format and version (mandatory) List of resources and associated configuration values (mandatory) Template parameters (optional) Output values (optional) List of data tables (optional). References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/management-tools/aws-cloudformation/ https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section- structure.html

**Q40. A**  
_General Design_  
Each Amazon S3 object has data, a key, and metadata. The object key (or key name) uniquely identifies the object in a bucket. Object metadata is a set of name-value pairs. The only way to modify object metadata is to make a copy of the object and set the metadata. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.htm

**Q41. B, E**  
_S3 Storage Classes & Lifecycle_  
Amazon S3 Glacier and S3 Glacier Deep Archive are a secure, durable, and extremely low-cost Amazon S3 cloud storage classes for data archiving and long-term backup. They are designed to deliver 99.999999999% durability, and provide comprehensive security and compliance capabilities that can help meet even the most stringent regulatory requirements. Customers can store data for as little as $1 per terabyte per month, a significant savings compared to on-premises solutions. To keep costs low yet suitable for varying retrieval needs, Amazon S3 Glacier provides three options for access to archives, from a few minutes to several hours, and S3 Glacier Deep Archive provides two access options ranging from 12 to 48 hours. Refer: https://aws.amazon.com/glacier/ AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. Customers use Storage Gateway to simplify storage management and reduce costs for key hybrid cloud storage use cases. These include moving backups to the cloud, using on-premises file shares backed by cloud storage, and providing low latency access to data in AWS for on-premises applications. Refer: https://aws.amazon.com/storagegateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc

**Q42. C, D, E**  
_S3 Storage Classes & Lifecycle_  
Amazon Glacier stores data in archives, which are contained in vaults. Archives are identified by system-created archive IDs, not key names. Chapter 3: Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Elastic Block Store (Amazon EBS)

**Q43. A, D**  
_S3 Storage Classes & Lifecycle_  
You must enable versioning before you can enable cross-region replication, and Amazon S3 must have IAM permissions to perform the replication. Lifecycle rules migrate data from one storage class to another, not from one bucket to another. Static website hosting is not a prerequisite for replication.

**Q44. B, C**  
_S3 Storage Classes & Lifecycle_  
Glacier objects are visible through S3 only (not Glacier directly) The contents of an archive that has been uploaded cannot be modified Uploading archives is synchronous Downloading archives is asynchronous Retrieval can take a few hours. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

**Q45. A, D, E**  
_S3 Security, Access & Durability_  
Static website hosting does not restrict data access, and neither does an Amazon S3 lifecycle policy.

**Q46. C, D**  
_S3 Security, Access & Durability_  
Access policies define access to resources and can be associated with resources (buckets and objects) and users You can use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket. Bucket policies can be used to grant permissions to objects You can define permissions on objects when uploading and at any time afterwards using the AWS Management Console. You cannot use a bucket ACL to grant permissions to objects within the bucket. You must explicitly assign the permissions to each object through an ACL attached as a subresource to that object Using an EC2 instance as a bastion host to share the documents is not a feasible or scalable solution You can configure an S3 bucket as a static website and use CloudFront as a front-end however this is not necessary just to share the documents and imposes some constraints on the solution. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

**Q47. B, C, E**  
_DynamoDB Design & Capacity_  
Storing large amounts of infrequently accessed data. Amazon DynamoDB is ideal for existing or new applications that need a flexible NoSQL database with low read and write latencies, and the ability to scale storage and throughput up or down as needed without code changes or downtime. Refer: https://aws.amazon.com/dynamodb/#:~:text=Use%20cases-,Ad%20Tech,%2C%20ad%20targeting%2C%20and%20attribution.

**Q48. A, B**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q49. B, C, E, F**  
_VPC Security Groups & NACLs_  
The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. Refer: https://aws.amazon.com/compliance/shared-responsibility- model/#:~:text=The%20customer%20assumes%20responsibility%20and,AWS%20provided%20security%20group%20firewall.

**Q50. A, B**  
_EBS Volumes & Snapshots_  
The option is incorrect because an instance store will not be durable and a magnetic volume offers an average of 100 IOPS. Amazon EBS-optimized instances reserve network bandwidth on the instance for IO, and Provisioned IOPS SSD volumes provide the highest consistent IOPS.

**Q51. B, C, E**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q52. C, D**  
_EBS Volumes & Snapshots_  
Amazon S3 has various features you can use to organize and manage your data in ways that support specific use cases, enable cost efficiencies, enforce security, and meet compliance requirements. Data is stored as objects within resources called “buckets”, and a single object can be up to 5 terabytes in size. Refer: https://aws.amazon.com/s3/features/#:~:text=Amazon%20S3%20has%20various%20features,to%205%20terabytes%20in%20size.

**Q53. B, D**  
_EBS Volumes & Snapshots_  
In the EC2-Classic network, the EIP will be disassociated with the instance; in the EC2-VPC network, the EIP remains associated with the instance. Regardless of the underlying network, a stop/start of an Amazon EBS-backed Amazon EC2 instance always changes the host computer.

**Q54. A, B, C**  
_EBS Volumes & Snapshots_  
The three options are required and normally you also set a friendly CNAME to the bucket URL. Amazon S3 does not support FTP transfers, and HTTP does not need to be enabled.

**Q55. A, B**  
_EC2 Instances, AMIs & Placement_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not C:* If EC2 instance is terminated, by default the root volume is also deleted. But the EBS volume attached will be retained. We can change this default behavior by modifying the DeleteOnTermination attribute. When an instance terminates, the data on any instance store volumes associated with that instance is deleted. By default, Amazon EBS root device volumes are automatically deleted when the instance terminates. Refer: When an instance terminates, the data on any instance store volumes associated with that instance is deleted. By default, Amazon EBS root device volumes are automatically deleted when the instance terminates.

**Q56. C, D**  
_EC2 Instances, AMIs & Placement_  
Instance stores are low-durability, high-IOPS storage that is included for free with the hourly cost of an instance.

**Q57. B, C**  
_CloudFront & Edge Delivery_  
For serving both the media player and media files you need two types of distributions: - A web distribution for the media player - An RTMP distribution for the media files RTMP: - Distribute streaming media files using Adobe Flash Media Server’s RTMP protocol - Allows an end user to begin playing a media file before the file has finished downloading from a CloudFront edge location - Files must be stored in an S3 bucket (not an EBS volume or EC2 instance). References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon- cloudfront/

**Q58. A, E, F**  
_Lambda & Serverless Compute_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q59. A, C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Valid options for storing logs include: - CloudWatch Logs - Centralized logging system (e.g. Splunk) - Custom script and store on S3 RedShift, EFS and EBS are not valid options for storing CloudWatch log files. References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/management-tools/amazon-cloudwatch/

**Q60. B, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q61. C, D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon S3 provides read-after-write consistency for PUTs to new objects (new key), but eventual consistency for GETs and DELETEs of existing objects (existing key).

**Q62. B, D, E**  
_AWS Organizations & Multi-Account_  
Objects are private by default, and storage in a bucket does not need to be pre-allocated.

**Q63. B, C**  
_EFS, FSx & Shared File Storage_  
Amazon S3 cannot be mounted to an Amazon EC2 instance like a file system and should not serve as primary database storage.

**Q64. C, D, E**  
_General Design_  
Amazon S3 bucket policies cannot specify a company name or a country or origin, but they can specify request IP range, AWS account, and a prefix for objects that can be accessed.

**Q65. B, C**  
_General Design_  
Objects are stored in buckets, and objects contain both data and metadata
