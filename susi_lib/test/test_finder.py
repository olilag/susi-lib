import unittest
from susi_lib.finder import *
from susi_lib.functions import is_palindrome


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.text = "Lorem ipsum lolol sit amet".split(" ")
        self.f1 = is_palindrome
        self.f2 = lambda word: len(word) == 5

    def test_find_first(self):
        finder = Finder(self.text, self.f2)
        self.assertEqual(finder.find_first(), "Lorem")

    def test_find_all(self):
        finder = Finder(self.text, self.f2)
        self.assertEqual(finder.find_all(), ["Lorem", "ipsum", "lolol"])

    def test_modify_function(self):
        finder = Finder(self.text, self.f2)
        finder.change_function(self.f1)
        self.assertEqual(finder.find_first(), "lolol")
        self.assertEqual(finder.find_all(), ["lolol"])
        finder.add_function(self.f2)
        self.assertEqual(finder.find_first(), "lolol")
        self.assertEqual(finder.find_all(), ["lolol"])
        finder.add_function(lambda word: False)
        self.assertEqual(finder.find_first(), None)
        self.assertEqual(finder.find_all(), [])

    def test_iterate(self):
        finder = Finder(self.text, self.f2)
        for found, exp in zip(finder, ["Lorem", "ipsum", "lolol"]):
            self.assertEqual(found, exp)


if __name__ == "__main__":
    unittest.main()
