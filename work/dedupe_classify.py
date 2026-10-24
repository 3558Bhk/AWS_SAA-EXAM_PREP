import json, re, collections

qs = json.load(open("/home/user/work/raw_questions.json"))

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

STOP=set("the a an of to in for and or is are be with on at as by from that this which what you your we our their it its will would can should must not no any".split())
def toks(s): return {w for w in norm(s).split() if w not in STOP and len(w)>2}

for i,q in enumerate(qs):
    q["id"]=i
    q["n_correct"]=sum(1 for o in q["opts"] if o["correct"])
    q["type"]="MSQ" if q["n_correct"]>1 else "MCQ"
    q["_t"]=toks(q["q"])
    q["_key"]=norm(q["q"])[:160]

# ---- dedupe: exact-prefix bucket + jaccard on question tokens ----
qs.sort(key=lambda q:(-len(q["opts"]), -sum(len(o["expl"]) for o in q["opts"])))
kept=[]; dup=0
buckets=collections.defaultdict(list)
def sig(q):
    t=sorted(q["_t"])
    return tuple(t[:4])
for q in qs:
    cands=[]
    for k in range(len(sorted(q["_t"])[:6])):
        cands+=buckets[sorted(q["_t"])[k] if k<len(q["_t"]) else ""]
    best=None
    for c in set(cands):
        o=kept[c]
        if not q["_t"] or not o["_t"]: continue
        j=len(q["_t"]&o["_t"])/len(q["_t"]|o["_t"])
        if j>0.80: best=o; break
    if best:
        dup+=1
        best.setdefault("dupes",0)
        best["dupes"]+=1
        best["freq"]=best.get("freq",1)+1
        continue
    idx=len(kept); kept.append(q)
    for w in sorted(q["_t"])[:6]: buckets[w].append(idx)
print("raw:",len(qs),"unique:",len(kept),"dupes removed:",dup)

# ---- classification ----
TASKS = [
 ("1.1","Domain 1 - Design Secure Architectures (30%)","Task 1.1 - Design Secure Access to AWS Resources",
  ["iam","identity and access","policy","policies","role","roles","sts","assume","mfa","root user","access key",
   "federation","federated","saml","identity center","sso","organizations","scp","service control","permission",
   "principal","credential","cognito","directory service","active directory","control tower","trust policy",
   "cross-account","cross account","least privilege","iam user","iam group","resource-based policy","arn",
   "instance profile","access advisor","credential report","account alias","billing access","support plan"]),
 ("1.2","Domain 1 - Design Secure Architectures (30%)","Task 1.2 - Design Secure Workloads and Applications",
  ["security group","network acl","nacl","bastion","subnet","vpc","nat gateway","nat instance","internet gateway",
   "waf","shield","ddos","firewall","guardduty","inspector","macie","flow log","port","ssh","rdp","vpn",
   "direct connect","vpc endpoint","privatelink","peering","session manager","secrets manager","parameter store",
   "penetration","hardening","patch","systems manager","bastion host","egress","ingress","public subnet",
   "private subnet","route table","vpc flow"]),
 ("1.3","Domain 1 - Design Secure Architectures (30%)","Task 1.3 - Determine Appropriate Data Security Controls",
  ["encrypt","encryption","kms","cloudhsm","hsm","key management","certificate","acm","ssl","tls","at rest",
   "in transit","sse","server-side encryption","client-side encryption","envelope","object lock","vault lock",
   "mfa delete","versioning","compliance","hipaa","pci","gdpr","data classification","macie","audit",
   "cloudtrail","artifact","retention","immutable","wormin","governance mode","compliance mode","customer master key","cmk"]),
 ("2.1","Domain 2 - Design Resilient Architectures (26%)","Task 2.1 - Design Scalable and Loosely Coupled Architectures",
  ["sqs","queue","sns","topic","eventbridge","event bus","step functions","state machine","decouple","loosely coupled",
   "fan-out","fanout","message","visibility timeout","dead letter","dlq","long polling","api gateway","lambda",
   "microservice","amazon mq","kinesis","stateless","sticky session","session state","elastic beanstalk",
   "auto scaling","scaling policy","launch configuration","launch template","scale out","scale in","elasticache",
   "load balancer","elb","alb","nlb","target group","swf","simple workflow"]),
 ("2.2","Domain 2 - Design Resilient Architectures (26%)","Task 2.2 - Design Highly Available and Fault-Tolerant Architectures",
  ["high availability","highly available","fault tolerant","fault tolerance","multi-az","multi az","failover",
   "disaster recovery","rto","rpo","pilot light","warm standby","backup","restore","snapshot","standby","replica",
   "route 53","health check","failover routing","availability zone","single point of failure","resilien",
   "cross-region","cross region","global database","durability","recovery","redundan","aurora","read replica",
   "placement group","auto recovery"]),
 ("3.1","Domain 3 - Design High-Performing Architectures (24%)","Task 3.1 - High-Performing and Scalable Storage",
  ["s3","bucket","object","glacier","storage class","standard-ia","one zone","intelligent-tiering","lifecycle",
   "ebs","volume","gp2","gp3","io1","io2","st1","sc1","iops","throughput","instance store","ephemeral",
   "efs","fsx","lustre","file system","nfs","smb","storage gateway","datasync","snowball","snowmobile",
   "multipart","transfer acceleration","presigned","durability","petabyte","block storage","object storage"]),
 ("3.2","Domain 3 - Design High-Performing Architectures (24%)","Task 3.2 - High-Performing and Elastic Compute",
  ["ec2","instance type","instance family","compute optimized","memory optimized","t2","t3","m5","c5","r5",
   "graviton","burstable","cpu credit","lambda","fargate","ecs","eks","container","docker","batch","emr",
   "elastic fabric","placement group","hpc","gpu","spot","dedicated host","ami","user data","hibernat",
   "serverless","concurrency","cold start","vcpu","elastic ip","hypervisor","nitro"]),
 ("3.3","Domain 3 - Design High-Performing Architectures (24%)","Task 3.3 - High-Performing Database Solutions",
  ["rds","aurora","dynamodb","database","mysql","postgres","oracle","sql server","mariadb","redshift",
   "elasticache","redis","memcached","documentdb","neptune","timestream","qldb","keyspaces","dax",
   "read replica","rcu","wcu","provisioned throughput","partition key","sort key","global secondary index",
   "lsi","gsi","query","scan","nosql","opensearch","elasticsearch","data warehouse","oltp","olap","db instance"]),
 ("3.4","Domain 3 - Design High-Performing Architectures (24%)","Task 3.4 - High-Performing and Scalable Networks",
  ["cloudfront","edge location","cdn","global accelerator","route 53","dns","latency-based","geolocation",
   "transit gateway","vpc peering","direct connect","vpn","privatelink","vpc endpoint","bandwidth","latency",
   "network","cidr","ip address","elastic network interface","eni","jumbo frame","enhanced networking",
   "accelerat","anycast","origin","distribution","edge","hosted zone","alias record","cname","ttl"]),
 ("3.5","Domain 3 - Design High-Performing Architectures (24%)","Task 3.5 - High-Performing Data Ingestion and Transformation",
  ["kinesis","firehose","data stream","shard","glue","etl","athena","quicksight","emr","hadoop","spark",
   "data lake","lake formation","parquet","orc","crawler","data catalog","msk","kafka","flink","ingestion",
   "transform","analytics","redshift spectrum","data pipeline","batch processing","streaming","iot core","dms"]),
 ("4.1","Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.1 - Cost-Optimized Storage",
  ["storage cost","cost-effective storage","glacier","deep archive","lifecycle policy","infrequent access",
   "storage class analysis","storage lens","archive","retrieval fee","minimum duration","intelligent-tiering",
   "snapshot cost","unattached volume","cheapest storage","reduce storage"]),
 ("4.2","Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.2 - Cost-Optimized Compute",
  ["reserved instance","savings plan","spot instance","spot fleet","on-demand","dedicated host","pricing",
   "cost optimi","cost-effective","reduce cost","lower cost","cheapest","billing","budget","cost explorer",
   "trusted advisor","compute optimizer","right-siz","rightsiz","idle","underutilized","per-second billing",
   "partial upfront","all upfront","convertible","scheduled reserved"]),
 ("4.3","Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.3 - Cost-Optimized Databases",
  ["database cost","rds reserved","reserved node","dynamodb on-demand","provisioned capacity","capacity mode",
   "reserved capacity","aurora serverless","database pricing","redshift reserved","pause","cost of the database"]),
 ("4.4","Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.4 - Cost-Optimized Networks",
  ["data transfer","transfer cost","egress","bandwidth cost","nat gateway cost","cloudfront cost",
   "data transfer out","cross-az","inter-region","vpc endpoint cost","network cost","price class"]),
]

def classify(q):
    blob = norm(q["q"] + " " + " ".join(o["text"] for o in q["opts"]))
    cost_ctx = any(k in blob for k in ["cost","cheap","price","pricing","budget","billing","expensive","economical","save money"])
    best=None; bestscore=0
    for tid,dom,task,kws in TASKS:
        sc=0
        for k in kws:
            if k in blob:
                sc += 3 if len(k)>12 else (2 if len(k)>6 else 1)
        if tid.startswith("4"):
            sc = sc*2 if cost_ctx else sc*0.3
        if sc>bestscore: bestscore=sc; best=(tid,dom,task)
    if best is None: best=("3.2",TASKS[6][1],TASKS[6][2])
    return best

for q in kept:
    tid,dom,task = classify(q)
    q["task_id"]=tid; q["domain"]=dom; q["task"]=task
    q["freq"]=q.get("freq",1)

cnt=collections.Counter(q["task_id"] for q in kept)
print("\nper-task counts:")
for tid,dom,task,_ in TASKS:
    c=cnt[tid]
    m=sum(1 for q in kept if q["task_id"]==tid and q["type"]=="MSQ")
    print(f"  {tid}  total {c:4d}   MCQ {c-m:4d}   MSQ {m:3d}   {task}")
print("TOTAL unique:",len(kept))

for q in kept: q.pop("_t",None); q.pop("_key",None)
json.dump(kept, open("/home/user/work/unique_questions.json","w"), indent=1)
