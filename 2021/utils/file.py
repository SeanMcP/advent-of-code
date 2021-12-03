from os import replace
from typing import cast


def get_lines(file, castToInt=False):
    return list(map(lambda ln: int(ln.replace("\n", "")) if castToInt == True else ln.replace("\n", ""), file.readlines()))


def read_file(path, castToInt=False):
    with open(path) as file:
        return get_lines(file, castToInt)
