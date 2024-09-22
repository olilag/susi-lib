"""Tu je príklad použitia triedy Finder a funkcie is_palindrome.
Trieda Finder nájde v zadanom zozname slov/súbore (v súbore by malo byť jedno slovo na riadok).
Funkcia is_palindrome urči či, je daná vec (hocičo, čo sa dá iterovať) palindróm.

Funkcia long_word určí, či je zadaný reťazec dlhší ako 5. Spolu tento program vypíše prvý
palindróm zo súboru example.txt, následne sa pridá funkcia long_word do zoznamu funkcií,
takže volanie finder.find_all() vráti všetky palindrómy dlhšie ako 5 a vypíše ich.
"""

from susi_lib import Finder
from susi_lib.functions import is_palindrome


def long_word(word: str) -> bool:
    return len(word) > 5


def main():
    finder = Finder("example.txt", is_palindrome)
    print(finder.find_first())
    finder.add_function(long_word)
    print(finder.find_all())


if __name__ == "__main__":
    main()
