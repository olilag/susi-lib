import unittest
from susi_lib.types.braille import Braille


class BrailleTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Braille('a')
        self.b = Braille('b')
        self.meno = Braille("meno")

    def test_to_string(self):
        self.assertEqual(str(self.a), '⠁')
        self.assertEqual(str(self.b), '⠃')

    def test_get_points(self):
        self.assertEqual(self.a[0].get_points(), (True, False, False, False, False, False))
        self.assertEqual(self.b[0].get_points(), (True, True, False, False, False, False))
        self.assertEqual(self.meno[0].get_points(), (True, False, True, True, False, False))
        self.assertEqual(self.meno[1].get_points(), (True, False, False, False, True, False))
        self.assertEqual(self.meno[2].get_points(), (True, False, True, True, True, False))
        self.assertEqual(self.meno[3].get_points(), (True, False, True, False, True, False))


if __name__ == '__main__':
    unittest.main()