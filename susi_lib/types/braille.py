from typing import Tuple


class BrailleChar:
    __symbol_dict = {
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
    }

    def __init__(self, character):
        if not isinstance(character, str):
            raise TypeError
        if len(character) > 1 or (not character.isalpha() and character != " "):
            raise ValueError
        self.__char = character.lower()

    def __getitem__(self, item) -> bool:
        if 0 > item or item > 5:
            raise IndexError
        if self.__char == " ":
            return False
        return (self.__symbol_dict[self.__char] >> item) % 2 == 1

    def __str__(self):
        return chr(self.__symbol_dict[self.__char] + 0x2800)

    def __eq__(self, other):
        if isinstance(other, BrailleChar):
            return self.__char == other.__char
        raise TypeError

    def __ne__(self, other):
        if isinstance(other, BrailleChar):
            return not self == other
        raise TypeError

    def get_points(self) -> Tuple[bool, bool, bool, bool, bool, bool]:
        if self.__char == " ":
            return (False,) * 6
        return tuple(
            ((self.__symbol_dict[self.__char] >> i) % 2 == 1 for i in range(6))
        )

    @classmethod
    def get_dict(cls):
        return cls.__symbol_dict


class Braille:
    def __init__(self, characters: str):
        if isinstance(characters, str):
            correct = True
            for c in characters.lower():
                correct = correct and (c.isalpha() or c == " ")
            if not correct:
                raise ValueError
            self.__seq = [BrailleChar(c) for c in characters]
        elif isinstance(characters, list):
            self.__seq = characters
        else:
            raise TypeError

    def __str__(self):
        return "".join(str(c) for c in self.__seq)

    def __len__(self):
        return len(self.__seq)

    def __getitem__(self, item) -> BrailleChar:
        return self.__seq[item]

    def __add__(self, other):
        if isinstance(other, str):
            return Braille(self.__seq + [BrailleChar(c) for c in other])
        if isinstance(other, Braille):
            return Braille(self.__seq + other.__seq)
        if isinstance(other, BrailleChar):
            return Braille(self.__seq + [other])
        raise TypeError

    @staticmethod
    def get_dict():
        return BrailleChar.get_dict()
