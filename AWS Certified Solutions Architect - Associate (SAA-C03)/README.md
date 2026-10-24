# AWS Certified Solutions Architect – Associate (SAA-C03) — Complete Study Pack

Everything you need to pass, organized by the official exam guide. Each task folder contains:
- **notes.md** — detailed, exam-focused notes with decision tables and traps
- **practicequestions.md** — 20 questions with a full answer key and explanations

---

## Exam Logistics

| Item | Detail |
|---|---|
| Exam code | SAA-C03 |
| Questions | 65 (50 scored + 15 unscored) |
| Format | Multiple choice (1 of 4) and multiple response (2+ of 5+) |
| Time | 130 minutes |
| Passing score | **720 / 1000** (scaled) |
| Cost | 150 USD |
| Delivery | Pearson VUE test center or online proctored |
| Validity | 3 years |

**Scoring note:** it is compensatory — you don't need to pass each domain individually, only the total.

---

## Folder Map

```
AWS Certified Solutions Architect - Associate (SAA-C03)/
├── README.md                                   ← you are here
├── completenotes.md                            ← ALL 14 task notes merged into one file + 4 appendices
├── Exam-Day-Cheatsheet.md                      ← final 48-hour revision
├── Full-Length-Mock-Exam.md                    ← 65 questions, timed, weighted like the real exam
│
├── Domain 1 - Design Secure Architectures (30%)/
│   ├── Task 1.1 - Design Secure Access to AWS Resources/
│   ├── Task 1.2 - Design Secure Workloads and Applications/
│   └── Task 1.3 - Determine Appropriate Data Security Controls/
│
├── Domain 2 - Design Resilient Architectures (26%)/
│   ├── Task 2.1 - Design Scalable and Loosely Coupled Architectures/
│   └── Task 2.2 - Design Highly Available and Fault-Tolerant Architectures/
│
├── Domain 3 - Design High-Performing Architectures (24%)/
│   ├── Task 3.1 - High-Performing and Scalable Storage/
│   ├── Task 3.2 - High-Performing and Elastic Compute/
│   ├── Task 3.3 - High-Performing Database Solutions/
│   ├── Task 3.4 - High-Performing and Scalable Networks/
│   └── Task 3.5 - High-Performing Data Ingestion and Transformation/
│
└── Domain 4 - Design Cost-Optimized Architectures (20%)/
    ├── Task 4.1 - Cost-Optimized Storage/
    ├── Task 4.2 - Cost-Optimized Compute/
    ├── Task 4.3 - Cost-Optimized Databases/
    └── Task 4.4 - Cost-Optimized Networks/
```

**Total: 14 notes files + 14 practice sets (280 questions) + 65-question mock exam + cheat sheet.**

---

## Domain Weighting & Where to Spend Time

| Domain | Weight | ~Scored questions | Priority |
|---|---|---|---|
| 1 — Design Secure Architectures | **30%** | ~15 | Highest — IAM, VPC security, encryption |
| 2 — Design Resilient Architectures | **26%** | ~13 | High — HA, DR, decoupling |
| 3 — Design High-Performing Architectures | **24%** | ~12 | High — storage/compute/DB/network selection |
| 4 — Design Cost-Optimized Architectures | **20%** | ~10 | Medium — purchasing options, storage classes, data transfer |

In practice, services overlap heavily across domains — S3, VPC, RDS/Aurora, DynamoDB, Lambda, ELB/ASG, CloudFront and Route 53 appear in every domain.

---

## Suggested 4-Week Study Plan

**Week 1 — Domain 1 (Security)**
- Day 1–2: Task 1.1 notes + questions (IAM, Organizations, SCPs, Identity Center)
- Day 3–4: Task 1.2 notes + questions (VPC, SGs/NACLs, WAF/Shield, Secrets Manager)
- Day 5–6: Task 1.3 notes + questions (KMS, S3 security, backups, ACM)
- Day 7: Re-do every question you got wrong; build a flashcard list

**Week 2 — Domain 2 (Resilience)**
- Day 1–3: Task 2.1 (SQS/SNS/EventBridge/Step Functions, ALB/ASG, serverless, containers)
- Day 4–6: Task 2.2 (Multi-AZ, Aurora, Route 53, DR strategies, RDS Proxy)
- Day 7: Mixed review of Domains 1–2

**Week 3 — Domain 3 (Performance)**
- Day 1: Task 3.1 storage
- Day 2: Task 3.2 compute
- Day 3: Task 3.3 databases
- Day 4: Task 3.4 networking
- Day 5: Task 3.5 ingestion/analytics
- Day 6–7: Review all Domain 3 wrong answers + hands-on lab in the AWS free tier

**Week 4 — Domain 4 + Final Prep**
- Day 1–2: Tasks 4.1–4.4 (all cost notes + questions)
- Day 3: **Full-Length-Mock-Exam.md** under timed conditions (130 min)
- Day 4: Review every mock question, right and wrong
- Day 5: Re-read all 14 "Quick Decision Table" sections
- Day 6: **Exam-Day-Cheatsheet.md** + weak areas only
- Day 7: Light review, sleep well, take the exam

> If you have only 2 weeks: read all 14 notes files (skim the tables hard), do all 280 questions, then the mock exam. The decision tables alone cover the majority of scenario answers.

---

## How to Answer SAA-C03 Scenario Questions

1. **Read the last sentence first.** It tells you what is being optimized: *most cost-effective*, *least operational overhead*, *highest availability*, *most secure*, *least latency*.
2. **Identify the hard constraints** — "no code changes", "must be serverless", "RPO of 5 minutes", "cannot use the public internet".
3. **Eliminate the obviously wrong two.** Usually one option is technically impossible and one violates a best practice (hardcoded keys, public S3 buckets, root user, SSH open to 0.0.0.0/0).
4. **Choose the managed service.** AWS exams reward the answer with the least operational overhead when the question asks for it.
5. **Watch for these recurring correct answers:** IAM roles (not keys), Multi-AZ (HA) vs read replicas (performance), SQS for decoupling, VPC endpoints for private AWS access, CloudFront for global content, lifecycle policies for storage cost, Savings Plans/Spot for compute cost, Aurora for high-performance relational, DynamoDB for scale.
6. **Flag and move on.** Never spend more than ~2 minutes on one question — 130 min / 65 q = 2 min average.

---

## Common Distractor Patterns (instant eliminations)
- Anything storing **IAM access keys** on an instance or in code
- Making an **S3 bucket public** to solve an access problem
- Using the **root user** for anything routine
- **Security group deny rules** (they don't exist)
- Using **Multi-AZ to scale reads** (that's read replicas)
- Using **CloudFront for non-HTTP** protocols (that's Global Accelerator)
- **VPC peering** when CIDRs overlap, or expecting it to be transitive
- Putting a NAT gateway in a private subnet
- Attaching **WAF to an NLB or EC2** (not supported)
- Choosing **EBS for shared multi-instance file access** (that's EFS)
- Encrypting an existing RDS/EBS "in place" (must snapshot → copy encrypted → restore)
- Using **Glacier when millisecond access** is required (unless Glacier Instant Retrieval)

---

## Hands-On Practice (highly recommended, free tier)
1. Build a 2-AZ VPC: public/private subnets, IGW, NAT GW, route tables, SGs.
2. Launch an ALB + ASG of 2 instances serving a page; break one and watch it heal.
3. Create an RDS Multi-AZ instance; force a failover.
4. Create an S3 bucket: enable versioning, lifecycle rules, block public access, and a bucket policy forcing TLS.
5. Build API Gateway → Lambda → DynamoDB, add an SQS queue + DLQ.
6. Create a cross-account IAM role and assume it from the CLI.
7. Add a CloudFront distribution over an S3 bucket with OAC.
8. Set a Budget with an alert, and explore Cost Explorer by usage type.

Remember to delete everything afterwards (NAT gateways and ALBs are the usual surprise bill).
