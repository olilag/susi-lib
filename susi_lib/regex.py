import re
from typing import Union, List, Tuple
from enum import Enum, auto
from susi_lib.utils import export

__all__ = []


@export
class RegEx:

    def __init__(self, pattern: str):
        self.__re = re.compile(pattern, re.MULTILINE | re.IGNORECASE)
        self.__data = None

    def set_data(self, data: Union[List[str], str]):
        if isinstance(data, str):
            with open(data, "r", encoding="utf-8") as f:
                data = f.readlines()
        self.__data = data

    def execute(self):
        if self.__data is None:
            raise AttributeError

        input_text = "\n".join(self.__data)
        return self.__re.findall(input_text)


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
            part = position[0]
            match (position[1]):
                case Selection.NONE:
                    if len(part) == 0:
                        raise ValueError
                case Selection.INVERT:
                    if len(part) == 0:
                        raise ValueError
                    part = "^" + part
                case Selection.ANY:
                    part = "."
                case _:
                    raise ValueError
            pattern += f"[{part}]"
        pattern += "$"
        return RegEx(pattern)
    if length is None or letters is None or invert is None:
        raise ValueError
    inv = "^" if invert else ""
    quantify = (
        f"{{{length}}}" if isinstance(length, int) else f"{{{length[0]},{length[1]}}}"
    )
    pattern = f"^[{inv}{letters}]{quantify}$"
    return RegEx(pattern)
