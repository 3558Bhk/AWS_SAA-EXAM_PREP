# Task 3.1 — Determine High-Performing and/or Scalable Storage Solutions

> The exam tests whether you can match a workload description to the correct storage service and configuration. Almost every question reduces to three questions: **object, file, or block? how much throughput/IOPS/latency? how is it accessed and by how many clients?**

---

# 1. The Three Storage Types

| | **Object** | **File** | **Block** |
|---|---|---|---|
| Services | S3, S3 Glacier | EFS, FSx (Windows / Lustre / ONTAP / OpenZFS) | EBS, Instance store |
| Access | HTTP(S) API (GET/PUT), flat namespace with key prefixes | NFS / SMB mount, hierarchical directories, POSIX or NTFS permissions | Raw block device, you format it with a file system |
| Concurrency | Massive — any number of clients | Many clients simultaneously | Normally **one instance** (EBS Multi-Attach is the exception) |
| Update semantics | Whole-object replace (no partial in-place writes) | Partial file writes, locking, metadata | Random block-level reads/writes |
| Scale | Effectively unlimited | Petabytes, elastic | Per-volume limit (64 TiB) |
| Typical use | Static assets, backups, data lakes, media, logs | Shared content, home directories, HPC, lift-and-shift | Boot volumes, databases, transactional workloads |

**Decision shortcut:**
- "Many servers need to read/write the same files with normal file-system semantics" → **file (EFS or FSx)**
- "One server needs a fast disk for a database" → **block (EBS)**
- "Store and retrieve lots of unstructured data over HTTP at any scale" → **object (S3)**

---

# 2. Amazon S3 in Depth

## 2.1 Fundamentals

- **Unlimited total capacity.** Individual objects range from **0 bytes to 5 TB**. A single `PUT` can upload up to **5 GB**; above that you must use **multipart upload** (and AWS recommends it above ~100 MB).
- **Durability 99.999999999% (11 nines)** by storing data redundantly across **at least three Availability Zones** (except One Zone classes). Availability for S3 Standard is **99.99%**.
- **Strong read-after-write consistency** for all operations — PUTs, overwrites, deletes, and list operations — at no cost and with no performance penalty.
- Flat namespace: there are no real folders. `reports/2026/q1.csv` is just a key; the console displays it as folders. **Prefixes** matter for performance (see below).

## 2.2 Performance characteristics and how to scale

**Request rates:** S3 supports at least **3,500 PUT/COPY/POST/DELETE** and **5,500 GET/HEAD** requests per second **per partitioned prefix**. There is **no limit on the number of prefixes**, so request capacity scales horizontally: splitting objects across 10 prefixes gives roughly 35,000 writes/second and 55,000 reads/second.

If an application receives `503 Slow Down` responses, the fix is to **spread keys across more prefixes** (for example `logs/01/...` through `logs/20/...`), not to request a quota increase. S3 also auto-partitions over time, but that takes a while to adapt.

**Multipart upload** — splits an object into parts uploaded in parallel:
- Required above 5 GB, recommended above ~100 MB
- **Faster** (parallelism), **more resilient** (retry just a failed part), and **resumable**
- Always add a lifecycle rule to **abort incomplete multipart uploads** after N days, or you pay for orphaned parts forever

**Byte-range fetches** — request specific byte ranges of an object in parallel to speed up downloads, or to read just a header/footer of a large file.

**S3 Transfer Acceleration** — clients upload to the nearest **CloudFront edge location** and the data travels to the bucket over the optimized AWS backbone. Helps when users are geographically distant from the bucket; it costs extra, and AWS provides a speed comparison tool to check whether it actually helps.

**S3 Select** — run simple SQL (`SELECT ... WHERE`) against a **single object** (CSV, JSON, Parquet, optionally GZIP/BZIP2) server-side, returning only matching rows/columns. Dramatically reduces data transferred and client-side processing. For queries across **many** objects, use **Athena** instead.

**S3 Express One Zone** — a high-performance, single-AZ storage class delivering **single-digit-millisecond** (up to 10× faster) access and very high request rates, designed for latency-sensitive analytics and ML workloads. Data is co-located with compute in one AZ, with higher request costs and lower storage cost than Standard.

## 2.3 Storage classes

| Class | First-byte latency | Min duration | Min billable size | AZs | Designed for |
|---|---|---|---|---|---|
| **S3 Standard** | ms | — | — | ≥3 | Frequently accessed, hot data |
| **S3 Intelligent-Tiering** | ms (Frequent / Infrequent / Archive Instant tiers) | — (small monitoring fee per object) | 128 KB for auto-tiering | ≥3 | **Unknown or changing access patterns** |
| **S3 Standard-IA** | ms | **30 days** | 128 KB | ≥3 | Infrequently accessed but needs instant retrieval |
| **S3 One Zone-IA** | ms | **30 days** | 128 KB | **1** | Re-creatable, infrequently accessed |
| **S3 Glacier Instant Retrieval** | **ms** | **90 days** | 128 KB | ≥3 | Archive accessed about once a quarter but needing instant access |
| **S3 Glacier Flexible Retrieval** | Expedited 1–5 min, Standard 3–5 h, Bulk 5–12 h | **90 days** | 40 KB | ≥3 | Archive, occasional retrieval |
| **S3 Glacier Deep Archive** | Standard 12 h, Bulk 48 h | **180 days** | 40 KB | ≥3 | Long-term compliance archive, cheapest |
| **S3 Express One Zone** | **single-digit ms** | — | — | 1 | Latency-critical, high-request workloads |

**Intelligent-Tiering tiers:** Frequent Access → Infrequent Access (after 30 days without access) → Archive Instant Access (after 90 days) → optional Archive Access (90+) and Deep Archive Access (180+). **No retrieval fees** for the automatic tiers, which is why it is the right answer for unpredictable patterns.

## 2.4 Lifecycle management

Lifecycle rules automate transitions and deletions, scoped by prefix, tag, or object size:
- **Transition actions** — move between storage classes as objects age
- **Expiration actions** — delete current versions, delete **noncurrent versions** after N days, remove **expired delete markers**, and **abort incomplete multipart uploads**

Constraints: objects must be at least 30 days old before moving from Standard to Standard-IA, and transitions can only move "down" the tier hierarchy. Use **S3 Storage Class Analysis** or **Storage Lens** to decide the thresholds.

## 2.5 Other capabilities worth knowing

- **Event notifications** → SNS, SQS, Lambda, or **EventBridge** (richer filtering) when objects are created, deleted, restored, or replicated.
- **S3 Access Points** — unique hostnames with their own policies per application; **Object Lambda Access Points** transform data on retrieval (redaction, format conversion) without duplicating it.
- **Multi-Region Access Points** — a single global endpoint that routes to the nearest bucket over the AWS backbone, with automatic failover.
- **S3 Batch Operations** — perform actions (copy, restore, tag, invoke Lambda, replicate) across billions of objects from a manifest or inventory report.
- **S3 Inventory** — scheduled CSV/ORC/Parquet reports of objects and metadata.
- **Storage Lens** — organization-wide usage and activity analytics with cost-optimization recommendations.
- **Requester Pays** — the requester pays for requests and transfer, used for large shared datasets.
- **Static website hosting**, **presigned URLs**, **CORS**.

---

# 3. Amazon EBS

## 3.1 Fundamentals

An EBS volume is a **network-attached block device** that lives in **one Availability Zone** and attaches to an EC2 instance in that AZ. It persists independently of the instance lifecycle (unless `DeleteOnTermination` is set on the root volume).

- Volumes can be **modified live** with **Elastic Volumes**: change size, type, IOPS, and throughput without detaching. You can **increase** size but never decrease it.
- Snapshots are **incremental**, stored durably, and can be copied across Regions and accounts.
- **io1/io2 support Multi-Attach** — the same volume attached to up to **16 instances in the same AZ**, which requires a **cluster-aware file system** (not ext4/XFS) to avoid corruption.

## 3.2 Volume types

| Type | Media | Size range | Max IOPS | Max throughput | Boot volume? | Best for |
|---|---|---|---|---|---|---|
| **gp3** | SSD | 1 GiB – 16 TiB | **16,000** (3,000 baseline, provisioned independently of size) | 1,000 MB/s (125 MB/s baseline) | Yes | **Default general purpose**; ~20% cheaper than gp2 |
| **gp2** | SSD | 1 GiB – 16 TiB | 3 IOPS/GiB (min 100, max 16,000), burst to 3,000 | 250 MB/s | Yes | Legacy general purpose |
| **io1** | SSD | 4 GiB – 16 TiB | 64,000 | 1,000 MB/s | Yes | I/O-intensive, Multi-Attach |
| **io2** | SSD | 4 GiB – 16 TiB | 64,000 (higher durability: 99.999%) | 1,000 MB/s | Yes | Critical databases |
| **io2 Block Express** | SSD | up to **64 TiB** | **256,000** | **4,000 MB/s** | Yes | Largest, most demanding databases (SAP HANA, Oracle) |
| **st1** | HDD | 125 GiB – 16 TiB | 500 | **500 MB/s** | **No** | **Throughput-oriented**: big data, log processing, data warehouses |
| **sc1** | HDD | 125 GiB – 16 TiB | 250 | 250 MB/s | **No** | Coldest data, lowest cost per GB |

**Exam-critical facts:**
- **HDD volumes (st1, sc1) cannot be boot volumes.**
- **gp3 decouples IOPS and throughput from capacity**, so you no longer have to over-provision a large volume just to get IOPS (the classic gp2 problem).
- Reaching high IOPS also requires an **EBS-optimized instance** with sufficient network bandwidth; the instance type can be the bottleneck.
- **IOPS vs throughput:** IOPS matters for small random I/O (databases, transactional workloads); throughput (MB/s) matters for large sequential I/O (log processing, ETL, streaming reads).
- **RAID 0** across multiple EBS volumes can increase aggregate IOPS/throughput beyond a single volume's limit (at the cost of resilience); RAID 1 adds redundancy but EBS is already replicated within the AZ.

## 3.3 Instance store

**Physically attached NVMe SSDs** on the host. Characteristics:
- **Highest possible IOPS and lowest latency** — millions of IOPS on storage-optimized instances, because there is no network hop.
- **Ephemeral:** data is lost when the instance **stops, hibernates, or terminates**, or if the underlying hardware fails. It survives a reboot.
- Cost is included in the instance price (no separate charge).
- Capacity and presence are fixed by the instance type.

Use for: caches, buffers, temporary scratch space, swap, and **replicated** datastores where the cluster provides durability (Cassandra, Scylla, Elasticsearch hot tier, Hadoop HDFS temp).

## 3.4 Snapshots and performance

- Snapshots are incremental: only changed blocks are stored, but each snapshot is independently restorable.
- **Volumes restored from a snapshot are lazily loaded** — the first read of each block fetches from S3, causing elevated latency initially. **Fast Snapshot Restore (FSR)** pre-provisions the volume so it delivers full performance immediately (billed per AZ per snapshot).
- **Data Lifecycle Manager (DLM)** or **AWS Backup** automate snapshot creation, retention, and cross-Region copying.
- **EBS Snapshot Archive** stores rarely needed snapshots up to 75% cheaper (90-day minimum, 24–72 hour restore).

---

# 4. Amazon EFS

## 4.1 What it is

A fully managed, elastic **NFS v4.1** file system for **Linux** workloads. It can be mounted concurrently by **thousands of clients** — EC2 instances across multiple AZs, ECS and EKS containers, **Lambda functions**, and on-premises servers over Direct Connect or VPN.

- **Elastic capacity** — grows and shrinks automatically as files are added and removed, to petabyte scale; you pay only for what you store.
- A **mount target** is created per AZ (an ENI with a private IP); clients mount using the DNS name and are routed to their local AZ's mount target.
- Access is controlled by **security groups**, **POSIX permissions**, an **EFS file system policy** (IAM resource policy), and **EFS Access Points** (which enforce a specific POSIX user/group and root directory per application — ideal for multi-tenant or container use).
- Encryption at rest (KMS, set at creation) and in transit (TLS via the EFS mount helper).

## 4.2 Performance and throughput modes

**Performance modes** (set at creation, cannot be changed):
- **General Purpose** — lowest per-operation latency; the default and correct for almost all workloads including web serving and content management.
- **Max I/O** — higher aggregate throughput and IOPS, at the cost of slightly higher latency per operation. For highly parallelized workloads with thousands of clients (big data, media processing). *(Note: with Elastic throughput, General Purpose now scales very high, so Max I/O is increasingly legacy — but it remains an exam answer for "thousands of clients, maximum aggregate throughput, latency tolerance.")*

**Throughput modes:**
- **Elastic** (recommended default) — automatically scales throughput up and down with demand; pay only for what you use. Best for spiky or unpredictable workloads.
- **Bursting** — baseline throughput scales with the amount of data stored (50 KB/s per GiB) and uses burst credits for peaks. Cheap for large, lightly used file systems; a small file system with heavy I/O will exhaust credits.
- **Provisioned** — you specify a fixed MB/s independent of storage size. For small file systems that need high throughput.

## 4.3 Storage classes and lifecycle

- **EFS Standard** (multi-AZ) and **EFS One Zone** (single AZ, ~47% cheaper, for dev/test or re-creatable data).
- **Infrequent Access (IA)** and **Archive** classes within each, with **lifecycle management** automatically moving files after a period without access (and optionally moving them back on access). Savings of up to ~92% for cold data.

---

# 5. Amazon FSx Family

| Service | Protocol / engine | Key features | Choose when |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB**, NTFS | Active Directory integration, NTFS ACLs, DFS Namespaces, shadow copies (user-restorable previous versions), data deduplication, Multi-AZ, SSD or HDD storage | Windows applications, user home directories, .NET apps, SQL Server file shares, lift-and-shift of Windows file servers |
| **FSx for Lustre** | Lustre (POSIX) | **Sub-millisecond latency, hundreds of GB/s throughput, millions of IOPS**; **S3 integration** — presents an S3 bucket as a file system, lazily loading objects and optionally exporting results back | HPC, machine learning training, genomics, seismic analysis, financial modelling, video rendering |
| **FSx for NetApp ONTAP** | **NFS, SMB, and iSCSI** (multiprotocol) | Snapshots, SnapMirror, FlexClone, deduplication/compression, automatic tiering to capacity pool storage | Migrating existing NetApp estates; needing one file system served over multiple protocols |
| **FSx for OpenZFS** | NFS | ZFS snapshots and clones, very low latency, high IOPS | Migrating Linux/ZFS file servers; needing ZFS features |

**FSx for Lustre deployment options:**
- **Scratch** — temporary, **not replicated**, highest raw performance per dollar; data is lost if a file server fails. For short-lived processing.
- **Persistent** — replicated within an AZ, self-healing, for longer-running workloads. Available in several throughput tiers.

---

# 6. Hybrid Storage and Data Transfer

## 6.1 AWS Storage Gateway

A hybrid appliance (VM, hardware appliance, or EC2 instance) that gives on-premises applications access to AWS storage with a **local cache** for low-latency access to hot data.

| Gateway type | Presents | Stores into | Use case |
|---|---|---|---|
| **S3 File Gateway** | **NFS / SMB** file shares | Objects in **S3** (with lifecycle to Glacier) | On-prem apps that speak file protocols but you want data in S3 |
| **FSx File Gateway** | SMB | **FSx for Windows File Server** | Low-latency on-prem access to FSx shares |
| **Volume Gateway — cached** | **iSCSI block volumes** | Primary data in S3, hot cache on-prem | Extend on-prem storage capacity to the cloud |
| **Volume Gateway — stored** | iSCSI block volumes | Primary data **on-prem**, async backups to S3 as EBS snapshots | Keep low-latency local access, back up to AWS |
| **Tape Gateway (VTL)** | Virtual tape library (iSCSI VTL) | S3 and **Glacier / Deep Archive** | Replace physical tape infrastructure with existing backup software |

## 6.2 AWS DataSync

An online transfer service that moves data **between on-premises storage and AWS**, or **between AWS services**.
- Sources/targets: NFS, SMB, HDFS, self-managed object storage, **S3, EFS, FSx (all flavours)**, and other clouds.
- Up to **10× faster** than open-source tools thanks to a purpose-built protocol with parallelism and compression.
- **Scheduled, incremental, validated** transfers that **preserve metadata** (permissions, timestamps), with built-in encryption in transit.
- Runs via an **agent** on-premises (or agentless for AWS-to-AWS).
- The answer for *"recurring, automated, verified data synchronization."*

## 6.3 AWS Transfer Family

Fully managed **SFTP, FTPS, FTP, and AS2** endpoints that read and write directly to **S3 or EFS**. Authentication via service-managed users, Active Directory, or a custom identity provider. Use when **partners must keep using their existing file-transfer clients**.

## 6.4 AWS Snow Family

Physical devices for **offline bulk transfer** where the network is impractical:
- **Snowcone** — 8 TB HDD / 14 TB SSD, portable and rugged, can also run compute at the edge
- **Snowball Edge Storage Optimized** — ~80 TB usable, the workhorse for bulk migration
- **Snowball Edge Compute Optimized** — fewer TB, more vCPU/GPU, for edge processing
- **Snowmobile** — a shipping container for up to 100 PB (largely historical, but exam-relevant)

**Rule of thumb:** compute `time = data ÷ usable bandwidth`. If transferring over the network would take **more than about a week**, choose Snow. For example, 100 TB over a 1 Gbps link at full utilization is roughly 9 days — and real-world utilization is much lower.

## 6.5 Choosing a transfer method

| Situation | Service |
|---|---|
| One-time bulk move, poor bandwidth | **Snowball Edge** |
| Recurring scheduled sync | **DataSync** |
| Continuous hybrid file access with local cache | **Storage Gateway** |
| Partners uploading with SFTP clients | **Transfer Family** |
| Ongoing high-volume transfer over a private link | **Direct Connect** (+ DataSync) |
| Global users uploading large objects to S3 | **Multipart upload + Transfer Acceleration** |
| Database migration with change capture | **AWS DMS** |

---

# 7. Matching Workloads to Storage — Worked Scenarios

**Scenario 1 — "50 Linux web servers across 3 AZs must share the same content directory, and the dataset grows unpredictably."**
**Amazon EFS** with Elastic throughput. EBS cannot be shared across AZs; S3 is not POSIX; FSx for Windows is SMB.

**Scenario 2 — "A machine-learning training job must read 20 TB from S3 at hundreds of GB/s with sub-millisecond latency."**
**FSx for Lustre** linked to the S3 bucket (scratch deployment if the data is transient), which lazily imports objects and can export results back.

**Scenario 3 — "A PostgreSQL database on EC2 needs a sustained 45,000 IOPS with predictable latency."**
**io2 Block Express** (or io2) on an EBS-optimized instance large enough to support that bandwidth. gp3 tops out at 16,000 IOPS.

**Scenario 4 — "A Hadoop cluster needs maximum local throughput for temporary shuffle data."**
**Instance store** on a storage-optimized (I/D/H) instance family — ephemeral is fine because HDFS replicates.

**Scenario 5 — "Nightly log processing scans terabytes sequentially; cost matters."**
**st1 (throughput-optimized HDD)** — cheaper than SSD and designed for large sequential reads.

**Scenario 6 — "We don't know how often this new dataset will be accessed and don't want retrieval surprises."**
**S3 Intelligent-Tiering.**

**Scenario 7 — "Records must be kept 10 years, retrieval within 12 hours is fine."**
**S3 Glacier Deep Archive** via a lifecycle rule.

**Scenario 8 — "Global users complain that uploading 4 GB videos to our Mumbai bucket is slow."**
**Multipart upload** for parallelism plus **S3 Transfer Acceleration** to use the nearest edge.

**Scenario 9 — "Our on-prem application writes to an SMB share; we want the data in AWS without changing the application."**
**S3 File Gateway** (if S3 is the target) or **FSx File Gateway / FSx for Windows** (if a true Windows file system is needed).

**Scenario 10 — "We must migrate 500 TB within a month over a 500 Mbps link shared with production."**
**Snowball Edge** devices — the network path would take many months.

---

# 8. Quick Decision Table

| Requirement | Answer |
|---|---|
| Shared file storage, Linux, multi-AZ, elastic | **Amazon EFS** |
| Shared file storage, Windows, Active Directory, SMB | **FSx for Windows File Server** |
| HPC/ML parallel file system integrated with S3 | **FSx for Lustre** |
| Multiprotocol (NFS + SMB + iSCSI), NetApp features | **FSx for NetApp ONTAP** |
| Single-instance database volume, consistent high IOPS | **io2 / io2 Block Express** |
| General-purpose block storage, best value | **gp3** |
| Highest IOPS, data is disposable | **Instance store** |
| Large sequential throughput, lowest block cost | **st1** |
| Coldest block storage | **sc1** |
| Boot volume | **SSD only (gp3/gp2/io1/io2)** |
| Same volume attached to several instances in one AZ | **io1/io2 Multi-Attach + cluster-aware FS** |
| Unknown/changing access pattern | **S3 Intelligent-Tiering** |
| Infrequent access but instant retrieval needed | **S3 Standard-IA** (or Glacier Instant Retrieval for colder) |
| Re-creatable, infrequent, cheapest resilient option | **S3 One Zone-IA** |
| Deep archive, hours to retrieve | **S3 Glacier Deep Archive** |
| Single-digit-ms object storage for analytics | **S3 Express One Zone** |
| Exceeding 3,500 writes/s in S3 | **Spread keys across more prefixes** |
| Upload a 50 GB object reliably | **Multipart upload** |
| Speed up long-distance uploads | **S3 Transfer Acceleration** |
| Query a subset of one large object | **S3 Select** |
| Query across many objects | **Amazon Athena** |
| Restore a volume with immediate full performance | **Fast Snapshot Restore** |
| Rarely used snapshots, cut cost | **EBS Snapshot Archive** |
| On-prem NFS/SMB backed by S3 | **S3 File Gateway** |
| Replace physical tape backups | **Tape Gateway** |
| Scheduled, validated on-prem → AWS sync | **AWS DataSync** |
| Partners upload via SFTP | **AWS Transfer Family** |
| Petabyte migration with poor bandwidth | **AWS Snowball Edge** |
| Cold EFS data costing too much | **EFS lifecycle management to IA/Archive** |
