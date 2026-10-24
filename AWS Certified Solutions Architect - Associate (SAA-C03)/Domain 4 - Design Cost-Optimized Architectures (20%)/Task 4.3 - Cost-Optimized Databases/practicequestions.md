# Task 4.3 - Cost-Optimized Databases - Practice Questions

> **Domain 4 - Design Cost-Optimized Architectures (20%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **12 multiple-choice (single answer)** followed by **3 multiple-response (select 2+)**. Total **15**.


**Topic order in this file:** DynamoDB Design & Capacity → RDS Multi-AZ, Read Replicas & Aurora → Redshift, Athena & Analytics → ElastiCache & Caching Strategies


---


# Section A - Multiple Choice (one correct answer)


## DynamoDB Design & Capacity


**Q1.** A DynamoDB table is configured with 12,000 provisioned RCUs and 8,000 provisioned WCUs, but CloudWatch shows average consumption of roughly 600 RCUs and 400 WCUs with occasional short spikes. What is the MOST cost-effective change?

- **A.** Enable DynamoDB Accelerator (DAX) in front of the table
- **B.** Switch the table to on-demand capacity mode
- **C.** Reduce the provisioned capacity to the observed average and accept throttling during spikes
- **D.** Purchase DynamoDB reserved capacity for the current provisioned levels


**Q2.** An e-commerce DynamoDB table has highly predictable, steady traffic that has run at a consistent 4,000 RCUs and 2,000 WCUs for the past 18 months. The company wants to minimise cost and is willing to commit. What should the solutions architect recommend?

- **A.** Create a global table replica to spread the load across Regions
- **B.** Use provisioned capacity mode with auto scaling and purchase DynamoDB reserved capacity
- **C.** Switch the table to the DynamoDB Standard-Infrequent Access table class
- **D.** Switch the table to on-demand capacity mode


**Q3.** An application repeatedly runs a Scan operation with a filter expression on a 900 GB DynamoDB table to find items by a non-key attribute. The read costs are very high. What is the MOST cost-effective fix?

- **A.** Switch the table to on-demand capacity mode
- **B.** Enable DynamoDB Accelerator (DAX) to cache the Scan results
- **C.** Increase provisioned read capacity so the Scan completes faster
- **D.** Create a global secondary index on the attribute and replace the Scan with a Query


**Q4.** A DynamoDB table stores 8 TB of historical order records. Fewer than 1% of items are read in any month, but the table must remain queryable. Storage dominates the table's cost. Which change reduces cost the MOST?

- **A.** Create a global secondary index on the order date
- **B.** Switch the table to the DynamoDB Standard-Infrequent Access table class
- **C.** Enable point-in-time recovery
- **D.** Enable DynamoDB Accelerator (DAX)


**Q5.** A DynamoDB table stores user session records that remain valid for 24 hours. The table grows continuously and a nightly Lambda function issues millions of DeleteItem calls to purge stale sessions, consuming large amounts of write capacity. What is the MOST cost-effective alternative?

- **A.** Run the cleanup job on a larger Lambda memory setting to finish faster
- **B.** Switch the table to on-demand capacity mode during the cleanup window
- **C.** Export the table to Amazon S3 each night and recreate it empty
- **D.** Enable DynamoDB Time to Live (TTL) on an expiry timestamp attribute


## RDS Multi-AZ, Read Replicas & Aurora


**Q6.** A company runs 30 Amazon RDS for PostgreSQL instances in a development account. The instances are only used between 09:00 and 18:00 on weekdays but run continuously. Which approach reduces cost the MOST while keeping the databases available during working hours?

- **A.** Purchase 3-year all-upfront Reserved Instances for all development databases
- **B.** Convert all development instances to the db.t4g.micro instance class
- **C.** Schedule automated stop and start of the development instances outside working hours using EventBridge Scheduler and AWS Lambda
- **D.** Enable Multi-AZ on all development instances to improve utilisation


**Q7.** A solutions architect reviews an Aurora MySQL cluster bill and finds that I/O charges account for about 45% of the total cluster spend. Which change is MOST likely to reduce the overall cost?

- **A.** Enable Aurora Backtrack to reduce read I/O
- **B.** Add two more Aurora Replicas to spread the I/O load
- **C.** Switch the cluster to the Aurora I/O-Optimized configuration
- **D.** Move the cluster to Aurora Serverless v1


**Q8.** An internal reporting application queries an Amazon RDS for MySQL database a few times per hour. Traffic is highly intermittent, with long idle periods overnight and at weekends. Which database configuration is the MOST cost-effective?

- **A.** Amazon Aurora Serverless v2 with a low minimum Aurora Capacity Unit setting
- **B.** An RDS Multi-AZ deployment with two read replicas
- **C.** Amazon Redshift with Concurrency Scaling enabled
- **D.** A db.r6g.2xlarge RDS instance with a 3-year Reserved Instance


**Q9.** A company pays substantial Microsoft SQL Server licence fees for an Amazon RDS deployment. The application's data access layer uses standard T-SQL. Management wants to eliminate the licence cost with the least application rewriting. What should the solutions architect propose?

- **A.** Move the SQL Server instance to EC2 with a Dedicated Host and bring-your-own-licence
- **B.** Enable the RDS Multi-AZ DB cluster deployment for SQL Server
- **C.** Migrate to Amazon DynamoDB using the AWS Schema Conversion Tool
- **D.** Migrate to Amazon Aurora PostgreSQL with Babelfish enabled


## Redshift, Athena & Analytics


**Q10.** A business intelligence team runs a 10-node Amazon Redshift cluster that is only queried during a four-hour window each weekday. The cluster bills 24/7. Which option reduces cost with the least operational change?

- **A.** Pause the cluster outside the query window and resume it before the window begins, or migrate to Amazon Redshift Serverless
- **B.** Move all of the data to Amazon S3 and query it only with Redshift Spectrum
- **C.** Resize the cluster to 2 nodes and leave it running permanently
- **D.** Enable Concurrency Scaling on the cluster


**Q11.** Analysts query raw CSV files in an Amazon S3 data lake using Amazon Athena. Monthly Athena charges are high because each query scans hundreds of gigabytes. Which change will reduce Athena cost the MOST?

- **A.** Move the S3 data to S3 Intelligent-Tiering
- **B.** Increase the Athena workgroup query result cache size
- **C.** Convert the data to Snappy-compressed Apache Parquet and partition it by date
- **D.** Load all of the data into Amazon Redshift and query it there


## ElastiCache & Caching Strategies


**Q12.** A read-heavy application issues the same expensive query to an RDS database thousands of times per minute. The team is considering adding four more read replicas. Which alternative is likely to be more cost-effective while also improving latency?

- **A.** Upgrade the primary instance to the next larger instance class
- **B.** Enable Performance Insights on the database
- **C.** Add an Amazon ElastiCache cluster and implement a lazy-loading cache with a TTL
- **D.** Enable Multi-AZ on the primary database instance


# Section B - Multiple Response (select all that apply)


## DynamoDB Design & Capacity


**Q13.** A solutions architect is optimising DynamoDB read costs for a high-traffic application. Which TWO changes will directly reduce the read capacity consumed? (Select 2.) **(Select 2.)**

- **A.** Enable point-in-time recovery on the table
- **B.** Increase the provisioned read capacity units
- **C.** Add a local secondary index to every table
- **D.** Use eventually consistent reads instead of strongly consistent reads where the application tolerates it
- **E.** Replace Scan operations with Query operations against an appropriate index


## RDS Multi-AZ, Read Replicas & Aurora


**Q14.** A finance team is reviewing a production RDS bill. Which TWO actions reduce cost without reducing production availability? (Select 2.) **(Select 2.)**

- **A.** Delete all read replicas serving the reporting workload
- **B.** Reduce the automated backup retention period to 0 days
- **C.** Disable Multi-AZ on the production primary database
- **D.** Identify and delete orphaned manual DB snapshots that are no longer required
- **E.** Migrate the instances to Graviton-based db.r6g instance classes


## Redshift, Athena & Analytics


**Q15.** An operational RDS database holds 8 years of transaction history, but only the most recent 90 days is ever queried by the application. Which TWO actions form a cost-effective archival strategy? (Select 2.) **(Select 2.)**

- **A.** Increase the RDS allocated storage and enable storage autoscaling
- **B.** Apply an S3 lifecycle rule to transition the archived data to S3 Glacier classes as it ages
- **C.** Enable Multi-AZ so the historical data is replicated synchronously
- **D.** Export the historical rows to Amazon S3 in Apache Parquet format and query them with Amazon Athena when needed
- **E.** Create a cross-Region read replica to hold the historical data


---


# Answer Key & Explanations


**Q1. B**  
_DynamoDB Design & Capacity_  
At roughly 5% utilisation the table is paying for capacity it never uses. On-demand mode charges per request with no capacity planning and costs nothing when idle, which is far cheaper below roughly 15-20% utilisation. Reserved capacity would lock in the waste, and DAX addresses read latency, not over-provisioning.

**Q2. B**  
_DynamoDB Design & Capacity_  
For steady, predictable throughput, provisioned capacity is substantially cheaper per request than on-demand, and DynamoDB reserved capacity adds up to roughly 77% savings for a 1- or 3-year commitment. Auto scaling keeps utilisation high. Standard-IA reduces storage cost but raises request cost, and a global table multiplies cost.

**Q3. D**  
_DynamoDB Design & Capacity_  
A Scan reads every item in the table and bills for all of it before the filter is applied. A GSI on the queried attribute allows a Query that reads only matching items, typically reducing consumed capacity by orders of magnitude. Project only the attributes needed to keep index storage and write cost low.

**Q4. B**  
_DynamoDB Design & Capacity_  
The DynamoDB Standard-IA table class reduces storage costs by about 60% in exchange for higher read and write request costs, which is the right trade-off when storage dominates and access is rare. DAX and extra indexes add cost, and PITR adds backup charges.

**Q5. D**  
_DynamoDB Design & Capacity_  
DynamoDB TTL automatically deletes expired items at no additional cost and without consuming write capacity units. It also keeps the table small, reducing storage and scan costs. Issuing explicit DeleteItem calls consumes WCUs for every deletion.

**Q6. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Development databases needed roughly 45 of 168 hours per week can be stopped the rest of the time, cutting instance-hour charges by about 73%. RDS instances can be stopped for up to 7 days at a time. Note that storage and backups continue to bill while stopped. Reserved Instances would commit to paying for idle time, and Multi-AZ doubles cost.

**Q7. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Aurora I/O-Optimized removes per-I/O charges in exchange for a higher instance and storage rate, and becomes cheaper when I/O exceeds roughly 25% of the cluster's total spend. Adding replicas increases instance cost, and Backtrack is a recovery feature, not an I/O optimisation.

**Q8. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Aurora Serverless v2 scales capacity in fine-grained 0.5 ACU increments within a second and scales down during idle periods, so you pay close to nothing when the workload is quiet. A reserved provisioned instance pays for 24/7 capacity that is mostly idle.

**Q9. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Babelfish for Aurora PostgreSQL understands the SQL Server TDS wire protocol and T-SQL dialect, so many SQL Server applications connect and run with little or no code change while eliminating commercial licence fees. DynamoDB is non-relational and would require a full rewrite.

**Q10. A**  
_Redshift, Athena & Analytics_  
Pausing a Redshift cluster stops compute billing while retaining storage, and Redshift Serverless bills per RPU-second with no idle charge. Both suit a workload used only a few hours per day. Concurrency Scaling adds burst capacity but does not remove idle charges.

**Q11. C**  
_Redshift, Athena & Analytics_  
Athena bills about $5 per terabyte scanned. Columnar Parquet with compression lets Athena read only the required columns, and date partitioning lets it skip irrelevant prefixes entirely. Together these commonly reduce bytes scanned, and therefore cost, by over 90%. Storage class changes do not affect scan charges.

**Q12. C**  
_ElastiCache & Caching Strategies_  
A cache node is typically far cheaper than several full-price read replicas and serves repeated identical queries from memory in sub-millisecond time, removing most of the load from the database. Multi-AZ adds availability but no read capacity, and Performance Insights is a diagnostic tool.

**Q13. D, E**  
_DynamoDB Design & Capacity_  
An eventually consistent read consumes half the read capacity of a strongly consistent read. Replacing a Scan, which reads the whole table, with a Query that targets only relevant items dramatically reduces consumed RCUs. Adding indexes increases write cost and storage, and raising provisioned capacity raises cost rather than reducing consumption.

**Q14. D, E**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Graviton-based database instance classes deliver better price-performance at a lower hourly rate with no availability impact. Manual snapshots persist until explicitly deleted, even after the source instance is removed, and are a common silent cost. Disabling Multi-AZ, removing backups or deleting needed replicas all reduce availability or recoverability.

**Q15. B, D**  
_Redshift, Athena & Analytics_  
Moving cold rows out of expensive database storage into S3 as compressed Parquet, queryable on demand with Athena, is far cheaper than keeping them in RDS. Lifecycle rules then tier the archived objects to Glacier as they age. The other options increase cost without addressing the problem.
