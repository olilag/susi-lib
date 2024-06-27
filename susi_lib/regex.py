import re
from typing import Union, List, Tuple
from enum import Enum, auto
from susi_lib.utils import export


@export
class RegEx:

    def __init__(self, pattern: str):
        if not isinstance(pattern, str):
            raise TypeError("Pattern needs to be a string")
        try:
            self.__re = re.compile(pattern, re.MULTILINE | re.IGNORECASE)
        except Exception as e:
            raise ValueError("Invalid regex pattern: " + str(e))
        self.__data = None

    def set_data(self, data: Union[List[str], str]):
        if isinstance(data, str):
            with open(data, "r", encoding="utf-8") as f:
                self.__data = []
                for line in f:
                    self.__data.append(line.strip())
        elif isinstance(data, list):
            self.__data = data
        else:
            raise TypeError(
                "Data must be a string with filename or list[str] with some data"
            )

    def execute(self):
        if self.__data is None:
            raise AttributeError("Did not set data to search before search")

        input_text = "\n".join(self.__data)
        return self.__re.findall(input_text)

    def get_pattern(self):
        return self.__re.pattern


@export
class Selection(Enum):
    NONE = auto()
    INVERT = auto()
    ANY = auto()


@export
def create_regex(
    *args: Tuple[str, Selection],
    length: Union[int, Tuple[int, int]] = None,
    letters: str = None,
    invert: bool = None,
) -> RegEx:
    if len(args) > 0:
        pattern = "^"
        for position in args:
            if (
                len(position) != 2
                or not isinstance(position[0], str)
                or not isinstance(position[2], Selection)
            ):
                raise TypeError("All arguments must be tuples (str, Selection)")
            part = position[0]
            match (position[1]):
                case Selection.NONE:
                    if len(part) == 0:
                        raise ValueError("Set of letters can't be empty")
                case Selection.INVERT:
                    if len(part) == 0:
                        raise ValueError("Set of letters can't be empty")
                    part = "^" + part
                case Selection.ANY:
                    part = "."
                case _:
                    raise ValueError("Invalid enum value")
            pattern += f"[{part}]"
        pattern += "$"
        return RegEx(pattern)
    if length is None or letters is None or invert is None:
        raise ValueError("You must set all arguments")
    if not isinstance(length, Union[int, tuple]):
        raise TypeError("Length must an int or pair (int, int)")
    if not isinstance(letters, str):
        raise TypeError("Letters must be a string")
    if not isinstance(invert, bool):
        raise TypeError("Invert must be a bool")
    inv = "^" if invert else ""
    quantify = (
        f"{{{length}}}" if isinstance(length, int) else f"{{{length[0]},{length[1]}}}"
    )
    pattern = f"^[{inv}{letters}]{quantify}$"
    return RegEx(pattern)
