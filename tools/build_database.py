"""Rebuild the portable search index from canonical Markdown and JSONL."""
from pathlib import Path
from contextlib import closing
import json
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'database' / 'knowledge.sqlite'

def document_paths(root=ROOT):
    """Index only reviewed public documents, including in a non-Git export."""
    names = json.loads((root / 'database/documents.json').read_text(encoding='utf-8'))
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError('documents.json must be a list of relative Markdown paths')
    if names != sorted(set(names)):
        raise ValueError('documents.json must be sorted with no duplicate paths')
    paths = []
    for name in names:
        path = (root / name).resolve()
        relative = path.relative_to(root.resolve())
        if relative.as_posix() != name or path.suffix != '.md' or not path.is_file():
            raise ValueError(f'Invalid public document path: {name}')
        paths.append(path)
    return paths

def build():
    documents = document_paths()
    with closing(sqlite3.connect(DB)) as db:
        db.executescript('''
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS lessons;
        CREATE TABLE documents(path TEXT PRIMARY KEY, content TEXT NOT NULL);
        CREATE TABLE lessons(id TEXT PRIMARY KEY, topic TEXT NOT NULL,
          status TEXT NOT NULL, statement TEXT NOT NULL, details TEXT NOT NULL);
        PRAGMA user_version=1;
        ''')
        for path in documents:
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
