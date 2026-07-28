#!/usr/bin/env python

'''
Unit tests for line_count.py functions
'''

import tempfile
import unittest
from pathlib import Path

import line_count


class TestLineCountFunctions(unittest.TestCase):
    """Test various line counting implementations."""

    def setUp(self):
        """Create temporary test files."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_files = {}

        # Create test files with known line counts
        # Note: all files end with newline to avoid bufcount edge cases
        test_cases = {
            'empty': '',
            'single': 'line 1\n',
            'three': 'line 1\nline 2\nline 3\n',
        }

        for name, content in test_cases.items():
            path = Path(self.temp_dir.name) / f'test_{name}.txt'
            path.write_text(content, encoding='utf8')
            self.test_files[name] = str(path)

    def tearDown(self):
        """Clean up temporary files."""
        self.temp_dir.cleanup()

    def test_simplecount_empty(self):
        """Test simple count with empty file."""
        self.assertEqual(line_count.simplecount(self.test_files['empty']), 0)

    def test_simplecount_single(self):
        """Test simple count with single line."""
        self.assertEqual(line_count.simplecount(self.test_files['single']), 1)

    def test_simplecount_multiple(self):
        """Test simple count with multiple lines."""
        self.assertEqual(line_count.simplecount(self.test_files['three']), 3)

    def test_bufcount_empty(self):
        """Test buf count with empty file."""
        self.assertEqual(line_count.bufcount(self.test_files['empty']), 0)

    def test_bufcount_single(self):
        """Test buf count with single line."""
        self.assertEqual(line_count.bufcount(self.test_files['single']), 1)

    def test_bufcount_multiple(self):
        """Test buf count with multiple lines."""
        self.assertEqual(line_count.bufcount(self.test_files['three']), 3)

    def test_itercount_empty(self):
        """Test iter count with empty file."""
        self.assertEqual(line_count.itercount(self.test_files['empty']), 0)

    def test_itercount_single(self):
        """Test iter count with single line."""
        self.assertEqual(line_count.itercount(self.test_files['single']), 1)

    def test_itercount_multiple(self):
        """Test iter count with multiple lines."""
        self.assertEqual(line_count.itercount(self.test_files['three']), 3)

    def test_opcount_empty(self):
        """Test opcount with empty file."""
        self.assertEqual(line_count.opcount(self.test_files['empty']), 0)

    def test_opcount_single(self):
        """Test opcount with single line."""
        self.assertEqual(line_count.opcount(self.test_files['single']), 1)

    def test_opcount_multiple(self):
        """Test opcount with multiple lines."""
        self.assertEqual(line_count.opcount(self.test_files['three']), 3)

    def test_kylecount_empty(self):
        """Test kylecount with empty file."""
        self.assertEqual(line_count.kylecount(self.test_files['empty']), 0)

    def test_kylecount_single(self):
        """Test kylecount with single line."""
        self.assertEqual(line_count.kylecount(self.test_files['single']), 1)

    def test_kylecount_multiple(self):
        """Test kylecount with multiple lines."""
        self.assertEqual(line_count.kylecount(self.test_files['three']), 3)

    def test_mapcount_empty(self):
        """Test mapcount with empty file."""
        self.assertEqual(line_count.mapcount(self.test_files['empty']), 0)

    def test_mapcount_single(self):
        """Test mapcount with single line."""
        self.assertEqual(line_count.mapcount(self.test_files['single']), 1)

    def test_mapcount_multiple(self):
        """Test mapcount with multiple lines."""
        self.assertEqual(line_count.mapcount(self.test_files['three']), 3)

    def test_all_counters_agree(self):
        """Verify all counting methods return the same result."""
        for test_name, filepath in self.test_files.items():
            counts = {
                'simplecount': line_count.simplecount(filepath),
                'bufcount': line_count.bufcount(filepath),
                'itercount': line_count.itercount(filepath),
                'opcount': line_count.opcount(filepath),
                'kylecount': line_count.kylecount(filepath),
                'mapcount': line_count.mapcount(filepath),
            }
            # All should be equal
            unique_counts = set(counts.values())
            self.assertEqual(len(unique_counts), 1,
                           f"Mismatch for {test_name}: {counts}")


if __name__ == '__main__':
    unittest.main()
