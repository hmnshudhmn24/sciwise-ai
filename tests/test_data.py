from src.data.data_loader import load_jsonl
import json, tempfile

def test_load_jsonl(tmp_path):
    p = tmp_path / 'test.jsonl'
    data = {"id":"1","text":"hello"}
    p.write_text(json.dumps(data)+'\n')
    ds = load_jsonl(str(p))
    assert len(ds) == 1
