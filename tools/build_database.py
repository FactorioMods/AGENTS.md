"""Rebuild the portable search index from canonical Markdown and JSONL."""
from pathlib import Path
import json
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'database' / 'knowledge.sqlite'

def build():
    with sqlite3.connect(DB) as db:
        db.executescript('''
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS lessons;
        CREATE TABLE documents(path TEXT PRIMARY KEY, content TEXT NOT NULL);
        CREATE TABLE lessons(id TEXT PRIMARY KEY, topic TEXT NOT NULL,
          status TEXT NOT NULL, statement TEXT NOT NULL, details TEXT NOT NULL);
        PRAGMA user_version=1;
        ''')
        for path in sorted(ROOT.rglob('*.md')):
            if '.git' not in path.parts:
                db.execute('INSERT INTO documents VALUES (?,?)',
                           (path.relative_to(ROOT).as_posix(), path.read_text(encoding='utf-8')))
        for line in (ROOT / 'database/lessons.jsonl').read_text(encoding='utf-8').splitlines():
            record = json.loads(line)
            db.execute('INSERT INTO lessons VALUES (?,?,?,?,?)',
                       (record['id'], record['topic'], record['status'],
                        record['statement'], json.dumps(record, ensure_ascii=False)))
        db.commit()
        db.execute('VACUUM')
    print(f'Rebuilt {DB.name}')

if __name__ == '__main__':
    build()
