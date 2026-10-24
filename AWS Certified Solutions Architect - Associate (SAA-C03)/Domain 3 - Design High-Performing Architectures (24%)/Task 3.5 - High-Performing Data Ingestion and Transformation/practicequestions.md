# Task 3.5 - High-Performing Data Ingestion and Transformation - Practice Questions

> **Domain 3 - Design High-Performing Architectures (24%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **9 multiple-choice (single answer)** followed by **3 multiple-response (select 2+)**. Total **12**.


**Topic order in this file:** Auto Scaling & Elastic Load Balancing → DynamoDB Design & Capacity → Lambda & Serverless Compute → Kinesis & Streaming Ingestion → Redshift, Athena & Analytics → High Availability & Fault Tolerance


---


# Section A - Multiple Choice (one correct answer)


## Auto Scaling & Elastic Load Balancing


**Q1.** Your company collects information from the point of sale registers at all of its franchise locations. Each month these processes collect 200TB of information stored in Amazon Simple Storage Service (Amazon S3). Analytics jobs taking 24 hours are performed to gather knowledge from this data. Which of the following will allow you to perform these analytics in a cost-effective way?

- **A.** Create an application that reads the information of the Amazon S3 bucket and runs it through an Amazon Kinesis stream.
- **B.** Launch a d2.8xlarge (32 vCPU, 244GB RAM) Amazon Elastic Compute Cloud (Amazon EC2) instance, and run an application to read and process each object sequentially.
- **C.** Copy the data to a persistent Amazon Elastic MapReduce (Amazon EMR) cluster, and run the MapReduce jobs.
- **D.** Run a transient Amazon EMR cluster, and run the MapReduce jobs against the data directly in Amazon S3.


## DynamoDB Design & Capacity


**Q2.** You are a Solutions Architect at Digital Cloud Training. One of your clients runs an application that writes data to a DynamoDB table. The client has asked how they can implement a function that runs code in response to item level changes that take place in the DynamoDB table. What would you suggest to the client?

- **A.** Enable DynamoDB Streams and create an event source mapping between AWS Lambda and the relevant stream
- **B.** Use Kinesis Data Streams and configure DynamoDB as a producer
- **C.** Enable server access logging and create an event source mapping between AWS Lambda and the S3 bucket to which the logs are written
- **D.** Create a local secondary index that records item level changes and write some custom code that responds to updates to the index


## Lambda & Serverless Compute


**Q3.** An organization in the agriculture sector is deploying sensors and smart devices around factory plants and fields. The devices will collect information and send it to cloud applications running on AWS. Which AWS service will securely connect the devices to the cloud applications?

- **A.** AWS Glue
- **B.** AWS Lambda
- **C.** AWS IoT Core
- **D.** AWS DMS


## Kinesis & Streaming Ingestion


**Q4.** Your company has asked you to capture and forward a real-time data stream on a massive scale directly to RedShift for analysis with BI tools. What AWS tool is most appropriate that provides the feature set and cost effective?

- **A.** DynamoDB
- **B.** CloudFront
- **C.** Elastic Map Reduce
- **D.** SNS
- **E.** SQS
- **F.** Kinesis Firehose


**Q5.** The data scientists in your company are looking for a service that can process and analyze real-time, streaming data. They would like to use standard SQL queries to query the streaming data. Which combination of AWS services would deliver these requirements?

- **A.** DynamoDB and EMR
- **B.** Kinesis Data Streams and Kinesis Firehose
- **C.** Kinesis Data Streams and Kinesis Data Analytics
- **D.** ElastiCache and EMR


**Q6.** Your company has developed an IoT application that sends Telemetry data from 100,000 sensors. The sensors send a data point of 1 KB at one-minute intervals to a DynamoDB collector for monitoring purposes. What AWS stack would enable you to store data for real-time processing and analytics using BI tools?

- **A.** Sensors -> Kinesis Stream -> Firehose -> DynamoDB -> S3
- **B.** Sensors -> Kinesis Data Streams -> Firehose -> RDS
- **C.** Sensors -> AWS IoT -> Firehose -> RedShift
- **D.** Sensors -> Kinesis Stream -> Firehose -> DynamoDB


**Q7.** Which service allows you to process nearly limitless streams of data in flight?

- **A.** Amazon Kinesis Streams
- **B.** Amazon Elastic MapReduce (Amazon EMR)
- **C.** Amazon Redshift
- **D.** Amazon Kinesis Firehose


**Q8.** What is the capacity of a single Kinesis shard?

- **A.** 10 MB/sec data input and 10 MB/sec data output
- **B.** Unlimited
- **C.** 1 MB/sec data input and 2 MB/sec data output
- **D.** 1000 PUT records per second
- **E.** 2000 PUT records per second


## Redshift, Athena & Analytics


**Q9.** A Solutions Architect is designing a solution for a financial application that will receive trading data in large volumes. What is the best solution for ingesting and processing a very large number of data streams in near real time?

- **A.** Kinesis Data Streams
- **B.** Kinesis Firehose
- **C.** RedShift
- **D.** EMR


# Section B - Multiple Response (select all that apply)


## DynamoDB Design & Capacity


**Q10.** What are three examples of using Lambda functions to move data between AWS services? **(Select 3.)**

- **A.** Read data from DynamoDB stream to Firehose and write to S3
- **B.** Read data from Kinesis Firehose to Kinesis data stream
- **C.** Read data from Kinesis stream and write data to DynamoDB
- **D.** Read data from S3 and write metadata to DynamoDB
- **E.** Read data directly from DynamoDB streams to RDS


## High Availability & Fault Tolerance


**Q11.** A company is in the process of deploying an Amazon Elastic Map Reduce (EMR) cluster. Which of the statements below accurately describe the EMR service? **(Select 2.)**

- **A.** EMR makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), and other processing
- **B.** EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3
- **C.** EMR launches all nodes for a given cluster in the same Amazon EC2 Availability Zone
- **D.** EMR is a fully-managed service that makes it easy to set up and scale file storage in the Amazon Cloud


## Kinesis & Streaming Ingestion


**Q12.** You have been asked to implement a solution for capturing, transforming and loading streaming data into an Amazon RedShift cluster. The solution will capture data from Amazon Kinesis Data Streams. Which AWS services would you utilize in this scenario? **(Select 2.)**

- **A.** Kinesis Data Firehose for capturing the data and loading it into RedShift
- **B.** Kinesis Video Streams for capturing the data and loading it into RedShift
- **C.** EMR for transforming the data
- **D.** Lambda for transforming the data


---


# Answer Key & Explanations


**Q1. D**  
_Auto Scaling & Elastic Load Balancing_  
Because the job is run monthly, a persistent cluster will incur unnecessary compute costs during the rest of the month. Amazon Kinesis is not appropriate because the company is running analytics as a batch job and not on a stream. A single large instance does not scale out to accommodate the large compute needs.

**Q2. A**  
_DynamoDB Design & Capacity_  
DynamoDB Streams help you to keep a list of item level changes or provide a list of item level changes that have taken place in the last 24hrs. Amazon DynamoDB is integrated with AWS Lambda so that you can create triggers—pieces of code that automatically respond to events in DynamoDB Streams If you enable DynamoDB Streams on a table, you can associate the stream ARN with a Lambda function that you write. Immediately after an item in the table is modified, a new record appears in the table's stream. AWS Lambda polls the stream and invokes your Lambda function synchronously when it detects new stream records An event source mapping identifies a poll-based event source for a Lambda function. It can be either an Amazon Kinesis or DynamoDB stream. Event sources maintain the mapping configuration except for stream-based services (e.g. DynamoDB, Kinesis) for which the configuration is made on the Lambda side and Lambda performs the polling You cannot configure DynamoDB as a Kinesis Data Streams producer You can write Lambda functions to process S3 bucket events, such as the object-created or object-deleted events. For example, when a user uploads a photo to a bucket, you might want Amazon S3 to invoke your Lambda function so that it reads the image and creates a thumbnail for the photo . However, the questions asks for a solution that runs code in response to changes in a DynamoDB table, not an S3 bucket A local secondary index maintains an alternate sort key for a given partition key value, it does not record item level changes References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/database/amazon-dynamodb/ https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html https://digitalcloud.training/certification-training/aws-solutions- architect-associate/compute/aws-lambda/

**Q3. C**  
_Lambda & Serverless Compute_  
An organization in the agriculture sector is deploying sensors and smart devices around factory plants and fields. The devices will collect information and send it to cloud applications running on AWS

**Q4. F**  
_Kinesis & Streaming Ingestion_  
With Amazon Kinesis Data Firehose, you pay only for the volume of data you transmit through the service, and if applicable, for data format conversion. You also pay for Amazon VPC delivery and data transfer when applicable. There are no minimum fees or upfront commitments. You don’t need staff to operate, scale, and maintain infrastructure or custom applications to capture and load streaming data. https://aws.amazon.com/kinesis/data- firehose/features/ https://aws.amazon.com/kinesis/data-firehose/pricing/

**Q5. C**  
_Kinesis & Streaming Ingestion_  
Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized needs Amazon Kinesis Data Analytics is the easiest way to process and analyze real-time, streaming data. Kinesis Data Analytics can use standard SQL queries to process Kinesis data streams and can ingest data from Kinesis Streams and Kinesis Firehose but Firehose cannot be used for running SQL queries DynamoDB is a NoSQL database that can be used for storing data from a stream but cannot be used to process or analyze the data or to query it with SQL queries. Elastic Map Reduce (EMR) is a hosted Hadoop framework and is not used for analytics on streaming data. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/analytics/amazon-kinesis/

**Q6. C**  
_Kinesis & Streaming Ingestion_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not A:* With Amazon Kinesis Data Firehose, you can capture data continuously from connected devices such as consumer appliances, embedded sensors, and TV set-top boxes. Kinesis Data Firehose loads the data into Amazon S3 and Amazon Redshift, enabling you to provide your customers near real-time access to metrics, insights, and dashboards. Refer: https://aws.amazon.com/kinesis/data-firehose/

**Q7. A**  
_Kinesis & Streaming Ingestion_  
The Amazon Kinesis services enable you to work with large data streams. Within the Amazon Kinesis family of services, Amazon Kinesis Firehose saves streams to AWS storage services, while Amazon Kinesis Streams provide the ability to process the data in the stream.

**Q8. C**  
_Kinesis & Streaming Ingestion_  
Shard is the base throughput unit of a Kinesis stream. One shard provides a capacity of 1MB/sec data input and 2MB/sec data output. One shard can support up to 1000 PUT records per second. You will specify the number of shards needed when you create a stream. Refer: https://www.amazonaws.cn/en/kinesis/data-streams/faqs/#:~:text=Shard%20is%20the%20base%20throughput,when%20you%20create%20a%20stream.

**Q9. A**  
_Redshift, Athena & Analytics_  
Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized needs. It enables real- time processing of streaming big data and can be used for rapidly moving data off data producers and then continuously processing the data. Kinesis Data Streams stores data for later processing by applications (key difference with Firehose which delivers data directly to AWS services) Kinesis Firehose can allow transformation of data and it then delivers data to supported services RedShift is a data warehouse solution used for analyzing data EMR is a hosted Hadoop framework that is used for analytics References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/analytics/amazon-kinesis/

**Q10. A, C, D**  
_DynamoDB Design & Capacity_  
When building applications on AWS Lambda the core components are Lambda functions and triggers. A trigger is the AWS service or application that invokes a function, and a Lambda function is the code and runtime that process events. Refer: https://docs.aws.amazon.com/lambda/latest/dg/applications-usecases.html

**Q11. B, C**  
_High Availability & Fault Tolerance_  
Amazon EMR is a web service that enables businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3. EMR uses Apache Hadoop as its distributed data processing engine which is an open source, Java software framework that supports data-intensive distributed applications running on large clusters of commodity hardware Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), playback, and other processing EMR launches all nodes for a given cluster in the same Amazon EC2 Availability Zone EFS is a fully- managed service that makes it easy to set up and scale file storage in the Amazon Cloud. References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/analytics/amazon-emr/

**Q12. A, D**  
_Kinesis & Streaming Ingestion_  
For this solution Kinesis Data Firehose can be used as it can use Kinesis Data Streams as a source and can capture, transform, and load streaming data into a RedShift cluster. Kinesis Data Firehose can invoke a Lambda function to transform data before delivering it to destinations Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), and other processing, this solution does not involve video streams AWS Data Pipeline is used for processing and moving data between compute and storage services. It does not work with streaming data as Kinesis does Elastic Map Reduce (EMR) is used for processing and analyzing data using the Hadoop framework. It is not used for transforming streaming data. References: https://digitalcloud.training/certification-training/aws-solutions- architect-associate/analytics/amazon-kinesis/
