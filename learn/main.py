from pathlib import Path
from pprint import pformat, pprint
from typing import Any

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from termcolor import cprint


def pprint_color(obj: Any):
    print(
        highlight(pformat(obj, width=10), PythonLexer(), TerminalFormatter())
    )


import json

import tatsu
from tatsu import parse
from tatsu.util import asjson

GRAMMAR = Path("grammar/pin.ebnf").read_text()
parser = tatsu.compile(GRAMMAR)


def parse_code(code: str):
    ast = parser.parse(code)
    # print(ast)
    cprint(code, "cyan")
    pprint_color(asjson(ast))


var = """
u: u16 = 3
x: int
y := 1
z: i32, y: i8
"""

const = """
X :: 3
Y :: 4
Z :: 3, Y :: 4
"""

enum = """
IpAddr :: enum {
    V4,
    V6,
}
"""

func = """
   spam :: () -> {}
   egg :: () -> i16 {}
   mult2 :: (n:i32) -> {}
   add :: (a:i16, b:i16) -> i16 {}
"""

expr = """\
86 + 84 + 87 / (96 - 46) / 59
((((49)))) + ((46))
76 + 18 + 4 - (98) - 7 / 15
(((73)))
"""
"""
(55) - (false) * 55 + 92 - 13 - ((36))
(78) - (7 / 56 * 33)
(81) - 18 * (((true)) * 59 - 14)
(((8.9)))
(5.1239)
"""


def test_variable_declaration():
    ...
    parse_code("foo: i32 = 2 + 3\n")
    parse_code("foo: i32 = 2 + 3, bar: i32\n")
    parse_code("foo: i32 = 10, bar := 20\n")
    parse_code("foo: i32 = 10, bar := 20, baz: i32\n")
    parse_code("foo:=10, bar:= foo + 10\n")
    # parse_code(var)
    # parse_code(const)
    # parse_code(enum)
    # parse_code(func)
    # parse_code(expr)
    # for line in expr.splitlines():
    #     parse_code(line + "\n")


if __name__ == "__main__":
    test_variable_declaration()
