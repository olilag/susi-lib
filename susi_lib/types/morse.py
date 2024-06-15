from typing import List, Union


class Morse:
    __dot = '.'
    __dash = '-'
    __symbol_separator = '/'
    __word_separator = '⫽'
    __symbol_dict = {
        'a': __dot + __dash,
        'b': __dash + __dot + __dot + __dot,
        'c': __dash + __dot + __dash + __dot,
        'd': __dash + __dot + __dot,
        'e': __dot,
        'f': __dot + __dot + __dash + __dot,
        'g': __dash + __dash + __dot,
        'h': __dot + __dot + __dot + __dot,
        'i': __dot + __dot,
        'j': __dot + __dash + __dash + __dash,
        'k': __dash + __dot + __dash,
        'l': __dot + __dash + __dot + __dot,
        'm': __dash + __dash,
        'n': __dash + __dot,
        'o': __dash + __dash + __dash,
        'p': __dot + __dash + __dash + __dot,
        'q': __dash + __dash + __dot + __dash,
        'r': __dot + __dash + __dot,
        's': __dot + __dot + __dot,
        't': __dash,
        'u': __dot + __dot + __dash,
        'v': __dot + __dot + __dot + __dash,
        'w': __dot + __dash + __dash,
        'x': __dash + __dot + __dot + __dash,
        'y': __dash + __dot + __dash + __dash,
        'z': __dash + __dash + __dot + __dot,
        ' ': __word_separator,
        '': __symbol_separator
    }
    __symbol_dict_rev = {(v, k) for k, v in __symbol_dict.items()}

    def __init__(self, character: str):
        if not character.isalpha() and character != ' ' and len(character) > 1:
            raise ValueError("Character is not part of alphabet")
        self.__character = character
        self.dots = self.__symbol_dict[self.__character].count(self.__dot)
        self.dashes = self.__symbol_dict[self.__character].count(self.__dash)

    def __str__(self):
        return self.__symbol_dict[self.__character]

    def __eq__(self, other):
        return self.__character == other.__character

    def __add__(self, other):
        if self.__character in {'', ' '}:
            return other
        if isinstance(other, Morse):
            if other.__character not in {' ', ''}:
                return MorseSequence(init=[self, Morse(''), other])
            return MorseSequence(init=[self, other])
        if isinstance(other, MorseSequence):
            return (self + Morse('')) + other
        raise TypeError("Can't add these types")

    def __len__(self):
        if self.__character in {'', ' '}:
            return 0
        return len(self.__symbol_dict[self.__character])


class MorseSequence:
    def __init__(self, text="", init=None):
        if init is None:
            init = []
        self.__seq: List[Morse] = []
        if len(text) != 0:
            first = True
            for c in text:
                if first and c == ' ':
                    continue
                if first and c != ' ':
                    self.__seq.append(Morse(c))
                    first = False
                    continue
                if not first and c != ' ' and self.__seq[-1] not in (Morse(' '), Morse('')):
                    self.__seq.append(Morse(''))
                if c != ' ' or self.__seq[-1] not in (Morse(' '), Morse('')):
                    self.__seq.append(Morse(c))
            return
        self.__seq = init

    def __str__(self):
        return ''.join([str(x) for x in self.__seq])

    def __add__(self, other: Union["MorseSequence", Morse]):
        if isinstance(other, MorseSequence):
            if self.__seq[-1] not in (Morse(' '), Morse('')):
                self.__seq += Morse('') + other.__seq
            else:
                self.__seq += other.__seq
            return self

        if isinstance(other, Morse):
            if self.__seq[-1] not in (Morse(' '), Morse('')):
                self.__seq += [Morse(''), other]
            else:
                self.__seq.append(other)
            return self
        raise TypeError("Can't add these types")

    def __len__(self):
        return sum((1 if m not in (Morse(''), Morse(' ')) else 0 for m in self.__seq))
