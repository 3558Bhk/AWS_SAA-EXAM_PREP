# Task 3.3 - High-Performing Database Solutions - Practice Questions

> **Domain 3 - Design High-Performing Architectures (24%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **55 multiple-choice (single answer)** followed by **23 multiple-response (select 2+)**. Total **78**.


**Topic order in this file:** RDS Multi-AZ, Read Replicas & Aurora → DynamoDB Design & Capacity → Auto Scaling & Elastic Load Balancing → SQS, SNS & Decoupling → EBS Volumes & Snapshots → EC2 Instances, AMIs & Placement → ElastiCache & Caching Strategies → Redshift, Athena & Analytics → Kinesis & Streaming Ingestion → Monitoring: CloudWatch, CloudTrail & Config → Elastic Beanstalk & Deployment → General Design → High Availability & Fault Tolerance → Disaster Recovery, Backup & RTO/RPO


---


# Section A - Multiple Choice (one correct answer)


## RDS Multi-AZ, Read Replicas & Aurora


**Q1.** A critical database runs in your VPC for which availability is a concern. Which RDS DB instance events may force the DB to be taken offline during a maintenance window?

- **A.** Security patching
- **B.** Updating DB parameter groups
- **C.** Promoting a Read Replica
- **D.** Selecting the Multi-AZ feature


**Q2.** A customer has asked you to recommend the best solution for a highly available database. The database is a relational OLTP type of database and the customer does not want to manage the operating system the database runs on. Failover between AZs must be automatic. Which of the below options would you suggest to the customer?

- **A.** Use RedShift in a Multi-AZ configuration
- **B.** Use RDS in a Multi-AZ configuration
- **C.** Use DynamoDB
- **D.** Install a relational database on EC2 instances in multiple AZs and create a cluster


**Q3.** When automatic failover occurs, Amazon RDS will emit a DB Instance event to inform you that automatic failover occurred. You can use the _____ to return information about events related to your DB Instance

- **A.** DescriveFailure
- **B.** FetchFailure
- **C.** DescribeEvents
- **D.** FetchEvents


**Q4.** Which Amazon Relational Database Service (Amazon RDS) database engines support read replicas?

- **A.** MySQL and PostgreSQL
- **B.** Aurora, Microsoft SQL Server, and Oracle
- **C.** Microsoft SQL Server and Oracle
- **D.** MySQL, MariaDB, PostgreSQL, and Aurora


**Q5.** Which Amazon Relational Database Service (Amazon RDS) database engines support Multi-AZ?

- **A.** All of them
- **B.** MySQL
- **C.** Oracle, Amazon Aurora, and PostgreSQL
- **D.** Microsoft SQL Server, MySQL, and Oracle


**Q6.** What is an isolated database environment running in the cloud (Amazon RDS) called?

- **A.** DB Server
- **B.** DB Volume
- **C.** DB Instance
- **D.** DB Unit


**Q7.** When you resize the Amazon RDS DB instance, Amazon RDS will perform the upgrade during the next maintenance window. If you want the upgrade to be performed now, rather than waiting for the maintenance window, specify the _____ option.

- **A.** ApplyThis
- **B.** ApplyImmediately
- **C.** ApplyNow
- **D.** ApplySoon


**Q8.** The SQL Server _____ feature is an efficient means of copying data from a source database to your DB Instance. It writes the data that you specify to a data file, such as an ASCII file.

- **A.** group copy
- **B.** bulk copy
- **C.** mass copy
- **D.** dual copy


**Q9.** You are working for a small organization without a dedicated database administrator on staff. You need to install Microsoft SQL Server Enterprise edition quickly to support an accounting back office application on Amazon Relational Database Service (Amazon RDS). What should you do?

- **A.** Launch an Amazon RDS DB Instance, and select Microsoft SQL Server Enterprise Edition under the Bring Your Own License (BYOL) model.
- **B.** You cannot use SQL Server Enterprise edition on Amazon RDS. You should install this on to a dedicated Amazon Elastic Compute Cloud (Amazon EC2) Instance.
- **C.** SQL Server Enterprise edition is only available via the Command Line Interface (CLI). Install the command-line tools on your laptop, and then provision your new Amazon RDS Instance using the CLI.
- **D.** Provision SQL Server Enterprise Edition using the License Included option from the Amazon RDS Console.


**Q10.** Because of the extensibility limitations of striped storage attached to Windows Server, Amazon RDS does not currently support increasing storage on a _____ DB Instance.

- **A.** MySQL
- **B.** Oracle
- **C.** SQL Server


**Q11.** A company is migrating an on-premises 10 TB MySQL database to AWS. The company expects the database to quadruple in size and the business requirement is that replicate lag must be kept under 100 milliseconds. Which Amazon RDS engine meets these requirements?

- **A.** Oracle
- **B.** Microsoft SQL Server
- **C.** Amazon Aurora
- **D.** MySQL


**Q12.** Which DNS record should you use to configure the transmission of email to your intended mail server?

- **A.** SPF records
- **B.** MX records
- **C.** A records
- **D.** SOA record


**Q13.** 7. Which DNS records are commonly used to stop email spoofing and spam?

- **A.** A records
- **B.** C names
- **C.** MX records
- **D.** SPF records


**Q14.** What can I access by visiting the URL: http://status.aws.amazon.com/?

- **A.** Amazon Cloud Watch
- **B.** AWS Cloud Monitor
- **C.** AWS Service Health Dashboard
- **D.** Status of the Amazon RDS DB


**Q15.** SQL Server __________ store logins and passwords in the master database.

- **A.** does
- **B.** can be configured to but by default does not
- **C.** doesn't


## DynamoDB Design & Capacity


**Q16.** You are creating an Amazon DynamoDB table that will contain messages for a social chat application. This table will have the following attributes: Username (String), Timestamp (Number), Message (String). Which attribute should you use as the partition key? The sort key?

- **A.** Timestamp, Message
- **B.** Username, Message
- **C.** Message, Timestamp
- **D.** Username, Timestamp


**Q17.** What DynamoDB capacity management technique is based on the tenant specifying an upper and lower range for read/write capacity units?

- **A.** General purpose
- **B.** Reserved capacity
- **C.** Provisioned throughput
- **D.** Demand
- **E.** Auto scaling


**Q18.** You need a persistent and durable storage to trace call activity of an IVR (Interactive Voice Response) system. Call duration is mostly in the 2-3 minutes timeframe. Each traced call can be either active or terminated. An external application needs to know each minute the list of currently active calls, which are usually a few calls/second. Put once per month there is a periodic peak up to 1000 calls/second for a few hours. The system is open 24/7 and any downtime should be avoided. Historical data is periodically archived to files. Cost saving is a priority for this project. What database implementation would better fit this scenario, keeping costs as low as possible?

- **A.** Use DynamoDB with a 'Calls" table and a Global secondary index on a 'State" attribute that can equal to "active" or "terminated" in this way the Global Secondary index can be used for all Items in the table.
- **B.** Use RDS Multi-AZ with two tables, one for -Active calls" and one for -Terminated calls". In this way the "Active calls_ table is always small and effective to access.
- **C.** Use DynamoDB with a "Calls" table and a Global Secondary Index on a "IsActive'" attribute that is present for active calls only In this way the Global Secondary index is sparse and more effective.
- **D.** Use RDS Multi-AZ with a "CALLS" table and an Indexed "STATE* field that can be equal to 'ACTIVE" or -TERMINATED" In this way the SOL query Is optimized by the use of the Index.


**Q19.** What consistency model is the default used by DynamoDB?

- **A.** Strongly consistent
- **B.** No default model
- **C.** Casual consistency
- **D.** Sequential consistency
- **E.** Eventually consistent


**Q20.** Your company is publishing an online catalog of books that is currently using DynamoDB for storing the information associated with each item. There is a requirement to add images for each book. What solution is most cost effective and designed for that purpose?

- **A.** RDS
- **B.** Kinesis
- **C.** RedShift
- **D.** EBS
- **E.** S3


**Q21.** You must specify strongly consistent read and write capacity for your DynamoDB database. You have determined read capacity of 128 Kbps and write capacity of 25 Kbps is required for your application. What is the read and write capacity units required for DynamoDB table?

- **A.** 64 read units, 10 write units
- **B.** 32 read units, 25 write units
- **C.** 1 read unit, 1 write unit
- **D.** 16 read units, 2.5 write units


**Q22.** Which AWS database service is best suited for non-relational databases?

- **A.** Amazon Redshift
- **B.** Amazon DynamoDB
- **C.** Amazon Glacier
- **D.** Amazon Relational Database Service (Amazon RDS)


**Q23.** You are building a photo management application that maintains metadata on millions of images in an Amazon DynamoDB table. When a photo is retrieved, you want to display the metadata next to the image. Which Amazon DynamoDB operation will you use to retrieve the metadata attributes from the table?

- **A.** Find operation
- **B.** Search operation
- **C.** Scan operation
- **D.** Query operation


**Q24.** Do the system resources on the Micro instance meet the recommended configuration for Oracle?

- **A.** Yes completely
- **B.** Yes but only for certain situations
- **C.** Not in any circumstance


## Auto Scaling & Elastic Load Balancing


**Q25.** A DynamoDB table you manage has a variable load, ranging from sustained heavy usage some days, to only having small spikes on others. The load is 80% read and 20% write. The provisioned throughput capacity has been configured to account for the heavy load to ensure throttling does not occur.You have been asked to find a solution for saving cost. What would be the most efficient and cost-effective solution?

- **A.** Create a DynamoDB Auto Scaling scaling policy
- **B.** Use DynamoDB DAX to increase the performance of the database
- **C.** Create a CloudWatch alarm that triggers an AWS Lambda function that adjusts the provisioned throughput
- **D.** Create a CloudWatch alarm that notifies you of increased/decreased load, and manually adjust the provisioned throughput


**Q26.** A company is building a two-tier web application to serve dynamic transaction-based content. The data tier is leveraging an Online Transactional Processing (OLTP) database. What services should you leverage to enable an elastic and scalable web tier?

- **A.** Amazon RDS with Multi-AZ and Auto Scaling
- **B.** Elastic Load Balancing, Amazon EC2, and Auto Scaling
- **C.** Elastic Load Balancing, Amazon RDS with Multi-AZ, and Amazon S3
- **D.** Amazon EC2, Amazon DynamoDB, and Amazon S3


**Q27.** A large real-estate brokerage is exploring the option o( adding a cost-effective location based alert to their existing mobile application The application backend infrastructure currently runs on AWS Users who opt in to this service will receive alerts on their mobile device regarding real-estate otters in proximity to their location. For the alerts to be relevant delivery time needs to be in the low minute count the existing mobile app has 5 million users across the us Which one of the following architectural suggestions would you make to the customer?

- **A.** The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and EC2 instances: DynamoDB will be used to store and retrieve relevant otters EC2 instances will communicate with mobile earners/device providers to push alerts back to mobile application.
- **B.** The mobile application will send device location using SQS. EC2 instances will retrieve the relevant others from DynamoDB AWS Mobile Push will be used to send offers to the mobile application
- **C.** The mobile application will send device location using AWS Mobile Push EC2 instances will retrieve the relevant offers from DynamoDB EC2 instances will communicate with mobile carriers/device providers to push alerts back to the mobile application.
- **D.** Use AWS DirectConnect or VPN to establish connectivity with mobile carriers EC2 instances will receive the mobile applications ' location through carrier connection: ROS will be used to store and relevant relevant offers EC2 instances will communicate with mobile carriers to push alerts back to the mobile application


## SQS, SNS & Decoupling


**Q28.** Which of the following AWS Cloud services is a fully managed NoSQL database service?

- **A.** Amazon ElastiCache
- **B.** Amazon DynamoDB
- **C.** Amazon Simple Queue Service (Amazon SQS)
- **D.** Amazon Relational Database Service (Amazon RDS)


## EBS Volumes & Snapshots


**Q29.** What is the maximum volume size of a MySQLRDS database?

- **A.** unlimited
- **B.** 6 TB
- **C.** 16 TB
- **D.** 3 TB


**Q30.** You are building the database tier for an enterprise application that gets occasional activity throughout the day. Which storage type should you select as your default option?

- **A.** Provisioned IOPS (SSD)
- **B.** General Purpose Solid State Drive (SSD)
- **C.** Magnetic storage
- **D.** Storage Area Network (SAN)-attached


**Q31.** Your company plans to host a large donation website on Amazon Web Services (AWS). You anticipate a large and undetermined amount of traffic that will create many database writes. To be certain that you do not drop any writes to a database hosted on AWS. Which service should you use?

- **A.** Amazon DynamoDB with provisioned write throughput up to the anticipated peak write
- **B.** Amazon ElastiCache to store the writes until the writes are committed to the database.
- **C.** Amazon RDS with provisioned IOPS up to the anticipated peak write throughput.
- **D.** Amazon Simple Queue Service (SOS) for capturing the writes and draining the queue to write to the database.


**Q32.** If you are using Amazon RDS Provisioned IOPS storage with MySQL and Oracle database engines, you can scale the throughput of your database Instance by specifying the IOPS rate from __________ .

- **A.** 10, 000 to 1, 00, 000
- **B.** 1, 000 to 10, 000
- **C.** 100 to 1, 000
- **D.** 1,000 to 1, 00, 000


**Q33.** Can I use Provisioned IOPS with VPC?

- **A.** Yes for all RDS instances
- **B.** Only with MSSQL based RDS
- **C.** No
- **D.** Only Oracle based RDS


**Q34.** When should I choose Provisioned IOPS over Standard RDS storage?

- **A.** If you have batch-oriented workloads
- **B.** If you use production online transaction processing (OLTP) workloads.
- **C.** If you have workloads that are not sensitive to consistent performance


## EC2 Instances, AMIs & Placement


**Q35.** You are building an application that will collect information about user behavior. The application will rapidly ingest large amounts of dynamic data and requires very low latency. The database must be scalable without incurring downtime. Which database would you recommend for this scenario?

- **A.** RDS with Microsoft SQL
- **B.** RDS with MySQL
- **C.** DynamoDB
- **D.** RedShift


## ElastiCache & Caching Strategies


**Q36.** Your company is starting to use AWS to host new web-based applications. A new two-tier application will be deployed that provides customers with access to data records. It is important that the application is highly responsive and retrieval times are optimized. You’re looking for a persistent data store that can provide the required performance. From the list below what AWS service would you recommend for this requirement?

- **A.** ElastiCache with the Memcached engine
- **B.** Kinesis Data Streams
- **C.** ElastiCache with the Redis engine
- **D.** RDS in a multi-AZ configuration


**Q37.** A major upcoming sales event is likely to result in heavy read traffic to a web application your company manages. As the Solutions Architect you have been asked for advice on how best to protect the database tier from the heavy load and ensure the user experience is not impacted. The web application owner has also requested that the design be fault tolerant. The current configuration consists of a web application behind an ELB that uses Auto Scaling and an RDS MySQL database running in a multi-AZ configuration. As the database load is highly changeable the solution should allow elasticity by adding and removing nodes as required and should also be multi- threaded. What recommendations would you make?

- **A.** Deploy an ElastiCache Redis cluster with cluster mode disabled and multi-AZ with automatic failover
- **B.** Deploy an ElastiCache Memcached cluster in multi-AZ mode in the same AZs as RDS
- **C.** Deploy an ElastiCache Redis cluster with cluster mode enabled and multi-AZ with automatic failover
- **D.** Deploy an ElastiCache Memcached cluster in both AZs in which the RDS database is deployed


**Q38.** What service does not support session data persistence store to enable web-based stateful applications?

- **A.** Redis
- **B.** RedShift
- **C.** DynamoDB
- **D.** RDS
- **E.** Memcached


**Q39.** You are working on a mobile gaming application and are building the leaderboard feature to track the top scores across millions of users. Which AWS services are best suited for this use case?

- **A.** Amazon Redshift
- **B.** Amazon Simple Storage Service (S3)
- **C.** Amazon ElastiCache using Memcached
- **D.** Amazon ElastiCache using Redis


**Q40.** You are configuring your company's application to use Auto Scaling and need to move user state information. Which of the following AWS services provides a shared data store with durability and low latency?

- **A.** Amazon DynamoDB
- **B.** Amazon EC2 instance storage
- **C.** AWS ElastiCache Memcached
- **D.** Amazon Simple Storage Service


**Q41.** Your application is using an ELB in front of an Auto Scaling group of web/application servers deployed across two AZs and a Multi-AZ RDS Instance for data persistence. The database CPU is often above 80% usage and 90% of I/O operations on the database are reads. To improve performance you recently added a single-node Memcached ElastiCache Cluster to cache frequent DB query results. In the next weeks the overall workload is expected to grow by 30%. Do you need to change anything in the architecture to maintain the high availability or the application with the anticipated additional load? (Choose an appropriate reason to support your answer)

- **A.** No if the cache node fails you can always get the same data from the DB without having any availability impact.
- **B.** Yes. you should deploy two Memcached ElastiCache Clusters in different AZs because the ROS Instance will not Be able to handle the load It me cache node fails
- **C.** No. if the cache node fails the automated ElastiCache node recovery feature will prevent any availability impact.
- **D.** Yes you should deploy the Memcached ElastiCache Cluster with two nodes in the same AZ as the RDS DB master instance to handle the load if one cache node fails.


**Q42.** A Solutions Architect has been asked to improve the performance of a DynamoDB table. Latency is currently a few milliseconds and this needs to be reduced to microseconds whilst also scaling to millions of requests per second. What is the BEST architecture to support this?

- **A.** Create a DynamoDB Accelerator (DAX) cluster
- **B.** Reduce the number of Scan operations
- **C.** Create an ElastiCache Redis cluster
- **D.** Use CloudFront to cache the content


**Q43.** You have a requirement to create an index to search customer objects stored in S3 buckets. The solution should enable you to create a metadata search index for each object stored to an S3 bucket. Select the most scalable and cost effective solution?

- **A.** RDS, EMR, ALB
- **B.** DynamoDB, Lambda
- **C.** RDS, ElastiCache
- **D.** RedShift


## Redshift, Athena & Analytics


**Q44.** Your company is a provider of online gaming that customers access with various network access devices including mobile phones. What is a data warehousing solutions for large amounts of information on player behavior, statistics and events for analysis using SQLtools?

- **A.** RDS
- **B.** DynamoDB
- **C.** DynamoDB
- **D.** RedShift
- **E.** Elasticsearch


**Q45.** A Solutions Architect is developing an application that will store and index large (>1 MB) JSON files. The data store must be highly available and latency must be consistently low even during times of heavy usage. Which service should the Architect use?

- **A.** DynamoDB
- **B.** Amazon RedShift
- **C.** AWS CloudFormation
- **D.** Amazon EFS


**Q46.** Which AWS Cloud service is best suited for Online Analytics Processing (OLAP)?

- **A.** Amazon Relational Database Service (Amazon RDS)
- **B.** Amazon Glacier
- **C.** Amazon DynamoDB
- **D.** Amazon Redshift


**Q47.** You are designing an e-commerce web application that will scale to potentially hundreds of thousands of concurrent users. Which database technology is best suited to hold the session state for large numbers of concurrent users?

- **A.** Data warehouse using Amazon Redshift
- **B.** NoSQL database table using Amazon DynamoDB
- **C.** Amazon Simple Storage Service (Amazon S3)
- **D.** Relational database using Amazon Relational Database Service (Amazon RDS)


**Q48.** A company is running a batch analysis every hour on their main transactional DB. running on an RDS MySQL instance to populate their central Data Warehouse running on Redshift During the execution of the batch their transactional applications are very slow When the batch completes they need to update the top management dashboard with the new data The dashboard is produced by another system running on-premises that is currently started when a manually-sent email notifies that an update is required The on- premises system cannot be modified because is managed by another team. How would you optimize this scenario to solve performance issues and automate the process as much as possible?

- **A.** Create an RDS Read Replica for the batch analysis and SNS to notify me on-premises system to update the dashboard
- **B.** Create an RDS Read Replica for the batch analysis and SQS to send a message to the on-premises system to update the dashboard.
- **C.** Replace ROS with Redsnift for the oaten analysis and SQS to send a message to the on-premises system to update the dashboard
- **D.** Replace RDS with Redshift for the batch analysis and SNS to notify the on-premises system to update the dashboard


**Q49.** You are creating a design for a web-based application that will be based on a web front-end using EC2 instances and a database back-end. This application is a low priority and you do not want to incur costs in general day to day management. Which AWS database service can you use that will require the least operational overhead?

- **A.** EMR
- **B.** DynamoDB
- **C.** RedShift
- **D.** RDS


**Q50.** Which AWS database service is best suited for traditional Online Transaction Processing (OLTP)?

- **A.** Elastic Database
- **B.** Amazon Glacier
- **C.** Amazon Redshift
- **D.** Amazon Relational Database Service (Amazon RDS)


## Kinesis & Streaming Ingestion


**Q51.** What Amazon AWS service supports real-time processing of data stream from multiple consumers and replay of records?

- **A.** EMR
- **B.** SQS
- **C.** Ki Kinesis data streams i d t t
- **D.** DynamoDB
- **E.** RedShift


**Q52.** You are deploying an application to collect votes for a very popular television show. Millions of users will submit votes using mobile devices. The votes must be collected into a durable, scalable, and highly available data store for real-time public tabulation. Which service should you use?

- **A.** Amazon Redshift
- **B.** Amazon DynamoDB
- **C.** Amazon Simple Queue Service
- **D.** Amazon Kinesis


## Monitoring: CloudWatch, CloudTrail & Config


**Q53.** In the Amazon cloudwatch, which metric should I be checking to ensure that your DB Instance has enough free storage space?

- **A.** FreeStorageVolume
- **B.** FreeStorage
- **C.** FreeDBStorageSpace
- **D.** FreeStorageSpace


## Elastic Beanstalk & Deployment


**Q54.** A firm is moving its testing platform to AWS to provide developers with instant access to clean test and development environments. The primary requirement for the firm is to make environments easily reproducible and fungible. What service will help the firm meet their requirements?

- **A.** AWS CloudFormation
- **B.** AWS Trusted Advisor
- **C.** Amazon Redshift
- **D.** AWS Config


## General Design


**Q55.** In the context of MySQL, version numbers are organized as MySQL version = X.Y.Z. What does X denote here?

- **A.** Major version
- **B.** Version number
- **C.** Minor version
- **D.** Release level


# Section B - Multiple Response (select all that apply)


## DynamoDB Design & Capacity


**Q56.** Which of the following are IAM security features? **(Select 2.)**

- **A.** MFA
- **B.** Amazon DynamoDB global secondary indexes
- **C.** Password policies
- **D.** Consolidated Billing


**Q57.** Which of the following statements about Amazon DynamoDB tables are true? **(Select 2.)**

- **A.** You can only have one global secondary index.
- **B.** You can only have one local secondary index.
- **C.** Local secondary indexes can only be created when the table is being created.
- **D.** Global secondary indexes can only be created when the table is being created.


**Q58.** What are three advantages of using DynamoDB over S3 for storing IoT sensor data where there are 100,000 data point samples sent per minute? **(Select 3.)**

- **A.** DynamoDB provides fast read/writes to a structured table for queries
- **B.** IoT can write data directly to DynamoDB
- **C.** S3 must create a single file for each event
- **D.** IoT can write data directly to S3
- **E.** DynamoDB is designed for frequent access and fast lookup of small records
- **F.** S3 is designed for frequent access and fast lookup of smaller records


**Q59.** What happens when read or write requests exceed capacity units (throughput capacity) for a DynamoDB table or index? **(Select 2.)**

- **A.** DynamoDB automatically increases read/write units
- **B.** DynamoDB automatically increases read/write units if provisioned throughput is enabled
- **C.** DynamoDB can throttle requests so that requests are not exceeded
- **D.** HTTP 500 code is returned (Server Error)
- **E.** HTTP 400 code is returned (Bad Request)


## RDS Multi-AZ, Read Replicas & Aurora


**Q60.** When using Amazon Relational Database Service (Amazon RDS) Multi-AZ, how can you offload read requests from the primary? **(Select 2.)**

- **A.** Add a read replica DB instance, and configure the client’s application logic to use a read-replica.
- **B.** Amazon RDS automatically sends writes to the primary and sends reads to the secondary.
- **C.** Configure the connection string of the clients to connect to the secondary node and perform reads while the primary is used for writes.
- **D.** Create a caching environment using ElastiCache to cache frequently used data. Update the application logic to read/write from the cache.


**Q61.** There is a new requirement to implement in-memory caching for a Financial Services application due to increasing read-heavy load. The data must be stored persistently. Automatic failover across AZs is also required. Which two items from the list below are required to deliver these requirements? **(Select 2.)**

- **A.** ElastiCache with the Memcached engine
- **B.** ElastiCache with the Redis engine
- **C.** Multiple nodes placed in different AZs
- **D.** Multi-AZ with Cluster mode and Automatic Failover enabled


**Q62.** What cloud compute components are configured by tenants and not Amazon AWS support engineers? **(Select 3.)**

- **A.** Virtual appliances
- **B.** Guest operating system
- **C.** Upstream physical switch
- **D.** RDS
- **E.** Hypervisor
- **F.** Applications and databases


## Auto Scaling & Elastic Load Balancing


**Q63.** A colleague has asked you some questions about how AWS charge for DynamoDB. He is interested in knowing what type of workload DynamoDB is best suited for in relation to cost and how AWS charges for DynamoDB? **(Select 2.)**

- **A.** You provision for expected throughput but are only charged for what you use
- **B.** DynamoDB is more cost effective for write heavy workloads
- **C.** Priced based on provisioned throughput (read/write) regardless of whether you use it or not
- **D.** DynamoDB is more cost effective for read heavy workloads


## EBS Volumes & Snapshots


**Q64.** An application hosted in your VPC uses an EC2 instance with a MySQL DB running on it. The database uses a single 1TB General Purpose SSD (GP2) EBS volume. Recently it has been noticed that the database is not performing well and you need to improve the read performance. What are two possible ways this can be achieved? **(Select 2.)**

- **A.** Add multiple EBS volumes in a RAID 0 array
- **B.** Add an RDS read replica in another AZ
- **C.** Use a provisioned IOPS volume and specify the number of I/O operations required
- **D.** Add multiple EBS volumes in a RAID 1 array


**Q65.** Your team manages a popular website running Amazon Relational Database Service (Amazon RDS) MySQL back end. The Marketing department has just informed you about an upcoming television commercial that will drive thousands of new visitors to the website. How can you prepare your database to handle the load? **(Select 3.)**

- **A.** Create read replicas to offload read requests and update your application.
- **B.** Upgrade to Amazon Redshift for faster columnar storage.
- **C.** Vertically scale the DB Instance by selecting a more powerful instance class.
- **D.** Upgrade the storage from Magnetic volumes to General Purpose Solid State Drive (SSD) volumes.


## High Availability & Fault Tolerance


**Q66.** Which of the following AWS Cloud services are designed according to the Multi-AZ principle? **(Select 2.)**

- **A.** Amazon Simple Storage Service (Amazon S3)
- **B.** Amazon ElastiCache
- **C.** Amazon Virtual Private Cloud (Amazon VPC)
- **D.** Elastic Load Balancing
- **E.** Amazon DynamoDB


## ElastiCache & Caching Strategies


**Q67.** What caching engines are supported with Amazon ElastiCache? **(Select 2.)**

- **A.** CloudFront
- **B.** Redis
- **C.** HAProxy
- **D.** Route 53
- **E.** RedShift
- **F.** Memcached


**Q68.** Your manager has asked you to explain how Amazon ElastiCache may assist with the company痴 plans to improve the performance of database queries. Which of the below statements is a valid description of the benefits of Amazon ElastiCache? **(Select 2.)**

- **A.** ElastiCache can form clusters using a mixture of Memcached and Redis caching engines, allowing you to take advantage of the best features of each caching engine
- **B.** ElastiCache is best suited for scenarios where the data base load type is OLTP
- **C.** The in-memory caching provided by ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads
- **D.** ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in the cloud


**Q69.** Which cache engines does Amazon ElastiCache support? **(Select 2.)**

- **A.** Membase
- **B.** Couchbase
- **C.** Memcached
- **D.** Redis


**Q70.** How can you back up data stored in Amazon ElastiCache running Redis? **(Select 2.)**

- **A.** Create a snapshot manually.
- **B.** Redis clusters cannot be backed up.
- **C.** Create an image of the Amazon Elastic Compute Cloud (Amazon EC2) instance.
- **D.** Configure automatic snapshots to back up the cache environment every night.


**Q71.** Which of the following cache engines are supported by Amazon ElastiCache? **(Select 2.)**

- **A.** Memcached
- **B.** Redis
- **C.** Couchbase
- **D.** MySQL


**Q72.** An application currently uses Memcached to cache frequently used database queries. Which steps are required to migrate the application to use Amazon ElastiCache with minimal changes? **(Select 2.)**

- **A.** Configure a security group to allow access from the application servers.
- **B.** Connect to the Amazon ElastiCache nodes using Secure Shell (SSH) and install the latest version of Memcached.
- **C.** Recompile the application to use the Amazon ElastiCache libraries.
- **D.** Update the configuration file with the endpoint for the Amazon ElastiCache cluster.


**Q73.** Which services allow the customer to retain full administrative privileges of the underlying EC2 instances? **(Select 2.)**

- **A.** AWS Elastic Beanstalk
- **B.** Amazon Elastic Map Reduce
- **C.** Amazon Relational Database Service
- **D.** Amazon DynamoDB
- **E.** Amazon ElastiCache


## Redshift, Athena & Analytics


**Q74.** A company is investigating ways to analyze and process large amounts of data in the cloud faster, without needing to load or transform the data in a data warehouse. The data resides in Amazon S3. Which AWS services would allow the company to query the data in place? **(Select 2.)**

- **A.** Amazon S3 Select
- **B.** Amazon Kinesis Data Streams
- **C.** Amazon RedShift Spectrum
- **D.** Amazon Elasticsearch


**Q75.** Which of the following workloads are a good fit for running on Amazon Redshift? **(Select 2.)**

- **A.** Manage session state and user profile data for thousands of concurrent users
- **B.** Reporting database supporting back-office analytics
- **C.** Data warehouse used to aggregate multiple disparate data sources
- **D.** Transactional database supporting a busy e-commerce order processing website


**Q76.** What two statements are correct when comparing Elasticsearch and RedShift as analytical tools? **(Select 2.)**

- **A.** Elasticsearch supports SQLqueries
- **B.** RedShift supports complex SQL-based queries with Petabyte sized data store
- **C.** Elasticsearch is a text search engine and document indexing tool
- **D.** RedShift provides only basic analytical services
- **E.** Elasticsearch does not support JSON data type


## Disaster Recovery, Backup & RTO/RPO


**Q77.** Some data has become corrupt in an RDS database you manage. You are planning to use point-in-time restore to recover the data to the last known good configuration. Which of the following statements is correct about restoring an RDS database to a specific point-in-time? **(Select 2.)**

- **A.** The default DB security group is applied to the new DB instance
- **B.** You can restore up to the last 1 minute
- **C.** You can restore up to the last 5 minutes
- **D.** The database restore overwrites the existing database


## Monitoring: CloudWatch, CloudTrail & Config


**Q78.** What two statements correctly describe CloudWatch monitoring of database instances? **(Select 2.)**

- **A.** RDS does not support monitoring of operating system metrics
- **B.** Metrics are not enabled automatically for DynamoDB and RDS
- **C.** Metrics are sent automatically from DynamoDB and RDS to CloudWatch
- **D.** Alarms must be configured for DynamoDB and RDS within CloudWatch


---


# Answer Key & Explanations


**Q1. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Maintenance windows are configured to allow DB instance modifications to take place such as scaling and software patching. Some operations require the DB instance to be taken offline brie

**Q2. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon Relational Database Service (Amazon RDS) is a managed service that makes it easy to set up, operate, and scale a relational database in the cloud. With RDS you can configure Multi-AZ which creates a replica in another AZ and synchronously replicates to it (DR only) RedShift is used for analytics OLAP not OLTP If you install a DB on an EC2 instance you will need to manage to OS yourself and the customer wants it to be managed for them DynamoDB is a managed database of the NoSQL type. NoSQL DBs are not relational DBs. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/compute/aws-auto-scaling/

**Q3. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Yes, Amazon RDS will emit a DB instance event to inform you that automatic failover occurred. You can click the “Events” section of the Amazon RDS Console or use the DescribeEvents API to return information about events related to your DB instance. You can also use Amazon RDS Event Notifications to be notified when specific DB events occur. Refer: https://aws.amazon.com/rds/faqs/

**Q4. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Read replicas are supported by MySQL, MariaDB, PostgreSQL, and Aurora.

**Q5. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
All Amazon RDS database engines support Multi-AZ deployment

**Q6. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
A DB instance is an isolated database environment running in the cloud. It is the basic building block of Amazon RDS. A DB instance can contain multiple user-created databases, and can be accessed using the same client tools and applications you might use to access a standalone database instance. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html#:~:text=A%20DB%20instance%20is%20an,access%20a%20standalone%20database%20instance.

**Q7. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Deferred DB instance modifications that you have chosen not to apply immediately are applied during the maintenance window. For example, you may choose to change the DB instance class or parameter group during the maintenance window. To apply the changes to the maintenance window immediately, select Apply immediately. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html

**Q8. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
The SQL Server bulk copy feature is an efficient means of copying data from a source database to your DB instance. Bulk copy writes the data that you specify to a data file, such as an ASCII file. You can then run bulk copy again to write the contents of the file to the destination DB instance. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Snapshots.html

**Q9. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon RDS supports Microsoft SQL Server Enterprise edition and the license is available only under the BYOL model.

**Q10. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
DB instances for Amazon RDS for MySQL, MariaDB, PostgreSQL, Oracle, and Microsoft SQL Server use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage. Depending on the amount of storage requested, Amazon RDS automatically stripes across multiple Amazon EBS volumes to enhance performance. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html

**Q11. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Aurora databases can scale up to 64 TB and Aurora replicas features millisecond latency All other RDS engines have a limit of 16 TiB maximum DB size and asynchronous replication typically takes seconds References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/database/amazon-rds/ https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html

**Q12. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
You would use Mail eXchange (MX) records to define which inbound destination mail server should be used.

**Q13. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
SPF records are used to verify authorized senders of mail from your domain.

**Q14. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Refer: https://status.aws.amazon.com/

**Q15. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q16. D**  
_DynamoDB Design & Capacity_  
Using the Username as a partition key will evenly spread your users across the partitions. Messages are often filtered down by time range, so Timestamp makes sense as a sort key.

**Q17. E**  
_DynamoDB Design & Capacity_  
DynamoDB auto scaling actively manages throughput capacity for tables and global secondary indexes. With auto scaling, you define a range (upper and lower limits) for read and write capacity units. You also define a target utilization percentage within that range. DynamoDB auto scaling seeks to maintain your target utilization, even as your application workload increases or decreases. With DynamoDB auto scaling, a table or a global secondary index can increase its provisioned read and write capacity to handle sudden increases in traffic, without request throttling. When the workload decreases, DynamoDB auto scaling can decrease the throughput so that you don't pay for unused provisioned capacity. Refer: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.ProvisionedThroughput.Manual

**Q18. B**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q19. E**  
_DynamoDB Design & Capacity_  
DynamoDB uses eventually consistent reads, unless you specify otherwise. ... If you set this parameter to true, DynamoDB uses strongly consistent reads during the operation. While reading data from DynamoDB, user can specify whether they want the read to be eventually or strongly consistent, these are the two consistency model in DynamoDB. Eventually Consistent Reads (Default) – the eventual consistency option is used to maximize the read throughput. Refer: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html

**Q20. D**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q21. B**  
_DynamoDB Design & Capacity_  
BatchWriteItem—Writes up to 25 items to one or more tables. DynamoDB processes each item in the batch as an individual PutItem or DeleteItem request (updates are not supported). So DynamoDB first rounds up the size of each item to the next 1 KB boundary, and then calculates the total size. The result is not necessarily the same as the total size of all the items. For example, if BatchWriteItem writes a 500-byte item and a 3.5 KB item, DynamoDB calculates the size as 5 KB (1 KB + 4 KB), not 4 KB (500 bytes + 3.5 KB). Refer: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/switching.capacitymode.html

**Q22. B**  
_DynamoDB Design & Capacity_  
Amazon DynamoDB is best suited for non-relational databases. Amazon RDS and Amazon Redshift are both structured relational databases.

**Q23. D**  
_DynamoDB Design & Capacity_  
Query is the most efficient operation to find a single item in a large table.

**Q24. B**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q25. A**  
_Auto Scaling & Elastic Load Balancing_  
DynamoDB auto scalinguses the AWS Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns. This is the most efficient and cost-effective solution Manually adjusting the provisioned throughput is not efficient Using AWS Lambda to modify the provisioned throughput is possible but it would be more cost-effective to use DynamoDB Auto Scaling as there is no cost to using it DynamoDB DAX is an in-memory cache that increases the performance of DynamoDB. However, it costs money and there is no requirement to increase performance References: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html

**Q26. B**  
_Auto Scaling & Elastic Load Balancing_  
The measurements collected by Amazon CloudWatch provide Auto Scaling with the information needed to run enough Amazon EC2 instances to deal with the traffic load. Auto Scaling updates the Elastic Load Balancing service when new instances are launched or terminated to automatically scale the load-balanced capacity. Refer: https://aws.amazon.com/blogs/aws/new-aws-load-balancing-automatic-scaling-and-cloud-monitoring- services/#:~:text=The%20measurements%20collected%20by%20Amazon,scale%20the%20load%2Dbalanced%20capacity.

**Q27. A**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q28. B**  
_SQS, SNS & Decoupling_  
. Amazon DynamoDB is a fully managed, fast, and flexible NoSQL database service for all applications that need consistent, single- digit millisecond latency at any scale. Amazon SQS, Amazon ElastiCache, and Amazon RDS do not provide a NoSQL database service. Amazon SQS is a managed message queuing service. Amazon ElastiCache is a service that provides in-memory cache in the cloud. Finally, Amazon RDS provides managed relational databases.

**Q29. C**  
_EBS Volumes & Snapshots_  
Amazon RDS for SQL Server Increases Maximum Database Storage Size to 16TB. You can now create Amazon RDS for SQL Server database instances with up to 16TB of storage, up from 4TB. The new storage limit is available when using the Provisioned IOPS and General Purpose (SSD) storage types. Refer:https://aws.amazon.com/about-aws/whats-new/2017/08/amazon-rds-for-sql-server-increases-maxiumum-database-storage- size-to-16-tb/#:~:text=Amazon%20RDS%20for%20SQL%20Server%20Increases%20Maximum%20Database%20Storage%20Size%20to%2016TB,- Posted%20On%3A%20Aug&text=You%20can%20now%20create%20Amazon,Purpose%20(SSD)%20storage%20types.

**Q30. B**  
_EBS Volumes & Snapshots_  
General Purpose (SSD) volumes are generally the right choice for databases that have bursts of activity.

**Q31. C**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q32. B**  
_EBS Volumes & Snapshots_  
Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html

**Q33. A**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q34. B**  
_EBS Volumes & Snapshots_  
Amazon RDS provisions that IOPS rate and storage for the lifetime of the DB instance or until you change it. Provisioned IOPS storage is optimized for I/O intensive, online transaction processing (OLTP) workloads that have consistent performance requirements. Provisioned IOPS helps performance tuning.

**Q35. C**  
_EC2 Instances, AMIs & Placement_  
Amazon Dynamo DB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability Push button scaling means that you can scale the DB at any time without incurring downtime DynamoDB provides low read and write latency RDS uses EC2 instances so you have to change your instance type/size in order to scale compute vertically RedShift uses EC2 instances as well so you need to choose your instance type/size for scaling compute vertically, but you can also scale horizontally by adding more nodes to the cluster Rapid ingestion of dynamic data is not an ideal use case for RDS or RedShift References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/database/amazon-dynamodb/

**Q36. C**  
_ElastiCache & Caching Strategies_  
ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in the cloud. The in-memory caching provided by ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads There are two different database engines with different characteristics as per below: Memcached - Not persistent - Cannot be used as a data store - Supports large nodes with multiple cores or threads - Scales out and in, by adding and removing nodes Redis - Data is persistent - Can be used as a datastore - Not multi-threaded - Scales by adding shards, not nodes Kinesis Data Streams is used for processing streams of data, it is not a persistent data store RDS is not the optimum solution due to the requirement to optimize retrieval times which is a better fit for an in-memory data store such as ElastiCache References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/database/amazon-elasticache/

**Q37. D**  
_ElastiCache & Caching Strategies_  
ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in the cloud The in- memory caching provided by ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads Memcached - Not persistent - Cannot be used as a data store - Supports large nodes with multiple cores or threads - Scales out and in, by adding and removing nodes Redis - Data is persistent - Can be used as a datastore - Not multi-threaded - Scales by adding shards, not nodes References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-elasticache/ https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/SelectEngine.html

**Q38. E**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache for Memcached is a Memcached-compatible in-memory key-value store service that can be used as a cache or a data store. It delivers the performance, ease-of-use, and simplicity of Memcached. ElastiCache for Memcached is fully managed, scalable, and secure - making it an ideal candidate for use cases where frequently accessed data must be in-memory. It is a popular choice for use cases such as Web, Mobile Apps, Gaming, Ad-Tech, and E-Commerce. Refer: https://aws.amazon.com/elasticache/memcached/

**Q39. D**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache with Redis provides native functions that simplify the development of leaderboards. With Memcached, it is more difficult to sort and rank large datasets. Amazon Redshift and Amazon S3 are not designed for high volumes of small reads and writes, typical of a mobile game.

**Q40. D**  
_ElastiCache & Caching Strategies_  
Amazon Simple Storage Service is storage for the Internet. It is designed to make web-scale computing easier for developers. Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html

**Q41. C**  
_ElastiCache & Caching Strategies_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q42. A**  
_ElastiCache & Caching Strategies_  
Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance improvement – from milliseconds to microseconds – even at millions of requests per second It is possible to use ElastiCache in front of DynamoDB, however this is not a supported architecture DynamoDB is not a supported origin for CloudFront Reducing the number of Scan operations on DynamoDB may improve performance but will not reduce latency to microseconds References: https://aws.amazon.com/dynamodb/dax/

**Q43. B**  
_ElastiCache & Caching Strategies_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q44. D**  
_Redshift, Athena & Analytics_  
Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more. This enables you to use your data to acquire new insights for your business and customers. Refer: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html

**Q45. D**  
_Redshift, Athena & Analytics_  
EFS provides a highly-available data store with consistent low latencies and elasticity to scale as required RedShift is a data warehouse that is used for analyzing data using SQL DynamoDB is a low latency, highly available NoSQL DB. You can store JSON files up to 400KB in size in a DynamoDB table, for anything bigger you'd want to store a pointer to an object outside of the table CloudFormation is an orchestration tool and does not help with storing documents References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

**Q46. D**  
_Redshift, Athena & Analytics_  
Amazon Redshift is best suited for traditional OLAP transactions. While Amazon RDS can also be used for OLAP, Amazon Redshift is purpose-built as an OLAP data warehouse.

**Q47. B**  
_Redshift, Athena & Analytics_  
NoSQL databases like Amazon DynamoDB excel at scaling to hundreds of thousands of requests with key/value access to user profile and session.

**Q48. B**  
_Redshift, Athena & Analytics_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q49. B**  
_Redshift, Athena & Analytics_  
Out of the options in the list, DynamoDB requires the least operational overhead as there are no backups, maintenance periods, software updates etc. to deal with RDS, RedShift and EMR all require some operational overhead to deal with backups, software updates and maintenance periods References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-dynamodb/

**Q50. D**  
_Redshift, Athena & Analytics_  
Amazon RDS is best suited for traditional OLTP transactions. Amazon Redshift, on the other hand, is designed for OLAP workloads. Amazon Glacier is designed for cold archival storage.

**Q51. C**  
_Kinesis & Streaming Ingestion_  
Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications. Refer: https://aws.amazon.com/kinesis/data- streams/faqs/#:~:text=Amazon%20Kinesis%20Data%20Streams%20enables%20real%2Dtime%20processing%20of%20streaming,to%20multiple%20Amazon%20Kinesis%20Applications.

**Q52. D**  
_Kinesis & Streaming Ingestion_  
Amazon Kinesis Data Streams is a scalable and durable real-time data streaming service that can continuously capture gigabytes of data per second from hundreds of thousands of sources. Refer: https://aws.amazon.com/kinesis/#:~:text=Amazon%20Kinesis%20Data%20Streams%20is,streams%20into%20AWS%20data%20stores

**Q53. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Create alarms in the CloudWatch console or use the AWS Command Line Interface (AWS CLI) to create alarms that monitor free storage space. By creating CloudWatch alarms that notify you when the FreeStorageSpace metric reaches a defined threshold, you can prevent storage full issues. This can prevent downtime that occurs when your RDS DB instance runs out of storage. Refer: https://aws.amazon.com/premiumsupport/knowledge- center/storage-full-rds-cloudwatch-alarm/

**Q54. A**  
_Elastic Beanstalk & Deployment_  
With AWS CloudFormation, you can reuse your template to set up your resources consistently and repeatedly. Just describe your resources once and then provision the same resources over and over in multiple stacks.

**Q55. A**  
_General Design_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q56. A, C**  
_DynamoDB Design & Capacity_  
Amazon DynamoDB global secondary indexes are a performance feature of Amazon DynamoDB; Consolidated Billing is an accounting feature allowing all bills to roll up under a single account. While both are very valuable features, neither is a security feature.

**Q57. B, C**  
_DynamoDB Design & Capacity_  
You can only have a single local secondary index, and it must be created at the same time the table is created. You can create many global secondary indexes after the table has been created.

**Q58. A, B, E**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q59. C, E**  
_DynamoDB Design & Capacity_  
Provisioned throughput is the maximum amount of capacity that an application can consume from a table or index. If your application exceeds your provisioned throughput capacity on a table or index, it is subject to request throttling. Throttling prevents your application from consuming too many capacity units. When a request is throttled, it fails with an HTTP 400 code (Bad Request) and a ProvisionedThroughputExceededException. The AWS SDKs have built-in support for retrying throttled requests (see Error Retries and Exponential Backoff), so you do not need to write this logic yourself. Refer: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html

**Q60. A, D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon RDS allows for the creation of one or more read-replicas for many engines that can be used to handle reads. Another common pattern is to create a cache using Memcached and Amazon ElastiCache to store frequently used queries. The secondary slave DB Instance is not accessible and cannot be used to offload queries.

**Q61. B, D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Redis engine stores data persistently Memached engine does not store data persistently Redis engine supports Multi-AZ using read replicas in another AZ in the same region You can have a fully automated, fault tolerant ElastiCache-Redis implementation by enabling both cluster mode and multi- AZ failover Memcached engine does not support Multi-AZ failover or replication. References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/database/amazon-elasticache/

**Q62. A, B, F**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q63. C, D**  
_Auto Scaling & Elastic Load Balancing_  
DynamoDB charges: - DynamoDB is more cost effective for read heavy workloads - It is priced based on provisioned throughput (read/write) regardless of whether you use it or not NOTE: With the DynamoDB Auto Scaling feature you can now have DynamoDB dynamically adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns. However, this is relatively new and may not yet feature on the exam. See the link below for more details References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/database/amazon-dynamodb/ https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html

**Q64. A, C**  
_EBS Volumes & Snapshots_  
RAID 0 = 0 striping – data is written across multiple disks and increases performance but no redundancy RAID 1 = 1 mirroring – creates 2 copies of the data but does not increase performance, only redundancy SSD, Provisioned IOPS – I01 provides higher performance than General Purpose SSD (GP2) and you can specify the IOPS required up to 50 IOPS per GB and a maximum of 32000 IOPS RDS read replicas cannot be created from EC2 instances Creating an active/passive cluster doesn't improve read performance as the passive node is not servicing requests. This is use for fault tolerance References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ebs/

**Q65. A, C, D**  
_EBS Volumes & Snapshots_  
Vertically scaling up is one of the simpler options that can give you additional processing power without making any architectural changes. Read replicas require some application changes but let you scale processing power horizontally. Finally, busy databases are often I/O- bound, so upgrading storage to General Purpose (SSD) or Provisioned IOPS (SSD) can often allow for additional request processing.

**Q66. A, E**  
_High Availability & Fault Tolerance_  
Amazon DynamoDB runs across AWS proven, high-availability data centers. The service replicates data across three facilities in an AWS region to provide fault tolerance in the event of a server failure or Availability Zone outage. Amazon S3 provides durable infrastructure to store important data and is designed for durability of 99.999999999% of objects. Your data is redundantly stored across multiple facilities and multiple devices in each facility.

**Q67. B, F**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache supports two major open source in-memory caching engines: Memcached and Redis. ElastiCache users typically select between the two caching engines, depending on the design of the corresponding application.

**Q68. C, D**  
_ElastiCache & Caching Strategies_  
ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in the cloud The in- memory caching provided by ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads ElastiCache is best for scenarios where the DB load is based on Online Analytics Processing (OLAP) transactions not Online Transaction Processing (OLTP) Elasticache EC2 nodes cannot be accessed from the Internet, nor can they be accessed by EC2 instances in other VPCs You cannot mix Memcached and Redis in a cluster References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/networking-and-content-delivery/amazon-route-53/

**Q69. C, D**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache supports both Memcached and Redis. You can run self- managed installations of Membase and Couchbase using Amazon Elastic Compute Cloud

**Q70. A, D**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache with the Redis engine allows for both manual and automatic snapshots. Memcached does not have a backup function.

**Q71. A, B**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache supports Memcached and Redis cache engines. MySQL is not a cache engine, and Couchbase is not supported.

**Q72. A, D**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache is Application Programming Interface (API)-compatible with existing Memcached clients and does not require the application to be recompiled or linked against the libraries. Amazon ElastiCache manages the deployment of the Amazon ElastiCache binaries.

**Q73. A, B**  
_ElastiCache & Caching Strategies_  
AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, . NET, PHP, Node. js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. Refer: https://aws.amazon.com/elasticbeanstalk/ Amazon Elastic MapReduce (Amazon EMR) is a web service that makes it easy to quickly and cost-effectively process vast amounts of data. Amazon EMR uses Hadoop, an open source framework, to distribute your data and processing across a resizable cluster of Amazon EC2 instances. Refer: https://www.amazonaws.cn/en/elasticmapreduce/#:~:text=Amazon%20Elastic%20MapReduce%20(Amazon%20EMR,cluster%20of%20Amazon%20EC2%20instances.

**Q74. A, C**  
_Redshift, Athena & Analytics_  
Amazon S3 Select is designed to help analyze and process data within an object in Amazon S3 buckets, faster and cheaper. It works by providing the ability to retrieve a subset of data from an object in Amazon S3 using simple SQL expressions Amazon Redshift Spectrum allows you to directly run SQL queries against exabytes of unstructured data in Amazon S3. No loading or transformation is required Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. It does not allow you to perform query-in-place operations on S3 Amazon Elasticsearch Service, is a fully managed service that makes it easy for you to deploy, secure, operate, and scale Elasticsearch to search, analyze, and visualize data in real-time Amazon SWF helps developers build, run, and scale background jobs that have parallel or sequential steps References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-redshift/ https://aws.amazon.com/blogs/aws/s3-glacier- select/ https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-spectrum-is-now-available-in-four-additional-aws-regions-and-enhances- query-performance-in-all-available-aws-regions/

**Q75. B, C**  
_Redshift, Athena & Analytics_  
Amazon Redshift is an Online Analytical Processing (OLAP) data warehouse designed for analytics, Extract, Transform, Load (ETL), and high-speed querying. It is not well suited for running transactional applications that require high volumes of small inserts or updates.

**Q76. B, C**  
_Redshift, Athena & Analytics_  
Refer:https://aws.amazon.com/big-data/datalakes-and-analytics/

**Q77. A, C**  
_Disaster Recovery, Backup & RTO/RPO_  
Restored DBs will always be a new RDS instance with a new DNS endpoint and you can restore up to the last 5 minutes You cannot restore from a DB snapshot to an existing DB – a new instance is created when you restore Only default DB parameters and security groups are restored – you must manually associate all other DB parameters and SGs. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/database/amazon-rds/ https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html

**Q78. C, D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._
