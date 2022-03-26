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


val = """
foo: i32 = 2 + 3, bar: i32
foo: i32 = 10, bar := foo, X :: 3
Z :: 3, Y : u8 : 4
"""

enum = """
IpAddr :: enum {
    V4,
    V6,
}
"""

func = """
   spam :: () -> { foo: i32 }
   egg :: () -> i16 {
        foo: i32 = 2 + 3, bar: i32
   }
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
    # parse_code(val)
    # parse_code(enum)
    parse_code(func)
    # parse_code(expr)


if __name__ == "__main__":
    test_variable_declaration()
