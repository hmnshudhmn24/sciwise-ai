import os, json
from datasets import Dataset

def load_jsonl(path):
    records = []
    if os.path.isdir(path):
        files = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jsonl') or f.endswith('.json')]
    else:
        files = [path]
    for f in files:
        with open(f,'r',encoding='utf-8') as fh:
            for line in fh:
                line=line.strip()
                if not line: continue
                records.append(json.loads(line))
    return Dataset.from_list(records)
