from susi_lib.types import Symbols


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def decode(string: str):
    return Symbols.from_string(string)


def encode_morse(string: str):
    return str(Symbols(string).to_morse())


def encode_braille(string: str):
    return str(Symbols(string).to_braille())


def encode_semaphore(string: str):
    return str(Symbols(string).to_semaphore())


def encode_numbers(string: str, base=10):
    return str(Symbols(string).to_number_systems(base))
