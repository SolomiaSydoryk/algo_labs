import unittest

from src.main import rabin_karp


class TestRabinKarp(unittest.TestCase):

    def test_single_occurrence(self):
        haystack = "kkkkabckkkk"
        needle = "abc"
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [4])

    def test_multiple_occurrences(self):
        haystack = "abcabcabc"
        needle = "abc"
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [0, 3, 6])

    def test_no_occurrence(self):
        haystack = "abcdefg"
        needle = "io"
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_needle(self):
        haystack = "abc"
        needle = ""
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "abc"
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [])

    def test_both_empty(self):
        haystack = ""
        needle = ""
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
