from susi_lib.types import Symbols
from susi_lib.utils import export


@export
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


@export
def decode(string: str):
    return Symbols.from_string(string)


@export
def encode_morse(string: str):
    return str(Symbols(string).to_morse())


@export
def encode_braille(string: str):
    return str(Symbols(string).to_braille())


@export
def encode_semaphore(string: str):
    return str(Symbols(string).to_semaphore())


@export
def encode_numbers(string: str, base=10):
    return str(Symbols(string).to_number_systems(base))
