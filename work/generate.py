import json, re, random, os, collections
ROOT="/home/user/AWS Certified Solutions Architect - Associate (SAA-C03)"
qs=json.load(open("/home/user/work/ranked.json"))

TASKMAP={
 "1.1":("Domain 1 - Design Secure Architectures (30%)","Task 1.1 - Design Secure Access to AWS Resources"),
 "1.2":("Domain 1 - Design Secure Architectures (30%)","Task 1.2 - Design Secure Workloads and Applications"),
 "1.3":("Domain 1 - Design Secure Architectures (30%)","Task 1.3 - Determine Appropriate Data Security Controls"),
 "2.1":("Domain 2 - Design Resilient Architectures (26%)","Task 2.1 - Design Scalable and Loosely Coupled Architectures"),
 "2.2":("Domain 2 - Design Resilient Architectures (26%)","Task 2.2 - Design Highly Available and Fault-Tolerant Architectures"),
 "3.1":("Domain 3 - Design High-Performing Architectures (24%)","Task 3.1 - High-Performing and Scalable Storage"),
 "3.2":("Domain 3 - Design High-Performing Architectures (24%)","Task 3.2 - High-Performing and Elastic Compute"),
 "3.3":("Domain 3 - Design High-Performing Architectures (24%)","Task 3.3 - High-Performing Database Solutions"),
 "3.4":("Domain 3 - Design High-Performing Architectures (24%)","Task 3.4 - High-Performing and Scalable Networks"),
 "3.5":("Domain 3 - Design High-Performing Architectures (24%)","Task 3.5 - High-Performing Data Ingestion and Transformation"),
 "4.1":("Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.1 - Cost-Optimized Storage"),
 "4.2":("Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.2 - Cost-Optimized Compute"),
 "4.3":("Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.3 - Cost-Optimized Databases"),
 "4.4":("Domain 4 - Design Cost-Optimized Architectures (20%)","Task 4.4 - Cost-Optimized Networks"),
}
LET="ABCDEFGH"

def clean(t):
    t=re.sub(r"\s+"," ",t).strip()
    t=re.sub(r"\s*\((choose|select)\s+\d+( answers?)?\)\s*$","",t,flags=re.I)
    t=re.sub(r"\s*\((choose|select)\s+(two|three|four)( answers?)?\)\s*$","",t,flags=re.I)
    t=t.replace("–","-").replace("—","-")
    return t.strip()

def fix_expl(q):
    ex=[o["expl"] for o in q["opts"] if o["correct"] and o["expl"]]
    seen=[];out=[]
    for e in ex:
        k=e[:60]
        if k not in seen: seen.append(k); out.append(e)
    return " ".join(out).strip()

by={}
for q in qs: by.setdefault(q["task_id"],[]).append(q)

rng=random.Random(42)
summary=[]
for tid,(dom,task) in TASKMAP.items():
    items=by.get(tid,[])
    for q in items:
        q["q_clean"]=clean(q["q"])
        o=q["opts"][:]; rng.shuffle(o); q["opts_s"]=o
    def order(arr):
        g={}
        for q in arr: g.setdefault(q["topic"],[]).append(q)
        tord=sorted(g, key=lambda t:(min(x["rank"] for x in g[t]), -len(g[t]), t))
        out=[]
        for t in tord:
            out+=sorted(g[t], key=lambda q:-q["score"])
        return out
    mcq=order([q for q in items if q["type"]=="MCQ"])
    msq=order([q for q in items if q["type"]=="MSQ"])
    d=os.path.join(ROOT,dom,task)
    os.makedirs(d,exist_ok=True)
    L=[]
    L.append(f"# {task} - Practice Questions\n")
    L.append(f"> **{dom}**  \n> Curated from 18 practice sets: duplicates removed, outdated items retired, "
             f"ordered **highest-frequency exam topics first**.  \n"
             f"> **{len(mcq)} multiple-choice (single answer)** followed by **{len(msq)} multiple-response (select 2+)**. "
             f"Total **{len(mcq)+len(msq)}**.\n")
    if not items:
        L.append("\n> _Questions for this task are being authored in the next batch._\n")
        open(os.path.join(d,"practicequestions.md"),"w").write("\n".join(L)); 
        summary.append((tid,task,0,0)); continue
    # topic order listing
    tp=[]
    for q in mcq+msq:
        if q["topic"] not in tp: tp.append(q["topic"])
    L.append("\n**Topic order in this file:** " + " → ".join(tp) + "\n")
    L.append("\n---\n")
    n=0; key=[]
    for sect,arr in (("A",mcq),("B",msq)):
        if not arr: continue
        if sect=="A":
            L.append("\n# Section A - Multiple Choice (one correct answer)\n")
        else:
            L.append("\n# Section B - Multiple Response (select all that apply)\n")
        cur=None
        for q in arr:
            n+=1
            if q["topic"]!=cur:
                cur=q["topic"]
                L.append(f"\n## {cur}\n")
            nc=sum(1 for o in q["opts_s"] if o["correct"])
            suffix=f" **(Select {nc}.)**" if nc>1 else ""
            L.append(f"\n**Q{n}.** {q['q_clean']}{suffix}\n")
            for i,o in enumerate(q["opts_s"]):
                L.append(f"- **{LET[i]}.** {re.sub(chr(32)+chr(43),chr(32),o['text']).strip()}")
            ans="".join(LET[i] for i,o in enumerate(q["opts_s"]) if o["correct"])
            wrongs=[(LET[i],o["expl"]) for i,o in enumerate(q["opts_s"]) if not o["correct"] and o["expl"]]
            key.append((n,", ".join(ans), fix_expl(q), q["topic"], wrongs))
            L.append("")
    L.append("\n---\n")
    L.append("\n# Answer Key & Explanations\n")
    for n_,a,e,tp_,wr in key:
        L.append(f"\n**Q{n_}. {a}**  ")
        L.append(f"_{tp_}_  ")
        L.append(e if e else "_See the matching section of this task's `notes.md` for the underlying concept._")
        for lt,w in wr:
            L.append(f"- *Why not {lt}:* {w}")
    open(os.path.join(d,"practicequestions.md"),"w").write("\n".join(L)+"\n")
    summary.append((tid,task,len(mcq),len(msq)))

print(f"{'task':6} {'MCQ':>4} {'MSQ':>4} {'tot':>4}")
tm=tn=0
for tid,task,a,b in summary:
    tm+=a; tn+=b
    print(f"{tid:6} {a:4d} {b:4d} {a+b:4d}  {task[:46]}")
print(f"{'TOTAL':6} {tm:4d} {tn:4d} {tm+tn:4d}")
