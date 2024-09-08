# pylint: skip-file
import os
import sys
import unittest
from unittest.mock import patch

from susi_lib.regex import create_regex
from susi_lib.word_finder_cli import _translate, _validate_input, main


class TestWordFinder(unittest.TestCase):

    def test_pattern_creation(self):
        tests = [
            (7, ["abc"], r"^[abc]{7}$"),
            ((4, 7), ["abc"], r"^[abc]{4,7}$"),
            (3, "a b c".split(), r"^[a][b][c]$"),
            (4, "a ^bef c-f gag".split(), r"^[a][^bef][c-f][gag]$"),
        ]

        for length, letters, result in tests:
            args, kwargs = _translate(letters, length, [])
            regex = create_regex(*args, **kwargs)
            self.assertEqual(regex.get_pattern(), result)

    def test_input_validation(self):
        tests = [
            ("7", ["abc"], True),
            ("4-7", ["abc"], True),
            (None, "a b c".split(), True),
            ("4", "a ^bef c-f gag".split(), True),
            ("7", "ab c".split(), False),
            ("4-7", "ab c".split(), False),
            (None, ["abc"], True),
            ("4--7", ["abc"], False),
            ("ab-cd", ["abc"], False),
        ]

        for length, letters, result in tests:
            valid, _ = _validate_input(letters, length)
            self.assertEqual(valid, result, f"len: {length}, let: {letters}")

    def test_full_cli(self):
        file_location = os.path.dirname(os.path.realpath(__file__)) + "/lorem.txt"
        correct = [
            f"susi-word-finder abc . . ^a-f .  -w 5 -i {file_location}".split(),
            f"susi-word-finder -w 7 abc -i {file_location}".split(),
            f"susi-word-finder -w 4-7 abc -i {file_location}".split(),
            f"susi-word-finder abc . . ^a-f . -i {file_location}".split(),
        ]

        for args in correct:
            with patch.object(sys, "argv", args):
                main()

        bad_usage = [
            f"susi-word-finder abc . . ^a-f -w 5 -i {file_location}".split(),
            f"susi-word-finder -w 7 ab c -i {file_location}".split(),
            f"susi-word-finder -w 4---7 abc -i {file_location}".split(),
            f"susi-word-finder -w ab-cd abc . . ^a-f . -i {file_location}".split(),
        ]

        for args in bad_usage:
            with patch.object(sys, "argv", args):
                with self.assertRaises(SystemExit):
                    main()
                    unittest.main(exit=False)


if __name__ == "__main__":
    unittest.main()
