# Task 3.2 - High-Performing and Elastic Compute - Practice Questions

> **Domain 3 - Design High-Performing Architectures (24%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **35 multiple-choice (single answer)** followed by **14 multiple-response (select 2+)**. Total **49**.


**Topic order in this file:** IAM Roles, Policies & Permissions → EC2 Instances, AMIs & Placement → Lambda & Serverless Compute → Encryption & AWS KMS → High Availability & Fault Tolerance → Route 53 & DNS Routing → Monitoring: CloudWatch, CloudTrail & Config → AWS Organizations & Multi-Account → Containers: ECS, EKS & Fargate → Cost Management & Optimization Tools → Secrets, Parameters & Credentials → General Design → Well-Architected & General Design → Elastic Beanstalk & Deployment → EBS Volumes & Snapshots


---


# Section A - Multiple Choice (one correct answer)


## IAM Roles, Policies & Permissions


**Q1.** Which of the following is the most recent version of the AWS digital signature calculation process?

- **A.** Signature Version 4
- **B.** Signature Version 1
- **C.** Signature Version 2
- **D.** Signature Version 3


## EC2 Instances, AMIs & Placement


**Q2.** A t2.medium EC2 instance type must be launched with what type of Amazon Machine Image (AMI)?

- **A.** An Amazon EBS-backed Hardware Virtual Machine AMI
- **B.** An Instance store Paravirtual AMI
- **C.** An Instance store Hardware Virtual Machine AMI
- **D.** An Amazon EBS-backed Paravirtual AMI


**Q3.** If you want to launch Amazon Elastic Compute Cloud (EC2) instances and assign each instance a predetermined private IP address you should ______________.

- **A.** Launch the instance from a private Amazon Machine Image (AMI).
- **B.** Launch the instances in the Amazon Virtual Private Cloud (VPC).
- **C.** Launch the instances in a Placement Group.
- **D.** Use standard EC2 instances since each instance gets a private Domain Name Service (DNS) already
- **E.** Assign a group of sequential Elastic IP address to the instances.


**Q4.** One of you clients has asked for assistance with a performance issue they are experiencing. The client has a fleet of EC2 instances behind an Elastic Load Balancer (ELB) that are a mixture of c4.2xlarge instance types and c5.large instances. The load on the CPUs on the c5.large instances has been very high, often hitting 100% utilization, whereas the c4.2xlarge instances have been performing well. The client has asked for advice on the most cost effective way to resolve the performance problems?

- **A.** Enable the weighted routing policy on the ELB and configure a higher weighting for the c4.2xlarge instances
- **B.** Change the configuration to use only c4.2xlarge instance types
- **C.** Add all of the instances into a Placement Group
- **D.** Add more c5.large instances to spread the load more evenly


**Q5.** Please select the Amazon EC2 resource which can be tagged.

- **A.** Amazon EBS snapshots
- **B.** Elastic IP addresses
- **C.** Key pairs
- **D.** Placement groups


**Q6.** 20. How are you billed for elastic IP addresses?

- **A.** Based on the data that flows through them
- **B.** Based on the instance type to which they are attaché
- **C.** Hourly when they are associated with an instance
- **D.** Hourly when they are not associated with an instance


**Q7.** How is capacity (compute, storage and network speed) managed and assigned to EC2 instances?

- **A.** IOPS
- **B.** Instance type
- **C.** Auto-Scaling
- **D.** AMI


**Q8.** Which Amazon Elastic Compute Cloud (Amazon EC2) feature ensures that your instances will not share a physical host with instances from any other AWS customer?

- **A.** Reserved Instances
- **B.** Dedicated Instances
- **C.** Placement groups
- **D.** Amazon Virtual Private Cloud (VPC)


**Q9.** By default what are ENIs that are automatically created and attached to instances using the EC2 console set to do when the attached instance terminates?

- **A.** Remain as is
- **B.** Terminate
- **C.** Pause
- **D.** Hibernate


**Q10.** What is the default maximum number of Elastic IP addresses assignable per Amazon AWS region?

- **A.** 5
- **B.** unlimited
- **C.** 1
- **D.** 100


**Q11.** How many Elastic IP by default in Amazon Account?

- **A.** 5 Elastic IP
- **B.** 0 Elastic IP
- **C.** 3 Elastic IP
- **D.** 1 Elastic IP


**Q12.** Which protocol is used by DNS when response data size exceeds 512 bytes?

- **A.** Transmission Control Protocol (TCP)
- **B.** User Datagram Protocol (UDP)
- **C.** File Transfer Protocol (FTP)
- **D.** Hyper Text Transfer Protocol (HTTP)


**Q13.** Which protocol is primarily used by DNS to serve requests?

- **A.** Hyper Text Transfer Protocol (HTTP)
- **B.** User Datagram Protocol (UDP)
- **C.** Transmission Control Protocol (TCP)
- **D.** File Transfer Protocol (FTP)


**Q14.** You recently made some configuration changes to an EC2 instance. You then launched a new EC2 instance from the same AMI however none of the settings were saved. What is the cause of this error?

- **A.** did not create new AMI
- **B.** did not reboot EC2 instance to enable changes
- **C.** did not save configuration changes to AMI
- **D.** did not save configuration changes to EC2 instance


## Lambda & Serverless Compute


**Q15.** To help you manage your Amazon EC2 instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of____________

- **A.** Tags
- **B.** Wildcards
- **C.** Functions
- **D.** Special filters


**Q16.** What is the difference between Stream-based and AWS Services when enabling Lambda?

- **A.** Streams maintains event source mapping in API
- **B.** Streams maintains event source mapping in Lambda
- **C.** Streams maintains event source mapping in EC2 instance
- **D.** Streams maintains event source mapping in event source
- **E.** Streams maintains event source mapping in notification


## Encryption & AWS KMS


**Q17.** Which Amazon Elastic Compute Cloud feature can you query from within the instance to access instance properties?

- **A.** Resource tags
- **B.** Instance user data
- **C.** Amazon Machine Image
- **D.** Instance metadata


## High Availability & Fault Tolerance


**Q18.** Which of the following describes a physical location around the world where AWS clusters data centers?

- **A.** Collection
- **B.** Region
- **C.** Fleet
- **D.** Endpoint


## Route 53 & DNS Routing


**Q19.** Which DNS name can only be resolved within Amazon EC2?

- **A.** External DNS name
- **B.** Internal DNS name
- **C.** Private DNS name
- **D.** Global DNS name


## Monitoring: CloudWatch, CloudTrail & Config


**Q20.** In the basic monitoring package for Amazon Elastic Compute Cloud (Amazon EC2), what Amazon CloudWatch metrics are available?

- **A.** Database visible metrics such as number of connections
- **B.** Hypervisor visible metrics such as CPU utilization
- **C.** Web server visible metrics such as number of failed transaction requests
- **D.** Operating system visible metrics such as memory utilization


**Q21.** Which of the following requires a custom CloudWatch metric to monitor?

- **A.** Data transfer of an EC2 instance
- **B.** CPU Utilization of an EC2 instance
- **C.** Disk usage activity of an EC2 instance
- **D.** Memory Utilization of an EC2 instance


**Q22.** What is the minimum time Interval for the data that Amazon CloudWatch receives and aggregates?

- **A.** Three minutes
- **B.** One second
- **C.** Five minutes
- **D.** One minute
- **E.** Five seconds


**Q23.** How long does Amazon CloudWatch keep metric data?

- **A.** 2 days
- **B.** 2 weeks
- **C.** 1 day
- **D.** 1 week


**Q24.** What does specifying the mapping /dev/sdc=none when launching an instance do?

- **A.** Prevents /dev/sdc from attaching to the instance.
- **B.** Set the value of /dev/sdc to 'zero'.
- **C.** Prevents /dev/sdc from creating the instance.
- **D.** Prevents /dev/sdc from deleting the instance.


## AWS Organizations & Multi-Account


**Q25.** What does Amazon EC2 provide?

- **A.** Computer Clusters in the Cloud.
- **B.** Virtual servers in the Cloud.
- **C.** Physical servers, remotely managed by the customer.
- **D.** A platform to run code (Java, PHP, Python), paying on an hourly basis.


**Q26.** Are you able to integrate a multi-factor token service with the AWS Platform?

- **A.** No, you cannot integrate multi-factor token devices with the AWS platform.
- **B.** Yes, you can integrate private multi-factor token devices to authenticate users to the AWS platform.
- **C.** Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.


## Containers: ECS, EKS & Fargate


**Q27.** A development team are creating a Continuous Integration and Continuous Delivery (CI/CD) toolchain on the AWS cloud. The team currently use Jenkins X and Kubernetes on-premise and are looking to utilize the same services in the AWS cloud. What AWS service can provide a managed container platform that is MOST similar to their current CI/CD toolchain?

- **A.** Amazon EKS
- **B.** AWS CodePipeline
- **C.** Amazon ECS
- **D.** AWS Lambda


**Q28.** What Amazon AWS service is available for container management?

- **A.** ECS
- **B.** Lambda
- **C.** Kinesis
- **D.** Docker


## Cost Management & Optimization Tools


**Q29.** What is the maximum key length of a tag?

- **A.** 512 Unicode characters
- **B.** 64 Unicode characters
- **C.** 256 Unicode characters
- **D.** 128 Unicode characters


## Secrets, Parameters & Credentials


**Q30.** You are planning to launch a fleet of EC2 instances running Linux. As part of the launch you would like to install some application development frameworks and custom software onto the instances. The installation will be initiated using some scripts you have written. What feature allows you to specify the scripts so you can install the software during the EC2 instance launch?

- **A.** User data
- **B.** Run command
- **C.** AWS Config
- **D.** Metadata


## General Design


**Q31.** If I want my instance to run on a single-tenant hardware, which value do I have to set the instance's tenancy attribute to?

- **A.** Dedicated
- **B.** Reserved
- **C.** One
- **D.** Isolated


**Q32.** When it comes to risk management, which of the following is true?

- **A.** AWS has developed a strategic business plan to identify any risks and has implemented controls to mitigate or manage those risks. Customers should also develop and maintain their own risk management plans to ensure they are compliant with any relevant controls and certifications
- **B.** AWS has developed a strategic business plan to identify any risks and implemented controls to mitigate or manage those risks. Customers do not need to develop and maintain their own risk management plans.
- **C.** AWS does not develop a strategic business plan; risk management and mitigation is entirely the responsibility of the customer.
- **D.** Neither AWS nor the customer needs to worry about risk management, so no plan is needed from either party.


## Well-Architected & General Design


**Q33.** Which of the following statements is true when it comes to the AWS shared responsibility model?

- **A.** The shared responsibility model is only applicable for customers who want to be compliant with SOC 1 Type II.
- **B.** The shared responsibility model is not just limited to security considerations; it also extends to IT controls.
- **C.** The shared responsibility model is limited to security considerations only; it does not extend to IT controls.
- **D.** The shared responsibility model is only applicable for customers who want to be compliant with ISO 27001.


**Q34.** Which of the following is the name of the security model employed by AWS with its customers?

- **A.** The secret key responsibility model
- **B.** The shared responsibility model
- **C.** The shared secret model
- **D.** The shared secret key model


## Elastic Beanstalk & Deployment


**Q35.** What is the deployment term for an environment that extends an existing on-premises infrastructure into the cloud to connect cloud resources to internal systems?

- **A.** On-premises deployment
- **B.** Scatter deployment
- **C.** Hybrid deployment
- **D.** All-in deployment


# Section B - Multiple Response (select all that apply)


## EC2 Instances, AMIs & Placement


**Q36.** What three attributes are used to define a launch configuration template for an Auto-Scaling group? **(Select 3.)**

- **A.** Instance type
- **B.** Private IP address
- **C.** Elastic IP
- **D.** AMI
- **E.** Security group


**Q37.** Select two difference between HVM and PV virtualization types? **(Select 2.)**

- **A.** HVM supports all current generation instance types
- **B.** HVM doesn’t support current generation instance types
- **C.** HVM is similar to bare metal hypervisor architecture
- **D.** HVM doesn’t support enhanced networking
- **E.** PV provides better performance than HVM for most instance types


**Q38.** What three characteristics or limitations differentiate EC2 instance types? **(Select 3.)**

- **A.** EBS volume only
- **B.** VPC only
- **C.** AWS service selected
- **D.** Virtualization type
- **E.** Application type


**Q39.** Which of the following must be specified when launching a new Amazon Elastic Compute Cloud (Amazon EC2) Windows instance? **(Select 2.)**

- **A.** Amazon EC2 instance type
- **B.** Password for the administrator account
- **C.** The Amazon EC2 instance ID
- **D.** Amazon Machine Image (AMI)


**Q40.** What are two advantages of Elastic IP (EIP) over AWS public IPv4 addresses? **(Select 2.)**

- **A.** EIP is persistent
- **B.** EIP is dynamic
- **C.** EIP is private
- **D.** EIP can be reassigned
- **E.** EIP is public and private


**Q41.** What are two attributes that define an EC2 instance type? **(Select 2.)**

- **A.** vCPU
- **B.** EBS volume storage
- **C.** License type
- **D.** Auto-Scaling
- **E.** IP address


**Q42.** Which of the following can be used to address an Amazon Elastic Compute Cloud (Amazon EC2) instance over the web? **(Select 2.)**

- **A.** Elastic IP address
- **B.** Public DNS name
- **C.** Amazon EC2 instance ID
- **D.** Windows machine name


## EBS Volumes & Snapshots


**Q43.** Which of the following are true regarding encrypted Amazon Elastic Block Store (EBS) volumes? **(Select 2.)**

- **A.** Snapshots are automatically encrypted
- **B.** Existing volumes can be encrypted
- **C.** shared volumes can be encrypted
- **D.** Supported on all Amazon EBS volume types
- **E.** Available to all instance types


**Q44.** What statements are correct concerning DisableApiTermination attribute? **(Select 2.)**

- **A.** Termination protection is disabled by default for an EC2 instance
- **B.** Cannot enable termination protection for Spot instances
- **C.** Can enable termination protection for Spot instances
- **D.** DisableApiTermination attribute supported for EBS-backed instances only
- **E.** Termination protection is enabled by default for an EC2 instance


## Lambda & Serverless Compute


**Q45.** What three characteristics differentiate Lambda from traditional EC2 deployment or containerization? **(Select 3.)**

- **A.** Lambda is a code-based service
- **B.** Lambda supports only S3 and Glacier
- **C.** Tenant has ownership of EC2 instances
- **D.** Lambda is based on Kinesis scripts
- **E.** Lambda is serverless
- **F.** Tenant has no control of EC2 instances


## Monitoring: CloudWatch, CloudTrail & Config


**Q46.** A Solutions Architect is designing the system monitoring and deployment layers of a serverless application. The system monitoring layer will manage system visibility through recording logs and metrics and the deployment layer will deploy the application stack and manage workload changes through a release management process.The Architect needs to select the most appropriate AWS services for these functions. Which services and frameworks should be used for the system monitoring and deployment layers? **(Select 2.)**

- **A.** Use AWS Lambda to package, test, and deploy the serverless application stack
- **B.** Use Amazon CloudWatch for consolidating system and application logs and monitoring custom metrics
- **C.** Use AWS SAM to package, test, and deploy the serverless application stack
- **D.** Use AWS X-Ray to package, test, and deploy the serverless application stack


## Containers: ECS, EKS & Fargate


**Q47.** You have been tasked with building an ECS cluster using the EC2 launch type and need to ensure container instances can connect to the cluster. A colleague informed you that you must ensure the ECS container agent is installed on your EC2 instances. You have selected to use the Amazon ECS-optimized AMI. Which of the statements below are correct? **(Select 2.)**

- **A.** You can install the ECS container agent on any Amazon EC2 instance that supports the Amazon ECS specification
- **B.** The Amazon ECS container agent must be installed for all AMIs
- **C.** The Amazon ECS container agent is included in the Amazon ECS-optimized AMI
- **D.** The Amazon ECS container agent is installed on the AWS managed infrastructure used for tasks using the EC2 launch type so you don't need to do anything


**Q48.** How is versioning supported with Lambda? **(Select 2.)**

- **A.** Aliases
- **B.** ECS container
- **C.** Lambda native support
- **D.** Not supported
- **E.** Replication
- **F.** S3 versioning


## Elastic Beanstalk & Deployment


**Q49.** What are the advantages of Beanstalk? **(Select 2.)**

- **A.** Template-oriented deployment service
- **B.** Orchestration and deployment abstraction
- **C.** Does not support cloud containers
- **D.** Easiest solution for developers to deploy cloud applications


---


# Answer Key & Explanations


**Q1. A**  
_IAM Roles, Policies & Permissions_  
The Signature Version 4 signing process describes how to add authentication information to AWS requests. For security, most requests to AWS must be signed with an access key (Access Key ID [AKI] and Secret Access Key [SAK]). If you use the AWS Command Line Interface (AWS CLI) or one of the AWS Software Development Kits (SDKs), those tools automatically sign requests for you based on credentials that you specify when you configure the tools. However, if you make direct HTTP or HTTPS calls to AWS,

**Q2. A**  
_EC2 Instances, AMIs & Placement_  
Virtualization type: Choose whether instances launched from this AMI use paravirtual (PV) or hardware virtual machine (HVM) virtualization. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html

**Q3. B**  
_EC2 Instances, AMIs & Placement_  
If you want to launch Amazon Elastic Compute Cloud (EC2) Instances and assign each Instance a predetermined private IP address you should: 1. Assign a group or sequential Elastic IP address to the instances. 2. Launch the instances in a Placement Group. 3. Launch the instances in the Amazon virtual Private Cloud (VPC). Refer: https://aws.amazon.com/premiumsupport/knowledge-center/custom-private-primary-address-ec2/

**Q4. B**  
_EC2 Instances, AMIs & Placement_  
The 2xlarge instance type provides more CPUs. The best answer is to use this instance type for all instances A placement group helps provide low-latency connectivity between instances and would not help here The weighted routing policy is a Route 53 feature that would not assist in this situation References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

**Q5. D**  
_EC2 Instances, AMIs & Placement_  
To help categorize and manage your existing placement groups, you can tag them with custom metadata. For more information about how tags work, see Tagging your Amazon EC2 resources. When you tag a placement group, the instances that are launched into the placement group are not automatically tagged. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement- groups.html#:~:text=To%20help%20categorize%20and%20manage,group%20are%20not%20automatically%20tagged.

**Q6. D**  
_EC2 Instances, AMIs & Placement_  
There is a very small hourly charge for allocated elastic IP addresses that are not associated with an instance

**Q7. B**  
_EC2 Instances, AMIs & Placement_  
Amazon EC2 provides a wide selection of instance types optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications. Each instance type includes one or more instance sizes, allowing you to scale your resources to the requirements of your target workload. Refer: https://aws.amazon.com/ec2/instance-types/

**Q8. B**  
_EC2 Instances, AMIs & Placement_  
Dedicated Instances will not share hosts with other accounts

**Q9. B**  
_EC2 Instances, AMIs & Placement_  
You can set the termination behavior for a network interface that's attached to an instance. You can specify whether the network interface should be automatically deleted when you terminate the instance to which it's attached. In the Change Termination Behavior dialog box, select the Delete on termination check box if you want the network interface to be deleted when you terminate an instance. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html

**Q10. A**  
_EC2 Instances, AMIs & Placement_  
By default, all AWS accounts are limited to five (5) Elastic IP addresses per Region, because public (IPv4) internet addresses are a scarce public resource. Refer: https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses- eip.html#:~:text=Sending%20Limitations%20page.-,Elastic%20IP%20address%20limit,are%20a%20scarce%20public%20resource.

**Q11. A**  
_EC2 Instances, AMIs & Placement_  
By default, all AWS accounts are limited to five (5) Elastic IP addresses per Region, because public (IPv4) internet addresses are a scarce public resource. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html

**Q12. A**  
_EC2 Instances, AMIs & Placement_  
The TCP protocol is used by DNS server when the response data size exceeds 512 bytes or for tasks such as zone transfers.

**Q13. B**  
_EC2 Instances, AMIs & Placement_  
DNS primarily uses UDP to serve requests.

**Q14. A**  
_EC2 Instances, AMIs & Placement_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q15. A**  
_Lambda & Serverless Compute_  
To help you manage your instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of tags. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags that you've assigned to it. This topic describes tags and shows you how to create them. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html

**Q16. B**  
_Lambda & Serverless Compute_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q17. D**  
_Encryption & AWS KMS_  
Although you can only access instance metadata and user data from within the instance itself, the data is not protected by authentication or cryptographic methods. Anyone who has direct access to the instance, and potentially any software running on the instance, can view its metadata. Therefore, you should not store sensitive data, such as passwords or long-lived encryption keys, as user data. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

**Q18. B**  
_High Availability & Fault Tolerance_  
A region is a named set of AWS resources in the same geographical area. A region comprises at least two Availability Zones. Endpoint, Collection, and Fleet do not describe a physical location around the world where AWS clusters data centers.

**Q19. B**  
_Route 53 & DNS Routing_  
When you launch an instance, we allocate a primary private IPv4 address for the instance. Each instance is also given an internal DNS hostname that resolves to the primary private IPv4 address; for example, ip-10-251-50-12.ec2.internal. You can use the internal DNS hostname for communication between instances in the same VPC, but we can't resolve the internal DNS hostname outside of the VPC. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html

**Q20. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch metrics provide hypervisor visible metrics.

**Q21. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch is a web service that enables you to monitor, manage, and publish various metrics, as well as configure alarm actions based on data from metrics. You can define custom metrics for your own use, and Elastic Beanstalk will push those metrics to Amazon CloudWatch. Refer: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-cw.html

**Q22. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
The minimum resolution supported by CloudWatch is 1-second data points, which is a high-resolution metric, or you can store metrics at 1- minute granularity. Sometimes metrics are received by Cloudwatch at varying intervals, such as 3-minute or 5-minute intervals. If you do not specify that a metric is high resolution, by setting the StorageResolution field in the PutMetricData API request, then by default CloudWatch will aggregate and store the metrics at 1-minute resolution. Depending on the age of data requested, metrics will be available at the resolutions defined in the retention schedules above. For example, if you request for 1-minute data for a day from 10 days ago, you will receive the 1440 data points. However, if you request for 1-minute data from 5 months back, the UI will automatically change the granularity to 1-hour and the GetMetricStatistics API will not return any output. Refer: https://aws.amazon.com/cloudwatch/faqs/

**Q23. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch metric data is kept for 2 weeks.

**Q24. A**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q25. B**  
_AWS Organizations & Multi-Account_  
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2's simple web service interface allows you to obtain and configure capacity with minimal friction. Refer: https://aws.amazon.com/ec2/#:~:text=Amazon%20Elastic%20Compute%20Cloud%20(Amazon,configure%20capacity%20with%20minimal%20friction.

**Q26. C**  
_AWS Organizations & Multi-Account_  
Refer: https://aws.amazon.com/iam/faqs/#MFA_FAQs

**Q27. A**  
_Containers: ECS, EKS & Fargate_  
Amazon EKS is AWS’ managed Kubernetes offering, which enables you to focus on building applications, while letting AWS handle managing Kubernetes and the underlying cloud infrastructure Amazon Elastic Container Service (ECS) does not use Kubernetes so it is not the most similar product AWS Lambda is a serverless service that executes code as functions AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. It is not a container platform References: https://aws.amazon.com/eks/

**Q28. A**  
_Containers: ECS, EKS & Fargate_  
Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that provides the most secure, reliable and scalable way to run containerized applications. Refer: https://aws.amazon.com/containers/services/#:~:text=Amazon%20Elastic%20Container%20Service%20(Amazon,way%20to%20run%20containerized%20applications.

**Q29. D**  
_Cost Management & Optimization Tools_  
The tag key must be a minimum of 1 and a maximum of 128 Unicode characters in UTF-8. Refer: https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html

**Q30. A**  
_Secrets, Parameters & Credentials_  
When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to perform common automated configuration tasks and even run scripts after the instance starts. You can pass two types of user data to Amazon EC2: shell scripts and cloud- init directives User data is data that is supplied by the user at instance launch in the form of a script and is limited to 16KB User data and meta data are not encrypted. Instance metadata is available at http://169.254.169.254/latest/meta-data. The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or category names The AWS Systems Manager run command is used to manage the configuration of existing instances by using remotely executed commands. User data is better for specifying scripts to run at startup. References: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ec2/

**Q31. A**  
_General Design_  
Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single payer account. However, Dedicated Instances may share hardware with other instances from the same AWS account that are not Dedicated Instances. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html

**Q32. A**  
_General Design_  
AWS has developed a strategic business plan, and customers should also develop and maintain their own risk management plans, therefore answer is correct.

**Q33. B**  
_Well-Architected & General Design_  
The shared responsibility model can include IT controls, and it is not just limited to security considerations. Therefore, answer C is correct.

**Q34. B**  
_Well-Architected & General Design_  
The shared responsibility model is the name of the model employed by AWS with its customers.

**Q35. C**  
_Elastic Beanstalk & Deployment_  
A hybrid deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud. An all-in deployment refers to an environment that exclusively runs in the cloud. An on-premises deployment refers to an environment that runs exclusively in an organization’s data center.

**Q36. A, D, E**  
_EC2 Instances, AMIs & Placement_  
Keep the following considerations in mind when creating a launch template for use with an Auto Scaling group: Launch templates give you the flexibility of launching one type of instance, or a combination of instance types and On-Demand and Spot purchase options. For more information, see Auto Scaling Groups with Multiple Instance Types and Purchase Options. Launching instances with such a combination is not supported: If you specify a Spot Instance request in Additional Details In EC2-Classic If you configure a network type (VPC or EC2-Classic), subnet, and Availability Zone for your template, these settings are ignored in favor of what is specified in the Auto Scaling group. If you specify a network interface, you must configure the security group as part of the network interface, and not in the Security Groups section of the template. You cannot specify multiple network interfaces. You cannot assign specific private IP addresses. When an instance launches, a private address is allocated from the CIDR range of the subnet in which the instance is launched. For more information on specifying CIDR ranges for your VPC or subnet, see the Amazon VPC User Guide. To specify an existing network interface to use, its device index must be 0 (eth0). For this scenario, you must use the CLI or API to create the Auto Scaling group. When you create the group using the CLI create-auto-scaling-group command or API CreateAutoScalingGroup action, you must specify the Availability Zones parameter instead of the subnet (VPC zone identifier) parameter. You cannot use host placement affinity or target a specific host by choosing a host ID. Support for Dedicated Hosts (host tenancy) is only available if you specify a host resource group. For more information, see Host Resource Groups in the AWS License Manager User Guide. Note that each AMI based on a license configuration association can be mapped to only one host resource group at a time. Refer: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html

**Q37. A, C**  
_EC2 Instances, AMIs & Placement_  
Linux Amazon Machine Images use one of two types of virtualization: paravirtual (PV) or hardware virtual machine (HVM). The main differences between PV and HVM AMIs are the way in which they boot and whether they can take advantage of special hardware extensions (CPU, network, and storage) for better performance. Paravirtual guests traditionally performed better with storage and network operations than HVM guests because they could leverage special drivers for I/O that avoided the overhead of emulating network and disk hardware, whereas HVM guests had to translate these instructions to emulated hardware. Now PV drivers are available for HVM guests, so operating systems that cannot be ported to run in a paravirtualized environment can still see performance advantages in storage and network I/O by using them. With these PV on HVM drivers, HVM guests can get the same, or better, performance than paravirtual guests. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html#:~:text=Linux%20Amazon%20Machine%20Images%20use,and%20storage)%20for%20better%20perfo

**Q38. A, B, D**  
_EC2 Instances, AMIs & Placement_  
When you launch an instance, the instance type that you specify determines the hardware of the host computer used for your instance. Each instance type offers different compute, memory, and storage capabilities and are grouped in instance families based on these capabilities. Select an instance type based on the requirements of the application or software that you plan to run on your instance. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html

**Q39. A, D**  
_EC2 Instances, AMIs & Placement_  
The Amazon EC2 instance ID will be assigned by AWS as part of the launch process. The administrator password is assigned by AWS and encrypted via the public key. The instance type defines the virtual hardware and the AMI defines the initial software state. You must specify both upon launch.

**Q40. A, D**  
_EC2 Instances, AMIs & Placement_  
An Elastic IP address is a static, public IPv4 address designed for dynamic cloud computing. You can associate an Elastic IP address with any instance or network interface for any VPC in your account. With an Elastic IP address, you can mask the failure of an instance by rapidly remapping the address to another instance in your VPC. Note that the advantage of associating the Elastic IP address with the network interface instead of directly with the instance is that you can move all the attributes of the network interface from one instance to another in a single step. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html

**Q41. A, B**  
_EC2 Instances, AMIs & Placement_  
Refer: https://aws.amazon.com/ec2/instance-types/

**Q42. A, B**  
_EC2 Instances, AMIs & Placement_  
Neither the Windows machine name nor the Amazon EC2 instance ID can be resolved into an IP address to access the instance

**Q43. A, D**  
_EBS Volumes & Snapshots_  
This feature is supported on all Amazon EBS volume types (General Purpose (SSD), Provisioned IOPS (SSD), and Magnetic). You can access encrypted Amazon EBS volumes the same way you access existing volumes; encryption and decryption are handled transparently and they require no additional action from you, your Amazon EC2 instance, or your application. Snapshots of encrypted Amazon EBS volumes are automatically encrypted, and volumes that are created from encrypted Amazon EBS snapshots are also au

**Q44. A, B**  
_EBS Volumes & Snapshots_  
The DisableApiTermination attribute controls whether the instance can be terminated using the console, CLI, or API. By default, termination protection is disabled for your instance. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html

**Q45. A, E, F**  
_Lambda & Serverless Compute_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q46. B, C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
AWS Serverless Application Model (AWS SAM) is an extension of AWS CloudFormation that is used to package, test, and deploy serverless applications With Amazon CloudWatch, you can access system metrics on all the AWS services you use, consolidate system and application level logs, and create business key performance indicators (KPIs) as custom metrics for your specific needs AWS Lambda is used for executing your code as functions, it is not used for packaging, testing and deployment. AWS Lambda is used with AWS SAM AWS X-Ray lets you analyze and debug serverless applications by providing distributed tracing and service maps to easily identify performance bottlenecks by visualizing a request end-to-end References: https://docs.aws.amazon.com/lambda/latest/dg/serverless_app.html https://digitalcloud.training/certification-training/aws-solutions-architect- associate/management-tools/amazon-cloudwatch/

**Q47. A, C**  
_Containers: ECS, EKS & Fargate_  
The ECS container agent allows container instances to connect to the cluster nd runs on each infrastructure resource on an ECS cluster. The ECS container agent is included in the Amazon ECS optimized AMI and can also be installed on any EC2 instance that supports the ECS specification (only supported on EC2 instances). It is available for Linux and Windows The ECS container agent does not need to be installed for all AMIs as it is included in the Amazon ECS optimized AMI With the EC2 launch type the container agent is not installed on AWS managed infrastructure - however this is true for the Fargate launch type You can install the EC2 container agent on Windows instances References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/compute/amazon-ecs/

**Q48. A, C**  
_Containers: ECS, EKS & Fargate_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q49. B, D**  
_Elastic Beanstalk & Deployment_  
Refer: https://aws.amazon.com/elasticbeanstalk/
