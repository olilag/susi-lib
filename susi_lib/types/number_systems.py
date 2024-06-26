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


class NumberSystems:
    def __init__(self, characters, base=10):
        if not isinstance(characters, str):
            raise TypeError
        correct = True
        for c in characters.lower():
            correct = correct and (c.isalpha() or c == " ")
        if not correct:
            raise ValueError
        self.__base = base
        self.__seq = [NumberChar(c) for c in characters]

    def __str__(self):
        return ", ".join([str(c) for c in self.__seq])

    def __len__(self):
        return len(self.__seq)

    def __getitem__(self, item) -> NumberChar:
        return self.__seq[item]

    def __add__(self, other):
        if isinstance(other, str):
            self.__seq += [NumberChar(c, self.__base) for c in other]
        if isinstance(other, NumberSystems):
            other.change_base(self.__base)
            self.__seq += other.__seq
            return self
        if isinstance(other, NumberChar):
            self.__seq.append(other.change_base(self.__base))
            return self
        raise TypeError

    def change_base(self, base):
        if not isinstance(base, int):
            raise TypeError
        self.__base = base
        for n in self.__seq:
            n.change_base(self.__base)

    @classmethod
    def get_dict(cls):
        return cls.__symbol_dict
