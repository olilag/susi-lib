from typing import Tuple

class BrailleChar:
    __symbol_dict = {
        'a': 0x1,
        'b': 0x3,
        'c': 0x9,
        'd': 0x19,
        'e': 0x11,
        'f': 0xb,
        'g': 0x1b,
        'h': 0x13,
        'i': 0xa,
        'j': 0x1a,
        'k': 0x5,
        'l': 0x7,
        'm': 0xd,
        'n': 0x1d,
        'o': 0x15,
        'p': 0xf,
        'q': 0x1f,
        'r': 0x17,
        's': 0xe,
        't': 0x1e,
        'u': 0x25,
        'v': 0x27,
        'w': 0x37,
        'x': 0x2d,
        'y': 0x3d,
        'z': 0x35,
        ' ': ord(' ') - 0x2800
    }

    def __init__(self, character):
        if not isinstance(character, str):
            raise TypeError
        if len(character) > 1 or (not character.isalpha() and character != ' '):
            raise ValueError
        self.__char = character.lower()

    def __getitem__(self, item) -> bool:
        if 0 > item or item > 5:
            raise IndexError
        if self.__char == ' ':
            return False
        return (self.__symbol_dict[self.__char] >> item) % 2 == 1

    def __str__(self):
        return chr(self.__symbol_dict[self.__char] + 0x2800)

    def get_points(self) -> Tuple[bool, bool, bool, bool, bool, bool]:
        if self.__char == ' ':
            return (False,)*6
        return tuple(((self.__symbol_dict[self.__char] >> i) % 2 == 1 for i in range(6)))


class Braille:
    def __init__(self, characters: str):
        if not isinstance(characters, str):
            raise TypeError
        correct = True
        for c in characters.lower():
            correct = correct and (c.isalpha() or c == ' ')
        if not correct:
            raise ValueError
        self.__seq = [BrailleChar(c) for c in characters]

    def __str__(self):
        return ''.join(str(c) for c in self.__seq)

    def __len__(self):
        return len(self.__seq)

    def __getitem__(self, item) -> BrailleChar:
        return self.__seq[item]
