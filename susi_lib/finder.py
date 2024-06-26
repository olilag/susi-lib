from typing import Callable, Literal, overload, List


class Finder:
    def __init__(self, file_name: str, *functions: Callable[[str], bool]):
        with open(file_name, "r", encoding="utf-8") as f:
            self.__text = f.readlines()
        self.__function = list(functions)

    def __valid_word(self, word: str):
        for f in self.__function:
            if not f(word):
                return False
        return True

    @overload
    def __execute(self, first: Literal[True]) -> str: ...

    @overload
    def __execute(self, first: Literal[False]) -> List[str]: ...

    def __execute(self, first: bool):
        result = []
        for word in self.__text:
            if self.__valid_word(word):
                if first:
                    return word
                result.append(word)
        return result

    def __iter__(self):
        for word in self.__text:
            if self.__valid_word(word):
                yield word

    def find_first(self):
        return self.__execute(True)

    def find_all(self):
        return self.__execute(False)

    def change_function(self, *functions: Callable[[str], bool]):
        self.__function = list(functions)

    def add_function(self, *functions: Callable[[str], bool]):
        self.__function.extend(functions)
