from susi_lib.types import Braille
from susi_lib.types import Morse
from susi_lib.types import NumberSystems
from susi_lib.types import Semaphore
from susi_lib.utils import export


@export
class Symbols:
    __rev_braille = {
        chr(value + 0x2800): key
        for key, value in {
            "a": 0x1,
            "b": 0x3,
            "c": 0x9,
            "d": 0x19,
            "e": 0x11,
            "f": 0xB,
            "g": 0x1B,
            "h": 0x13,
            "i": 0xA,
            "j": 0x1A,
            "k": 0x5,
            "l": 0x7,
            "m": 0xD,
            "n": 0x1D,
            "o": 0x15,
            "p": 0xF,
            "q": 0x1F,
            "r": 0x17,
            "s": 0xE,
            "t": 0x1E,
            "u": 0x25,
            "v": 0x27,
            "w": 0x37,
            "x": 0x2D,
            "y": 0x3D,
            "z": 0x35,
            " ": ord(" ") - 0x2800,
        }.items()
    }

    __left = "\u2190"
    __up = "\u2191"
    __right = "\u2192"
    __down = "\u2193"
    __left_up = "\u2196"
    __right_up = "\u2197"
    __right_down = "\u2198"
    __left_down = "\u2199"
    __directions = [
        __down,
        __left_down,
        __left,
        __left_up,
        __up,
        __right_up,
        __right,
        __right_down,
    ]
    __rev_semaphore = {
        value: key
        for key, value in {
            "a": (2, 1),
            "b": (3, 1),
            "c": (4, 1),
            "d": (5, 1),
            "e": (1, 6),
            "f": (1, 7),
            "g": (1, 8),
            "h": (3, 2),
            "i": (4, 2),
            "j": (5, 7),
            "k": (2, 5),
            "l": (2, 6),
            "m": (2, 7),
            "n": (2, 8),
            "o": (3, 4),
            "p": (3, 5),
            "q": (3, 6),
            "r": (3, 7),
            "s": (3, 8),
            "t": (4, 5),
            "u": (4, 6),
            "v": (5, 6),
            "w": (6, 7),
            "x": (6, 8),
            "y": (4, 7),
            "z": (8, 7),
        }.items()
    }

    __dot = "."
    __dash = "-"
    __symbol_separator = "/"
    __word_separator = "⫽"
    __rev_morse = {
        value: key
        for key, value in {
            "a": __dot + __dash,
            "b": __dash + __dot + __dot + __dot,
            "c": __dash + __dot + __dash + __dot,
            "d": __dash + __dot + __dot,
            "e": __dot,
            "f": __dot + __dot + __dash + __dot,
            "g": __dash + __dash + __dot,
            "h": __dot + __dot + __dot + __dot,
            "i": __dot + __dot,
            "j": __dot + __dash + __dash + __dash,
            "k": __dash + __dot + __dash,
            "l": __dot + __dash + __dot + __dot,
            "m": __dash + __dash,
            "n": __dash + __dot,
            "o": __dash + __dash + __dash,
            "p": __dot + __dash + __dash + __dot,
            "q": __dash + __dash + __dot + __dash,
            "r": __dot + __dash + __dot,
            "s": __dot + __dot + __dot,
            "t": __dash,
            "u": __dot + __dot + __dash,
            "v": __dot + __dot + __dot + __dash,
            "w": __dot + __dash + __dash,
            "x": __dash + __dot + __dot + __dash,
            "y": __dash + __dot + __dash + __dash,
            "z": __dash + __dash + __dot + __dot,
            " ": __word_separator,
            "": __symbol_separator,
        }.items()
    }

    def __init__(self, characters: str):
        if not isinstance(characters, str):
            raise TypeError
        self.__characters = characters.lower()
        if isinstance(list(self.__rev_semaphore.keys())[0], tuple):
            self.__rev_semaphore = {
                self.__directions[key[0] - 1] + self.__directions[key[1] - 1]: value
                for key, value in self.__rev_semaphore.items()
            }

    @classmethod
    def from_string(cls, string: str) -> str:
        if isinstance(list(cls.__rev_semaphore.keys())[0], tuple):
            cls.__rev_semaphore = {
                cls.__directions[key[0] - 1] + cls.__directions[key[1] - 1]: value
                for key, value in cls.__rev_semaphore.items()
            }
        if not isinstance(string, str):
            raise TypeError
        r = cls.__braille_from_string(string)
        if r[0]:
            return r[1].strip()
        r = cls.__semaphore_from_string(string)
        if r[0]:
            return r[1].strip()
        r = cls.__numbers_from_string(string)
        if r[0]:
            return r[1].strip()
        r = cls.__morse_from_string(string)
        if r[0]:
            return r[1].strip()
        raise ValueError

    @classmethod
    def __braille_from_string(cls, string: str):
        result = ""
        for c in string:
            if c not in cls.__rev_braille.keys():
                return False, ""
            result += cls.__rev_braille[c]
        return True, result

    @classmethod
    def __semaphore_from_string(cls, string: str):
        result = ""
        for word in string.split(" "):
            if len(word) % 4 != 0:
                return False, ""
            for i in range(len(word) // 4):
                begin = i * 4
                if word[begin] != "(" or word[begin + 3] != ")":
                    return False, ""
                if word[begin + 1 : begin + 3] not in cls.__rev_semaphore.keys():
                    return False, ""
                result += cls.__rev_semaphore[word[begin + 1 : begin + 3]]
            result += " "
        return True, result

    @classmethod
    def __morse_from_string(cls, string: str):
        result = ""
        for word in string.split(cls.__word_separator):
            for char in word.split(cls.__symbol_separator):
                if char not in cls.__rev_morse.keys():
                    return False, ""
                result += cls.__rev_morse[char]
            result += " "
        return True, result

    @classmethod
    def __numbers_from_string(cls, string: str):
        nums = string.split(", ")
        bases = [2, 10, 16]
        base = 2
        miss = 0
        for b in bases:
            try:
                int(nums[0], b)
            except ValueError:
                miss += 1
            else:
                base = b
                break
        if miss == 3:
            return False, ""
        result = ""
        for num in nums:
            result += chr(ord("a") - 1 + int(num, base))
        return True, result

    def to_braille(self) -> Braille:
        return Braille(self.__characters)

    def to_morse(self) -> Morse:
        return Morse(self.__characters)

    def to_number_systems(self, base=10) -> NumberSystems:
        return NumberSystems(self.__characters, base)

    def to_semaphore(self) -> Semaphore:
        return Semaphore(self.__characters)

    def __getitem__(self, item) -> "Symbols":
        return Symbols(self.__characters[item])

    def __str__(self):
        return self.__characters

    def __len__(self):
        return len(self.__characters)

    def __eq__(self, other):
        if not isinstance(other, Symbols):
            raise TypeError
        return self.__characters == other.__characters

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if isinstance(other, str):
            return Symbols(self.__characters + other)
        if isinstance(other, Symbols):
            return Symbols(self.__characters + other.__characters)
        raise TypeError
