import unittest
from susi_lib.finder import *
from susi_lib.functions import is_palindrome


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.text = "Lorem ipsum lolol sit amet".split(" ")
        self.f1 = is_palindrome
        self.f2 = lambda word: len(word) == 5

    def test_finder(self):
        finder = Finder(self.text, self.f2)
        self.assertEqual(finder.find_first(), "Lorem")
        self.assertEqual(finder.find_all(), ["Lorem", "ipsum", "lolol"])
        for found, exp in zip(finder, ["Lorem", "ipsum", "lolol"]):
            self.assertEqual(found, exp)
        finder.change_function(self.f1)
        self.assertEqual(finder.find_first(), "lolol")
        self.assertEqual(finder.find_all(), ["lolol"])
        finder.add_function(self.f2)
        self.assertEqual(finder.find_first(), "lolol")
        self.assertEqual(finder.find_all(), ["lolol"])
        finder.add_function(lambda word: False)
        self.assertEqual(finder.find_first(), None)
        self.assertEqual(finder.find_all(), [])



if __name__ == "__main__":
    unittest.main()
