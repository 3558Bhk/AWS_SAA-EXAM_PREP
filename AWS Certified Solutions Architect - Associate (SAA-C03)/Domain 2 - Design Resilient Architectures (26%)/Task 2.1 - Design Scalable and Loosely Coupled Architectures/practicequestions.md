# Task 2.1 - Design Scalable and Loosely Coupled Architectures - Practice Questions

> **Domain 2 - Design Resilient Architectures (26%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **60 multiple-choice (single answer)** followed by **32 multiple-response (select 2+)**. Total **92**.


**Topic order in this file:** Auto Scaling & Elastic Load Balancing → SQS, SNS & Decoupling → DynamoDB Design & Capacity → Route 53 & DNS Routing → CloudFront & Edge Delivery → Lambda & Serverless Compute → Monitoring: CloudWatch, CloudTrail & Config → ElastiCache & Caching Strategies → Hybrid Connectivity: Direct Connect & VPN → Elastic Beanstalk & Deployment → S3 Storage Classes & Lifecycle → High Availability & Fault Tolerance → EBS Volumes & Snapshots


---


# Section A - Multiple Choice (one correct answer)


## Auto Scaling & Elastic Load Balancing


**Q1.** Where are Elastic Load Balancer and Auto-Scaling groups deployed as a unified solution for horizontal scaling?

- **A.** Default VPC only
- **B.** Web server instances
- **C.** Database instances
- **D.** All instances


**Q2.** A cell phone company is running dynamic-content television commercials for a contest. They want their website to handle traffic spikes that come after a commercial airs. The website is interactive, offering personalized content to each visitor based on location, purchase history, and the current commercial airing. Which architecture will configure Auto Scaling to scale out to respond to spikes of demand, while minimizing costs during quiet periods?

- **A.** Create an Auto Scaling group large enough to handle peak traffic loads, and then stop some instances. Configure Auto Scaling to scale out when traffic increases using the stopped instances, so new capacity will come online quickly.
- **B.** Configure Auto Scaling to scale out as traffic increases. Configure the launch configuration to start new instances from a preconfigured Amazon Machine Image (AMI).
- **C.** Use Amazon CloudFront and Amazon Simple Storage Service (Amazon S3) to cache changing content, with the Auto Scaling group set as the origin. Configure Auto Scaling to have sufficient instances necessary to initially populate CloudFront and Amazon ElastiCache, and then scale in after the cache is fully populated.
- **D.** Set the minimum size of the Auto Scaling group so that it can handle high traffic volumes without needing to scale out.


**Q3.** You have decided to change the instance type for instances running in your application tier that is using Auto Scaling. In which area below would you change the instance type definition?

- **A.** Auto Scaling launch configuration
- **B.** Auto Scaling group
- **C.** Auto Scaling policy
- **D.** Auto Scaling tags


**Q4.** One of the applications you manage receives a high traffic loads between 7:30am and 9:30am daily. The application uses an Auto Scaling Group (ASG) to maintain 3 EC2 instances most of the time but during the peak period requires 6 EC2 instances. How can you configure ASG to perform a regular scale-out event at 7:30am and a scale-in event at 9:30am daily to account for the peak load?

- **A.** Use a Dynamic scaling policy
- **B.** Use a Scheduled scaling policy
- **C.** Use a Step scaling policy
- **D.** Use a Simple scaling policy


**Q5.** You are running an Auto Scaling Group (ASG) with an Elastic Load Balancer (ELB) and a fleet of EC2 instances. Health checks are configured on the ASG to use EC2 status checks The ELB has determined that an EC2 instance is unhealthy and has removed it from service. However, you noticed that the instance is still running and has not been terminated by the ASG. What would be an explanation for this?

- **A.** The ASG is waiting for the cooldown timer to expire before terminating the instance
- **B.** The health check grace period has not yet expired
- **C.** The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been determined to be unhealthy by the ELB and has been removed from service
- **D.** Connection draining is enabled and the ASG is waiting for in-flight requests to complete


**Q6.** What method detects when to replace an EC2 instance that is assigned to an Auto-Scaling group?

- **A.** dynamic path detection
- **B.** load balancing algorithm
- **C.** EC2 health check
- **D.** not currently supported
- **E.** health check
- **F.** Auto-Scaling


**Q7.** You work for a company that produces TV commercials. You are planning to run an advertising campaign during a major political event that will be watched by millions of people over several days. It is expected that your website will receive large bursts of traffic following commercial breaks. You have performed an analysis and determined that you will need up to 150 EC2 web instances to process the traffic which is within the client's budgetYou need to ensure you deliver a high quality and consistent user experience whilst not exceeding the client's budget. How would you design a highly available and elastic solution?

- **A.** Create an Auto Scaling Group across multiple AZs with a desired capacity of 150 EC2 instances. Launch an Application Load Balancer and specify the same AZs as the ASG and pre-warm the ALB by contacting AWS prior to the event
- **B.** Create an Auto Scaling Group across multiple AZs with a desired capacity of 150 EC2 instances. Launch an Application Load Balancer and specify the same AZs as the ASG
- **C.** Create an Auto Scaling Group across multiple AZs with a maximum capacity of 150 EC2 instances. Launch an Application Load Balancer and specify the same AZs as the ASG and pre-warm the ALB by contacting AWS prior to the event
- **D.** Create an Auto Scaling Group across multiple AZs with a maximum capacity of 150 EC2 instances. Launch an Application Load Balancer and specify the same AZs as the ASG


**Q8.** Which of the following are the minimum required elements to create an Auto Scaling launch configuration?

- **A.** Launch configuration name, AMI, instance type, key pair, and security group
- **B.** Launch configuration name, Amazon Machine Image (AMI), and instance type
- **C.** Launch configuration name, AMI, instance type, and key pair
- **D.** Launch configuration name, AMI, instance type, key pair, security group, and block device mapping


**Q9.** You have a content management system running on an Amazon EC2 instance that is approaching 100% CPU utilization. Which option will reduce load on the Amazon EC2instance?

- **A.** Create a load balancer, and register the Amazon EC2 instance with it
- **B.** Create a launch configuration from the instance using the CreateLaunchConfiguration action
- **C.** Create a CloudFront distribution, and configure the Amazon EC2 instance as the origin
- **D.** Create an Auto Scaling group from the instance using the CreateAutoScalingGroup action


**Q10.** What feature enables CloudWatch to manage capacity dynamically for EC2 instances?

- **A.** Auto-Scaling
- **B.** Replication lag
- **C.** Elastic Load Balancer
- **D.** Vertical scaling


**Q11.** The company you work for is currently transitioning their infrastructure and applications into the AWS cloud. You are planning to deploy an Elastic Load Balancer (ELB) that distributes traffic for a web application running on EC2 instances. You still have some application servers running on-premise and you would like to distribute application traffic across both your AWS and on-premises resources. How can this be achieved?

- **A.** Provision an IPSec VPN connection between your on-premises location and AWS and create a CLB that uses cross-zone load balancing to distributed traffic across EC2 instances and on-premises servers
- **B.** Provision a Direct Connect connection between your on-premises location and AWS and create a target group on an ALB to use Instance ID based targets for both your EC2 instances and on-premises server
- **C.** Provision a Direct Connect connection between your on-premises location and AWS and create a target group on an ALB to use IP based targets for both your EC2 instances and on-premises servers
- **D.** This cannot be done, ELBs are an AWS service and can only distributed traffic within the AWS cloud


**Q12.** Your company experiences fluctuations in traffic patterns to their e-commerce website based on flash sales. What service can help your company dynamically match the required compute capacity to the spike in traffic during flash sales?

- **A.** Auto Scaling
- **B.** Amazon Simple Notification Service (Amazon SNS)
- **C.** Amazon Glacier
- **D.** Amazon Virtual Private Cloud (Amazon VPC)


**Q13.** What feature is used for horizontal scaling of consumers to process data records from a Kinesis data stream?

- **A.** Vertical scaling shards
- **B.** Lambda
- **C.** Auto-Scaling
- **D.** Elastic Load Balancer


**Q14.** Your web application front end consists of multiple Amazon Compute Cloud (Amazon EC2) instances behind an Elastic Load Balancing load balancer. You have configured the load balancer to perform health checks on these Amazon EC2 instances. If an instance fails to pass health checks, which statement will be true?

- **A.** The instance is replaced automatically by the load balancer.
- **B.** The instance is quarantined by the load balancer for root cause analysis.
- **C.** The load balancer stops sending traffic to the instance that failed its health check.
- **D.** The instance is terminated automatically by the load balancer.


**Q15.** You create an Auto Scaling group in a new region that is configured with a minimum size value of 10, a maximum size value of 100, and a desired capacity value of 50. However, you notice that 30 of the Amazon Elastic Compute Cloud (Amazon EC2) instances within the Auto Scaling group fail to launch. Which of the following is the cause of this behavior?

- **A.** You have not raised your default Amazon EC2 capacity (20) for the new region.
- **B.** You did not attach an Elastic Load Balancing load balancer to the Auto Scaling group.
- **C.** The Auto Scaling group maximum value cannot be more than 20.
- **D.** You cannot define an Auto Scaling group larger than 20.


**Q16.** Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You configured ELB to perform health checks on these EC2 instances, if an instance fails to pass health checks, which statement will be true?

- **A.** The instance gets quarantined by the ELB for root cause analysis.
- **B.** The instance is replaced automatically by the ELB.
- **C.** The instance gets terminated automatically by the ELB.
- **D.** The ELB stops sending traffic to the instance that failed its health check.


**Q17.** You have recently enabled Access Logs on your Application Load Balancer (ALB). One of your colleagues would like to process the log files using a hosted Hadoop service. What configuration changes and services can be leveraged to deliver this requirement?

- **A.** Configure Access Logs to be delivered to S3 and use Kinesis for processing the log files
- **B.** Configure Access Logs to be delivered to EC2 and install Hadoop for processing the log files
- **C.** Configure Access Logs to be delivered to DynamoDB and use EMR for processing the log files
- **D.** Configure Access Logs to be delivered to S3 and use EMR for processing the log files


**Q18.** One of your EC2 instances that is behind an Elastic Load Balancer (ELB) is in the process of being de-registered. Which ELB feature can be used to allow existing connections to close cleanly?

- **A.** Deletion Protection
- **B.** Connection Draining
- **C.** Proxy Protocol
- **D.** Sticky Sessions


**Q19.** Which of the following Elastic Load Balancing options ensure that the load balancer determines which cipher is used for a Secure Sockets Layer (SSL) connection?

- **A.** Client Server Cipher Suite
- **B.** Server Order Preference
- **C.** First Server Cipher
- **D.** Server Cipher Only


**Q20.** What enables load balancing between multiple applications per load balancer?

- **A.** Sticky sessions
- **B.** Backend server authentication
- **C.** Path-based routing
- **D.** Listeners


**Q21.** Which of the following must be configured on an Elastic Load Balancing load balancer to accept incoming traffic?

- **A.** An instance
- **B.** A port
- **C.** A network interface
- **D.** A listener


**Q22.** You have created an Elastic Load Balancing load balancer listening on port 80, and you registered it with a single Amazon Elastic Compute Cloud (Amazon EC2) instance also listening on port 80. A client makes a request to the load balancer with the correct protocol and port for the load balancer. In this scenario, how many connections does the balancer maintain?

- **A.** 2
- **B.** 1
- **C.** 3
- **D.** 4


**Q23.** Your customer is willing to consolidate their log streams (access logs application logs security logs etc.) in one single system. Once consolidated, the customer wants to analyze these logs in real time based on heuristics. From time to time, the customer needs to validate heuristics, which requires going back to data samples extracted from the last 12 hours? What is the best approach to meet your customer’s requirements?

- **A.** Configure Amazon Cloud Trail to receive custom logs, use EMR to apply heuristics the logs
- **B.** Setup an Auto Scaling group of EC2 syslogd servers, store the logs on S3 use EMR to apply heuristics on the logs
- **C.** Send all the log events to Amazon Kinesis develop a client process to apply heuristics on the logs
- **D.** Send all the log events to Amazon SQS. Setup an Auto Scaling group of EC2 servers to consume the logs and apply the heuristics.


**Q24.** How is an Amazon Elastic Load Balancer (ELB) assigned?

- **A.** Per subnet
- **B.** Per EC2 instance
- **C.** Per VPC
- **D.** Per Auto-Scaling group


## SQS, SNS & Decoupling


**Q25.** A media sharing application is producing a very high volume of data in a very short period of time. Your back-end services are unable to manage the large volume of transactions. What option provides a way to manage the flow of transactions to your back-end services?

- **A.** Use an Amazon Simple Queue Service (Amazon SQS) queue to buffer the inbound transactions.
- **B.** Store the inbound transactions in an Amazon Relational Database Service (Amazon RDS) instance so that your back-end services can retrieve them as time permits.
- **C.** Store the inbound transactions in an Amazon Elastic MapReduce (Amazon EMR) cluster so that your back-end services can retrieve them as time permits.
- **D.** Use an Amazon Simple Notification Service (Amazon SNS) topic to buffer the inbound transactions.


**Q26.** You are using a series of Spot instances that process messages from an SQS queue and store results in a DynamoDB table. Shortly after picking up a message from the queue AWS terminated the Spot instance. The Spot instance had not finished processing the message. What will happen to the message?

- **A.** The message will become available for processing again after the visibility timeout expires
- **B.** The message will be lost as it would have been deleted from the queue when processed
- **C.** The message will remain in the queue and be immediately picked up by another instance
- **D.** The results may be duplicated in DynamoDB as the message will likely be processed multiple times


**Q27.** Your company provides a mobile voting application for a popular TV show, and 5 to 25 million viewers all vote in a 15- second timespan. What mechanism can you use to decouple the voting application from your back-end services that tally the votes?

- **A.** AWS CloudTrail
- **B.** Amazon Redshift
- **C.** Amazon Simple Notification Service (Amazon SNS)
- **D.** Amazon Simple Queue Service (Amazon SQS)


**Q28.** A web application you manage receives order processing information from customers and places the messages on an SQS queue. A fleet of EC2 instances are configured to pick up the messages, process them, and store the results in a DynamoDB table. The current configuration has been resulting in a large number of empty responses to ReceiveMessage requests. You would like to update the configuration to eliminate empty responses to reduce operational overhead. How can this be done?

- **A.** Use a Standard queue to provide at-least-once delivery, which means that each message is delivered at least once
- **B.** Use a FIFO (first-in-first-out) queue to preserve the exact order in which messages are sent and received
- **C.** Configure Short Polling to eliminate empty responses by reducing the length of time a connection request remains open
- **D.** Configure Long Polling to eliminate empty responses by allowing Amazon SQS to wait until a message is available in a queue before sending a response


**Q29.** You are a Solutions Architect at a media company and you need to build an application stack that can receive customer comments from sporting events. The application is expected to receive significant load that could scale to millions of messages within a short space of time following high-profile matches. As you are unsure of the load required for the database layer what is the most cost-effective way to ensure that the messages are not dropped?

- **A.** Create an SQS queue and modify the application to write to the SQS queue. Launch another application instance the polls the queue and writes messages to the database
- **B.** Use DynamoDB and provision enough write capacity to handle the highest expected load
- **C.** Write the data to an S3 bucket, configure RDS to poll the bucket for new messages
- **D.** Use RDS Auto Scaling for the database layer which will automatically scale as required


**Q30.** Your application polls an Amazon Simple Queue Service (Amazon SQS) queue frequently and returns immediately, often with empty ReceiveMessageResponses. What is one thing that can be done to reduce Amazon SQS costs?

- **A.** Pricing on Amazon SQS does not include a cost for service requests; therefore, there is no concern.
- **B.** Increase the timeout value for short polling to wait for messages longer before returning a response.
- **C.** Use long polling by supplying a WaitTimeSeconds of greater than 0 seconds when calling ReceiveMessage.
- **D.** Change the message visibility value to a higher number.


**Q31.** Of the following options, what is an efficient way to fanout a single Amazon Simple Notification Service (Amazon SNS) message to multiple Amazon Simple Queue Service (Amazon SQS) queues?

- **A.** Amazon SNS allows exactly one subscriber to each topic, so fanout is not possible.
- **B.** Create one Amazon SQS queue that subscribes to multiple Amazon SNS topics.
- **C.** Create an Amazon SNS topic using Amazon SNS. Create an application that subscribes to that topic and duplicates the message. Send copies to multiple Amazon SQS queues.
- **D.** Create an Amazon SNS topic using Amazon SNS. Then create and subscribe multiple Amazon SQS queues sent to the Amazon SNS topic.


**Q32.** Can an Amazon Simple Notification Service (Amazon SNS) message be deleted after being published to a topic?

- **A.** Only if a subscriber(s) has/have not read the message yet
- **B.** Yes. However it can be deleted only if the subscribers are Amazon SQS queues.
- **C.** Only if the Amazon SNS recall message parameter has been set
- **D.** No. After a message has been successfully published to a topic, it cannot be recalled.


**Q33.** When you create a new Amazon Simple Notification Service (Amazon SNS) topic, which of the following is created automatically?

- **A.** A message
- **B.** An Amazon Simple Queue Service (Amazon SQS) queue to deliver your Amazon SNS topic
- **C.** A subscriber
- **D.** An Amazon Resource Name (ARN)


**Q34.** What is the default time for an Amazon Simple Queue Service (Amazon SQS) visibility timeout?

- **A.** 30 seconds
- **B.** 12 hours
- **C.** 1 hour
- **D.** 60 seconds


**Q35.** What is the longest time available for an Amazon Simple Queue Service (Amazon SQS) visibility timeout?

- **A.** 60 seconds
- **B.** 1 hour
- **C.** 12 hours
- **D.** 30 seconds


**Q36.** What new feature was recently added to SQS that defines how messages are ordered?

- **A.** FIFO
- **B.** SNS
- **C.** decoupling
- **D.** TLS
- **E.** streams


**Q37.** What is the longest time available for an Amazon Simple Queue Service (Amazon SQS) long polling timeout?

- **A.** 30 seconds
- **B.** 20 seconds
- **C.** 10 seconds
- **D.** 1 hour


**Q38.** What AWS service can send notifications to customer smartphones and mobile applications with attached video and/or alerts?

- **A.** SQS
- **B.** Lambda
- **C.** EMR
- **D.** SNS
- **E.** CloudTrail


**Q39.** What Amazon AWS service is available to guarantee the consuming of a unique message only once?

- **A.** SQS
- **B.** Exchange
- **C.** SQL
- **D.** Beanstalk


**Q40.** What happens when you create a topic on Amazon SNS?

- **A.** You can create a topic on Amazon SQS, not on Amazon SNS.
- **B.** This question doesn't make sense.
- **C.** An ARN (Amazon Resource Name) is created.
- **D.** The topic is created, and it has the name you specified for it.


**Q41.** What is the default message retention period for Amazon Simple Queue Service (Amazon SQS)?

- **A.** 30 minutes
- **B.** 14 days
- **C.** 30 seconds
- **D.** 4 days


**Q42.** What is the longest configurable message retention period for Amazon Simple Queue Service (Amazon SQS)?

- **A.** 4 days
- **B.** 30 minutes
- **C.** 14 days
- **D.** 30 seconds


**Q43.** How does Amazon Simple Queue Service (Amazon SQS) deliver messages?

- **A.** Sequentially
- **B.** First In, First Out (FIFO)
- **C.** Amazon SQS doesn’t guarantee delivery of your messages in any particular order.
- **D.** Last In, First Out (LIFO)


**Q44.** Your application provides data transformation services. Files containing data to be transformed are first uploaded to Amazon S3 and then transformed by a fleet of spot EC2 instances. Files submitted by your premium customers must be transformed with the highest priority. How should you implement such a system?

- **A.** Use a single SQS queue. Each message contains the priority level. Transformation instances poll high-priority messages first.
- **B.** Use two SQS queues, one for high priority messages, the other for default priority. Transformation instances first poll the high priority queue; if there is no message, they poll the default priority queue.
- **C.** Use Route 53 latency based-routing to send high priority tasks to the closest transformation instances.
- **D.** Use a DynamoDB table with an attribute defining the priority level. Transformation instances will scan the table for tasks, sorting the results by priority level.


**Q45.** Can an Amazon Simple Notification Service (Amazon SNS) topic be recreated with a previously used topic name?

- **A.** Yes. The topic name should typically be available after 30–60 seconds after the previous topic with the same name has been deleted.
- **B.** Yes. The topic name should typically be available after 1–3 hours after the previous topic with the same name has been deleted.
- **C.** At this time, this feature is not supported.
- **D.** Yes. The topic name should typically be available after 24 hours after the previous topic with the same name has been deleted.


**Q46.** Amazon Simple Notification Service (Amazon SNS) is a push notification service that lets you send individual or multiple messages to large numbers of recipients. What types of clients are supported?

- **A.** Mobile and AMQP support for publisher and subscriber client types
- **B.** Java and JavaScript clients that support publisher and subscriber types
- **C.** Producers and consumers supported by C and C++ clients
- **D.** Publisher and subscriber client types


**Q47.** A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They use EC2 worker instances that pull transcoding jobs from SQS. Why is SQS an appropriate service for this scenario?

- **A.** SQS synchronously provides transcoding output.
- **B.** SQS checks the health of the worker instances.
- **C.** SQS guarantees the order of the messages.
- **D.** SQS helps to facilitate horizontal scaling of encoding tasks.


## DynamoDB Design & Capacity


**Q48.** Which of the following is not a supported Amazon Simple Notification Service (Amazon SNS) protocol?

- **A.** Amazon DynamoDB
- **B.** AWS Lambda
- **C.** Email-JSON
- **D.** HTTPS


## Route 53 & DNS Routing


**Q49.** A US-based company is expanding their web presence into Europe. The company wants to extend their AWS infrastructure from Northern Virginia (us-east-1) into the Dublin (eu-west1) region. Which of the following options would enable an equivalent experience for users on both continents?

- **A.** Use a public-facing load balancer per region to load-balance web traffic, and enable HTTP health checks.
- **B.** Use Amazon Route 53, and apply a weighted routing policy to distribute traffic across both regions.
- **C.** Use a public-facing load balancer per region to load-balance web traffic, and enable sticky sessions.
- **D.** Use Amazon Route 53, and apply a geolocation routing policy to distribute traffic across both regions.


**Q50.** You are configuring Route 53 for a customer’s website. Their web servers are behind an Internet-facing ELB. What record set would you create to point the customer’s DNS zone apex record at the ELB?

- **A.** Create a CNAME record that is an Alias, and select the ELB DNS as a target
- **B.** Create a PTR record pointing to the DNS name of the load balancer
- **C.** Create an A record that is an Alias, and select the ELB DNS as a target
- **D.** Create an A record pointing to the DNS name of the load balancer


## CloudFront & Edge Delivery


**Q51.** You have an unhealthy EC2 instance attached to an ELB that is being taken out of service. While the EC2 instance is being de- registered from the ELB, which ELB feature will cause the ELB to stop sending any new requests to the EC2 instance whilst allowing in-flight sessions to complete?

- **A.** ELB Cross zone load balancing
- **B.** ELB connection draining
- **C.** ELB proxy protocol
- **D.** ELB session affinity (sticky session)


## Lambda & Serverless Compute


**Q52.** You are running a suite of microservices on AWS Lambda that provide the business logic and access to data stored in Amazon DynamoDB for your task management system. You need to create well-defined RESTful Application Program Interfaces (APIs) for these microservices that will scale with traffic to support a new mobile application. What AWS Cloud service can you use to create the necessary RESTful APIs?

- **A.** Amazon Elastic Compute Cloud (Amazon EC2) Container Registry
- **B.** Amazon API Gateway
- **C.** Amazon Cognito
- **D.** Amazon Kinesis


## Monitoring: CloudWatch, CloudTrail & Config


**Q53.** A customer needs to capture all client connection information from their load balancer every five minutes. The company wants to use this data for analyzing traffic patterns and troubleshooting their applications. Which of the following options meets the customer requirements?

- **A.** Install the Amazon CloudWatch Logs agent on the load balancer.
- **B.** Enable Amazon CloudWatch metrics on the load balancer.
- **C.** Enable access logs on the load balancer.
- **D.** Enable AWS CloudTrail for the load balancer.


**Q54.** All of the website deployments are currently done by your company’s development team. With a surge in website popularity, the company is looking for ways to be more agile with deployments. What AWS cloud service can help the developers focus more on writing code instead of spending time managing and configuring servers, databases, load balancers, firewalls, and networks?

- **A.** AWS Trusted Advisor
- **B.** AWS Elastic Beanstalk
- **C.** AWS Config
- **D.** Amazon Kinesis


**Q55.** You are responsible for the application logging solution for your company’s existing applications running on multiple Amazon EC2 instances. Which of the following is the best approach for aggregating the application logs within AWS?

- **A.** Amazon CloudWatch Logs Agent
- **B.** An Elastic Load Balancing listener
- **C.** An internal Elastic Load Balancing load balancer
- **D.** Amazon CloudWatch custom metrics


**Q56.** You deployed your company website using Elastic Beanstalk and you enabled log file rotation to S3. An Elastic Map Reduce job is periodically analyzing the logs on S3 to build a usage dashboard that you share with your CIO. You recently improved overall performance of the website using Cloud Front for dynamic content delivery and your website as the origin After this architectural change, the usage dashboard shows that the traffic on your website dropped by an order of magnitude. How do you fix your usage dashboard?

- **A.** Change your log collection process to use Cloud Watch ELB metrics as input of the Elastic Map Reduce job
- **B.** Turn on Cloud Trail and use trail log tiles on S3 as input of the Elastic Map Reduce job
- **C.** Use Elastic Beanstalk 'Restart App server(s)" option to update log delivery to the Elastic Map Reduce job.
- **D.** Use Elastic Beanstalk "Rebuild Environment" option to update log delivery to the Elastic Map Reduce job.
- **E.** Enable Cloud Front to deliver access logs to S3 and use them as input of the Elastic Map Reduce job.


## ElastiCache & Caching Strategies


**Q57.** You have built a large web application that uses Amazon ElastiCache using Memcached to store frequent query results. You plan to expand both the web fleet and the cache fleet multiple times over the next year to accommodate increased user traffic. How do you minimize the amount of changes required when a scaling event occurs?

- **A.** Use an Elastic Load Balancer to proxy the requests
- **B.** Configure AutoDiscovery on the server side
- **C.** Configure AutoDiscovery on the client side
- **D.** Update the configuration file each time a new cluster


**Q58.** You are changing your application to move session state information off the individual Amazon Elastic Compute Cloud (Amazon EC2) instances to take advantage of the elasticity and cost benefits provided by Auto Scaling. Which of the following AWS Cloud services is best suited as an alternative for storing session state information?

- **A.** Amazon Storage Gateway
- **B.** Amazon DynamoDB
- **C.** Amazon Redshift
- **D.** Amazon Kinesis


## Hybrid Connectivity: Direct Connect & VPN


**Q59.** What is a primary difference between Classic and Network Load Balancer?

- **A.** Protocol target
- **B.** Cross-zone load balancing
- **C.** listener
- **D.** IP address target
- **E.** Auto-Scaling


## Elastic Beanstalk & Deployment


**Q60.** A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer, an Auto-Scaling group of Java/Tomcat application-servers, andDynamoDB as data store. The main web-application best runs on m2 x large instances since it is highly memory- bound Each new deployment requires semi-automated creationand testing of a new AMI for the application servers which takes quite a while ana is therefore only done once per week. Recently, a new chat feature has been implemented in nodejs and wails to be integrated in the architecture. First tests show that the new component is CPU bound Because the company has some experience with using Chef, they decided to streamline the deployment process and use AWS Ops Works as an application life cycle tool to simplify management of the application and reduce the deployment cycles. What configuration in AWS Ops Works is necessary to integrate the new chat module in the most cost-efficient and flexible way?

- **A.** Create one AWS Ops Works stack, create one AWS Ops Works layer, create one custom recipe
- **B.** Create two AWS Ops Works stacks create two AWS Ops Works layers create one custom recipe
- **C.** Create two AWS Ops Works stacks create two AWS Ops Works layers create two custom recipe
- **D.** Create one AWS Ops Works stack create two AWS Ops Works layers create one custom recipe


# Section B - Multiple Response (select all that apply)


## Auto Scaling & Elastic Load Balancing


**Q61.** Which of the following are required elements of an Auto Scaling group? **(Select 2.)**

- **A.** Desired capacity
- **B.** Minimum size
- **C.** Launch configuration
- **D.** Health checks


**Q62.** Which of the following are characteristics of the Auto Scaling service on AWS? **(Select 3.)**

- **A.** Sends traffic to healthy instances
- **B.** Collects and tracks metrics and sets alarms
- **C.** Launches instances from a specified Amazon Machine Image (AMI)
- **D.** Enforces a minimum number of running Amazon EC2 instances
- **E.** Delivers push notifications
- **F.** Responds to changing conditions by adding or terminating Amazon Elastic Compute Cloud (Amazon EC2) instances


**Q63.** An Auto Scaling group may use: **(Select 2.)**

- **A.** Stopped instances
- **B.** Already running instances if they use the same Amazon Machine Image (AMI) as the Auto Scaling group’s launch configuration and are not already part of another Auto Scaling group
- **C.** On-Demand Instances
- **D.** On-premises instances
- **E.** Spot Instances


**Q64.** What are the first two conditions used by Amazon AWS default termination policy for Multi-AZ architecture? **(Select 2.)**

- **A.** Availability Zone (AZ) with the most instances
- **B.** Unprotected instance closest to the next billing hour
- **C.** Random selection of any unprotected instance
- **D.** At least one instance that is not protected from scale in
- **E.** Unprotected instance with oldest launch configuration


**Q65.** Your e-commerce site was designed to be stateless and currently runs on a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances. In an effort to control cost and increase availability, you have a requirement to scale the fleet based on CPU and network utilization to match the demand curve for your site. What services do you need to meet this requirement? **(Select 2.)**

- **A.** Amazon CloudWatch
- **B.** Elastic Load Balancing
- **C.** Auto Scaling
- **D.** Amazon Simple Storage Service (Amazon S3)
- **E.** Amazon DynamoDB


**Q66.** What two features describe an Application Load Balancer (ALB)? **(Select 2.)**

- **A.** Layer 7 load balancer
- **B.** SSLlistener
- **C.** Backend server authentication
- **D.** Dynamic port mapping
- **E.** Multi-region forwarding


**Q67.** Auto Scaling supports which of the following plans for Auto Scaling groups? **(Select 3.)**

- **A.** End-user request driven
- **B.** Preemptive
- **C.** Dynamic
- **D.** Scheduled
- **E.** Manual
- **F.** Predictive


**Q68.** Elastic Load Balancing supports which of the following types of load balancers? **(Select 3.)**

- **A.** Interim
- **B.** Hypertext Transfer Protocol Secure (HTTPS) using Secure Sockets Layer (SSL)
- **C.** Internet-facing
- **D.** Cross-region
- **E.** Itinerant
- **F.** Internal


**Q69.** When an Amazon Elastic Compute Cloud (Amazon EC2) instance registered with an Elastic Load Balancing load balancer using connection draining is deregistered or unhealthy, which of the following will happen? **(Select 2.)**

- **A.** Forcibly close all connections to that instance after a timeout period.
- **B.** Leave the connections open as long as the load balancer is running.
- **C.** Immediately close all existing connections to that instance.
- **D.** Keep the connections open to that instance, and attempt to complete in-flight requests.
- **E.** Redirect the requests to a user-defined error page like “Oops this is embarrassing” or “Under Construction.”


**Q70.** An Auto-Scaling group spans 3 AZs and currently has 4 running EC2 instances. When Auto Scaling needs to terminate an EC2 instance by default, AutoScaling will ___________________. **(Select 2.)**

- **A.** Send an SNS notification, if configured to do so.
- **B.** Terminate the instance with the least active network connections. If multiple instances meet this criterion, one will be randomly selected.
- **C.** Randomly select one of the 3 AZs, and then terminate an instance in that AZ.
- **D.** Allow at least five minutes for Windows/Linux shutdown scripts to complete, before terminating the instance.
- **E.** Terminate an instance in the AZ which currently has 2 running EC2 instances.


**Q71.** Select two custom origin servers from the following options? **(Select 2.)**

- **A.** S3 object
- **B.** Elastic Load Balancer
- **C.** EC2 instance
- **D.** API gateway
- **E.** S3 bucket


**Q72.** You manage an application that uses Auto Scaling. Recently there have been incidents of multiple scaling events in an hour and you are looking at methods of stabilising the Auto Scaling Group. Select the statements below that are correct with regards to the Auto Scaling cooldown period? **(Select 2.)**

- **A.** It ensures that the Auto Scaling group terminates the EC2 instances that are least busy
- **B.** It ensures that the Auto Scaling group does not launch or terminate additional EC2 instances before the previous scaling activity takes effect
- **C.** The default value is 300 seconds
- **D.** It ensures that before the Auto Scaling group scales out, the EC2 instances can apply system updates


**Q73.** An EC2 instance in an Auto Scaling group that has been reported as unhealthy has been marked for replacement. What is the process Auto Scaling uses to replace the instance? **(Select 2.)**

- **A.** Auto Scaling will terminate the existing instance before launching a replacement instance
- **B.** Auto Scaling has to launch a replacement first before it can terminate the unhealthy instance
- **C.** If connection draining is enabled, Auto Scaling will wait for in-flight connections to complete or timeout
- **D.** Auto Scaling has to perform rebalancing first, and then terminate the instance


**Q74.** Several websites you run on AWS use multiple Internet-facing Elastic Load Balancers (ELB) to distribute incoming connections to EC2 instances running web applications. The ELBs are configured to forward using either TCP (layer 4) or HTTP (layer 7) protocols. You would like to start recording the IP addresses of the clients that connect to your web applications. Which ELB features will you implement with which protocols? **(Select 2.)**

- **A.** X-Forwarded-For request header and HTTP
- **B.** X-Forwarded-For request header and TCP
- **C.** Proxy Protocol and TCP
- **D.** Proxy Protocol and HTTP


## SQS, SNS & Decoupling


**Q75.** When designing a loosely coupled system, which AWS services provide an intermediate durable storage layer between components? **(Select 2.)**

- **A.** Amazon Simple Queue Service (Amazon SQS)
- **B.** Amazon Route 53
- **C.** AWS CloudFormation
- **D.** Amazon CloudFront
- **E.** Amazon Kinesis


**Q76.** Which of the following options are valid properties of an Amazon Simple Queue Service (Amazon SQS) message? **(Select 2.)**

- **A.** Message ID
- **B.** Type
- **C.** Body
- **D.** Destination


**Q77.** Which of the following actions can be authorized by IAM? **(Select 2.)**

- **A.** Querying an Oracle database
- **B.** Installing ASP.NET on a Windows Server
- **C.** Launching an Amazon Linux EC2 instance
- **D.** Adding a message to an Amazon Simple Queue Service (Amazon SQS) queue


**Q78.** Which of the following are features of Amazon Simple Notification Service (Amazon SNS)? **(Select 3.)**

- **A.** Subscribers
- **B.** Readers
- **C.** Publishers
- **D.** Topic


## DynamoDB Design & Capacity


**Q79.** What three services enable Single-AZ as a default? **(Select 3.)**

- **A.** S3
- **B.** ELB
- **C.** DynamoDB
- **D.** EC2
- **E.** Auto-Scaling


**Q80.** What two services enable automatic polling of a stream for new records only and forward them to an AWS storage service? **(Select 2.)**

- **A.** DynamoDB
- **B.** Kinesis
- **C.** Lambda
- **D.** SNS


## S3 Storage Classes & Lifecycle


**Q81.** A Solutions Architect is building a complex application with several back-end APIs. The architect is considering using Amazon API Gateway. With Amazon API Gateway what are features that assist with creating and managing APIs? **(Select 2.)**

- **A.** You can define plans that meter and restrict third-party developer access to APIs
- **B.** Flexible message delivery over multiple transport protocols
- **C.** You can operate multiple API versions and multiple stages for each version simultaneously
- **D.** You can define the maintenance window or AWS will schedule a 30 minute window


## Lambda & Serverless Compute


**Q82.** What are three valid endpoints for an API gateway? **(Select 3.)**

- **A.** HTTP method
- **B.** RESTful API
- **C.** Web server
- **D.** AWS service
- **E.** Lambda function


**Q83.** You are a Solutions Architect at Digital Cloud Training. A client of yours is using API Gateway for accepting and processing a large number of API calls to AWS Lambda. The client痴 business is rapidly growing and he is therefore expecting a large increase in traffic to his API Gateway and AWS Lambda services.The client has asked for advice on ensuring the services can scale without any reduction in performance. What advice would you give to the client? **(Select 2.)**

- **A.** API Gateway scales up to the default throttling limit, with some additional burst capacity available
- **B.** AWS Lambda scales concurrently executing functions up to your default limit
- **C.** API Gateway scales manually through the assignment of provisioned throughput
- **D.** API Gateway can only scale up to the fixed throttling limits


**Q84.** A Solutions Architect is creating a design for a multi-tiered serverless application. Which two services form the application facing services from the AWS serverless infrastructure? **(Select 2.)**

- **A.** Elastic Load Balancer
- **B.** AWS Lambda
- **C.** AWS Cognito
- **D.** API Gateway


**Q85.** The association between a poll-based source and a Lambda function is called the event source mapping. Event sources maintain the mapping configuration except for stream-based services such as ________ and ________ for which the configuration is made on the Lambda side and Lambda performs the polling. Fill in the blanks from the options below **(Select 2.)**

- **A.** S3
- **B.** Kinesis
- **C.** IoT Button
- **D.** DynamoDB


## High Availability & Fault Tolerance


**Q86.** What two statements correctly describes Elastic Load Balancer operation? **(Select 2.)**

- **A.** No cross-region support
- **B.** Spans multiple regions
- **C.** Assigned per Auto-Scaling group
- **D.** Assigned per subnet
- **E.** Assigned per EC2 instance


**Q87.** You would like to create a highly available web application that serves static content using multiple On-Demand EC2 instances. Which of the following AWS services will help you to achieve this? **(Select 2.)**

- **A.** DynamoDB and ElastiCache
- **B.** Elastic Load Balancer and Auto Scaling
- **C.** Multiple Availability Zones
- **D.** Direct Connect


## EBS Volumes & Snapshots


**Q88.** You are running a news website in the eu-west-1 region that updates every 15 minutes. The website has a world-wide audience it uses an Auto Scaling group behind an Elastic Load Balancer and an Amazon RDS database Static content resides on Amazon S3, and is distributed through Amazon CloudFront. Your Auto Scaling group is set to trigger a scale up event at 60% CPU utilization, you use an Amazon RDS extra large DB instance with 10.000 Provisioned IOPS its CPU utilization is around 80%. While freeable memory is in the 2 GB range. Web analytics reports show that the average load time of your web pages is around 1 5 to 2 seconds, but your SEO consultant wants to bring down the average load time to under 0.5 seconds. How would you improve page load times for your users? **(Select 3.)**

- **A.** Set up a second installation in another region, and use the Amazon Route 53 latencybased routing feature to select the right region.
- **B.** Switch Amazon RDS database to the high memory extra large Instance type
- **C.** Lower the scale up trigger of your Auto Scaling group to 30% so it scales more aggressively
- **D.** Configure Amazon CloudFront dynamic content support to enable caching of re-usable content from your site
- **E.** Add an Amazon ElastiCache caching layer to your application for storing sessions and frequent DB queries


## Monitoring: CloudWatch, CloudTrail & Config


**Q89.** An application you manage uses Auto Scaling and a fleet of EC2 instances. You recently noticed that Auto Scaling is scaling the number of instances up and down multiple times in the same hour. You need to implement a remediation to reduce the amount of scaling events. The remediation must be cost-effective and preserve elasticity What design changes would you implement? **(Select 2.)**

- **A.** Modify the Auto Scaling group termination policy to terminate the oldest instance first
- **B.** Modify the CloudWatch alarm period that triggers your Auto Scaling scale down policy
- **C.** Modify the Auto Scaling group cool-down timers
- **D.** Modify the Auto Scaling policy to use scheduled scaling actions


**Q90.** Select two cloud infrastructure services and/or components included with default CloudWatch monitoring? **(Select 2.)**

- **A.** Hypervisor metrics
- **B.** Operating system metrics
- **C.** Application level metrics
- **D.** SQS queues
- **E.** Virtual appliances


**Q91.** You need to implement a service to scan Application Program Interface (API) calls and related events’ history to your AWS account. This service will detect things like unused permissions, overuse of privileged accounts, and anomalous logins. Which of the following AWS Cloud services can be leveraged to implement this service? **(Select 3.)**

- **A.** AWS CloudTrail
- **B.** Auto Scaling
- **C.** AWS Lambda
- **D.** Amazon Route 53
- **E.** Amazon Simple Storage Service (Amazon S3)


## ElastiCache & Caching Strategies


**Q92.** Which of the following objects are good candidates to store in a cache? **(Select 3.)**

- **A.** Shopping cart
- **B.** Bank account balance
- **C.** Product catalog
- **D.** Session state


---


# Answer Key & Explanations


**Q1. B**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not D:* When you create an Auto Scaling group, you must specify the necessary information to configure the Amazon EC2 instances, the subnets for the instances, and the initial number of instances. To configure Amazon EC2 instances, you can specify a launch configuration, a launch template, or an EC2 instance. The following procedure demonstrates how to create an Auto Scaling group using an EC2 instance. To use a launch configuration or a launch template, see Creating an Auto Scaling Group Using a Launch Configuration or Creating an Auto Scaling Group Using a Launch Template. Refer: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html When you create an Auto Scaling group using an EC2 instance, Amazon EC2 Auto Scaling creates a launch configuration for you and associates it with the Auto Scaling group. This launch configuration has the same name as the Auto Scaling group, and it derives its attributes from the specified instance, such as AMI ID, instance type, and Availability Zone. Refer: This is the new world of scalable, on-demand web services. Pay for what you need and use, and not a byte more. Shortly after the launch of Amazon Elastic Compute Cloud (EC2), it was easy to do this with the simultaneous launch of Elastic Load Balancing, EC2 Auto Scaling, and Amazon CloudWatch. Since then we have added Auto Scaling to other AWS services including ECS, Spot Fleets, DynamoDB, Aurora, AppStream 2.0, and EMR. We have also added features such as target tracking to make it easier for you to scale based on the metric that is most appropriate for your application. Refer: https://aws.amazon.com/blogs/aws/aws-auto-scaling-unified-scaling-for-your-cloud-applications/

**Q2. B**  
_Auto Scaling & Elastic Load Balancing_  
Auto Scaling is designed to scale out based on an event like increased traffic while being cost effective when not needed.

**Q3. A**  
_Auto Scaling & Elastic Load Balancing_  
A launch configuration is a template that an EC2 Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances such as the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an EC2 instance before, you specified the same information in order to launch the instance. When you create an EC2 Auto Scaling group, you must specify a launch configuration. You can specify your launch configuration with multiple EC2 Auto Scaling groups. However, you can only specify one launch configuration for an EC2 Auto Scaling group at a time, and you can't modify a launch configuration after you've created it. Therefore, if you want to change the launch configuration for your EC2 Auto Scaling group, you must create a launch configuration and then update your EC2 Auto Scaling group with the new launch configuration. When you change the launch configuration for your EC2 Auto Scaling group, any new instances are launched using the new configuration parameters, but existing instances are not affected. Refer: https://aws.amazon.com/ec2/autoscaling/faqs/

**Q4. B**  
_Auto Scaling & Elastic Load Balancing_  
Simple – maintains a current number of instances, you can manually change the ASGs min/desired/max and attach/detach instances Scheduled – Used for predictable load changes, can be a single event or a recurring schedule Dynamic (event based) – scale in response to an event/alarm Step – configure multiple scaling steps in response to multiple alarms References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/compute/aws-auto-scaling/

**Q5. C**  
_Auto Scaling & Elastic Load Balancing_  
If using an ELB it is best to enable ELB health checks as otherwise EC2 status checks may show an instance as being healthy that the ELB has determined is unhealthy. In this case the instance will be removed from service by the ELB but will not be terminated by Auto Scaling Connection draining is not the correct answer as the ELB has taken the instance out of service so there are no active connections The health check grace period allows a period of time for a new instance to warm up before performing a health check More information on ASG health checks: By default uses EC2 status checks Can also use ELB health checks and custom health checks ELB health checks are in addition to the EC2 status checks If any health check returns an unhealthy status the instance will be terminated With ELB an instance is marked as unhealthy if ELB reports it as OutOfService A healthy instance enters the InService state If an instance is marked as unhealthy it will be scheduled for replacement If connection draining is enabled, Auto Scaling waits for in-flight requests to complete or timeout before terminating instances The health check grace period allows a period of time for a new instance to warm up before performing a health check (300 seconds by default) References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/aws-auto-scaling/

**Q6. E**  
_Auto Scaling & Elastic Load Balancing_  
A Classic Load Balancer is recommended only for EC2 Classic instances. The Application Load Balancer operates at the request level only. If you're dealing with HTTP requests, which you are for your web application, you can use this. It supports the basic feature of distributing requests using the round robin algorithm.

**Q7. C**  
_Auto Scaling & Elastic Load Balancing_  
For this solution you must provide an elastic solution that can scale quickly with demand up to the client's budget limit. Therefore, as the analysis shows you will need up to 150 EC2 instances, which is within the client's budget you should set the ASG with a maximum capacity of 150 EC2 instances so it cannot exceed the budget. If you’re anticipating a fast increase in load you can contact AWS and instruct them to pre-warm (provision) additional ELB nodes, this will ensure that the nodes will be ready when needed. References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/compute/aws-auto-scaling/ https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic- load-balancing/

**Q8. B**  
_Auto Scaling & Elastic Load Balancing_  
Only the launch configuration name, AMI, and instance type are needed to create an Auto Scaling launch configuration. Identifying a key pair, security group, and a block device mapping are optional elements for an Auto Scaling launch configuration.

**Q9. C**  
_Auto Scaling & Elastic Load Balancing_  
Refer: https://aws.amazon.com/cloudfront/getting-started/EC2/

**Q10. A**  
_Auto Scaling & Elastic Load Balancing_  
Amazon EC2 Auto Scaling is a fully managed service designed to launch or terminate Amazon EC2 instances automatically to help ensure you have the correct number of Amazon EC2 instances available to handle the load for your application. Amazon EC2 Auto Scaling helps you maintain application availability through fleet management for EC2 instances, which detects and replaces unhealthy instances, and by scaling your Amazon EC2 capacity up or down automatically according to conditions you define. You can use Amazon EC2 Auto Scaling to automatically increase the number of Amazon EC2 instances during demand spikes to maintain performance and decrease capacity during lulls to reduce costs. Refer: https://aws.amazon.com/ec2/autoscaling/faqs/

**Q11. C**  
_Auto Scaling & Elastic Load Balancing_  
The ALB (and NLB) supports IP addresses as targets Using IP addresses as targets allows load balancing any application hosted in AWS or on-premises using IP addresses of the application back-ends as targets You must have a VPN or Direct Connect connection to enable this configuration to work You cannot use instance ID based targets for on-premises servers and you cannot mix instance ID and IP address target types in a single target group The CLB does not support IP addresses as targets. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/elastic-load-balancing/ https://aws.amazon.com/blogs/aws/new-application-load-balancing-via-ip-address-to-aws-on-premises- resources/

**Q12. A**  
_Auto Scaling & Elastic Load Balancing_  
Auto Scaling helps maintain application availability and allows organizations to scale Amazon Elastic Compute Cloud (Amazon EC2) capacity up or down automatically according to conditions defined for the particular workload. Not only can it be used to help ensure that the desired number of Amazon EC2 instances are running, but it also allows resources to scale in and out to match the demands of dynamic workloads. Amazon Glacier, Amazon SNS, and Amazon VPC do not provide services to scale compute

**Q13. C**  
_Auto Scaling & Elastic Load Balancing_  
Recently, AWS launched a new feature of AWS Application Auto Scaling that let you define scaling policies that automatically add and remove shards to an Amazon Kinesis Data Stream. Refer: https://aws.amazon.com/blogs/big-data/scaling-amazon-kinesis-data-streams-with-aws- application-auto-scaling/

**Q14. C**  
_Auto Scaling & Elastic Load Balancing_  
When Amazon EC2 instances fail the requisite number of consecutive health checks, the load balancer stops sending traffic to the Amazon EC2 instance.

**Q15. A**  
_Auto Scaling & Elastic Load Balancing_  
The default Amazon EC2 instance limit for all regions is 20.

**Q16. D**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q17. D**  
_Auto Scaling & Elastic Load Balancing_  
Access Logs can be enabled on ALB and configured to store data in an S3 bucket. Amazon EMR is a web service that enables businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3 Neither Kinesis or EC2 provide a hosted Hadoop service You cannot configure access logs to be delivered to DynamoDB References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/ https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/

**Q18. B**  
_Auto Scaling & Elastic Load Balancing_  
Connection draining is enabled by default and provides a period of time for existing connections to close cleanly. When connection draining is in action an CLB will be in the status “InService: Instance deregistration currently in progress?? Session stickiness uses cookies and ensures a client is bound to an individual back-end instance for the duration of the cookie lifetime Deletion protection is used to protect the ELB from deletion The Proxy Protocol header helps you identify the IP address of a client when you have a load balancer that uses TCP for back-end connections. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/

**Q19. B**  
_Auto Scaling & Elastic Load Balancing_  
Elastic Load Balancing supports the Server Order Preference option for negotiating connections between a client and a load balancer. During the SSL connection negotiation process, the client and the load balancer present a list of ciphers and protocols that they each support, in order of preference. By default, the first cipher on the client’s list that matches any one of the load balancer’s ciphers is selected for the SSL connection. If the load balancer is configured to support Server Order Pr

**Q20. C**  
_Auto Scaling & Elastic Load Balancing_  
You can create a listener with rules to forward requests based on the URL path. This is known as path-based routing. If you are running microservices, you can route traffic to multiple back-end services using path-based routing. For example, you can route general requests to one target group and requests to render images to another target group. Refer: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-load- balancer-routing.html

**Q21. D**  
_Auto Scaling & Elastic Load Balancing_  
You can use the Amazon CloudWatch Logs Agent installer on existing Amazon EC2 instances to install and configure the CloudWatch Logs Agent.

**Q22. A**  
_Auto Scaling & Elastic Load Balancing_  
The load balancer maintains two separate connections: one connection with the client and one connection with the Amazon EC2 instance.

**Q23. A**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q24. B**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q25. A**  
_SQS, SNS & Decoupling_  
Amazon SQS is a fast, reliable, scalable, and fully managed message queuing service. Amazon SQS should be used to decouple the large volume of inbound transactions, allowing the back-end services to manage the level of throughput without losing messages.

**Q26. A**  
_SQS, SNS & Decoupling_  
The visibility timeout is the amount of time a message is invisible in the queue after a reader picks up the message. If a job is processed within the visibility timeout the message will be deleted. If a job is not processed within the visibility timeout the message will become visible again (could be delivered twice). The maximum visibility timeout for an Amazon SQS message is 12 hours The message will not be lost and will not be immediately picked up by another instance. As mentioned above it will be available for processing in the queue again after the timeout expires As the instance had not finished processing the message it should only be fully processed once. Depending on your application process however it is possible some data was written to DynamoDB. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/application-integration/amazon-sqs/

**Q27. D**  
_SQS, SNS & Decoupling_  
Amazon SQS is a fast, reliable, scalable, fully managed message queuing service that allows organizations to decouple the components of a cloud application. With Amazon SQS, organizations can transmit any volume of data, at any level of throughput, without losing messages or requiring other services to be always available. AWS CloudTrail records AWS API calls, and Amazon Redshift is a data warehouse, neither of which would be useful as an architecture component for decoupling components. Amazon

**Q28. D**  
_SQS, SNS & Decoupling_  
The correct answer is to use Long Polling which will eliminate empty responses by allowing Amazon SQS to wait until a message is available in a queue before sending a response The problem does not relate to the order in which the messages are processed in and there are no concerns over messages being delivered more than once so it doesn't matter whether you use a FIFO or standard queue Long Polling: - Uses fewer requests and reduces cost - Eliminates false empty responses by querying all servers - SQS waits until a message is available in the queue before sending a response - Requests contain at least one of the available messages up to the maximum number of messages specified in the ReceiveMessage action - Shouldn’t be used if your application expects an immediate response to receive message calls - ReceiveMessageWaitTime is set to a non-zero value (up to 20 seconds) - Same charge per million requests as short polling Changing the queue type would not assist in this situation Short Polling: - Does not wait for messages to appear in the queue - It queries only a subset of the available servers for messages (based on weighted random execution) - Short polling is the default - ReceiveMessageWaitTime is set to 0 - More requests are used, which implies higher cost References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/application-integration/amazon-sqs/ https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs- long-polling.html

**Q29. A**  
_SQS, SNS & Decoupling_  
Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages waiting to be processed. SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers and is used for distributed/decoupled applications This is a great use case for SQS as the messages you don't have to over-provision the database layer or worry about messages being dropped RDS Auto Scaling does not exist. With RDS you have to select the underlying EC2 instance type to use and pay for that regardless of the actual load on the DB With DynamoDB there are now 2 pricing options: - Provisioned capacity has been around forever and is one of the incorrect answers to this question. With provisioned capacity you have to specify the number of read/write capacity units to provision and pay for these regardless of the load on the database. - With the the new On-demand capacity mode DynamoDB is charged based on the data reads and writes your application performs on your tables. You do not need to specify how much read and write throughput you expect your application to perform because DynamoDB instantly accommodates your workloads as they ramp up or down. it might be a good solution to this question but is not an available option. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-integration/amazon- sqs/

**Q30. C**  
_SQS, SNS & Decoupling_  
Long polling allows your application to poll the queue, and, if nothing is there, Amazon Elastic Compute Cloud (Amazon EC2) waits for an amount of time you specify (between 1 and 20 seconds). If a message arrives in that time, it is delivered to your application as soon as possible. If a message does not arrive in that time, you need to execute the ReceiveMessage function again.

**Q31. D**  
_SQS, SNS & Decoupling_  
Multiple queues can subscribe to an Amazon SNS topic, which can enable parallel asynchronous processing.

**Q32. D**  
_SQS, SNS & Decoupling_  
No. After a message has been successfully published to a topic, it cannot be recalled.

**Q33. D**  
_SQS, SNS & Decoupling_  
When you create a new Amazon SNS topic, an Amazon ARN is created automatically.

**Q34. A**  
_SQS, SNS & Decoupling_  
The default time for an Amazon SQS visibility timeout is 30 seconds

**Q35. C**  
_SQS, SNS & Decoupling_  
The maximum time for an Amazon SQS visibility timeout is 12 hours

**Q36. A**  
_SQS, SNS & Decoupling_  
SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

**Q37. B**  
_SQS, SNS & Decoupling_  
The maximum time for an Amazon SQS long polling timeout is 20 seconds

**Q38. D**  
_SQS, SNS & Decoupling_  
With Amazon SNS , you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts. Refer: https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as- subscriber.html#:~:text=With%20Amazon%20SNS%20%2C%20you%20have,updates%2C%20or%20even%20sound%20alerts.

**Q39. A**  
_SQS, SNS & Decoupling_  
Standard queues provide at-least-once delivery, which means that each message is delivered at least once. FIFO queues provide exactly- once processing, which means that each message is delivered once and remains available until a consumer processes it and deletes it. Refer: https://aws.amazon.com/sqs/faqs/#:~:text=Q%3A%20Does%20Amazon%20SQS%20guarantee,processes%20it%20and%20deletes%20it.

**Q40. C**  
_SQS, SNS & Decoupling_  
When a topic is created, Amazon SNS will assign a unique ARN (Amazon Resource Name) to the topic, which will include the service name (SNS), region, AWS ID of the user and the topic name. The ARN will be returned as part of the API call to create the topic. Refer: https://aws.amazon.com/sns/faqs/#:~:text=When%20a%20topic%20is%20created,call%20to%20create%20the%20topic.

**Q41. D**  
_SQS, SNS & Decoupling_  
The default message retention period that can be set in Amazon SQS is four days.

**Q42. C**  
_SQS, SNS & Decoupling_  
The longest configurable message retention period for Amazon SQS is 14 days.

**Q43. C**  
_SQS, SNS & Decoupling_  
Amazon SQS does not guarantee in what order your messages will be delivered

**Q44. B**  
_SQS, SNS & Decoupling_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q45. A**  
_SQS, SNS & Decoupling_  
Topic names should typically be available for reuse approximately 30–60 seconds after the previous topic with the same name has been deleted. The exact time will depend on the number of subscriptions active on the topic; topics with a few subscribers will be available instantly for reuse, while topics with larger subscriber lists may take longer.

**Q46. D**  
_SQS, SNS & Decoupling_  
With Amazon SNS, you send individual or multiple messages to large numbers of recipients using publisher and subscriber client types.

**Q47. D**  
_SQS, SNS & Decoupling_  
Refer: https://aws.amazon.com/sqs/faqs/

**Q48. A**  
_DynamoDB Design & Capacity_  
Amazon DynamoDB is not a supported Amazon SNS protocol.

**Q49. B**  
_Route 53 & DNS Routing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q50. C**  
_Route 53 & DNS Routing_  
An Alias record can be used for resolving apex or naked domain names (e.g. example.com). You can create an A record that is an Alias that uses the customer's website zone apex domain name and map it to the ELB DNS name A CNAME record can’t be used for resolving apex or naked domain names A standard A record maps the DNS domain name to the IP address of a resource. You cannot obtain the IP of the ELB so you must use an Alias record which maps the DNS domain name of the customer's website to the ELB DNS name (rather than its IP) PTR records are reverse lookup records where you use the IP to find the DNS name References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and- content-delivery/amazon-route-53/

**Q51. B**  
_CloudFront & Edge Delivery_  
Connection draining is enabled by default and provides a period of time for existing connections to close cleanly. When connection draining is in action an CLB will be in the status “InService: Instance deregistration currently in progress?? Cross-zone load balancing is used to enable equal distribution of connections to targets in multiple AZs Session affinity enables the load balancer to bind a user's session to a specific instance Proxy Protocol is an Internet protocol used to carry connection information from the source requesting the connection to the destination for which the connection was requested References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/

**Q52. B**  
_Lambda & Serverless Compute_  
Amazon API Gateway is a fully managed service that makes it easy for developers to publish, maintain, monitor, and secure APIs at any scale. You can create an API that acts as a “front door” for applications to access data, business logic, or functionality from your code running on AWS Lambda. Amazon API Gateway handles all of the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitor

**Q53. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q54. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
AWS Elastic Beanstalk is the fastest and simplest way to get an application up and running on AWS. Developers can simply upload their application code, and the service automatically handles all the details such as resource provisioning, load balancing, Auto Scaling, and monitoring.

**Q55. A**  
_Monitoring: CloudWatch, CloudTrail & Config_  
You can use the Amazon CloudWatch Logs Agent installer on existing Amazon EC2 instances to install and configure the CloudWatch Logs Agent.

**Q56. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q57. C**  
_ElastiCache & Caching Strategies_  
When the clients are configured to use AutoDiscovery, they can discover new cache nodes as they are added or removed. AutoDiscovery must be configured on each client and is not active server side. Updating the configuration file each time will be very difficult to manage. Using an Elastic Load Balancer is not recommended for this scenario.

**Q58. B**  
_ElastiCache & Caching Strategies_  
Amazon DynamoDB is a NoSQL database store that is a great choice as an alternative due to its scalability, high-availability, and durability characteristics. Many platforms provide open-source, drop-in replacement libraries that allow you to store native sessions in Amazon DynamoDB. Amazon DynamoDB is a great candidate for a session storage solution in a share-nothing, distributed architecture.

**Q59. D**  
_Hybrid Connectivity: Direct Connect & VPN_  
You can load balance any application hosted in AWS or on-premises using IP addresses of the application backends as targets. This allows load balancing to an application backend hosted on any IP address and any interface on an instance. Each application hosted on the same instance can have an associated security group and use the same port. You can also use IP addresses as targets to load balance applications hosted in on-premises locations (over a Direct Connect or VPN connection), peered VPCs and EC2-Classic (using ClassicLink). The ability to load balance across AWS and on- prem resources helps you migrate-to-cloud, burst-to-cloud or failover-to-cloud. For Network Load Balancer - Network Load Balancer preserves the client side source IP allowing the back-end to see the IP address of the client. This can then be used by applications for further processing. For Classic Load Balancer - When using Amazon Virtual Private Cloud (Amazon VPC), you can create and manage security groups associated with Classic Load Balancer to provide additional networking and security options. You can also create a Classic Load Balancer without public IP addresses to serve as an internal (non-internet-facing) load balancer. Refer: https://aws.amazon.com/elasticloadbalancing/features/

**Q60. B**  
_Elastic Beanstalk & Deployment_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q61. B, C**  
_Auto Scaling & Elastic Load Balancing_  
An Auto Scaling group must have a minimum size and a launch configuration defined in order to be created. Health checks and a desired capacity are optional.

**Q62. C, D, F**  
_Auto Scaling & Elastic Load Balancing_  
Auto Scaling responds to changing conditions by adding or terminating instances, launches instances from an AMI specified in the launch configuration associated with the Auto Scaling group, and enforces a minimum number of instances in the min-size parameter of the Auto Scaling group.

**Q63. C, E**  
_Auto Scaling & Elastic Load Balancing_  
An Auto Scaling group may use On-Demand and Spot Instances. An Auto Scaling group may not use already stopped instances, instances running someplace other than AWS, and already running instances not started by the Auto Scaling group itself.

**Q64. A, D**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q65. A, C**  
_Auto Scaling & Elastic Load Balancing_  
Auto Scaling enables you to follow the demand curve for your applications closely, reducing the need to provision Amazon EC2 capacity manually in advance. For example, you can set a condition to add new Amazon EC2 instances in increments to the Auto Scaling group when the average CPU and network utilization of your Amazon EC2 fleet monitored in Amazon CloudWatch is high; similarly, you can set a condition to remove instances in the same increments when CPU and network utilization are low.

**Q66. A, D**  
_Auto Scaling & Elastic Load Balancing_  
Refer: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html

**Q67. C, D, E**  
_Auto Scaling & Elastic Load Balancing_  
Auto Scaling supports maintaining the current size of an Auto Scaling group using four plans: maintain current levels, manual scaling, scheduled scaling, and dynamic scaling.

**Q68. B, C, F**  
_Auto Scaling & Elastic Load Balancing_  
Elastic Load Balancing supports Internet-facing, internal, and HTTPS load balancers.

**Q69. D, E**  
_Auto Scaling & Elastic Load Balancing_  
When connection draining is enabled, the load balancer will stop sending requests to a deregistered or unhealthy instance and attempt to complete in-flight requests until a connection draining timeout period is reached, which is 300 seconds by default.

**Q70. A, C**  
_Auto Scaling & Elastic Load Balancing_  
Refer: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

**Q71. B, C**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q72. B, C**  
_Auto Scaling & Elastic Load Balancing_  
The cooldown period is a configurable setting for your Auto Scaling group that helps to ensure that it doesn't launch or terminate additional instances before the previous scaling activity takes effect The default cooldown period is applied when you create your Auto Scaling group The default value is 300 seconds You can configure the default cooldown period when you create the Auto Scaling group, using the AWS Management Console, the create-auto-scaling-group command (AWS CLI), or the CreateAutoScalingGroup API operation References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/compute/aws-auto-scaling/ https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html

**Q73. A, C**  
_Auto Scaling & Elastic Load Balancing_  
If connection draining is enabled, Auto Scaling waits for in-flight requests to complete or timeout before terminating instances. Auto Scaling will terminate the existing instance before launching a replacement instance Auto Scaling does not send a notification to the administrator Unlike AZ rebalancing, termination of unhealthy instances happens first, then Auto Scaling attempts to launch new instances to replace terminated instances References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-scaling/

**Q74. A, C**  
_Auto Scaling & Elastic Load Balancing_  
Proxy protocol for TCP/SSL carries the source (client) IP/port information X-forwarded-for for HTTP/HTTPS carries the source IP/port information In both cases the protocol carries the source IP/port information right through to the web server. If you were happy to just record the source connections on the load balancer you could use access logs. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/elastic-load-balancing/

**Q75. A, E**  
_SQS, SNS & Decoupling_  
Amazon Kinesis is a platform for streaming data on AWS, offering powerful services to make it easy to load and analyze streaming data. Amazon SQS is a fast, reliable, scalable, and fully managed message queuing service. Amazon SQS makes it simple and cost-effective to decouple the components of a cloud application.

**Q76. A, C**  
_SQS, SNS & Decoupling_  
The valid properties of an SQS message are Message ID and Body. Each message receives a system-assigned Message ID that Amazon SQS returns to you in the SendMessage response. The Message Body is composed of name/value pairs and the unstructured, uninterpreted content.

**Q77. C, D**  
_SQS, SNS & Decoupling_  
IAM controls access to AWS resources only. Installing ASP.NET will require Windows operating system authorization, and querying an Oracle database will require Oracle authorization.

**Q78. A, C, D**  
_SQS, SNS & Decoupling_  
Publishers, subscribers, and topics are the correct answers. You have subscribers to an Amazon SNS topic, not readers.

**Q79. B, D, E**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q80. B, C**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q81. A, C**  
_S3 Storage Classes & Lifecycle_  
Metering – define plans that meter and restrict third-party developer access to APIs Lifecycle Management – Operate multiple API versions and multiple stages for each version simultaneously so that existing applications can continue to call previous versions after new API versions are published References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-api- gateway/

**Q82. C, D, E**  
_Lambda & Serverless Compute_  
Refer: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html

**Q83. A, B**  
_Lambda & Serverless Compute_  
API Gateway can scale to any level of traffic received by an API. API Gateway scales up to the default throttling limit of 10,000 requests per second, and can burst past that up to 5,000 RPS. Throttling is used to protect back-end instances from traffic spikes Lambda uses continuous scaling  scales out not up. Lambda scales concurrently executing functions up to your default limit (1000) API Gateway does not use provisioned throughput - this is something that is used to provision performance in DynamoDB API Gateway can scale past the default throttling limits (they are not fixed, you just have to apply to have them adjusted) References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/networking-and-content-delivery/amazon-api-gateway/ https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/aws-lambda/

**Q84. B, D**  
_Lambda & Serverless Compute_  
The only application services here are API Gateway and Lambda and these are considered to be serverless services ECS provides the platform for running containers and uses Amazon EC2 instances ELB provides distribution of incoming network connections and also uses Amazon EC2 instances AWS Cognito is used for providing authentication services for web and mobile apps References: https://aws.amazon.com/serverless/

**Q85. B, D**  
_Lambda & Serverless Compute_  
Event sources are mapped to Lambda functions Event sources maintain the mapping configuration except for stream-based services (e.g. DynamoDB, Kinesis) for which the configuration is made on the Lambda side and Lambda performs the polling This question is really just asking you to identify which of the listed services are stream-based services. DynamoDB and Kinesis are both used for streaming data. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-route-53/

**Q86. A, C**  
_High Availability & Fault Tolerance_  
Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones. Elastic Load Balancing offers three types of load balancers that all feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant. Refer: https://aws.amazon.com/elasticloadbalancing/#:~:text=Elastic%20Load%20Balancing%20automatically%20distributes,or%20across%20multiple%20Availability%20Zones.

**Q87. B, C**  
_High Availability & Fault Tolerance_  
None of the answer options present the full solution. However, you have been asked which services will help you to achieve the desired outcome. In this case we need high availability for on-demand EC2 instances. A single Auto Scaling Group will enable the on-demand instances to be launched into multiple availability zones with an elastic load balancer distributing incoming connections to the available EC2 instances. This provides high availability and elasticity Amazon S3 and CloudFront could be used to serve static content from an S3 bucket, however the question states that the web application runs on EC2 instances DynamoDB and ElastiCache are both database services, not web application services, and cannot help deliver high availability for EC2 instances Direct Connect is used for connecting on-premise data centers into AWS using a private network connection and does not help in this situation at all. References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/networking-and-content-delivery/amazon-vpc/ https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/elastic-load-balancing/ https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto- scaling/

**Q88. B, C, E**  
_EBS Volumes & Snapshots_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q89. B, C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
The cooldown period is a configurable setting for your Auto Scaling group that helps to ensure that it doesn't launch or terminate additional instances before the previous scaling activity takes effect so this would help. After the Auto Scaling group dynamically scales using a simple scaling policy, it waits for the cooldown period to complete before resuming scaling activities The CloudWatch Alarm Evaluation Period is the number of the most recent data points to evaluate when determining alarm state. This would help as you can increase the number of datapoints required to trigger an alarm The order in which Auto Scaling terminates instances is not the issue here, the problem is that the workload is dynamic and Auto Scaling is constantly reacting to change and launching or terminating instances References: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation https://digitalcloud.guru/certification- training/aws-solutions-architect-associate/compute/aws-auto-scaling/

**Q90. A, D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Refer: https://aws.amazon.com/cloudwatch/

**Q91. A, C, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
You can enable AWS CloudTrail in your AWS account to get logs of API calls and related events’ history in your account. AWS CloudTrail records all of the API access events as objects in an Amazon S3 bucket that you specify at the time you enable AWS CloudTrail. You can take advantage of Amazon S3’s bucket notification feature by directing Amazon S3 to publish object-created events to AWS Lambda. Whenever AWS CloudTrail writes logs to your Amazon S3 bucket, Amazon S3 can then invoke your AWS Lambda.

**Q92. A, C, D**  
_ElastiCache & Caching Strategies_  
Many types of objects are good candidates to cache because they have the potential to be accessed by numerous users repeatedly. Even the balance of a bank account could be cached for short periods of time if the back-end database query is slow to respond.
