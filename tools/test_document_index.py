"""Public index boundaries, using a disposable source export without Git."""
import json
from contextlib import closing
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest

from build_database import document_paths


class DocumentIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'database').mkdir()
        (self.root / 'tools').mkdir()
        (self.root / 'approved.md').write_text('Reviewed public guide.', encoding='utf-8')
        (self.root / 'private.md').write_text('PRIVATE_SENTINEL', encoding='utf-8')
        self.manifest = self.root / 'database/documents.json'
        self.manifest.write_text('["approved.md"]', encoding='utf-8')

    def test_export_build_indexes_only_approved_documents(self):
        shutil.copy2(Path(__file__).with_name('build_database.py'), self.root / 'tools/build_database.py')
        lesson = {'id': 'fixture', 'topic': 'test', 'status': 'verified-local', 'statement': 'fixture'}
        (self.root / 'database/lessons.jsonl').write_text(json.dumps(lesson)+'\n', encoding='utf-8')
        subprocess.run([sys.executable, str(self.root / 'tools/build_database.py')],
                       check=True, capture_output=True)
        with closing(sqlite3.connect(self.root / 'database/knowledge.sqlite')) as db:
            self.assertEqual(db.execute('SELECT path,content FROM documents').fetchall(),
                             [('approved.md', 'Reviewed public guide.')])

    def test_rejects_invalid_manifest_boundaries(self):
        for names in (['approved.md', 'approved.md'], ['../outside.md'], ['missing.md'],
                      ['database/documents.json'], ['./approved.md'], {'approved.md': True}):
            with self.subTest(names=names):
                self.manifest.write_text(json.dumps(names), encoding='utf-8')
                with self.assertRaises(ValueError):
                    document_paths(self.root)


if __name__ == '__main__':
    unittest.main()
