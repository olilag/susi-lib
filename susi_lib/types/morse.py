class Morse:
    __dot = '.'
    __dash = '-'
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
        'z': __dash + __dash + __dot + __dot
    }
    __symbol_dict_rev = {(v, k) for k, v in __symbol_dict}

    def __init__(self, character: str):
        if not character.isalpha():
            raise ValueError("Character is not part of alphabet")
        self.__character = character

    def __str__(self):
        return self.__symbol_dict[self.__character]
