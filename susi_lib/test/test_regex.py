import unittest
from susi_lib.regex import *


class MyTestCase(unittest.TestCase):
    def test_create_regex(self):
        self.assertEqual(
            create_regex(
                ("abc", Selection.NONE), ("def", Selection.INVERT), ("", Selection.ANY)
            ).get_pattern(),
            "^[abc][^def][.]$",
        )
        self.assertEqual(
            create_regex(length=5, letters="auto", invert=False).get_pattern(),
            "^[auto]{5}$",
        )
        self.assertEqual(
            create_regex(length=(5, 10), letters="auto", invert=False).get_pattern(),
            "^[auto]{5,10}$",
        )
        self.assertEqual(
            create_regex(length=5, letters="auto", invert=True).get_pattern(),
            "^[^auto]{5}$",
        )
        with self.assertRaises(ValueError):
            create_regex(("abc", Selection.NONE), ("def"), ("", Selection.ANY))
        with self.assertRaises(ValueError):
            create_regex(
                ("abc", Selection.NONE), ("def", Selection.INVERT), ("", Selection.NONE)
            )

    def test_regex(self):
        pass


if __name__ == "__main__":
    unittest.main()
