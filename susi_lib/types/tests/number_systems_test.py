import unittest
from susi_lib.types import NumberSystems


class NumberSystemsCase(unittest.TestCase):
    def setUp(self):
        self.a = NumberSystems('a')
        self.meno = NumberSystems("meno")
        self.meno_mesto = NumberSystems("meno mesto")
        self.a_b = NumberSystems('a', 2)
        self.meno_b = NumberSystems("meno", 2)
        self.meno_mesto_b = NumberSystems("meno mesto", 2)
        self.a_h = NumberSystems('a', 16)
        self.meno_h = NumberSystems("meno", 16)
        self.meno_mesto_h = NumberSystems("meno mesto", 16)

    def test_construct(self):
        with self.assertRaises(TypeError):
            NumberSystems(10)

        with self.assertRaises(ValueError):
            NumberSystems("a8951 78 |")

    def test_to_string(self):
        self.assertEqual(str(self.a), '1')
        self.assertEqual(str(self.meno), ", ".join((str(x) for x in (13, 5, 14, 15))))
        self.assertEqual(str(self.meno_mesto), ", ".join((str(x) for x in (13, 5, 14, 15, 13, 5, 19, 20, 15))))
        self.assertEqual(str(self.a_b), format(1, "05b"))
        self.assertEqual(str(self.meno_b), ", ".join((format(x, "05b") for x in (13, 5, 14, 15))))
        self.assertEqual(str(self.meno_mesto_b), ", ".join((format(x, "05b") for x in (13, 5, 14, 15, 13, 5, 19, 20, 15))))
        self.assertEqual(str(self.a_h), format(1, 'x'))
        self.assertEqual(str(self.meno_h), ", ".join((format(x, 'x') for x in (13, 5, 14, 15))))
        self.assertEqual(str(self.meno_mesto_h),
                         ", ".join((format(x, 'x') for x in (13, 5, 14, 15, 13, 5, 19, 20, 15))))

    def test_add(self):
        self.assertEqual(self.a + self.a, NumberSystems("aa"))
        self.assertEqual(self.a + self.a_h, NumberSystems("aa"))
        with self.assertRaises(TypeError):
            x = self.a + 10


if __name__ == '__main__':
    unittest.main()
