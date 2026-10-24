# Task 3.5 — Determine High-Performing Data Ingestion and Transformation Solutions

> This task covers the **data pipeline**: getting data in (batch or streaming), landing it somewhere (usually S3), transforming it, and making it queryable. The recurring exam decisions are **Kinesis vs SQS vs MSK**, **Firehose vs Data Streams**, **Glue vs EMR vs Lambda**, and **Athena vs Redshift**.

---

# 1. Data Pipeline Concepts

## 1.1 The stages

```
SOURCES → INGESTION → STORAGE (raw) → TRANSFORMATION → STORAGE (curated) → ANALYTICS / ML
```

| Stage | Typical AWS services |
|---|---|
| **Ingestion** | Kinesis Data Streams, Data Firehose, MSK, IoT Core, DMS, DataSync, Snowball, Transfer Family, API Gateway, SQS |
| **Raw storage (data lake)** | **Amazon S3**, Lake Formation |
| **Catalog** | **AWS Glue Data Catalog**, Glue crawlers |
| **Transformation** | Glue ETL, Glue DataBrew, EMR, Lambda, Step Functions, Managed Service for Apache Flink, Athena CTAS, Redshift SQL |
| **Curated storage** | S3 (Parquet, partitioned), Redshift, DynamoDB, OpenSearch |
| **Consumption** | Athena, Redshift, QuickSight, OpenSearch Dashboards, SageMaker |
| **Orchestration** | Step Functions, MWAA (Managed Workflows for Apache Airflow), EventBridge, Glue workflows |

## 1.2 Batch vs streaming

| | **Batch** | **Streaming** |
|---|---|---|
| Data arrives | Periodically, in bulk | Continuously, record by record |
| Latency | Minutes to hours | **Milliseconds to seconds** |
| Processing | Over a bounded dataset | Over unbounded data, in windows |
| Services | Glue, EMR, Batch, Lambda, Redshift COPY | Kinesis, MSK, Flink, Lambda |
| Use cases | Nightly reports, daily aggregation, historical reprocessing | Fraud detection, real-time dashboards, clickstream, IoT telemetry, log monitoring |

**Lambda architecture** (speed layer + batch layer) and **Kappa architecture** (one streaming path for everything) are the two canonical designs; AWS pipelines often land streaming data in S3 and then batch-process it, which blends both.

## 1.3 ETL vs ELT

- **ETL** — transform before loading. Classic for warehouses where the target schema is rigid.
- **ELT** — load raw into S3 or Redshift and transform in place with the power of the target engine. More common today because storage is cheap and schema-on-read gives flexibility. Athena and Redshift Spectrum make ELT practical.

---

# 2. Streaming Ingestion

## 2.1 Amazon Kinesis Data Streams

A durable, ordered, replayable stream of records.

**Mechanics:**
- A stream is divided into **shards**. Each shard supports **1 MB/s or 1,000 records/s in**, and **2 MB/s out** (shared across standard consumers).
- A record has a **partition key**, which is hashed to decide the shard. Records with the same partition key go to the same shard and are therefore **ordered within that key**.
- **Retention** is 24 hours by default, extendable to **365 days**, which makes **replay** possible — a key differentiator from SQS, where a message disappears once deleted.
- **Multiple independent consumers** can read the same data simultaneously.

**Capacity modes:**
- **Provisioned** — you manage shard count and can reshard (split/merge). Cheaper at steady, known throughput.
- **On-demand** — scales automatically up to 200 MB/s per stream with no shard management. Better for unpredictable load.

**Consumers:**
- **Standard (shared) consumers** poll and share the 2 MB/s per shard.
- **Enhanced fan-out** gives **each consumer its own 2 MB/s per shard** and pushes data with ~70 ms latency. Use when several consumers need full throughput or low latency.
- **Lambda event source mapping** — by default one concurrent invocation per shard; raise it with the **parallelization factor** (up to 10) for more concurrency while preserving per-partition-key ordering.
- **Kinesis Client Library (KCL)** handles checkpointing and shard rebalancing for custom consumers.

**Producers:** the **Kinesis Producer Library (KPL)** (aggregation and batching for efficiency), the SDK `PutRecords`, the **Kinesis Agent** for log files, and direct integrations from IoT Core, CloudWatch Logs, and EventBridge Pipes.

**Problems and fixes:**
- **`ProvisionedThroughputExceededException`** → a **hot shard** from a skewed partition key, or too few shards. Fix the partition key distribution or add shards.
- **`IteratorAgeMilliseconds` rising** → consumers are falling behind; add consumers/concurrency, use enhanced fan-out, or increase the parallelization factor.

## 2.2 Amazon Data Firehose (formerly Kinesis Data Firehose)

The **fully managed delivery** service: it ingests streaming data and writes it to a destination with **no shard or capacity management**.

- **Destinations:** **S3**, **Redshift** (via S3), **OpenSearch**, Splunk, and HTTP endpoints including partners like Datadog, New Relic, MongoDB.
- **Near real time** — buffered by **size (1–128 MB)** or **time (60–900 seconds)**, so the minimum latency is about **60 seconds**. Firehose is *not* real time; Data Streams is.
- **Built-in transformation** via a Lambda function, **format conversion** to **Parquet or ORC**, compression (GZIP, Snappy, ZIP), and **dynamic partitioning** of S3 prefixes based on record content.
- **No storage/replay** — once delivered, it's gone (failed records go to an S3 error prefix).
- Serverless and auto-scaling; you pay per GB ingested.

**Data Streams vs Firehose — the classic exam pair:**

| | **Kinesis Data Streams** | **Data Firehose** |
|---|---|---|
| Latency | **~200 ms (real time)** | **~60 s minimum (near real time)** |
| Storage/replay | **1–365 days, replayable** | None |
| Scaling | Shards (or on-demand) | **Fully automatic** |
| Consumers | Many custom consumers | Fixed set of destinations |
| Custom processing | Yes, any consumer code | Lambda transform only |
| Management | You manage shards | **Zero** |

Choose **Firehose** when the requirement is "load streaming data into S3/Redshift/OpenSearch with no administration." Choose **Data Streams** when you need **sub-second latency, replay, ordering, or multiple independent consumers**.

## 2.3 Amazon Managed Service for Apache Flink

Formerly Kinesis Data Analytics. Runs **Apache Flink** applications (Java, Scala, Python) or SQL over streaming data for **windowed aggregations, joins across streams, anomaly detection (`RANDOM_CUT_FOREST`), and enrichment** — all in real time, serverless.

Reads from Kinesis Data Streams or MSK; writes to Data Streams, Firehose, Lambda, S3, OpenSearch.

**Exam cue:** "real-time aggregation/analytics on a stream," "compute a moving average over a 5-minute window," "detect anomalies in streaming data."

## 2.4 Amazon MSK (Managed Streaming for Apache Kafka)

Fully managed **Apache Kafka**.

- Choose it when you need **Kafka APIs and ecosystem** — existing Kafka producers/consumers, Kafka Connect, Kafka Streams, Schema Registry — or when migrating an on-premises Kafka cluster.
- **Topics and partitions** instead of shards; message size up to **default 1 MB, configurable higher** (versus Kinesis's hard 1 MB).
- Retention is configurable, including **unlimited with tiered storage**.
- **MSK Serverless** removes broker capacity management.
- More operational knobs and more flexibility than Kinesis, but more to think about.

**Kinesis vs MSK:** Kinesis is simpler, deeply integrated with AWS services, and fully managed with shards; MSK is for Kafka compatibility and portability.

## 2.5 SQS vs Kinesis — a very common confusion

| | **SQS** | **Kinesis Data Streams** |
|---|---|---|
| Model | **Queue** — a message is consumed and deleted | **Stream** — records persist and can be re-read |
| Consumers | Typically one consumer per message | **Many consumers read the same records** |
| Ordering | Standard: best effort; FIFO: per group | **Per shard / partition key** |
| Replay | **No** | **Yes** |
| Scaling | Automatic, unlimited | Shards (or on-demand) |
| Use | Decoupling, work queues, task buffering | Analytics, real-time processing, log/event pipelines, multiple consumers |

"Multiple applications must process the same events" and "we must be able to replay the last 7 days" both point unambiguously to **Kinesis** (or MSK).

## 2.6 AWS IoT Core

Ingests device telemetry over **MQTT, HTTPS, and WebSockets** with device authentication (X.509), a device registry, device shadows, and a **rules engine** that routes messages to Kinesis, Firehose, Lambda, S3, DynamoDB, SNS, or OpenSearch. The front door for IoT pipelines at the scale of millions of devices.

---

# 3. Batch Ingestion and Migration

| Service | Purpose |
|---|---|
| **AWS DMS** | Database migration and **ongoing replication with CDC**; targets include S3, Kinesis, Redshift, OpenSearch, DynamoDB |
| **AWS DataSync** | Scheduled, validated, incremental transfer between on-prem (NFS/SMB/HDFS/object) and S3/EFS/FSx, up to 10× faster than open-source tools |
| **AWS Snow Family** | Offline petabyte-scale transfer when the network would take too long |
| **AWS Transfer Family** | Managed SFTP/FTPS/FTP/AS2 landing directly in S3 or EFS |
| **Storage Gateway** | Continuous hybrid file/volume/tape access backed by S3 |
| **S3 direct upload** | Multipart upload + Transfer Acceleration for large objects from distant clients |
| **Redshift COPY** | Bulk load from S3 in parallel — the correct way to load Redshift (never row-by-row INSERTs) |

---

# 4. Transformation

## 4.1 AWS Glue

A **serverless ETL and data-catalog** service.

- **Glue Data Catalog** — a central metadata repository of databases, tables, schemas, and partitions. It is the metastore used by **Athena, Redshift Spectrum, EMR, and Lake Formation** (and is Hive-metastore compatible).
- **Crawlers** scan S3 (and JDBC sources), **infer schema and partitions**, and populate the catalog on a schedule or trigger.
- **Glue ETL jobs** run **Apache Spark** (Scala/Python) or **Python shell** scripts serverlessly, billed per **DPU-hour** with a 1-minute minimum. **Glue Studio** gives a visual job editor; **job bookmarks** track what has already been processed so incremental runs don't reprocess old data.
- **Glue Streaming ETL** processes Kinesis/Kafka streams with Spark Structured Streaming.
- **Glue DataBrew** — a **visual, no-code** data preparation tool with 250+ built-in transformations, aimed at analysts for cleaning and normalizing data.
- **Glue Data Quality** defines and monitors data-quality rules.
- **Glue workflows and triggers** orchestrate multi-job pipelines.

**Glue vs EMR:** Glue is serverless, quick to start, and ideal for standard ETL and cataloguing. EMR gives you full cluster control, any framework/version, custom libraries, Spot cost optimization, and is better for very large or highly customized processing.

## 4.2 Amazon EMR

Managed Hadoop ecosystem: **Spark, Hive, Presto/Trino, HBase, Flink, Hudi, Iceberg**.

- **Node types:** **master** (coordination), **core** (compute + HDFS — losing them loses data), **task** (compute only — **ideal for Spot instances**).
- **Instance fleets** with mixed types and Spot allocation strategies; **managed scaling** resizes the cluster automatically.
- **EMRFS** lets jobs read/write S3 directly, which decouples storage from compute so clusters can be **transient** (spin up, run the job, terminate) — a major cost pattern.
- Variants: **EMR on EC2**, **EMR on EKS** (run Spark on an existing Kubernetes cluster), **EMR Serverless** (no cluster at all).

## 4.3 Lambda and Step Functions for transformation

- **Lambda** suits lightweight, event-driven transformation: an S3 `ObjectCreated` event triggers a function that validates, converts, enriches, or routes the object. Constrained by the **15-minute timeout**, 10 GB memory, and 10 GB `/tmp`.
- **Step Functions** orchestrates multi-stage pipelines with retries, parallel branches, and **Distributed Map** for fanning out over millions of S3 objects.
- **MWAA (Managed Workflows for Apache Airflow)** is the choice when the team already uses Airflow DAGs or needs complex scheduling and dependency management.

## 4.4 File formats and partitioning — the biggest performance lever

Converting raw CSV/JSON into **columnar, compressed, partitioned** files routinely cuts query time and cost by 90%+.

| Format | Type | Notes |
|---|---|---|
| CSV / JSON | Row, text | Human readable, large, no schema enforcement, slow to query |
| **Parquet** | **Columnar** | Best for analytics; column pruning, predicate pushdown, excellent compression. **The default recommendation.** |
| **ORC** | Columnar | Similar benefits, strong in the Hive ecosystem |
| **Avro** | Row, binary | Good for streaming/write-heavy and schema evolution |

**Compression:** **Snappy** (fast, splittable with Parquet/ORC — the usual choice), **GZIP** (better ratio, not splittable for text), **BZIP2** (splittable, slow), **ZSTD** (good balance).

**Partitioning:** organize S3 keys as `s3://bucket/table/year=2026/month=10/day=23/`. Queries with a `WHERE year=2026 AND month=10` clause then scan only those prefixes — **partition pruning**. Use **Hive-style `key=value`** naming so Athena and Glue detect partitions automatically; run `MSCK REPAIR TABLE` or use **partition projection** for very large partition counts.

**Other optimizations:** avoid many tiny files (compact into 128 MB–1 GB objects), bucket/sort data on common join keys, and use **open table formats** (**Apache Iceberg**, **Hudi**, **Delta Lake**) when you need ACID transactions, row-level updates/deletes, and time travel on a data lake. Athena and EMR both support Iceberg.

---

# 5. Query and Analytics Layer

## 5.1 Amazon Athena

**Serverless, interactive SQL (Trino/Presto) directly over S3** using the Glue Data Catalog.

- **Pay per terabyte scanned** (~$5/TB) — so every optimization that reduces bytes scanned reduces cost proportionally: **columnar formats, compression, partitioning, and selecting only needed columns**.
- **CTAS (`CREATE TABLE AS SELECT`)** converts and repartitions data in place — the standard trick to turn raw CSV into partitioned Parquet.
- **Federated queries** reach other data sources (RDS, DynamoDB, Redshift, CloudWatch, on-prem) through Lambda connectors.
- **Workgroups** separate teams, enforce **per-query and per-workgroup data scan limits**, and track cost.
- **Athena for Apache Spark** runs notebooks serverlessly.
- Best for ad-hoc analysis, log querying, and infrequent reporting. Not for high-concurrency sub-second dashboards — that is Redshift's job.

## 5.2 Amazon Redshift (analytics perspective)

Columnar MPP warehouse for repeated, complex, high-concurrency analytical queries. Key performance items: **distribution style** (KEY/ALL/EVEN/AUTO), **sort keys** and zone maps, **compression encodings**, **COPY** for parallel bulk loads, **Concurrency Scaling**, **materialized views**, **result caching**, **RA3 + managed storage**, **Spectrum** for S3, and **zero-ETL** ingestion from Aurora/RDS/DynamoDB.

**Athena vs Redshift:** Athena if the data lives in S3, queries are ad hoc, and you don't want a cluster. Redshift if you run the same complex queries repeatedly at high concurrency with low latency, and want to join across large curated tables.

## 5.3 Amazon OpenSearch Service

For **full-text search** and **log analytics** with near-real-time ingestion and rich dashboards. Typical pipeline: logs → Firehose (or OpenSearch Ingestion) → OpenSearch → Dashboards. Use **UltraWarm/Cold** tiers and **Index State Management** to control cost as indices age.

## 5.4 Amazon QuickSight

Serverless BI with **SPICE** (an in-memory engine for fast, repeated queries), ML Insights, embedded dashboards, and paginated reports. Connects to Athena, Redshift, RDS, S3, and more.

## 5.5 AWS Lake Formation

Builds and secures a data lake on S3: centralizes **fine-grained permissions** (database, table, **column**, **row**, and cell level) across Athena, Redshift Spectrum, EMR, and Glue, with **tag-based access control** and blueprints for ingestion. The answer to "grant analysts access to some columns but not the PII ones."

## 5.6 Amazon DataZone / Glue Data Quality
DataZone provides business-level data cataloguing, discovery, and governed sharing across an organization; Glue Data Quality monitors rules on datasets. Both appear occasionally in governance-flavoured questions.

---

# 6. Reference Architectures

**Real-time clickstream analytics**
```
Web/app → Kinesis Data Streams → Managed Service for Apache Flink (windowed aggregation)
            ├→ Data Firehose → S3 (Parquet, partitioned) → Athena / Redshift Spectrum
            └→ Lambda → DynamoDB → live dashboard (API Gateway + WebSocket)
```

**Serverless data lake**
```
Sources → (Firehose / DataSync / DMS) → S3 raw
        → Glue crawler → Glue Data Catalog
        → Glue ETL (convert to Parquet, partition) → S3 curated
        → Athena / Redshift Spectrum → QuickSight
        → Lake Formation for fine-grained permissions
```

**IoT telemetry**
```
Devices → IoT Core (MQTT) → Rules engine
        ├→ Kinesis Data Streams → Flink → alerts (SNS)
        ├→ Firehose → S3 → Athena
        └→ Timestream → Grafana / QuickSight
```

**Log analytics**
```
CloudWatch Logs / agents → Firehose → OpenSearch (hot) → Dashboards
                                   └→ S3 (UltraWarm/archive) → Athena
```

**Near-real-time warehouse without ETL**
```
Aurora / RDS MySQL / DynamoDB → zero-ETL integration → Redshift → QuickSight
```

---

# 7. Worked Scenarios

**Scenario 1 — "Stream clickstream data into S3 as Parquet with the least operational overhead."**
**Amazon Data Firehose** with record format conversion to Parquet and dynamic partitioning. No shards to manage.

**Scenario 2 — "Three different teams must each process the same event stream independently, and we need to replay the last week."**
**Kinesis Data Streams** with 7-day retention and **enhanced fan-out** consumers. SQS cannot replay; Firehose has no consumers.

**Scenario 3 — "Athena queries cost too much and take minutes."**
Convert to **Parquet with Snappy**, **partition** by date, compact small files, and select only required columns. Optionally add workgroup scan limits.

**Scenario 4 — "We need a moving 5-minute average and anomaly detection on sensor data in real time."**
**Managed Service for Apache Flink** reading from Kinesis Data Streams.

**Scenario 5 — "Migrate an on-prem Oracle database to Redshift with continuous replication."**
**AWS SCT** for schema plus **DMS with CDC** (optionally landing in S3 and loading with COPY).

**Scenario 6 — "Analysts want to clean and normalize data without writing code."**
**AWS Glue DataBrew.**

**Scenario 7 — "Catalogue our S3 data lake automatically so Athena can query it."**
**Glue crawlers** → **Glue Data Catalog** → Athena.

**Scenario 8 — "Grant the marketing team access to the orders table but hide the credit-card column."**
**AWS Lake Formation** column-level permissions.

**Scenario 9 — "Our Kinesis consumers keep falling behind (IteratorAge climbing)."**
Add shards if writes are throttled, enable **enhanced fan-out**, increase the Lambda **parallelization factor**, or scale out consumers. Check for a hot partition key.

**Scenario 10 — "We already run Kafka on-premises and want to move to AWS with no code changes."**
**Amazon MSK** (or MSK Serverless).

**Scenario 11 — "Nightly Spark job on 50 TB, cost is the priority, job is restartable."**
**Transient EMR cluster** reading from S3 (EMRFS) with **task nodes on Spot**, terminating on completion. Or **EMR Serverless**.

---

# 8. Quick Decision Table

| Requirement | Answer |
|---|---|
| Real-time stream, multiple consumers, replay | **Kinesis Data Streams** |
| Load streaming data to S3/Redshift/OpenSearch, zero admin | **Amazon Data Firehose** |
| Real-time windowed analytics / anomaly detection | **Managed Service for Apache Flink** |
| Kafka compatibility | **Amazon MSK** |
| Decouple producers/consumers, work queue | **Amazon SQS** |
| Millions of IoT devices over MQTT | **AWS IoT Core** |
| Serverless ETL + data catalog | **AWS Glue** |
| Automatically infer schema from S3 | **Glue crawler** |
| No-code visual data prep | **Glue DataBrew** |
| Big Spark/Hadoop clusters, custom frameworks, Spot savings | **Amazon EMR** |
| Lightweight event-driven transform | **Lambda** |
| Orchestrate a multi-step pipeline | **Step Functions** (or **MWAA** for Airflow) |
| Ad-hoc SQL over S3, pay per query | **Amazon Athena** |
| Repeated complex BI at high concurrency | **Amazon Redshift** |
| Query S3 from Redshift | **Redshift Spectrum** |
| Full-text search / log exploration | **OpenSearch Service** |
| Dashboards and BI | **Amazon QuickSight** |
| Column/row-level data lake permissions | **AWS Lake Formation** |
| Reduce Athena cost | **Parquet + Snappy + partitioning** |
| ACID updates/deletes and time travel on S3 | **Apache Iceberg / Hudi** |
| Database migration with CDC | **AWS DMS** |
| Scheduled on-prem → AWS file sync | **AWS DataSync** |
| Petabytes with poor bandwidth | **AWS Snowball Edge** |
| Load Redshift efficiently | **COPY from S3** |
| Analytics on operational data with no pipeline | **Zero-ETL integration** |
