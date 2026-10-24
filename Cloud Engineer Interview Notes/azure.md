# Azure — Cloud Engineer Interview Master Notes (4–6 Years Experience)

> **Covers:** Cloud Engineer · Senior DevOps Engineer · SRE · Platform Engineer · Solutions Architect interview scope for Microsoft Azure.
> **Structure for every topic:** Definition → Important Points → Edge Cases & Gotchas → High-Frequency Interview Questions (Basic / Medium / Hard-Scenario) with direct answers.
> **Six-part standard for service-depth topics:** Definition → Important Points → Use cases & comparisons → Edge cases & gotchas → Interview Q&A → Production troubleshooting (command, expected output, root cause, mitigation, prevention). Section **12.5** is the Azure troubleshooting command reference; the scenario method and the 15 playbooks live in `aws.md` Part 12 and apply to both clouds.
> **Legend:** ★★★ = asked in almost every 4-year interview · ★★ = common follow-up · ★ = senior/architect depth.
> **Accuracy note:** SKUs, quotas, feature availability and region support change frequently. Figures here reflect the state at the time of writing (Oct 2026). Verify against Microsoft Learn, the Azure pricing calculator and `az provider show`/quota pages before an interview or a production decision. Where a preview/retired feature is mentioned, it is flagged.

---

<details>
<summary><strong>Table of contents</strong> (click to expand)</summary>


**PART 1 — GLOBAL INFRASTRUCTURE & FUNDAMENTALS**

- [1.1 Azure Geographies ★★ · `TIER 3 — awareness`](#11-azure-geographies)
- [1.2 Azure Regions ★★★](#12-azure-regions)
- [1.3 Azure Paired Regions ★ · `TIER 3 — awareness`](#13-azure-paired-regions)
- [1.4 Subscriptions, Management Groups & Tenants ★★★](#14-subscriptions-management-groups-tenants)
- [1.5 Azure Resource Groups ★★★](#15-azure-resource-groups)
- [1.6 Azure Shared Responsibility Model ★★★](#16-azure-shared-responsibility-model)
- [1.7 Azure Well-Architected Framework & Cloud Adoption Framework ★★★](#17-azure-well-architected-framework-cloud-adoption-framework)
- [1.8 Azure Quotas, SKU Availability & Regional Capacity ★★](#18-azure-quotas-sku-availability-regional-capacity)
- [1.9 Azure Migrate ★★](#19-azure-migrate)

**PART 2 — NETWORKING**

- [2.1 Azure Virtual Network (VNet) & Subnets ★★★ · `TIER 1`](#21-azure-virtual-network-vnet-subnets)
- [2.2 Route Tables & User-Defined Routes ★★★](#22-route-tables-user-defined-routes)
- [2.3 VNet Peering ★★★](#23-vnet-peering)
- [2.4 Hub-and-Spoke Architecture ★★★](#24-hub-and-spoke-architecture)
- [2.5 Azure Virtual WAN ★ · `TIER 3 — awareness`](#25-azure-virtual-wan)
- [2.6 Network Security Groups (NSG) ★★★](#26-network-security-groups-nsg)
- [2.7 Application Security Groups (ASG) ★★](#27-application-security-groups-asg)
- [2.8 Azure Firewall ★★★](#28-azure-firewall)
- [2.9 Azure NAT Gateway ★★★](#29-azure-nat-gateway)
- [2.10 Azure Private Link & Private Endpoints ★★★](#210-azure-private-link-private-endpoints)
- [2.11 Service Endpoints & Private DNS ★★★](#211-service-endpoints-private-dns)
- [2.12 Azure Load Balancer ★★★](#212-azure-load-balancer)
- [2.13 Azure Application Gateway ★★★](#213-azure-application-gateway)
- [2.14 Azure Front Door ★★★](#214-azure-front-door)
- [2.15 Azure Traffic Manager ★★★](#215-azure-traffic-manager)
- [2.16 ExpressRoute ★★★](#216-expressroute)
- [2.17 VPN Gateway (Site-to-Site, Point-to-Site) ★★★](#217-vpn-gateway-site-to-site-point-to-site)
- [2.18 DDoS Protection, Azure Bastion & Network Watcher ★★](#218-ddos-protection-azure-bastion-network-watcher)
- [2.19 Azure DNS & DNS Design in Hybrid Networks ★★](#219-azure-dns-dns-design-in-hybrid-networks)
- [2.20 Azure Virtual Network Manager & Network Security Perimeter ★ · `TIER 3 — awareness`](#220-azure-virtual-network-manager-network-security-perimeter)

**PART 3 — COMPUTE**

- [3.1 Azure Virtual Machines ★★★](#31-azure-virtual-machines)
- [3.2 Availability Sets vs Availability Zones vs Region Pairs ★★★](#32-availability-sets-vs-availability-zones-vs-region-pairs)
- [3.3 Virtual Machine Scale Sets (VMSS) ★★★](#33-virtual-machine-scale-sets-vmss)
- [3.4 Azure App Service (PaaS) ★★★](#34-azure-app-service-paas)
- [3.5 Azure Kubernetes Service (AKS) ★★★](#35-azure-kubernetes-service-aks)
- [3.6 Azure Container Apps & Container Instances ★★ · `TIER 2/3`](#36-azure-container-apps-container-instances)
- [3.7 Azure Functions ★★★](#37-azure-functions)
- [3.8 Azure Compute Gallery, Images & Hybrid Edge ★ · `TIER 3 — awareness`](#38-azure-compute-gallery-images-hybrid-edge)
- [3.9 AKS Advanced Networking — CNI, ingress, egress, policies, private clusters ★★★](#39-aks-advanced-networking-cni-ingress-egress-policies-private-clusters)
- [3.10 GitOps for AKS — Flux and Argo CD ★★](#310-gitops-for-aks-flux-and-argo-cd)

**PART 4 — STORAGE**

- [4.1 Azure Storage Accounts ★★★](#41-azure-storage-accounts)
- [4.2 Azure Storage Redundancy ★★★](#42-azure-storage-redundancy)
- [4.3 Blob Storage — Tiers, Lifecycle & Features ★★★](#43-blob-storage-tiers-lifecycle-features)
- [4.4 Shared Access Signatures (SAS) & Access Management ★★★](#44-shared-access-signatures-sas-access-management)
- [4.5 Azure Files, Disks & Data Lake ★★★](#45-azure-files-disks-data-lake)
- [4.6 Storage Security & Encryption ★★★](#46-storage-security-encryption)

**PART 5 — DATABASES**

- [5.1 Azure SQL Database ★★★](#51-azure-sql-database)
- [5.2 Azure SQL — HA, Backups & Geo-Replication ★★★](#52-azure-sql-ha-backups-geo-replication)
- [5.3 Azure SQL Managed Instance & SQL on VM ★★](#53-azure-sql-managed-instance-sql-on-vm)
- [5.4 Azure Cosmos DB ★★★ · `TIER 2 — core mechanics only`](#54-azure-cosmos-db)
- [5.5 Azure Database for MySQL / PostgreSQL (Flexible Server) ★★★](#55-azure-database-for-mysql-postgresql-flexible-server)
- [5.6 Azure Cache for Redis / Managed Redis ★★★](#56-azure-cache-for-redis-managed-redis)
- [5.7 Azure Synapse, Data Factory & Fabric ★ · `TIER 3 — awareness`](#57-azure-synapse-data-factory-fabric)
- [5.8 Database Selection Matrix ★★★](#58-database-selection-matrix)

**PART 6 — IDENTITY, SECURITY & GOVERNANCE**

- [6.1 Microsoft Entra ID ★★★ · `TIER 1`](#61-microsoft-entra-id)
- [6.2 Azure RBAC ★★★](#62-azure-rbac)
- [6.3 Azure Key Vault ★★★](#63-azure-key-vault)
- [6.4 Azure Policy ★★★](#64-azure-policy)
- [6.5 Azure PIM, Access Reviews & Identity Governance ★★](#65-azure-pim-access-reviews-identity-governance)
- [6.6 Microsoft Defender for Cloud & Sentinel ★★](#66-microsoft-defender-for-cloud-sentinel)
- [6.7 Azure Governance Baseline Checklist ★★](#67-azure-governance-baseline-checklist)
- [6.8 Azure Lighthouse (cross-tenant management) ★](#68-azure-lighthouse-cross-tenant-management)

**PART 7 — INTEGRATION, MESSAGING & API**

- [7.1 Azure API Management ★★](#71-azure-api-management)
- [7.2 Azure Service Bus ★★★](#72-azure-service-bus)
- [7.3 Azure Event Grid ★★](#73-azure-event-grid)
- [7.4 Azure Logic Apps ★★](#74-azure-logic-apps)
- [7.5 Messaging & integration selection sheet](#75-messaging-integration-selection-sheet)

**PART 8 — MONITORING, BACKUP & OPERATIONS**

- [8.1 Azure Monitor — Platform Overview ★★★](#81-azure-monitor-platform-overview)
- [8.2 Log Analytics & KQL ★★★](#82-log-analytics-kql)
- [8.3 Application Insights ★★★](#83-application-insights)
- [8.4 Alerts, Action Groups & Alert Processing Rules ★★★](#84-alerts-action-groups-alert-processing-rules)
- [8.5 Data Collection Rules, AMA & Diagnostic Settings ★★](#85-data-collection-rules-ama-diagnostic-settings)
- [8.6 Azure Backup & Recovery Services Vault ★★★](#86-azure-backup-recovery-services-vault)
- [8.7 Azure Site Recovery (ASR) ★★★](#87-azure-site-recovery-asr)
- [8.8 Azure Cost Management, Advisor & Service Health ★★](#88-azure-cost-management-advisor-service-health)
- [8.9 Azure Update Manager ★★★](#89-azure-update-manager)
- [8.10 Azure Resource Graph ★★★](#810-azure-resource-graph)
- [8.11 Azure Automation, Runbooks & State Configuration ★★](#811-azure-automation-runbooks-state-configuration)
- [8.12 Azure CLI & PowerShell — the working toolkit ★★★](#812-azure-cli-powershell-the-working-toolkit)

**PART 9 — IaC & DEVOPS ON AZURE**

- [9.1 ARM Templates & Bicep ★★★](#91-arm-templates-bicep)
- [9.2 Terraform on Azure ★★★ · `TIER 1`](#92-terraform-on-azure)
- [9.3 Azure DevOps & GitHub Actions ★★★](#93-azure-devops-github-actions)
- [9.4 Azure Container Registry & Supply Chain ★★](#94-azure-container-registry-supply-chain)
- [9.5 Deployment Strategies on Azure ★★★](#95-deployment-strategies-on-azure)

**PART 10 — HIGH AVAILABILITY & DISASTER RECOVERY DESIGN**

- [10.1 Azure Resiliency Building Blocks ★★★](#101-azure-resiliency-building-blocks)
- [10.2 Four DR Strategies on Azure ★★★](#102-four-dr-strategies-on-azure)
- [10.3 Designing a Highly Available Three-Tier Azure Application ★★★](#103-designing-a-highly-available-three-tier-azure-application)
- [10.4 Reliability Patterns & Chaos Engineering on Azure ★★](#104-reliability-patterns-chaos-engineering-on-azure)

**PART 11 — SENIOR SCENARIO DRILLS**


**PART 12 — RAPID REVISION**

- [12.1 AWS ↔ Azure equivalents — one concise sheet (Tier-1 services only)](#121-aws-azure-equivalents-one-concise-sheet-tier-1-services-only)
- [12.2 Numbers worth memorising (verify before quoting)](#122-numbers-worth-memorising-verify-before-quoting)
- [12.3 One-line answers you must not fumble](#123-one-line-answers-you-must-not-fumble)
- [12.4 Final 60-second self-test](#124-final-60-second-self-test)
- [12.5 Command cheat sheet — troubleshooting with az CLI](#125-command-cheat-sheet-troubleshooting-with-az-cli)

</details>



---

## How to use these notes — syllabus is frozen, effort is now tiered

> **Syllabus freeze:** the topic list in this file is considered complete for a general 4-year Cloud Engineer role. Stop adding services. Spend the remaining time on hands-on labs, troubleshooting and explaining decisions from your own projects.

**Study-time allocation — 70 / 20 / 10**

| Tier | Share | What belongs here | Standard to reach |
| --- | --- | --- | --- |
| **Tier 1 — must master** | **70%** | VNets, NSGs, UDRs, peering, load balancing, VMs, VMSS, storage, Entra ID, RBAC, managed identities, Key Vault, Azure Monitor, KQL, Terraform, backup, DR, troubleshooting | Design, configure, secure, break and fix without a tutorial |
| **Tier 2 — strong working knowledge** | **20%** | AKS, App Service, Functions, Azure SQL, Cosmos DB, Azure Firewall, ExpressRoute, Private Link, Azure DevOps, Bicep, Policy, Defender for Cloud, cost optimisation, Service Bus, API Management | Choose it, compare it, and explain its failure modes |
| **Tier 3 — awareness** | **10%** | Virtual WAN, Synapse/Data Factory/Fabric, Compute Gallery, Lighthouse, Virtual Network Manager, specialist hybrid/edge, advanced governance features | Two accurate sentences + when it is used |

> **For an AKS-heavy Platform Engineer role, move AKS (3.5, 3.9, 3.10) from Tier 2 to Tier 1.**
> Sections marked `TIER 3 — awareness` or `TIER 2 — core mechanics only` in their heading should be read once, not memorised.

**7-day revision sprint (6–8 focused hours/day)**

| Day | Focus (Tier 1 first) | Practical outcome |
| --- | --- | --- |
| 1 | Tenancy/subscriptions/RGs, VNet, subnets, NSG, UDR, peering, hub-and-spoke | Whiteboard a hub-and-spoke with firewall UDRs, and prove a denied flow with `test-ip-flow` |
| 2 | Private Link + private DNS + load balancing stack + ExpressRoute/VPN | Diagnose a broken private endpoint end-to-end |
| 3 | VM, VMSS, App Service, AKS (incl. CNI/overlay/egress) | Pick a compute platform for 5 workloads; fix a failing scale-out |
| 4 | Storage, Azure SQL, Cosmos, Service Bus | Choose redundancy/SKU and messaging pattern with RPO/RTO justification |
| 5 | Entra ID, RBAC, Key Vault, Policy, Defender, Update Manager | Explain an authorization failure and a patch-compliance gap from evidence |
| 6 | Azure Monitor, KQL, Backup, ASR, Terraform, Bicep, CI/CD | Investigate an incident with KQL; recover a VM; fix a Terraform lock/drift |
| 7 | Architecture scenarios, DR design, mock interviews | Two technical mocks; write your weak-area list |

**Interview-ready checklist — apply to every Tier 1 service**

- [ ] Explain it accurately in 30–60 seconds.
- [ ] Design and configure it **without** following a tutorial.
- [ ] Compare it against at least one alternative, and say when you would *not* use it.
- [ ] State its security controls (identity, network, encryption, logging) and its cost drivers.
- [ ] Troubleshoot two or three realistic failures, with commands and expected output.
- [ ] Show the Azure CLI / PowerShell / Terraform you would actually run.
- [ ] Describe monitoring, backup and recovery for it.
- [ ] Connect it to a project you personally implemented — with a metric or outcome.

**The 5-stage answer framework (use for every scenario):**
1. **Impact** — users, services, regions, business impact.
2. **Telemetry** — metrics, logs, traces, health probes, recent changes (**Activity Log first**).
3. **Isolate** — identity → network (NSG/route/DNS) → compute → storage → dependency.
4. **Mitigate safely** — rollback, failover, scale, traffic shift, config fix.
5. **Prevent recurrence** — RCA, policy guardrails, alerts, automation, tested recovery.

**The 6 questions behind every Azure service question at this level:**
Why this service → how is it configured → how is it secured → how does it fail → how do you monitor it → how do you recover it.

**Azure-specific instinct to build:** most "it's broken" incidents are **identity/RBAC**, **NSG/UDR**, **DNS (private zones)** or **quota/SKU availability** — check the *Activity Log* and *Effective routes / Effective security rules* before guessing.

**Beyond these notes (prepare separately — this file cannot cover them):**
Linux administration (systemd, journald, `ss`, `ip`, `tcpdump`, permissions, SELinux/AppArmor) · TCP/IP and DNS fundamentals · scripting (Bash/PowerShell/Python) · Git branching and review practice · CI/CD pipeline design · containers and Dockerfile discipline · Kubernetes fundamentals beyond AKS specifics · production incident handling and on-call practice · behavioural STAR stories with measurable outcomes.

---

# PART 1 — GLOBAL INFRASTRUCTURE & FUNDAMENTALS

## 1.1 Azure Geographies ★★ · `TIER 3 — awareness`

**Definition:** An Azure geography is a defined geographical or data-residency boundary containing one or more Azure Regions.

**Important Points**
- Examples: India, United States, Europe, Asia Pacific, Brazil, Government (US Gov Virginia etc.).
- A geography typically contains multiple Regions; data residency commitments are made at geography level for many services.
- Some services are **global** (Entra ID, Azure DNS, Front Door, Traffic Manager, Policy definitions) with different data-storage behaviour. *(Awareness: know this must be checked per service; do not memorise each residency statement.)*
- Data residency is **service-specific**: metadata, logs, backups, support access, and preview features can behave differently.
- Use case: an Indian bank selects `Central India`/`South India` (or `India South Central`) and validates each service's residency behaviour before sign-off.

**Edge Cases & Gotchas**
- Selecting a geography does not guarantee every byte of metadata/telemetry stays there — validate per service and read the Microsoft data-residency/trust docs.
- Geo-redundant storage replicates to a **paired region**, which for some geographies is in a different country — a compliance trap.
- Backup, Log Analytics export, and ASR replication can move data across geographies if configured carelessly.
- Some services (e.g., certain AI/communication services) have geography-scoped instance selection requirements.

**Interview Questions**
- **Basic — What is an Azure geography?** → A defined boundary (often a country or region group) containing one or more Azure Regions, used for data residency and compliance.
- **Medium — Geography vs Region?** → Geography is the broader residency/compliance boundary; a Region is a set of data centers within it where you deploy resources.
- **Hard/Scenario — A customer requires all data to remain in India. Design it.** → Deploy in India Regions, choose LRS/ZRS (not GRS) to avoid replication to a paired region outside India, use region-scoped backups, confirm logs stay in-region, validate each PaaS service's residency statement, and document exceptions. Then verify with Policy `allowed locations`.

## 1.2 Azure Regions ★★★

**Definition:** An Azure Region is a set of data centers in a defined geographical area, connected by a dedicated low-latency network, where you deploy Azure resources.

**Important Points**
- Region codes: `centralindia`, `southindia`, `westindia`, `eastus`, `westeurope`, `southeastasia`.
- Not all Regions have Availability Zones; not all services/SKUs exist in all Regions (check `az vm list-skus --location X`).
- **Regional** resources: VNets, VMs, disks, App Service plans, SQL servers/databases.
- **Global** services: Entra ID, Front Door, Traffic Manager, Azure DNS, Azure Policy, Resource Manager control plane.
- **Resource Group location** is only metadata storage — resources inside can be in any Region.
- Region choice affects latency, cost (prices vary), compliance, SKU availability, zone support and paired-region availability.
- Quotas are **per subscription per Region** for most resources.
- Use case: app VMs + Azure SQL in `centralindia` to keep app-to-DB latency low; Front Door for global entry.

**Edge Cases & Gotchas**
- Multi-zone deployment in one Region does not survive a Region-wide outage.
- Regional services can still depend on global components (Entra ID, DNS, ARM) — a global control-plane issue can stop *deployments* even if data-plane traffic still works.
- Some VM sizes are only available in specific zones, not just Regions.
- Resource Group "location" confusion is a classic ticketing cause — it does not mean resources live there.
- Cross-region egress is billed; chatty multi-region designs get expensive.
- Preview services are region-limited and not covered by standard SLAs.

**Interview Questions**
- **Basic — What is an Azure Region?** → A geographical location containing Azure data centers connected by a low-latency network, where you deploy resources.
- **Medium — Can resources in one Resource Group be in different Regions?** → Yes — Resource Groups are logical; each resource has its own Region.
- **Hard/Scenario — The primary Region becomes unavailable. What restores service?** → A planned secondary Region with replicated data (SQL failover group, Cosmos DB multi-region, GRS/RA-GRS storage, ASR), pre-provisioned or IaC-rebuildable capacity, and global traffic routing (Front Door/Traffic Manager). Multi-zone alone does not help. State the RTO/RPO and test.

## 1.3 Azure Paired Regions ★ · `TIER 3 — awareness`

**Definition:** A relationship Microsoft designates between certain Azure Regions within a geography, used by several platform replication and recovery features.

**Important Points**
- Used by **GRS/RA-GRS/GZRS storage**, some platform updates and some service geo-replication.
- Pairs are usually within the same geography (exception: Brazil South ↔ South Central US).
- Pairing enables staggered platform maintenance (one region updated at a time) and prioritised recovery for at least one region in a pair during a broad outage.
- Many newer Regions are **non-paired** — Microsoft's current reliability guidance distinguishes paired vs non-paired regions and does not require pairing for DR design.
- **Pairing relationships are not static.** Microsoft may designate or change pairs, so residency claims such as "GRS for India replicates outside India" must be re-checked against the current pair mapping for the exact Region before you use them in a compliance decision.
- Use case: storage GRS for backup copies automatically replicates to the paired Region.

**Edge Cases & Gotchas**
- Pairing does **not** replicate VMs, App Service content, or database data automatically — only services that explicitly use it (e.g., GRS storage).
- Your paired region can be in a different country (compliance!).
- A paired Region is not a DR plan; you still design and test failover.
- Not every service supports failover to the pair, and asymmetric availability is possible.
- Microsoft may change pairing relationships over time — don't hardcode assumptions in runbooks without verification.

**Interview Questions**
- **Basic — What is a region pair?** → A Microsoft-designated relationship between two Regions in a geography used by certain replication/maintenance features.
- **Medium — Does deploying a VM automatically create anything in the paired Region?** → No. Only services that explicitly support geo-pairing (e.g., GRS storage) replicate.
- **Hard/Scenario — Compliance forbids data leaving India, but storage is GRS.** → GRS replicates to the paired Region, which for India is outside India. Use LRS/ZRS, or RA-GRS only if the paired location is acceptable; document the residency impact and validate with storage replication settings.

## 1.4 Subscriptions, Management Groups & Tenants ★★★

**Definition:** An Entra ID tenant is the identity boundary; subscriptions are billing/administration/quota boundaries; management groups organise subscriptions into a policy/RBAC hierarchy.

**Important Points**
- **Hierarchy:** Tenant (Entra ID) → Root management group → management groups (up to 6 levels below root, 10,000 MGs per directory) → subscriptions → resource groups → resources.
- **Tenant** = identity; a subscription can only trust one tenant; multiple tenants require B2B/Lighthouse or separate designs.
- **Subscription limits** exist per service per Region (vCPU quotas, public IPs, storage accounts, etc.); quotas are raised per subscription.
- **Management groups** apply RBAC and Azure Policy **by inheritance** to all child subscriptions.
- **Subscription types**: Pay-As-You-Go, EA, CSP, Microsoft Customer Agreement, Free/Trial, Dev/Test (no SLA/benefit restrictions), Government.
- **Subscription vending / landing zones** standardise new subscription creation.
- Common design: `Root → Platform (Identity, Connectivity, Management) → Landing Zones (Corp, Online) → Sandbox → Decommissioned`.
- Use case: policy that denies public IPs applied at the `Landing Zones` management group flows to every subscription beneath it.

**Edge Cases & Gotchas**
- A subscription is a **quota and blast-radius** boundary, not just billing — use separate subscriptions per environment/workload at scale.
- Moving a subscription between management groups changes inherited policies/permissions — always evaluate the target.
- Moving resources between subscriptions/RGs is not supported for every resource type, and can break dependencies (e.g., a VM's NIC, a disk's disk-encryption set).
- Deleting a subscription is a soft-delete in some flows; resources remain until fully purged.
- RBAC and Policy inheritance cannot be blocked by child scopes (except with exceptions/exemptions) — that's the point and the danger.
- Default "Access to Azure Active Directory" and classic administrator roles are legacy — remove them.

**Interview Questions**
- **Basic — What is a management group?** → A container for organising subscriptions so RBAC and Policy apply consistently by inheritance.
- **Medium — Subscription vs resource group?** → A subscription is a billing, quota and security boundary; a resource group is a logical lifecycle container inside it.
- **Hard/Scenario — 25 workloads across 4 environments must follow the same guardrails but have separate quotas and billing.** → Management groups per environment/archetype, subscription-per-workload (or per env), Policy at the MG level, RBAC via Entra groups/PIM, budgets per subscription, and a subscription-vending process via Bicep/Terraform.

## 1.5 Azure Resource Groups ★★★

**Definition:** A logical container that groups related Azure resources for deployment, management, access control and lifecycle operations.

**Important Points**
- Every ARM resource belongs to exactly one resource group; a resource group belongs to one subscription.
- Resources in a group can span Regions; the group's own "location" only stores metadata.
- **Deployment unit:** ARM/Bicep deployments target a resource group (also subscription/management-group/tenant scopes exist).
- **RBAC and Policy** can be scoped to the group; **locks** (CanNotDelete / ReadOnly) protect it.
- **Tags** for cost/ownership; **cost analysis** can be filtered by RG.
- Deleting the resource group deletes everything inside (subject to locks and dependencies).
- `Complete` deployment mode in ARM/Bicep **deletes** resources in the group not present in the template — dangerous.
- Use case: one RG per application per environment (`app1-prod-rg`) with a deploy pipeline scoped to it.

**Edge Cases & Gotchas**
- Grouping by type (all VNets in one RG) breaks lifecycle management; group by **workload + environment** instead.
- Deleting an RG fails if resources are locked or if nested features (e.g., a vNet with peerings, a Key Vault with purge protection) block it — the error usually lists the blocker.
- Cross-RG dependencies (a VM in RG-A using a VNet in RG-B) are allowed but create hidden coupling; document them.
- `ReadOnly` locks block not just writes but also operations that *look* read-only, such as listing keys from a storage account or Key Vault (control-plane POST actions).
- Resources cannot be moved between Regions; moves between RGs/subscriptions are supported only for specific types and can take time.
- A resource group is **not** a network or security boundary.

**Interview Questions**
- **Basic — What is a resource group?** → A logical container for related resources sharing a lifecycle, permissions and policy scope.
- **Medium — Can resources in different Regions share a group?** → Yes; the group's location is only metadata.
- **Hard/Scenario — Terraform/Bicep cannot delete a resource group.** → Check resource locks, RBAC at the RG, nested resources with their own protection (Key Vault purge protection, backup vaults, peerings), and the deployment mode. Read the exact error — Azure usually names the blocking resource.

## 1.6 Azure Shared Responsibility Model ★★★

**Definition:** A model that splits security duties between Microsoft and the customer, shifting by service model (IaaS → PaaS → SaaS).

**Important Points**

| Responsibility | IaaS (VM) | PaaS (App Service/SQL DB) | SaaS |
| --- | --- | --- | --- |
| Physical datacenter, hosts, network | Microsoft | Microsoft | Microsoft |
| Hypervisor / host OS | Microsoft | Microsoft | Microsoft |
| Guest OS patching | **Customer** | Microsoft | Microsoft |
| Runtime/middleware | Customer | Microsoft | Microsoft |
| Application code | Customer | **Customer** | Microsoft |
| Identity & access configuration | Customer | Customer | Shared |
| Data classification/protection | Customer | Customer | Shared |
| Network controls (NSG/firewall) | Customer | Customer (where exposed) | Shared |

- "Always retained by the customer": **data**, **identities and access**, **endpoints**, **accounts/permissions**, **configuration**.
- Microsoft provides the controls; you decide whether they are enabled (encryption, private endpoints, defender plans, logging).
- Compliance is shared: Microsoft's certifications cover the platform; **your** workload compliance is your evidence to produce.

**Edge Cases & Gotchas**
- "It's PaaS, so it's secure" is wrong — a public SQL firewall rule or an over-permissive SAS token is a customer failure.
- Managed disks and blobs are encrypted by default, but **key management** (platform-managed vs customer-managed) and access control remain yours.
- Microsoft patches the platform OS in App Service — you still patch your dependencies and containers, and manage runtime versions that go EOL.
- Defender for Cloud recommendations are shared-responsibility gap detection — treat them as your scorecard.

**Interview Questions**
- **Basic — Who patches the OS in a VM vs App Service?** → You patch the VM guest OS; Microsoft patches the platform OS for App Service.
- **Medium — What always stays with the customer?** → Data, identities/access, endpoints exposed, configuration choices and application security.
- **Hard/Scenario — A storage account is exposed via an over-permissive SAS token. Who is responsible and what do you do?** → Customer responsibility. Revoke immediately (rotate the account key or user-delegation key, or remove the stored access policy), review access logs/Activity Log, replace with a short-lived scoped SAS or Managed Identity access, and add Policy/Defender alerts for public or overly permissive SAS.

## 1.7 Azure Well-Architected Framework & Cloud Adoption Framework ★★★

**Definition:** WAF defines five pillars for workload quality; CAF provides the methodology (strategy, plan, ready, adopt, govern, manage) for cloud adoption.

**Important Points**
- **WAF pillars:** Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency (+ **Sustainability** guidance added to WAF in recent revisions — verify current pillar list).
- **WAF tools:** Azure Well-Architected Review assessment, Architecture Center reference architectures, **Azure Advisor** recommendations mapped to pillars.
- **CAF stages:** Strategy → Plan → Ready (landing zone) → Adopt (migrate/innovate) → Govern → Manage.
- **Landing zone:** the "Ready" output — management groups, subscriptions, identity, connectivity (hub VNet), policy, logging, security baseline.
- **Reference:** Azure Landing Zone (ALZ) accelerator (Bicep/Terraform), Cloud Adoption Framework critical design areas.
- Use case: a WAF review before go-live with a prioritised remediation backlog; CAF to structure a 200-application migration.

**Edge Cases & Gotchas**
- WAF reviews without owners and dates become shelfware — track remediation in the backlog with severity.
- Landing zones that are built once and never updated drift from Microsoft's evolving baseline.
- Advisor is a starting point, not a full architecture review (it cannot see your business constraints).
- Cost optimization trade-offs must be validated against reliability — cutting redundancy is not free.

**Interview Questions**
- **Basic — Name the WAF pillars.** → Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency (plus sustainability guidance).
- **Medium — WAF vs CAF?** → WAF = how to build a good workload; CAF = how an organisation plans, lands, governs and operates cloud adoption.
- **Hard/Scenario — You inherit 80 subscriptions with no governance. What's your first 90 days?** → Assess (Advisor, Secure Score, Policy compliance, cost), establish management groups and baseline Policy/RBAC/logging, build connectivity, define a landing-zone vending process, then migrate workloads in waves with owners and KPIs.

## 1.8 Azure Quotas, SKU Availability & Regional Capacity ★★

**Definition:** Azure enforces per-subscription, per-region quotas on resources and offers specific VM SKUs per region/zone, subject to capacity.

**Important Points**
- Quota examples: vCPUs per VM family per region, public IP addresses, network interfaces, storage accounts per region, load balancers, NICs per VM, NSG rules, Route table routes, AKS node limits.
- Check with `az vm list-usage --location <region>`, `az quota`, or the portal's Usage + quotas blade.
- **VM SKU availability** is per region **and per zone**; not all families exist everywhere.
- **Capacity** can fail independently of quota — `SkuNotAvailable` / `AllocationFailed` errors happen in busy regions/zones.
- **Reservations** can be scoped to a subscription/RG or shared; **Azure savings plan for compute** applies hourly commitment across eligible compute.
- **Spot VMs** provide discounted, evictable capacity for batch/interruptible workloads.
- **Dedicated hosts** for hardware isolation/BYOL licensing.
- Use case: DR region pre-raised quotas and a tested deployment of the same SKUs.

**Edge Cases & Gotchas**
- Quota is per **family**, so "Total Regional vCPUs" can be free while "Standard Dv5 Family vCPUs" is exhausted.
- AKS/VMSS scale-out failures are frequently quota or capacity related, not configuration.
- Zone-pinned deployments can fail in one zone while others are available — design zonal fallback.
- Trusted launch/Generation-2 image requirements restrict SKUs.
- Some SKUs are retiring; check the retirement announcements before committing.
- DR Regions often have **no** spare capacity for GPU or specialised SKUs.

**Interview Questions**
- **Basic — Where do you check remaining vCPU quota?** → Usage + quotas in the portal, or `az vm list-usage --location`.
- **Medium — Quota vs capacity?** → Quota is your subscription's allowance set by Microsoft; capacity is the physical availability of the SKU at deploy time. Both can block a deployment.
- **Hard/Scenario — A VMSS won't scale during a spike with "AllocationFailed".** → Check family vCPU quota, zone-specific availability, SKU restrictions for the subscription/region, and alternative sizes/zones. Mitigate with a flexible SKU list/spot mix, pre-scaled capacity for known events, and reserved instances/dedicated capacity for critical workloads.

---

## 1.9 Azure Migrate ★★

**Definition:** Azure Migrate is the assessment and migration hub for discovering on-premises/other-cloud servers, databases, web apps and data, sizing them for Azure and executing the move.

**Important Points**
- **Discovery:** appliance-based (VMware/Hyper-V/physical) or agentless/agent-based; **dependency mapping** shows east-west traffic so you migrate in the right grouping rather than by VM name.
- **Assessment:** right-sizing (performance-based vs as-is), readiness checks, Azure SKU recommendations, cost estimates, and gap analysis for unsupported configurations.
- **Migration tools under the hub:** **Server Migration** (agentless replication of VMware/Hyper-V/physical), **Azure Database Migration Service** for databases, **Web App Migration Assistant**, **Data Box/Storage Mover** for data.
- **Business case / TCO** and **Azure Migrate: Discovery and assessment** reports are what you show a stakeholder before committing.
- Migrations run in **waves**: assess → pilot a small group → migrate → validate → scale, with a rollback plan per wave.
- Use case: 300 VMware VMs discovered over a month, dependency maps collapse them into 40 application groups, then migrations run in 6 waves with performance-based sizing to cut over-provisioned CPU.

**Edge Cases & Gotchas**
- Performance-based sizing with only a few weeks of data can under-size; collect across a full business cycle (month-end batches matter).
- Dependency mapping requires credentials/ports and can miss agentless network flows — validate with application owners, not just the tool.
- Unsupported OS versions, legacy boot (BIOS), and multi-disk LVM layouts often fail post-migration; test boot and drivers first.
- Cutover downtime depends on the final replication delta — large delta means a longer freeze; plan the window from measured data.
- Assessment recommendations are a starting point, not a design: UDP requirements, latency-sensitive tiers and licence constraints still need decisions.
- Post-migration validation is the step teams skip — check services, DNS, certificates, scheduled tasks and licence activation before decommissioning the source.

**Interview Questions**
- **Basic — What does Azure Migrate do?** → Discovers and assesses on-premises/other-cloud workloads, recommends Azure sizing and cost, and orchestrates the migration.
- **Medium — Why is dependency mapping important?** → It groups servers by actual network relationship so you migrate a coherent application, avoiding broken dependencies and enabling wave planning.
- **Hard/Scenario — A migrated VM boots but the application fails.** → Check drivers/agents, disk layout and boot configuration, static IP/DNS settings, service dependencies that were on another server, certificates and licence activation, and security software. Keep the source powered off but intact until post-migration validation passes.

---

# PART 2 — NETWORKING

## 2.1 Azure Virtual Network (VNet) & Subnets ★★★ · `TIER 1`

**Definition:** A VNet is a logically isolated private network in Azure with its own address space; subnets divide that space and carry the network policies.

**Important Points**
- A VNet is **regional**, belongs to one subscription and one resource group, and can have multiple address spaces (IPv4 and IPv6).
- Subnets belong to one VNet and are **not** zonal objects in Azure (unlike AWS subnets) — but resources deployed in a subnet can be **zonal**, **zone-redundant**, or **regional**.
- **Azure reserves 5 IPv4 addresses per subnet:** `x.x.x.0` network, `x.x.x.1` default gateway, `x.x.x.2` and `x.x.x.3` for Azure DNS mapping, and the last address broadcast. → `/24` = **251 usable**, `/29` = **3 usable**, `/28` = **11 usable**.
- Dedicated/required subnets: **GatewaySubnet** (VPN/ExpressRoute gateways), **AzureFirewallSubnet** (and `AzureFirewallManagementSubnet` for forced tunnelling), **AzureBastionSubnet** (/26+ recommended), **GatewayLoadBalancerSubnet** for NVA chaining.
- **Delegation** lets a PaaS service own a subnet (e.g., Azure SQL Managed Instance, App Service VNet integration, Container Apps, Purview).
- **Service endpoints** extend the VNet identity to supported PaaS services over the Azure backbone.
- **Private endpoints** place a private IP (NIC) in the subnet for a PaaS resource.
- NSGs attach to **subnets and NICs**; UDRs attach to subnets; both are evaluated on the traffic path.
- Use case: 3-tier app — `web-subnet`, `app-subnet`, `db-subnet`, plus `AzureBastionSubnet`, across a /16 address space.

**Edge Cases & Gotchas**
- **Subnet resizing is constrained, not always impossible.** You can update a subnet's address prefix within the VNet address space in many cases (`az network vnet subnet update --address-prefix`), but shrinking requires the addresses to be unused, the new range must not overlap other subnets, and some resources/delegations block changes. **Treat sizing as effectively permanent and verify current behaviour for your case** — plan for growth: /24 minimum for VM/app subnets, /26+ for Application Gateway and Bastion, /27+ for Azure Firewall, and headroom for private endpoints in busy platform subnets.
- Private endpoints and AKS nodes consume IPs quickly — a /24 in a busy platform team is gone within months.
- Overlapping address spaces block peering and can block VPN/ExpressRoute; fix the IP plan before building.
- You cannot add NSG/UDR to **GatewaySubnet** the way you do elsewhere — special rules apply.
- Azure reserves the first three usable addresses beyond gateway/DNS — a `/29` leaving 3 usable IPs surprises people building gateway subnets.
- Deleting a subnet requires all resources in it to be deleted first.
- **Default outbound access is being retired** — new VMs may have no outbound internet unless you attach a NAT Gateway, a load balancer outbound rule, or a public IP. Retirement dates and per-subscription behaviour have changed more than once: **verify the current state for your subscription and Region**, and treat explicit egress (NAT Gateway) as the default design choice.

**Interview Questions**
- **Basic — How many usable IPs in an Azure /24 subnet?** → 251 (256 − 5 reserved).
- **Medium — VNet vs subnet?** → A VNet is the isolated network boundary with an address space; subnets are ranges inside it that carry NSGs, UDRs and delegations.
- **Hard/Scenario — A /24 app subnet is full and new VMs/private endpoints fail.** → Assess current allocations (VMs, AKS pods with Azure CNI, private endpoints, load balancer frontends), then expand the subnet range if supported (empty subnet) or add a new subnet and redeploy/plan IP capacity. Long term: use IPAM-style planning, larger prefixes, and CNI Overlay for AKS to reduce IP consumption.

## 2.2 Route Tables & User-Defined Routes ★★★

**Definition:** Route tables contain user-defined routes (UDRs) that override or supplement Azure's system routes to control where subnet traffic goes.

**Important Points**
- Azure creates **system routes** for the VNet, peered VNets, and default internet (0.0.0.0/0), plus BGP-learned routes from VPN/ExpressRoute when gateway propagation is enabled.
- **Route selection order:**
  1. **Longest prefix match** wins.
  2. For an identical prefix: **UDR > BGP > system route**.
- **Next-hop types:** Virtual network gateway, Virtual network, Internet, Virtual appliance (NVA/firewall), **None** (blackhole/drop).
- `0.0.0.0/0 → Virtual appliance` = forced tunnelling through a firewall/NVA.
- `Propagate gateway routes` (BGP) can be disabled to prevent on-prem routes leaking into a subnet.
- **Effective routes** (NIC → Effective routes in the portal, or `az network nic show-effective-route-table`) is the single most useful troubleshooting view.
- UDRs are required for hub-and-spoke inspection — spokes route 0.0.0.0/0 (or on-prem ranges) to the firewall's private IP.
- Use case: all spoke egress through Azure Firewall in the hub; `GatewaySubnet` routes on-prem traffic correctly.

**Edge Cases & Gotchas**
- A wrong UDR blackholes traffic *silently* (packets dropped at `None` or sent to a dead NVA) — no error is returned to the user.
- Asymmetric routing breaks stateful firewalls: return traffic must come back through the same appliance, or connections drop.
- **You do not steer traffic to a private endpoint with a UDR** — reachability comes from the endpoint's NIC in the subnet plus **name resolution** to that private IP. UDRs still apply to the subnet's traffic in general (e.g., forcing egress through a firewall), and a badly aimed default route can blackhole private-endpoint traffic. In practice the failure is nearly always DNS or an NSG, not routing — verify with `nslookup` from the client before touching route tables.
- `0.0.0.0/0 → Internet` does **not** bypass Azure Firewall if the firewall is not in the path — route *and* firewall placement must match.
- Peering traffic is enabled by default but `Allow forwarded traffic` and `Allow gateway transit` settings govern NVA/gateway scenarios.
- System routes to peered VNets can be overridden by UDRs — check effective routes, not assumptions.
- Gateway route propagation to a spoke requires `Use remote gateways` on the spoke peering.

**Interview Questions**
- **Basic — What is a UDR?** → A customer-defined route that directs subnet traffic to a specified next hop (firewall, NVA, gateway, internet, or None).
- **Medium — How does Azure choose between a UDR and a BGP route for the same prefix?** → Longest prefix wins first; for identical prefixes the UDR takes precedence over BGP, which takes precedence over system routes.
- **Hard/Scenario — After associating a route table, a VM loses internet access but can still reach other VNets.** → A `0.0.0.0/0 → Virtual appliance` route points to a firewall/NVA that is down, misconfigured, or not allowing the traffic. Check effective routes on the NIC, the firewall's rules and IP forwarding setting, the return path, and the NVA's own NSG. Remove or fix the route; verify with Connection Troubleshoot in Network Watcher.

## 2.3 VNet Peering ★★★

**Definition:** Peering connects two VNets so resources communicate privately over Microsoft's backbone using private IPs.

**Important Points**
- Same-Region (**regional**) or cross-Region (**global**) peering; same or different subscriptions/tenants (with the right permissions).
- **Non-transitive by default**: A↔B and B↔C does not give A↔C.
- Address spaces **must not overlap**.
- Peering is created in **both directions**; each side must have the peering resource and be `Connected`.
- Traffic is governed by NSGs, Azure Firewall, and route tables — peering itself is just connectivity.
- Options: `Allow virtual network access`, `Allow forwarded traffic`, `Allow gateway transit` (hub) and `Use remote gateways` (spoke).
- **Global peering** incurs data transfer charges and higher latency than regional peering.
- Peering does not merge address spaces, does not share DNS by default, and does not share gateways unless configured.
- Use case: connect an app VNet to a shared services VNet; spokes to a hub.

**Edge Cases & Gotchas**
- One-directional peering (created only on one side) shows as `Initiated` and passes no traffic — the #1 peering ticket.
- Overlapping CIDRs can never be peered; you need Private Link, VPN with NAT (where supported), or a redesign.
- Deleting and recreating a VNet breaks peering silently.
- Global peering data transfer costs surprise teams running cross-region backups/replication over peering.
- Gateway transit requires **both** the hub peering (`Allow gateway transit`) and the spoke peering (`Use remote gateways`) + `Allow forwarded traffic` where applicable.
- Peering is not a security boundary — NSGs must be right on both sides.

**Interview Questions**
- **Basic — What is VNet peering?** → Private connectivity between two VNets over the Microsoft backbone using private IP addresses.
- **Medium — Is peering transitive?** → No. Design hub-and-spoke with a firewall/NVA or use Virtual WAN for transit.
- **Hard/Scenario — Two peered VNets cannot communicate. What do you check?** → Peering state on **both** sides (`Connected`), address overlap, effective routes, NSGs at subnet and NIC level, Azure Firewall/NVA rules, DNS resolution (if using hostnames), guest OS firewall, and whether the traffic is being forced to an appliance that drops it.

## 2.4 Hub-and-Spoke Architecture ★★★

**Definition:** A topology where a central hub VNet provides shared connectivity and security services, and spoke VNets host individual workloads.

**Important Points**
- **Hub hosts:** Azure Firewall, VPN Gateway, ExpressRoute Gateway, DNS (private resolver/forwarders), Bastion, shared monitoring, and sometimes an NVA.
- **Spokes host:** application VNets, each peered to the hub only.
- **Transit:** spoke → hub firewall → on-prem/internet/other spokes via UDRs. Spoke-to-spoke traffic is *not* automatic.
- **Segmentation:** separate route tables and firewall policies per environment/OU; no default spoke-to-spoke allow.
- **Scaling:** hubs per Region, VNet peering or **Virtual WAN** hubs for many spokes; **Azure Virtual Network Manager** for central management at scale (verify).
- **DNS:** Azure Private DNS zones linked to the hub (or a central DNS subscription) so spokes resolve private endpoints and internal names.
- Use case: platform team owns the hub (firewall, gateway, DNS), product teams own spokes with delegated subnets.

**Edge Cases & Gotchas**
- Spoke-to-spoke fails unless traffic is routed through the hub firewall/NVA and the firewall allows it — peering is not transitive.
- Asymmetric routing through the firewall breaks stateful inspection.
- A single firewall instance/SKU becomes a throughput bottleneck — scale units, zones, and multiple hubs per region matter.
- Overlapping spoke CIDRs break future connectivity.
- Gateway transit misconfiguration is common — check `Use remote gateways` on the spoke peering and the hub's `Allow gateway transit`.
- Shared hub changes have blast radius across every spoke — change control and canary rollouts are mandatory.

**Interview Questions**
- **Basic — What is hub-and-spoke?** → A network topology with a central hub for shared services (firewall, gateways, DNS) connected to multiple workload spokes.
- **Medium — Why not peer every VNet to every other VNet?** → A full mesh scales as n(n−1)/2 peerings, is hard to govern, and gives no central inspection or segmentation.
- **Hard/Scenario — Two spokes cannot talk even though both are peered to the hub.** → Configure UDRs in each spoke pointing spoke-to-spoke traffic at the firewall's private IP, enable IP forwarding, ensure the firewall policy allows it, and verify the return route. Then test with Network Watcher's IP flow verify and check NSGs.

## 2.5 Azure Virtual WAN ★ · `TIER 3 — awareness`

**Definition:** A managed networking service providing global transit connectivity between branches, VNets, VPN, ExpressRoute and remote users through Microsoft-managed virtual hubs.

**Important Points**
- **Hubs** are Microsoft-managed VNets with built-in routing (no manual peering/UDR spaghetti).
- Connect **VNet connections**, **site-to-site VPN**, **point-to-site VPN**, and **ExpressRoute** to hubs.
- **Routing intent / routing policies** centralise internet and private traffic through a secured hub (Azure Firewall).
- SKUs: **Basic** (site-to-site only, limited) vs **Standard** (full transit, any-to-any, ExpressRoute, P2S, hub-to-hub).
- Hub-to-hub connects Regions automatically (global transit).
- Works well for large branch estates and multi-Region topologies where hub-and-spoke peering becomes unmanageable.
- Use case: 40 branches, 3 Regions, 60 VNets, one global transit fabric with central firewall policy.

**Edge Cases & Gotchas**
- Virtual WAN enforces its own address space structure; migrating existing hub-and-spoke requires coexistence planning.
- Routing intent simplifies security but can break asymmetric/NVA designs that need custom paths.
- Not every NVA/firewall pattern is supported in secured hubs; some advanced inspection requires a separate architecture.
- Costs: hub hourly, scale units, plus data processing — model it before choosing.
- Custom routing requirements (e.g., specific branch-to-branch policies) can conflict with the managed routing model.

**Interview Questions**
- **Basic — What is Azure Virtual WAN?** → A managed global transit service that connects VNets, branches and remote users through Microsoft-managed hubs.
- **Medium — Virtual WAN vs hub-and-spoke?** → Virtual WAN provides managed hubs and automatic any-to-any routing; hub-and-spoke uses customer-managed VNets, peerings and UDRs.
- **Hard/Scenario — A multinational with 30 branches and 40 VNets needs central security and internet egress.** → Standard Virtual WAN with regional hubs, secured hubs (Azure Firewall) + routing intent for internet/private traffic, ExpressRoute/VPN for branches, and central policy/logging; pilot one region before rollout.

## 2.6 Network Security Groups (NSG) ★★★

**Definition:** A stateful Layer 3/4 packet filter applied to a subnet, a NIC, or both, using prioritised allow/deny rules.

**Important Points**
- Rules match on source/destination (IP, CIDR, service tag, ASG), protocol, port range, and have a **priority number (100–4096, lower = evaluated first)**.
- **Stateful:** return traffic for an allowed flow is automatically permitted.
- **Default rules** (cannot be deleted): AllowVnetInBound, AllowAzureLoadBalancerInBound, DenyAllInBound (and equivalents outbound) — these allow broader intra-VNet traffic than many people expect.
- **Service tags** (`Internet`, `VirtualNetwork`, `AzureLoadBalancer`, `Storage`, `Sql`, `AzureCloud`, `AzureMonitor`, region-specific tags) simplify rules and track Microsoft ranges.
- **Application Security Groups (ASG)** group NICs so rules reference roles (`web-asg` → `db-asg`) instead of IPs.
- NSGs apply to **both subnet and NIC**; traffic must be allowed at **both** levels.
- Flow logs live in **Network Watcher / VNet flow logs** (NSG flow logs are being superseded by VNet flow logs — verify).
- Use case: allow 443 from Internet to the web ASG, allow 8080 from web ASG to app ASG, allow 1433 from app ASG to db ASG, deny everything else.

**When to use / alternatives:** **NSG** = distributed L3/L4 filtering at subnet and NIC, delegated to workload teams. **ASG** = grouping for NSG rules, not filtering. **Azure Firewall** = centralised egress/inbound policy with FQDN rules and logging. **WAF** = L7 request inspection for HTTP(S). Use NSGs everywhere as the baseline; add a firewall when you need central egress control and audit; add WAF for web-facing apps.
**Edge Cases & Gotchas**
- A higher-priority **Deny** overrides a lower-priority Allow — eval is first-match, not "any allow wins".
- Existing flows continue after an NSG change (stateful flow records); new connections follow the new rules — this looks like "the rule didn't apply".
- NSG on the NIC of a PaaS-integrated VM vs the subnet — both must permit.
- `AzureLoadBalancer` tag is required for health probes to reach the backend; removing it breaks probes only (the app still works directly), which is very confusing.
- NSGs do not inspect application payloads — that is WAF.
- Default `AllowVnetInBound` means all VMs in the VNet can talk to each other until you add deny rules — a flat network by default.
- NSG rules are evaluated for traffic in the subnet; for NVA-routed traffic, the NVA's subnet/NIC NSGs also apply.
- Deleting a rule in the portal while a pipeline re-applies it = flapping security postures; manage NSGs as code.

**Production Troubleshooting**
```bash
# Which rule decides this flow? (allow/deny + the exact rule name)
az network watcher test-ip-flow --vm <vm> -g <rg> --direction Inbound \
  --protocol TCP --local 10.0.1.4:443 --remote 203.0.113.10:51234
# Everything that will actually be evaluated on this NIC (subnet + NIC NSGs, defaults)
az network nic list-effective-nsg -g <rg> -n <nic> --query "value[].{subnet:association.subnet.id,nsg:association.networkSecurityGroup.id,rule:effectiveSecurityRules[].{name:name,access:access,prio:priority,dir:direction,port:destinationPortRange}}"
```
Interpretation: `test-ip-flow` returning `Deny` with a rule name is your root cause sentence — check both the **subnet** and **NIC** NSGs, because the more restrictive one wins. If flow is allowed but the app still fails, the packet is being dropped elsewhere (guest firewall, UDR to a firewall/NVA, or the app isn't listening). `AllowVnetInBound`/default rules explain "it works from inside the VNet but not from on-prem".

**Interview Questions**
- **Basic — What is an NSG?** → A stateful L3/L4 filter applied to subnets/NICs with prioritised allow/deny rules.
- **Medium — How is a rule evaluated?** → Priority order, lowest number first; the first matching rule decides. Returns are automatic for established flows.
- **Hard/Scenario — The NIC NSG allows 443 but clients time out.** → Check the **subnet** NSG (both apply), effective security rules, UDR/next hop (traffic may be routed to a firewall that drops it), Azure Firewall policy, guest OS firewall (iptables/ufw/Windows Firewall), listener status on the VM, and the return path. `Network Watcher → IP flow verify` gives a yes/no with the blocking rule.

## 2.7 Application Security Groups (ASG) ★★

**Definition:** Logical groupings of NICs used as source/destination in NSG rules instead of IP addresses.

**Important Points**
- ASGs make NSG rules role-based (`web-asg` → `app-asg:8080`) and survive IP changes and autoscaling.
- Membership is per NIC, in the **same VNet** as the NSG's subnet scope (generally).
- Multiple ASGs per NIC are allowed.
- Best practice naming: `asg-web-prod`, `asg-app-prod`, `asg-db-prod`.
- Use case: VMSS scales from 3 to 30 instances — the NSG rule never changes.

**Edge Cases & Gotchas**
- ASGs don't filter anything by themselves — you still need the NSG rule.
- Cross-VNet ASG usage is not supported — use IP/service tags or private endpoints.
- Incorrect grouping (putting a jump host in the web ASG) broadens access silently.
- ASGs are not identity controls — RBAC governs who can modify them.

**Interview Questions**
- **Basic — What is an ASG?** → A logical grouping of NICs used in NSG rules to avoid IP-based rules.
- **Medium — NSG vs ASG?** → The NSG enforces rules; the ASG groups interfaces that those rules reference.
- **Hard/Scenario — Autoscaling VMs need DB access without constantly editing NSG rules.** → Put the app NICs in `asg-app`, the DB NICs in `asg-db`, and write a single rule `asg-app → asg-db:1433`. New instances inherit access immediately.

## 2.8 Azure Firewall ★★★

**Definition:** A managed, stateful, cloud-native network security service with network rules, application (FQDN) rules, DNAT rules, threat intelligence and central policy.

**Important Points**
- **SKUs:** Basic (SMB, limited throughput), **Standard** (L3/L4 + FQDN filtering, threat intel), **Premium** (TLS inspection, IDPS, URL filtering, web categories).
- **Rule types:** NAT rules (DNAT inbound), Network rules (IP/port/protocol), Application rules (FQDN/URL), evaluated NAT → Network → Application.
- **Firewall Policy** (child policies) for central management at scale; **hierarchical policies** for enterprise/team delegation.
- **Threat intelligence** modes: Off / Alert / Alert and Deny (deny known-malicious IPs/FQDNs).
- **DNS proxy** so FQDN rules work for clients that don't use Azure DNS; `AzureFirewallSubnet` requirement.
- **Forced tunnelling** to on-prem is supported with a separate management subnet.
- **IP groups**, **FQDN tags** (`WindowsUpdate`, `AzureKubernetesService`), **service tags**.
- **Availability:** zone-redundant deployment across AZs; autoscale; SLA.
- **Logging:** structured logs to Log Analytics / Storage / Event Hub via diagnostic settings; `AzureFirewallApplicationRule`/`NetworkRule`/`NatRule` tables.
- Use case: hub firewall with default-deny egress, an allow-list of FQDNs per spoke, DNAT for on-prem inbound.

**When to use / alternatives:** choose **Azure Firewall** for centralised, auditable egress/inbound control across spokes with FQDN filtering (Premium adds TLS inspection/IDPS). Choose **NSGs** for cheap per-subnet enforcement without a central appliance. Use a **third-party NVA** only when you need a vendor feature set and can accept the HA/throughput/complexity cost. **WAF** handles HTTP attack patterns that a network firewall is not designed for.
**Edge Cases & Gotchas**
- Azure Firewall in a hub does **nothing** unless spokes' UDRs point at it — the most common architectural failure.
- Asymmetric routing (return path bypassing the firewall) silently drops connections.
- FQDN rules rely on SNI/DNS — traffic to IP literals or encrypted SNI (ESNI/ECH) can't be classified; use network rules.
- TLS inspection (Premium) requires distributing a CA cert to clients, and breaks pinned apps.
- Throughput is capacity-dependent; monitor `Throughput`/`FirewallHealth` metrics and scale or shard.
- Cost: per-hour per deployment + data processed; a Basic firewall in a dev hub is cheap, a Premium with TLS inspection is not.
- Firewall rules cannot override NSG denies — both must allow.

**Interview Questions**
- **Basic — Azure Firewall vs NSG?** → NSGs are distributed L3/L4 filters on subnets/NICs; Azure Firewall is a centralised stateful service with FQDN rules, DNAT, IDPS/TLS inspection and central policy.
- **Medium — How do you force all spoke internet traffic through the hub firewall?** → Create UDRs in each spoke (`0.0.0.0/0 → Virtual appliance = firewall private IP`), enable IP forwarding on the firewall (automatic), ensure the firewall subnet has internet egress, and verify effective routes and the return path.
- **Hard/Scenario — Some applications bypass the firewall after a platform change.** → Compare effective routes on affected NICs, check for a `0.0.0.0/0 → Internet` route added by a new peering/AKS egress path, review peering `Allow forwarded traffic`, and audit route tables via Policy. Add a deny-and-alert guardrail and enforce routes as code.

## 2.9 Azure NAT Gateway ★★★

**Definition:** A managed outbound-only SNAT service associated with one or more subnets, providing predictable public IPs and scalable outbound connections.

**Important Points**
- Outbound only — no unsolicited inbound.
- Uses **public IP addresses or public IP prefixes** (16 addresses each); adding IPs raises SNAT capacity.
- Can associate with multiple subnets in the same VNet; a subnet can have one NAT gateway.
- Provides **predictable egress IPs** for partner allow-lists.
- Replaces the implicit default outbound model (being retired — verify current status) and avoids the SNAT port exhaustion characteristics of load-balancer outbound rules.
- Supports TCP/UDP; idle timeout configurable (4–120 min).
- Zone-isolated or zone-redundant deployments depending on configuration (verify).
- Use case: 200 private VMs calling a third-party API that allow-lists a fixed IP.

**Edge Cases & Gotchas**
- **SNAT port exhaustion** still occurs if you have too few public IPs for very high connection churn (e.g., thousands of short-lived HTTPS connections); monitor `SNATConnectionCount` / failed connections.
- NAT Gateway does not filter traffic — pair it with NSG/Firewall for security.
- Traffic to private endpoints does **not** go through NAT Gateway.
- If a UDR sends 0.0.0.0/0 to a firewall, the firewall (not NAT Gateway) provides egress — NAT is then unused unless the firewall itself routes back to internet.
- A NAT gateway cannot be moved between subnets without reconfiguration.
- Where default outbound access has been retired for a subscription, a VM without NAT/outbound rules/public IP has **no** outbound internet — a growing source of "cloud-init/extension failed" tickets. Test the behaviour on a scratch VM rather than assuming.

**Interview Questions**
- **Basic — What is NAT Gateway?** → A managed outbound SNAT service giving a subnet predictable public egress IPs.
- **Medium — NAT Gateway vs Azure Firewall?** → NAT gives outbound connectivity/SNAT; Firewall gives centralised filtering, FQDN rules, DNAT and inspection.
- **Hard/Scenario — Hundreds of VMs intermittently fail to reach an external API.** → Check SNAT port exhaustion (metrics), connection churn/keep-alive settings, public IP count on the NAT gateway, DNS resolution, UDR path, and the external API's own rate limits. Mitigate with connection pooling, more public IPs/prefix, or multiple NAT gateways per workload.

## 2.10 Azure Private Link & Private Endpoints ★★★

**Definition:** Private Link provides private IP connectivity to PaaS services (and your own services) via a network interface in your subnet, instead of the service's public endpoint.

**Important Points**
- **Private endpoint (PE):** a NIC with a private IP in your subnet, mapped to a specific **sub-resource** of a service (e.g., blob, file, sqlServer, vault).
- **Private DNS zone integration** (`privatelink.blob.core.windows.net`, `privatelink.database.windows.net`, `privatelink.vaultcore.azure.net`) resolves the public FQDN to the PE IP.
- **Approval flow:** private endpoints can require manual approval on the target resource (cross-tenant/owner-controlled).
- **DNS is the make-or-break:** the client must resolve the service FQDN to the private IP. Link the private DNS zone to the client VNet, and use custom DNS/forwarders in hub-spoke designs.
- **Private Endpoint vs Service Endpoint:**

| | Service Endpoint | Private Endpoint |
| --- | --- | --- |
| IP used | Public IP of service, routed over backbone | Private IP in your subnet |
| Access from on-prem/peered VNets | No | Yes (with DNS + routing) |
| Service firewall exposure | `Allow trusted Microsoft services`/VNet rules | Public access can be fully disabled |
| Cost | Free | Per hour + per GB |
| Granularity | Service-level | Per sub-resource |

- **Private Link Service** exposes your own service (behind a Standard Load Balancer) to other VNets/tenants.
- **Private Endpoint network policies / NSG for private endpoints** are supported in many cases now (verify per service).
- Use case: disable public access on Storage, SQL, Key Vault, ACR and Cosmos DB; access everything via private endpoints from app subnets and on-prem.

**When to use / alternatives:** **Private endpoint** when the workload must reach PaaS over a private IP, including from on-prem/peered networks, and you want public access disabled. **Service endpoint** when you only need VNet-restricted access from that VNet and want zero cost. **Public endpoint + firewall/IP allow-list** only as a temporary or low-risk exception. **Private Link Service** when exposing *your* service to other VNets/tenants without peering.
**Edge Cases & Gotchas**
- **DNS misconfiguration is the #1 failure** — the endpoint exists but the FQDN still resolves to the public IP, so traffic goes over the internet (and is blocked by the firewall) or fails.
- Creating a PE does **not** disable public access — you must set `publicNetworkAccess: Disabled` and/or firewall rules.
- Each service sub-resource needs its own PE (blob + file + queue + table = 4 endpoints, 4 IPs, 4 DNS records).
- On-prem clients need DNS forwarding to Azure (Private DNS Resolver or DNS VMs) and ExpressRoute/VPN routes.
- Private DNS zone links must include every VNet that needs resolution — the hub link doesn't automatically cover spokes unless configured.
- Deleting a PE leaves stale DNS records; the zone record is removed only if managed automatically (verify).
- Cost adds up with many endpoints across many VNets.
- AKS with private endpoints plus private DNS needs the zone linked to the AKS VNet.

**Production Troubleshooting**
```bash
# 1. Is the endpoint approved and where does it live?
az network private-endpoint show -g <rg> -n <pe-name> \
  --query "{state:privateLinkServiceConnections[0].privateLinkServiceConnectionState.status,ip:customDnsConfigs[0].ipAddresses,nic:networkInterfaces[0].id}"

# 2. Does the CLIENT resolve the FQDN to the private IP? (run from the workload subnet)
nslookup mystorage.blob.core.windows.net

# 3. Is public access really disabled, and is DNS linked?
az storage account show -n <acct> -g <rg> --query "publicNetworkAccess"
az network private-dns link vnet list -g <dns-rg> -z privatelink.blob.core.windows.net -o table
```
Interpretation: resolution returning a **public** IP is the fault 90% of the time — the `privatelink.*` zone is not linked to the client VNet, or the VNet's custom DNS doesn't forward to Azure DNS. `state: Pending` means the endpoint was never approved. Public IP + `publicNetworkAccess: Disabled` produces a timeout that looks like a firewall problem.

**Interview Questions**
- **Basic — What is a private endpoint?** → A private IP NIC in your subnet that connects to a specific PaaS service sub-resource.
- **Medium — Service endpoint vs private endpoint?** → Service endpoints keep the public service IP but restrict access to listed VNets; private endpoints give a private IP in your VNet, work from on-prem/peered networks, and allow disabling public access entirely.
- **Hard/Scenario — A VM cannot reach a private SQL endpoint after everything "looks configured".** → Verify the PE's connection state (Approved), DNS resolution from the VM (`nslookup db.database.windows.net` must return the private IP), private DNS zone links, NSGs on the subnet/NIC, UDR path, SQL server firewall settings (`publicNetworkAccess`, Azure services exception), and the connection string's server name. Test with `Test-NetConnection`/`nc -vz`.

## 2.11 Service Endpoints & Private DNS ★★★

**Definition:** Service endpoints extend the VNet identity to supported PaaS services over the Azure backbone while keeping the service's public IP; Private DNS provides name resolution for private endpoints and internal zones.

**Important Points**
- Service endpoints appear as routes to `AzureCloud`/service tags and are enabled per subnet per service.
- The service's firewall must allow the VNet/subnet (or you rely on the endpoint's implicit allow) — access from other VNets is not covered unless they also have endpoints.
- **Private DNS zones** (`privatelink.<service>.<domain>`) hold the A records for private endpoints; they must be **linked** to each VNet that resolves them.
- **Azure DNS Private Resolver** provides inbound (on-prem → Azure) and outbound (Azure → on-prem) endpoints with forwarding rules, replacing DNS-forwarding VM pairs.
- **Azure DNS** public zones host public records with anycast resolution and alias records to Azure resources.
- **Custom DNS servers** on a VNet override Azure-provided DNS — get forwarding right or private endpoint resolution breaks.
- Zones can be **cross-subscription** (managed centrally) and use RBAC to prevent app teams editing them.
- Use case: central `privatelink` zones in the connectivity subscription, linked to hub and all spokes, with an inbound resolver for on-prem.

**Edge Cases & Gotchas**
- `168.63.129.16` is the Azure platform DNS/health-probing address — custom DNS must forward to it for Azure-provided names.
- A private DNS zone linked to the wrong VNet gives "record exists but not resolving" behaviour.
- Overlapping private zones with the same name in multiple subscriptions resolve unpredictably.
- Auto-registration of VM DNS records only works in zones with auto-registration enabled and is not supported in every zone type.
- Service endpoints cannot be used from on-prem — private endpoints or Public IP allow-lists are required.
- Changing DNS on a live AKS cluster/VM requires a restart of networking components or the node.

**Interview Questions**
- **Basic — Why is private DNS needed for private endpoints?** → Because the client connects using the public service FQDN; without the private DNS record it resolves to the public IP and bypasses (or is blocked from) the private path.
- **Medium — What does Azure DNS Private Resolver do?** → Provides managed inbound/outbound DNS endpoints and forwarding rules to connect on-premises DNS with Azure private zones, removing the need for DNS VMs.
- **Hard/Scenario — Private endpoint works from the app subnet but not from on-prem.** → Add/verify a Private DNS Resolver inbound endpoint (or DNS forwarder), conditional forwarding on-prem for `privatelink.*`, ExpressRoute/VPN routes to the PE subnet, and NSG rules for 53 and the app port. Then confirm resolution from an on-prem host.

## 2.12 Azure Load Balancer ★★★

**Definition:** A Layer 4 load balancer distributing TCP/UDP flows to backend pool members using frontend IP configurations, rules, and health probes.

**Important Points**
- **SKUs:** **Standard** (zone-redundant/zonal, secure by default, SLA, HA ports, outbound rules). Basic SKU retirement has been announced and staged — **verify the current status in your Regions**; design new work on Standard.
- **Public vs internal:** public frontend (internet-facing) or private frontend IP (internal LB for n-tier).
- **Components:** frontend IP config → load-balancing rules → backend pool (NICs, VMSS, IPs) → health probe; optional **inbound NAT rules**.
- **Distribution:** 5-tuple hash (source IP/port, dest IP/port, protocol) by default; **session persistence** options: None, Client IP, Client IP + protocol.
- **Health probes:** TCP, HTTP, HTTPS with interval/threshold; a failed probe removes the instance from rotation (it does **not** restart it unless the health probe is used with VMSS automatic repairs).
- **HA ports:** all ports/protocols for NVA/internal scenarios.
- **Outbound rules / SNAT:** outbound connectivity for backend pools; port allocation matters.
- **Zone redundancy:** zone-redundant frontend survives a zone failure; zonal frontends pin to one zone.
- **Cross-region load balancing** (global tier) exists for geo-redundant frontends (verify).
- Use case: internal Standard LB in front of 3 app VMs in 3 zones; public LB for a non-HTTP TCP service.

**When to use / alternatives:** **Load Balancer** for L4 TCP/UDP (or when you need an internal VIP). **Application Gateway** for HTTP host/path routing, TLS termination and WAF in one region. **Front Door** for global edge routing, caching and failover. **Traffic Manager** for pure DNS-based distribution across Regions or external endpoints. In practice they stack: Front Door → App Gateway → app, or Traffic Manager → regional LBs.
**Edge Cases & Gotchas**
- **SNAT port exhaustion** on outbound rules is a classic intermittent failure — use NAT Gateway for egress instead.
- Standard LB is **closed by default**: no inbound connectivity unless an NSG allows it (`AzureLoadBalancer` service tag must be permitted for probes).
- Health probe failure removes the VM from rotation — the app may be up but the probe path/port wrong.
- Frontend IP change requires updating DNS; TTL matters for failover.
- Backend pool health is per-rule; multiple rules can have different probe results.
- Session persistence with `Client IP` breaks even distribution behind NAT.
- Idle timeout (default 4 min) silently closes long-lived idle TCP sessions.
- A zone-redundant LB frontend does **not** make a single-zone backend redundant.

**Interview Questions**
- **Basic — What layer is Azure Load Balancer?** → Layer 4 (TCP/UDP).
- **Medium — Public vs internal LB?** → Public has an internet-facing frontend IP; internal has a private frontend and serves VNet/on-prem clients.
- **Hard/Scenario — One backend VM is running but never receives traffic.** → Check probe configuration (port/path/protocol), NSG rules allowing the probe from `AzureLoadBalancer`, guest firewall, the app listening on the probe port, and the backend pool membership. Then check distribution/session persistence and whether the VM is in a different zone than a zonal frontend.

## 2.13 Azure Application Gateway ★★★

**Definition:** A regional Layer 7 web traffic manager (reverse proxy) providing HTTP/HTTPS routing, TLS termination, WAF, autoscaling and zone redundancy (v2).

**Important Points**
- **Components:** frontend IP (public/private), listeners (basic/multi-site), **routing rules** (basic/path-based), backend pools (VMs, VMSS, App Service, IP/FQDN), HTTP settings (port, protocol, host header, cookie affinity, timeouts, health probe).
- **Features:** host-based and path-based routing, TLS termination and **end-to-end TLS**, WAF (OWASP/CRS + bot protection), custom error pages, rewrites, redirects, connection draining, autoscaling (v2), zone redundancy, private-only frontends.
- **SKUs:** Standard_v2 and WAF_v2 are the current generations (v1 retirement announced/staged — verify). Capacity is measured in **capacity units** (compute + connections + throughput).
- **Health probes** per HTTP settings; a backend is unhealthy if the probe fails — 502 to clients.
- **Session affinity:** cookie-based, disabled by default; app-managed affinity recommended.
- **WAF modes:** Detection and Prevention; exclusions and custom rules; per-site policies.
- **Logs:** access logs, firewall logs, performance; metrics on healthy/unhealthy host count, response status.
- Use case: `/api/*` → API pool, `/images/*` → storage origin, WAF in prevention mode, TLS with a Key Vault certificate.

**Edge Cases & Gotchas**
- **502 Bad Gateway** is the signature error: backend unhealthy, wrong port/protocol/host header, TLS mismatch (needs `Pick hostname from backend`/SNI), NSG blocking, backend timeout, or the app not listening.
- **504** = backend timeout (default 20–30 s request timeout for v2; configurable) — slow app, not the gateway.
- Health probe using HTTPS with the wrong host header fails while the site works in a browser.
- WAF in Prevention mode breaks legitimate uploads/JSON payloads — start in Detection, tune exclusions.
- App Gateway is **regional** — it cannot fail over across Regions (Front Door/Traffic Manager do that).
- Custom domains need certificates in the listener; Key Vault integration requires managed identity + access policy/RBAC.
- The dedicated subnet should be /24 (or /26 minimum for v2) and must not host other resources.
- Autoscaling has a minimum instance count — scale-in during quiet periods can cause cold-start latency.

**Interview Questions**
- **Basic — What layer is Application Gateway?** → Layer 7.
- **Medium — App Gateway vs Azure Load Balancer?** → App Gateway understands HTTP: host/path routing, TLS termination, WAF, cookies; Load Balancer is L4 flow hashing.
- **Hard/Scenario — App Gateway returns 502 for one backend pool only.** → Check backend health, probe settings (path/host header/port), HTTP settings (`Pick hostname from backend`, protocol), NSGs on the backend subnet, the app listener, TLS certificate trust for end-to-end TLS, and the timeout. Use the `BackendHealth` API and access logs to see the exact failure reason.

## 2.14 Azure Front Door ★★★

**Definition:** A global Layer 7 edge service providing anycast entry, routing, acceleration, caching, WAF and origin failover for HTTP(S) applications.

**Important Points**
- **Tiers:** Standard (routing, caching, WAF) and **Premium** (Private Link origins, enhanced WAF/bot protection, security analytics, managed rules) — verify current feature split.
- **Components:** frontend/domain → route → **origin group** → origins; rules engine for headers/redirects/rewrites; caching rules; WAF policy.
- **Origins:** App Service, App Gateway, Load Balancer frontends, storage, any public/private (Premium + Private Link) endpoint.
- **Health probes** per origin with latency-based, priority-based or weighted routing inside the origin group.
- **Caching** at the edge with TTLs and purge; compression; **rules engine** for request/response manipulation.
- **Security:** WAF (managed + custom rules, rate limiting), TLS, custom domains, Private Link origins so the origin has no public exposure.
- **Logs/metrics** in Azure Monitor; access logs to Log Analytics/Storage/Event Hub.
- Use case: active-active in `centralindia` and `southeastasia`, health-probed origin groups, WAF in prevention, private origins via Private Link.

**Edge Cases & Gotchas**
- **Origin exposure:** if the origin is publicly reachable, attackers bypass Front Door and its WAF. Use Private Link origins (Premium), App Gateway with private frontend, or an origin secret header.
- Cached responses can serve stale data after a deploy — purge or version assets.
- Health probes hitting a static page mask a broken application — probe a real readiness endpoint.
- Front Door is HTTP(S) only — use Traffic Manager/Global Accelerator equivalents for TCP/UDP (Azure has no global L4 anycast service equivalent to AWS Global Accelerator's static IPs — verify current options).
- Custom domain validation (CNAME/TXT) and certificate state are common deployment blockers.
- Front Door sits outside the VNet — NSGs don't filter traffic before it reaches the origin.
- Logging must be enabled explicitly per profile.

**Interview Questions**
- **Basic — What is Azure Front Door?** → A global Layer 7 anycast entry service with routing, caching, WAF and origin health-based failover.
- **Medium — Front Door vs Application Gateway?** → Front Door is global edge routing/failover and CDN-like caching; App Gateway is regional L7 load balancing with WAF and deep HTTP routing inside a Region.
- **Hard/Scenario — India origin fails; Europe must take over with minimal disruption.** → Origin group with both origins, health probes on a readiness endpoint, priority/latency routing, WAF at the edge, data replicated (SQL failover group / Cosmos DB), and origin capacity pre-scaled. Test with a controlled failover and verify session handling (externalised state) and cache behaviour.

## 2.15 Azure Traffic Manager ★★★

**Definition:** A DNS-based global traffic distributor that returns endpoint addresses according to routing method and endpoint health.

**Important Points**
- **Routing methods:** Priority, Weighted, Performance, Geographic, Multivalue, Subnet.
- DNS-based: the client resolves and connects directly to the endpoint — Traffic Manager is **not in the data path**.
- **Endpoint monitoring:** HTTP/HTTPS/TCP probes from multiple locations, with interval/timeout/tolerated failures.
- Works with Azure and external endpoints; nested profiles are supported for complex hierarchies.
- **TTL** and client/resolver caching determine actual failover time (default 60 s for the profile, probes every 30 s by default).
- Use case: priority failover between two Regions; performance routing for global users; geographic routing for data residency.

**Edge Cases & Gotchas**
- DNS failover is not instant and cannot move established connections — a 30-second RTO is unrealistic with DNS alone.
- Endpoint monitors can be fooled by a static page health check.
- Performance routing uses a latency table, not real-time congestion — it's approximate.
- Geographic routing may send users to a slower endpoint by design (residency).
- If the endpoint is an Azure Web App, use the `*.azurewebsites.net` name vs custom domain carefully (SNI/host header).
- Health probes come from Microsoft IP ranges; firewall/NSG allow-listing must account for them.

**Interview Questions**
- **Basic — What is Traffic Manager?** → A DNS-based global traffic routing service with health monitoring and multiple routing methods.
- **Medium — Traffic Manager vs Front Door?** → Traffic Manager answers DNS and traffic flows directly to the endpoint; Front Door proxies HTTP(S) through the edge, so it can cache, WAF and fail over without waiting for DNS.
- **Hard/Scenario — Traffic Manager fails over, but some users still hit the dead Region.** → DNS TTL and client/resolver caching, plus long-lived connections and connection reuse. Reduce TTL, verify probe settings, and for tight RTO move to Front Door (proxied) instead of DNS.

## 2.16 ExpressRoute ★★★

**Definition:** A private, dedicated connection from on-premises to Azure through a connectivity provider, bypassing the public internet.

**Important Points**
- **Circuit** (provider/provisioned bandwidth: 50 Mbps–100 Gbps) → **peering** → **ExpressRoute gateway** in the GatewaySubnet → VNets.
- **Peering types:** **Azure private** (VNet private IPs), **Microsoft peering** (Microsoft 365/public Azure services — with policy considerations), and **Azure public** peering (legacy/being retired — verify).
- **ExpressRoute Global Reach:** connect two on-prem sites through the ExpressRoute backbone.
- **FastPath:** bypasses the ExpressRoute virtual network gateway for data-plane traffic to improve latency/throughput (verify per gateway SKU).
- **Gateways:** Standard, HighPerformance, UltraPerformance, ErGw1AZ/2AZ/3AZ (zone-redundant); throughput and connection limits per SKU.
- **Redundancy:** dual circuits from two providers/locations; **ExpressRoute + VPN failover**; zone-redundant gateways.
- **BGP** exchanges routes; AS path and local preference determine preference; VNet route tables/UDRs can override.
- **ExpressRoute Direct** for 10/100 Gbps direct ports.
- Monitoring: `CircuitBitsInPerSecond`, `ArpAvailability`, gateway metrics, BGP session state.
- Use case: 10 Gbps private connectivity for a data-centre workload, with a site-to-site VPN as backup.

**Edge Cases & Gotchas**
- A single circuit is not HA — provider or location failure takes you down.
- Gateway subnet sizing and SKU determine throughput; undersized gateways bottleneck even with a big circuit.
- Route overlap between on-prem and Azure address space breaks connectivity (longest prefix may route wrongly or be dropped).
- **Asymmetric routing** across ExpressRoute + VPN breaks firewalls.
- Microsoft peering requires public IP/ASN registration and is intended for specific services — not a general internet bypass.
- BGP misconfiguration looks like "circuit up, traffic dead" — check advertised/received routes and gateway health.
- ExpressRoute does **not** encrypt traffic; use IPsec VPN over ExpressRoute or application TLS for confidentiality.
- Cost: circuit + gateway + egress; compare with VPN for small bandwidth needs.

**Interview Questions**
- **Basic — What is ExpressRoute?** → A dedicated private connection from on-prem to Azure via a connectivity provider, avoiding the public internet.
- **Medium — ExpressRoute vs site-to-site VPN?** → ExpressRoute is dedicated, predictable bandwidth/latency, higher setup time and cost; VPN runs over the internet with IPsec, faster to deploy, lower bandwidth/reliability.
- **Hard/Scenario — After adding a VPN backup to ExpressRoute, some flows fail intermittently.** → Asymmetric routing: the return path uses a different link than the outbound path, so stateful firewalls drop it. Use BGP metrics/AS-path prepending to make preference deterministic, or route both directions through one path with failover policy.

## 2.17 VPN Gateway (Site-to-Site, Point-to-Site) ★★★

**Definition:** An Azure virtual network gateway that terminates IPsec/IKE site-to-site tunnels and SSL/IKEv2 point-to-site connections into a VNet.

**Important Points**
- **Gateway types:** VPN, ExpressRoute, or both (`VpnGw1`–`VpnGw5` and AZ variants). Deployed in **GatewaySubnet**.
- **S2S:** IPsec/IKEv2 tunnels to on-prem devices or other clouds; **active-active** for HA (two public IPs), BGP support for dynamic routing.
- **P2S:** IKEv2/SSTP/**OpenVPN**; authentication with certificates, Entra ID, or RADIUS; address pool assignment.
- **Policy-based vs route-based:** route-based (VpnGw SKUs) is required for multi-site, P2S coexistence, and BGP.
- **Gateway SKU** determines throughput, tunnel count, and P2S connections — plan and monitor.
- **NAT rules** on the gateway can handle overlapping address spaces (verify support/SKU).
- **Azure Virtual WAN** provides a managed alternative for large-scale site connectivity.
- **Zone-redundant gateways** improve resilience in supported Regions.
- Use case: 20 branch offices via S2S VPN with BGP; developers via P2S OpenVPN with Entra ID auth.

**Edge Cases & Gotchas**
- GatewaySubnet must be /27 or larger (recommended /27+; smaller prefixes fail or limit SKUs depending on configuration) — plan it at VNet design time.
- A gateway is a shared, bandwidth-limited appliance: one busy tunnel starves others (SKU limits).
- Active-passive vs active-active changes failover behaviour; test it.
- P2S address pool must not overlap VNet/on-prem ranges.
- Certificate expiry (P2S root/leaf) breaks client connectivity silently.
- Tunnel up ≠ traffic flowing: check BGP routes, NSGs, and the on-prem device's interesting traffic/ACLs.
- VPN over ExpressRoute (dual path) needs careful BGP preference to avoid flaps.

**Interview Questions**
- **Basic — What is a VPN Gateway?** → An Azure gateway that terminates encrypted S2S and P2S connections into a VNet.
- **Medium — Policy-based vs route-based VPN?** → Policy-based ties traffic to specific source/dest pairs (limited); route-based uses routing tables/BGP and supports multi-site and P2S coexistence.
- **Hard/Scenario — Site-to-site tunnel is up but on-prem cannot reach a VM.** → Verify on-prem advertised routes and Azure-learned routes (BGP), VNet effective routes, NSGs on the VM subnet, gateway subnet NSG/UDR (which should normally not block), VM guest firewall, and the correct VM private IP. On-prem ACLs/interesting traffic are frequently the cause.

## 2.18 DDoS Protection, Azure Bastion & Network Watcher ★★

**Definition:** Azure DDoS Protection provides L3/L4 attack mitigation; Bastion provides managed browser-based RDP/SSH without public IPs; Network Watcher provides diagnostics (flow logs, connection troubleshoot, packet capture, topology, effective routes/rules).

**Important Points**
- **DDoS Network Protection** (per-VNet) and **DDoS IP Protection** (per public IP); platform-level protection is always on. Mitigation policies, adaptive tuning, attack analytics, rapid response support.
- **Bastion** deploys into `AzureBastionSubnet` (/26+ recommended), gives browser/CLI RDP-SSH over TLS 443 without exposing VMs; SKUs Basic/Standard (Standard adds IP-based, native client, peering support).
- **Network Watcher:** IP flow verify, next hop, connection troubleshoot, connection monitor, packet capture, NSG/VNet flow logs, topology, VPN troubleshoot, effective security rules/routes.
- **Azure Network Watcher Agent** on VMs enables packet capture and connection monitor.
- Use case: no public IPs on VMs, Bastion for admin access, VNet flow logs to a central storage/Log Analytics, Connection Monitor for hybrid latency.

**Edge Cases & Gotchas**
- DDoS Standard/Network Protection does not replace WAF — L7 attacks need Front Door/App Gateway WAF.
- Bastion requires the `AzureBastionSubnet` naming and NSG rules for 443 from Internet and 443/22/3389 from the Bastion host to targets.
- Bastion throughput/SKU limits affect large teams (concurrent sessions).
- Flow logs capture flow metadata, not payloads; retention and cost need planning.
- Packet capture requires the agent and RBAC; storage paths must be accessible.
- Network Watcher is regional; enabling it is automatic for some subscriptions but check each Region.

**Interview Questions**
- **Basic — What is Azure Bastion?** → A managed jump service providing RDP/SSH over TLS through the portal/CLI without public IPs on VMs.
- **Medium — Which tool proves a security rule blocks traffic?** → Network Watcher **IP flow verify** (and effective security rules) — it names the rule that allows or denies a 5-tuple.
- **Hard/Scenario — A VM is unreachable from on-prem and you have 15 minutes to find out why.** → Check the VM's NIC effective routes and effective NSGs, IP flow verify from the on-prem source, gateway BGP routes, whether the VM is running and the guest firewall is open, and the connection monitor/metrics. Then packet capture if still ambiguous.

## 2.19 Azure DNS & DNS Design in Hybrid Networks ★★

**Definition:** Azure DNS hosts public zones; Private DNS zones resolve private endpoint and internal names; hybrid resolution uses forwarders or Azure DNS Private Resolver.

**Important Points**
- **Public zones:** anycast, alias records to Azure resources (App Service, Front Door, Public IP, Traffic Manager), DNSSEC (verify current support), RBAC-scoped.
- **Private zones:** linked to VNets; auto-registration for VM records; used for `privatelink.*` and internal names.
- **DNS Private Resolver:** inbound endpoint (on-prem → Azure) and outbound endpoint + forwarding ruleset (Azure → on-prem), with rules for specific domains.
- **Custom DNS servers** on a VNet replace Azure DNS (168.63.129.16) — you must forward unresolved queries to it.
- **Hub-spoke DNS pattern:** DNS in the hub/identity subscription, private zones linked to hub, spokes peer and use the hub as DNS, on-prem forwards to the inbound resolver.
- Use case: `app.contoso.internal` resolves across on-prem and Azure; `*.blob.core.windows.net` resolves privately everywhere.

**Edge Cases & Gotchas**
- Conditional forwarders on-prem must include every `privatelink` zone you use — omissions cause fallback to public IPs.
- Changing VNet DNS servers requires a NIC/VM restart to take effect (DHCP option refresh).
- Auto-registration conflicts when the same hostname exists in multiple linked zones.
- Zone links cost nothing but mis-linking gives silent failures.
- Azure DNS (public) cannot host records for a zone whose name you don't own — delegation is required at the registrar.
- Private zones with the same name linked to the same VNet create ambiguous resolution.

**Interview Questions**
- **Basic — How does a VM resolve a private endpoint FQDN?** → It queries Azure DNS, which follows VNet links to the `privatelink.*` private zone that contains the PE's A record.
- **Medium — How do you resolve Azure private zones from on-prem?** → Deploy Azure DNS Private Resolver with an inbound endpoint (or DNS forwarder VMs), route ExpressRoute/VPN to it, and add conditional forwarders on-prem for each private zone.
- **Hard/Scenario — Private endpoints work in the hub but fail in spokes.** → The zone isn't linked to the spoke VNets, or the spokes don't use a DNS server that can resolve it. Link the zones to every VNet (or centralise with forwarding), verify with `nslookup` from a spoke VM, and confirm custom DNS settings point to the hub resolver.

## 2.20 Azure Virtual Network Manager & Network Security Perimeter ★ · `TIER 3 — awareness`

**Definition:** Azure Virtual Network Manager centrally manages connectivity/security configurations across subscriptions; Network Security Perimeter defines logical isolation boundaries around PaaS resources (preview/GA status varies — verify).

**Important Points**
- VNet Manager: **network groups**, **connectivity configuration** and **security admin rules** (central policies that take precedence over NSGs).
- Network Security Perimeter groups PaaS resources so access is evaluated on perimeter membership (verify GA/region support).
- *`TIER 3` — one paragraph is enough: know what it centralises and that security admin rules override NSGs.* Use case: 100+ spokes from one connectivity config; a central deny of outbound 22/3389.

**Edge Cases & Gotchas**
- Security admin rules override NSGs — a misconfigured deny breaks everything at scale.
- Preview features are not covered by support SLAs.
- Delegation of network group membership is easy to get wrong, leaving VNets ungoverned.
- Central configuration drift detection is limited; test in a sandbox network group first.

**Interview Questions**
- **Basic — What is Azure Virtual Network Manager?** → A management service to group VNets and apply connectivity and security admin configurations centrally.
- **Medium — Security admin rules vs NSGs?** → Security admin rules are central, higher-precedence guardrails; NSGs are local and delegated to workload teams.
- **Hard/Scenario — You must deny outbound RDP/SSH from all 120 VNets but teams keep adding allow rules.** → Use VNet Manager security admin rules with a Deny at high precedence, verified in a pilot network group, plus Azure Policy to ensure VNets join the group, and monitoring for exemptions.

---

# PART 3 — COMPUTE

## 3.1 Azure Virtual Machines ★★★

**Definition:** Azure VMs are IaaS compute instances running Windows or Linux on Microsoft-managed infrastructure, with full OS control.

**Important Points**
- **Series:** B (burstable), D (general purpose), E (memory), F (compute), L (storage), M (large memory), N (GPU), HB/HC (HPC). Suffixes indicate features (`s` premium storage, `d` local disk, `v5` generation, `p` ARM).
- **Disks:** OS disk + data disks (Standard HDD/SSD, Premium SSD, Premium SSD v2, Ultra). **Temporary disk** is local, non-persistent, and lost on deallocate/resize.
- **Networking:** NICs, accelerated networking (SR-IOV), public IP (Standard SKU — note new VMs get **no** default outbound internet; use NAT Gateway/LB outbound), private IP.
- **Identity:** system-assigned or user-assigned **managed identity** for Key Vault/Storage access — no secrets on the box.
- **Extensions:** Azure Monitor Agent, Custom Script, Desired State Configuration, VM Backup, Diagnostics, Defender.
- **Access:** Bastion, Just-in-Time VM access (Defender), serial console, run command, Entra ID login for Linux/Windows (verify SKU support).
- **Sizes/availability:** regional, zonal (pinned to an AZ), or zone-redundant (VMSS).
- **Boot diagnostics**, **serial console**, and **redeploy** for recovery.
- **Spot VMs**, **reserved instances**, **savings plan**, **hybrid benefit (Windows Server/SQL licences)**.
- Use case: lift-and-shift app servers behind a Standard LB across three zones.

**When to use / alternatives:** **VM** when you need OS-level control, legacy software, custom kernels/drivers, or licensing that requires a host. **VMSS** for the same workload at scale with autoscaling. **App Service** when you just need to run web apps/APIs. **AKS** for many containerised services needing orchestration. **Functions/Container Apps** for event-driven, spiky or scale-to-zero work. Prefer the highest managed tier that meets the control requirement — you inherit patching, HA and backup work with every step down.
**Edge Cases & Gotchas**
- **Stop (not deallocate) still bills compute**; only **deallocate** releases the VM to stop compute charges. Disks and public IPs continue to bill.
- Resizing a VM may require deallocation, and the target size may not exist in the current zone/cluster.
- A VM's **public IP changes** on stop/deallocate unless it's a static Standard IP.
- Temporary disk data disappears on deallocate/resize — never put data there.
- No default outbound internet for new VMs (retirement of default outbound access) — cloud-init/extension failures often trace to this.
- Guest OS firewall + NSG + Azure Firewall + UDR — four layers can each block traffic.
- Accelerated networking unsupported on some sizes/OS versions.
- Reboot vs redeploy vs reapply: redeploy moves the VM to new hardware; reapply re-applies the model (useful after a failed extension).
- Deleting a VM does not delete the NIC/disks by default unless you select those options.

**Interview Questions**
- **Basic — Stop vs deallocate?** → Stop keeps the VM allocated and billing compute; deallocate releases the allocation and stops compute billing (disks/IPs still bill).
- **Medium — How does a VM access Key Vault without a secret?** → Assign a managed identity to the VM, grant it Key Vault RBAC/access policy permissions for the secret, and use the Azure SDK's `DefaultAzureCredential`/managed identity endpoint.
- **Hard/Scenario — SSH fails though the VM is running.** → Check the VM is running and booted (boot diagnostics/serial console), NSG on NIC and subnet for 22 (or Bastion/JIT), public IP/route, guest firewall (`sshd` running, `ss -lntp`), disk full, `/etc/fstab` breaking boot, and Azure serial console to recover. Then use Run Command to test from inside.

## 3.2 Availability Sets vs Availability Zones vs Region Pairs ★★★

**Definition:** Three fault-isolation mechanisms: Availability Sets (fault/update domains within a datacenter cluster), Availability Zones (physically separate datacenters in a Region), and Region pairs (geographic DR).

**Important Points**

| Feature | Availability Set | Availability Zone |
| --- | --- | --- |
| Isolation | Fault domains (FD) + update domains (UD) within a Region | Separate physical datacenters with independent power/cooling/network |
| Failure covered | Host/rack hardware, planned maintenance | Datacenter-level failure |
| SLA | 99.95% (with 2+ VMs) | 99.99% (with 2+ VMs across zones) |
| Network | No isolation | Latency ~1–2 ms between zones |
| Deployment | Created before VMs; can't change after | Selected per VM/VMSS |
| Use | Legacy/non-zonal Regions, simple HA | Preferred for production |

- **Fault domain** = shared power/network rack; **update domain** = a group rebooted together during planned maintenance.
- **Availability Zones** give the strongest in-Region isolation; not every Region/SKU has them.
- **Zone-redundant** services (Load Balancer, App Gateway v2, VMSS, SQL DB, storage ZRS) span zones automatically.
- **Region pairs** are the outer layer for DR, but many regions are non-paired; design DR explicitly.
- Use case: 2+ VMs across 3 zones behind a zone-redundant Standard LB, zone-redundant Azure SQL, ZRS storage → 99.99% path.

**Edge Cases & Gotchas**
- A single VM in a zone is **not** highly available — redundancy requires multiple instances.
- Availability Sets do not protect against a zone/datacenter failure.
- Mixing zonal and regional resources (e.g., a zonal VM behind a regional-only service) can break resilience assumptions.
- Managed disks are zonal; a VM can only attach disks from its own zone (zonal disks) unless using zone-redundant storage options.
- Changing a VM's zone after deployment is impossible — recreate.
- Zone-redundant services can still have zonal dependencies (e.g., an instance pinned to a zone).
- SLA numbers assume specific configurations — read the SLA document before quoting.

**Interview Questions**
- **Basic — What is an Availability Set?** → A logical grouping that distributes VMs across fault and update domains to reduce correlated failures.
- **Medium — Availability Set vs Zone?** → Sets protect against host/rack failure and maintenance; zones protect against datacenter failure with stronger isolation and a higher SLA.
- **Hard/Scenario — Design for 99.99% within one Region.** → At least 2 (preferably 3) instances across zones, zone-redundant LB/App Gateway, zone-redundant database (Azure SQL zone-redundant or Business Critical), ZRS storage, zone-redundant public IPs, no single-zone dependency (NAT gateway, firewall, jump host), and tested failure of one zone.

## 3.3 Virtual Machine Scale Sets (VMSS) ★★★

**Definition:** A compute resource that deploys and manages a group of identical (uniform) or individually managed (flexible) VMs with autoscaling.

**Important Points**
- **Orchestration modes:** **Uniform** (identical instances from an image/model — classic scale sets) vs **Flexible** (mix of VM sizes/configs, manual or automatic scaling, better for migrating existing VM fleets). New workloads often choose Flexible.
- **Autoscale rules:** metric-based (CPU, memory via agent, custom metrics, queue depth) with min/max/default, scale-out/in rules, cooldown, scheduled profiles.
- **Zone-spanning** deployments give zone redundancy; `zonal` placement pins instances.
- **Upgrade policies:** Manual, Automatic, Rolling (with health checks), plus **instance repair**.
- **Health probes** via LB/App Gateway + **application health extension** for automatic repair.
- **Flexible mode** supports mixing Spot and pay-as-you-go, and standalone VMs can join a scale set.
- **Images:** Marketplace, custom managed image, **Azure Compute Gallery** (versioning, replication, shared across subscriptions/tenants).
- Use case: web tier 3→60 instances across 3 zones with App Gateway health probes.

**Edge Cases & Gotchas**
- Scale-out fails on **quota** (family vCPU) or **capacity** (`AllocationFailed`) — this is the most common VMSS incident.
- The default autoscale cooldown can cause oscillation; use longer windows and separate scale-in/out thresholds.
- Application startup slower than the health probe → instances marked unhealthy and repaired/replaced in a loop.
- Rolling upgrades need health probes to work, otherwise the upgrade stalls.
- Custom images must be rebuilt for patching — VMSS does not patch your app for you.
- Uniform mode cannot mix VM sizes; flexible mode has some feature limitations (verify).
- Scale-in may delete instances with local state — externalise state.
- Zones + Premium SSD v2/Ultra have SKU/zone restrictions.

**Production Troubleshooting**
```bash
# Why did scaling not happen / why are instances unhealthy?
az monitor autoscale show -g <rg> -n <autoscale-name> --query "{enabled:enabled,profiles:profiles[].rules[].metricTrigger}"
az vmss list-instances -g <rg> -n <vmss> -o table
az vmss get-instance-view -g <rg> -n <vmss> --instance-id 3 --query "statuses[].code"

# Is it quota or capacity? (the usual blocker)
az vm list-usage -l centralindia --query "[?contains(localName,'Dv5')].{name:localName,current:currentValue,limit:limit}"
```
Interpretation: `statuses` showing `ProvisioningState/failed` with `AllocationFailed` = capacity/quota, not configuration — check family vCPU usage and try alternate sizes/zones or a flexible orchestration set. Instances healthy but count stuck = autoscale rule/cooldown/max-capacity issue. New instances cycling to unhealthy = application startup slower than the health probe; increase the grace period or fix boot time.

**Interview Questions**
- **Basic — What is VMSS?** → A group of VMs created from the same configuration that can autoscale and be managed as one unit.
- **Medium — Uniform vs Flexible orchestration?** → Uniform requires identical instances and gives classic scale-set behaviour; Flexible allows heterogeneous VMs and is the recommended path for new/migrating workloads.
- **Hard/Scenario — CPU is 90% but VMSS does not scale out.** → Check autoscale settings (enabled, rules, max instances), metric source (guest vs host — host CPU can under-report), cooldown, quota/capacity errors in the activity log, subnet IP availability, and load balancer probe health (unhealthy instances are replaced, not scaled).

## 3.4 Azure App Service (PaaS) ★★★

**Definition:** A managed platform for hosting web apps, APIs and web jobs on Windows or Linux, with built-in scaling, deployment slots, TLS and authentication.

**Important Points**
- **Plan** defines compute (tier, cores, memory, features); multiple apps share a plan and compete for its resources.
- **Tiers:** Free/Shared (no SLA), Basic (dev), **Standard** (autoscale, slots, backups), **Premium v3** (better perf, more slots, zone redundancy), **Isolated/ASE** (dedicated VNet-injected environment).
- **Deployment slots:** staging/production with **swap** (warm-up, slot-sticky settings), ideal for blue/green.
- **Scaling:** manual scale-out (instance count) and autoscale rules; **Automatic scaling** (Premium v2/v3, HTTP-based).
- **Networking:** **VNet integration** (outbound to your VNet), **private endpoint** (inbound private), **access restrictions**, hybrid connections, App Service Environment.
- **Identity:** system/user-assigned managed identity → Key Vault, Storage, SQL.
- **Configuration:** app settings, connection strings (Key Vault references), slot settings, always-on, health check, ARR affinity, custom domains + TLS, IP restrictions.
- **Deployment:** zip deploy, container (ACI/ACR), GitHub Actions/Azure DevOps, WebDeploy, FTP (disable).
- **Backups** (Standard+) and **snapshots**; **App Service Health Check** with instance replacement.
- Use case: Spring Boot API on Linux Premium v3 with VNet integration, private endpoint, Key Vault references, slots for staging swaps.

**Edge Cases & Gotchas**
- **VNet integration is outbound only**; inbound private access needs a **private endpoint**. Mixing these up is the most common App Service networking error.
- Apps sharing a plan compete for CPU/memory — one noisy app degrades the others.
- Slot swap swaps settings marked "slot setting"; unmarked settings move with the code, causing prod pointing at a staging DB.
- File system is shared/persistent-ish but not a general distributed store; don't use local files for session state or user uploads.
- Cold start and **app initialization** affect swaps — enable warm-up/health check.
- Scale-out does not fix in-process session state or singleton background jobs.
- Private endpoint + private DNS: app's `azurewebsites.net` name resolution must reach the private IP.
- Outbound connections can hit **SNAT port exhaustion** under high fan-out (common with microservices) — use VNet integration + NAT Gateway.
- Platform updates can restart instances — design for it; use health checks and multiple instances.

**Interview Questions**
- **Basic — What is App Service?** → A managed PaaS platform hosting web apps/APIs without managing the underlying servers.
- **Medium — VNet integration vs private endpoint?** → VNet integration gives outbound access from the app into a VNet; a private endpoint gives inbound private access to the app.
- **Hard/Scenario — The app works publicly but cannot reach a private Azure SQL endpoint.** → Verify VNet integration is enabled on the correct subnet (delegated), the private endpoint's DNS zone is linked to the integration VNet, the app resolves the SQL FQDN to the private IP (Kudu console `nameresolver`), NSGs on the integration subnet allow outbound, and SQL firewall/`publicNetworkAccess` settings. Then check authentication (managed identity) separately.

## 3.5 Azure Kubernetes Service (AKS) ★★★

**Definition:** A managed Kubernetes service where Microsoft operates the control plane and you manage node pools, workloads and add-ons.

**Important Points**
- **Control plane tiers:** Free (no uptime SLA), Standard (SLA, some free allowance), Premium (long-term support, more features — verify). Control plane is free/paid per tier.
- **Node pools:** system pool (CriticalAddonsOnly) and user pools; multiple pools with different SKUs/OS; **cluster autoscaler** per pool; **node image upgrades**, **auto-upgrade channels**, **node surge**.
- **Networking:** **Azure CNI** (pod IPs from the VNet), **CNI Overlay** (pods get an overlay address space, conserving VNet IPs — recommended for large clusters), **kubenet** (legacy/limited — not for new clusters), **CNI powered by Cilium** for eBPF/network policy. **Network policies** require a supported CNI (Calico/Cilium/Azure).
- **Ingress/egress:** NGINX/app routing add-on (web application routing), **Application Gateway for Containers** / AGIC, LoadBalancer services; **managed NAT Gateway** or user-assigned NAT for predictable egress; **UDR** for egress through firewall.
- **Identity:** **Workload Identity** (federated credentials with Entra ID) replaces pod-managed identity; kubelet identity for ACR pulls; Entra ID integration for cluster auth + Kubernetes RBAC/Azure RBAC.
- **Storage:** Azure Disk CSI (RWO, zonal!), Azure Files CSI (RWX), Blob CSI; snapshots; storage classes.
- **Scaling:** HPA (metrics server), **KEDA** (event-driven), VPA, cluster autoscaler, **Node Auto-Provisioning (NAP)** (verify maturity).
- **Security:** private cluster, authorized IP ranges, Defender for Containers, Azure Policy for AKS (OPA Gatekeeper), image scanning, secrets (Key Vault CSI driver / external secrets).
- **Observability:** Container Insights (Managed Prometheus + Grafana + Container Logs v2), diagnostic settings.
- Use case: multi-team platform with system + user pools, CNI Overlay, workload identity, AGIC/App Gateway, KEDA autoscaling, private cluster.

**Edge Cases & Gotchas**
- **Subnet IP exhaustion** with Azure CNI is the classic failure — each pod gets a VNet IP; use CNI Overlay, larger subnets, or fewer pods/node.
- **Azure Disk is zonal**: a pod with a disk PVC is pinned to the zone of the disk — rescheduling across zones fails, so use ZRS-capable storage or Files/Blob for shared state.
- **Upgrades**: control-plane upgrade then node pools; API deprecations break workloads; use `kubectl convert`/pluto and staging clusters first.
- Workload Identity misconfiguration (wrong federated subject/audience/issuer) gives `AADSTS`/403 errors even when RBAC looks right.
- **Outbound type** matters: `loadBalancer` (default, SNAT exhaustion risk), `userDefinedRouting` (firewall), `managedNATGateway` (recommended predictable egress).
- **Private cluster** breaks node-to-control-plane access if DNS/private endpoint is wrong; also blocks `kubectl` from the internet.
- System pool taints and resource pressure — don't run apps on the system pool.
- Kubelet identity/ACR integration fails with `ImagePullBackOff` after identity changes.
- Cluster autoscaler won't scale down with local storage, PDBs blocking eviction, or pods without controllers.

**Interview Questions**
- **Basic — What does AKS manage?** → The control plane (API server, etcd, upgrades, patching, SLA); you manage nodes, workloads, networking, identity and add-ons.
- **Medium — Azure CNI vs CNI Overlay?** → Azure CNI assigns VNet IPs to every pod (simple, IP-hungry, routable from on-prem); Overlay assigns pods addresses from a separate CIDR with node-level routing (IP-efficient, still supports network policy).
- **Hard/Scenario — Pods are stuck Pending with "insufficient IPs" after adding a new pool.** → The node subnet has no free IPs. Check free addresses, pod-per-node limits, CNI mode, and the pool's subnet. Mitigate with a larger subnet or a new subnet/pool using CNI Overlay, reduce `maxPods`, and monitor subnet capacity.

## 3.6 Azure Container Apps & Container Instances ★★ · `TIER 2/3`

**Definition:** Container Apps is a serverless container platform on Kubernetes (KEDA/Dapr) with scale-to-zero; Container Instances (ACI) runs single containers without orchestration.

**Important Points**
- **Container Apps:** environments, revisions, traffic splitting, scale rules (HTTP, queue, KEDA scalers), scale-to-zero, ingress (internal/external), managed identity, secrets, Dapr integration, jobs for batch.
- **ACI:** fast single-container/burst workloads, no orchestration, per-second billing, VNet injection (into a delegated subnet), useful for CI agents and short jobs.
- **Container Apps environments** can be VNet-injected for private networking.
- Use case: event-driven microservices with scale-to-zero; ACI for one-off batch tasks.

**Edge Cases & Gotchas**
- Container Apps has cold starts on scale-to-zero — set minimum replicas for latency-sensitive APIs.
- Not a full Kubernetes API — CRDs/operators/daemonsets are unavailable; move to AKS if you need them.
- VNet injection limits and subnet sizing per environment.
- ACI has no built-in HA/load balancing — don't run production APIs there without a front door.
- Revision traffic splitting interacts with session state; externalise state.

**Interview Questions**
- **Basic — Container Apps vs AKS?** → Container Apps is a managed serverless container platform with less control; AKS gives full Kubernetes.
- **Medium — When ACI?** → Short-lived, single-container tasks, burst jobs, or CI build agents where orchestration adds no value.
- **Hard/Scenario — An event-driven worker must scale to zero and handle bursts of 5,000 messages.** → Container Apps with a KEDA queue scaler, max replicas tuned to downstream capacity, idempotent processing, and a dead-letter queue; verify cold-start latency and downstream rate limits.

## 3.7 Azure Functions ★★★

**Definition:** Serverless compute for event-driven functions with multiple hosting plans (Consumption, Flex Consumption, Premium, Dedicated/App Service, Container Apps).

**Important Points**
- **Triggers/bindings:** HTTP, Timer, Queue/Service Bus, Event Hub, Event Grid, Blob, Cosmos DB, Service Bus, Kafka (verify).
- **Plans:**
  - **Consumption** — scale to zero, pay per execution/GB-s, cold starts, 5–10 min timeout (configurable, max 10 min).
  - **Flex Consumption** — newer serverless plan with faster scaling, VNet integration and instance concurrency control (verify region/feature support).
  - **Premium** — pre-warmed instances, VNet integration, longer timeouts, higher scale, no cold start (costlier).
  - **Dedicated** — runs on App Service plan.
- **Durable Functions** for orchestration (function chaining, fan-out/fan-in, async HTTP, monitors, human interaction) with state stored in Storage.
- **Configuration:** `host.json`, `function.json`/decorators, app settings, Key Vault references, managed identity.
- **Deployment:** zip, containers, slots on Premium/Dedicated.
- Use case: blob-triggered processing, scheduled jobs, Service Bus consumers, Durable orchestrations.

**Edge Cases & Gotchas**
- Consumption plan does **not** support VNet integration (classic) — Premium/Flex/Dedicated do. Networking surprises are common.
- Timeout limits break long jobs — use Durable Functions or Container Apps jobs.
- **At-least-once** triggers (Service Bus/Storage Queue) mean duplicate invocations — make handlers idempotent.
- Cold starts on Consumption; Premium pre-warmed instances cost money.
- Concurrency: a single instance can process multiple messages — set `maxConcurrentCalls`/batch sizes to protect downstream systems.
- Storage account dependency for the Functions runtime (`AzureWebJobsStorage`) — a deleted/rotated key breaks the app.
- Durable Functions history size limits; large payloads should be externalised.

**Interview Questions**
- **Basic — What is Azure Functions?** → Serverless, event-driven compute with triggers and bindings.
- **Medium — Consumption vs Premium?** → Consumption scales to zero and bills per execution (cold starts, no classic VNet); Premium gives pre-warmed instances, VNet integration and longer execution.
- **Hard/Scenario — A Service Bus-triggered function reprocesses the same message after scaling.** → Message lock renewal expired because processing exceeded the lock duration, so the message became visible again. Increase lock duration or renew it, make the handler idempotent, use sessions/ordered processing if required, and monitor dead-letter queues.

## 3.8 Azure Compute Gallery, Images & Hybrid Edge ★ · `TIER 3 — awareness`

**Definition:** Compute Gallery stores and versions VM images and shares them across subscriptions/tenants; Azure Arc extends Azure management to on-prem/multicloud servers and Kubernetes.

**Important Points**
- **Compute Gallery:** image definitions + versions, replication to target Regions, RBAC sharing, used by VMSS/AKS node images. **Image Builder** automates builds. *(Awareness: versioning + replication + VMSS/AKS integration is enough.)*
- **Azure Arc:** projects non-Azure servers/K8s into Azure for Policy, Monitor, Defender, Update Manager; requires the Connected Machine agent.
- **Azure Stack HCI / Edge** for on-prem Azure-consistent infrastructure (awareness).
- Use case: golden images versioned in a gallery and replicated to DR Regions; Arc-enabled on-prem SQL servers onboarded to Defender.

**Edge Cases & Gotchas**
- Gallery replication lag: a new image version may not exist in the target Region when a deployment starts.
- Arc-enabled servers still need network egress to Azure endpoints — private endpoints/proxies must be configured.
- Arc does not make an on-prem box an Azure VM; it's a management projection.
- Image versioning policy matters — pin versions in IaC, don't rely on `latest`.

**Interview Questions**
- **Basic — What is Azure Compute Gallery?** → A repository for versioned VM images that can be replicated and shared.
- **Medium — Why use a gallery instead of a managed image?** → Versioning, regional replication, sharing across subscriptions/tenants, and integration with VMSS/AKS.
- **Hard/Scenario — A DR Region deployment fails because the image isn't there.** → Replicate the image version to the DR Region ahead of time in the pipeline, pin the exact version in the deployment, and alarm on replication status; never depend on implicit replication.

---

## 3.9 AKS Advanced Networking — CNI, ingress, egress, policies, private clusters ★★★

**Definition:** The networking layer of AKS determines how pods get IP addresses, how traffic enters and leaves the cluster, and how pods are isolated from each other.

**Important Points**
- **Pod IP models:**
  - **Azure CNI (VNet-native):** every pod gets a VNet IP — routable from on-prem/peered networks, but **IP-hungry** and limited by subnet size and ENI density.
  - **Azure CNI Overlay:** pods get IPs from a private overlay CIDR; only nodes consume VNet IPs. This is the default recommendation for large/new clusters because it removes subnet exhaustion.
  - **kubenet:** legacy, limited features — not for new clusters.
  - **CNI powered by Cilium** (eBPF) provides network policy, service routing and better performance on supported versions.
- **Ingress options:** the **Application Routing add-on** (managed NGINX), **Application Gateway for Containers** / AGIC, or your own ingress controller. A `LoadBalancer` service creates an Azure LB per service — usually only for L4 services, not every app.
- **Egress options (`outboundType`):**
  - `loadBalancer` (default) — SNAT via a public LB; **port exhaustion risk** under high fan-out.
  - `managedNATGateway` / user-assigned NAT — predictable egress IPs, recommended for private APIs and partner allow-lists.
  - `userDefinedRouting` (UDR) — force egress through Azure Firewall/NVA for inspection and logging.
  - `none` — you provide the egress path (advanced).
- **Network policy:** requires a supported dataplane (Cilium or Calico). Default is allow-all between pods — in a multi-tenant cluster that is a lateral-movement problem. Start with default-deny ingress in a namespace and explicitly allow DNS + required paths.
- **Private cluster:** the API server gets a private endpoint; nodes and `kubectl` reach it privately. Requires private DNS, a jump host/Bastion or a self-hosted runner, and breaks any tooling that expects a public FQDN. `authorized IP ranges` is the lighter alternative when the API must stay public.
- **Service networking:** ClusterIP services, `kube-proxy`/Cilium service handling, DNS (CoreDNS) and **local DNS caching** for large clusters.
- **DNS and private endpoints:** workloads reaching PaaS over private endpoints need the `privatelink` zones linked to the **cluster VNet**, otherwise they resolve public IPs and fail.
- Use case: 500-pod cluster with CNI Overlay, egress via NAT Gateway for a partner allow-list, Cilium network policies per namespace, private API server, and ingress through Application Gateway with WAF.

**Edge Cases & Gotchas**
- **Subnet IP exhaustion** with Azure CNI is the number-one AKS outage: `failed to assign an IP address`. Check available IPs, `maxPods`, and pod density before blaming the scheduler.
- Changing CNI mode after creation is not supported — it is a rebuild decision.
- `userDefinedRouting` requires the UDR **and** a firewall that allows node-to-control-plane and node-to-node traffic; a missing rule produces a cluster that provisions but cannot pull images or join nodes.
- Default egress via LB SNAT shows up as intermittent timeouts to external APIs — monitor SNAT connection metrics.
- Network policies do not apply to host-network pods and are bypassed by some CNI paths — verify with a test pod.
- Private cluster + `kubectl` from a laptop silently fails until DNS resolves the private API endpoint; teams often "fix" it by re-enabling public access, which defeats the design.
- Overlay CIDR must not overlap the VNet or on-prem ranges, and it cannot be changed later without a rebuild.
- CoreDNS scaling/NDOTS issues cause widespread 5-second DNS latency — watch CoreDNS replicas and node pressure.

**Comparison**
- **Azure CNI** — when pods must be directly addressable from on-prem/peered networks.
- **CNI Overlay** — when you need scale and IP efficiency and do not require pod IPs to be routable.
- **Cilium** — when you need eBPF performance and richer network policy/observability.

**Interview Questions**
- **Basic — Why does AKS need a networking decision up front?** → CNI mode, pod CIDR, egress type and ingress model are effectively immutable per cluster and determine IP consumption, routability, security and cost.
- **Medium — How do you give a cluster predictable outbound IPs without opening it to the internet?** → Use `managedNATGateway` (or a user-assigned NAT Gateway) for stable egress IPs, keep the cluster private, and allow-list those IPs at the partner. Use UDR + Azure Firewall if egress must also be inspected.
- **Hard/Scenario — Pods in one namespace can reach a database in another namespace, which security forbids.** → Enable network policy with Cilium or Calico, apply a default-deny ingress policy in each namespace, then add explicit allows for DNS and the required service-to-service paths; verify with `kubectl exec` connectivity tests and audit the policies as code.

## 3.10 GitOps for AKS — Flux and Argo CD ★★

**Definition:** GitOps keeps a Git repository as the source of truth for cluster state, with an in-cluster agent continuously reconciling the live cluster to what Git declares.

**Important Points**
- **Flux** (CNCF, often deployed via the AKS **GitOps extension**) and **Argo CD** are the two common implementations; both watch Git and apply manifests/Helm/Kustomize.
- **Pull-based** model: the cluster agent pulls changes, so CI does not need cluster credentials — a major security win over `kubectl apply` from a pipeline.
- **Reconciliation loop** detects and reverts drift (`kubectl edit` changes are reverted). **Prune** removes resources deleted from Git — powerful and dangerous; start with prune disabled in production.
- **Structure:** `clusters/<env>/…` → Kustomize overlays or Helm values per environment; app-of-apps (Argo) or a root Kustomization (Flux) to bootstrap.
- **Promotion** = merging a PR that changes an image tag/digest; the same manifest set is promoted across environments with only overlay differences.
- **Secrets:** never in Git — use **External Secrets Operator** or the **Secrets Store CSI driver** with Key Vault, or SOPS-encrypted secrets.
- **Observability of reconciliation:** Argo CD sync status/health, Flux `Kustomization`/`HelmRelease` readiness conditions, and alerts on `OutOfSync`/reconcile failures.
- Use case: 4 clusters (dev/stage/prod/prod-dr) reconciled from one repo; image updates via automated PRs; drift alerts to Teams; secrets from Key Vault via workload identity.

**Edge Cases & Gotchas**
- **Drift is now visible** — and noisy. Teams must agree what "managed by GitOps" means, or hotfixes fight the controller in a revert loop.
- With **prune enabled**, removing a directory deletes production resources; guard with sync windows, approvals and a separate cluster-scoped directory.
- GitOps does not replace CI: images still need building, scanning and signing before the tag lands in Git.
- A broken manifest in the "root" app breaks **all** downstream reconciliation — use app-of-apps with health gates and canary clusters.
- Secrets accidentally committed are still in Git history — rotate, don't just delete the file.
- Argo CD manages cluster-scoped resources and RBAC if you let it; scope its permissions tightly per cluster.
- Reconciliation lag means "merged" ≠ "running" — deploy verification must read cluster state (Argo sync status health), not assume success.

**Comparison**
- **GitOps (Flux/Argo)** — declarative, continuously reconciled, audit trail in Git, drift correction.
- **CI push (`kubectl apply`/Helm in a pipeline)** — simpler for a single cluster, but needs cluster credentials in CI, drifts after the pipeline finishes, and leaves no continuous reconciliation.

**Interview Questions**
- **Basic — What is GitOps?** → Git as the single source of truth for desired state, with an in-cluster agent continuously reconciling the cluster to it.
- **Medium — How do you handle secrets in a GitOps repository?** → Keep them out of Git: External Secrets Operator or the CSI driver pulling from Key Vault with workload identity, or SOPS/sealed secrets with the decryption key held in the cluster.
- **Hard/Scenario — A developer hotfixed production with `kubectl edit` and the fix disappeared.** → Expected behaviour: the reconciler reverted the drift. Recover by applying the change through Git (PR → merge → reconcile), and use a drift-alerting workflow plus an agreed emergency procedure (a documented break-glass that still lands in Git afterwards).

---

# PART 4 — STORAGE

## 4.1 Azure Storage Accounts ★★★

**Definition:** A storage account is a unique namespace and management boundary for Blob, File, Queue and Table storage, with a chosen performance tier, redundancy and access controls.

**Important Points**
- **Account kinds:** general-purpose v2 (Standard) is the default; **Premium** variants for block blobs, files, page blobs; **BlobStorage** legacy.
- **Endpoints:** `<account>.blob.core.windows.net`, `.file.`, `.queue.`, `.table.`, `.dfs.` (ADLS Gen2 hierarchical namespace).
- **Performance:** Standard (HDD-backed, per-GB capacity + transactions) vs Premium (SSD, performance-oriented).
- **Redundancy:** LRS, ZRS, GRS, RA-GRS, GZRS, RA-GZRS (see 4.2).
- **Access:** account keys (full control — avoid), SAS, Entra ID + RBAC data-plane roles (`Storage Blob Data Reader/Contributor/Owner`), shared key access can be disabled.
- **Network:** public endpoint + firewall (selected networks/VNet rules), service endpoints, **private endpoints**, `publicNetworkAccess: Disabled`.
- **Security:** encryption at rest (Microsoft-managed or CMK), infrastructure encryption (double), TLS minimum version, secure transfer required, **soft delete** for blobs/containers/files, **versioning**, **immutable storage (WORM)**, **object replication**.
- **Limits:** account name uniqueness, 5 PiB capacity per account (verify), per-account scale targets and egress limits.
- Use case: one storage account per workload/environment with private endpoints, RBAC-only access, soft delete and lifecycle policies.

**When to use / alternatives:** **Blob** for objects, static assets, backups and data-lake files. **Azure Files** for SMB/NFS shares shared between machines. **Managed Disks** for VM OS/data volumes. **NetApp Files** when you need advanced NFS/SMB features (snapshots, dual-protocol, volume clones). **Queue/Table** for simple messaging and key-value at low cost. Do not use blob storage as a POSIX filesystem for write-heavy workloads.
**Edge Cases & Gotchas**
- **Keys are all-powerful** — a leaked key bypasses RBAC entirely; prefer Entra ID + disable shared key access.
- `ReadOnly` resource locks still allow data-plane writes; they block control-plane updates but **listing keys** (a POST) is blocked, which breaks tools.
- Disabling shared key access breaks legacy apps/SAS signed with account keys — plan migration to user-delegation SAS.
- Account-level limits can throttle many workloads sharing one account — shard across accounts for very high throughput.
- **Firewall "Allow Azure services"** is broad — it includes other tenants' Azure resources in some configurations; prefer private endpoints.
- Turning on hierarchical namespace (ADLS Gen2) is **irreversible**.
- Changing redundancy (LRS→GRS) initiates an async conversion; performance/replication lag during conversion.
- Deleting a storage account deletes all data — soft delete doesn't protect account deletion unless configured (and recoverable only within the retention window).

**Production Troubleshooting**
```bash
# 1. Network path / auth mode: who is calling and is public access blocked?
az storage account show -n <acct> -g <rg> --query "{publicNetworkAccess:publicNetworkAccess,defaultAction:networkRuleSet.defaultAction,allowSharedKey:allowSharedKeyAccess}"

# 2. Does the identity hold a DATA-PLANE role? (Contributor is not enough)
az role assignment list --scope <storage-account-id> --include-inherited \
  --query "[].{principal:principalName,role:roleDefinitionName}"

# 3. Resolve privately from the workload
nslookup <acct>.blob.core.windows.net
```
Interpretation: `AuthorizationPermissionMismatch`/403 with a valid identity = missing `Storage Blob Data Reader/Contributor` (management-plane roles do not grant data access). 403 after disabling public access = private endpoint/DNS. `KeyBasedAuthenticationNotPermitted` = shared key access disabled by policy — switch the client to Entra ID/managed identity or user-delegation SAS.

**Interview Questions**
- **Basic — What is a storage account?** → A namespace and management boundary for Azure Storage services with a chosen redundancy and performance tier.
- **Medium — Account key vs Entra ID?** → Keys grant full data access and bypass RBAC; Entra ID + RBAC gives identity-based, auditable least-privilege access (and supports user-delegation SAS).
- **Hard/Scenario — After disabling public network access, an app breaks.** → It was reaching the public endpoint; enable a private endpoint in the app's VNet, link the `privatelink.blob.core.windows.net` zone, ensure DNS resolves privately, and check firewall rules for any remaining public clients. Then validate authentication separately (managed identity + RBAC role).

## 4.2 Azure Storage Redundancy ★★★

**Definition:** Redundancy options determine how many copies of data Azure keeps and where: LRS (3 copies in one datacenter), ZRS (3 copies across zones), GRS/GZRS (plus a secondary Region), RA- variants (read access to the secondary).

**Important Points**
- Redundancy is chosen **per storage account at creation** (and can be changed with constraints) — decide with the workload's durability and residency requirements, not by default.
- Synchronous copies (LRS/ZRS) survive infrastructure failure; asynchronous copies (GRS/GZRS) survive Region failure with a nonzero RPO.
- Redundancy protects against hardware/infrastructure failure only — it replicates deletions and corruption too.
- Read access to the secondary (RA-) is eventually consistent and is billed as a separate capability.
- Cost ordering (roughly): LRS < ZRS < GRS < GZRS, with RA- variants above their base.

| Option | Copies | Scope | Read from secondary | Use case |
| --- | --- | --- | --- | --- |
| LRS | 3 | One datacenter in one Region | No | Dev/test, cheap, non-critical |
| ZRS | 3 | 3 zones in one Region | No | Production within a Region |
| GRS | 6 | 3 local + 3 in paired Region | No | Regional DR (secondary not readable) |
| RA-GRS | 6 | Same as GRS | **Yes** | Read-scale + DR |
| GZRS | 6 | 3 zones + 3 in paired Region | No | Maximum durability/regional HA |
| RA-GZRS | 6 | Same as GZRS | **Yes** | Best durability + read access |

- **RPO:** GRS/GZRS async replication is typically within 15 minutes (Microsoft-documented target — verify).
- Failover to the secondary is **customer-initiated** (account failover) for GRS/GZRS; RA-GRS read access is always available at the `-secondary` endpoint.
- **Account failover** may lose data written after the last replication (RPO), and after failover the account becomes LRS in the former secondary until re-replicated.
- Use case: production blobs on **ZRS** within a Region, compliance backups on **GZRS**, read-heavy global reads via **RA-GRS**.

**Edge Cases & Gotchas**
- GRS replicates to that Region's **current paired Region**, which may be in another country — a data-residency conflict. Verify the live pair mapping (`az account list-locations` / Microsoft's cross-region replication docs) rather than a remembered pairing.
- RA-GRS is **eventually consistent**; reading the secondary can return stale data.
- Account failover requires a support-independent operation but causes downtime while DNS/endpoints switch; some features are unavailable after failover.
- You cannot convert some redundancy configurations freely (e.g., ZRS availability varies by Region and account type).
- Redundancy protects against **infrastructure** failure, not accidental deletion or ransomware — that needs soft delete/versioning/immutable storage/backup.
- Object replication (blob-to-blob across accounts/Regions) is a different mechanism with its own lag and policy requirements.

**Interview Questions**
- **Basic — What's the difference between LRS and ZRS?** → LRS keeps 3 copies in one datacenter; ZRS keeps 3 copies across three Availability Zones in a Region.
- **Medium — GRS vs RA-GRS?** → Both replicate to a paired Region; RA-GRS also allows reads from the secondary endpoint.
- **Hard/Scenario — Compliance mandates no data leaves India, but the team wants maximum durability.** → Use ZRS (or LRS where ZRS isn't available) inside India, plus in-Region versioning/soft delete/immutable policies and backups; GRS/GZRS would replicate outside India to the paired Region. Document the trade-off and validate against the actual pair location.

## 4.3 Blob Storage — Tiers, Lifecycle & Features ★★★

**Definition:** Blob Storage stores unstructured objects (block/append/page blobs) with access tiers, lifecycle rules, versioning and change feeds.

**Important Points**
- **Blob types:** block blobs (files/media — default), append blobs (logs), page blobs (VHDs/disks).
- **Access tiers:** **Hot**, **Cool** (30-day min), **Cold** (90-day min), **Archive** (180-day min, offline, rehydration required), plus **Premium** block blob (SSD) accounts. Tier can be set at upload, per-blob, or via lifecycle.
- **Lifecycle management:** rules on prefix/tags to tier down, delete, and delete old versions/snapshots.
- **Versioning** + **soft delete** (blob and container) — the practical ransomware/accidental-delete defence.
- **Immutable storage:** time-based retention and legal hold (WORM).
- **Change feed** for ordered change logs; **event subscriptions** to Event Grid for reactive processing.
- **Static website hosting**, **custom domain**, **CDN/Front Door** in front.
- **ADLS Gen2** hierarchical namespace for analytics workloads (irreversible conversion).
- **Blob index tags** and **object replication** for cross-account/Region copies.
- **Scale targets:** block blob throughput per account; use multiple accounts/prefixes for very high rates.
- Use case: app media in Hot → Cool at 30 d → Archive at 180 d, versioning + soft delete enabled, lifecycle deletes old versions at 90 d.

**Edge Cases & Gotchas**
- **Archive-tier blobs cannot be read directly** — rehydrate (hours) or copy to a Hot tier; a restore workflow must exist before you need it.
- Early deletion from Cool/Cold/Archive incurs charges for the remaining minimum duration.
- Lifecycle rules run **once per day** and can take up to 48 h to take effect — not immediate.
- Versioning without lifecycle cleanup grows storage cost indefinitely (old versions are billable).
- Soft delete protects deletes but not all overwrites unless versioning is on.
- Blob leases prevent concurrent writes; a forgotten lease blocks deployments.
- Static website hosting serves public content — don't enable for internal data.
- Rehydration priority (Standard vs High) affects cost/time.
- Metadata-only tier changes do not require re-upload; the completeness of the move depends on the operation.

**Interview Questions**
- **Basic — Hot vs Cool vs Archive?** → Hot for frequent access, Cool for infrequent with 30-day minimum, Archive for offline long-term with rehydration delays and 180-day minimum.
- **Medium — How do you protect blobs from accidental deletion or ransomware?** → Soft delete (blobs + containers), versioning, immutable time-based retention, resource locks on the account, least privilege (no account keys), Defender for Storage, and separate backup/controlled retention.
- **Hard/Scenario — Storage cost doubled with no traffic growth.** → Check versioning/old versions, snapshots, incomplete uploads, blobs in Hot that should be Cool/Archive, lifecycle rules not applied (prefix/tag mismatch), replication/SAS churn, and transaction-heavy small reads. Use Storage Insights/Cost Analysis by meter.

## 4.4 Shared Access Signatures (SAS) & Access Management ★★★

**Definition:** A SAS is a signed URL granting time-limited, permission-scoped access to storage resources without sharing account keys.

**Important Points**
- **Types:**
  - **User delegation SAS** — signed with an Entra ID credential; most secure; blob only; max validity typically 7 days.
  - **Service SAS** — signed with an account key (or a stored access policy); scoped to one service.
  - **Account SAS** — signed with an account key; broad access across services.
- **Constraints:** permissions (r/w/d/l/a/c), start/expiry, allowed IP range, allowed protocols (HTTPS only), stored access policy for revocation.
- **Stored access policies** on containers/queues/tables/files let you revoke/alter service SAS without rotating keys.
- **Revocation:** user delegation key revoke; delete/modify the stored access policy; rotate the account key (invalidates all key-signed SAS — blunt instrument).
- **Best practice:** short expiry, least permissions, HTTPS+IP restriction where possible, prefer user delegation, never log or email SAS URLs, and never embed in public client code.
- Use case: mobile app uploads via a user-delegation SAS issued by an API after authentication; partners get a read-only SAS for 1 hour.

**Edge Cases & Gotchas**
- **A SAS is a bearer token** — anyone with the URL has the access until expiry; there's no per-user attribution beyond the request logs.
- Account-key-signed SAS is invalidated by key rotation — which may be your only revocation option, so it breaks all consumers.
- Deleting the stored access policy revokes all SAS referencing it.
- Clock skew and long expiries create security holes.
- `spr=https` is not set by default in some SDK paths — enforce it.
- SAS cannot grant more permissions than the signer has (for user delegation).
- SAS in a public repo/browser history = incident; treat it like a password.

**Interview Questions**
- **Basic — What is a SAS?** → A signed URL granting scoped, time-limited access to a storage resource without exposing keys.
- **Medium — SAS vs RBAC?** → RBAC authorizes identities continuously and is centrally revocable; SAS delegates access to anyone holding the URL for its lifetime.
- **Hard/Scenario — A SAS URL was leaked publicly. How do you revoke it fast?** → Identify the SAS type: revoke the user delegation key, or delete/modify the stored access policy, or (for account-key SAS without a policy) rotate the account key. Then review logs for access, shorten future expiries, restrict by IP/protocol, and move to Managed Identity where possible.

## 4.5 Azure Files, Disks & Data Lake ★★★

**Definition:** Azure Files provides managed SMB/NFS shares; Managed Disks provide block storage for VMs; ADLS Gen2 is blob storage with a hierarchical namespace for analytics.

**Important Points**
- **Azure Files:** SMB 3.x (Windows/Linux/macOS), NFS 4.1 (Premium only), Azure File Sync for on-prem caching, identity-based auth via AD DS/Entra Domain Services/Kerberos, snapshots, backup via Azure Backup, soft delete, larger share sizes on Premium.
- **Managed Disks:** Standard HDD, Standard SSD, **Premium SSD**, **Premium SSD v2** (independent IOPS/throughput, no size-based provisioning), **Ultra Disk** (configurable to very high IOPS, zonal, for tier-1 DBs).
- **Disk caching**, burst credits (smaller P-series), host caching recommendations per workload.
- **Shared disks** for clustered apps (WSFC, Pacemaker) — require cluster-aware file systems.
- **Disks are zonal** with the VM; snapshots/incremental snapshots and disk encryption sets (CMK) are supported.
- **ADLS Gen2:** hierarchical namespace, POSIX ACLs, Blob API compatibility, used by Synapse/Databricks/ADF.
- Use case: FSLogix profiles on Azure Files Premium with Entra Kerberos; SQL data disks on Premium SSD v2; analytics lake on ADLS Gen2.

**Edge Cases & Gotchas**
- Azure Files performance is limited by share size/tier and protocol (SMB encryption adds latency); not suitable for databases.
- NFS Azure Files requires Premium and a VNet; no identity-based auth like SMB.
- File Sync agent and server endpoints have limits (per-server, per-share) and cloud-tiering policies must be tuned.
- Disk performance is bounded by both disk SKU **and VM** (uncached IOPS/throughput limits) — resizing the disk may not help if the VM caps it.
- Premium SSD v2 and Ultra have Region/zone availability restrictions and cannot be used as OS disks.
- Bursting on P-series only applies below certain sizes; sustained IOPS can drop.
- Increasing disk size does not automatically grow the partition/filesystem.
- ADLS Gen2 ACLs can conflict with RBAC — effective permission evaluation is a frequent confusion point.

**Interview Questions**
- **Basic — What is Azure Files?** → Managed SMB/NFS file shares accessible from Windows/Linux/macOS and Azure File Sync.
- **Medium — Premium SSD vs Ultra Disk?** → Premium SSD has size-based performance tiers and broad support; Ultra offers independent, very high IOPS/throughput with zonal constraints and higher cost.
- **Hard/Scenario — A database VM has high disk latency despite Premium SSD.** → Check VM size's max uncached IOPS/throughput, disk queue depth and I/O size, host caching settings, whether the workload exceeds the disk's provisioned performance, and whether spreading across multiple disks/Ultra/Premium v2 is needed. Validate with Azure Monitor disk metrics (`OS Disk/Data Disk Queue Depth`, `IOPS Consumed %`).

## 4.6 Storage Security & Encryption ★★★

**Definition:** Azure Storage encrypts all data at rest by default and offers multiple layers of network and identity control.

**Important Points**
- **Encryption at rest:** SSE with Microsoft-managed keys by default; **CMK** via Key Vault (account-level scope), **infrastructure encryption** (double encryption), and encryption in transit (TLS 1.2+).
- **CMK requires a user-assigned managed identity** with `get/wrapKey/unwrapKey` on the key vault; if the identity or key is disabled, storage operations fail.
- **Network controls:** private endpoints, selected networks (VNet/subnet + IP rules), `publicNetworkAccess: Disabled`, "Allow trusted Microsoft services" exception (needed for some Azure services like Backup).
- **Auth:** Entra ID RBAC (recommended), user delegation SAS, service SAS, account keys (restrict/disable).
- **Data protection:** soft delete, versioning, immutable storage, object replication, backup (operational vs vaulted).
- **Detection:** Defender for Storage (activity/anomaly detection, malware scanning where available), Storage analytics/insights, Activity Log.
- Use case: CMK-backed storage with a customer key vault, private endpoints, shared key disabled, Defender for Storage on, immutable retention for audit blobs.

**Edge Cases & Gotchas**
- A disabled/deleted CMK or a revoked Key Vault permission causes a **storage outage** for every operation — monitor key vault availability and use purge protection.
- CMK rotation must be planned (key version pinning vs auto-update).
- Disabling shared key access breaks AzCopy/Storage Explorer/legacy SDKs using keys — migrate them first.
- "Allow trusted Microsoft services" can be broader than expected; validate which services need it.
- Soft delete doesn't protect against a malicious principal with delete permissions on the whole account — use locks + immutable storage + least privilege.
- Cross-tenant private endpoint approval can hang deployments; coordinate owners.
- Encryption does not prevent data exfiltration by an authorized identity — monitor egress and anomalous access.

**Interview Questions**
- **Basic — Is Azure Storage encrypted by default?** → Yes, at rest with Microsoft-managed keys, and in transit with TLS.
- **Medium — How do CMKs work for storage?** → A user-assigned managed identity gets Key Vault key permissions; the storage account uses that identity to wrap/unwrap the account encryption key. Revoking it makes the account inaccessible.
- **Hard/Scenario — After moving to customer-managed keys, backup jobs fail.** → The backup service needs access to the key (via the key vault permissions/trusted services) and network access to the account; verify the key vault firewall allows Azure Backup, the key is enabled, the identity has wrap/unwrap, and "trusted Microsoft services" is enabled as required.

---

# PART 5 — DATABASES

## 5.1 Azure SQL Database ★★★

**Definition:** A fully managed SQL Server-engine relational database (DBaaS) with built-in HA, backups, patching and multiple purchasing models.

**Important Points**
- **Deployment options:** **Single database**, **Elastic pool** (shared resources across many DBs), **Managed Instance** (near-full instance compatibility), **SQL Server on VM** (full control, you manage everything).
- **Purchasing models:** **DTU** (bundled) vs **vCore** (compute + storage + IOPS separately; **serverless** with auto-pause; **Hyperscale** for very large, fast-scaling databases).
- **Service tiers:** General Purpose, Business Critical (local SSD + readable secondary, in-memory OLTP), Hyperscale (page servers, fast restore, up to 100 TB).
- **HA:** built-in (locally redundant by default); **zone-redundant** configuration for AZ resilience; Business Critical includes an Always On availability group with a readable secondary.
- **Backups:** automated full/differential/log backups, **PITR 7–35 days**, **long-term retention** up to 10 years, geo-restore, **failover groups** for cross-Region.
- **Security:** Entra ID authentication (MFA, managed identity), TDE with service-managed or CMK, Always Encrypted, Dynamic Data Masking, auditing, Advanced Threat Protection/Defender, private endpoints, firewall rules.
- **Performance:** Query Store, automatic tuning, Intelligent Insights, read scale-out (secondary), elastic query.
- **Networking:** public endpoint with firewall rules, **private endpoint**, service endpoint, "Allow Azure services" (avoid in production).
- Use case: multi-tenant SaaS with elastic pools; business-critical app with zone-redundant Business Critical and a failover group to a secondary Region.

**When to use / alternatives:** **Azure SQL Database** for app databases needing managed HA, PITR and elastic scale. **Managed Instance** when the app needs instance-level SQL Server features (Agent, cross-DB queries, linked servers). **SQL on VM** when you need OS/host control or unsupported features. **PostgreSQL/MySQL Flexible Server** for open-source engines. **Cosmos DB** when global distribution and multi-region writes matter more than relational joins.
**Edge Cases & Gotchas**
- Azure SQL DB is **not** the same as SQL Server on a VM — instance-level features (Agent, cross-database queries in some modes, CLR, certain server roles) need Managed Instance or a VM.
- **Failover group forced failover can lose data** if the secondary hasn't caught up (async replication) — know your RPO.
- The failover group **listener endpoint** must be used in connection strings, otherwise failover doesn't help.
- Connection limits and tier limits cause intermittent errors under load — pool connections, use retry logic.
- **Private endpoint + firewall**: disabling public access breaks tools using public endpoints (SSMS from a laptop).
- Auto-pause (serverless) causes cold-start latency on first connection.
- DTU→vCore migration needs capacity assessment.
- Long-running transactions, missing indexes, and parameter sniffing remain your problem — it's managed, not magic.
- Deleting a server deletes all its databases; PITR can't restore a dropped database beyond the retention window.

**Production Troubleshooting**
```bash
# 1. Is the database the bottleneck, or is the app waiting/reconnecting?
az sql db show -g <rg> -s <server> -n <db> --query "{status:status,sku:currentSku.name,zoneRedundant:zoneRedundant}"
az monitor metrics list --resource <db-id> --metric cpu_percent dtu_consumption_percent connection_successful connection_failed --interval PT1M --offset 1h

# 2. Who is connected, and what are they running? (Query Store / DMV via the query editor or sqlcmd)
#    SELECT TOP 10 qsqt.query_sql_text, rs.avg_cpu_time FROM sys.query_store_runtime_stats ...
sqlcmd -S <server>.database.windows.net -d <db> -G -Q "SELECT COUNT(*) FROM sys.dm_exec_sessions"
```
Interpretation: `connection_failed` spiking with `connection_successful` flat = connection storm or firewall/private-endpoint issue, not CPU. CPU pinned + Query Store showing one expensive query = missing index/plan regression. `status: Paused` on serverless = auto-pause cold start. Latency after a failover with connections failing = DNS/reconnect, fix with retry logic and the failover-group listener.

**Interview Questions**
- **Basic — What is Azure SQL Database?** → A managed relational DB based on SQL Server with automated patching, backups and HA.
- **Medium — Azure SQL DB vs Managed Instance?** → SQL DB is optimized for cloud app databases with limited instance-level features; Managed Instance offers near-full SQL Server compatibility (Agent, cross-DB queries, instance-level features) with managed operations.
- **Hard/Scenario — The primary Region fails. Restore database connectivity.** → Use an auto-failover group (automatic) or manual failover to the geo-secondary, connect using the failover group listener (not the server name), validate authentication (Entra/managed identity), network access from the app Region, and application retry logic. Then confirm data loss within RPO and plan failback.

## 5.2 Azure SQL — HA, Backups & Geo-Replication ★★★

**Definition:** Three distinct mechanisms: built-in local HA (zone redundancy), automated backups (PITR/LTR), and geo-replication/failover groups (cross-Region DR).

**Important Points**

| Mechanism | Protects against | RPO | RTO | How |
| --- | --- | --- | --- | --- |
| Zone-redundant HA | Datacenter/AZ failure | ~0 (sync) | Seconds–minutes | Built-in, needs ZR tier/Region |
| Automated backups + PITR | Data corruption, accidental delete | Up to minutes | Minutes–hours | Restore to point in time (same Region) |
| Geo-restore | Regional disaster with backups | Backup interval | Hours | Restore from geo-redundant backups into another Region |
| Active geo-replication | Regional disaster | Seconds–minutes (async) | Minutes | Readable secondary; manual failover |
| **Auto-failover group** | Regional disaster | Seconds–minutes (async) | Minutes (automatic policy) | Listener endpoint, read-write/read-only |

- **PITR** default 7 days (up to 35); **LTR** weekly/monthly/yearly up to 10 years.
- **Geo-redundant backup storage** is a configuration choice — verify it is on if you rely on geo-restore.
- **Failover groups** support automatic failover with a grace period, and read-only listener routing to the secondary.
- Backups are **encrypted**; CMK-protected databases restrict restore across subscriptions (use the same key).
- Use case: Business Critical zone-redundant primary in `centralindia`, failover group to `southindia`, PITR 35 days + LTR 7 years.

**Edge Cases & Gotchas**
- **Zone redundancy requires a supported tier and Region** — the default may be locally redundant only.
- Geo-replication is **asynchronous** — forced failover can lose the tail of transactions.
- Backups are not a substitute for DR if `geo-redundant backup storage` is disabled.
- PITR cannot go earlier than the retention window; a drop beyond retention is unrecoverable.
- Failover group failover changes the primary; connection strings using the listener survive, server-name strings do not.
- After failover, the old primary may need re-seeding.
- CMK/TDE with customer keys: if the key vault is in the failed Region, the database may be unavailable — keep keys in a resilient, accessible key vault (and in both Regions where required).
- Elastic pool max size and per-DB limits interact — one DB can consume the pool.

**Interview Questions**
- **Basic — What's the difference between PITR and a failover group?** → PITR restores a database to an earlier point (data recovery); a failover group redirects the app to a secondary Region (service continuity).
- **Medium — Explain RPO/RTO for geo-replication.** → Replication is asynchronous, so RPO is seconds-to-minutes of potential data loss; RTO is the failover + app reconnect time (minutes) provided the app uses the listener and capacity exists.
- **Hard/Scenario — A developer ran DELETE without WHERE in production.** → Restore to a point in time just before the deletion into a **new** database, validate the data, then copy the affected rows back (or switch over). This is why PITR retention, LTR, least privilege and `DELETE` guardrails matter. Failover groups would not help here.

## 5.3 Azure SQL Managed Instance & SQL on VM ★★

**Definition:** Managed Instance is a PaaS deployment of SQL Server with near-full instance compatibility inside a VNet; SQL on VM is IaaS with full control.

**Important Points**
- **MI:** instance-level features (SQL Agent, linked servers, cross-database queries, service broker, CLR), VNet deployment, private IP, built-in HA (zone-redundant option), PITR/LTR, failover groups.
- **MI subnet requirements:** dedicated delegated subnet, minimum size (large — verify), NSG/UDR rules; no other resources in the subnet.
- **SQL on VM:** you manage OS, patching, HA (Always On AG), backups, and licensing (AHB applies); best for legacy apps needing OS/host control.
- Use case: lift-and-shift of a legacy app depending on SQL Agent jobs and cross-DB joins → MI; vendor app requiring OS-level components → SQL on VM.

**Edge Cases & Gotchas**
- MI deployment takes hours and needs a large empty subnet — plan network first.
- Some features remain unsupported vs on-prem (e.g., certain FILESTREAM/CLR or replication options — verify).
- MI has no public endpoint by default; you need a VNet/peering/private endpoint or a public endpoint opt-in (discouraged).
- SQL on VM HA requires you to build AGs across zones and handle quorum — often underestimated.
- Licensing: AHB can halve cost, but only for eligible licences with Software Assurance.

**Interview Questions**
- **Basic — When would you choose Managed Instance?** → When the app needs SQL Server instance-level features but you still want PaaS operations.
- **Medium — MI vs SQL DB?** → MI gives instance-level compatibility and VNet-native deployment; SQL DB is simpler, more elastic and cheaper for app databases.
- **Hard/Scenario — A legacy app uses SQL Agent jobs, linked servers and cross-DB queries.** → Managed Instance (or SQL on VM if OS-level dependencies exist); validate feature support, size the subnet, configure HA/failover group, and test the jobs/linked server security context.

## 5.4 Azure Cosmos DB ★★★ · `TIER 2 — core mechanics only`

**Definition:** A globally distributed, multi-model NoSQL database with turnkey multi-Region replication and five tunable consistency levels.

**Important Points**
- **APIs:** NoSQL (SQL API), MongoDB, Cassandra, Gremlin, Table. *(Awareness only — know NoSQL is the default and that the others exist; do not memorise each API's quirks.)*
- **Partition key** determines distribution and scalability; a **logical partition** max is 20 GB; throughput is spread across physical partitions.
- **Throughput:** **RU/s** (provisioned, database or container level), **autoscale** (max RU/s, scales down when idle), **serverless** (per-operation, single Region). RU cost varies by operation/item size/indexing.
- **Consistency levels (strongest → weakest):** Strong, Bounded staleness, Session (default), Consistent prefix, Eventual. Strong is only possible in a single write Region.
- **Multi-Region:** single write + read Regions, or **multi-region writes** (active-active) with conflict resolution (last-write-wins or stored procedure); **conflict feed**.
- **Indexing:** automatic, policy-based; exclude unused paths to reduce RU/write cost; composite indexes for ORDER BY on multiple fields.
- **Integration:** **change feed** (event sourcing, materialised views) and **TTL**. *(Skip stored-procedure/trigger internals unless the role is Cosmos-heavy.)*
- **Security:** keys (dangerous), Entra ID RBAC + data-plane roles, private endpoint, firewall, customer-managed keys.
- Use case: globally distributed product catalogue with session consistency; IoT device state with TTL and change feed to analytics.

**Edge Cases & Gotchas**
- **Hot partition** — a low-cardinality partition key (e.g., `status`, `tenantId` for one huge tenant) caps throughput and throttles with 429s.
- 429s are **rate limiting, not errors** — the SDK retries; monitor `NormalizedRUConsumption` and `TotalRequests` by status code.
- Cross-partition queries are expensive and slower; design for partition-key-scoped reads.
- **Strong consistency + multi-region** is not allowed; consistency changes need planning.
- Multi-region writes conflict resolution can silently overwrite values — model last-writer-wins semantics carefully.
- Indexing everything inflates write RU cost; exclude unused paths.
- Autoscale has a minimum of 10% of max RU/s charged even at low traffic.
- Serverless cannot span Regions and has burst limits.
- Backup: periodic (default) vs continuous (PITR) — configure explicitly.

**Interview Questions**
- **Basic — What is Cosmos DB?** → A globally distributed, multi-model NoSQL service with tunable consistency and automatic replication.
- **Medium — Which consistency level would you choose and why?** → Session for most apps (per-client consistency with low latency). Strong only if you need linearizability and can accept single-Region writes; Eventual for telemetry where staleness is fine.
- **Hard/Scenario — One tenant generates most of the traffic and requests 429.** → Confirm the hot partition with metrics, then redesign the partition key (add a suffix/hash bucket for write sharding, or split large tenants into their own containers), increase RU/s or enable autoscale, cache hot reads, and exclude unused index paths to reduce write RU cost. Re-check `NormalizedRUConsumption` per partition.

## 5.5 Azure Database for MySQL / PostgreSQL (Flexible Server) ★★★

**Definition:** Managed open-source databases with the Flexible Server deployment model (VNet integration, zone-redundant HA, configurable maintenance).

**Important Points**
- **Flexible Server** is the current model; Single Server retirement is staged across Regions — **verify**. Features: **zone-redundant HA** (or same-zone HA), burstable/general/memory tiers, storage autogrow, read replicas (up to 5, cross-Region), PITR 7–35 days, geo-restore, private access (VNet injection/private endpoint) or public access with firewall.
- **PostgreSQL extensions** and `shared_preload_libraries` supported via server parameters; PgBouncer built in for connection pooling (verify version support).
- **Maintenance windows** and **planned maintenance notifications**; minor version auto-upgrade.
- **Performance:** Query Store-like `pg_stat_statements`, slow query log, Performance Recommendations, metrics in Azure Monitor.
- **Authentication:** password or Entra ID for PostgreSQL/MySQL (verify version support), SSL enforcement.
- Use case: a Spring Boot app on MySQL Flexible Server with zone-redundant HA, private VNet access and PITR 14 days.

**Edge Cases & Gotchas**
- **HA failover** takes seconds to a minute; the application must retry connections — the endpoint name stays the same but IPs change.
- VNet-injected servers consume delegated subnet IPs and cannot be moved easily.
- Storage can grow but not shrink; IOPS scale with size on some tiers.
- Read replicas are asynchronous (lag) and do not participate in HA.
- TLS enforcement and legacy client certificate chains break older drivers.
- Connection storms: enable PgBouncer or a pool; max_connections is tier-bound.
- Maintenance windows apply to HA and can cause a brief failover.
- Backup retention is capped; long-term archival needs export.

**Interview Questions**
- **Basic — What is a Flexible Server?** → The current managed deployment for MySQL/PostgreSQL with VNet integration, HA options and configurable maintenance.
- **Medium — Zone-redundant vs same-zone HA?** → Zone-redundant places the standby in another AZ (survives an AZ failure); same-zone HA protects against host failure only, with lower latency and cost.
- **Hard/Scenario — After an HA failover, the app throws connection errors for a minute.** → Expected: DNS/IP change and connection drops. Implement retry with backoff and connection validation in the app/driver, brief DNS caching, health checks, and set the app's connection pool to discard stale connections. Validate with a planned failover test.

## 5.6 Azure Cache for Redis / Managed Redis ★★★

**Definition:** A managed Redis service for caching, session state, rate limiting and messaging, with tiers from Basic to Enterprise.

**Important Points**
- **Tiers:** Basic (single node, dev), Standard (replicated), Premium (higher throughput, VNet, clustering, persistence, geo-replication), Enterprise/Enterprise Flash (Redis Enterprise modules, active-active geo), and **Azure Managed Redis** (newer offering — verify status/features).
- **Networking:** public endpoint with firewall, **private endpoint**, VNet injection (Premium), **Private Link**.
- **Auth:** access keys (default), **Entra ID authentication** (verify tier support), TLS-only, disable non-TLS port.
- **Features:** data persistence (RDB/AOF, Premium+), clustering/shards, geo-replication, **zone redundancy** (Premium/Enterprise), scheduled updates, patching windows.
- **Patterns:** cache-aside, write-through, session store, distributed locks (RedLock caveats), rate limiting counters, pub/sub.
- Use case: session cache for a web farm, product cache with 5-minute TTL, rate limiting for an API.

**Edge Cases & Gotchas**
- **Eviction policy** (`allkeys-lru`, `volatile-lru`, `noeviction`) determines whether writes fail or keys get dropped — a misconfigured policy causes silent data loss or write errors.
- Cache stampede after failover/flush can take down the database behind it.
- Premium/Enterprise clustering changes multi-key operations — use hash tags.
- Public endpoint exposure is a common finding; use private endpoints and disable non-TLS ports.
- Redis is single-threaded per shard — O(N) commands (`KEYS`, big `SMEMBERS`) stall it.
- Data is not durable by default; never make the cache the only copy.
- In-Region geo-replication is not the same as cross-Region DR; know the failover procedure.

**Interview Questions**
- **Basic — What is Azure Cache for Redis used for?** → In-memory caching, session state, rate limiting and low-latency data structures.
- **Medium — How do you secure a cache?** → Private endpoint/VNet, TLS-only, Entra ID or tightly managed keys stored in Key Vault, firewall rules, and disable public access.
- **Hard/Scenario — After a cache node failover, the SQL database is overwhelmed.** → Cache went cold and every request hit the DB. Immediate: rate-limit/queue, scale DB, warm the cache. Permanent: zone-redundant/replicated cache, request coalescing, jittered TTLs, circuit breakers, and DB headroom.

## 5.7 Azure Synapse, Data Factory & Fabric ★ · `TIER 3 — awareness`

**Definition:** Synapse is a unified analytics platform (dedicated/ serverless SQL pools, Spark, pipelines); Data Factory is managed data integration/ETL; Microsoft Fabric is the newer unified analytics SaaS (verify current positioning).

**Important Points**
- **Synapse dedicated SQL pool** is provisioned MPP warehousing (DWUs); **serverless SQL pool** queries data lake files on demand; **Spark pools** for big data; **pipelines** for orchestration.
- **Pipelines:** linked services, datasets, activities, integration runtime (Azure/Auto-hosted/SSIS), triggers, mapping data flows.
- **Data Lake/ADLS Gen2** is the storage layer; **PolyBase/COPY** for loading.
- **Microsoft Fabric** consolidates Power BI, Data Factory, Synapse-style warehousing and lakehouse into one SaaS platform (OneLake, capacity-based licensing) — verify what your organisation uses.
- Use case: nightly ADF pipeline → ADLS → Synapse serverless queries for BI.

**Edge Cases & Gotchas**
- Dedicated SQL pools bill while running — pause in non-prod (but resuming takes minutes).
- Serverless SQL bills per TB of data processed — partition/columnarise.
- ADF integration runtime placement determines network access; self-hosted IR needs a VM and HA.
- Data skew and distribution choices dominate dedicated pool query performance.
- Fabric licensing is capacity-based and can be significantly more expensive if undersized.

**Interview Questions**
- **Basic — What is Azure Data Factory?** → A managed orchestration/ETL service for moving and transforming data across sources.
- **Medium — Synapse dedicated vs serverless SQL?** → Dedicated is provisioned MPP for sustained warehouse workloads; serverless is on-demand query over lake files with per-TB billing.
- **Hard/Scenario — A nightly pipeline takes 9 hours and must finish in 3.** → Parallelise activities/partitions, use mapping data flows sparingly (they spin up Spark), push down filters, optimise file layout (Parquet, partitioning), increase DIU/IR capacity, and monitor per-activity duration in ADF to find the bottleneck.

## 5.8 Database Selection Matrix ★★★

**Definition:** A selection framework mapping data shape, scale, consistency and operational model to the right Azure database service.

**Important Points**
- Choose based on **data model and access pattern** (relational joins vs partition-key access vs cache vs analytics), then operational model (PaaS vs IaaS), then cost.
- Azure SQL family covers most relational needs: single DB for app databases, elastic pools for many small tenants, Managed Instance for instance-level compatibility, SQL on VM for OS control.
- Cosmos DB is the choice for global distribution and multi-region writes — but only with a well-designed partition key.
- Flexible Server is the current managed home for MySQL/PostgreSQL; Single Server retirement is staged — verify before referencing old SKUs.
- Every database needs an explicit HA choice, backup/PITR retention, and a DR mechanism — these are separate decisions from the engine.

| Requirement | Choose | Notes |
| --- | --- | --- |
| Relational OLTP, SQL Server compatibility | Azure SQL DB | Managed, elastic, built-in HA |
| Near-full SQL Server instance features | SQL Managed Instance | VNet-native, instance-level features |
| Legacy needing OS control | SQL Server on VM | You manage HA/patching |
| MySQL/PostgreSQL | Flexible Server | VNet, zone-redundant HA |
| Global NoSQL, multi-region writes | Cosmos DB | Partition key + consistency are the design |
| Cache/session | Azure Cache for Redis / Managed Redis | TTL + eviction policy |
| Warehouse/BI | Synapse / Fabric | DWU/capacity |
| ETL/orchestration | Data Factory / Fabric | Pipelines |
| Files | Azure Files | SMB/NFS |
| High IOPS DB VM volumes | Premium SSD v2 / Ultra | VM limits apply |
| Ledger/immutable audit | SQL ledger tables / immutable blob | Verify feature support |

**Edge Cases & Gotchas**
- Choosing Cosmos DB without a partition-key design is the most expensive mistake in this list — repartitioning means migrating data.
- Running a database on a VM when a PaaS option fits multiplies patching, HA and backup work; running on PaaS when you need OS-level control blocks you later.
- HA and DR are separate: zone redundancy does not survive a Region loss, and geo-replication is asynchronous.
- Backup retention defaults are short and geo-redundant backup storage can be off — verify both before claiming an RPO.
- Connection limits and pooling are the most common production surprise when moving to PaaS.

**Interview Questions**
- **Basic — When Cosmos DB over Azure SQL?** → Global distribution, multi-region writes, flexible schema, and predictable access by partition key; not for complex relational joins.
- **Medium — When Azure SQL over Cosmos?** → Relational integrity, joins, transactions and SQL skills dominate; single-Region or failover-group DR is sufficient.
- **Hard/Scenario — Design storage for a global order system needing <10 ms writes in two Regions.** → Cosmos DB with multi-region writes, partition key `tenantId` (or a sharded key for large tenants), Session consistency unless the business needs stronger, conflict resolution policy, change feed to downstream systems, and PITR backups. Validate RU cost per operation with a load test.

---

# PART 6 — IDENTITY, SECURITY & GOVERNANCE

## 6.1 Microsoft Entra ID ★★★ · `TIER 1`

**Definition:** Microsoft's cloud identity provider (formerly Azure AD) for authentication, SSO, MFA, Conditional Access and application identity.

**Important Points**
- **Tenant** = identity boundary; users, groups, devices, applications, service principals, managed identities live here.
- **Protocols:** OIDC/OAuth 2.0, SAML 2.0, WS-Federation; SCIM provisioning; B2B (guest) and B2C/External ID (customer identities).
- **Licences:** Free, P1 (Conditional Access, dynamic groups, self-service password reset writeback, PIM basics), P2 (PIM, Identity Protection risk policies, access reviews).
- **Conditional Access:** if-then policies on user/group, app, device state, location (named locations), risk, client app; grant controls (MFA, compliant device, hybrid join) or block. **Report-only** mode for safe rollout.
- **MFA / passwordless:** Authenticator, FIDO2, Windows Hello, Temporary Access Pass; SSPR.
- **Identity Protection:** risky users/sign-ins, risk policies (requires P2).
- **Hybrid identity:** Entra Connect Sync / Cloud Sync, password hash sync, pass-through auth, federation; seamless SSO.
- **App model:** **app registration** (definition) vs **enterprise app/service principal** (instance in the tenant); permissions (delegated vs application), consent, admin consent, client secrets/certificates/**federated credentials**.
- **Managed identity:** system- vs user-assigned, no secrets, token via IMDS/local endpoint; works with resources that support Entra auth.
- **Workload identity federation:** GitHub Actions/OIDC → Entra app, removing secrets from CI.
- Use case: Entra ID + Conditional Access requiring compliant devices for admin apps, PIM for privileged roles, managed identities for all app-to-service auth.

**When to use / alternatives:** **Entra ID** for cloud identity, SSO, MFA, Conditional Access and app identity. **Entra Domain Services** when legacy apps need LDAP/Kerberos/NTLM without running domain controllers. **AD DS on VMs** only when you need full domain-controller control. **External ID** for customer (B2C-style) identities. Entra authenticates; **Azure RBAC** authorises resource actions — they are not interchangeable.
**Edge Cases & Gotchas**
- **Authentication ≠ authorization** — a valid token says nothing about Azure RBAC permissions.
- Conditional Access can lock out admins — always maintain **break-glass** accounts excluded from CA, with monitoring.
- Deleting an app registration deletes the service principal and breaks all integrations; secrets expire silently and cause 401s at the worst time.
- Client secrets in code/pipelines are a top finding — use federated credentials or managed identity.
- Token lifetime and cached tokens delay permission changes taking effect (up to ~1 h for some tokens); revoke sessions (`Revoke-AzureADUserAllRefreshToken` equivalent) when needed.
- Guest (B2B) users and cross-tenant access settings can block legitimate collaboration.
- Directory roles (e.g., Global Administrator) vs Azure RBAC roles (Owner) are separate planes — a Global Admin can elevate but doesn't automatically have data access.
- PIM activation does not bypass Conditional Access.
- Hybrid sync misconfiguration (duplicate UPN, filtering) creates hard-to-debug sign-in issues.

**Interview Questions**
- **Basic — What is Entra ID?** → Microsoft's cloud identity service for authentication, SSO, MFA, conditional access and application identity.
- **Medium — Entra ID vs Azure RBAC?** → Entra ID authenticates identities and manages directory objects; Azure RBAC authorizes actions on Azure resources at scopes.
- **Hard/Scenario — An App Service must read a Key Vault secret with no secrets in code.** → Enable a system- or user-assigned managed identity on the App Service, grant it `Key Vault Secrets User` (RBAC model) or an access policy for Get, ensure network access (private endpoint/firewall), and use `DefaultAzureCredential` in code with caching. Then verify with `az keyvault secret show --id`.

## 6.2 Azure RBAC ★★★

**Definition:** Azure's authorization system: role assignments bind a **security principal** to a **role definition** at a **scope**.

**Important Points**
- **Scope hierarchy:** management group → subscription → resource group → resource; permissions **inherit downward**.
- **Built-in roles:** Owner (full + manage access), Contributor (manage resources, cannot grant access), Reader, User Access Administrator, plus service-specific data roles (`Storage Blob Data Contributor`, `Key Vault Secrets User`, `Monitoring Reader`).
- **Custom roles:** `Actions`, `NotActions`, `DataActions`, `NotDataActions`, `AssignableScopes` — NotActions are **not** deny rules; they subtract from allowed actions.
- **Management plane vs data plane:** Contributor on a storage account does not grant blob data access — a separate data role is required. This is the most-asked RBAC question.
- **Deny assignments** exist (created by managed services like Blueprints/Deployment Stacks) and override allows; they are not user-editable.
- **ABAC conditions** on role assignments (e.g., allow only blobs with a specific tag/container) — verify support per service.
- **PIM** provides eligible (just-in-time), time-bound, approval-gated role activation with MFA and access reviews.
- **Best practice:** Entra groups for assignment, least privilege, PIM for privileged roles, regular access reviews, and no direct user assignments at subscription scope.
- Use case: platform team Owner at the management group; app team Contributor on their RG; app identity `Storage Blob Data Contributor` on one container.

**Edge Cases & Gotchas**
- **Propagation delay**: role assignments can take up to several minutes (sometimes longer) to apply — retry before debugging deeper.
- Contributor cannot read secrets/blobs — data-plane roles are separate and often missed.
- A custom role with `*/read` plus a specific write can still be broad — review the full action set.
- Classic administrator roles (`Co-Administrator`, `Service Administrator`) bypass RBAC — remove them.
- Deny assignments from Deployment Stacks/Blueprints can silently block an Owner.
- Assigning at subscription scope "for convenience" is a common least-privilege violation.
- Deleting a group removes its role assignments (good) but breaks the identities relying on them (bad if not planned).
- Guest users can hold RBAC assignments in your tenant — audit regularly.

**Interview Questions**
- **Basic — What is Azure RBAC?** → An authorization system that grants roles to principals at scopes, inherited down the hierarchy.
- **Medium — Owner vs Contributor?** → Both manage resources; only Owner (and User Access Administrator) can manage role assignments.
- **Hard/Scenario — A user has Contributor on the RG but cannot read Key Vault secrets.** → Contributor is a management-plane role; reading secrets requires a **data-plane** role (`Key Vault Secrets User`) or an access policy, plus network access if the vault is firewalled/private. Assign the data role at the vault scope.

## 6.3 Azure Key Vault ★★★

**Definition:** A managed service for secrets, keys and certificates, with HSM-backed key protection and integration with Entra ID and Azure services.

**Important Points**
- **Objects:** secrets (strings, max 25 KB), keys (RSA/EC, HSM-protected in Premium/Managed HSM), certificates (with lifecycle/issuance from DigiCert/GlobalSign or a private CA).
- **Authorization models:** **Azure RBAC** (recommended: `Key Vault Secrets User/Officer`, `Key Vault Crypto User`, `Key Vault Certificates Officer`) or legacy **access policies**.
- **Network:** public endpoint with firewall (VNet rules, IP rules, "Allow trusted Microsoft services"), **private endpoint**, `publicNetworkAccess: Disabled`.
- **Protection:** **soft delete** (default, 90-day retention) and **purge protection** (irreversible) to prevent malicious deletion.
- **Rotation:** key rotation policies, secret versioning, Event Grid notifications near expiry; certificate auto-renewal.
- **Managed HSM** for FIPS 140-2 Level 3 single-tenant HSM requirements.
- **Diagnostic logging** (`AuditEvent`) to Log Analytics is essential — Key Vault access auditing is a compliance requirement.
- **Caching:** apps should cache secrets and use `SecretClient` with refresh, not call Key Vault per request.
- Use case: DB credentials and API keys with rotation, TLS certs issued to App Gateway/Front Door, CMK for storage/SQL.

**When to use / alternatives:** **Key Vault** for secrets, certificates and software-protected keys with RBAC and auditing. **Managed HSM** when regulation requires single-tenant FIPS 140-2 Level 3 hardware. **App Configuration** for non-secret feature flags/settings (use Key Vault references for the secrets). Never keep secrets in pipeline variables, repo files or app settings in plaintext.
**Edge Cases & Gotchas**
- **Both planes must agree:** RBAC alone isn't enough if the network (firewall/private endpoint) blocks the caller.
- **Purge protection is irreversible** — once enabled it cannot be disabled; soft-deleted vaults with the same name block recreation for the retention period.
- Throttling: Key Vault has request-rate limits (per vault, varies by operation) — high-frequency secret reads cause 429s. Use caching and consider per-service vaults.
- Deleting a vault with purge protection on means you cannot reuse the name for 90 days.
- Key vault firewall "Allow trusted Microsoft services" is required for services like Azure Backup/Disk Encryption, but not sufficient for all scenarios.
- Private endpoint DNS must resolve the vault FQDN to the private IP, or the app falls back to the public endpoint (and fails).
- Access policy model and RBAC model should not be mixed carelessly — enabling RBAC on a vault ignores access policies.
- CMK key vault in a failed Region = dependent services fail; design key vault resilience.

**Production Troubleshooting**
```bash
# 1. Can the identity read the secret? (data-plane permission, not Contributor)
az keyvault secret show --vault-name <kv> --name <secret> --query "{enabled:attributes.enabled,expires:attributes.expires}"

# 2. What does the vault's audit log say? (403 vs network denial vs throttling)
az monitor log-analytics query -w <workspace-id> --analytics-query \
  "AzureDiagnostics | where ResourceProvider=='MICROSOFT.KEYVAULT' | where ResultType != 'Success' | project TimeGenerated, OperationName, CallerIPAddress, ResultSignature, identity_claim_oid_g"

# 3. Is the identity even assigned, and is the vault firewalled?
az role assignment list --scope <vault-id> --query "[].{p:principalName,r:roleDefinitionName}"
az keyvault show -n <kv> --query "{publicAccess:properties.publicNetworkAccess,default:properties.networkAcls.defaultAction}"
```
Interpretation: `ForbiddenByPolicy`/403 with the correct role = wrong vault scope or a **network** deny (public access disabled without a private endpoint/DNS). `SecretDisabled`/expired explains an outage that started at a specific time. Throttling (`429`) comes from per-request secret reads — cache in the app, don't call per request.

**Interview Questions**
- **Basic — What is Key Vault?** → A managed store for secrets, keys and certificates with access control, logging and HSM options.
- **Medium — RBAC vs access policies?** → Both authorize data-plane access; RBAC is the recommended model with central Azure role management, while access policies are vault-local and legacy.
- **Hard/Scenario — Production suddenly cannot fetch a secret.** → Check the identity's token (managed identity still assigned?), RBAC role/access policy, secret expiry/disabled state, deleted/soft-deleted vault, network path (private endpoint DNS, firewall), Key Vault audit logs for 403s, and throttling. Check the Activity Log for recent permission or network changes.

## 6.4 Azure Policy ★★★

**Definition:** A governance service that evaluates resources against rules and enforces effects such as Deny, Audit, Modify, or DeployIfNotExists.

**Important Points**
- **Structure:** policy definition (rule + effect + parameters) → **initiative** (a group of definitions) → assignment (scope + exemptions + parameters) → compliance evaluation.
- **Effects:** **Deny**, **Audit**, **Append**, **Modify**, **DeployIfNotExists (DINE)**, **AuditIfNotExists**, **DenyAction**, **Manual** (attestation), plus `Disabled`.
- **Scopes:** management group, subscription, resource group; inherited downward.
- **Exemptions** (waiver/mitigated) and **exclusions** allow managed exceptions with expiry — prefer exemptions for auditability.
- **Remediation tasks** for DINE/Modify require a **managed identity** with permissions on the target scope; existing non-compliant resources are not fixed automatically until a task is run.
- **Policy vs RBAC:** RBAC controls *who can do what*; Policy controls *what the result must look like*.
- **Common policies:** allowed locations, allowed resource types/SKUs, require tags, require private endpoints, enforce TLS version, deny public IPs, deploy diagnostic settings, deny management ports from the internet.
- **Regulatory compliance** built-in initiatives (CIS, PCI DSS, ISO 27001, NIST).
- Use case: deny resources outside India Regions at the `Landing Zones` management group; DINE diagnostic settings to a central Log Analytics workspace.

**Edge Cases & Gotchas**
- **DINE/Modify do not remediate existing resources automatically** — you must create a remediation task (and re-run after new assignments).
- Policy evaluation is periodic (plus on resource create/update); compliance can lag by minutes to hours.
- **Deny at scale can break a deployment pipeline** with no obvious cause — check the policy assignment on the resource.
- Exemptions without expiry become permanent holes; review them.
- Policy doesn't retroactively delete non-compliant resources — it blocks new ones (unless DenyAction/Delete effect is configured where supported).
- The managed identity used for remediation can be blocked by its own policy/network rules.
- Some resources/evaluations are preview-only and not enforced.
- Policy assignments to the tenant root/management group apply to sandbox subscriptions too — test with `Audit` first.

**Interview Questions**
- **Basic — What is Azure Policy?** → A governance service that enforces and audits resource configuration rules across scopes.
- **Medium — Policy vs RBAC?** → RBAC answers "can this identity perform this action?"; Policy answers "does the resulting resource comply with our rules?"
- **Hard/Scenario — You must ensure every new storage account has private endpoints and diagnostic logs.** → Assign an initiative with `Deny` for accounts lacking private endpoints (or Audit first), and `DeployIfNotExists` for diagnostic settings, with a remediation managed identity on the correct scope. Test on a pilot subscription, run remediation for existing resources, and track compliance percentage.

## 6.5 Azure PIM, Access Reviews & Identity Governance ★★

**Definition:** Privileged Identity Management provides just-in-time, time-bound, approval-gated role activation; Access Reviews periodically recertify access.

**Important Points**
- **Eligible vs active** assignments; activation requires MFA, justification, approval (optional), ticket (optional), and max duration.
- Applies to **Entra directory roles**, **Azure RBAC roles**, and **PIM for Groups**.
- **Access reviews** for groups, apps and roles; auto-remove on no response.
- **Entitlement management** (access packages) for B2B/partner access with lifecycle.
- **Break-glass accounts**: 2 cloud-only Global Admins, excluded from CA, monitored, credentials in a physical safe.
- Use case: platform engineers eligible for Owner on prod subscription for 2 hours with approval; quarterly access review of all subscription Owner assignments.

**Edge Cases & Gotchas**
- PIM activation doesn't guarantee access if a Deny assignment or Policy blocks it.
- Eligible assignments still need correct licensing (P1/P2).
- Approvals can stall on-call during incidents — define an emergency activation path.
- Access reviews that auto-remove can break automation running under human accounts.
- Break-glass accounts excluded from CA need very strong monitoring and no interactive use.

**Interview Questions**
- **Basic — What is PIM?** → Just-in-time privileged role activation with approval, MFA and time limits.
- **Medium — Why PIM over permanent assignments?** → Reduces standing privilege and blast radius, creates an audit trail, and supports access reviews.
- **Hard/Scenario — A team needs Owner on prod every day.** → If truly needed, PIM with scheduled activation for the team group, short duration, approval by the platform lead, and access reviews every quarter; otherwise move to a scoped custom role with only the needed actions.

## 6.6 Microsoft Defender for Cloud & Sentinel ★★

**Definition:** Defender for Cloud is CSPM (secure score, recommendations, regulatory compliance) plus workload protection plans; Sentinel is a cloud-native SIEM/SOAR built on Log Analytics.

**Important Points**
- **Defender for Cloud:** secure score, recommendations, **attack path analysis**, regulatory compliance dashboards, **Defender plans** for Servers (P1/P2), Storage, SQL, App Service, Containers (Defender for Containers), Key Vault, DNS, ARM, and DevOps security (verify current plan list).
- **Just-in-time VM access** and **adaptive application controls** come with Defender for Servers P2.
- **Security alerts** flow to the Defender portal / Sentinel; **continuous export** to Log Analytics/Event Hub.
- **Sentinel:** data connectors, **analytics rules** (scheduled, NRT, ML, anomaly), incident management, **automation rules/playbooks** (Logic Apps), hunting queries, workbooks, UEBA, threat intelligence.
- **Agentless scanning** for servers/containers (verify).
- Use case: Defender for Cloud at the management-group level with Log Analytics export into Sentinel, where a playbook isolates a VM on a high-severity alert.

**Edge Cases & Gotchas**
- Secure Score is a comparative metric, not a compliance statement — don't quote it as proof.
- Recommendations can be noisy or irrelevant (exclusions rec show gaps) — justify exclusions explicitly.
- Defender plans cost per resource/hour — enabling everything across 500 VMs has a real bill.
- Many recommendations need the Azure Monitor Agent/extension — missing agents cause "no data" findings.
- Sentinel ingestion costs dominate — filter/tier data and use Analytics vs Basic/Data lake tiers where appropriate (verify).
- Automation playbooks need permissions (managed identity/logic app connector) that can be blocked by CA.
- Alert fatigue without tuning creates the very incident you fear.

**Interview Questions**
- **Basic — Defender for Cloud vs Sentinel?** → Defender assesses posture and protects workloads (CSPM/CWPP); Sentinel aggregates and correlates security events across sources (SIEM/SOAR).
- **Medium — How do you prioritise Defender recommendations?** → By attack path exposure and business criticality, not raw score: internet-facing + data + identity risk first; then cost/effort.
- **Hard/Scenario — A high-severity alert fires at 2 a.m. for a VM beaconing to a suspicious IP.** → Isolate the VM (NSG/quarantine), snapshot disks for forensics, revoke the VM identity's tokens/permissions, review Defender/Sentinel alerts and DNS/flow logs for lateral movement, notify on-call security per playbook, then remediate and rebuild. The runbook and permissions must exist before the incident.

## 6.7 Azure Governance Baseline Checklist ★★

**Definition:** The non-negotiable controls every subscription should inherit before workloads deploy.

**Important Points**
- Management group hierarchy with Policy + RBAC inheritance.
- **Policy:** allowed Regions, required tags, deny public IPs/management ports from internet, enforce TLS 1.2+, require private endpoints where mandated, DINE diagnostic settings, deny resource types not approved.
- **RBAC:** Entra groups, PIM for privileged roles, no direct user assignments, data-plane roles scoped tightly.
- **Logging:** diagnostic settings to a central Log Analytics workspace, activity logs exported, Defender plans enabled per risk, Sentinel connected.
- **Network:** hub connectivity via VNet Manager/peering, forced egress through Azure Firewall, DDoS plan, NSGs at subnet level.
- **Data:** encryption (CMK where required), backup policy, soft delete/immutable storage, Key Vault with purge protection.
- **Cost:** budgets + alerts per subscription, tags for cost allocation, Advisor recommendations reviewed monthly.
- **Locks:** `CanNotDelete` on connectivity, key vaults, log analytics, and backup vaults.
- **Landing zone vending** automated with Bicep/Terraform and a subscription placement policy.

**Edge Cases & Gotchas**
- Locks on Log Analytics/Key Vault block automation that needs delete capability — scope locks to the right level.
- Policy + deployments: Deny policies break pipelines; communicate and test in Audit first.
- Central logging can become a cost sink — set table retention and sampling deliberately.
- Baseline drift after manual console changes — use Azure Policy compliance + IaC pipelines, not trust.

**Interview Questions**
- **Basic — Name five controls in a new subscription baseline.** → Policy (regions/tags), RBAC + PIM, diagnostic settings to central logs, Defender plans, backups + resource locks (plus network egress via firewall).
- **Medium — How do you prevent public IP creation?** → Policy `Deny` on `Microsoft.Network/publicIPAddresses` (with exemptions for approved edge resources), applied at the management group, plus Azure Firewall/NAT for egress.
- **Hard/Scenario — An audit finds three subscriptions with no logging for 6 months.** → Export/verify diagnostic settings via Policy DINE, backfill where possible (activity logs max 90 days), document the gap, add an alert on missing diagnostic settings, and enforce with Policy + deployment guardrails.

---

## 6.8 Azure Lighthouse (cross-tenant management) ★

**Definition:** Azure Lighthouse lets a service provider (or central IT tenant) manage resources in a customer's tenant through delegated resource management, without switching tenants or sharing credentials.

**Important Points**
- **Delegation** is defined by an ARM template that offers **authorizations** (principal IDs + built-in roles) for specific **scopes** (subscription or resource group) to the managing tenant.
- The managing tenant's engineers see and act on the delegated subscriptions from their own tenant, using their own identities — the customer keeps ownership and can revoke the delegation at any time.
- **RBAC applies at the delegated scope**: assign the minimum role, never Owner across everything.
- **Visibility** for the customer: delegated resources appear under "Service providers" and every action is recorded in **their** Activity Log — the audit trail stays with the data owner.
- Lighthouse is for **cross-tenant** management; within one tenant use management groups + PIM.
- Use case: an MSP manages 40 customer tenants from one operations tenant with a `Reader` + `Contributor` pair per scope; central IT manages subsidiary tenants without guest accounts.

**Edge Cases & Gotchas**
- Delegation is **not** guest access — do not mix the two models; guest accounts in the customer tenant are a different (and heavier) mechanism.
- Roles are assigned at delegation scope; a `Contributor` at subscription scope is a very large blast radius — scope to resource groups where possible.
- Some operations are not supported across tenants (certain resource types/services), and support-request workflows may differ.
- Lighthouse does not grant access to the customer's **Entra ID** directory data, only Azure resources at the delegated scope.
- Removing a delegation takes effect but leaves any resources the provider created — agree on cleanup before revocation.
- Monitoring/automation across tenants still needs the data to land centrally (Log Analytics, Azure Monitor) — delegation alone does not consolidate telemetry.

**Interview Questions**
- **Basic — What does Azure Lighthouse enable?** → Cross-tenant management of Azure resources through delegated resource management, using the managing tenant's own identities.
- **Medium — Lighthouse vs guest accounts?** → Lighthouse delegates scoped Azure RBAC without creating identities in the customer tenant and keeps the audit trail on the customer side; guests are real identities in the tenant with broader access implications.
- **Hard/Scenario — An MSP needs read-only access to 30 customer tenants but write access only to one resource group each.** → Publish a delegation template offering `Reader` at subscription scope and `Contributor` at the specific resource group scope, onboard each customer with their consent, and enforce least privilege plus activity-log monitoring on the customer side.

---

# PART 7 — INTEGRATION, MESSAGING & API

## 7.1 Azure API Management ★★

**Definition:** API Management (APIM) is a managed API gateway that publishes, secures, throttles and observes APIs across backends using policies.

**Important Points**
- **Components:** **service instance** (a deployment = gateway) → **APIs** → **operations** → **backends**; **products** and **subscriptions** (API keys) package APIs for consumers; **policies** are XML executed at inbound/backend/outbound/on-error.
- **Tiers:** Consumption (serverless, per-call), Developer (no SLA), Basic/Standard, **Premium** (multi-Region gateways, VNet, availability zones), and **v2 tiers (Basic v2/Standard v2/Premium v2)** — verify the current tier matrix and which features exist per tier.
- **Networking:** public gateway, **internal VNet mode** (private gateway), **external mode**, **private endpoint** for the gateway, and **backend access** via VNet/private endpoint or self-hosted gateway. The common hub-spoke pattern is internal-mode APIM in a spoke, reached through Application Gateway/Front Door.
- **Policies worth knowing:** `rate-limit` / `rate-limit-by-key`, `quota`, `validate-jwt` (Entra ID/other IdP), `authentication-certificate`, `set-backend-service`, `rewrite-uri`, `cache-lookup`/`cache-store`, `retry`, `mock-response`, `ip-filter`, `cors`, `send-request` (call another API to enrich), `choose`/`set-variable`.
- **Security:** subscription keys are identification, **not** authentication — pair with OAuth2/JWT validation (Entra ID), mTLS to backend, Named Values/Key Vault for secrets, `validate-content` for schema enforcement.
- **Observation:** Application Insights integration, `ApiManagementGatewayLogs`, request/response tracing, built-in analytics.
- **Self-hosted gateway** runs the APIM gateway in AKS/on-prem for hybrid/edge APIs (verify SKU requirements).
- Use case: expose internal microservices to partners with OAuth2 + per-partner rate limits; put a stable public contract in front of a backend that changes API versions frequently.

**Edge Cases & Gotchas**
- **Subscription keys are not security**: leaking a key in a mobile app is common and expected — enforce JWT validation and per-user rate limits (`rate-limit-by-key` with `context.Subscription.Id` or a JWT claim).
- Internal-mode APIM is invisible from the internet — teams forget to route inbound through App Gateway/Front Door and conclude "APIM is down".
- Premium tier costs are significant; v2 tiers narrow the feature gap but not for every capability — check before designing multi-Region.
- Policy errors fail closed at the gateway (500), and `<on-error>` handling is easy to forget — a bad `validate-jwt` config takes the whole API down.
- APIM is **regional**; global distribution needs Premium multi-Region gateways or Front Door in front.
- Rate limits are per gateway instance/shard in some configurations — verify that distributed limits behave as you expect at scale.
- Backend health is not automatically load-balanced unless you configure backend pools with health probes.

**Comparison — when to use which gateway**
- **APIM** — you need products/subscriptions, developer portal, policy transformation, quotas and an API catalogue for external or many internal consumers.
- **Application Gateway** — regional L7 load balancing + WAF for your own apps, no API product/consumer model.
- **Front Door** — global edge routing, caching and WAF in front of one or many API backends (and often in front of APIM).

**Interview Questions**
- **Basic — What is APIM?** → A managed API gateway for publishing, securing, throttling and observing APIs with policy-based transformation.
- **Medium — How do you protect an API in APIM?** → Enforce JWT validation against Entra ID, keep subscription keys for identification/quotas, apply per-key rate limits and quotas, validate schemas, keep secrets in Key Vault via Named Values, and restrict the backend network path.
- **Hard/Scenario — Partners report 429s at peak while your own apps are fine.** → Check whether limits are per-subscription (`rate-limit-by-key`) or global (`rate-limit`), the policy scope (product vs API vs operation), the backend's own limits, and whether the gateway is scaled for the region. Fix with per-partner quotas sized to contracts, backend capacity, and a documented 429 + retry-after contract.

## 7.2 Azure Service Bus ★★★

**Definition:** Service Bus is a managed enterprise message broker with queues and topics/subscriptions, supporting sessions, transactions, dead-lettering and scheduled delivery.

**Important Points**
- **Entities:** **queue** (point-to-point) and **topic → subscriptions** (pub/sub with filter rules and actions). **Sessions** give ordered, exclusive processing per session ID.
- **Tiers:** Basic, Standard, **Premium** (dedicated resources, VNet/private endpoint, larger messages, higher throughput) — verify per-tier limits.
- **Delivery semantics:** **at-least-once** by default; **peek-lock** (explicit complete/abandon/defer) vs **receive-and-delete**; **duplicate detection** with a window gives effectively-once within that window.
- **Failure handling:** `maxDeliveryCount` → **dead-letter queue** (DLQ) with `DeadLetterReason`; DLQ messages must be processed/monitored — an unread DLQ is silent data loss.
- **Features:** scheduled messages, deferred messages, transactions (send/complete across entities in a namespace), **auto-forwarding**, message sessions, `ServiceBusProcessor` for concurrent consumers.
- **Security:** Entra ID + Azure RBAC (`Azure Service Bus Data Receiver/Sender`) or SAS policies; **prefer managed identity over SAS**; private endpoint + firewall; disable local auth where possible.
- **Scaling/quotas:** namespaces have throughput/connection limits; Premium messaging units can be scaled; split workloads across namespaces.
- **Max message size** is tier-dependent (verify); large payloads belong in Blob Storage with a claim-check pattern.
- Use case: order processing where each order must be processed exactly once in order (sessions) with a DLQ for poison messages; fan-out of an event to billing and notification subscriptions.

**Edge Cases & Gotchas**
- **Duplicate processing** is normal with at-least-once delivery — consumers must be idempotent even when duplicate detection is enabled (the window is finite).
- A **lock expiring** while a slow consumer works causes the message to become visible again and be processed twice — renew the lock (`RenewMessageLock`) or shorten work.
- **DLQ growth** is the most common silent failure; alarm on `DeadletteredMessages` and `ActiveMessages` / `Size`.
- Sessions are bound to a session ID — a hot session serialises throughput and can bottleneck.
- Standard tier has no VNet integration; private endpoints require Premium.
- Topic subscription filters are evaluated per message and can quietly drop messages if the filter is wrong.
- Large batch prefetch + long processing multiplies lock-expiry risk.

**Comparison — which messaging service?**
- **Service Bus** — guaranteed delivery, ordering (sessions), transactions, DLQ, enterprise messaging between services. Choose it for business messages that must not be lost.
- **Storage Queue** — cheap, very large volumes, simple; no ordering, sessions, or transactions, and 64 KB messages.
- **Event Grid** — reactive notifications about state changes, filtered push delivery; not for guaranteed business message processing.
- **Event Hubs** — high-throughput telemetry/streaming with replay and consumer groups, not per-message acknowledgement.

**Production Troubleshooting**
```bash
# Is the backlog or the DLQ growing? (the two numbers that explain "messages are stuck")
az monitor metrics list --resource <namespace-id> --metric ActiveMessages DeadletteredMessages \
  --interval PT5M --aggregation Average Maximum --offset 2h

# Is a consumer failing, or never receiving? (compare incoming vs outgoing vs dead-lettered)
az servicebus queue show -g rg -n ns --name orders --query '{active:countDetails.activeMessageCount,dead:countDetails.deadLetterMessageCount,incoming:countDetails.incomingMessageCount}'

# Who can read it? (identity path, not SAS)
az role assignment list --scope <namespace-id> --query "[].{principal:principalName,role:roleDefinitionName}"
```
Interpretation: `activeMessageCount` growing with zero outgoing → consumers are down, throttled, or not listening (check the processor's error logs and the namespace connection limits). Growing `deadLetterMessageCount` with `DeadLetterReason: MaxDeliveryCountExceeded` → poison message or a persistent consumer exception; inspect a DLQ message body before redeploying. Permission errors surface as `401`/`UnauthorizedAccess` at connect time, not as message loss.

**Interview Questions**
- **Basic — Queue vs topic?** → A queue delivers each message to one competing consumer; a topic delivers a copy to each subscription (pub/sub fan-out), with filters per subscription.
- **Medium — How do you handle poison messages?** → Let `maxDeliveryCount` route them to the DLQ, monitor and alert on DLQ depth, inspect and repair/replay deliberately, and fix the consumer to be idempotent and bounded in execution time.
- **Hard/Scenario — Orders are occasionally processed twice.** → At-least-once delivery plus lock expiry or consumer crashes produce duplicates. Make processing idempotent (dedupe by message ID/order ID in the datastore), renew locks for long work, enable duplicate detection for the send side, and reduce prefetch/lock duration mismatch.

## 7.3 Azure Event Grid ★★

**Definition:** Event Grid is a managed event-routing service that delivers event notifications from sources to subscribers with content-based filtering.

**Important Points**
- **Sources/systems:** Azure services (Blob created, Resource events, Key Vault, Container Registry, IoT Hub), custom topics, domains, partner namespaces.
- **Concepts:** **topic** (publisher endpoint) → **subscription** (filter + endpoint + delivery properties) → **event handler** (Function, Logic App, Service Bus/Storage queue, webhook, Event Hubs, hybrid relay).
- **Filtering:** event types, subject prefix/suffix, and advanced attribute filters; **event domains** organise many topics under one endpoint for multi-tenant publishers.
- **Delivery:** retries with backoff and **24-hour retention** default; undelivered events go to a **dead-letter storage container** if configured. Delivery is **at-least-once** and **not ordered**.
- **Schemas:** Event Grid schema vs **CloudEvents v1.0** — choose CloudEvents for portability.
- **Security:** Microsoft Entra ID for publishing, **webhook validation handshake**, private endpoints, managed identity for delivery.
- Use case: resize a blob on upload (Blob Created → Function); open a ticket when a VM is deleted (Resource event → Logic App); route IoT telemetry events to different handlers.

**Edge Cases & Gotchas**
- **Events can be missed by design**: Event Grid is a notification system with retries and expiry, not a durable log. For business-critical flows, land events into a queue (Service Bus/Storage) first or use a change feed/CDC.
- Ordering is not guaranteed — handlers must be order-agnostic or reconcile from the source of truth.
- Webhook endpoints must complete the validation handshake or subscriptions stay unvalidated and receive nothing.
- Delivery failures are invisible unless you configure a **dead-letter destination** and alert on it.
- Duplicate deliveries happen — handlers must be idempotent.
- Event size limits (verify) mean large payloads should carry a reference to Blob Storage.

**Comparison — Event Grid vs Event Hubs vs Service Bus**
- **Event Grid** — "something happened", reactive fan-out, filtered, at-least-once with expiry (no replay of a stream).
- **Event Hubs** — high-volume telemetry stream, partitioned, replayable via offsets, consumer groups.
- **Service Bus** — durable business messages with acknowledgement, ordering and DLQ.

**Interview Questions**
- **Basic — What is Event Grid?** → A managed publish/subscribe router that delivers Azure and custom events to subscribers based on filters.
- **Medium — How do you avoid losing events?** → Configure a dead-letter destination and alerts, land critical events into a durable queue, make handlers idempotent, and monitor delivery failure metrics.
- **Hard/Scenario — A blob-triggered Function misses occasional files.** → Event Grid delivery is at-least-once but can expire after retries, and Functions can fail silently on concurrency limits. Add a dead-letter container, reconcile periodically by listing the container against processed items, raise Function concurrency or use a queue, and make the handler idempotent on blob ETag.

## 7.4 Azure Logic Apps ★★

**Definition:** Logic Apps is a managed workflow/orchestration platform (low-code designer + code view) for integrating SaaS and Azure services with triggers, actions, conditions and loops.

**Important Points**
- **Consumption** (multi-tenant, pay per action/run) vs **Standard** (single-tenant, runs in an App Service-like plan, VNet integration, local dev with VS Code) — Standard is generally the choice when you need VNet/private access.
- **Triggers:** HTTP request, recurrence (schedule), Service Bus/Event Grid/Blob/queue, SaaS connectors (Office 365, Salesforce, SAP, Dataverse).
- **Control flow:** conditions, switch, foreach/until, scope, parallel branches, terminate; **run-after** configuration controls failure paths.
- **Reliability:** retry policies per action, run history (with input/output payloads), resubmit from history, **integration account** for B2B/EDI (AS2, X12, EDIFACT maps).
- **Security:** managed identity for connections where supported, Key Vault for secrets, IP restrictions, private endpoints (Standard), and careful handling of run history (it stores payloads).
- Use case: approval workflow triggered by a Service Bus message with Teams/email notifications; scheduled nightly job that calls an API, transforms JSON and writes to Blob.

**Edge Cases & Gotchas**
- Run history **retains message payloads** — PII ends up in logs; restrict access and set retention.
- Consumption workflows can hit connector throttling limits; retries are per-action and easy to misconfigure.
- Long-running workflows with `until` loops can silently run for hours and cost more than expected.
- Managed identity support varies **per connector** — some still require secrets/OAuth connections.
- Standard vs Consumption differences (VNet, networking, hosting) surprise teams migrating.
- Logic Apps is orchestration, not a message broker — do not use a workflow as your queue.

**Comparison — Logic Apps vs Functions vs Durable Functions vs Data Factory**
- **Logic Apps** — connector-heavy integration/approval workflows with minimal code.
- **Functions** — code-first event handlers; **Durable Functions** for code-defined orchestration with state.
- **Data Factory** — data movement/transformation pipelines at scale.

**Interview Questions**
- **Basic — What is Logic Apps?** → A managed workflow service for integrating services and automating processes with triggers and actions.
- **Medium — Consumption vs Standard?** → Consumption is multi-tenant and per-execution; Standard is single-tenant with VNet integration, local development and better isolation.
- **Hard/Scenario — A production workflow intermittently fails on a SaaS connector.** → Inspect run history for the failing action and error code; connector throttling (429) needs retry policy and backoff; check connection authentication expiry; consider moving to a queue-based decoupling pattern so the workflow is retryable per message.

## 7.5 Messaging & integration selection sheet ★★

**Definition:** A decision guide mapping delivery semantics and integration style to the right Azure service, so messaging choices are made deliberately rather than by habit.

**Important Points**
- Ask four questions first: **must the message be durable? is ordering required? one consumer or many? code-first or connector-first?**
- Durability and acknowledgement point to **Service Bus** (or Storage Queue for cheap volume); reactive notification points to **Event Grid**; streaming/replay points to **Event Hubs**.
- Every asynchronous hop needs a **dead-letter path, an alarm on backlog, and an idempotent consumer**.

**Edge Cases & Gotchas**
- Using Event Grid where messages must not be lost — it retries and expires, it is not a durable log.
- Using Service Bus for high-volume telemetry — cost and throughput are wrong for that shape.
- A DLQ nobody monitors is silent data loss.

| Need | Service | Why |
| --- | --- | --- |
| Durable business messages, ordering, DLQ | **Service Bus** (sessions for order) | Acknowledgement, transactions, dead-lettering |
| Cheap high-volume simple queue | **Storage Queue** | Very low cost, simple polling |
| Reactive notification on a state change | **Event Grid** | Filtered push, broad Azure source coverage |
| Telemetry/streaming with replay | **Event Hubs** | Partitions, consumer groups, retention |
| Connector-heavy workflow / approvals | **Logic Apps** | Hundreds of connectors, low code |
| Code-first handler | **Functions** | Event-driven compute |
| Code-defined orchestration | **Durable Functions** | State, retries, fan-out/fan-in |
| API façade, quotas, products | **API Management** | Policy, subscriptions, portal |
| Bulk data movement | **Data Factory** | Pipelines, connectors, mapping flows |

> **Rule of thumb:** if losing the message is a business incident, it belongs on Service Bus (or a queue) — not on Event Grid alone.

**Interview Questions**
- **Basic — Which service would you choose for order messages that must not be lost?** → Service Bus (sessions if per-order ordering matters) with a DLQ and idempotent consumers.
- **Medium — Event Grid vs Event Hubs vs Service Bus in one line each?** → Event Grid: "something happened", filtered fan-out, retry-with-expiry. Event Hubs: high-volume partitioned stream with replay. Service Bus: durable business messages with acknowledgement, ordering and dead-lettering.
- **Hard/Scenario — A downstream consumer falls behind and messages expire.** → Move the consumer off a notification path onto a durable queue, scale consumers on backlog depth (KEDA/autoscale), add a DLQ and alerting, and make processing idempotent so retries are safe.

---

---

# PART 8 — MONITORING, BACKUP & OPERATIONS

## 8.1 Azure Monitor — Platform Overview ★★★

**Definition:** Azure Monitor is the unified observability platform for metrics, logs, traces, alerts and dashboards across Azure, hybrid and multicloud resources.

**Important Points**
- **Data types:**
  - **Metrics** — numeric time series, near-real-time, platform metrics retained 93 days (mostly), queryable via Metrics Explorer/API.
  - **Logs** — structured records in **Log Analytics workspaces**, queried with **KQL**, retention configurable (interactive 30–730 days, plus long-term/archive).
  - **Activity Log** — subscription-level control-plane events (who created/deleted/changed what), retained 90 days, export for longer.
  - **Traces** — distributed tracing via Application Insights / OpenTelemetry.
- **Components:** Log Analytics workspaces, Application Insights, **Data Collection Rules (DCR)** + **Azure Monitor Agent (AMA)**, diagnostic settings, Alerts, Action Groups, Workbooks, Dashboards, Managed Grafana, Managed Prometheus (for AKS).
- **Diagnostic settings** route resource logs/metrics to Log Analytics, Storage, Event Hubs, or a partner solution — **not enabled by default** for most resources.
- **Cross-resource queries** let one query span multiple workspaces/subscriptions (use `workspace()`).
- **Azure Monitor Private Link Scope (AMPLS)** for private ingestion/query.
- **Cost drivers:** log ingestion (per GB) + retention, plus alerts/notifications and any Prometheus/Grafana managed components.
- Use case: central Log Analytics workspace per Region, all resources sending diagnostics, Container Insights for AKS, App Insights for APIs, workbooks per service, alerts to Action Groups.

**When to use / alternatives:** **Azure Monitor** for platform metrics, logs, alerts and APM across Azure/hybrid. **Sentinel** when you need SIEM/SOAR correlation across security sources. **Managed Grafana/Prometheus** for Kubernetes-centric visualisation and PromQL. Third-party APM only when its specific capability justifies a second bill — otherwise duplicate agents and split dashboards cost more than they add.
**Edge Cases & Gotchas**
- **Guest OS metrics (memory, disk) require the Azure Monitor Agent + DCR** — they don't exist as platform metrics (same trap as CloudWatch).
- Platform metrics are pre-aggregated at 1-minute granularity; sub-minute needs custom metrics.
- **Activity Log ≠ resource logs** — Activity Log is control-plane; resource logs are data-plane/diagnostic.
- Diagnostic settings must be enabled per resource (or enforced with Policy DINE) — a new resource without them is invisible.
- Log ingestion is the largest observability cost for most teams — set table plans (Analytics/Basic/Auxiliary) and retention deliberately.
- Metric alerts evaluate at a cadence; very short spikes may be missed — use log alerts or shorter windows where supported.
- Workspace design: one central workspace simplifies queries but complicates RBAC/data residency; per-workload workspaces improve isolation but increase overhead.
- The legacy Log Analytics agent (MMA/OMS) is retired — use AMA; migration gaps are a common audit finding.

**Interview Questions**
- **Basic — What is Azure Monitor?** → The observability platform for metrics, logs, traces, alerts and dashboards across Azure and hybrid resources.
- **Medium — Metrics vs Logs?** → Metrics are numeric time series for fast, cheap alerting/dashboards; logs are structured records for detailed queries, correlation and retention.
- **Hard/Scenario — A new VM's memory alerts never fire.** → Memory is a guest metric: install the Azure Monitor Agent, attach a DCR collecting performance counters, confirm the workspace, and verify the alert rule queries the right table/workspace. Platform metrics alone cannot see inside the guest OS.

## 8.2 Log Analytics & KQL ★★★

**Definition:** Log Analytics is the log store/query engine in Azure Monitor; KQL (Kusto Query Language) is the query language used across Azure Monitor, Sentinel, and Data Explorer.

**Important Points**
- **Table basics:** `Heartbeat`, `Perf`, `Event`, `Syslog`, `AzureActivity`, `AzureDiagnostics` (legacy multi-category), resource-specific tables (`AppRequests`, `AppExceptions`, `AppDependencies`, `ContainerLogV2`, `AKSAudit`), `SecurityEvent`, `SigninLogs`, `AuditLogs`.
- **Query pipeline:** `Table | where | summarize by | order by | take | project | extend | join | render`.
- **`summarize`** with `bin(TimeGenerated, 5m)`, `count()`, `avg()`, `percentile()`, `dcount()`, `make_set()`.
- **`extend`** for derived values; `parse_json`/`todynamic` for JSON; `mv-expand` for arrays.
- **`join` kinds** (inner, leftouter) and `union` for combining tables/workspaces.
- **Saved queries, functions** (`let`), **workbooks** for reuse.
- **Retention & plans:** interactive retention, long-term archive, table plans (Analytics, Basic, Auxiliary) — verify current pricing/feature matrix.
- **Data ingestion paths:** AMA → DCR → workspace; diagnostic settings; Application Insights; custom logs API; Event Hub; Logs Ingestion API.
- Use case: "Top 10 failing endpoints in the last hour by error code" and "VM disk free trend by computer".

**Example — VM free disk trend**

```
Perf
| where ObjectName == "LogicalDisk" and CounterName == "% Free Space"
| where InstanceName in ("C:", "/")
| summarize FreePercent = avg(CounterValue) by bin(TimeGenerated, 15m), Computer
| render timechart
```

**Example — Activity Log: who deleted resources**

```
AzureActivity
| where OperationNameValue endswith "DELETE"
| where ActivityStatusValue == "Success"
| project TimeGenerated, Caller, ResourceGroup, OperationNameValue, ResourceId
| order by TimeGenerated desc
```

**Example — Failed requests by result code (Application Insights)**

```
AppRequests
| where TimeGenerated > ago(1h)
| where Success == false
| summarize FailedRequests = count() by ResultCode, Name
| order by FailedRequests desc
```

> Classic workspace tables (`requests`, `dependencies`, `exceptions`) still work in many workspaces; newer resource-centric tables are `AppRequests`, `AppDependencies`, `AppExceptions`. Confirm which schema your workspace uses before writing alerts.

**Edge Cases & Gotchas**
- Queries scan data by time range — always filter `TimeGenerated` first or you pay in time/cost.
- `AzureDiagnostics` is a legacy catch-all; resource-specific tables are preferred and cheaper to query.
- `dcount()` is approximate unless you request accuracy; cardinality affects cost.
- Log ingestion and query costs are separate; big ad-hoc queries over months are slow.
- Data arrives late (ingestion latency of seconds to minutes) — alerts on freshly deployed resources may show gaps.
- Table plan changes affect what query features are available (Basic tables don't support all KQL/alert types).
- Workspace RBAC: `Log Analytics Reader` vs `Contributor` vs table-level RBAC (verify).

**Interview Questions**
- **Basic — What is KQL?** → Kusto Query Language, the read-only query language for logs in Azure Monitor, Sentinel and Data Explorer.
- **Medium — How do you query across multiple workspaces?** → Use `workspace("id")` / `workspace("name")` references inside `union` (with cross-workspace query permissions) or a cross-workspace query resource.
- **Hard/Scenario — A workspace query for 30 days takes minutes and times out an alert.** → Alerts should query short windows with pre-aggregated/summarised data; reduce the range, filter early, project fewer columns, use resource-specific tables, and move long-term analytics out of alert rules into scheduled workbooks/reports.

## 8.3 Application Insights ★★★

**Definition:** Application Performance Monitoring (APM) for request rates, failures, dependency calls, exceptions, traces and live metrics, with distributed tracing.

**Important Points**
- **Instrumentation:** auto-instrumentation (agent/extension) for App Service, AKS, Functions, VMs; SDKs for .NET/Java/Node/Python; **OpenTelemetry** via the Azure Monitor exporter.
- **Data:** `requests`, `dependencies`, `exceptions`, `traces`, `customEvents`, `customMetrics`, `pageViews`; in workspace-based resources: `AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces`, etc.
- **Connection string** (newer) replaces instrumentation key.
- **Distributed tracing:** W3C trace context, operation IDs, dependency correlation; **Application Map** visualises service topology and failure rates.
- **Sampling:** adaptive sampling reduces volume/cost but can hide individual failures — tune per environment.
- **Availability tests:** URL ping (standard), multi-step, custom TrackAvailability.
- **Smart detection/auto-alerts**, **Live Metrics**, **Profiler** and **Snapshot Debugger** (verify per platform), **Transaction diagnostics**.
- **Workbooks** and **Failures/Performance** blades for triage.
- Use case: API latency regression traced to a slow SQL dependency in App Insights; 5xx alert on failed requests; availability test from 5 Regions.

**Edge Cases & Gotchas**
- **No instrumentation = no telemetry**; auto-instrumentation is per-platform and may need configuration/connection string at the app level.
- Sampling hides low-frequency errors — use exception sampling exclusions or adjust for critical paths.
- Client-side vs server-side telemetry mismatch causes confusing duplicate or missing requests (CORS/ingestion delays).
- High-cardinality custom properties inflate cost and slow queries.
- Application Insights is billed by data ingested + retention (+ multi-step availability tests) — watch custom metrics/log volumes.
- Async flows (queues) need manual correlation propagation.
- Exceptions are not automatically "handled" by App Insights — log them properly with context.
- Workspace-based resources query via `App*` tables; classic queries (`requests`) may return nothing in newer workspaces.

**Interview Questions**
- **Basic — What is Application Insights?** → An APM service for request/dependency/exception telemetry and distributed tracing of applications.
- **Medium — How do you find the cause of a latency spike?** → Check request duration percentiles, then dependency durations (SQL/HTTP), failures/exceptions, server metrics, and recent deployments; use the transaction/end-to-end view and Application Map to localise the slow hop.
- **Hard/Scenario — Users see intermittent 500s but CPU/memory are normal.** → Query `AppExceptions`/`AppRequests` for failed operations and stack traces, check dependency failures (timeouts/throttling), database error codes, deployment/correlation with an operation ID, and sample a full transaction. Normal infrastructure metrics never reveal application-level faults.

## 8.4 Alerts, Action Groups & Alert Processing Rules ★★★

**Definition:** Azure Monitor alerts evaluate metric/log/activity-log signals and trigger action groups; alert processing rules modify notifications (suppression, routing).

**Important Points**
- **Alert types:** metric alerts (static or dynamic/anomaly thresholds, multi-resource), log search alerts (KQL with aggregation and evaluation frequency), activity log alerts (service health, resource changes), smart detection (App Insights), Prometheus alerts (AKS).
- **Action groups:** email/SMS/push/voice, webhook, Logic Apps, Functions, Automation runbooks, Event Hubs, ITSM; each has a per-action rate limit.
- **Alert processing rules:** suppress (maintenance windows) or apply action groups to a scope.
- **Common alert schema** for webhooks — design for it early.
- **Severity mapping** (Sev0 critical → Sev4 verbose) and ownership/triage routing.
- **Alert state** (New/Acknowledged/Closed) and auto-resolve for metric alerts.
- **Suppression during deployments** via alert processing rules prevents noise storms.
- Use case: Sev2 log alert on 5xx rate > 2% for 5 min → Action Group → Teams + PagerDuty + runbook link.

**Edge Cases & Gotchas**
- **Log alerts have a minimum evaluation frequency and window** (often 1 min/5 min) and a cost per rule — many rules get expensive.
- Metric alert dimensions/aggregation mistakes (avg vs max) create false negatives.
- Splitting alerts by high-cardinality dimensions can exceed rule limits and cost.
- Action group rate limits (e.g., SMS/voice per hour) silently drop notifications during storms.
- Notification endpoints (webhooks) may block Microsoft IPs or require validation handshakes.
- An alert without a runbook and owner is noise; alert quality beats alert quantity.
- Activity log alerts on "Service Health" are easy to miss unless explicitly created per subscription.
- Nobody tests alerts until an outage — schedule alert tests/game days.

**Interview Questions**
- **Basic — What is an action group?** → A reusable set of notification and automation actions triggered by an alert.
- **Medium — Metric alert vs log search alert?** → Metric alerts are fast and cheap on time-series; log alerts run KQL and can express complex conditions but are slower and costlier.
- **Hard/Scenario — During every deployment the on-call is paged 50 times.** → Add alert processing rules that suppress non-critical alerts during change windows, gate alerts on sustained conditions (e.g., 5 min), make deploy markers visible on dashboards, and split deployment-induced blips from real incidents with severity/routing logic.

## 8.5 Data Collection Rules, AMA & Diagnostic Settings ★★

**Definition:** Azure Monitor Agent plus Data Collection Rules define what guest telemetry is collected from which machines and where it is sent; diagnostic settings route platform logs/metrics.

**Important Points**
- **AMA** replaces legacy MMA/OMS and Azure Diagnostics extension; installed as a VM extension or via Policy/Arc.
- **DCRs** define data sources (performance counters, Windows event logs, Syslog, custom text/JSON logs, IIS logs), destinations (Log Analytics workspace), and associations (which VMs).
- **Data Collection Endpoints (DCE)** for private ingestion scenarios (AMPLS).
- **Diagnostic settings** per resource: categories (e.g., `AuditEvent` for Key Vault, `StorageRead/Write/Delete` for blobs, `AppServiceHTTPLogs`) → Log Analytics, Storage, Event Hub, partner.
- **Enforce with Policy DINE** so every new resource ships its logs centrally.
- Use case: one DCR collecting security events and performance counters from all servers, sent to a central workspace; Policy auto-deploys diagnostic settings for Key Vault and NSGs.

**Edge Cases & Gotchas**
- DCR association at scale requires Policy/Arc — manual association doesn't scale and drifts.
- Some data sources are collected by the agent only in certain OS versions; verify.
- Diagnostic settings have per-resource category limits and costs; enabling "all logs" on high-traffic resources is expensive.
- Deleting a DCR breaks collection silently.
- Private ingestion requires AMPLS + DNS + DCEs on both agent and resource paths.
- Multiple DCRs can apply to a VM — precedence rules matter.

**Interview Questions**
- **Basic — What is a DCR?** → A rule defining what telemetry the Azure Monitor Agent collects and where it sends it.
- **Medium — How do you ensure all VMs send logs centrally?** → Policy that deploys AMA + associates a DCR to every VM (including Arc), plus troubleshooting via the agent health workbook.
- **Hard/Scenario — Half the fleet stopped sending logs after a migration.** → Check AMA extension health and DCR association, workspace permissions (agent needs the monitoring metrics publisher identity/role), private-link/DNS changes, and whether legacy MMA-based policies were removed. Re-associate via Policy and validate with `Heartbeat`.

## 8.6 Azure Backup & Recovery Services Vault ★★★

**Definition:** Azure Backup is the managed backup service; a Recovery Services Vault (or Backup Vault) stores policies, recovery points and protected items.

**Important Points**
- **Vaults:** **Recovery Services Vault** (VMs, SQL in VM, SAP HANA, Azure Files, on-prem via MARS/DPM) and **Backup Vault** (newer: blobs, AKS, PostgreSQL Flexible Server, disks, etc. — verify per workload).
- **Redundancy per vault:** LRS, ZRS (in supported Regions), GRS — **set at vault creation** for RSV (cannot change easily).
- **Policies:** schedule (daily/weekly) + retention (daily/weekly/monthly/yearly); enhanced policies for VMs support multiple backups/day and longer retention.
- **Features:** instant restore (snapshot tier), **soft delete** (14 days default, extendable), **immutable vault** (cannot delete/disable), **Multi-User Authorization (MUA)** for destructive operations, **Cross-Region Restore** (requires GRS), **Backup Center** for fleet management, **vault-level RBAC + resource guard**.
- **Workloads:** Azure VMs (application-consistent via VSS on Windows / pre-post scripts on Linux), SQL Server in VM (log backups, PITR), SAP HANA, Azure Files (share snapshots), blobs (operational/vaulted backup), AKS (Backup extension), PostgreSQL Flexible Server.
- **Security:** encryption, vault RBAC, private endpoints, resource guard, MUA, soft delete + immutable.
- Use case: daily VM backup with 30-day daily/12-month monthly retention, GRS vault, soft delete + immutable + MUA, quarterly restore drills.

**When to use / alternatives:** **Azure Backup** for recoverable point-in-time copies (RPO = backup frequency). **ASR** for low-RTO workload failover. **Storage redundancy (GRS/RA-GRS)** for infrastructure-level durability, not for accidental deletion. **Snapshots** for fast, short-term rollback (and as a backup building block). **Immutable storage** for regulatory WORM. Backup and DR are different problems — most production designs need both.
**Edge Cases & Gotchas**
- **Backup ≠ DR** — backups give you data recovery; RTO is restore time (hours for large VMs). ASR gives workload failover.
- GRS vault replicates to the paired Region (which may be outside your country) — residency conflict.
- Soft delete can be disabled only within limits and by privileged users — protect it with immutable vault + MUA.
- Changing vault redundancy after creation isn't supported for RSV (verify current options).
- Backup of a VM does not capture data on **temporary disks** or data written by apps that are not VSS-aware.
- Large VMs take hours to restore — test RTO, use instant restore, consider ASR for critical workloads.
- Restore of a VM creates a new VM (with disks/NIC) — networking and identity need to be reattached.
- Backup jobs can fail on disk-encryption-set permission changes, agent issues, or network restrictions (private endpoints).
- Deleting a vault requires deleting all protected items; immutable vaults block deletion.

**Interview Questions**
- **Basic — What is a Recovery Services Vault?** → An Azure resource that stores backup policies, recovery points and protected items.
- **Medium — Azure Backup vs Azure Site Recovery?** → Backup makes recoverable copies (RPO = backup frequency, RTO = restore time); ASR continuously replicates VMs for orchestrated failover with much lower RTO/RPO.
- **Hard/Scenario — A production VM is deleted. Walk through recovery.** → Check the vault for recovery points and soft-delete status; restore the VM (or its disks) from the latest/desired recovery point; reattach NSG/public IP/private DNS/identity as needed; validate the app and data. Then add resource locks, Azure Policy, and ASR for critical workloads to reduce future RTO.

## 8.7 Azure Site Recovery (ASR) ★★★

**Definition:** A disaster recovery service that continuously replicates supported workloads to a secondary location and orchestrates failover/failback with recovery plans.

**Important Points**
- **Supported:** Azure VMs (Region-to-Region), VMware/Hyper-V (to Azure or secondary site), physical servers, Azure Arc-enabled servers (verify).
- **Replication:** agentless (Azure-to-Azure) using a cache storage account and replication policy; **crash-consistent** recovery points typically every 5 minutes, **app-consistent** at configured frequency.
- **Recovery plan:** ordered groups of machines, pre/post scripts (Automation runbooks), manual actions, and a test-failover mode.
- **Failover types:** test failover (isolated VNet, no impact), planned failover (zero data loss when source is available), unplanned failover (possible data loss within RPO).
- **Failback:** re-protect and fail back to the original/primary Region after it recovers.
- **Networking:** target VNet/subnet/IP mapping, NSGs, public IPs, load balancers, DNS changes — recovery plans must handle them.
- **RPO/RTO:** defined by replication policy (RPO typically ~5 min or better for crash consistency) and by how quickly the recovery plan runs (RTO).
- **Cost:** ASR licence per protected instance + cache storage/egress + target infrastructure (which may be minimal if not pre-provisioned).
- Use case: 40 critical VMs replicated to a secondary Region, quarterly test failover into an isolated VNet, documented RTO of 45 minutes.

**Edge Cases & Gotchas**
- **Test failover must be into a VNet with non-overlapping addressing and isolated NSGs**, or you create an accidental production outage/duplicate identities.
- ASR does not replicate data to **on-prem or across geographies** beyond configured targets; it is Region-to-Region for Azure VMs.
- **IP address changes on failover** break app configs and DNS — plan static IPs/DNS updates in the recovery plan.
- Some workloads (domain controllers, SQL clusters, shared disks) need special handling and sequenced recovery plans.
- **Failback is not automatic** and can fail if the original Region's resources changed.
- Replication lag > RPO during high churn; monitor `Replicated items` health and alerts.
- A single cache storage account per workload affects throughput; monitor its health.
- ASR is not a backup — it doesn't protect against logical corruption propagating to replicas (keep backups too).

**Interview Questions**
- **Basic — What is ASR?** → A DR service that replicates workloads to a secondary site/Region and orchestrates failover with recovery plans.
- **Medium — ASR vs Backup?** → ASR gives low RTO/RPO continuous replication and orchestrated failover; Backup gives point-in-time copies for data recovery. Use both.
- **Hard/Scenario — RTO is 30 minutes for a three-tier app.** → ASR with a recovery plan that sequences DB → app → web tiers, pre-provisioned target network/identity, pre-staged runbooks for DNS/traffic switch (Front Door/Traffic Manager), tested monthly with test failover, plus documented manual steps for external dependencies. Measure actual RTO each drill.

## 8.8 Azure Cost Management, Advisor & Service Health ★★

**Definition:** Cost Management provides cost analysis/budgets/exports; Advisor gives recommendations; Service Health reports Azure incidents and planned maintenance.

**Important Points**
- **Cost Management:** cost analysis by resource/group/tag/subscription, **budgets** with alerts (actual/forecast), **exports** to Storage, **cost allocation rules**, **reservations/savings plan** recommendations, **Anomaly alerts** (verify availability).
- **Tags** for allocation; **cost allocation** for shared resources (e.g., hub firewall, Log Analytics).
- **Advisor:** reliability, security, performance, cost, operational excellence recommendations; **service retirement/upgrade** notices.
- **Service Health:** active incidents, planned maintenance, health advisories, **Service Health alerts** (create them per subscription), Resource Health for individual resource status.
- **Azure savings plan for compute** (hourly commitment, 1/3-year) vs **reservations** (specific SKU/Region) vs **Hybrid Benefit** (Windows/SQL licences).
- **Common cost levers:** right-size VMs, deallocate idle VMs, autoscale, reservations/savings plans, storage tiering/lifecycle, delete unused disks/IPs/snapshots, log retention tuning, reduce cross-region egress, AHB, dev/test pricing.
- Use case: budget per subscription with 80%/100% alerts to the owner; monthly Advisor review; Service Health alerts to the platform team.

**Edge Cases & Gotchas**
- Budgets are **not hard caps** — they alert but do not stop spending (unless you build automation on the alert).
- Cost data lags (hours to a day) — a runaway resource can spend a lot before an alert fires.
- Reservations bought for a shrinking footprint are sunk cost; monitor utilisation.
- `Stopped (not deallocated)` VMs still bill compute; disks and static public IPs always bill.
- Advisor cost recommendations can conflict with reliability/performance — review context.
- Service Health alerts must be created per subscription and per event type; they aren't automatic.
- Deleting an unused disk requires checking attachments — an "unattached" disk may be a backup target.
- Cross-region egress and NAT Gateway data processing are the usual hidden items.

**Interview Questions**
- **Basic — What is a budget in Cost Management?** → A spending threshold with alert notifications (actual/forecast) at set percentages.
- **Medium — How do you reduce Azure spend without hurting reliability?** → Right-size and autoscale, use reservations/savings plans/AHB for steady workloads, delete orphaned resources, tier storage, tune log retention, remove cross-region chatter, and shut down non-prod on schedules — then verify SLOs after each change.
- **Hard/Scenario — Monthly spend jumped 35% with stable traffic.** → Cost analysis by service/resource/Region, check for new deployments, disk/snapshot growth, log ingestion, NAT/egress, idle but allocated VMs, backup storage, and reservations expiring. Add anomaly alerts and a tag-based review process.

---

## 8.9 Azure Update Manager ★★★

**Definition:** Update Manager is the Azure-native service for assessing and installing OS and software updates on Azure VMs, Arc-enabled servers and (where configured) on-premises machines, with schedules, windows and compliance reporting.

**Important Points**
- **Scope:** Azure VMs (Windows/Linux), **Arc-enabled** servers, and — where supported — machines managed through Automation accounts (verify the current migration path from Automation Update Management, which is being retired).
- **Core objects:** **maintenance configuration** (schedule + window + reboot option + classifications/patches to include-exclude) → **assessment** (what is missing) → **deployment** (install run).
- **Periodic assessment** runs on a configurable cadence (or on demand); **one-time update** for ad-hoc patching.
- **Reboot options:** Always / IfRequired / Never. "Never" plus pending reboots is how patches silently fail to take effect.
- **Dynamic scoping** by subscription/resource group/tag means new VMs are automatically in scope — otherwise you patch the fleet minus the newest machines.
- **Compliance views:** per-machine update state and a fleet compliance dashboard (Reporting); exportable to Log Analytics for alerting.
- **Prerequisites:** the **Azure Connected Machine agent** (Arc) for non-Azure machines, extension-based patching agent, outbound connectivity (or private endpoints), and the appropriate RBAC (`Virtual Machine Contributor` + `Azure Connected Machine Resource Administrator` where applicable).
- **Integration:** Maintenance configurations can be shared across subscriptions; **pre/post events** (where supported) allow hooks such as draining from a load balancer before patching.
- Use case: monthly patch window per environment (prod Sunday 02:00, 3-hour window, reboot IfRequired), staged rings (canary → 10% → rest), compliance dashboard reviewed weekly, exceptions documented per machine.

**Edge Cases & Gotchas**
- **Patching ≠ compliance**: a machine can be "patched" and still require a reboot; track pending-reboot state, not just install status.
- VMs that are **deallocated** or offline during the window are skipped — the schedule does not queue them forever; they show as non-compliant until the next run.
- A window shorter than the patch install time leaves a partially patched machine; measure actual install durations before setting windows.
- Rebooting a single-instance workload during the window is a self-inflicted outage — coordinate with load balancers/ASGs or use pre/post hooks and health checks.
- **Exclusions** are easy to forget: an excluded patch can sit unapplied for months and appear only in an audit.
- Arc machines need connectivity and the correct agent version; an unhealthy agent reports stale compliance data, which is worse than no data.
- Linux patch classification depends on the distro's repositories (and whether third-party repos are in scope); "no updates" can simply mean the repo is unreachable.
- Update Manager is not a configuration-management tool — it patches, it does not enforce desired state (that is DSC/Arc extensions/Ansible).

**Comparison**
- **Update Manager** — Azure-native scheduling, assessment and compliance for Azure/Arc machines.
- **Image pipeline** — rebuild and replace (immutable infrastructure) for cattle-style fleets; often preferred over in-place patching.
- **Automation Update Management** — legacy; migrate to Update Manager.
- **Defender for Cloud** — surfaces missing patches as recommendations but does not schedule installs.

**Production Troubleshooting**
```bash
# What is missing on this machine, and when was it last assessed?
az maintenance applyupdate list --provider-name Microsoft.Maintenance --resource-type virtualMachines \
  --resource-name <vm> --resource-group <rg> -o table
az maintenance assessment list --resource-group <rg> -o table

# Which machines are non-compliant across the subscription?
az graph query -q "patchassessmentresources | where type =~ 'microsoft.compute/virtualmachines/patchassessmentresults' | summarize count() by properties.status" -o table

# Did the last deployment actually run (vs silently skipped)?
az maintenance applyupdate show --provider-name Microsoft.Maintenance --resource-type virtualMachines \
  --resource-name <vm> --resource-group <rg> --apply-update-name <name> -o json
```
Interpretation: `assessment` with `status: Failed` usually means the agent is unhealthy or the machine was offline. `applyupdate` with `status: Completed` but a machine still showing updates missing → reboot pending or repository/classification exclusions. No rows at all for a machine → it is not in scope of a maintenance configuration (classic dynamic-scoping miss).

**Interview Questions**
- **Basic — What does Update Manager do?** → Assesses and installs OS updates on Azure and Arc machines on a schedule, with reboot control and compliance reporting.
- **Medium — How do you roll out patching safely across a fleet?** → Maintenance configurations per ring: canary machines first, then a small percentage, then the rest; measure install time to size the window; reboot `IfRequired`; health checks/pre-post hooks; compliance dashboard reviewed after each window.
- **Hard/Scenario — A weekly patch run reports success, but audits show missing patches.** → Check for pending reboots, exclusion lists, dynamic-scoping gaps (machines not in any configuration), offline/deallocated VMs at window time, and Linux repository reachability. Then verify against the machine's own inventory (`Get-HotFix`/`dnf check-update`) rather than the portal.

## 8.10 Azure Resource Graph ★★★

**Definition:** Resource Graph is a read-only query service (Kusto/KQL syntax) over Azure Resource Manager data, letting you query resources, policy state and patch state across many subscriptions at once.

**Important Points**
- **Scope:** a single query can span subscriptions, management groups or the whole tenant — the key differentiator from per-resource CLI calls.
- **Tables:** `Resources` (inventory), `ResourceContainers` (subscriptions/resource groups), `PolicyResources`, `PatchAssessmentResources`, `AuthorizationResources` (RBAC assignments), `SecurityResources` (Defender/Alerts), `HealthResources`, `AdvisorResources`, `MaintenanceResources`.
- **Syntax:** `Resources | where type =~ 'microsoft.compute/virtualmachines' | project name, resourceGroup, location, tags | summarize count() by location`.
- **Use cases:** inventory and ownership audits, tag compliance, finding public IPs or public storage, untagged/unattached resources, RBAC assignment reviews, policy compliance dashboards, cost-allocation prep, **workbook and dashboard backends**.
- **Access:** requires `Reader` on the scopes queried; results respect RBAC — you cannot see what you cannot read.
- **Limits:** throttled (per-user/per-tenant request limits), paged results (1000 rows per page), and **5-minute cached freshness** (verify) — not a real-time transaction log.
- **Availability:** `az graph query`, PowerShell `Search-AzGraph`, REST, and it is the engine behind many portals blades.
- Use case: "list every storage account with publicNetworkAccess enabled across 60 subscriptions", "find all VMs without an Owner tag", "who has Owner at subscription scope".

**Edge Cases & Gotchas**
- **Freshness/staleness**: recently created or changed resources can take minutes to appear — do not use Resource Graph as a deployment verification tool.
- Not all services/properties are exposed (some nested/sensitive properties are absent); fall back to the service API for those.
- Large queries hit throttling and paging — use `summarize`, `project` fewer columns, and paginate with `skip`/`take` or `mv-expand` carefully.
- Case sensitivity: resource `type` comparisons should use `=~`, and property paths vary by API version.
- RBAC applies, so a query run as a personal user and as a pipeline identity can return different results — understand the identity before trusting a count.
- It is read-only: use it to find, then act with CLI/Terraform/Policy — never script mutations from query output without an approval step.

**Comparison**
- **Resource Graph** — fast, cross-subscription, read-only inventory and audit queries.
- **Log Analytics** — operational/telemetry data over time (logs, metrics, activity), not current resource configuration.
- **Activity Log** — what changed and who did it (per scope, 90 days).
- **Azure Policy compliance** — evaluated configuration state with remediation.

**Interview Questions**
- **Basic — What is Resource Graph?** → A read-only KQL query service over ARM data across subscriptions, used for inventory, audit and compliance reporting.
- **Medium — Resource Graph vs Log Analytics vs Activity Log?** → Graph is current resource configuration across scopes; Log Analytics is telemetry/logs over time; Activity Log is the control-plane change history.
- **Hard/Scenario — You must prove no public storage accounts exist in 60 subscriptions.** → Query `Resources` for `microsoft.storage/storageaccounts` with `properties.publicNetworkAccess`/`allowBlobPublicAccess` set permissively, export to a scheduled report or Workbook, cross-check with Policy compliance state, and add a `Deny` policy plus an alert so the answer stays true next month.

## 8.11 Azure Automation, Runbooks & State Configuration ★★

**Definition:** Azure Automation hosts runbooks, schedules and (legacy) DSC configuration for operational tasks and remediation across Azure and hybrid machines.

**Important Points**
- **Runbook types:** **PowerShell** and **PowerShell Workflow** (long-running/checkpointing, legacy) and **Python**; PowerShell 7 runbooks supported (verify current support matrix); graphical runbooks exist but are not recommended.
- **Execution:** **Azure sandbox** (hosted, no persistent state) vs **Hybrid Runbook Worker** (a machine/Arc server/AKS in your network for on-prem or private-endpoint access).
- **Assets:** variables, credentials, **certificates**, **connections**, and **modules** (pin module versions; gallery drift breaks runbooks).
- **Scheduling and triggers:** schedules, webhooks (with expiry), and — the modern pattern — **EventBridge-for-Azure style automation**: Event Grid/Alert → Logic App or Automation webhook → runbook.
- **Managed identity** for the Automation account (system or user assigned) is strongly preferred over Run As accounts, which are retired/being retired — **verify** the current state and migrate.
- **State Configuration (DSC)** is a legacy feature with a migration path to machine configuration/Azure Policy guest configuration — know it exists, do not design new work on it.
- **Common remediation patterns:** start/stop VMs on a schedule, delete unattached disks, enforce tags, rotate secrets, restart a service, snapshot a disk before a risky change.
- Use case: Event Grid alert on a non-compliant public IP → runbook removes it and posts to Teams; nightly runbook deallocates dev VMs.

**Edge Cases & Gotchas**
- **Run As accounts and classic assets are being retired** — build on managed identities; check the current retirement dates before copying an old design.
- Azure sandbox has **timeouts and no persistent state** — long jobs need checkpoints, Hybrid Workers, or Durable Functions/Logic Apps instead.
- Runbooks fail silently if module versions drift — pin modules and test after gallery updates.
- Webhook URLs are **bearer secrets** — anyone with the URL can trigger the runbook; treat like a password, rotate, and prefer managed identity/Event Grid with auth.
- A runbook that mutates resources at scale needs the same review as code: what-if/verbose logging, dry-run mode, and change control.
- Hybrid Runbook Worker connectivity depends on the Log Analytics/agent path — agent issues look like "the runbook didn't run".
- Jobs can overlap on a schedule; add a mutex/state check unless re-entrancy is safe.

**Comparison**
- **Automation runbooks** — operational glue, inventory-wide tasks, scheduled/idempotent jobs.
- **Azure Functions** — event-driven code with better scaling, bindings and DevOps integration; usually the better choice for new remediation code.
- **Logic Apps** — connector-heavy orchestration and approvals.
- **Bicep/Terraform** — declarative provisioning, not runtime remediation.

**Interview Questions**
- **Basic — What is Azure Automation used for?** → Running scheduled or triggered operational runbooks, storing shared assets, and automating remediation across Azure and hybrid machines.
- **Medium — Azure Automation vs Azure Functions for remediation?** → Automation is convenient for PowerShell glue and existing assets; Functions gives better scaling, dependency management, bindings and CI/CD — prefer Functions for new code unless you need the Automation sandbox/Hybrid Worker model.
- **Hard/Scenario — A runbook that deletes unattached disks runs nightly and one night deletes the wrong disk.** → The runbook trusted "unattached" as a proxy for "unused". Add explicit exclusions/tag opt-ins, dry-run and reporting mode first, a snapshot or soft-delete path, approval for destructive actions, and alerting on resources deleted per run. Then post-incident, restore from snapshot and fix the selection logic.

## 8.12 Azure CLI & PowerShell — the working toolkit ★★★

**Definition:** The two primary administration surfaces: cross-platform **Azure CLI** (`az`) for scripting and automation, and **Az PowerShell** for Windows-centric and object-pipeline automation (plus AzureRM→Az migration history you should recognise).

**Important Points**
- **Authentication:** interactive `az login`, **service principal** with secret/certificate, and **workload identity federation (OIDC)** for CI — prefer OIDC; `az login --identity` for managed identity on a VM/runner.
- **Context management:** `az account show` / `az account set -s <sub>`; in PowerShell `Get-AzContext` / `Set-AzContext`. Most "wrong results" incidents are the **wrong subscription context**.
- **Output formats that matter:** `--output table` (read), `--output json` (parse), `--query` (JMESPath) to shape results; in PowerShell use `Select-Object`/`Where-Object` over objects.
- **Idempotence and scripting:** `--yes`, `--no-wait`, `--only-show-errors`, `--what-if` (deployments) and `--dryrun` (some commands) — know which commands are safe to re-run.
- **PowerShell specifics:** `Az` module (install/version pinning), `Connect-AzAccount`, resource cmdlets (`New-AzVM`, `Get-AzResource`), and **Az.ResourceGraph** for cross-scope queries.
- **Idempotent vs imperative:** CLI/PowerShell are imperative — for repeatable infrastructure use Bicep/Terraform and reserve CLI for operations, diagnostics and one-off remediation.
- **Discoverability:** `az find`, `az <group> -h`, `az upgrade`; extension model (`az extension add/update`), and `az config set` for defaults.
- Use case: a runbook/pipeline that queries Resource Graph, remediates with `az`, and asserts the result — all with managed identity.

**Edge Cases & Gotchas**
- **Context drift**: running a destructive command while pointed at the wrong subscription is a classic outage. Always `az account show` before mutating, and use explicit `--subscription`/`-SubscriptionId` in scripts.
- Interactive prompts in CI hang the pipeline — pass `--yes`/`--no-wait` deliberately and set non-interactive defaults (`az config set core.only_show_errors=true`).
- `az` and `Az` are separate codebases with different parameter names (`--resource-group` vs `-ResourceGroupName`) — mixing them in one script causes silent mistakes.
- Deprecated modules/calls (AzureRM, `az vm create` older parameter sets) still "work" until they don't — pin versions and read deprecation notices.
- Service principal secrets in scripts are a finding; use federated credentials and short-lived tokens.
- Long-running commands with `--no-wait` return before the operation completes — poll the operation (`az ... show` / provisioningState) before the next step.
- PowerShell output that is an object array vs a single object changes pipeline behaviour (`@()` wrapping, `-First 1`).
- CLI throttling (429) on tight loops — add backoff and reduce call counts by batching with Resource Graph.

**Comparison**
- **Azure CLI** — shell-friendly, JSON/table output, best for CI on Linux and quick scripting.
- **Az PowerShell** — object pipeline, Windows/admin-friendly, strong for bulk resource manipulation and reporting.
- **Bicep/Terraform** — declarative, reviewed infrastructure; the correct tool for standing resources.
- **Portal** — discovery/visual checks; never the change-control mechanism.

**Interview Questions**
- **Basic — How do you authenticate a pipeline to Azure without storing a password?** → Workload identity federation (OIDC): a federated credential trusts the pipeline's issuer/subject and exchanges a short-lived token; or a managed identity when the runner is in Azure.
- **Medium — When CLI versus IaC?** → IaC (Bicep/Terraform) owns standing infrastructure so changes are reviewed, repeatable and drift-detected; CLI/PowerShell own operations, diagnostics and one-off remediation.
- **Hard/Scenario — A script deleted the wrong resource group.** → Context drift or a variable expansion bug inside a loop. Prevent by asserting `az account show`/subscription and resource identity at the top of every script, using `--what-if`/dry-run for anything destructive, requiring explicit resource IDs (not names), deleting only resources selected by tag/owner, and running destructive actions through reviewed pipelines with `CanNotDelete` locks in place.

---

# PART 9 — IaC & DEVOPS ON AZURE

## 9.1 ARM Templates & Bicep ★★★

**Definition:** ARM is Azure's declarative resource-manager API; Bicep is a domain-specific language that transpiles to ARM JSON with cleaner syntax, modules and type safety.

**Important Points**
- **Template anatomy:** `$schema`, `contentVersion`, `parameters`, `variables`, `resources`, `outputs`; Bicep equivalents (`param`, `var`, `resource`, `output`, `module`).
- **Deployment modes:** **Incremental** (default — creates/updates, leaves others) vs **Complete** (deletes resources in the scope not in the template — dangerous unless the scope is dedicated).
- **Scopes:** resource group, subscription, management group, tenant; **nested/child templates** and **Bicep modules**; **template specs** for reusable approved templates; **deployment stacks** for lifecycle + deny settings (verify current GA state).
- **`what-if`** previews changes (`az deployment group what-if`) — always run before apply.
- **`dependsOn`** and implicit dependencies; `existing` keyword in Bicep to reference without redeploying.
- **Loops** (`for`), conditions (`if`), scopes (`scope:`), and user-defined types (newer Bicep).
- **State:** ARM/Bicep have **no local state file** — Azure Resource Manager is the source of truth. This is the biggest conceptual difference from Terraform.
- **Linting:** `bicep lint`, `arm-ttk`, `PSRule for Azure`.
- Use case: a landing-zone module library in Bicep with a subscription-scoped deployment that creates RGs, VNets, policy assignments and diagnostics.

**Edge Cases & Gotchas**
- **Complete mode deletes resources** not in the template — never use it casually on a shared RG.
- Bicep/ARM will not manage resources created outside the template in the same way Terraform does; drift is not detected automatically (use what-if/Policy).
- Deployment failures roll back inconsistently — a partially applied deployment can leave resources behind; check the operation list.
- Deleting a deployment **does not** delete the resources (unless deployment stacks are used).
- Secrets in parameter files end up in deployment history — use Key Vault references or secure parameters.
- API versions matter; older versions miss properties and new features.
- Cross-scope deployments (e.g., subscription-level policy) need the right scope and permissions (`User Access Administrator` for role assignments).
- `what-if` can show noisy/false changes (e.g., generated values) — interpret with experience.

**Interview Questions**
- **Basic — What is Bicep?** → A declarative IaC language for Azure that transpiles to ARM templates, with modules, loops and type safety.
- **Medium — Incremental vs Complete mode?** → Incremental adds/updates resources and leaves others untouched; Complete makes the scope match the template exactly, deleting anything not declared.
- **Hard/Scenario — A pipeline deployment deleted a database.** → Complete deployment mode on a shared resource group with the database (or a child resource) not in the template. Recovery: PITR restore, then switch to incremental mode, isolate stateful resources into their own RG/stack, add `prevent`/locks, and require `what-if` review gates in the pipeline.

## 9.2 Terraform on Azure ★★★ · `TIER 1`

**Definition:** Terraform uses the AzureRM/AzAPI providers to plan and apply Azure resources, with state stored remotely (typically an Azure Storage account).

**Important Points**
- **Providers:** `azurerm` (curated, opinionated) and `azapi` (raw ARM — use for preview/new features).
- **State:** remote backend in Azure Storage (`azurerm` backend) with container, key, and **state locking via blob lease**; enable versioning + soft delete on the storage account.
- **State per environment/scope:** separate state files per subscription/environment; **workspaces** exist but separate directories/state is safer for isolation.
- **Auth:** Azure CLI/service principal/**OIDC workload identity federation** from GitHub Actions/Azure DevOps (recommended, no secrets).
- **Modules:** registry modules (e.g., AVM — Azure Verified Modules), version pinning.
- **Workflow:** `fmt` → `validate` → `plan` (saved artifact) → approval → `apply` (the saved plan), with `-out`/`plan` gating.
- **Drift:** scheduled `plan -detailed-exitcode`; import blocks for brownfield; `moved` blocks for refactors.
- **Policy:** `terraform-compliance`/OPA/Checkov/tfsec in CI; Azure Policy remains the runtime guardrail.
- Use case: 40 subscriptions managed from one repo with per-subscription state, AVM modules, OIDC auth and plan-based approvals.

**When to use / alternatives:** **Terraform** when you need multi-cloud/multi-provider, a mature plan/apply workflow, or an existing Terraform estate. **Bicep** for Azure-only estates wanting ARM-native day-zero support with **no state file**. **ARM JSON** only for legacy templates. Use **azapi** for preview features the AzureRM provider has not caught up with. Whichever you choose, the pipeline (not a laptop) should apply.
**Edge Cases & Gotchas**
- **State locking** requires the storage account to be reachable and not locked; a stuck lease blocks all runs (break the lease carefully).
- State contains secrets in plaintext (e.g., generated keys) — restrict access and enable encryption.
- `terraform destroy` in the wrong workspace destroys production — `prevent_destroy`, separate workspaces, and RBAC guardrails.
- Complete-mode equivalents: Terraform deletes resources it manages but not what it doesn't know about — but `state rm` mistakes cause orphans that still bill.
- Provider upgrade breaking changes; pin `~>` versions.
- Importing resources doesn't generate config (newer `import` blocks help) — mismatch causes plans that destroy/replace.
- Plan/apply drift between CI and local runs; enforce pipeline-only applies for prod.
- Long-lived service principal secrets in CI are a finding — use federated credentials.

**Production Troubleshooting**
```bash
# 1. Who holds the state lock? (blob lease on the state file)
az storage blob show --account-name <tfstate> --container-name tfstate --name prod.tfstate \
  --query "{lease:properties.lease,etag:properties.etag}"

# 2. What does the plan really want to do? (drift vs intended, and replacements)
terraform plan -detailed-exitcode -out=tfplan
terraform show -json tfplan | jq '.resource_changes[] | select(.change.actions|index("delete") or index("replace")) | .address'

# 3. Did someone change the portal? (correlate drift with Activity Log)
az monitor activity-log list --offset 24h --query "[?contains(operationName.value,'write')].{t:eventTimestamp,caller:caller,op:operationName.value}" -o table
```
Interpretation: an old `lease` with no running pipeline = stale lock → `terraform force-unlock <id>` only after confirming the remote state is intact. A plan full of `update` on resources nobody touched = console drift; decide policy (revert or codify) before applying. Any unexpected `replace` on a database/disk/VM means **stop** and restructure state first.

**Interview Questions**
- **Basic — Where is Terraform state stored for Azure?** → Remote state in an Azure Storage container (with locking via blob lease), never on a laptop or in Git.
- **Medium — Bicep vs Terraform?** → Bicep is Azure-native with no state and ARM-native day-zero support; Terraform is multi-cloud with a state file, a larger provider ecosystem and mature plan workflow.
- **Hard/Scenario — Terraform wants to replace a production VM after an unrelated change.** → Run `plan` and inspect the replacement reason (often a changed `name`, `zone`, `size` requiring replacement, or a provider behaviour change). Use `lifecycle { prevent_destroy }`, `create_before_destroy` where appropriate, `moved` blocks for refactors, and separate stateful resources into their own state.

## 9.3 Azure DevOps & GitHub Actions ★★★

**Definition:** CI/CD platforms (Azure Pipelines/GitHub Actions) that build, test, scan and deploy Azure resources and applications.

**Important Points**
- **Azure Pipelines:** YAML pipelines, stages/jobs/steps, **service connections** (prefer **workload identity federation** over secrets), **environments** with approvals/checks, **variable groups** linked to Key Vault, self-hosted vs Microsoft-hosted agents, templates for reuse.
- **GitHub Actions:** workflows, OIDC federated credentials to Entra ID, environments with protection rules, reusable workflows/composite actions, self-hosted runners (VNet access) vs hosted runners (public endpoints).
- **Deployment strategies:** framework-specified rolling, **slots swap** (App Service), blue/green, canary (Front Door/Traffic Manager weight), and `az deployment` with what-if gates.
- **Pipeline stages:** lint/validate → build → unit tests → security scan (SAST/SCA/IaC) → deploy dev → integration/e2e → approval → deploy prod → smoke tests.
- **Secrets:** Key Vault + managed identity/OIDC; never in YAML/variable groups in plaintext.
- **Artifacts:** versioned build output, container images in **ACR** (with geo-replication and tasks).
- **Infrastructure pipelines vs application pipelines** separated with different approvals/roles.
- Use case: PR pipeline runs `bicep what-if` + tests; merge deploys dev automatically; prod requires an environment approval and runs smoke tests + rollback.

**Edge Cases & Gotchas**
- Service connections/service principals with **Owner at subscription scope** are a top audit finding — scope to RG, use custom roles, use federation.
- Approvals in Azure DevOps environments apply per stage, but a bypassed "check" (branch control) can let unapproved code through.
- Long-lived secrets in variable groups; Key Vault-linked groups still copy values at runtime — prefer OIDC + Key Vault references.
- Self-hosted agents inside a VNet are needed for private endpoints; hosted agents cannot reach private resources.
- Concurrent deployments to the same environment corrupt state — use locks/exclusive locks in pipelines.
- Hosted agent IPs vary — IP-restricted resources need self-hosted or private endpoints.
- Rollbacks are rarely automated; without versioned artifacts + slots, "rollback" is a redeploy from memory.
- Pipeline permissions to create role assignments need `User Access Administrator`/Owner — grant at the narrowest scope.

**Interview Questions**
- **Basic — How do you authenticate a pipeline to Azure without secrets?** → Workload identity federation (OIDC): a federated credential trusts the pipeline's issuer/subject and exchanges a short-lived token for an Entra token.
- **Medium — Deployment slots vs blue/green?** → Slots are App Service's built-in blue/green with warm-up and swap; blue/green in general means a parallel environment switched at the traffic layer (Front Door/App Gateway).
- **Hard/Scenario — A prod deployment must be reversible within 5 minutes.** → Deploy immutable artifacts, use slots with swap-back or keep the previous container image tag, automate rollback on smoke-test/alarm failure, and make database changes backward-compatible (expand/contract) so the old version can run.

## 9.4 Azure Container Registry & Supply Chain ★★

**Definition:** ACR is a managed Docker/OCI registry with geo-replication, tasks, retention and security integrations.

**Important Points**
- **SKUs:** Basic, Standard, Premium (geo-replication, private link, content trust, higher throughput).
- **Auth:** Entra ID (managed identity for AKS/App Service), admin account (disable), ACR tokens with scoped permissions, repository-scoped tokens.
- **Features:** **ACR Tasks** (build/patch on commit), **geo-replication** for multi-Region pulls, **retention policy** for untagged manifests, **image scanning** (Defender for Containers/Qualys), **signing** (Notation), **private endpoint** + firewall, **artifact cache** for upstream registries (verify).
- **AKS integration:** attach ACR to AKS (kubelet identity gets `AcrPull`); avoid imagePullSecrets where possible.
- Use case: Premium ACR geo-replicated to two Regions, private endpoint, Defender scanning, immutable tags, AKS pulls via attached identity.

**Edge Cases & Gotchas**
- `ImagePullBackOff` after identity changes — check `AcrPull` on the kubelet identity and network path (private endpoint DNS).
- Admin account enabled is a common security finding.
- Untagged images accumulate cost — retention policy is not default-on in every SKU.
- Geo-replication does not replicate all artifact types in every configuration (verify).
- Private endpoint requires private DNS zone `privatelink.azurecr.io` linked to the AKS VNet.
- Tag mutability breaks reproducibility — use digests or immutable tags.

**Interview Questions**
- **Basic — How does AKS pull from a private ACR?** → Attach ACR to AKS (grants `AcrPull` to the kubelet identity) and ensure network access via private endpoint/DNS.
- **Medium — Why immutable tags/digests?** → Guarantees the deployed artifact is exactly what was tested, enabling rollbacks and audit.
- **Hard/Scenario — A new Region's cluster cannot pull images while the primary can.** → ACR isn't geo-replicated to the new Region, or the cluster's identity lacks `AcrPull`, or the private endpoint DNS isn't linked to the new VNet. Check `az acr replication list`, role assignments and `nslookup <registry>.azurecr.io` from a pod.

## 9.5 Deployment Strategies on Azure ★★★

**Definition:** Patterns for releasing changes with controlled risk: rolling, blue/green, canary, ring, and feature flags.

**Important Points**
- **Rolling:** replace instances in batches (VMSS rolling upgrade, AKS maxSurge/maxUnavailable). Simple, no extra infrastructure, temporary mixed versions.
- **Blue/green:** two identical environments; switch traffic at App Gateway/Front Door/DNS after validation. Instant rollback by switching back.
- **Canary:** small percentage of traffic to the new version via Front Door/Traffic Manager weights or App Gateway backend pools; increase based on metrics.
- **Ring:** internal → pilot customers → everyone.
- **Feature flags:** decouple deploy from release; dark launches.
- **Database changes:** expand/contract, backward-compatible migrations, never destructive in the same release as code.
- **App Service slots:** a built-in blue/green with warm-up, swap and swap-back.
- Use case: API v2 via Front Door 5% → 25% → 100% with automatic rollback on 5xx/latency alarms.

**Edge Cases & Gotchas**
- Session state on local disk breaks blue/green and canary — externalise (Redis/SQL).
- Blue/green doubles cost while both environments run.
- Canary with a shared database means the schema must support both versions.
- Traffic weights don't control already-open connections; long-lived WebSockets/HTTP2 may pin to the old version.
- Health checks that pass on a static page mask canary failures.
- Slot swap can swap app settings by accident if not marked slot-sticky.

**Interview Questions**
- **Basic — What is blue/green?** → Running two identical environments and switching traffic after validating the new one.
- **Medium — When canary over blue/green?** → When you want progressive exposure and real-traffic validation with a fast rollback path, rather than an all-at-once switch.
- **Hard/Scenario — A canary passes smoke tests but error rates rise at 25% traffic.** → Smoke tests don't cover real traffic paths. Add automated gates on error rate, latency and saturation before each increment, correlate with App Insights dependency failures, and auto-rollback. Then fix the root cause with a targeted test added to the suite.

---

# PART 10 — HIGH AVAILABILITY & DISASTER RECOVERY DESIGN

## 10.1 Azure Resiliency Building Blocks ★★★

**Definition:** The layers of resilience available in Azure: instance redundancy, zone redundancy, regional DR, and global routing.

**Important Points**

| Layer | Mechanism | Protects against | Examples |
| --- | --- | --- | --- |
| Instance | Multiple instances, health probes, autoscale | Process/host failure | VMSS, App Service instances |
| Zone | Zone-redundant or zonal placement | Datacenter/AZ failure | ZRS storage, zone-redundant LB/SQL/Firewall |
| Region | Multi-Region replication + routing | Region failure | SQL failover groups, Cosmos DB multi-write, ASR, RA-GRS |
| Global | Anycast/proxied entry | Regional loss + client routing | Front Door, Traffic Manager, Azure DNS |
| Data protection | Backup, snapshots, immutable storage | Corruption/deletion/ransomware | Azure Backup, soft delete, WORM |

- **Composite SLA math:** 99.9% × 99.9% ≈ 99.8%; adding serial dependencies lowers availability, redundancy raises it. Quote the SLA of the whole path, not one service.
- **Design for failure of a zone by default**; design for Region failure where the business case justifies the cost.
- **State is the hard part:** compute is easy to duplicate; data replication and consistency determine real RTO/RPO.
- Use case: Front Door → App Gateway (zone-redundant) → App Service (3 instances, zone-redundant) → Azure SQL zone-redundant + failover group → ZRS/GZRS storage → Backup + ASR.

**Interview Questions**
- **Basic — What are the four resilience layers?** → Instance redundancy, zone redundancy, regional DR, and global traffic routing (plus backup for data protection).
- **Medium — Why is a composite SLA lower than the individual SLAs?** → Serial dependencies multiply: 99.9% × 99.9% × 99.9% ≈ 99.7%. Redundancy and independence raise it; each added serial dependency lowers it.
- **Hard/Scenario — The platform claims 99.99% but outages are frequent.** → Audit every dependency's zone/Region scope (DB, cache, DNS, firewall, Key Vault), single-instance components, deployment practices, and whether DR has been tested. Then set an SLO, measure error budget, and fix the weakest serial dependency rather than adding more instances at the front end.

**Edge Cases & Gotchas**
- Zone redundancy is **per service and per tier** — a zone-redundant front end with a single-zone cache or NAT gateway still fails.
- Some services are regional-only and cannot be made zone-resilient (or require a different SKU/Region).
- Composite SLAs assume independent failures; shared dependencies (DNS, identity, a shared hub firewall) correlate failures across "independent" tiers.
- Global services (Entra ID, ARM control plane, Front Door) are outside your zone design — plan for control-plane outages (deployments fail while data plane runs).
- Backup is not HA and HA is not backup — you need both, engineered independently.

## 10.2 Four DR Strategies on Azure ★★★

**Definition:** Backup & restore, pilot light, warm standby, and active-active — each trading cost for RTO/RPO.

**Important Points**
- Choose the cheapest strategy that meets the **business-approved RTO/RPO** — not the most resilient one you can imagine.
- RPO is set by the data replication mechanism; RTO is set by infrastructure readiness, automation and the runbook (people are usually the slowest step).
- Active-active requires stateless application design and conflict-tolerant data — a rewrite, not a deployment change.
- Every strategy needs the DR Region's "boring" dependencies pre-created: VNet/subnets, NSGs, DNS zones, Key Vault, identities, certificates, images and quotas.
- The cost of DR is continuous (duplicate capacity, replication egress); the cost of not having it is an outage.

| Strategy | Secondary Region state | RTO | RPO | Cost | Azure tooling |
| --- | --- | --- | --- | --- | --- |
| Backup & restore | Nothing running; backups replicated | Hours–days | Hours | $ | Azure Backup + Cross-Region Restore, geo-redundant storage, IaC rebuild |
| Pilot light | Data replicated + core network/identity; app tier off/absent | 30 min–hours | Minutes | $$ | SQL failover groups, ASR (VMs off), IaC for compute |
| Warm standby | Scaled-down full stack running | Minutes | Seconds–minutes | $$$ | ASR, SQL failover group, Front Door priority routing, pre-built App Service/VMSS |
| Active-active | Full capacity in 2+ Regions serving traffic | Near-zero | Near-zero (data-dependent) | $$$$ | Front Door, Cosmos DB multi-write / SQL geo-secondary, stateless app design |

- **What must exist in the DR Region:** VNet + subnets + NSGs + routes + firewall, private DNS zones linked, Key Vault + keys + secrets, managed identities/permissions, certificates, container images (geo-replicated ACR), VM images, quotas, and monitoring/alerting.
- **Traffic switch:** Front Door (fast, proxied) > Traffic Manager (DNS TTL) > manual DNS.
- **Data:** SQL failover groups (async), Cosmos DB multi-Region (sync/async per consistency), storage RA-GRS (async ~15 min), ASR (crash-consistent ~5 min), app-level replication.
- **Test:** planned failover drills, ASR test failover into an isolated VNet, Chaos Studio experiments, and measured RTO/RPO records.
- Use case: pilot light for internal apps; warm standby for customer-facing; active-active for global read-heavy APIs on Cosmos DB.

**Edge Cases & Gotchas**
- The DR Region often fails on the **missing dependency**: DNS zone link, Key Vault permission, certificate, managed identity, or quota — not the compute.
- GRS/ASR target may be outside your data-residency boundary.
- Failover without failback planning leaves you stranded in the secondary with drift.
- Active-active requires **conflict-free data** and idempotent writes — many apps are not ready.
- DNS-based failover is slower than proxied failover; don't promise 30-second RTO with Traffic Manager and 60-second TTL.
- Untested DR runbooks are assumptions, not plans.

**Interview Questions**
- **Basic — What is pilot light on Azure?** → Core data and minimal infrastructure are replicated/pre-created in a secondary Region; the rest is provisioned or scaled during failover.
- **Medium — Warm standby vs active-active?** → Warm standby runs a scaled-down full stack and scales up on failover; active-active serves production traffic from multiple Regions simultaneously.
- **Hard/Scenario — Design 15-minute RTO / 5-minute RPO for a 3-tier app.** → Warm standby: zone-redundant primary, SQL failover group to the secondary with lag alarms, ASR or pre-deployed VMSS/App Service in the secondary, Front Door with health-probed origin groups and priority routing, pre-linked private DNS and Key Vault, runbook automated with pipelines, quarterly drills measuring actual RTO/RPO.

## 10.3 Designing a Highly Available Three-Tier Azure Application ★★★

**Definition:** Separating presentation, application and data tiers while adding redundancy, health checks and recovery at each layer.

**Important Points**
- **Presentation:** Front Door (global) → App Gateway with WAF (regional) → static content on storage + CDN; zone-redundant frontends.
- **Application:** App Service (3+ instances, zone-redundant), VMSS across zones, or AKS with multi-zone node pools; **stateless** design with external session state.
- **Data:** Azure SQL Business Critical zone-redundant + failover group; Cosmos DB multi-region; storage ZRS/GZRS; cache zone-redundant; backups.
- **Identity/secrets:** managed identities, Key Vault with private endpoint and purge protection, keys replicated for DR.
- **Network:** hub-and-spoke with firewall egress, private endpoints for PaaS, private DNS linked everywhere, Bastion/JIT for admin.
- **Observability:** App Insights + Log Analytics + alerts (5xx, latency, saturation, dependency failures) + Service Health alerts.
- **Recovery:** Backup + ASR/DR Region, documented and tested runbooks.
- **Change safety:** IaC, staged deployments, slots/canary, backward-compatible DB migrations.
- Use case: e-commerce app in `centralindia` with DR in `southindia`, active-passive.

**Edge Cases & Gotchas**
- Multi-zone compute with a single-zone database gives an illusion of HA — audit every dependency's zone/Region scope.
- Session state on a VM/instance breaks scale-out and failover.
- A private DNS failure looks like a database outage — monitor DNS resolution.
- Front Door origin health checks point at a static page and fail over to a broken origin.
- Scaling limits (App Service plan max instances, subnet IPs, quotas) cap real capacity — test at scale.
- Cost of DR capacity is often not budgeted — agree the strategy with the business.

**Interview Questions**
- **Basic — What are the three tiers?** → Presentation, application/business logic, and data.
- **Medium — How do you make each tier highly available?** → Redundant instances across zones behind health-probed load balancers (presentation/app), and zone-redundant plus geo-replicated data with backups (data).
- **Hard/Scenario — Survive a full Region outage with minimal downtime.** → Front Door with two origin groups, warm standby in the secondary Region (App Service/VMSS pre-deployed), SQL failover group or Cosmos DB multi-Region, pre-linked private DNS and Key Vault, externalised session state, automated runbook + regular drills.

## 10.4 Reliability Patterns & Chaos Engineering on Azure ★★

**Definition:** Application-level patterns (retry, circuit breaker, bulkhead, idempotency, queue-based load levelling) plus controlled failure injection.

**Important Points**
- **Transient fault handling:** retries with exponential backoff + jitter via SDKs (Polly, `Microsoft.Extensions.Http.Resilience`, Azure SDK retry policies); retry only idempotent/transient failures.
- **Circuit breaker / bulkhead / timeout:** isolate failure domains per dependency.
- **Queue-based load levelling:** Service Bus/Storage Queue absorbs spikes; consumers scale on queue depth (KEDA).
- **Idempotency:** payment/order APIs must tolerate retries — idempotency keys, dedup tables, conditional writes.
- **Graceful degradation:** cached/stale reads, feature toggles, read-only mode.
- **Chaos Studio:** experiments (VM shutdown, network latency, NSG deny) with scoped targets and stop conditions (verify region/support).
- **Availability tests + Synthetic transactions** to detect user-impacting failures early.
- Use case: Service Bus consumer with Polly retries, circuit breaker to a payment gateway, idempotency keys, and quarterly Chaos Studio experiments on the app tier.

**Edge Cases & Gotchas**
- Retry without jitter creates synchronised retry storms.
- Retrying a non-idempotent POST duplicates business operations.
- Timeouts must be shorter than the caller's timeout, cascading inward.
- Circuit breakers need sane thresholds and half-open probes, or they flap.
- Chaos experiments in production need explicit business approval and blast-radius limits.
- Health checks that call dependencies can cause the whole fleet to go unhealthy during a dependency blip (use shallow liveness + deep readiness).

**Interview Questions**
- **Basic — Why is idempotency required?** → Because messaging and HTTP retries are inevitable; idempotent handlers ensure a repeated request doesn't duplicate side effects.
- **Medium — What does a circuit breaker protect?** → It prevents cascading failure by failing fast when a dependency is unhealthy and recovering gradually.
- **Hard/Scenario — One dependency outage takes down the entire site.** → The app has no timeouts/bulkheads/circuit breakers and shares a single thread pool. Add per-dependency timeouts, bounded concurrency, circuit breakers, cached fallbacks, and load-test to prove isolation; add a Chaos experiment to prevent regression.

---

# PART 11 — SENIOR SCENARIO DRILLS

> Say each answer out loud in 60–90 seconds, then compare.

**1. Two peered VNets cannot communicate.**
Peering state on **both** sides, address overlap, effective routes, NSGs at subnet and NIC, Azure Firewall/NVA policy, DNS for hostnames, guest firewall. Peering is not transitive.

**2. Application Gateway returns HTTP 502.**
Backend health, probe path/host header/port, HTTP settings (protocol, `Pick hostname from backend`, timeout), NSG on the backend subnet, backend listener, TLS trust for end-to-end, and access logs. 504 = backend timeout, 502 = bad backend response.

**3. Managed identity cannot read a Key Vault secret.**
Identity assigned to the resource, correct secret scope, RBAC role (`Key Vault Secrets User`) or access policy, secret enabled and not expired, network path (private endpoint DNS/firewall), Key Vault audit logs, throttling, and token audience.

**4. The primary Azure Region fails.**
Front Door/Traffic Manager failover, SQL failover group/Cosmos DB secondary, ASR or pre-deployed compute, private DNS and Key Vault available in the secondary, connection strings using listeners, measured RTO/RPO, and a failback plan.

**5. Application latency rises but VM CPU is normal.**
Percentile latency, dependency timings (SQL/cache/HTTP), thread pool/connection pool saturation, GC pauses, disk/network queue depth, downstream throttling, and App Insights transaction view. CPU average hides queueing and I/O waits.

**6. VMSS won't scale during a spike.**
Autoscale enabled/rules/max instances, metric correctness (guest vs host), cooldown, quota (`az vm list-usage`), capacity (`AllocationFailed`), subnet IPs, and load balancer probe health.

**7. App Service works publicly but can't reach a private SQL endpoint.**
VNet integration subnet (delegated), private endpoint approval/DNS zone link, resolution of the SQL FQDN to the private IP from the app (`nameresolver`), NSGs, and SQL `publicNetworkAccess`. Authentication is a separate check.

**8. AKS pods stay Pending.**
Subnet IP exhaustion (Azure CNI), node quota/capacity, insufficient CPU/memory requests, taints/affinity/topology spread, PVC zone mismatch (Azure Disk is zonal), and autoscaler configuration.

**9. A developer deleted a resource group in production.**
Restore from backup/PITR where possible, check soft delete for storage/Key Vault, use Resource Graph/Activity Log to identify what existed, and rebuild from IaC. Prevent: `CanNotDelete` locks, PIM-gated Contributor, deny-action policies, and backup/DR.

**10. A storage account became publicly accessible.**
Contain immediately (set `publicNetworkAccess: Disabled`, firewall, remove SAS), review logs/Activity Log, rotate keys and revoke SAS, then enforce private endpoints + Policy + Defender for Storage.

**11. Log Analytics costs doubled.**
Check ingestion by table/resource, VM insights/Container Insights volume, diagnostic categories too verbose, Application Insights sampling, retention and table plans, and duplicate collection (multiple DCRs/agents). Tune at the source.

**12. ExpressRoute circuit is up but traffic fails to a VNet.**
BGP routes advertised/received, gateway SKU/health, `GatewaySubnet` correctness, VNet peering to the gateway, UDR overrides, NSGs, overlapping prefixes, and asymmetric routing.

**13. An AKS cluster must be upgraded with zero downtime.**
Control-plane upgrade first, then node pools with surge settings, PodDisruptionBudgets, multi-zone/replica capacity headroom, API deprecation check, tested in staging, and a rollback/mitigation plan (blue/green node pools for critical workloads).

**14. Traffic Manager failover leaves some users on the dead Region.**
DNS TTL and resolver caching, long-lived connections, and probe evaluation time. Reduce TTL, use Front Door (proxied) for strict RTO, and add client-side retry/DNS refresh.

**15. A pipeline with Owner rights was compromised.**
**16. A private endpoint works from the hub but not from a spoke.**
Check that the `privatelink.*` zone is linked to the spoke VNet (or that the spoke forwards DNS to the hub resolver), then `nslookup` from a pod/VM in the spoke. The endpoint's approval state and NSGs are usually fine — it is DNS.

**17. An unhealthy VMSS deployment must be recovered during a release.**
`az vmss get-instance-view` → `ProvisioningState/failed`; check `AllocationFailed` (capacity/quota) vs application health. Roll back to the previous model (`az vmss update` with the prior image version or rollback the pipeline), then fix startup/health grace periods before re-releasing.

**18. Patch compliance shows machines missing updates for months.**
Check dynamic scoping (is the machine in a maintenance configuration?), excluded classifications, pending reboots, deallocated VMs at window time, and Arc agent health. Prove with the machine's own inventory, not the portal.

**19. Terraform state is locked and the pipeline is blocked before a release.**
Inspect the blob lease; confirm no active run; `terraform force-unlock`; then add a pipeline concurrency lock and alerting so a killed job cannot silently hold state.

**20. A regional failover is ordered by the business — explain how you execute it.**
Declare, then: verify data replication/lag, promote the database or fail the failover group, scale the secondary compute to production capacity, switch Front Door/Traffic Manager priorities, validate a smoke transaction, confirm the failback plan, and report the achieved RTO/RPO with evidence.

Revoke the service connection/federated credential, rotate secrets, review Activity Log and deployment history for malicious changes, scope the connection to RG-level custom roles, enable approvals/branch policies, and enforce pipeline permissions reviews.

---

# PART 12 — RAPID REVISION

## 12.1 AWS ↔ Azure equivalents — one concise sheet (Tier-1 services only)

| Capability | AWS | Azure | Important distinction |
<!-- Awareness-level mapping. Do not memorise service-for-service parity; the distinctions matter more than the names. -->
| --- | --- | --- | --- |
| Region / AZ | Region / AZ | Region / AZ | Azure subnets are **not** zonal; resources are |
| Private network | VPC | VNet | Azure reserves 5 IPs; subnets carry NSG/UDR |
| Stateful filter | Security Group | NSG | NSG supports **explicit deny**; SG does not |
| Stateless subnet filter | NACL | (none directly; NSG at subnet) | Azure has no separate stateless ACL |
| Resource grouping for rules | SG referencing | **ASG** | ASGs group NICs; SGs also enforce |
| Central transit | Transit Gateway | Virtual WAN / hub-and-spoke + VNet Manager | VWAN is managed hubs, no peering mesh |
| Private PaaS access | PrivateLink endpoint | Private Endpoint / Private Link | Azure needs private DNS zone links |
| Outbound NAT | NAT Gateway | NAT Gateway | Azure's default outbound is being retired |
| L4 LB | NLB | Azure Load Balancer (Standard) | Zone-redundant frontends |
| L7 LB | ALB | Application Gateway | WAF_v2, path/host routing |
| Global L7 entry | CloudFront / Global Accelerator | Front Door | Global anycast + WAF + caching |
| DNS routing | Route 53 policies | Traffic Manager | DNS-based, not in data path |
| CDN | CloudFront | Azure Front Door / CDN | Front Door Premium has Private Link origins |
| Hybrid private | Direct Connect | ExpressRoute | Both need redundant circuits |
| Hybrid encrypted | Site-to-Site VPN | VPN Gateway | BGP + active-active |
| VM | EC2 | Azure VM | Stop ≠ deallocate |
| VM fleet scaling | ASG | VMSS | Uniform vs Flexible orchestration |
| Serverless containers | Fargate | Container Apps / ACI | ACA has KEDA/scale-to-zero |
| Kubernetes | EKS | AKS | Control plane free tier exists |
| Serverless functions | Lambda | Azure Functions | Consumption vs Premium plans |
| Object storage | S3 | Blob Storage | Tiers Hot/Cool/Cold/Archive |
| Block storage | EBS | Managed Disks | Ultra/Premium SSD v2 |
| Shared file | EFS / FSx | Azure Files / NetApp Files | SMB/NFS support differs |
| Managed relational | RDS / Aurora | Azure SQL DB / SQL MI / Flexible Server | MI for instance-level features |
| Global NoSQL | DynamoDB (+Global Tables) | Cosmos DB | Consistency levels, RU/s |
| Queue | SQS | Storage Queue / Service Bus | Service Bus adds sessions, topics, transactions |
| Pub/sub | SNS | Service Bus topics / Event Grid | Event Grid = event routing |
| Event bus | EventBridge | Event Grid | Both at-least-once |
| IAM | IAM roles/policies | Entra ID + Azure RBAC | Authentication vs authorization split |
| SCP | Organizations SCP | Azure Policy (+ Deny) + management groups | Policy is config-based, SCP is permission-based |
| Secrets | Secrets Manager / SSM | Key Vault | RBAC vs access policy |
| KMS | KMS | Key Vault keys / Managed HSM | CMK requires managed identity |
| Audit API calls | CloudTrail | Activity Log | Activity Log retains 90 days |
| Resource config audit | AWS Config | Azure Policy + Resource Graph | Policy evaluates continuously |
| Threat detection | GuardDuty | Defender for Cloud | Sentinel for SIEM |
| Monitoring | CloudWatch | Azure Monitor | Metrics + Log Analytics |
| Backup | AWS Backup | Azure Backup | Vault redundancy choice |
| DR replication | Elastic Disaster Recovery | Azure Site Recovery | Recovery plans + test failover |
| IaC native | CloudFormation | ARM / Bicep | Bicep has **no state file** |

## 12.2 Numbers worth memorising (verify before quoting)

| Item | Value |
| --- | --- |
| Azure reserved IPs per subnet | 5 (`/24` = 251 usable, `/29` = 3 usable) |
| Route selection | Longest prefix → UDR > BGP > system |
| NSG priority range | 100–4096 (lower wins) |
| Management group depth | 6 levels below root, 10,000 MGs |
| Activity Log retention | 90 days |
| Platform metrics retention | ~93 days |
| Log Analytics interactive retention | 30 days default, up to 730 |
| Blob tiers minimum duration | Cool 30 d, Cold 90 d, Archive 180 d |
| GRS replication RPO target | ~15 minutes (verify) |
| ASR crash-consistent RPO | ~5 minutes |
| SQL DB PITR | 7 days default, 35 max |
| SQL DB LTR | Up to 10 years |
| Key Vault soft delete | 90 days |
| Key Vault secret max size | 25 KB |
| VM SLA (2+ instances in a set/zone) | 99.95% (set) / 99.99% (zones) |
| App Gateway subnet | /24 recommended, /26 minimum (v2) |
| Bastion subnet | /26 minimum recommended |
| Firewall subnet | /26 (AzureFirewallSubnet) |
| GatewaySubnet | /27+ recommended |
| Cosmos DB logical partition limit | 20 GB |
| Azure Files SMB/NFS | SMB 3.x; NFS 4.1 Premium only |
| Public IP SKU note | Standard is static, secure by default |

## 12.3 One-line answers you must not fumble

- **NSG vs ASG** → NSG enforces rules; ASG groups NICs for use in rules.
- **NSG vs Azure Firewall** → distributed L3/L4 vs centralised stateful with FQDN/IDPS.
- **Service endpoint vs private endpoint** → public IP + VNet restriction vs private IP in your subnet.
- **Load Balancer vs App Gateway** → L4 flow hashing vs L7 HTTP routing + WAF.
- **App Gateway vs Front Door** → regional L7 vs global edge with anycast + caching.
- **Traffic Manager vs Front Door** → DNS answer vs proxied request path.
- **VNet peering vs Virtual WAN** → manual peerings/UDRs vs managed hubs with automatic transit.
- **Availability Set vs Zone** → host/rack+maintenance vs datacenter-level isolation.
- **Stop vs deallocate** → compute still billed vs compute released.
- **App Service VNet integration vs private endpoint** → outbound vs inbound.
- **RBAC vs Policy** → who can act vs what the result must look like.
- **Entra ID vs RBAC** → authentication vs authorization on resources.
- **Key Vault RBAC vs access policy** → central role model vs vault-local legacy.
- **Backup vs ASR** → recoverable copies vs orchestrated failover.
- **GRS vs RA-GRS** → secondary not readable vs readable secondary.
- **LRS vs ZRS** → one datacenter vs three zones.
- **Bicep vs Terraform** → no state, ARM-native vs state file, multi-cloud.
- **Incremental vs Complete deployment** → additive vs exact-match with deletions.

## 12.4 Final 60-second self-test

1. Draw a hub-and-spoke with Azure Firewall, private DNS, private endpoints and Bastion — with the UDRs.
2. Explain NSG vs ASG vs Azure Firewall in one breath each.
3. Explain why an App Service can't reach a private SQL endpoint — all five checks.
4. Choose LB vs App Gateway vs Front Door vs Traffic Manager for four scenarios.
5. Explain the five Azure storage redundancy options with a use case each.
6. Explain RBAC vs Policy vs Entra ID in three sentences.
7. Explain Backup vs ASR vs failover groups vs Cosmos DB multi-region.
8. Give the four DR strategies with RTO/RPO/cost.
9. List the checks for "VMSS not scaling" and "AKS pods Pending".
10. Describe how you would prove a Region failover works.

## 12.5 Command cheat sheet — troubleshooting with az CLI

| Question you are answering | Command | What "good" looks like |
| --- | --- | --- |
| Which identity/tenant am I? | `az account show` + `az ad signed-in-user show` | Correct subscription, expected tenant |
| Is the resource actually healthy? | `az resource show --ids <id> --query properties.provisioningState` | `Succeeded` (and `Resource Health` = Available) |
| Who changed it? | `az monitor activity-log list --resource-id <id> --offset 24h` | An entry naming the caller, operation and timestamp |
| Is the VM reachable? | `az vm get-instance-view` → statuses · `az network watcher test-connectivity` | `PowerState/running` + `ProvisioningState/succeeded`; connectivity `Reachable` |
| Which rule blocks traffic? | `az network watcher test-ip-flow` (or `show-effective-nsg`) | `Access: Allow`; a deny result names the **NSG rule name** |
| Which route is used? | `az network nic show-effective-route-table -n <nic> -g <rg>` | The expected next hop (VirtualAppliance/Firewall), not `Internet` by accident |
| Does the name resolve privately? | `nslookup <svc>.database.windows.net` (from inside the VNet) | The **private endpoint IP**, not a public address |
| Is the private endpoint approved? | `az network private-endpoint show --query 'privateLinkServiceConnections[].privateLinkServiceConnectionState'` | `status: Approved` |
| Why is App Gateway returning 502? | `az network application-gateway show-backend-health` | `Healthy`; otherwise health, host header, port and TLS details |
| Why is a VMSS not scaling? | `az monitor autoscale show` + `az vmss list-instances` + `az vm list-usage -l <region>` | Rules enabled, instance count < max, vCPU quota headroom |
| Are pods schedulable? | `kubectl describe pod` → Events · `kubectl describe node` → Allocatable | `Scheduled`; `FailedScheduling` names the constraint or subnet IP exhaustion |
| Can the app reach Key Vault? | `az keyvault secret show --vault-name <kv> --name <s>` + Key Vault `AuditEvent` logs | Secret returned; audit shows `SecretGet` success from the identity |
| Is storage reachable privately? | `nslookup <acct>.blob.core.windows.net` + `az storage account show --query publicNetworkAccess` | Private IP returned, `publicNetworkAccess: Disabled` |
| What did the policy block? | `az policy state list --resource <id>` + deny message in the deployment error | `Compliant`; a deny names the policy assignment |
| Is monitoring actually collected? | `az monitor diagnostic-settings list --resource <id>` · Log Analytics `Heartbeat`/`Perf` | A diagnostic setting exists and tables have recent rows |
| Can I recover the VM? | `az backup recoverypoint list` + `az backup restore restore-disks` | A recovery point within your RPO, restore job `Completed` |
| Will DR work? | `az site-recovery job list` + a **test failover** into an isolated VNet | Replication healthy and a measured, successful test failover |
| What is costing money? | `az consumption usage list` / Cost Management by resource and tag | Top resources attributed to an owner tag |


> **Verification note:** re-check current SKUs, quotas, region/support matrices and pricing in Microsoft Learn and the Azure portal before interviews or production design. Services such as Azure Managed Redis, AKS Automatic, Deployment Stacks, network security perimeter, Fabric and Defender plans evolve quickly; preview features carry no SLA.

---

**Sources to keep open:** Microsoft Learn (Azure Architecture Center, Well-Architected, Cloud Adoption Framework) · Azure Updates · Azure pricing calculator · Azure SLA summary · Azure Policy built-ins · `az` CLI reference.
