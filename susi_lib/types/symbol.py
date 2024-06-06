from susi_lib.types import Braille
from susi_lib.types import Morse
class Symbol:
    def __init__(self, character: str):
        self.__character = character

    def to_braille(self) -> Braille:
        pass

    def to_morse(self) -> Morse:
        return Morse(self.__character)
