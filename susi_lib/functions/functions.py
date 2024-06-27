from susi_lib.types import Symbols
from susi_lib.utils import export
from typing import Iterable


@export
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


@export
def decode(string: str):
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return Symbols.from_string(string)


@export
def encode_morse(string: str):
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_morse())


@export
def encode_braille(string: str):
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_braille())


@export
def encode_semaphore(string: str):
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_semaphore())


@export
def encode_numbers(string: str, base=10):
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    if not isinstance(base, int):
        raise TypeError("Base must be an int")
    if not base in [2, 10, 16]:
        raise ValueError("Valid values for base are 2, 10, 16")
    return str(Symbols(string).to_number_systems(base))
