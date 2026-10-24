# Task 4.1 — Design Cost-Optimized Storage Solutions

> Storage cost questions are mostly about **matching the access pattern to the right tier** and **automating the movement between tiers**. You also need to know the cost-management toolkit, because it is referenced across all four Domain 4 tasks.

---

# 1. The AWS Cost-Management Toolkit

These tools appear throughout Domain 4; learn which one answers which question.

| Tool | What it does | The question it answers |
|---|---|---|
| **AWS Cost Explorer** | Visualize and filter up to 12 months of historical cost and usage, with **12-month forecasts**, grouping by service, account, tag, Region; also surfaces **rightsizing recommendations** and RI/Savings Plans recommendations | "Where is our money going, and what will it be next month?" |
| **AWS Budgets** | Set cost, usage, RI/SP utilization or coverage budgets with **alerts** (SNS/email/Chatbot) and **Budget Actions** (apply an IAM policy, stop instances, target an SCP) | "Alert me — or act — before we overspend" |
| **AWS Cost and Usage Report (CUR)** | The most granular billing data (hourly/resource level) delivered to S3 for Athena/Redshift/QuickSight analysis | "I need the raw data for custom chargeback analysis" |
| **AWS Cost Anomaly Detection** | ML-based detection of unusual spend, with alerts | "Tell me when something unexpected starts costing money" |
| **AWS Trusted Advisor** | Checks across cost, performance, security, fault tolerance, service limits — including **idle load balancers, underutilized EBS volumes and instances, unassociated Elastic IPs**. Full checks require Business/Enterprise Support | "What obvious waste can I clean up right now?" |
| **AWS Compute Optimizer** | ML-driven **rightsizing** recommendations for EC2, ASGs, EBS volumes, Lambda functions, ECS on Fargate, and RDS | "Which specific instance type/size should I move to?" |
| **AWS Pricing Calculator** | Model costs **before** deploying | "What will this architecture cost?" |
| **S3 Storage Lens** | Organization-wide S3 usage and activity metrics with cost-efficiency recommendations | "Which buckets and prefixes are wasting money?" |
| **S3 Storage Class Analysis** | Analyzes access patterns per bucket/prefix to recommend lifecycle transition ages | "When should objects move to IA?" |
| **AWS Billing Conductor** | Custom billing views and rates for internal chargeback / resellers | "Show each business unit a customized bill" |
| **Cost Categories & cost allocation tags** | Group costs by team, project, environment; **tags must be activated in the Billing console** and only apply from activation forward | "Split the bill by team" |
| **Consolidated billing (Organizations)** | One bill, **shared volume discounts**, and **shared RI/Savings Plans benefits** across accounts | "Reduce cost across many accounts" |

**Exam cue pairs to memorize:** historical analysis and forecasting → **Cost Explorer**; proactive alerting/action → **Budgets**; granular raw data → **CUR**; unexpected spikes → **Cost Anomaly Detection**; quick waste checks → **Trusted Advisor**; specific resize recommendations → **Compute Optimizer**.

---

# 2. How S3 Billing Actually Works

You pay for several independent dimensions, and the exam often hinges on one of the less obvious ones:

1. **Storage per GB-month** — varies enormously by storage class
2. **Requests** — PUT/COPY/POST/LIST and GET/SELECT, priced per 1,000; **colder classes have higher request costs**
3. **Data transfer OUT to the internet** — the big one; transfer **IN is free**, and transfer to **CloudFront is free**
4. **Retrieval fees** — charged per GB for Standard-IA, One Zone-IA, and all Glacier classes
5. **Early deletion charges** — if you delete before the **minimum storage duration**, you still pay for the full duration
6. **Minimum billable object size** — 128 KB for IA/Glacier Instant, 40 KB for Glacier Flexible/Deep Archive
7. **Management features** — Intelligent-Tiering monitoring fee per object, Inventory, Storage Lens advanced metrics, replication, Object Lambda

**The classic trap:** moving millions of **small** objects to Glacier Deep Archive can *increase* cost, because each object is billed at the 40 KB minimum plus per-object transition request charges. Aggregate small files first.

**The second classic trap:** moving frequently accessed data to IA saves on storage but incurs **retrieval fees** on every access, often costing more overall. IA is for data accessed roughly **less than once a month**.

---

# 3. S3 Storage Classes — Cost View

| Class | Relative storage cost | Retrieval fee | Min duration | Min billable size | AZs | When it's the cheapest correct answer |
|---|---|---|---|---|---|---|
| **S3 Standard** | Baseline (highest) | None | — | — | ≥3 | Frequently accessed, short-lived, or unpredictable *and* latency-critical |
| **Intelligent-Tiering** | Standard rate in the frequent tier, dropping automatically; small **monitoring fee per object** | **None** for automatic tiers | — | 128 KB for auto-tiering | ≥3 | **Unknown or changing access patterns** — the safe default |
| **Standard-IA** | ~45% less than Standard | Per GB | **30 days** | 128 KB | ≥3 | Accessed less than monthly but needs millisecond access |
| **One Zone-IA** | ~20% less than Standard-IA | Per GB | **30 days** | 128 KB | **1** | Re-creatable or secondary copies; accept AZ-loss risk |
| **Glacier Instant Retrieval** | ~68% less than Standard | Per GB (higher) | **90 days** | 128 KB | ≥3 | Archive accessed ~quarterly that still needs **millisecond** retrieval |
| **Glacier Flexible Retrieval** | ~80%+ less | Per GB; Expedited 1–5 min / Standard 3–5 h / **Bulk free 5–12 h** | **90 days** | 40 KB | ≥3 | Archive with occasional, non-urgent retrieval |
| **Glacier Deep Archive** | **Cheapest** (~95% less) | Per GB; Standard 12 h / Bulk 48 h | **180 days** | 40 KB | ≥3 | Long-term compliance retention, rarely if ever retrieved |
| **Express One Zone** | Higher storage, **much lower request cost** | None | — | — | 1 | Very high request rates with low latency; cheaper *per request*, not per GB |

**Decision logic:**
- Accessed daily → **Standard**
- Access pattern unknown or variable → **Intelligent-Tiering**
- Accessed less than monthly, needs instant access → **Standard-IA**
- Easily re-created (thumbnails, transcodes, logs you can regenerate) → **One Zone-IA**
- Accessed a few times a year, instant access required → **Glacier Instant Retrieval**
- Archive, hours acceptable → **Glacier Flexible Retrieval**
- 7–10 year retention, almost never read → **Glacier Deep Archive**

---

# 4. Lifecycle Policies

Lifecycle rules are the automation that makes tiering real. A rule has a **filter** (prefix, tag, object size) and **actions**.

**Transition actions** move objects between classes as they age. Example policy:

```json
{
  "Rules": [{
    "ID": "log-tiering",
    "Status": "Enabled",
    "Filter": { "Prefix": "logs/" },
    "Transitions": [
      { "Days": 30,  "StorageClass": "STANDARD_IA" },
      { "Days": 90,  "StorageClass": "GLACIER_IR" },
      { "Days": 365, "StorageClass": "DEEP_ARCHIVE" }
    ],
    "Expiration": { "Days": 2555 },
    "NoncurrentVersionTransitions": [
      { "NoncurrentDays": 30, "StorageClass": "GLACIER" }
    ],
    "NoncurrentVersionExpiration": { "NoncurrentDays": 365 },
    "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 7 }
  }]
}
```

**Four actions that save money and are frequently forgotten:**
1. **`AbortIncompleteMultipartUpload`** — failed multipart uploads leave orphaned parts you pay for **forever** and which don't appear in the console object list. Always set this (7 days is typical).
2. **`NoncurrentVersionExpiration`** — in a versioned bucket, every overwrite keeps the old version. Without this rule, storage grows without bound.
3. **`ExpiredObjectDeleteMarker`** — clean up delete markers left behind when all versions of an object are gone.
4. **`Expiration`** — actually delete data you are not required to keep. Deleting is the ultimate cost optimization.

**Constraints:** objects must be ≥30 days in Standard before transitioning to Standard-IA or One Zone-IA; transitions only move "down" the hierarchy; there are per-object transition request charges, so transitioning millions of tiny objects may not pay off.

**Deciding thresholds:** use **S3 Storage Class Analysis** (per bucket/prefix access analysis with recommended ages) and **S3 Storage Lens** (organization-wide usage, with recommendations like "enable lifecycle rules on these buckets").

---

# 5. Reducing S3 Data Transfer and Request Costs

- **Transfer IN is free.** **Transfer OUT to the internet is the expensive direction.**
- **S3 → CloudFront is free**, and CloudFront's per-GB egress is cheaper than S3's. **Serving content through CloudFront reduces both transfer cost and origin requests** — a double saving that the exam loves.
- **VPC gateway endpoint for S3 is free** and removes **NAT gateway data-processing charges** (~$0.045/GB) for instances in private subnets pulling from S3. For a workload moving terabytes, this is a very large saving.
- **Same-Region, same-AZ** traffic is cheapest; **cross-AZ traffic costs** in both directions; **cross-Region** costs more.
- **S3 Select / Athena** reduce the volume of data transferred and processed by filtering server-side.
- **Requester Pays** shifts request and transfer costs to the consumer for large shared datasets.
- **Compress** objects and **batch small requests**; request charges on millions of tiny objects can exceed storage charges.
- **Aggregate small files** (e.g., combine log files into larger Parquet objects) to reduce both request count and minimum-size waste.

---

# 6. Cost-Optimizing EBS

| Action | Saving |
|---|---|
| **Migrate gp2 → gp3** | ~20% cheaper per GB, and IOPS/throughput are **decoupled from size**, so you stop over-provisioning capacity just to get IOPS. Usually the single biggest, lowest-risk EBS win. |
| **Delete unattached volumes** | A detached volume bills at full price indefinitely. Trusted Advisor and Compute Optimizer flag these. |
| **Right-size over-provisioned volumes** | Elastic Volumes allows live resize — but **you can only grow**, so plan carefully; otherwise snapshot and restore to a smaller volume. |
| **Use st1/sc1 for throughput/cold data** | HDD is far cheaper per GB than SSD for sequential workloads and archives (not bootable). |
| **Delete old snapshots** | Snapshots are incremental but accumulate. Use **Data Lifecycle Manager** retention policies. |
| **EBS Snapshot Archive** | Up to **75% cheaper** for snapshots kept long term; 90-day minimum, 24–72 h restore. |
| **Avoid unnecessary Fast Snapshot Restore** | FSR is billed per snapshot **per AZ per hour** and is expensive if left enabled. |
| **Set `DeleteOnTermination`** appropriately | Prevents orphaned root volumes. |
| **Use instance store** where data is ephemeral | Included in the instance price — no extra storage charge. |

---

# 7. Cost-Optimizing EFS and FSx

**EFS:**
- **Lifecycle management** moves files not accessed for N days to **Infrequent Access** (up to ~92% cheaper) and then **Archive**, with optional transition back on access. There is a per-GB retrieval fee for IA, so set the transition period sensibly.
- **EFS One Zone** is ~47% cheaper than Standard — appropriate for dev/test and re-creatable data.
- **Throughput mode**: **Elastic** charges for what you use (best for spiky); **Bursting** is cheapest for large, lightly used file systems; **Provisioned** is only worth it for small file systems needing constant high throughput — check whether you are paying for provisioned throughput you don't use.
- Delete stale data; EFS bills for every GB stored.

**FSx:**
- **FSx for Windows**: choose **HDD** storage instead of SSD where latency permits; enable **data deduplication** (often 50–60% savings on user shares); use **Single-AZ** for non-critical workloads.
- **FSx for Lustre**: use **scratch** file systems for transient jobs (cheaper, no replication) and **link to S3** so the durable copy lives in cheap object storage; delete the file system when the job ends.
- **FSx for ONTAP**: automatic tiering to the **capacity pool** moves cold data to much cheaper storage.

---

# 8. Backup, Archive and Data Lifecycle Cost

- **AWS Backup** centralizes policies; the cost lives in the underlying storage, so tune **retention** aggressively and use **cold storage tiers** for long-term recovery points (note the 90-day minimum for cold storage).
- **Over-retention is the most common backup waste.** Keep daily backups for weeks, not years; keep monthly/annual backups in Deep Archive if compliance requires long retention.
- **Cross-Region copies double storage cost and add transfer cost** — do it only for data that truly needs regional DR.
- **S3 Glacier Deep Archive** is the cheapest durable home for compliance archives.
- **Tape Gateway** replaces physical tape libraries with S3/Glacier-backed virtual tapes, eliminating tape hardware and offsite storage costs.
- **S3 Object Lock / Vault Lock** add compliance guarantees without extra storage cost, but note that **locked objects cannot be deleted**, so a mistake in retention settings is expensive and irreversible.

---

# 9. Choosing the Cheapest Correct Storage Service

| Need | Cheapest appropriate option |
|---|---|
| Static website assets | **S3 + CloudFront** (not EC2 web servers) |
| Shared Linux files, mostly cold | **EFS with lifecycle to IA/Archive**, or One Zone |
| Shared Linux files, dev/test | **EFS One Zone** |
| Log archive, 7-year retention | **S3 Glacier Deep Archive** via lifecycle |
| Backups of EC2 volumes | **EBS snapshots + DLM**, archive old ones |
| Large sequential analytics scans on block storage | **st1 HDD** |
| Temporary scratch space | **Instance store** or **FSx for Lustre scratch** |
| Petabyte data lake | **S3** with Parquet + partitioning (cheap storage, cheap queries) |
| On-prem file access with cloud economics | **Storage Gateway** |
| Replace tape infrastructure | **Tape Gateway** |
| Unknown access pattern | **S3 Intelligent-Tiering** |

---

# 10. Worked Scenarios

**Scenario 1 — "Logs are written daily, queried occasionally for 30 days, then kept 7 years for compliance."**
Lifecycle: Standard → **Standard-IA at 30 days** → **Glacier Flexible or Instant at 90 days** → **Deep Archive at 365 days** → expire at 7 years. Compact small log files into larger objects first.

**Scenario 2 — "Our S3 bill keeps growing although we delete objects regularly."**
The bucket is **versioned** — deletes only add delete markers. Add **NoncurrentVersionExpiration** and **ExpiredObjectDeleteMarker** rules, and **AbortIncompleteMultipartUpload**. Confirm with **Storage Lens**.

**Scenario 3 — "Access patterns for a new dataset are unknown and the team fears retrieval fees."**
**S3 Intelligent-Tiering** — automatic tiering with **no retrieval fees** for the automatic access tiers.

**Scenario 4 — "Thumbnails are regenerable and accessed rarely."**
**S3 One Zone-IA** — cheapest resilient-enough option for re-creatable data.

**Scenario 5 — "A large media library is served globally and the S3 data-transfer bill is huge."**
Put **CloudFront** in front: S3→CloudFront transfer is free, CloudFront egress is cheaper, and caching slashes origin requests.

**Scenario 6 — "EC2 instances in private subnets pull 50 TB/month from S3 through a NAT gateway."**
Add a **gateway VPC endpoint for S3** — free, and it eliminates NAT data-processing charges.

**Scenario 7 — "We have 400 gp2 volumes sized at 1 TB purely to get 3,000 IOPS."**
Migrate to **gp3** and provision IOPS independently — smaller volumes, ~20% lower per-GB price, same or better performance.

**Scenario 8 — "Compliance requires 10-year retention of records that will almost certainly never be read."**
**S3 Glacier Deep Archive** with **Object Lock** in compliance mode if immutability is required.

**Scenario 9 — "An EFS file system holds 40 TB, but only 2 TB is touched each month."**
Enable **EFS lifecycle management** to move untouched files to **IA** (and **Archive**), saving up to ~92% on the cold portion.

---

# 11. Quick Decision Table

| Scenario | Answer |
|---|---|
| Unknown or changing access pattern | **S3 Intelligent-Tiering** |
| Infrequent access, instant retrieval | **S3 Standard-IA** |
| Re-creatable, infrequent | **S3 One Zone-IA** |
| Archive, millisecond retrieval needed | **Glacier Instant Retrieval** |
| Archive, hours acceptable | **Glacier Flexible Retrieval** |
| Cheapest long-term archive | **Glacier Deep Archive** |
| Automate tiering and deletion | **S3 Lifecycle policies** |
| Orphaned multipart parts | **AbortIncompleteMultipartUpload rule** |
| Versioned bucket growing forever | **NoncurrentVersionExpiration** |
| Decide transition ages | **S3 Storage Class Analysis** |
| Org-wide S3 waste visibility | **S3 Storage Lens** |
| Cut S3 egress cost | **CloudFront** (free S3→CF transfer) |
| Cut NAT charges for S3 traffic | **Gateway VPC endpoint (free)** |
| Shift data costs to consumers | **Requester Pays** |
| Cheaper general-purpose block storage | **gp3** |
| Cheap sequential block storage | **st1** |
| Long-term snapshot retention | **EBS Snapshot Archive** |
| Automate snapshot retention | **Data Lifecycle Manager** |
| Cold EFS data | **EFS lifecycle to IA/Archive** |
| Dev/test shared file system | **EFS One Zone** |
| Windows shares costing too much | **HDD storage + data deduplication** |
| Transient HPC file system | **FSx for Lustre scratch + S3 link** |
| Replace physical tape | **Tape Gateway** |
| Find idle/unattached resources | **Trusted Advisor** |
| Rightsizing recommendations | **Compute Optimizer** |
| Historical cost analysis and forecast | **Cost Explorer** |
| Alert or act on overspend | **AWS Budgets (+ Budget Actions)** |
| Granular billing data for analysis | **Cost and Usage Report** |
| Detect unexpected spend spikes | **Cost Anomaly Detection** |
