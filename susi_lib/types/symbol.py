from susi_lib.types import Braille
from susi_lib.types import Morse
class Symbol:
    def __init__(self, character: str):
        self.__character = character.lower()

    def to_braille(self) -> Braille:
        pass

    def to_morse(self) -> Morse:
        return Morse(self.__character)


class SymbolSequence:
    def __init__(self, data):
        self.__characters = [Symbol(x) for x in data]
