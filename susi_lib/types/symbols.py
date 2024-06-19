from susi_lib.types import Braille
from susi_lib.types import Morse
class Symbols:
    def __init__(self, characters: str):
        if not isinstance(characters, str):
            raise TypeError
        self.__characters = characters.lower()

    def to_braille(self) -> Braille:
        pass

    def to_morse(self) -> Morse:
        return Morse(self.__characters)
