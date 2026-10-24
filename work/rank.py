import json, re, collections, sys
sys.path.insert(0,"/home/user/work")
from topics import TOPICS
qs=json.load(open("/home/user/work/kept.json"))
def L(s): return s.lower()
for q in qs:
    blob=L(q["q"]+" "+" ".join(o["text"] for o in q["opts"])+" "+" ".join(o["expl"] for o in q["opts"]))
    best=None;bs=0
    for rank,label,kws in TOPICS:
        sc=sum((3 if len(k)>12 else 2 if len(k)>7 else 1) for k in kws if k in blob)
        sc = sc * (1.0 + (6-rank)*0.12)
        if sc>bs: bs=sc; best=(rank,label)
    q["rank"],q["topic"] = best if best else (5,"General Design")
    q["score"]=round(bs,2)
c=collections.Counter((q["rank"],q["topic"]) for q in qs)
for (r,t),n in sorted(c.items(), key=lambda x:(x[0][0],-x[1])):
    print(f"  tier{r}  {n:4d}  {t}")
json.dump(qs, open("/home/user/work/ranked.json","w"), indent=1)
print("total",len(qs))
