# Task 3.3 — Determine High-Performing Database Solutions

> AWS has a **purpose-built database** for every data shape. The exam gives you a workload description and expects you to pick the right engine, then tune it (caching, read replicas, capacity mode, indexes, connection pooling).

---

# 1. Choosing the Right Database

## 1.1 The purpose-built catalogue

| Database type | AWS service | Data model | Classic use cases |
|---|---|---|---|
| **Relational (OLTP)** | **RDS** (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2), **Aurora** (MySQL/PostgreSQL compatible) | Tables, rows, joins, ACID, SQL | ERP, CRM, finance, e-commerce, any app needing complex queries and transactions |
| **Key-value / document** | **DynamoDB** | Items with attributes, accessed by key | Serverless apps, gaming leaderboards, session stores, IoT, shopping carts, high-scale web |
| **Document** | **DocumentDB** (MongoDB-compatible) | JSON documents, flexible schema | Content management, catalogues, user profiles, MongoDB migrations |
| **In-memory** | **ElastiCache** (Redis/Valkey, Memcached), **MemoryDB** | Key-value in RAM | Caching, session store, leaderboards, pub/sub, rate limiting; MemoryDB adds durability |
| **Graph** | **Neptune** | Nodes and edges (Gremlin, openCypher, SPARQL) | Social networks, fraud detection, recommendation engines, knowledge graphs, network topology |
| **Time series** | **Timestream** | Timestamped measures | IoT telemetry, DevOps metrics, industrial sensors, clickstream |
| **Wide column** | **Keyspaces** (Cassandra-compatible) | Partition/clustering keys, CQL | Cassandra migrations, industrial/fleet data at scale |
| **Ledger** | **QLDB** | Immutable, cryptographically verifiable journal | Audit trails, supply-chain provenance, financial records |
| **Data warehouse (OLAP)** | **Redshift** | Columnar, MPP | BI, dashboards, complex analytical queries over terabytes/petabytes |
| **Search** | **OpenSearch Service** | Inverted index | Full-text search, log analytics, observability |

## 1.2 How to decide

1. **Is the access pattern known and simple (get/put by key) with massive scale?** → **DynamoDB**.
2. **Do you need joins, complex ad-hoc queries, transactions across tables, or existing SQL?** → **RDS/Aurora**.
3. **Is the question analytical (aggregations over huge historical datasets)?** → **Redshift** (or Athena over S3 for ad hoc).
4. **Are relationships themselves the query ("friends of friends who bought X")?** → **Neptune**.
5. **Is it full-text search or log exploration?** → **OpenSearch**.
6. **Is it microsecond-latency reads of hot data?** → **ElastiCache/DAX/MemoryDB**.
7. **Is it append-only timestamped measurements?** → **Timestream**.

**OLTP vs OLAP** is the single most useful distinction: OLTP means many small, fast, concurrent reads/writes of individual records (row-oriented, RDS/Aurora/DynamoDB); OLAP means scanning and aggregating huge numbers of rows across few columns (column-oriented, Redshift).

---

# 2. Amazon RDS

## 2.1 Core concepts

A managed relational database: AWS handles provisioning, OS and engine patching, backups, monitoring, and failover. You remain responsible for schema design, query tuning, indexes, and parameter settings.

- **Instance classes** follow EC2 families: `db.t` (burstable), `db.m` (general), `db.r`/`db.x` (memory optimized). Graviton (`g`) classes give better price/performance.
- **Storage:** gp3 (general purpose SSD), io1/io2 (provisioned IOPS, up to 256,000 with io2 Block Express on supported engines), magnetic (legacy). **Storage autoscaling** grows the volume automatically when free space runs low.
- **Parameter groups** control engine settings (`max_connections`, buffer pool size, query cache, logging); some parameters are static and require a reboot. **Option groups** add engine features (Oracle TDE, SQL Server Audit).
- **Maintenance and backup windows** define when patching and backups occur; with Multi-AZ these are applied to the standby first.

## 2.2 Performance features

**Read replicas** — asynchronous copies that serve read traffic:
- Up to **5 per source** (15 for Aurora), in the same AZ, another AZ, or **another Region**
- **Eventually consistent** — never use when read-after-write consistency is required
- Can be promoted to a standalone database
- Each replica has its own endpoint; the application must be written to route reads to them (or use a proxy/Aurora reader endpoint)

**Multi-AZ** is for availability, not performance — **the standby serves no traffic** in the classic instance deployment. (The newer **Multi-AZ DB cluster** has two *readable* standbys and failover in under 35 seconds.)

**Amazon RDS Proxy** — a managed connection pool that:
- Multiplexes thousands of application connections onto a small number of database connections, solving **connection exhaustion** from Lambda and container fleets
- **Reduces failover time by up to 66%** by holding client connections while re-pointing to the new writer
- Supports **IAM authentication** and **Secrets Manager** credentials, and never exposes database credentials to the application

**Performance Insights** — a visual database load dashboard showing **average active sessions** broken down by wait event, SQL statement, host, and user. This is the tool for answering "which query is causing the load?" Retains 7 days free, up to 2 years paid.

**Enhanced Monitoring** — OS-level metrics (per-process CPU, memory, file system, disk I/O) at up to 1-second granularity, which standard CloudWatch metrics (hypervisor level) cannot provide.

**Other tuning levers:** right-size the instance class; use **gp3 or io2** with adequate IOPS; add indexes; use **connection pooling**; offload reads to replicas; cache in **ElastiCache**; partition large tables; archive cold data to S3.

---

# 3. Amazon Aurora

## 3.1 Architecture

Aurora is a cloud-native reimplementation of MySQL and PostgreSQL that separates compute from a distributed, log-structured storage layer.

- Storage keeps **six copies across three Availability Zones**, is self-healing, and grows automatically in 10 GB increments to **128 TiB**.
- Aurora tolerates the loss of **two copies for writes** and **three copies for reads** with no availability impact.
- Claimed performance: up to **5× MySQL** and **3× PostgreSQL** throughput on the same hardware, achieved largely by sending only redo log records to storage rather than full pages.
- Up to **15 Aurora Replicas** sharing the same storage, so replicas add no write overhead and lag is typically **under 10 ms**. Failover to a replica normally completes in **under 30 seconds**.

## 3.2 Endpoints

- **Cluster (writer) endpoint** — always points to the current primary; follows failover automatically
- **Reader endpoint** — DNS round-robins across all available replicas
- **Custom endpoints** — a subset of instances (e.g., route reporting queries to larger instances)
- **Instance endpoints** — a specific instance, for diagnostics

## 3.3 Aurora features

- **Aurora Serverless v2** — scales **in-place, in fine-grained increments** of Aurora Capacity Units (0.5 ACU steps, from 0.5 to 256 ACUs) in **under a second**, supports read replicas, Multi-AZ, and Global Database, and can be mixed with provisioned instances in one cluster. Ideal for **variable, unpredictable, or intermittent** workloads, dev/test, and multi-tenant SaaS. (v1 scaled by pausing and jumping between capacity points, with a connection interruption — v2 removed that.)
- **Aurora Global Database** — one primary Region and up to **five secondaries**, storage-level replication with typical lag **under one second**, **RPO ≈ 1 s / RTO < 1 min**, plus low-latency local reads and optional **write forwarding** from secondaries.
- **Backtrack** (Aurora MySQL) — rewind the cluster in place to a previous point in seconds without restoring from a snapshot. Perfect for undoing an accidental `DELETE` or a bad deployment.
- **Fast database cloning** — copy-on-write clones created in minutes, using almost no extra storage initially. Ideal for test environments on production-sized data.
- **Aurora Machine Learning** — call SageMaker/Comprehend from SQL.
- **Babelfish for Aurora PostgreSQL** — understands the SQL Server TDS protocol and T-SQL, so SQL Server applications can migrate with minimal code change.
- **Aurora I/O-Optimized** — a cluster configuration with no per-I/O charge; cheaper and more predictable when I/O spend exceeds ~25% of the bill.
- **Zero-ETL integration with Redshift** — near-real-time analytics on Aurora data without building pipelines.

## 3.4 Aurora vs RDS

Choose **Aurora** for higher performance, 15 low-lag replicas, faster failover, auto-scaling storage, Global Database, Backtrack, cloning, and Serverless v2. Choose **RDS** when you need an engine Aurora doesn't offer (Oracle, SQL Server, Db2, MariaDB), when the workload is small and cost-sensitive (a `db.t4g` RDS instance is cheaper than the smallest practical Aurora setup), or when you need specific engine versions/features.

---

# 4. Amazon DynamoDB

## 4.1 Data model and keys

- A **table** holds **items** (rows), each with **attributes**. Items can have different attributes — the schema is flexible apart from the key.
- **Primary key** is either:
  - **Partition key only** (simple) — must be unique
  - **Partition key + sort key** (composite) — the combination must be unique, and items with the same partition key are stored together, sorted by sort key, enabling efficient range queries
- The **partition key is hashed** to decide which physical partition stores the item. **Choosing a high-cardinality, evenly-accessed partition key is the single most important performance decision.** A low-cardinality key (e.g., `status = "active"`) creates a **hot partition** and throttling.
- Item size limit **400 KB** — store large blobs in S3 and keep the pointer in DynamoDB.

## 4.2 Capacity modes

| Mode | How you pay | Best for |
|---|---|---|
| **On-demand** | Per request (read/write request units) | Unpredictable or spiky traffic, new applications, dev/test, infrequent use; **no capacity planning**; instantly accommodates spikes |
| **Provisioned** | Per hour for provisioned **RCU/WCU**, with optional **auto scaling** | Predictable, steady traffic; **cheaper at consistent high utilization**; can be combined with **reserved capacity** for further savings |

**Capacity units:**
- 1 **WCU** = one write of up to **1 KB** per second
- 1 **RCU** = one **strongly consistent** read of up to **4 KB** per second, or **two eventually consistent** reads of up to 4 KB per second
- Transactional reads/writes consume **double**

**Burst capacity** holds up to 5 minutes of unused capacity; **adaptive capacity** automatically shifts throughput toward hot partitions and isolates frequently accessed items, which mitigates but does not eliminate bad key design.

## 4.3 Reads, queries and indexes

- **GetItem** — retrieve one item by full primary key (fastest, cheapest)
- **Query** — retrieve items sharing a partition key, optionally filtered by sort key conditions. **Efficient.**
- **Scan** — reads the **entire table** then filters. **Expensive and slow**; use only for small tables or infrequent full exports. Mitigate with parallel scans and projections, but the real fix is usually a **GSI** so you can `Query` instead.
- **Consistency:** eventually consistent by default (cheaper, lower latency); strongly consistent reads cost double and are not available on GSIs.

**Secondary indexes:**

| | **Local Secondary Index (LSI)** | **Global Secondary Index (GSI)** |
|---|---|---|
| Key | **Same partition key**, different sort key | **Any** partition and sort key |
| When created | **Only at table creation** | Any time, and deletable |
| Limit | 5 per table | 20 per table (soft) |
| Capacity | Shares the table's capacity | **Its own** RCU/WCU |
| Consistency | Supports strongly consistent reads | **Eventually consistent only** |
| Size | 10 GB limit per partition key value | No limit |

**Exam cue:** "query on a non-key attribute" → **GSI**. If a GSI is throttled, it can **throttle writes on the base table** — size GSI capacity appropriately and project only the attributes you need.

## 4.4 DynamoDB Accelerator (DAX)

A fully managed, in-memory cache **purpose-built for DynamoDB**:
- Reduces read latency from single-digit **milliseconds** to **microseconds**
- **API-compatible** — point the DAX client at the cluster; no application rewrite of the data access logic
- Caches both item responses and query/scan results
- Runs inside your VPC as a multi-node cluster
- **Only helps reads**, and is eventually consistent (strongly consistent reads pass through to DynamoDB)

If a question says "microsecond reads for DynamoDB with minimal application changes," the answer is **DAX**, not ElastiCache.

## 4.5 Other DynamoDB capabilities

- **DynamoDB Streams** — an ordered, 24-hour change log of item-level modifications, consumed by Lambda or KCL. Powers event-driven architectures, aggregation, replication, and audit.
- **Global tables** — multi-Region, **multi-active** replication with last-writer-wins conflict resolution, typically sub-second.
- **TTL** — automatically delete expired items at no cost (perfect for sessions, temporary data, and keeping tables small).
- **Point-in-time recovery** (any second in the last 35 days) and on-demand backups.
- **Transactions** — ACID across up to 100 items/multiple tables.
- **Export to S3** (no capacity consumed) for analytics with Athena, and **zero-ETL to Redshift/OpenSearch**.
- **Standard-IA table class** for tables where storage dominates cost over throughput.
- **Fine-grained access control** with `dynamodb:LeadingKeys` so a user can only access items whose partition key matches their identity.

---

# 5. Caching Layers

## 5.1 ElastiCache: Redis/Valkey vs Memcached

| | **Redis / Valkey** | **Memcached** |
|---|---|---|
| Data structures | Strings, lists, sets, sorted sets, hashes, bitmaps, HyperLogLog, streams, geospatial | Simple key-value strings only |
| Persistence | **Yes** (snapshots, AOF) | No |
| Replication / HA | **Replicas + Multi-AZ with automatic failover** | None |
| Scaling | Read replicas; **cluster mode** shards across up to 500 nodes | **Horizontal** — add nodes, client-side sharding |
| Multi-threaded | Mostly single-threaded (Valkey/Redis 7+ improves this) | **Multi-threaded** |
| Extras | Pub/sub, Lua scripting, transactions, **sorted sets for leaderboards**, geospatial queries | Pure, simple, very fast cache |

**Choose Redis** when you need persistence, HA, replication, or rich data structures (leaderboards, rate limiting, pub/sub, session store with failover). **Choose Memcached** for a simple, multi-threaded, horizontally scalable object cache where losing the cache is harmless.

**Amazon MemoryDB for Redis** is a *durable* Redis-compatible **primary database** with multi-AZ transaction-log durability — use it when Redis is the system of record, not just a cache.

## 5.2 Caching strategies

- **Lazy loading (cache-aside)** — check the cache; on a miss, read the database and populate the cache. Only requested data is cached and a cache failure is survivable, but misses cost extra latency and data can go stale.
- **Write-through** — write to the cache whenever you write to the database. Data is never stale and reads are fast, but writes are slower and the cache holds data that may never be read.
- **TTL** — bound staleness regardless of strategy.
- **Write-behind** — buffer writes and flush asynchronously (risk of loss).
- **Typical answer:** lazy loading + TTL, with write-through for hot keys.

**Cache problems to recognize:**
- **Thundering herd / cache stampede** — a popular key expires and thousands of requests hit the database at once. Mitigate with jittered TTLs, request coalescing, or pre-warming.
- **Hot key** — one key receives disproportionate traffic. Mitigate by replicating the key across shards or adding a local in-process cache.
- **Eviction** — when memory fills, Redis applies a maxmemory policy (`allkeys-lru` is common for caches). Watch the `Evictions` metric; rising evictions mean you need a bigger node.

## 5.3 Where caching fits

| Layer | Service |
|---|---|
| Edge/static + dynamic HTTP | **CloudFront** |
| API responses | **API Gateway caching** |
| Application/session/query results | **ElastiCache** |
| DynamoDB reads | **DAX** |
| Relational read scaling | **Read replicas** |
| DNS | Route 53 TTL |

---

# 6. Analytics and Search Data Stores

## 6.1 Amazon Redshift

A petabyte-scale, **columnar, massively parallel processing** data warehouse.

- **Architecture:** a leader node plans queries and distributes work to compute nodes, which are divided into slices. **RA3 nodes** with **managed storage** separate compute from storage (data lives in S3, hot data is cached locally), so you scale each independently.
- **Distribution styles** decide how rows are spread across slices: **KEY** (co-locate rows that join on the same column), **ALL** (replicate a small dimension table to every node to avoid shuffles), **EVEN** (round-robin), **AUTO** (Redshift decides). Bad distribution causes data shuffling and slow joins.
- **Sort keys** (compound or interleaved) let Redshift skip blocks using zone maps, hugely reducing I/O for range-restricted queries.
- **Redshift Spectrum** queries data directly in S3 without loading it, so you keep hot data in the cluster and cold data in the lake.
- **Concurrency Scaling** adds transient clusters automatically during bursts of queries.
- **Materialized views**, **result caching**, **workload management (WLM)** queues, and **AQUA** for acceleration.
- **Redshift Serverless** removes cluster management entirely and bills per RPU-second.
- **Zero-ETL integrations** from Aurora, RDS MySQL, and DynamoDB.

**Redshift is not an OLTP database** — it is poor at single-row lookups and high-frequency small writes.

## 6.2 Athena vs Redshift vs EMR

| | **Athena** | **Redshift** | **EMR** |
|---|---|---|---|
| Model | Serverless SQL over S3 (Presto/Trino) | Provisioned/serverless MPP warehouse | Managed Hadoop/Spark clusters |
| Pay for | **Data scanned** ($5/TB) | Cluster hours or RPU | Cluster hours |
| Best for | Ad-hoc queries, infrequent analysis, log analysis | Repeated complex BI queries, dashboards, joins across large tables | Custom code, ML, non-SQL processing, huge ETL |
| Optimization | **Partition, compress, and convert to Parquet/ORC** | Distribution keys, sort keys, compression | Instance/fleet tuning, Spot task nodes |

## 6.3 Amazon OpenSearch Service

Managed OpenSearch/Elasticsearch for **full-text search** and **log analytics**, with OpenSearch Dashboards for visualization.
- Deploy across 3 AZs with dedicated master nodes for production.
- **UltraWarm** and **Cold storage** tiers back by S3 cut the cost of older indices dramatically.
- **Index State Management** automates rollover and tier transitions.
- **OpenSearch Serverless** for variable workloads.
- Typical pipeline: application/VPC/CloudFront logs → Kinesis Data Firehose / OpenSearch Ingestion → OpenSearch → Dashboards.

---

# 7. Migration and Schema Conversion

- **AWS Database Migration Service (DMS)** — migrates databases with **minimal downtime** using full load plus **change data capture (CDC)**. Supports homogeneous (Oracle→Oracle) and heterogeneous (Oracle→Aurora PostgreSQL) migrations, and targets including S3, Kinesis, OpenSearch, Redshift, and DocumentDB. DMS Serverless removes replication-instance sizing.
- **AWS Schema Conversion Tool (SCT)** — converts schema, stored procedures, and application SQL between different engines; produces an assessment report listing what cannot be converted automatically. Use **SCT + DMS** together for heterogeneous migrations.
- **Babelfish** — lets SQL Server applications talk to Aurora PostgreSQL with little or no code change.
- **AWS DataSync / Snowball** for very large offline data movement feeding a migration.

---

# 8. Worked Scenarios

**Scenario 1 — "Read traffic has grown 10×; writes are unchanged; the RDS primary is saturated."**
Add **read replicas** and route reads to them; add **ElastiCache** for repeated queries. Multi-AZ would not help — the standby serves no traffic.

**Scenario 2 — "We need microsecond reads from DynamoDB without rewriting the data layer."**
**DAX.**

**Scenario 3 — "A DynamoDB table throttles even though provisioned capacity looks adequate overall."**
A **hot partition** from a low-cardinality partition key. Redesign the key (add a suffix/shard, use a high-cardinality attribute), or switch to **on-demand**. Also check whether a GSI is the throttled resource.

**Scenario 4 — "The application queries a non-key attribute and the scan is too slow."**
Create a **GSI** on that attribute and use `Query`.

**Scenario 5 — "Traffic is completely unpredictable and we don't want to manage capacity."**
**DynamoDB on-demand**, or **Aurora Serverless v2** for relational.

**Scenario 6 — "Global users need low-latency reads and writes to the same dataset."**
**DynamoDB global tables** (multi-active), or **Aurora Global Database** with write forwarding for relational.

**Scenario 7 — "Thousands of Lambda functions exhaust database connections."**
**RDS Proxy.**

**Scenario 8 — "Analysts run complex joins across billions of rows and the RDS instance can't cope."**
Move analytics to **Redshift** (or Athena over S3 if queries are ad hoc and infrequent), keeping RDS for OLTP.

**Scenario 9 — "Find all users within three degrees of connection who purchased a product."**
**Amazon Neptune.**

**Scenario 10 — "Migrate an on-prem Oracle database to Aurora PostgreSQL with minimal downtime."**
**SCT** to convert the schema, **DMS** with CDC for the data and ongoing changes, then cut over.

**Scenario 11 — "Session data needs sub-millisecond access and must survive a node failure."**
**ElastiCache for Redis** with Multi-AZ and automatic failover (or **MemoryDB** if it must be durable as a primary store).

**Scenario 12 — "We need to undo an accidental mass delete in Aurora MySQL immediately."**
**Backtrack.**

---

# 9. Quick Decision Table

| Requirement | Answer |
|---|---|
| Relational, managed, standard engines | **Amazon RDS** |
| Relational with high performance, 15 replicas, fast failover | **Amazon Aurora** |
| Relational with unpredictable load, no capacity management | **Aurora Serverless v2** |
| Global relational, RPO ~1 s | **Aurora Global Database** |
| Undo a bad write in seconds (Aurora MySQL) | **Backtrack** |
| Clone production data for test quickly and cheaply | **Aurora fast database cloning** |
| Key-value at any scale, single-digit ms | **DynamoDB** |
| Microsecond DynamoDB reads | **DAX** |
| Query a non-key attribute | **Global Secondary Index** |
| Same partition key, alternate sort key, strong consistency | **Local Secondary Index** (table creation only) |
| Auto-delete expired items | **DynamoDB TTL** |
| React to item changes | **DynamoDB Streams → Lambda** |
| Multi-Region active-active NoSQL | **Global tables** |
| Caching with data structures, persistence, HA | **ElastiCache for Redis** |
| Simple, multi-threaded object cache | **ElastiCache for Memcached** |
| Durable Redis as a primary database | **MemoryDB** |
| MongoDB-compatible | **DocumentDB** |
| Cassandra-compatible | **Keyspaces** |
| Relationship/graph queries | **Neptune** |
| Time-series IoT metrics | **Timestream** |
| Immutable, verifiable audit ledger | **QLDB** |
| Complex BI over terabytes | **Redshift** |
| Ad-hoc SQL over S3, pay per query | **Athena** |
| Query S3 from the warehouse | **Redshift Spectrum** |
| Full-text search / log analytics | **OpenSearch Service** |
| Connection pooling and faster failover | **RDS Proxy** |
| Find the SQL causing database load | **Performance Insights** |
| OS-level DB metrics at 1-second granularity | **Enhanced Monitoring** |
| Migrate with minimal downtime | **DMS (+ SCT for heterogeneous)** |
| Run SQL Server apps on Aurora PostgreSQL | **Babelfish** |
