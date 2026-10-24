import json, re, collections
qs=json.load(open("/home/user/work/unique_questions.json"))

def L(s): return s.lower()

DEPRECATED = [
 "classic load balancer","simple workflow","amazon swf"," swf ","data pipeline","reduced redundancy",
 "simpledb","cloudsearch","elastic transcoder","opsworks","mechanical turk","amazon machine learning",
 "m1.small","m1.large","m1.medium","c1.","cc2","cr1.","hs1.","t1.micro","m3 ","c3 ","compute-optimized c3",
 "general purpose m3","storage-optimized 12","premium support","support plan","technical account manager",
 "aws import/export","snowmobile","s3-based ami","s3 based ami","instance store-backed ami",
 "elastic ip addresses are free","aws cloudformation designer","amazon cloudfront streaming",
 "rrs","standard - infrequent","vm import","aws oem","glacier vault lock policy editor",
]
UI_WORDS = ["click","clicksave","wizard","check mark","checkmark","dropdown","drop-down","navigate to",
            "management console and select","console and click","tick the","radio button","left pane","menu"]
TF_OPT = {"correct","incorrect","true","false","yes","no"}
MC_META = ["all of the above","none of the above","a and b","a and c","b and c","a, b and c","a, b, and c",
           "b and d","a and d","only through","both a and b","all of these","none of these",
           "1 and 2","2 and 3","1, 2 and 3","statement 1","option a","option b"]

def reason(q):
    ql=L(q["q"]); opts=[L(o["text"]).strip() for o in q["opts"]]; blob=ql+" "+" ".join(opts)
    if sum(1 for o in opts if o in TF_OPT)>=2: return "true-false / correct-incorrect format"
    if "state whether" in ql or "holds true or false" in ql or "true or false" in ql: return "true/false format"
    if any(any(m==o or o.startswith(m) for m in MC_META) for o in opts): return "all-of-the-above / letter-combination options"
    if re.search(r"^\s*[a-d]\)\s", q["q"]) or re.search(r"\n[a-d]\)\s", q["q"]): return "lettered sub-list format"
    for d in DEPRECATED:
        if d in blob: return f"deprecated/retired topic ({d.strip()})"
    if any(u in blob for u in UI_WORDS): return "console click-step question"
    if re.search(r"how many .*(nodes|can you (add|create|have))", ql): return "service-limit trivia (limits have changed)"
    if re.search(r"(what is the (maximum|minimum|default) (number|size|limit))", ql) and "s3" not in ql: return "hard-limit trivia"
    if re.search(r"\b(which|what) (is|are) the (four|three|two|five) ", ql): return "enumeration trivia"
    if re.search(r"^(where do you|what is the name of|which of the following best describes|what does .* stand for)", ql): return "definition trivia"
    if len(q["opts"])<3: return "fewer than 3 options"
    if q["n_correct"]==0: return "no correct answer captured"
    if len(ql.split())<8 and not any(w in ql for w in ["s3","ec2","rds","vpc","iam","kms","sqs","sns","dynamodb"]):
        return "too short / non-scenario trivia"
    return None

keep=[]; drop=[]
for q in qs:
    r=reason(q)
    if r: q["drop_reason"]=r; drop.append(q)
    else: keep.append(q)

print(f"kept {len(keep)}   dropped {len(drop)}")
print("\ndrop reasons:")
for r,c in collections.Counter(d["drop_reason"] for d in drop).most_common():
    print(f"  {c:4d}  {r}")
print("\n--- sample dropped ---")
for d in drop[:6]:
    print(f"  [{d['drop_reason']}] {d['q'][:95]}")
print("\n--- kept per task ---")
c=collections.Counter(q["task_id"] for q in keep)
for t in ["1.1","1.2","1.3","2.1","2.2","3.1","3.2","3.3","3.4","3.5","4.1","4.2","4.3","4.4"]:
    m=sum(1 for q in keep if q["task_id"]==t and q["type"]=="MSQ")
    print(f"  {t}: {c[t]:4d}  (MCQ {c[t]-m:3d} / MSQ {m:3d})")
json.dump(keep, open("/home/user/work/kept.json","w"), indent=1)
json.dump(drop, open("/home/user/work/dropped.json","w"), indent=1)
