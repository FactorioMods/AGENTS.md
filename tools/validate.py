"""Validate handoff records, local links, asset hashes and search-index parity."""
from pathlib import Path
import hashlib
import json
import re
import sqlite3

root = Path(__file__).resolve().parents[1]
assert (root / 'AGENTS.md').stat().st_size < 32768
records = [json.loads(s) for s in (root / 'database/lessons.jsonl').read_text(encoding='utf-8').splitlines()]
assert len({r['id'] for r in records}) == len(records)
for record in records:
    assert all(record.get(k) for k in ('id','topic','status','statement','source','verification','date'))
    assert record['status'] in {'verified-local','historical-evidence','user-requirement','open-gap'}
    assert (root / record['source']).is_file(), record
for path in root.rglob('*.json'):
    if '.git' not in path.parts:
        json.loads(path.read_text(encoding='utf-8'))
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            assert (path.parent / target.split('#')[0]).is_file(), (path, target)
for asset in json.loads((root / 'database/assets.json').read_text(encoding='utf-8')):
    path = root / asset['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256'], path
with sqlite3.connect(root / 'database/knowledge.sqlite') as db:
    assert db.execute('SELECT COUNT(*) FROM lessons').fetchone()[0] == len(records)
    for path, text in db.execute('SELECT path,content FROM documents'):
        assert (root / path).read_text(encoding='utf-8') == text, path
print(f'PASS: {len(records)} lessons, JSON, local links, asset hashes, database parity')
