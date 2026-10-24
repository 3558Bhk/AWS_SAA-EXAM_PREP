# Task 4.3 — Design Cost-Optimized Database Solutions

> Database cost comes from four places: **instance hours**, **storage and I/O**, **backups and snapshots**, and **data transfer**. The exam tests whether you can pick the cheapest *appropriate* engine, size it correctly, commit where usage is steady, and move cold data out of expensive storage.

---

# 1. Where Database Cost Comes From

| Cost dimension | Applies to | How to reduce it |
|---|---|---|
| **Instance hours** | RDS, Aurora provisioned, ElastiCache, Redshift, DocumentDB, Neptune, OpenSearch | Right-size, use Graviton, stop non-prod, commit with Reserved Instances, use serverless for variable load |
| **Storage (GB-month)** | All | Archive cold data to S3, delete unused data, use TTL, choose the right storage type |
| **I/O operations** | Aurora (standard config), RDS with io1/io2, DynamoDB RCU/WCU | Aurora **I/O-Optimized**, caching, efficient queries, right capacity mode |
| **Provisioned throughput** | DynamoDB provisioned | Auto scaling, reserved capacity, or on-demand for spiky load |
| **Backups and snapshots** | All | Shorter retention, delete manual snapshots, export to S3 |
| **Data transfer** | Cross-AZ, cross-Region, internet | Co-locate, avoid unnecessary cross-Region replicas |
| **Licences** | RDS Oracle/SQL Server | BYOL, Optimize CPU options, migrate to open-source engines |

---

# 2. Choosing the Cheapest Appropriate Engine

**The cheapest database is often not a database at all.** Before sizing anything, ask whether the data belongs somewhere cheaper:

| If the data is… | Put it in… |
|---|---|
| Large files or blobs | **S3** (with the pointer in the database) |
| Rarely queried historical records | **S3 + Athena** (pennies per GB vs database storage) |
| Session or temporary state | **DynamoDB with TTL** or **ElastiCache** |
| Logs | **CloudWatch Logs** (with retention set) or **S3 + Athena**, not a relational table |
| Simple key-value lookups at scale | **DynamoDB** rather than an over-provisioned RDS instance |
| Analytics | **Redshift or Athena**, not an oversized OLTP instance |

**Engine selection economics:**
- **DynamoDB on-demand** can be far cheaper than a small always-on RDS instance for low or spiky traffic — and it scales to zero cost when idle.
- **Aurora Serverless v2** suits variable or intermittent relational workloads, scaling in 0.5-ACU increments.
- **RDS on a `db.t4g` burstable Graviton instance** is the cheapest managed relational option for small, bursty workloads.
- **Open-source engines (MySQL, PostgreSQL, MariaDB)** avoid the licence costs of Oracle and SQL Server. **Babelfish** lets SQL Server applications run on Aurora PostgreSQL with minimal change; **SCT + DMS** handles the heavier migrations.
- **Self-managed databases on EC2** are usually *more* expensive in total than RDS once you count instances, storage, backup tooling, HA design, and administration — choose EC2 only when you need OS access or an unsupported engine/version.

---

# 3. Cost-Optimizing RDS and Aurora

## 3.1 Instance sizing and commitments

- **Right-size** with **Compute Optimizer for RDS**, **Performance Insights** (is the load real or is it a bad query?), and CloudWatch metrics. Many production databases run at single-digit CPU.
- **Graviton (`db.*g`) instance classes** give better price/performance at a lower hourly rate — often a 20%+ saving for a version upgrade and a reboot.
- **Burstable `db.t4g`** classes are cheap for dev/test and small workloads, but watch CPU credits for sustained load.
- **Reserved Instances** for RDS: 1 or 3 years, up to **~69%** off. Note that **Savings Plans do not cover RDS** — RIs are the only commitment mechanism (same for ElastiCache, Redshift, OpenSearch, and DynamoDB reserved capacity).
- **Stop non-production databases.** An RDS instance can be stopped for up to **7 days** (it restarts automatically after that), which still saves meaningfully; alternatively snapshot and delete, restoring when needed. Aurora Serverless v2 can scale down to a minimal ACU instead.

## 3.2 Storage and I/O

- **gp3** is the default and cheapest general-purpose RDS storage; use **io1/io2** only when you genuinely need provisioned IOPS, because provisioned IOPS carry a significant premium.
- **Storage autoscaling** avoids over-provisioning up front — but note storage **can only grow**, never shrink, so over-allocating is permanent until you migrate.
- **Aurora I/O-Optimized** removes per-I/O charges for a higher instance/storage rate. It becomes cheaper when **I/O exceeds roughly 25% of the cluster's total spend** — typical of write-heavy or scan-heavy workloads. Aurora **Standard** is cheaper for low-I/O workloads.
- **Aurora storage auto-grows and auto-shrinks**, and you pay only for what is used — unlike RDS, where allocated storage is billed whether used or not.

## 3.3 Multi-AZ and replicas

- **Multi-AZ roughly doubles the instance cost.** It is essential for production, but it is pure waste on dev/test environments — a frequent, easy saving.
- Each **read replica** is a full-priced instance. Add them only when read load genuinely requires it, and consider **ElastiCache** first: a cache node is often cheaper than a replica and removes far more load.
- **Cross-Region read replicas** add instance cost **plus cross-Region data transfer**. Use only where a business requirement (DR or local latency) justifies it.

## 3.4 Backups and snapshots

- **Automated backup storage equal to the database size is free**; beyond that you pay per GB-month. Keep retention to what you actually need (1–35 days).
- **Manual snapshots persist until you delete them** — and they survive the deletion of the database instance. Orphaned manual snapshots are a classic silent cost. Audit and delete them.
- **Export snapshots to S3 in Parquet** for long-term retention at object-storage prices and query them with Athena, instead of paying database-snapshot rates.
- **Cross-Region snapshot copies** double storage cost and add transfer cost.

## 3.5 Other levers

- **Archive cold rows to S3** and query with Athena or Redshift Spectrum; keep the OLTP database small and fast.
- **Caching with ElastiCache** reduces the instance size you need and may let you drop replicas.
- **RDS Proxy** reduces connection overhead so a smaller instance can handle the same application fleet (it does have its own per-vCPU charge, so weigh it).
- **Fix inefficient queries and add indexes** — a missing index is often the real reason someone wants a bigger instance.
- **Licence optimization:** BYOL on Dedicated Hosts, **Optimize CPU options** to reduce licensed cores, or migrate to open source.

---

# 4. Cost-Optimizing DynamoDB

## 4.1 Capacity mode is the biggest decision

| Mode | Billing | Cheapest when |
|---|---|---|
| **On-demand** | Per read/write request unit | Traffic is **spiky, unpredictable, low, or intermittent**; new applications; dev/test. Costs nothing when idle. |
| **Provisioned** | Per hour of provisioned RCU/WCU | Traffic is **steady and predictable** with high utilization — can be ~6–7× cheaper per request than on-demand at consistent load |

Rules of thumb: if average utilization of provisioned capacity would be **below ~15–20%**, on-demand is usually cheaper. If you can keep utilization high with **auto scaling** (target ~70%), provisioned wins. You can switch modes (once every 24 hours).

**Further provisioned savings:** **DynamoDB reserved capacity** (1 or 3 years) gives up to ~77% off provisioned throughput for predictable baselines.

## 4.2 Design choices that cut cost

- **Avoid `Scan`.** A scan reads the entire table and bills for it. Use `Query` with a well-chosen key, or create a **GSI** so you can query instead.
- **Eventually consistent reads cost half** of strongly consistent reads. Use them wherever the application tolerates it.
- **Project only needed attributes** into GSIs — a GSI with `ALL` projection duplicates the whole table's storage and write cost. `KEYS_ONLY` or `INCLUDE` is often enough.
- **Every GSI multiplies write cost** — each write to the base table also writes to each affected index. Delete unused indexes.
- **Keep items small.** WCUs are billed per 1 KB and RCUs per 4 KB, so trimming attribute names and moving blobs to S3 directly reduces consumed capacity.
- **TTL deletes expired items for free** — far cheaper than issuing delete requests, and it keeps storage and scan costs down.
- **DynamoDB Standard-IA table class** cuts storage cost ~60% (with higher request costs) for tables where **storage dominates** — archives, logs, old orders.
- **DAX** reduces read capacity consumption for repeated reads; weigh the cluster cost against RCU savings.
- **Export to S3** for analytics consumes **no read capacity** — never run analytical scans against the live table.
- **Global tables** multiply cost by the number of Regions (plus replication traffic) — use only where multi-Region is required.

---

# 5. Cost-Optimizing Caching and Analytics Stores

**ElastiCache**
- **Reserved nodes** for steady workloads (up to ~55% off).
- **Right-size node types** and use **Graviton** nodes.
- **Redis cluster mode** lets you scale horizontally with smaller nodes rather than one oversized node.
- A cache is often cheaper than additional read replicas or a larger database instance — the saving appears on the *database* line.
- **Data tiering** (r6gd nodes) moves cold data to local NVMe for a much lower cost per GB on large Redis datasets.
- Delete idle dev/test clusters; they bill continuously.

**Amazon Redshift**
- **Reserved nodes** for steady clusters (up to ~75% off).
- **RA3 + managed storage** separates compute and storage, so you stop paying for compute just to hold data.
- **Pause and resume** clusters (or **Redshift Serverless**) for intermittent analytics — Serverless bills per RPU-second with no idle cost.
- **Redshift Spectrum** keeps cold data in S3 and queries it in place, instead of loading everything into the cluster.
- **Concurrency Scaling** earns free credits (one hour per day per cluster), making burst handling cheap.
- **Compression encodings** and good **sort/distribution keys** reduce the storage and compute needed.

**Amazon OpenSearch**
- **UltraWarm** and **Cold storage** tiers (backed by S3) cut the cost of older indices by up to 90%.
- **Index State Management** automates rollover and tier transitions.
- **Reserved Instances** for steady clusters; **OpenSearch Serverless** for variable workloads.
- Set realistic retention — most log data has no value after 30 days in hot storage.

**Amazon Athena**
- Billed at **~$5 per TB scanned**, so cost control *is* scan reduction: **Parquet/ORC, compression, partitioning, selecting fewer columns**, and compacting small files. Use **workgroup data-scan limits** to prevent runaway queries.

---

# 6. Data Lifecycle for Databases

A disciplined lifecycle is often the largest database saving available:

```
Hot (0–90 days)      → RDS/Aurora/DynamoDB      — fast, expensive
Warm (90 days–1 yr)  → S3 Standard / Redshift   — queryable, cheaper
Cold (1–7 years)     → S3 Glacier classes       — archival, cheapest
Expired              → deleted                   — free
```

Mechanisms: **DynamoDB TTL**, scheduled archive jobs writing Parquet to S3, **RDS snapshot export to S3**, **DynamoDB export to S3**, **Redshift unload to S3**, and S3 lifecycle rules moving the archived data onward to Glacier.

---

# 7. Worked Scenarios

**Scenario 1 — "Our RDS database runs 24/7 at 8% CPU with Multi-AZ on a dev account."**
Right-size the instance class (Compute Optimizer), move to **Graviton**, **disable Multi-AZ on dev**, and **stop the instance outside working hours**.

**Scenario 2 — "A DynamoDB table is provisioned at 10,000 RCU/WCU but averages 400."**
Enable **auto scaling** targeting ~70% utilization, or switch to **on-demand** if the pattern is genuinely spiky. Consider **reserved capacity** for the steady baseline.

**Scenario 3 — "A new application has unpredictable traffic and we don't want to plan capacity."**
**DynamoDB on-demand**, or **Aurora Serverless v2** for relational.

**Scenario 4 — "Reporting queries are hammering the production database and someone proposes a bigger instance."**
Add **ElastiCache** for repeated queries and/or a **read replica**, or move analytics to **Redshift/Athena**. Scaling the OLTP instance up is the expensive answer.

**Scenario 5 — "Our Aurora bill shows enormous I/O charges."**
Switch the cluster to **Aurora I/O-Optimized** (worth it above ~25% I/O spend), add caching, and tune queries that scan excessively.

**Scenario 6 — "Seven years of order history sits in RDS but only the last 90 days is queried."**
Archive older rows to **S3 as Parquet**, query with **Athena** (or **Redshift Spectrum**), and shrink the database. Apply S3 lifecycle rules to Glacier afterwards.

**Scenario 7 — "We pay heavily for SQL Server licences on RDS."**
Migrate to **Aurora PostgreSQL with Babelfish** (minimal application change) or use **SCT + DMS**; alternatively BYOL on Dedicated Hosts or **Optimize CPU options**.

**Scenario 8 — "Our OpenSearch cluster keeps 2 years of logs in hot storage."**
Apply **Index State Management** to roll indices into **UltraWarm** then **Cold**, and archive to S3 with a defined retention policy.

**Scenario 9 — "Analytics runs once a week but the Redshift cluster bills continuously."**
**Pause/resume** the cluster, or move to **Redshift Serverless**, or query S3 directly with **Athena**.

**Scenario 10 — "Session data in RDS is causing high write load and cost."**
Move sessions to **DynamoDB with TTL** or **ElastiCache** — cheaper, faster, and self-expiring.

---

# 8. Quick Decision Table

| Scenario | Answer |
|---|---|
| Steady relational workload, 1–3 years | **RDS/Aurora Reserved Instances** (Savings Plans don't cover RDS) |
| Variable relational workload | **Aurora Serverless v2** |
| Small, bursty relational workload | **`db.t4g` Graviton burstable** |
| Better price/performance, same engine | **Graviton DB instance classes** |
| Dev/test database running 24/7 | **Stop it** (up to 7 days) / snapshot and delete; disable Multi-AZ |
| High Aurora I/O charges | **Aurora I/O-Optimized** |
| Spiky or unknown NoSQL traffic | **DynamoDB on-demand** |
| Steady, predictable NoSQL traffic | **DynamoDB provisioned + auto scaling (+ reserved capacity)** |
| Expensive table scans | **GSI + Query**, never `Scan` |
| Halve read cost | **Eventually consistent reads** |
| Storage-heavy, rarely read DynamoDB table | **Standard-IA table class** |
| Expire old items for free | **DynamoDB TTL** |
| Reduce GSI write amplification | **Project only needed attributes / delete unused GSIs** |
| Analytics on DynamoDB without consuming capacity | **Export to S3 + Athena** |
| Repeated identical queries | **ElastiCache** (cheaper than more replicas) |
| Steady cache workload | **ElastiCache reserved nodes** |
| Large Redis dataset, cost-sensitive | **Data tiering (r6gd)** |
| Intermittent analytics | **Redshift pause/resume or Serverless; Athena** |
| Keep cold warehouse data cheap | **Redshift Spectrum / RA3 managed storage** |
| Old log indices costing too much | **OpenSearch UltraWarm / Cold + ISM** |
| Reduce Athena cost | **Parquet + compression + partitioning** |
| Archive cold database rows | **Export to S3 (Parquet) + lifecycle to Glacier** |
| Orphaned manual snapshots | **Audit and delete; export to S3 instead** |
| Oracle/SQL Server licence cost | **Migrate to Aurora (SCT/DMS/Babelfish)** or **BYOL + Optimize CPU** |
| Blobs stored in the database | **Move to S3, keep the pointer** |
