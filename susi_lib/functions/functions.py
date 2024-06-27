"""Contains some useful functions"""

from susi_lib.types import Symbols
from susi_lib.utils import export


@export
def is_palindrome(word):
    """Checks if a value is a palindrome (is the same from front and back).

    :param word: value to check, it needs to have __getitem__, __len__ and __ne__
    :return: True if it is a palindrome, False when it is not
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


@export
def decode(string: str):
    """Decodes a given value.

    Supported encodings are Braille, Numbers, Morse and Semaphore. Encoding should be the same
    as the strings returned by __str__ method of classes in susi_lib.types.
    :param string: The string to decode
    :return: Decoded string
    """
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return Symbols.from_string(string)


@export
def encode_morse(string: str):
    """Encode the given string into morse.

    :param string: The string to encode (should contain only alphabetical chars and spaces)
    :return: Encoded morse string
    """
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_morse())


@export
def encode_braille(string: str):
    """Encode the given string into braille.

    :param string: The string to encode (should contain only alphabetical chars and spaces)
    :return: Encoded braille string
    """
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_braille())


@export
def encode_semaphore(string: str):
    """Encode the given string into semaphore.

    :param string: The string to encode (should contain only alphabetical chars and spaces)
    :return: Encoded semaphore string
    """
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    return str(Symbols(string).to_semaphore())


@export
def encode_numbers(string: str, base=10):
    """Encode the given string into numbers of given base

    :param string: The string to encode (should contain only alphabetical chars and spaces)
    :param base: The base of the number system (2, 10, 16)
    :return: Encoded numbers string
    """
    if not isinstance(string, str):
        raise TypeError("String needs to be a string")
    if not isinstance(base, int):
        raise TypeError("Base must be an int")
    if base not in [2, 10, 16]:
        raise ValueError("Valid values for base are 2, 10, 16")
    return str(Symbols(string).to_number_systems(base))
