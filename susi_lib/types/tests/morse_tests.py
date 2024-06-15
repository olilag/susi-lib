import unittest
from susi_lib.types.morse import Morse, MorseSequence


class MorseTestCase(unittest.TestCase):
    def setUp(self):
        self.dot = Morse._Morse__dot
        self.dash = Morse._Morse__dash
        self.sym_sep = Morse._Morse__symbol_separator
        self.word_sep = Morse._Morse__word_separator
        self.empty = Morse('')
        self.separator = Morse(' ')
        self.a = Morse('a')
        self.a_morse = self.dot + self.dash
        self.x = Morse('x')
        self.x_morse = self.dash + self.dot + self.dot + self.dash
        self.e = Morse('e')
        self.e_morse = self.dot
        self.q = Morse('q')
        self.q_morse = self.dash + self.dash + self.dot + self.dash
        self.r = Morse('r')
        self.r_morse = self.dot + self.dash + self.dot
        self.text = MorseSequence("axerq")
        self.text_morse = self.dot + self.dash + self.sym_sep + \
                          self.dash + self.dot + self.dot + self.dash + self.sym_sep + \
                          self.dot + self.sym_sep + \
                          self.dot + self.dash + self.dot + self.sym_sep + \
                          self.dash + self.dash + self.dot + self.dash
        self.text2 = MorseSequence("axe rq")
        self.text2_morse = self.dot + self.dash + self.sym_sep + \
                          self.dash + self.dot + self.dot + self.dash + self.sym_sep + \
                          self.dot + self.word_sep + \
                          self.dot + self.dash + self.dot + self.sym_sep + \
                          self.dash + self.dash + self.dot + self.dash
        self.text3 = MorseSequence("  axe   rq")
        self.text3_morse = self.dot + self.dash + self.sym_sep + \
                           self.dash + self.dot + self.dot + self.dash + self.sym_sep + \
                           self.dot + self.word_sep + \
                           self.dot + self.dash + self.dot + self.sym_sep + \
                           self.dash + self.dash + self.dot + self.dash

    def test_construct(self):
        self.assertEqual(str(self.empty), self.sym_sep)
        self.assertEqual(str(self.separator), self.word_sep)
        self.assertEqual(str(self.a), self.a_morse)
        self.assertEqual(str(self.x), self.x_morse)
        self.assertEqual(str(self.e), self.e_morse)
        self.assertEqual(str(self.q), self.q_morse)
        self.assertEqual(str(self.r), self.r_morse)
        self.assertEqual(str(self.text), self.text_morse)
        self.assertEqual(str(self.text2), self.text2_morse)
        self.assertEqual(str(self.text3), self.text3_morse)

    def test_add(self):
        ax = self.a + self.x
        self.assertEqual(str(ax), self.a_morse + self.sym_sep + self.x_morse)
        rax = self.r + ax
        self.assertEqual(str(rax), self.r_morse + self.sym_sep + \
                         self.a_morse + self.sym_sep + self.x_morse)
        e_rax = self.empty + rax
        self.assertEqual(str(e_rax), str(rax))
        rax_e = rax + self.empty
        self.assertEqual(str(rax_e), str(rax))
        e_a = self.empty + self.a
        self.assertEqual(str(e_a), self.a_morse)

    def test_length(self):
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(Morse(' ')), 0)
        self.assertEqual(len(self.a), 2)
        self.assertEqual(len(self.e), 1)
        self.assertEqual(len(self.q), 4)
        self.assertEqual(len(self.r), 3)
        self.assertEqual(len(self.text), 5)
        self.assertEqual(len(self.text2), 5)
        self.assertEqual(len(self.text3), 5)


if __name__ == '__main__':
    unittest.main()
