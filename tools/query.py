"""Simple portable search, with no optional SQLite extensions required."""
from pathlib import Path
import sqlite3
import sys

root = Path(__file__).resolve().parents[1]
if len(sys.argv) < 2:
    raise SystemExit('Usage: python tools/query.py SEARCH TERMS')
term = ' '.join(sys.argv[1:])
with sqlite3.connect((root / 'database/knowledge.sqlite').as_uri() + '?mode=ro', uri=True) as db:
    for ident, topic, status, statement in db.execute(
        'SELECT id,topic,status,statement FROM lessons WHERE instr(lower(details),lower(?)) > 0', (term,)):
        print(f'{ident} [{topic}; {status}] {statement}')
    print('\nDocuments:')
    for path, in db.execute('SELECT path FROM documents WHERE instr(lower(content),lower(?)) > 0', (term,)):
        print(path)
