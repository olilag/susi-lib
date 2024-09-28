# pylint: skip-file
import unittest

from susi_lib.functions import find_anagrams, is_palindrome, unique_letters
from susi_lib.types import Symbols


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("tacocat"), True)
        self.assertEqual(is_palindrome("abc"), False)
        self.assertEqual(is_palindrome([1, 2, 1]), True)
        self.assertEqual(is_palindrome(Symbols("tacocat")), True)

    def test_find_anagrams(self):
        self.word_list = "makrela reklama kamarat abeceda kokos skoko".split(" ")
        self.assertEqual(
            find_anagrams("karamel", self.word_list), ["makrela", "reklama"]
        )
        self.assertEqual(find_anagrams("abc", self.word_list), [])
        self.assertEqual(find_anagrams("kokos", self.word_list), ["skoko"])

        with self.assertRaises(TypeError):
            find_anagrams(1, self.word_list)
        with self.assertRaises(TypeError):
            find_anagrams("kokos", "lol")
        with self.assertRaises(TypeError):
            find_anagrams("kokos", [1, 2, 3])

    def test_unique_letters(self):
        self.assertTrue(unique_letters("abc"))
        self.assertFalse(unique_letters("kokos"))


if __name__ == "__main__":
    unittest.main()
