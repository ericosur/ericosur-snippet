#!/usr/bin/env python3

"""Unit tests for gngan_yaljux."""

from __future__ import annotations

import unittest

from gngan_yaljux import GanChi, do_nothing, get_thisyear


class TestGanChi(unittest.TestCase):
    """Tests for GanChi core behavior."""

    def setUp(self) -> None:
        self.gc = GanChi(_logd=do_nothing)

    def test_normalize_year_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.gc.normalize_year(0)

    def test_normalize_year_too_old_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.gc.normalize_year(-2998)

    def test_get_reminder_known_year(self) -> None:
        # 1975 is expected to be Yi-Mao in this implementation.
        self.assertEqual(self.gc.get_reminder(1975), (1, 3))

    def test_to_gc_known_year(self) -> None:
        self.assertEqual(self.gc.to_gc(1975), "乙卯(兔)")

    def test_check_ab_valid(self) -> None:
        self.assertTrue(self.gc.check_ab(1, 3, do_nothing))

    def test_check_ab_invalid_parity(self) -> None:
        self.assertFalse(self.gc.check_ab(1, 4, do_nothing))

    def test_check_ab_invalid_range(self) -> None:
        self.assertFalse(self.gc.check_ab(-1, 0, do_nothing))
        self.assertFalse(self.gc.check_ab(0, 12, do_nothing))

    def test_bruteforce_returns_expected_cycle_shape(self) -> None:
        ans = self.gc.brute_force_try(0, 0, _logd=do_nothing)
        self.assertEqual(len(ans), 4)
        self.assertEqual(ans, sorted(ans))

        # Consecutive answers should be exactly one cycle apart.
        for idx in range(1, len(ans)):
            self.assertEqual(ans[idx] - ans[idx - 1], 60)

        # Every returned year should match the requested Gan/Zhi reminder.
        for year in ans:
            self.assertEqual(self.gc.get_reminder(year), (0, 0))

    def test_bruteforce_contains_next_match_in_window(self) -> None:
        ans = self.gc.brute_force_try(1, 3, _logd=do_nothing)
        self.assertTrue(ans)

        this_year = get_thisyear()
        next_match = ans[-1]
        self.assertGreaterEqual(next_match, this_year)
        self.assertLess(next_match, this_year + 60)

    def test_bruteforce_invalid_input_returns_empty(self) -> None:
        self.assertEqual(self.gc.brute_force_try(1, 4, _logd=do_nothing), [])


if __name__ == "__main__":
    unittest.main()
