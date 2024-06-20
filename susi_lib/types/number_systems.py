class NumberSystems:
    __symbol_dict = {chr(ord("a") + x): x + 1 for x in range(26)}
    __format = {2: "05b", 10: "d", 16: "x"}

    def __init__(self, characters, base=10):
        if not isinstance(characters, str):
            raise TypeError
        correct = True
        for c in characters.lower():
            correct = correct and (c.isalpha() or c == " ")
        if not correct:
            raise ValueError
        self.__characters = characters.lower()
        self.__base = base

    def __str__(self):
        return ", ".join(
            [
                format(self.__symbol_dict[c], self.__format[self.__base])
                for c in self.__characters
                if c != " "
            ]
        )

    def __add__(self, other):
        if isinstance(other, str):
            other = NumberSystems(other)
        if not isinstance(other, NumberSystems):
            raise TypeError
        return NumberSystems(self.__characters + other.__characters, self.__base)

    def get(self):
        return [self.__symbol_dict[c] for c in self.__characters]

    def change_base(self, base):
        if not isinstance(base, int):
            raise TypeError
        self.__base = base

    def __eq__(self, other):
        if not isinstance(other, NumberSystems):
            raise TypeError
        return self.__characters == other.__characters
