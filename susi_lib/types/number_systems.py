class NumberChar:
    __symbol_dict = {chr(ord("a") + x): x + 1 for x in range(26)}
    __format = {2: "05b", 10: "d", 16: "x"}

    def __init__(self, character, base=10):
        if not isinstance(character, str):
            raise TypeError
        if len(character) > 1 or (not character.isalpha() and character != " "):
            raise ValueError
        self.__char = character.lower()
        self.__base = base

    def change_base(self, base):
        if not isinstance(base, int):
            raise TypeError
        self.__base = base

    def __str__(self):
        if self.__char == " ":
            return ""
        return format(self.__symbol_dict[self.__char], self.__format[self.__base])

    def __eq__(self, other):
        if not isinstance(other, NumberChar):
            raise TypeError
        return self.__char == other.__char and self.__base == other.__base

    def __ne__(self, other):
        if isinstance(other, BrailleChar):
            return not self == other
        raise TypeError

    @classmethod
    def get_dict(cls):
        return cls.__symbol_dict


class NumberSystems:
    def __init__(self, characters, base=10):
        if isinstance(characters, str):
            correct = True
            for c in characters.lower():
                correct = correct and (c.isalpha() or c == " ")
            if not correct:
                raise ValueError
            self.__base = base
            self.__seq = [NumberChar(c, self.__base) for c in characters]
        elif isinstance(characters, list):
            self.__base = base
            self.__seq = characters
        else:
            raise TypeError

    def __str__(self):
        return ", ".join(
            [str(c) for c in self.__seq if c != NumberChar(" ", self.__base)]
        )

    def __len__(self):
        return len(self.__seq)

    def __getitem__(self, item) -> NumberChar:
        return self.__seq[item]

    def __add__(self, other):
        if isinstance(other, str):
            return NumberSystems(
                self.__seq + [NumberChar(c, self.__base) for c in other]
            )
        if isinstance(other, NumberSystems):
            old_base = other.__base
            other.change_base(self.__base)
            ret = NumberSystems(self.__seq + other.__seq, self.__base)
            other.change_base(old_base)
            return ret
        if isinstance(other, NumberChar):
            return NumberSystems(self.__seq + [other], self.__base)
        raise TypeError

    def change_base(self, base: int):
        if not isinstance(base, int):
            raise TypeError
        self.__base = base
        for n in self.__seq:
            n.change_base(self.__base)

    @staticmethod
    def get_dict():
        return NumberChar.get_dict()
