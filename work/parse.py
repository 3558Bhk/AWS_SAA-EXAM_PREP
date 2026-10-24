import pymupdf, glob, os, re, json, collections

def is_pua(s):
    s=s.strip()
    return bool(s) and all(0xE000<=ord(c)<=0xF8FF for c in s)

def parse_pdf(path):
    doc=pymupdf.open(path); items=[]
    for pi,pg in enumerate(doc):
        rows=[]
        for b in pg.get_text("dict")["blocks"]:
            if b["type"]!=0: continue
            for l in b["lines"]:
                t="".join(s["text"] for s in l["spans"]).strip()
                if not t: continue
                rows.append({"y":round(l["bbox"][1],2),"x":round(l["bbox"][0],2),"t":t,"mark":is_pua(t),"p":pi})
        rows.sort(key=lambda r:(r["y"],r["x"]))
        items+=rows

    nxt=collections.Counter()
    for i,r in enumerate(items):
        if not r["mark"]: continue
        for j in range(i+1,min(i+3,len(items))):
            if not items[j]["mark"]: nxt[items[j]["x"]]+=1; break
    OPTX = nxt.most_common(1)[0][0] if nxt else 80.2
    def isopt(r): return abs(r["x"]-OPTX)<2.0

    qs=[];cur=None;curopt=None;mode=None;pend=None
    for r in items:
        t=r["t"]
        if r["mark"]: pend=t; continue
        if re.match(r"^Q\d+\s*\)",t):
            if cur: qs.append(cur)
            cur={"src":os.path.basename(path),"qno":int(re.match(r"^Q(\d+)",t).group(1)),
                 "q":re.sub(r"^Q\d+\s*\)\s*","",t),"opts":[]}
            curopt=None;mode="q";pend=None;continue
        if cur is None: continue
        if pend is not None and isopt(r):
            curopt={"text":t,"cp":pend,"expl":""}; cur["opts"].append(curopt)
            mode="otext"; pend=None; continue
        pend=None
        if mode=="q":
            cur["q"]+=" "+t
        elif curopt is not None:
            if re.match(r"^Explanation\s*:-",t):
                mode="expl"
                curopt["expl"]=re.sub(r"^Explanation\s*:-\s*","",t)
            elif mode=="expl":
                curopt["expl"]+=" "+t
            else:
                curopt["text"]+=" "+t
    if cur: qs.append(cur)

    # ---- which codepoint means "selected/correct"? validate against "(choose N)" ----
    cps=sorted({o["cp"] for q in qs for o in q["opts"]})
    def nwanted(txt):
        m=re.search(r"\((?:choose|select)\s+(\d+|two|three|four)\b",txt,re.I)
        if not m: return None
        w=m.group(1).lower()
        return {"two":2,"three":3,"four":4}.get(w, int(w) if w.isdigit() else None)
    def cp_score(cp):
        sc=0
        for q in qs:
            n=nwanted(q["q"]); k=sum(1 for o in q["opts"] if o["cp"]==cp)
            if n is not None:
                sc += 3 if k==n else -2
            else:
                sc += 2 if k==1 else (0 if k==2 else -2)
        return sc
    correct_cp = max(cps, key=cp_score) if cps else None

    for q in qs:
        for o in q["opts"]:
            o["correct"]=(o.pop("cp")==correct_cp)
            o["expl"]=o["expl"].strip()
            o["text"]=re.sub(r"\s+"," ",o["text"]).strip()
        q["q"]=re.sub(r"\s+"," ",q["q"]).strip()
    return qs, correct_cp

allq=[]
for f in sorted(glob.glob("/home/user/uploads/*.pdf")):
    qs,cp=parse_pdf(f)
    nc=collections.Counter(sum(1 for o in q["opts"] if o["correct"]) for q in qs)
    avglen=sum(len(o["text"]) for q in qs for o in q["opts"])/max(1,sum(len(q["opts"]) for q in qs))
    print(f"{len(qs):4d}q cp=U+{ord(cp):04X} avgOptLen={avglen:5.1f} ncorrect={dict(sorted(nc.items()))} {os.path.basename(f)[-26:]}")
    allq+=qs
json.dump(allq,open("/home/user/work/raw_questions.json","w"),indent=1)
print("TOTAL",len(allq))
