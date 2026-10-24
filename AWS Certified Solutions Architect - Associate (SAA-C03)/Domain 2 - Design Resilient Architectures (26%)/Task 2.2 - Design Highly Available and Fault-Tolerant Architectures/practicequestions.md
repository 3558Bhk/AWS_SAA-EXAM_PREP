# Task 2.2 - Design Highly Available and Fault-Tolerant Architectures - Practice Questions

> **Domain 2 - Design Resilient Architectures (26%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **57 multiple-choice (single answer)** followed by **27 multiple-response (select 2+)**. Total **84**.


**Topic order in this file:** RDS Multi-AZ, Read Replicas & Aurora → S3 Security, Access & Durability → Auto Scaling & Elastic Load Balancing → IAM Roles, Policies & Permissions → SQS, SNS & Decoupling → EBS Volumes & Snapshots → High Availability & Fault Tolerance → Route 53 & DNS Routing → EC2 Instances, AMIs & Placement → Disaster Recovery, Backup & RTO/RPO → Monitoring: CloudWatch, CloudTrail & Config → Elastic Beanstalk & Deployment → S3 Storage Classes & Lifecycle → Encryption & AWS KMS → ElastiCache & Caching Strategies


---


# Section A - Multiple Choice (one correct answer)


## RDS Multi-AZ, Read Replicas & Aurora


**Q1.** If you have chosen Multi-AZ deployment, in the event of a planned or unplanned outage of your primary DB Instance, Amazon RDS automatically switches to the standby replica. The automatic failover mechanism simply changes the ______ record of the main DB Instance to point to the standby DB Instance.

- **A.** TXT
- **B.** DNAME
- **C.** MX
- **D.** DNS


**Q2.** My Read Replica appears "stuck" after a Multi-AZ failover and is unable to obtain or apply updates from the source DB Instance. What do I do?

- **A.** You will need to delete the DB Instance and create a new one to replace it.
- **B.** The instance should be deployed to Single AZ and then moved to Multi- AZ once again
- **C.** You will need to delete the Read Replica and create a new one to replace it.
- **D.** You will need to disassociate the DB Engine and re associate it.


**Q3.** Your team is building an order processing system that will span multiple Availability Zones. During testing, the team wanted to test how the application will react to a database failover. How can you enable this type of test?

- **A.** Terminate the DB instance, and create a new one. Update the connection string.
- **B.** It is not possible to test a failover.
- **C.** Create a support case asking for a failover.
- **D.** Force a Multi-AZ failover from one Availability Zone to another by rebooting the primary instance using the Amazon RDS console.


**Q4.** If I have multiple Read Replicas for my master DB Instance and I promote one of them, what happens to the rest of the Read Replicas?

- **A.** The remaining Read Replicas will be deleted
- **B.** The remaining Read Replicas will still replicate from the older master DB Instance
- **C.** The remaining Read Replicas will be combined to one read replica


**Q5.** You are a Solutions Architect at Digital Cloud Training. A large multi-national client has requested a design for a multi-region database. The master database will be in the EU (Frankfurt) region and databases will be located in 4 other regions to service local read traffic. The database should be a fully managed service including the replication. Which AWS service can deliver these requirements?

- **A.** RDS with cross-region Read Replicas
- **B.** DynamoDB with Global Tables
- **C.** RDS with Multi-AZ
- **D.** EC2 instances with EBS replication


**Q6.** It is advised that you watch the Amazon CloudWatch "_____" metric (available via the AWS Management Console or Amazon Cloud Watch APIs) carefully and recreate the Read Replica should it fall behind due to replication errors.

- **A.** Read Replica
- **B.** Single Replica
- **C.** Write Lag
- **D.** Replica Lag


**Q7.** Your e-commerce application provides daily and ad hoc reporting to various business units on customer purchases. This is resulting in an extremely high level of read traffic to your MySQL Amazon Relational Database Service (Amazon RDS) instance. What can you do to scale up read traffic without impacting your database’s performance?

- **A.** Modify the Amazon RDS instance to be a Multi-AZ deployment.
- **B.** Change the Amazon RDS instance DB engine version.
- **C.** Create a read replica for an Amazon RDS instance.
- **D.** Increase the allocated storage for the Amazon RDS instance.


**Q8.** You are a solutions architect working for a media company that hosts its website on AWS. Currently, there is a single Amazon Elastic Compute Cloud (Amazon EC2) Instance on AWS with MySQL installed locally to that Amazon EC2 Instance. You have been asked to make the company’s production environment more resilient and to increase performance. You suggest that the company split out the MySQL database onto an Amazon RDS Instance with Multi-AZ enabled. This addresses the company’s increased resiliency requirements. Now you need to suggest how you can increase performance. Ninety-nine percent of the company’s end users are magazine subscribers who will be reading additional articles on the website, so only one percent of end users will need to write data to the site. What should you suggest to increase performance?

- **A.** Alter the connection string so that if a user is going to write data, it is written to the secondary copy of the Multi-AZ database.
- **B.** Recommend that the company use read replicas, and distribute the traffic across multiple read replicas.
- **C.** Alter the connection string so that if a user is going to write data, it is written to the primary copy of the Multi-AZ database.
- **D.** Migrate the MySQL database to Amazon Redshift to take advantage of columnar storage and maximize performance.


**Q9.** You are a system administrator whose company has moved its production database to AWS. Your company monitors its estate using Amazon CloudWatch, which sends alarms using Amazon Simple Notification Service (Amazon SNS) to your mobile phone. One night, you get an alert that your primary Amazon Relational Database Service (Amazon RDS) Instance has gone down. You have Multi-AZ enabled on this instance. What should you do to ensure the failover happens quickly?

- **A.** Connect to your server using Secure Shell (SSH) and update your connection strings so that your application can communicate to the secondary instance instead of the failed primary instance.
- **B.** Update your Domain Name System (DNS) to point to the secondary instance’s new IP address, forcing your application to fail over to the secondary instance.
- **C.** No action is necessary. Your connection string points to the database endpoint, and AWS automatically updates this endpoint to point to your secondary instance.
- **D.** Take a snapshot of the secondary instance and create a new instance using this snapshot, then update your connection string to point to the new instance.


**Q10.** A 3-tier e-commerce web application is current deployed on-premises and will be migrated to AWS for greater scalability and elasticity The web server currently shares read-only data using a network distributed file system The app server tier uses a clustering mechanism for discovery and shared session state that depends on IP multicast The database tier uses shared-storage clustering to provide database fall over capability, and uses several read slaves for scaling Data on all servers and the distributed file system directory is backed up weekly to off-site tapes Which AWS storage and database architecture meets the requirements of the application?

- **A.** Web servers store -read-only data in S3, and copy from S3 to root volume at boot time App servers share state using a combination of DynamoDB and IP unicast Database, use RDS with multi-AZ deployment and one or more read replicas Backup web servers app servers, and database backed up weekly to Glacier using snapshots.
- **B.** Web servers, store read-only data in an EC2 NFS server, mount to each web server at boot time App servers share state using a combination of DynamoDB and IP multicast Database use RDS with multi-AZ deployment and one or more Read Replicas Backup web and app servers backed up weekly via Mils database backed up via DB snapshots
- **C.** Web servers, store read-only data in S3, and copy from S3 to root volume at boot time App servers snare state using a combination or DynamoDB and IP unicast Database use RDS with multi-AZ deployment and one or more Read Replicas Backup web and app servers backed up weekly via Mils database backed up via DB snapshots.
- **D.** Web servers store read-only data In S3 and copy from S3 to root volume at boot time App servers share state using a combination of DynamoDB and IP unicast Database use RDS with multi-AZ deployment Backup web and app servers backed up weekly via AM is. Database backed up via DB snapshots


**Q11.** What is the charge for the data transfer incurred in replicating data between your primary and standby?

- **A.** Same as the standard data transfer charge
- **B.** No charge. It is free.
- **C.** Double the standard data transfer charge
- **D.** Half of the standard data transfer charge


**Q12.** Your company has HQ in Tokyo and branch offices all over the world and is using a logistics software with a multi-regional deployment on AWS in Japan, Europe and USA. The logistic software has a 3-tier architecture and currently uses MySQL 5.6 for data persistence. Each region has deployed its own database In the HQ region you run an hourly batch process reading data from every region to compute cross-regional reports that are sent by email to all offices this batch process must be completed as fast as possible to quickly optimize logistics how do you build the database architecture in order to meet the requirements’?

- **A.** For each regional deployment, use RDS MySQL with a master in the region and send hourly RDS snapshots to the HQ region
- **B.** For each regional deployment, use MySQL on EC2 with a master in the region and send hourly EBS snapshots to the HQ region
- **C.** For each regional deployment, use MySQL on EC2 with a master in the region and use S3 to copy data files hourly to the HQ region
- **D.** For each regional deployment, use RDS MySQL with a master in the region and a read replica in the HQ region
- **E.** Use Direct Connect to connect all regional MySQL deployments to the HQ region and reduce network latency for the batch process


**Q13.** As a Solutions Architect at Digital Cloud Training you are helping a client to design a multi-tier web application architecture. The client has requested that the architecture provide low-latency connectivity between all servers and be resilient across multiple locations. The client uses Microsoft SQL Server for existing databases. The client has a limited budget for staff costs and does not need to access the underlying operating system What would you recommend as the most efficient solution?

- **A.** Amazon EC2 instances with Microsoft SQL Server and data replication between two different AZs
- **B.** Amazon RDS with Microsoft SQL Server
- **C.** Amazon EC2 instances with Microsoft SQL Server and data replication within an AZ
- **D.** Amazon RDS with Microsoft SQL Server in a Multi-AZ configuration


**Q14.** You are a Solutions Architect at Digital Cloud Training. A large multi-national client has requested a design for a multi-region, multi-master database. The client has requested that the database be designed for fast, massively scaled applications for a global user base. The database should be a fully managed service including the replication. Which AWS service can deliver these requirements?

- **A.** EC2 instances with EBS replication
- **B.** RDS with Multi-AZ
- **C.** S3 with Cross Region Replication
- **D.** DynamoDB with Global Tables and Cross Region Replication


**Q15.** Fill in the blanks: "To ensure failover capabilities, consider using a _____ for incoming traffic on a network interface".

- **A.** secondary private IP
- **B.** secondary public IP
- **C.** add on secondary IP
- **D.** primary public IP


**Q16.** While launching an RDS DB instance, on which page I can select the Availability Zone?

- **A.** ADDITIONAL CONFIGURATION
- **B.** MANAGEMENT OPTIONS
- **C.** DB INSTANCE DETAILS
- **D.** REVIEW


**Q17.** _________ let you categorize your EC2 resources in different ways, for example, by purpose, owner, or environment.

- **A.** Special filters
- **B.** Tags
- **C.** Pointers
- **D.** Wildcards


## S3 Security, Access & Durability


**Q18.** How is data stored in Amazon Simple Storage Service (Amazon S3) for high durability?

- **A.** Data is automatically replicated to other regions.
- **B.** Data is automatically backed up on tape and restored if needed.
- **C.** Data is automatically replicated within a region.
- **D.** Data is replicated only if versioning is enabled on the bucket.


**Q19.** You have a popular web application that accesses data stored in an Amazon Simple Storage Service (Amazon S3) bucket. You expect the access to be very read-intensive, with expected request rates of up to 500 GETs per second from many clients. How can you increase the performance and scalability of Amazon S3 in this case?

- **A.** Turn on cross-region replication to ensure that data is served from multiple locations.
- **B.** Ensure that key names are sequential to enable pre-fetch.
- **C.** Ensure randomness in the namespace by including a hash prefix to key names.
- **D.** Turn on server access logging.


## Auto Scaling & Elastic Load Balancing


**Q20.** How are DNS records managed with Amazon AWS to enable high availability?

- **A.** Reverse proxy
- **B.** Auto-Scaling
- **C.** Elastic load balancing
- **D.** Server health checks


## IAM Roles, Policies & Permissions


**Q21.** What statement correctly describes IAM architecture?

- **A.** IAM security is defined separately per region and cross-region security enabled for an AWS account
- **B.** IAM security is defined per region for roles only on an AWS tenant account
- **C.** IAM allows you to manage users, groups, and roles and their corresponding level of access to the AWS Platform.
- **D.** IAM security is globally unified across the AWS cloud for an AWS tenant account
- **E.** IAM security is unified per region and replicated based on requirements for an AWS tenant account


## SQS, SNS & Decoupling


**Q22.** You have been asked to design a cloud-native application architecture using AWS services. What is a typical use case for SQS?

- **A.** Sending emails to clients when a job is completed
- **B.** Co-ordination of work items between different human and non-human workers
- **C.** Decoupling application components to ensure that there is no dependency on the availability of a single component
- **D.** Providing fault tolerance for S3


## EBS Volumes & Snapshots


**Q23.** What storage type is recommended for an online transaction processing (OLTP) application deployed to Multi-AZ RDS with significant workloads?

- **A.** General Purpose SSD
- **B.** Provisioned IOPS
- **C.** EBS volumes
- **D.** Magnetic


**Q24.** Which procedure for backing up a relational database on EC2 that is using a set of RAlDed EBS volumes for storage minimizes the time during which the database cannot be written to and results in a consistent backup?

- **A.** 1. Detach EBS volumes, 2. Start EBS snapshot of volumes, 3. Re-attach EBS volumes
- **B.** 1. Suspend disk I/O, 2. Start EBS snapshot of volumes, 3. Wait for snapshots to complete, 4. Resume disk I/O
- **C.** 1. Suspend disk I/O, 2. Create an image of the EC2 Instance, 3. Resume disk I/O
- **D.** 1. Suspend disk I/O, 2. Start EBS snapshot of volumes, 3. Resume disk I/O
- **E.** 1. Stop the EC2 Instance. 2. Snapshot the EBS volumes


**Q25.** An EBS-backed EC2 instance has been configured with some proprietary software that uses an embedded license. You need to move the EC2 instance to another Availability Zone (AZ) within the region. How can this be accomplished? Choose the best answer.

- **A.** Perform a copy operation to move the EC2 instance to the destination AZ
- **B.** Create an image from the instance. Launch an instance from the AMI in the destination AZ
- **C.** Take a snapshot of the instance. Create a new EC2 instance and perform a restore from the snapshot
- **D.** Use the AWS Management Console to select a different AZ for the existing instance


**Q26.** When creation of an EBS snapshot is initiated, but not completed, the EBS volume _____________________.

- **A.** Can be used while the snapshot is in progress.
- **B.** Cannot be used until the snapshot completes.
- **C.** Cannot be detached or attached to an EC2 instance until the snapshot completes
- **D.** Can be used in read-only mode while the snapshot is in progress.


**Q27.** How are the EBS snapshots saved on Amazon S3?

- **A.** Exponentially
- **B.** Decrementally
- **C.** EBS snapshots are not stored in the Amazon S3
- **D.** Incrementally


**Q28.** To help prevent data loss due to the failure of any single hardware component, Amazon Elastic Block Storage (Amazon EBS) automatically replicates EBS volume data to which of the following?

- **A.** Amazon EBS replicates EBS volume data within the same Availability Zone in a region.
- **B.** Amazon EBS replicates EBS volume data across Availability Zones in the same region and in Availability Zones in one other region.
- **C.** Amazon EBS replicates EBS volume data across Availability Zones in the same region and in Availability Zones in every other region.
- **D.** Amazon EBS replicates EBS volume data across other Availability Zones within the same region.


**Q29.** How is a volume selected (identified) when making an EBS Snapshot?

- **A.** ARN
- **B.** tag
- **C.** volume id
- **D.** account id


**Q30.** You are restoring an Amazon Elastic Block Store (Amazon EBS) volume from a snapshot. How long will it be before the data is available?

- **A.** The data will be available immediately.
- **B.** It depends on the amount of data stored on the volume.
- **C.** It depends on the provisioned size of the volume.
- **D.** It depends on whether the attached instance is an Amazon EBS-optimized instance.


**Q31.** You need to take a snapshot of an Amazon Elastic Block Store (Amazon EBS) volume. How long will the volume be unavailable?

- **A.** It depends on the provisioned size of the volume.
- **B.** It depends on whether the attached instance is an Amazon EBS-optimized instance.
- **C.** The volume will be available immediately.
- **D.** It depends on the amount of data stored on the volume.


**Q32.** How can an EBS volume that is currently attached to an EC2 instance be migrated from one Availability Zone to another?

- **A.** Detach the volume and attach it to another EC2 instance in the other AZ.
- **B.** Create a snapshot of the volume, and create a new volume from the snapshot in the other AZ.
- **C.** Detach the volume, then use the ec2-migrate-voiume command to move it to another AZ.
- **D.** Simply create a new volume in the other AZ and specify the original volume as the source.


**Q33.** You have been using Amazon Relational Database Service (Amazon RDS) for the last year to run an important application with automated backups enabled. One of your team members is performing routine maintenance and accidentally drops an important table, causing an outage. How can you recover the missing data while minimizing the duration of the outage?

- **A.** Restore only the dropped table from the DB snapshot.
- **B.** The data cannot be recovered.
- **C.** Perform an undo operation and recover the table.
- **D.** Restore the database from a recent automated DB snapshot.


**Q34.** While creating the snapshots using the command line tools, which command should I be using?

- **A.** ec2-new-snapshot
- **B.** ec2-fresh-snapshot
- **C.** ec2-create-snapshot
- **D.** ec2-deploy-snapshot


**Q35.** While creating the snapshots using the API, which Action should I be using?

- **A.** MakeSnapShot
- **B.** FreshSnapshot
- **C.** CreateSnapshot
- **D.** DeploySnapshot


## High Availability & Fault Tolerance


**Q36.** Your company runs a two-tier application on the AWS cloud that is composed of a web front-end and an RDS database. The web front-end uses multiple EC2 instances in multiple Availability Zones (AZ) in an Auto Scaling group behind an Elastic Load Balancer. Your manager is concerned about a single point of failure in the RDS database layer. What would be the most effective approach to minimizing the risk of an AZ failure causing an outage to your database layer?

- **A.** Create a Read Replica of the RDS DB instance in another AZ
- **B.** Increase the DB instance size
- **C.** Enable Multi-AZ for the RDS DB instance
- **D.** Take a snapshot of the database


**Q37.** Each AWS region is composed of two or more locations that offer organizations the ability to operate production systems that are more highly available, fault tolerant, and scalable than would be possible using a single data center. What are these locations called?

- **A.** Replication areas
- **B.** Geographic districts
- **C.** Availability Zones
- **D.** Compute centers


**Q38.** You are a Solutions Architect at Digital Cloud Training. A client has requested a design for a highly-available, fault tolerant architecture for the web and app tiers of a three-tier application. The requirements are as follows: - Web instances will be in a public subnet and app instances will be in a private subnet - Connections to EC2 instances should be automatically distributed across AZs - A minimum of 12 web server EC2 instances must be running at all times - A minimum of 6 app server EC2 instances must be running at all times - The failure of a single availability zone (AZ) must not affect The availability of The application or result in a reduction of capacity beneath The stated requirements Which of the following design options would be the most suitable and cost-effective solution?

- **A.** One Auto Scaling Group with a minimum of 12 EC2 instances for the web layer. One Auto Scaling Group using 3 AZs and a minimum of 6 EC2 instances for the app layer. A single Internet-facing ALB using 3 AZs and two target groups for the web and app layers
- **B.** One Auto Scaling Group with a minimum of 18 EC2 instances for the web layer. One Auto Scaling Group using 3 AZs and a minimum of 9 EC2 instances for the app layer. A single Internet-facing ALB using 3 AZs and two target groups for the web and app layers
- **C.** One Auto Scaling Group using 3 AZs and a minimum of 12 EC2 instances behind an Internet facing ALB for the web layer. One Auto Scaling Group using 3 AZs and a minimum of 6 EC2 instances behind an internal-only ALB for the app layer
- **D.** One Auto Scaling Group using 3 AZs and a minimum of 18 EC2 instances behind an Internet facing ALB for the web layer. One Auto Scaling Group using 3 AZs and a minimum of 9 EC2 instances behind an internal-only ALB for the app layer


**Q39.** A company is deploying a new two-tier web application in AWS. The company has limited staff and requires high availability, and the application requires complex queries and table joins. Which configuration provides the solution for the company's requirements?

- **A.** MySQL Installed on two Amazon EC2 Instances in a single Availability Zone
- **B.** Amazon RDS for MySQL with Multi-AZ
- **C.** Amazon DynamoDB
- **D.** Amazon ElastiCache


**Q40.** For an application running in the ap-northeast-1 region with three Availability Zones (apnortheast-1a, ap-northeast-1b, and ap-northeast-1c), which instance deployment provides high availability for the application that normally requires nine running Amazon Elastic Compute Cloud (Amazon EC2) instances but can run on a minimum of 65 percent capacity while Auto Scaling launches replacement instances in the remaining Availability Zones?

- **A.** Deploy the application on four servers in ap-northeast-1a and five servers in apnortheast-1b, and keep five stopped instances in ap-northeast-1a as reserve.
- **B.** Deploy the application on three servers in ap-northeast-1a, three servers in apnortheast-1b, and three servers in ap-northeast-1c.
- **C.** Deploy the application on six servers in ap-northeast-1b and three servers in apnortheast-1c.
- **D.** Deploy the application on nine servers in ap-northeast-1b, and keep nine stopped instances in ap-northeast-1a as reserve.


**Q41.** A client application requires operating system privileges on a relational database server. What is an appropriate configuration for a highly available database architecture?

- **A.** A standalone Amazon EC2 instance
- **B.** Amazon RDS in a Multi-AZ configuration
- **C.** Amazon EC2 instances in a replication configuration utilizing two different Availability Zones
- **D.** Amazon EC2 instances in a replication configuration utilizing a single Availability Zone


**Q42.** You have a web application running on six Amazon EC2 instances, consuming about 45% of resources on each instance. You are using auto-scaling to make sure that six instances are running at all times. The number of requests this application processes is consistent and does not experience spikes. The application is critical to your business and you want high availability at all times. You want the load to be distributed evenly between all instances. You also want to use the same Amazon Machine Image (AMI) for all instances. Which of the following architectural choices should you make?

- **A.** Deploy 3 EC2 instances in one availability zone and 3 in another availability zone and use Amazon Elastic Load Balancer.
- **B.** Deploy 6 EC2 instances in one availability zone and use Amazon Elastic Load Balancer.
- **C.** Deploy 2 EC2 instances in three regions and use Amazon Elastic Load Balancer.
- **D.** Deploy 3 EC2 instances in one region and 3 in another region and use Amazon Elastic Load Balancer.


**Q43.** As a Solutions Architect, how should you architect systems on AWS?

- **A.** You should architect your AWS usage to take advantage of Amazon Simple Storage Service’s (Amazon S3) durability.
- **B.** You should architect with Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling to ensure capacity is available when needed.
- **C.** You should architect your AWS usage to take advantage of multiple regions and Availability Zones.
- **D.** You should architect for least cost.


**Q44.** Which of the following statements best describes an Availability Zone?

- **A.** Each Availability Zone consists of multiple discrete data centers with shared power and redundant networking/connectivity
- **B.** Each Availability Zone consists of multiple discrete regions, each with a single data center with redundant power and networking/connectivity.
- **C.** Each Availability Zone consists of multiple discrete data centers with redundant power and networking/connectivity.
- **D.** E Each Availability Zone consists of a single discrete data center with redundant power and networking/connectivity. h A il bilit Z i t f i l di t d t t ith d d t d t ki / ti it


**Q45.** You are planning to launch a RedShift cluster for processing and analyzing a large amount of data. The RedShift cluster will be deployed into a VPC with multiple subnets. Which construct is used when provisioning the cluster to allow you to specify a set of subnets in the VPC that the cluster will be deployed into?

- **A.** Availability Zone (AZ)
- **B.** Cluster Subnet Group
- **C.** Subnet Group
- **D.** DB Subnet Group


**Q46.** What is the recommended method for migrating (copying) an EC2 instance to a different region?

- **A.** Terminate instance, select region, copy instance to destination region
- **B.** Select AMI associated with EC2 instance and use Copy AMI option
- **C.** Cross-region copy is not currently supported
- **D.** Stop instance and copy AMI to destination region


**Q47.** What feature is supported when attaching or detaching an EBS volume from an EC2 instance?

- **A.** EBS volume can be attached and detached to an EC2 instance that is cross-region
- **B.** EBS volume can only be copied and attached to an EC2 instance that is cross-region
- **C.** EBS volume can only be attached and detached to an EC2 instance in the same Availability Zone
- **D.** EBS volume can be attached and detached to an EC2 instance in the same region


## Route 53 & DNS Routing


**Q48.** Your company has its primary production site in Western Europe and its DR site in the Asia Pacific. You need to configure DNS so that if your primary site becomes unavailable, you can fail DNS over to the secondary site. Which DNS routing policy would best achieve this?

- **A.** Failover routing
- **B.** Simple routing
- **C.** Geolocation routing
- **D.** Weighted routing


**Q49.** You are rolling out A and B test versions of a web application to see which version results in the most sales. You need 10 percent of your traffic to go to version A, 10 percent to go to version B, and the rest to go to your current production version. Which routing policy should you choose to achieve this?

- **A.** Simple routing
- **B.** Weighted routing
- **C.** Geolocation routing
- **D.** Failover routing


**Q50.** You have an application that for legal reasons must be hosted in the United States when U.S. citizens access it. The application must be hosted in the European Union when citizens of the EU access it. For all other citizens of the world, the application must be hosted in Sydney. Which routing policy should you choose in order to achieve this?

- **A.** Failover routing
- **B.** Latency-based routing
- **C.** Geolocation routing
- **D.** Simple routing


**Q51.** Which is a function that Amazon Route 53 does not perform?

- **A.** DNS service
- **B.** Load balancing
- **C.** Domain registration
- **D.** Health checks


**Q52.** Your website is hosted on a fleet of web servers that are load balanced across multiple Availability Zones using an Elastic Load Balancer (ELB). What type of record set in Amazon Route 53 can be used to point myawesomeapp.com to your website?

- **A.** Type A Alias resource record set
- **B.** TXT record set
- **C.** CNAME record set
- **D.** MX record set


**Q53.** Does Amazon Route 53 support NS Records?

- **A.** It supports only MX records.
- **B.** Yes, it supports Name Service records.
- **C.** Yes, it supports Name Server records.
- **D.** No


## EC2 Instances, AMIs & Placement


**Q54.** A week before Cyber Monday last year, your corporate data center experienced a failed air conditioning unit that caused flooding into the server racks. The resulting outage cost your company significant revenue. Your CIO mandated a move to the cloud, but he is still concerned about catastrophic failures in a data center. What can you do to alleviate his concerns?

- **A.** Use an Amazon Virtual Private Cloud (Amazon VPC) with subnets.
- **B.** Purchase Reserved Instances for the processing services instances.
- **C.** Launch the compute for the processing services in a placement group.
- **D.** Distribute the architecture across multiple Availability Zones.


## Disaster Recovery, Backup & RTO/RPO


**Q55.** Disabling automated backups ______ disable the point-in-time recovery.

- **A.** will never
- **B.** if configured to can
- **C.** will


## Monitoring: CloudWatch, CloudTrail & Config


**Q56.** What service can automate EBS snapshots (backups) for restoring EBS volumes?

- **A.** CloudWatch alarm
- **B.** CloudWatch event
- **C.** Amazon Inspector
- **D.** SNS topic
- **E.** CloudTrail


## Elastic Beanstalk & Deployment


**Q57.** What deployment service enables tenants to replicate an existing AWS stack?

- **A.** CloudFormation
- **B.** RedShift
- **C.** Beanstalk
- **D.** EMR


# Section B - Multiple Response (select all that apply)


## RDS Multi-AZ, Read Replicas & Aurora


**Q58.** An online events registration system is hosted in AWS and uses ECS to host its front-end tier and a Multi-AZ RDS for its database tier, which also has a standby replica. What are the events that will make Amazon RDS automatically perform a failover to the standby replica? (Select TWO.) **(Select 2.)**

- **A.** Storage failure on primary
- **B.** Storage failure on secondary DB instance
- **C.** Loss of availability in primary Availability Zone
- **D.** Compute unit failure on secondary DB instance
- **E.** In the event of Read Replica failure


**Q59.** Which of the following techniques can you use to help you meet Recovery Point Objective (RPO) and Recovery Time Objective (RTO) requirements? **(Select 3.)**

- **A.** DB snapshots
- **B.** DB option groups
- **C.** Multi-AZ deployment
- **D.** Read replica


**Q60.** What are two characteristics of Amazon RDS? **(Select 2.)**

- **A.** Native load balancer
- **B.** Database managed service
- **C.** NoSQLqueries
- **D.** Database write replicas
- **E.** Automatic failover of read replica


**Q61.** What features are supported with Amazon RDS? **(Select 3.)**

- **A.** Horizontal scaling with multiple read replicas
- **B.** Replicate read replicas cross-region
- **C.** Automatic failover to master database instance
- **D.** Elastic load balancing RDS read replicas
- **E.** Application load balancer (ALB)


**Q62.** An RDS database is experiencing heavy read traffic. You are planning on creating read replicas. When using Amazon RDS with Read Replicas, which of the deployment options below are valid? **(Select 2.)**

- **A.** Within an Availability Zone
- **B.** Cross-Continent
- **C.** Cross-Availability Zone
- **D.** Cross-subnet


**Q63.** What statements correctly describe support for Microsoft SQLServer within Amazon VPC? **(Select 3.)**

- **A.** Read replica only
- **B.** S3 storage only
- **C.** Native load balancing
- **D.** EBS storage only
- **E.** Vertical scaling
- **F.** Read/write replica


**Q64.** Select two features available with Amazon RDS for MySQL? **(Select 2.)**

- **A.** Auto-Scaling
- **B.** Active read requests only
- **C.** Read requests to standby replicas
- **D.** Real-time database replication


## Auto Scaling & Elastic Load Balancing


**Q65.** The company you work for has a presence across multiple AWS regions. As part of disaster recovery planning you are formulating a solution to provide a regional DR capability for an application running on a fleet of Amazon EC2 instances that are provisioned by an Auto Scaling Group (ASG). The applications are stateless and read and write data to an S3 bucket. You would like to utilize the current AMI used by the ASG as it has some customizations made to it. What are the steps you might take to enable a regional DR capability for this application? **(Select 2.)**

- **A.** Modify the permissions of the AMI so it can be used across multiple regions
- **B.** Enable multi-AZ for the S3 bucket to enable synchronous replication to the DR region
- **C.** Copy the AMI to the DR region and create a new launch configuration for the ASG that uses the AMI
- **D.** Enable cross region replication on the S3 bucket and specify a destination bucket in the DR region


**Q66.** Elastic Load Balancing health checks may be _____________. **(Select 3.)**

- **A.** An Amazon Elastic Compute Cloud (Amazon EC2) instance status check
- **B.** A connection attempt
- **C.** A ping
- **D.** A page request
- **E.** A key pair verification


## S3 Security, Access & Durability


**Q67.** What are some reasons to enable cross-region replication on an Amazon Simple Storage Service (Amazon S3) bucket? **(Select 2.)**

- **A.** For compliance reasons, you need to store data in a location at least 300 miles away from the first region.
- **B.** You want a backup of your data in case of accidental deletion.
- **C.** You have a set of users or customers who can access the second bucket with lower latency.
- **D.** Your data needs at least five nines of durability.


**Q68.** A company has deployed Amazon RedShift for performing analytics on user data. When using Amazon RedShift, which of the following statements are correct in relation to availability and durability? **(Select 2.)**

- **A.** Single-node clusters support data replication
- **B.** RedShift always keeps five copies of your data
- **C.** RedShift always keeps three copies of your data
- **D.** RedShift provides continuous/incremental backups


## S3 Storage Classes & Lifecycle


**Q69.** Amazon Glacier is well-suited to data that is which of the following? **(Select 2.)**

- **A.** Is infrequently or rarely accessed
- **B.** Must be immediately available when needed
- **C.** Is available after a three- to five-hour restore period
- **D.** Is frequently erased within 30 days


## SQS, SNS & Decoupling


**Q70.** A company needs to monitor the read and write IOPs metrics for their AWS MySQL RDS instance and send real-time alerts to their operations team. Which AWS services can accomplish this? **(Select 2.)**

- **A.** Amazon CloudWatch
- **B.** Amazon Simple Email Service
- **C.** Amazon Simple Queue Service
- **D.** Amazon Route 53
- **E.** Amazon Simple Notification Service


## High Availability & Fault Tolerance


**Q71.** When using the following AWS services, which should be implemented in multiple Availability Zones for high availability solutions? **(Select 2.)**

- **A.** Amazon Simple Notification Service (SNS)
- **B.** Amazon Simple Storage Service (S3)
- **C.** Amazon Elastic Load Balancing
- **D.** Amazon Elastic Compute Cloud (EC2)
- **E.** Amazon DynamoDB


**Q72.** You have an application running in ap-southeast that requires six EC2 instances running at all times. With three Availability Zones available in that region (ap-southeast-2a, ap-southeast-2b, and ap-southeast-2c), which of the following deployments provides fault tolerance if any single Availability Zone in ap-southeast-2 becomes unavailable? **(Select 2.)**

- **A.** 3 EC2 instances in ap-southeast-2a, 3 EC2 instances in ap-southeast-2b, no EC2 instances in ap-southeast-2c
- **B.** 6 EC2 instances in ap-southeast-2a, 6 EC2 instances in ap-southeast-2b, no EC2 instances in ap-southeast-2c
- **C.** 3 EC2 instances in ap-southeast-2a, 3 EC2 instances in ap-southeast-2b, 3 EC2 instances in ap-southeast-2c
- **D.** 2 EC2 instances in ap-southeast-2a, 2 EC2 instances in ap-southeast-2b, 2 EC2 instances in ap-southeast-2c


**Q73.** What are two features that correctly describe Availability Zone (AZ) architecture? **(Select 2.)**

- **A.** Direct Connect supports Layer 2 connectivity to region
- **B.** Multiple AZ per region
- **C.** Multiple regions per AZ
- **D.** Interconnected with private WAN links
- **E.** Data auto-replicated between zones in different regions
- **F.** Interconnected with public WAN links


**Q74.** What are three advantages of standby replica in a Multi-AZ RDS deployment? **(Select 3.)**

- **A.** Fault tolerance
- **B.** Vertical scaling
- **C.** Horizontal scaling
- **D.** Eliminate I/O freezes
- **E.** Data redundancy


**Q75.** What are three primary characteristics of DynamoDB? **(Select 3.)**

- **A.** Less scalable than RDS
- **B.** Replication to three Availability Zones
- **C.** Store metadata for S3 objects
- **D.** Static content
- **E.** High read/write throughput


**Q76.** Which of the following are features of Amazon Elastic Block Store (Amazon EBS)? **(Select 2.)**

- **A.** Data stored on Amazon EBS is automatically replicated within an Availability Zone.
- **B.** Amazon EBS data is automatically backed up to tape.
- **C.** Amazon EBS volumes can be encrypted transparently to workloads on the attached instance.
- **D.** Data on an Amazon EBS volume is lost when the attached instance is stopped.


## Route 53 & DNS Routing


**Q77.** You are putting together a design for a web-facing application. The application will be run on EC2 instances behind ELBs in multiple regions in an active/passive configuration. The website address the application runs on is digitalcloud.guru. You will be using Route 53 to perform DNS resolution for the application. How would you configure Route 53 in this scenario based on AWS best practices? **(Select 2.)**

- **A.** Use a Failover Routing Policy
- **B.** Connect the ELBs using Alias records
- **C.** Connect the ELBs using CNAME records
- **D.** Use a Weighted Routing Policy


**Q78.** How is DNS Route 53 configured for Multi-Site fault tolerance? **(Select 2.)**

- **A.** Health checks
- **B.** Weighted records (non-zero)
- **C.** Alias records
- **D.** IP address
- **E.** Zero weighted records


**Q79.** How is Route 53 configured for Warm Standby fault tolerance? **(Select 2.)**

- **A.** Automated health checks
- **B.** Path-based routing
- **C.** Alias records
- **D.** Failover records


## EBS Volumes & Snapshots


**Q80.** What are three primary differences between S3 vs EBS? **(Select 3.)**

- **A.** EBS is directly assigned to a tenant VPC EC2 instance
- **B.** EBS and S3 are based on block level storage
- **C.** S3 is a multi-purpose public internet-based storage
- **D.** EBS and S3 use buckets to manage files
- **E.** EBS and S3 provide persistent storage
- **F.** EBS snapshots are typically stored on S3 buckets


## EC2 Instances, AMIs & Placement


**Q81.** How do you launch an EC2 instance after it is terminated? **(Select 2.)**

- **A.** Reboot instance from CLI
- **B.** Launch a new instance using the same AMI
- **C.** Contact AWS support to reset
- **D.** Reboot instance from management console
- **E.** Launch a new instance from a Snapshot


## Encryption & AWS KMS


**Q82.** A large quantity of data that is rarely accessed is being archived onto Amazon Glacier. Your CIO wants to understand the resilience of the service. Which of the statements below is correct about Amazon Glacier storage? **(Select 2.)**

- **A.** Data is replicated globally
- **B.** Data is resilient in the event of one entire region destruction
- **C.** Provides 99.999999999% durability of archives
- **D.** Data is resilient in the event of one entire Availability Zone destruction


## Disaster Recovery, Backup & RTO/RPO


**Q83.** What is the difference between Warm Standby and Multi-Site fault tolerance? **(Select 2.)**

- **A.** Multi-Site provides active/active load balancing
- **B.** DNS Route 53 is not required for Warm Standby
- **C.** Multi-Site provides active/standby load balancing
- **D.** Multi-Site enables lower RTO and most recent RPO
- **E.** Warm Standby enables lower RTO and most recent RPO


## ElastiCache & Caching Strategies


**Q84.** What are three primary reasons for deploying ElastiCache? **(Select 3.)**

- **A.** Low latency
- **B.** Durability
- **C.** Data security
- **D.** Replication with Redis
- **E.** Managed service


---


# Answer Key & Explanations


**Q1. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
The failover mechanism automatically changes the Domain Name System (DNS) record of the DB instance to point to the standby DB instance. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html

**Q2. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q3. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
You can force a failover from one Availability Zone to another by rebooting the primary instance in the AWS Management Console. This is often how people test a failover in the real world. There is no need to create a support case.

**Q4. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
If you create multiple read replicas in parallel from the same source DB instance, Amazon RDS takes only one snapshot at the start of the first create action.

**Q5. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
RDS Read replicas are used for read heavy DBs and replication is asynchronous. Read replicas are for workload sharing and offloading. Read replicas can be in another region (uses asynchronous replication) RDS with Multi-AZ is within a region only DynamoDB with Global Tables and Cross Region Replication is a multi-master database configuration. The solution does not ask for multi-region resilience or a multi-master database. The requirement is simply to serve read traffic from the other regions EC2 instances with EBS replication is not a suitable solution. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

**Q6. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not B:* Search Results Featured snippet from the web Amazon RDS allows you to gain visibility into how far a read replica has fallen behind its source DB instance. The number of seconds that the read replica is behind the master is published as an Amazon CloudWatch metric ("Replica Lag") available via the AWS Management Console or Amazon CloudWatch APIs. Refer: https://acloud.guru/forums/aws-certified-sysops-administrator- associate/discussion/-KYSMGj7iTpg-gmqGLDE/what-is-replica- lag#:~:text=Amazon%20RDS%20allows%20you%20to,Console%20or%20Amazon%20CloudWatch%20APIs.

**Q7. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon RDS read replicas provide enhanced performance and durability for Amazon RDS instances. This replication feature makes it easy to scale out elastically beyond the capacity constraints of a single Amazon RDS instance for read-heavy database workloads. You can create one or more replicas of a given source Amazon RDS instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput.

**Q8. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
In this scenario, the best idea is to use read replicas to scale out the database and thus maximize read performance. When using Multi-AZ, the secondary database is not accessible and all reads and writes must go to the primary or any read replicas.

**Q9. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Monitor the environment while Amazon RDS attempts to recover automatically. AWS will update the DB endpoint to point to the secondary instance automatically.

**Q10. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q11. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
You are not charged for the data transfer incurred in replicating data between your primary and standby. Internet data transfer in and out of your DB instance is charged the same as with a standard deployment. Refer: https://aws.amazon.com/rds/faqs/

**Q12. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q13. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
As the client does not need to manage the underlying operating system and they have a limited budget for staff, they should use a managed service such as RDS. Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it which enables the required resilience across multiple locations With EC2 you have full control at the operating system layer (not required) and can install your own database. However, you would then need to manage the entire stack and therefore staff costs would increase so this is not the best solution. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/ https://digitalcloud.training/certification-training/aws-solutions- architect-associate/compute/amazon-ec2/ https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

**Q14. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Cross-region replication allows you to replicate across regions: - Amazon DynamoDB global tables provides a fully managed solution for deploying a multi-region, multi-master database - When you create a global table, you specify the AWS regions where you want the table to be available - DynamoDB performs all of the necessary tasks to create identical tables in these regions, and propagate ongoing data changes to all of them RDS with Multi-AZ is not multi-master (only one DB can be written to at a time), and does not span regions S3 is an object store not a multi- master database There is no such thing as EBS replication. You could build your own database stack on EC2 with DB-level replication but that is not what is presented in the answer. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon- dynamodb/

**Q15. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
To ensure failover capabilities, consider using a secondary private IPv4 for incoming traffic on a network interface. In the event of an instance failure, you can move the interface and/or secondary private IPv4 address to a standby instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/scenarios-enis.html

**Q16. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q17. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags that you've assigned to it. This topic describes tags and shows you how to create them. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html

**Q18. C**  
_S3 Security, Access & Durability_  
Data is automatically replicated within a region. Replication to other regions and versioning are optional. Amazon S3 data is not backed up to tape.

**Q19. C**  
_S3 Security, Access & Durability_  
Amazon S3 scales automatically, but for request rates over 100 GETS per second, it helps to make sure there is some randomness in the key space. Replication and logging will not affect performance or scalability. Using sequential key names could have a negative effect on performance or scalability.

**Q20. A**  
_Auto Scaling & Elastic Load Balancing_  
From split-horizon DNS to customer domain-based DNS records for AWS PrivateLink endpoints, enable varying degrees of traffic rerouting and high availability with ownership/management of the DNS infrastructure. Any implementation must consider a trade-off between service availability, changes to the client application, and management of DNS infrastructure. Refer: https://aws.amazon.com/blogs/apn/reviewing-dns-mechanisms-for-routing- traffic-and-enabling-failover-for-aws-privatelink-deployments/

**Q21. C**  
_IAM Roles, Policies & Permissions_  
To start using IAM, you must subscribe to at least one of the AWS services that is integrated with IAM. You then can create and manage users, groups, and permissions via IAM APIs, the AWS CLI, or the IAM console, which gives you a point-and-click, web-based interface. You can also use the visual editor to create policies. Refer: https://aws.amazon.com/iam/faqs/

**Q22. C**  
_SQS, SNS & Decoupling_  
Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages waiting to be processed. SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers. SQS is used for distributed/decoupled applications and can be used with RedShift, DynamoDB, EC2, ECS, RDS, S3 and Lambda SQS cannot be used for providing fault tolerance for S3 as messages can only be stored in the queue for a maximum amount of time Simple Workflow Service (SWF) is used for co-ordination of work items between different human and non-human workers Simple Notification Service (SNS) can be used for sending email notifications when certain events happen References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-integration/amazon-sqs/

**Q23. B**  
_EBS Volumes & Snapshots_  
For a production application that requires fast and consistent I/O performance, we recommend Provisioned IOPS (input/output operations per second) storage. Provisioned IOPS storage is a storage type that delivers predictable performance, and consistently low latency. Provisioned IOPS storage is optimized for online transaction processing (OLTP) workloads that have consistent performance requirements. Provisioned IOPS helps performance tuning of these workloads. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html

**Q24. A**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q25. B**  
_EBS Volumes & Snapshots_  
The easiest and recommended option is to create an AMI (image) from the instance and launch an instance from the AMI in the other AZ. AMIs are backed by snapshots which in turn are backed by S3 so the data is available from any AZ within the region You can take a snapshot, launch an instance in the destination AZ. Stop the instance, detach its root volume, create a volume from the snapshot you took and attach it to the instance. However, this is not the best option There痴 no way to move an EC2 instance from the management console You cannot perform a copy operation to move the instance References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/ https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/

**Q26. A**  
_EBS Volumes & Snapshots_  
During snapshot creation, the snapshots are managed together. If one of the snapshots in the volume set fails, the other snapshots are moved to error status for the volume set. You can monitor the progress of your snapshots using CloudWatch Events. After the snapshot creation process completes, CloudWatch generates an event that contains the status and all of the relevant snapshots details for the affected instance. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html

**Q27. D**  
_EBS Volumes & Snapshots_  
You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html#:~:text=You%20can%20back%20up%20the,most%20recent%20snapshot%20are%20saved.

**Q28. A**  
_EBS Volumes & Snapshots_  
When you create an Amazon EBS volume in an Availability Zone, it is automatically replicated within that Availability Zone to prevent data loss due to failure of any single hardware component. An EBS Snapshot creates a copy of an EBS volume to Amazon S3 so that copies of the volume can reside in different Availability Zones within a region.

**Q29. A**  
_EBS Volumes & Snapshots_  
An Amazon Resource Name (ARN) is a file naming convention used to identify a particular resource in the Amazon Web Services (AWS) public cloud. ARNs, which are specific to AWS, help an administrator track and use AWS items and policies across AWS products and API calls.

**Q30. A**  
_EBS Volumes & Snapshots_  
The volume is created immediately but the data is loaded lazily. This means that the volume can be accessed upon creation, and if the data being requested has not yet been restored, it will be restored upon first request.

**Q31. C**  
_EBS Volumes & Snapshots_  
There is no delay in processing when commencing a snapshot.

**Q32. B**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q33. D**  
_EBS Volumes & Snapshots_  
DB Snapshots can be used to restore a complete copy of the database at a specific point in time. Individual tables cannot be extracted from a snapshot.

**Q34. C**  
_EBS Volumes & Snapshots_  
Refer: https://docs.aws.amazon.com/cli/latest/reference/ec2/create-snapshot.html

**Q35. C**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q36. C**  
_High Availability & Fault Tolerance_  
Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it. This provides a DR solution as if the AZ in which the primary DB resides fails, multi-AZ will automatically fail over to the replica instance with minimal downtime Read replicas are used for read heavy DBs and replication is asynchronous. Read replicas do not provide HA/DR as you cannot fail over to a read replica. They are used purely for offloading read requests from the primary DB Taking a snapshot of the database is useful for being able to recover from a failure so you can restore the database. However, this does not prevent an outage from happening as there will be significant downtime while you try and restore the snapshot to a new DB instance in another AZ Increasing the DB instance size will not provide any benefits to enabling high availability or fault tolerance, it will only serve to improve the performance of the DB. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/database/amazon-rds/

**Q37. C**  
_High Availability & Fault Tolerance_  
An Availability Zone is a distinct location within a region that is insulated from failures in other Availability Zones and provides inexpensive, low-latency network connectivity to other Availability Zones in the same region. Replication areas, geographic districts, and compute centers are not terms used to describe AWS data center locations.

**Q38. D**  
_High Availability & Fault Tolerance_  
Simple scaling maintains a current number of instances, you can manually change the ASGs min/desired/max and attach/detach instances. Auto Scaling will try to distribute EC2 instances evenly across AZs In this scenario you must have a minimum of 12 instances running in the event of an AZ failure, therefore with 18 instances across 3 AZs if one AZ fails you still have enough instances ELBs can be Internet-facing or internal-only. Remember that internet-facing ELBs have public IPs, whereas internal-only ELBs have private IPs have public IPs. Therefore, you must have 2 ELBs, one for the web layer and one for the app layer. Otherwise the web layer would have to hairpin the traffic back to the public IP of the ELB rather than forwarding it to the internal ELB and this is not a supported configuration. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/compute/aws-auto-scaling/ https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/elastic-load-balancing/

**Q39. C**  
_High Availability & Fault Tolerance_  
Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. Refer: https://aws.amazon.com/dynamodb/

**Q40. B**  
_High Availability & Fault Tolerance_  
Auto Scaling will provide high availability across three Availability Zones with three Amazon EC2 instances in each and keep capacity above the required minimum capacity, even in the event of an entire Availability Zone becoming unavailable.

**Q41. C**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q42. A**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q43. C**  
_High Availability & Fault Tolerance_  
Distributing applications across multiple Availability Zones provides the ability to remain resilient in the face of most failure modes, including natural disasters or system failures.

**Q44. C**  
_High Availability & Fault Tolerance_  
An Availability Zone consists of multiple discrete data centers, each with their own redundant power and networking/connectivity, therefore answer is correct.

**Q45. B**  
_High Availability & Fault Tolerance_  
You create a cluster subnet group if you are provisioning your cluster in your virtual private cloud (VPC) A cluster subnet group allows you to specify a set of subnets in your VPC When provisioning a cluster you provide the subnet group and Amazon Redshift creates the cluster on one of the subnets in the group A DB Subnet Group is used by RDS A Subnet Group is used by ElastiCache Availability Zones are part of the AWS global infrastructure, subnets reside within AZs but in RedShift you provision the cluster into Cluster Subnet Groups. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-redshift/ https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html

**Q46. B**  
_High Availability & Fault Tolerance_  
Moving an EC2 Instance to a Different Availability Zone/Region 1. Shutdown / stop the instance. 2. Right-click the instance and select Create 3. Image to make an AMI from the instance. 4. Go to the AMI page, right-click on the new AMI and select Launch Instance. 5. In the new instance settings, choose a specific (different) availability zone. Refer: https://d1.awsstatic.com/whitepapers/AWS_Migrate_Resources_To_New_Region.pdf

**Q47. C**  
_High Availability & Fault Tolerance_  
You can attach an available EBS volume to one or more of your instances that is in the same Availability Zone as the volume. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html

**Q48. A**  
_Route 53 & DNS Routing_  
Failover-based routing would best achieve this objective.

**Q49. B**  
_Route 53 & DNS Routing_  
Weighted routing would best achieve this objective because it allows you to specify which percentage of traffic is directed to each endpoint.

**Q50. C**  
_Route 53 & DNS Routing_  
You should route your traffic based on where your end users are located. The best routing policy to achieve this is geolocation routing.

**Q51. B**  
_Route 53 & DNS Routing_  
Amazon Route 53 performs three main functions: domain registration, DNS service, and health checking.

**Q52. A**  
_Route 53 & DNS Routing_  
An alias resource record set can point to an ELB. You cannot create a CNAME record at the top node of a Domain Name Service (DNS) namespace, also known as the zone apex, as the case in this example. Alias resource record sets can save you time because Amazon Route 53 automatically recognizes changes in the resource record sets to which the alias resource record set refers.

**Q53. C**  
_Route 53 & DNS Routing_  
Refer: https://aws.amazon.com/route53/faqs/

**Q54. D**  
_EC2 Instances, AMIs & Placement_  
An Availability Zone consists of one or more physical data centers. Availability zones within a region provide inexpensive, low-latency network connectivity to other zones in the same region. This allows you to distribute your application across data centers. In the event of a catastrophic failure in a data center, the application will continue to handle requests.

**Q55. C**  
_Disaster Recovery, Backup & RTO/RPO_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q56. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
CloudWatch metrics are statistical data that you can use to view, analyze, and set alarms on the operational behavior of your volumes. You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion of snapshots taken to back up your Amazon EBS volumes. Automating snapshot management helps you to: Protect valuable data by enforcing a regular backup schedule. Retain backups as required by auditors or internal compliance. Reduce storage costs by deleting outdated backups. Combined with the monitoring features of Amazon CloudWatch Events and AWS CloudTrail, Amazon Data Lifecycle Manager provides a complete backup solution for EBS volumes at no additional cost. Refer:

**Q57. A**  
_Elastic Beanstalk & Deployment_  
AWS CloudFormation is a service that gives developers and businesses an easy way to create a collection of related AWS and third party resources and provision them in an orderly and predictable fashion. Refer: https://aws.amazon.com/cloudformation/faqs/

**Q58. A, C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon RDS provides high availability and failover support for DB instances using Multi-AZ deployments. Amazon RDS uses several different technologies to provide failover support. Multi-AZ deployments for Oracle, PostgreSQL, MySQL, and MariaDB DB instances use Amazon's failover technology. SQL Server DB instances use SQL Server Database Mirroring (DBM). In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups. Running a DB instance with high availability can enhance availability during planned system maintenance, and help protect your databases against DB instance failure and Availability Zone disruption. Amazon RDS detects and automatically recovers from the most common failure scenarios for Multi-AZ deployments so that you can resume database operations as quickly as possible without administrative intervention. The high-availability feature is not a scaling solution for read-only scenarios; you cannot use a standby replica to serve read traffic. To service read-only traffic, you should use a Read Replica. Amazon RDS automatically performs a failover in the event of any of the following: Loss of availability in primary Availability Zone Loss of network connectivity to primary Compute unit failure on primary Storage failure on primary

**Q59. A, C, D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
DB snapshots allow you to back up and recover your data, while read replicas and a Multi-AZ deployment allow you to replicate your data and reduce the time to failover.

**Q60. A, B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon RDS Features Lower administrative burden, performance, Storage, Scalability, Availability and durability, Automated backups, Security, Manageability, Cost-effectiveness. Refer: https://aws.amazon.com/rds/features/

**Q61. A, B, E**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q62. A, C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Read Replicas can be within an AZ, Cross-AZ and Cross-Region Read replicas are used for read heavy DBs and replication is asynchronous. Read replicas are for workload sharing and offloading Read replicas cannot be cross-continent, cross-subnet or cross-facility. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

**Q63. A, C, E**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q64. C, D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Refer: https://aws.amazon.com/rds/features/read-replicas/

**Q65. C, D**  
_Auto Scaling & Elastic Load Balancing_  
There are two parts to this solution. First you need to copy the S3 data to each region (as the instances are stateless), then you need to be able to deploy instances from an ASG using the same AMI in each regions. - CRR is an Amazon S3 feature that automatically replicates data across AWS Regions. With CRR, every object uploaded to an S3 bucket is automatically replicated to a destination bucket in a different AWS Region that you choose, this enables you to copy the existing data across to each region - AMIs of both Amazon EBS-backed AMIs and instance store-backed AMIs can be copied between regions. You can then use the copied AMI to create a new launch configuration (remember that you cannot modify an ASG launch configuration, you must create a new launch configuration) There's no such thing as Multi-AZ for an S3 bucket (it's an RDS concept) Changing permissions on an AMI doesn't make it usable from another region, the AMI needs to be present within each region to be used. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/ https://digitalcloud.training/certification-training/aws- solutions-architect-associate/compute/amazon-ebs/

**Q66. B, C, D**  
_Auto Scaling & Elastic Load Balancing_  
An Elastic Load Balancing health check may be a ping, a connection attempt, or a page that is checked

**Q67. A, C**  
_S3 Security, Access & Durability_  
Cross-region replication can help lower latency and satisfy compliance requirements on distance. Amazon S3 is designed for eleven nines durability for objects in a single region, so a second region does not significantly increase durability. Cross- region replication does not protect against accidental deletion.

**Q68. C, D**  
_S3 Security, Access & Durability_  
RedShift always keeps three copies of your data and provides continuous/incremental backups Corrections: Single-node clusters do not support data replication Manual backups are not automatically deleted when you delete a cluster References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/database/amazon-redshift/

**Q69. A, C**  
_S3 Storage Classes & Lifecycle_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q70. A, E**  
_SQS, SNS & Decoupling_  
Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications. Refer: https://aws.amazon.com/sns/ Amazon CloudWatch enables you to collect, access, and correlate this data on a single platform from across all your AWS resources, applications, and services that run on AWS and on-premises servers, helping you break down data silos so you can easily gain system-wide visibility and quickly resolve issues. Refer: https://aws.amazon.com/cloudwatch/

**Q71. C, D**  
_High Availability & Fault Tolerance_  
Amazon DynamoDB already replicates across AZs, Amazon Simple Notification Service (SNS) and Amazon Simple Storage Service (S3) are a Global Managed Service Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2's simple web service interface allows you to obtain and configure capacity with minimal friction. Refer: https://aws.amazon.com/ec2/

**Q72. B, C**  
_High Availability & Fault Tolerance_  
This is a simple mathematical problem. Take note that the question asks that 6 instances must be available in the event that ANY SINGLE AZ becomes unavailable. There are only 2 options that fulfil these criteria References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/compute/amazon-ec2/ https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content- delivery/amazon-vpc/

**Q73. B, D**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q74. A, D, E**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q75. B, C, E**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q76. A, C**  
_High Availability & Fault Tolerance_  
There are no tapes in the AWS infrastructure. Amazon EBS volumes persist when the instance is stopped. The data is automatically replicated within an Availability Zone. Amazon EBS volumes can be encrypted upon creation and used by an instance in the same manner as if they were not encrypted.

**Q77. A, B**  
_Route 53 & DNS Routing_  
The failover routing policy is used for active/passive configurations. Alias records can be used to map the domain apex (digitalcloud.training) to the Elastic Load Balancers. Weighted routing is not an active/passive routing policy. All records are active and the traffic is distributed according to the weighting You cannot use CNAME records for the domain apex record, you must use Alias records When using the failover routing policy with Alias records set Evaluate Target Health to “Yes?? and do not use health checks (set "Associate with Health Check" to "No") References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-route-53/

**Q78. A, B**  
_Route 53 & DNS Routing_  
Health checks: Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. Each health check that you create can monitor one of the following: The health of a specified resource, such as a web server. The status of other health checks. The status of an Amazon CloudWatch alarm. Additionally, with Amazon Route 53 Application Recovery Controller, you can set up routing control health checks with DNS failover records to manage traffic failover for your application. To learn more, see Amazon Route 53 Application Recovery Controller Developer Guide. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html Weighting fault-tolerant multi-record answers in Amazon Route 53: An Amazon Route 53 weighted record can only be associated with one record, meaning a combination of one name (for example, example.com) and one record type (for example, A). But it is often desirable to weight DNS responses that contain multiple records. For example, you might have eight Amazon EC2 instances or Elastic IP endpoints for a service. If the clients of that service support connection retries (as all common browsers do), then providing multiple IP addresses in DNS responses provides those clients with alternative endpoints in the event of the failure of any particular endpoint. You can even protect against the failure of an availability zone if you configure responses to contain a mix of IPs hosted in two or more availability zones. Multi-record answers are also useful when a large number of clients (for example, mobile web applications) share a small set of DNS caches. In this case, multi-record answers allow clients to direct requests to several endpoints even if they receive a common DNS response from the shared cache. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialWeightedFTMR.html

**Q79. A, D**  
_Route 53 & DNS Routing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q80. A, C, D**  
_EBS Volumes & Snapshots_  
EBS appears as a mountable volume while the S3 requires software to read and write data. EBS can accommodate a smaller amount of data than S3. EBS can only be used by one EC2 instance at a time while S3 can be used by multiple instances. S3 typically experiences write delays while EBS does not. Refer: http://www.differencebetween.net/technology/internet/difference-between-amazon-s3-and-amazon-ebs

**Q81. B, E**  
_EC2 Instances, AMIs & Placement_  
You can't connect to or start an instance after you've terminated it. However, you can launch additional instances using the same AMI. If you'd rather stop and start your instance, or hibernate it, see Stop and start your instance or Hibernate your Linux instance. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating- instances.html#:~:text=You%20can't%20connect%20to,or%20Hibernate%20your%20Linux%20instance.

**Q82. C, D**  
_Encryption & AWS KMS_  
Glacier is designed for durability of 99.999999999% of objects across multiple Availability Zones. Data is resilient in the event of one entire Availability Zone destruction. Glacier supports SSL for data in transit and encryption of data at rest. Glacier is extremely low cost and is ideal for long-term archival Data is not resilient to the failure of an entire region Data is not replicated globally There is no availability SLA with Glacier References: https://aws.amazon.com/s3/storage-classes/

**Q83. A, D**  
_Disaster Recovery, Backup & RTO/RPO_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q84. A, D, E**  
_ElastiCache & Caching Strategies_  
Amazon ElastiCache for Redis is a web service that makes it easy to deploy and run Redis protocol-compliant server nodes in the cloud. The service enables the management, monitoring and operation of a Redis node; creation, deletion and modification of the node can be carried out through the ElastiCache console, the command line interface or the web service APIs. Amazon ElastiCache for Redis supports Redis Master / Slave replication. Refer: https://aws.amazon.com/elasticache/redis/faqs/
