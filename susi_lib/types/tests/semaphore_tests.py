import unittest
from susi_lib.types.semaphore import Semaphore


class SemaphoreTestCase(unittest.TestCase):
    def setUp(self):
        self.__left = '\u2190'
        self.__up = '\u2191'
        self.__right = '\u2192'
        self.__down = '\u2193'
        self.__left_up = '\u2196'
        self.__right_up = '\u2197'
        self.__right_down = '\u2198'
        self.__left_down = '\u2199'
        self.a = Semaphore('a')
        self.ab = Semaphore("ab")
        self.meno_mesto = Semaphore("meno mesto")

    def test_to_string(self):
        self.assertEqual(str(self.a), '(' + self.__left_down + self.__down + ')')
        self.assertEqual(str(self.ab), '(' + self.__left_down + self.__down + ")(" + self.__left + self.__down + ')')
        m = '(' + self.__left_down + self.__right + ')'
        e = '(' + self.__down + self.__right_up + ')'
        s = '(' + self.__left + self.__right_down + ')'
        t = '(' + self.__left_up + self.__up + ')'
        o = '(' + self.__left + self.__left_up + ')'
        n = '(' + self.__left_down + self.__right_down + ')'
        self.assertEqual(str(self.meno_mesto), m+e+n+o+' '+m+e+s+t+o)

    def test_directions(self):
        self.assertEqual(self.a[0].get_directions(), (2, 1))
        self.assertEqual(self.ab[1].get_directions(), (3, 1))
        self.assertEqual(self.ab[2].get_directions(), (1, 1))

if __name__ == '__main__':
    unittest.main()
