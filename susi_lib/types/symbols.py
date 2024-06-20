from susi_lib.types import Braille
from susi_lib.types import Morse
from susi_lib.types import NumberSystems
from susi_lib.types import Semaphore


class Symbols:
    def __init__(self, characters: str):
        if not isinstance(characters, str):
            raise TypeError
        self.__characters = characters.lower()

    def to_braille(self) -> Braille:
        pass

    def to_morse(self) -> Morse:
        return Morse(self.__characters)

    def to_number_systems(self) -> NumberSystems:
        return NumberSystems(self.__characters)

    def to_semaphore(self) -> Semaphore:
        return Semaphore(self.__characters)

    def __getitem__(self, item) -> "Symbols":
        return Symbols(self.__characters[item])

    def __str__(self):
        return self.__characters

    def __len__(self):
        return len(self.__characters)
