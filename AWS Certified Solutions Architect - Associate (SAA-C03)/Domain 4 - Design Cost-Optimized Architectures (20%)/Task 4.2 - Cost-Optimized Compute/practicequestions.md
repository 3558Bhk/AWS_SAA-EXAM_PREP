# Task 4.2 - Cost-Optimized Compute - Practice Questions

> **Domain 4 - Design Cost-Optimized Architectures (20%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **12 multiple-choice (single answer)** followed by **3 multiple-response (select 2+)**. Total **15**.


**Topic order in this file:** RDS Multi-AZ, Read Replicas & Aurora → EC2 Pricing: Spot, RI & Savings Plans → High Availability & Fault Tolerance → AWS Organizations & Multi-Account → Monitoring: CloudWatch, CloudTrail & Config → Cost Management & Optimization Tools → EC2 Instances, AMIs & Placement


---


# Section A - Multiple Choice (one correct answer)


## RDS Multi-AZ, Read Replicas & Aurora


**Q1.** Changes to the backup window take effect ______.

- **A.** from the next billing cycle
- **B.** after 30 minutes
- **C.** immediately
- **D.** after 24 hours


## EC2 Pricing: Spot, RI & Savings Plans


**Q2.** You need to run a production process that will use several EC2 instances and run constantly on an ongoing basis. The process cannot be interrupted or restarted without issue. Which EC2 pricing model would be best for this workload?

- **A.** Spot instances
- **B.** Flexible instances
- **C.** On-demand instances
- **D.** Reserved instances


**Q3.** Your order-processing application processes orders extracted from a queue with two Reserved Instances processing 10 orders/minute. If an order fails during processing, then it is returned to the queue without penalty. Due to a weekend sale, the queues have several hundred orders backed up. While the backup is not catastrophic, you would like to drain it so that customers get their confirmation emails faster. What is a cost-effective way to drain the queue for orders?

- **A.** Create more queues.
- **B.** Deploy additional On-Demand Instances to assist in processing the orders.
- **C.** Deploy additional Reserved Instances to assist in processing the orders.
- **D.** Deploy additional Spot Instances to assist in processing the orders.


**Q4.** You have a distributed application that periodically processes large volumes of data across multiple Amazon EC2 Instances. The application is designed to recover gracefully from Amazon EC2 instance failures. You are required to accomplish this task in the most costeffective way. Which of the following will meet your requirements?

- **A.** Spot Instances
- **B.** Dedicated instances
- **C.** Reserved instances
- **D.** On-Demand instances


**Q5.** Your web application needs four instances to support steady traffic nearly all of the time. On the last day of each month, the traffic triples. What is a cost-effective way to handle this traffic pattern?

- **A.** Run four On-Demand Instances constantly, then add eight Reserved Instances on the last day of each month
- **B.** Run four Reserved Instances constantly, then add eight On-Demand Instances on the last day of each month.
- **C.** Run four On-Demand Instances constantly, then add eight more On-Demand Instances on the last day of each month.
- **D.** Run 12 Reserved Instances all of the time.


**Q6.** A development team needs to run up a few lab servers on a weekend for a new project. The servers will need to run uninterrupted for a few hours. Which EC2 pricing option would be most suitable?

- **A.** On-Demand
- **B.** Dedicated instances
- **C.** Spot
- **D.** Reserved


## High Availability & Fault Tolerance


**Q7.** The Trusted Advisor service provides insight regarding which four categories of an AWS account?

- **A.** Performance, cost optimization, access control, and connectivity
- **B.** Security, fault tolerance, high availability, and connectivity
- **C.** Performance, cost optimization, security, and fault tolerance
- **D.** Security, access control, high availability, and performance


## AWS Organizations & Multi-Account


**Q8.** When using consolidated billing there are two account types. What are they?

- **A.** Paying account and Linked account
- **B.** Main account and Sub account.
- **C.** Main account and Secondary account.
- **D.** Parent account and Child account


## Monitoring: CloudWatch, CloudTrail & Config


**Q9.** A customer wants to track access to their Amazon Simple Storage Service (S3) buckets and also use this information for their internal security and access audits. Which of the following will meet the Customer requirement?

- **A.** Enable AWS CloudTrail to audit all Amazon S3 bucket access.
- **B.** Enable the Requester Pays option to track access via AWS Billing
- **C.** Enable server access logging for all required Amazon S3 buckets.
- **D.** Enable Amazon S3 event notifications for Put and Post.


## Cost Management & Optimization Tools


**Q10.** You are an entrepreneur building a small company with some resources running on AWS. As you have limited funding you're extremely cost conscious. Which AWS service can send you alerts via email or SNS topic when you are forecast to exceed your funding capacity so you can take action?

- **A.** AWS Budgets
- **B.** Cost Explorer
- **C.** AWS Billing Dashboard
- **D.** Cost ; Usage reports


**Q11.** What feature is not available with AWS Trusted Advisor?

- **A.** Cost optimization
- **B.** Monitor application metrics
- **C.** Infrastructure best practices
- **D.** Vulnerability assessment


**Q12.** Your company’s IT management team is looking for an online tool to provide recommendations to save money, improve system availability and performance, and to help close security gaps. What can help the management team?

- **A.** Cloud-init
- **B.** Configuration Recorder
- **C.** AWS Trusted Advisor
- **D.** AWS Config


# Section B - Multiple Response (select all that apply)


## EC2 Instances, AMIs & Placement


**Q13.** A company is considering using EC2 Reserved Instances to reduce cost. The Architect involved is concerned about the potential limitations in flexibility of using RIs instead of On-Demand instances. Which of the following statements about RIs are useful to the Architect? **(Select 2.)**

- **A.** You cannot launch RIs using Auto Scaling Groups
- **B.** RIs can be sold on the Reserved Instance Marketplace
- **C.** There is a fee charged for any RI modifications
- **D.** You can use RIs in Placement Groups


**Q14.** Which of the following are characteristics of a reserved instance? **(Select 3.)**

- **A.** It can be used to lower Total Cost of Ownership (TCO) of a system
- **B.** It can be migrated across Availability Zones
- **C.** It is specific to an instance Type
- **D.** It is specific to an Amazon Machine Image (AMI)
- **E.** It can be applied to instances launched by Auto Scaling


**Q15.** You have purchased an m3.xlarge Linux Reserved instance in us-east-1a. In which ways can you modify this reservation? **(Select 2.)**

- **A.** Change it into two m3.large instances.
- **B.** Change it to a Windows instance.
- **C.** Move it to us-east-1b.
- **D.** Change it to an m4.xlarge.


---


# Answer Key & Explanations


**Q1. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Refer: https://aws.amazon.com/rds/faqs/

**Q2. D**  
_EC2 Pricing: Spot, RI & Savings Plans_  
In this scenario for a stable process that will run constantly on an ongoing basis RIs will be the most affordable solution RIs provide you with a significant discount (up to 75%) compared to On-Demand instance pricing. You have the flexibility to change families, OS types, and tenancies while benefitting from RI pricing when you use Convertible RIs Spot is more suited to short term jobs that can afford to be interrupted and offer the lowest price of all options On-demand is useful for short term ad-hoc requirements for which the job cannot afford to be interrupted and are typically more expensive than Spot instances There's no such thing as flexible instances References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ec2/ https://aws.amazon.com/ec2/pricing/reserved-instances/

**Q3. D**  
_EC2 Pricing: Spot, RI & Savings Plans_  
Spot Instances are a very cost-effective way to address temporary compute needs that are not urgent and are tolerant of interruption. That’s exactly the workload described here. Reserved Instances are inappropriate for temporary workloads. On-Demand Instances are good for temporary workloads, but don’t offer the cost savings of Spot Instances. Adding more queues is a non-responsive answer as it would not address the problem.

**Q4. A**  
_EC2 Pricing: Spot, RI & Savings Plans_  
A Spot Instance is an unused EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance is called a Spot price. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html

**Q5. B**  
_EC2 Pricing: Spot, RI & Savings Plans_  
Reserved Instances provide cost savings when you can commit to running instances full time, such as to handle the base traffic. On- Demand Instances provide the flexibility to handle traffic spikes, such as on the last day of the month

**Q6. A**  
_EC2 Pricing: Spot, RI & Savings Plans_  
Spot pricing may be the most economical option for a short duration over a weekend but you may have the instances terminated by AWS and there is a requirement that the servers run uninterrupted On-Demand pricing ensures that instances will not be terminated and is the most economical option Reserved pricing provides a reduced cost for a contracted period (1 or 3 years), and is not suitable for ad hoc requirements Dedicated instances run on hardware that's dedicated to a single customer and are more expensive than regular On-Demand instances References: https://aws.amazon.com/ec2/pricing/

**Q7. C**  
_High Availability & Fault Tolerance_  
AWS Trusted Advisor provides best practices in four categories: cost optimization, security, fault tolerance, and performance improvement. Refer: https://www.amazonaws.cn/en/support/trustedadvisor/#:~:text=AWS%20Trusted%20Advisor%20provides%20best,fault%20tolerance%2C%20and%20performance%20improvement.

**Q8. A**  
_AWS Organizations & Multi-Account_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q9. A**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Choose Properties. Choose Object-level logging. Choose an existing CloudTrail trail in the drop-down menu. The trail you select must be in the same AWS Region as your bucket, so the drop-down list contains only trails that are in the same Region as the bucket or trails that were created for all Regions. Refer: https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-cloudtrail- events.html#:~:text=Choose%20Properties.,were%20created%20for%20all%20Regions.

**Q10. A**  
_Cost Management & Optimization Tools_  
AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount. Budget alerts can be sent via email and/or Amazon Simple Notification Service (SNS) topic The AWS Cost Explorer is a free tool that allows you to view charts of your costs The AWS Billing Dashboard can send alerts when you're bill reaches certain thresholds but you must use AWS Budgets to created custom budgets that notify you when you are forecast to exceed a budget The AWS Cost and Usage report tracks your AWS usage and provides estimated charges associated with your AWS account but does not send alerts References: https://aws.amazon.com/aws-cost-management/aws- budgets/

**Q11. D**  
_Cost Management & Optimization Tools_  
AWS Trusted Advisor is now available in the AWS Management Console, with an enhanced dashboard and new customization features. AWS Trusted Advisor inspects your AWS environment and makes recommendations for saving money, improving system performance and reliability, or closing security gaps. Refer: https://aws.amazon.com/about-aws/whats-new/2014/07/23/introducing-aws-trusted-advisor-console

**Q12. C**  
_Cost Management & Optimization Tools_  
AWS Trusted Advisor inspects your AWS environment and makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps. AWS Trusted Advisor draws upon best practices learned from the aggregated operational history of serving hundreds of thousands of AWS customers.

**Q13. B, D**  
_EC2 Instances, AMIs & Placement_  
Capacity is reserved for a term of 1 or 3 years Standard = commitment of 1 or 3 years, charged whether it's on or off Scheduled = reserved for specific periods of time, accrue charges hourly, billed in monthly increments over the term (1 year) Scheduled RIs match your capacity reservation to a predictable recurring schedule RIs are used for steady state workloads and predictable usage Ideal for applications that need reserved capacity Upfront payments can reduce the hourly rate Can switch AZ within the same region Can change the instance size within the same instance type Instance type modifications are supported for Linux only Cannot change the instance size of Windows RIs Billed whether running or not Can sell reservations on the AWS marketplace Can be used in Auto Scaling Groups Can be used in Placement Groups. References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/compute/amazon-ec2/

**Q14. A, C, E**  
_EC2 Instances, AMIs & Placement_  
Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html A Reserved Instance has four instance attributes that determine its price - Instance type: For example, m4.large. This is composed of the instance family (for example, m4) and the instance size (for example, large). https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved- instances.html

**Q15. A, C**  
_EC2 Instances, AMIs & Placement_  
You can change the instance type only within the same instance type family, or you can change the Availability Zone. You cannot change the operating system nor the instance type family.
