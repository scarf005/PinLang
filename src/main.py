from pathlib import Path

from termcolor import cprint

GRAMMAR = Path("src/resources/smol.ebnf").read_text()
# GRAMMAR = Path("src/resources/pin.ebnf").read_text()
import json

import tatsu
from tatsu import parse
from tatsu.util import asjson

# model = tatsu.compile(GRAMMAR)
# code = tatsu.to_python_sourcecode(GRAMMAR)
# print(code)
# code = "안녕"
# code = "3 + 5 * ( 10 - 20 )"

parser = tatsu.compile(GRAMMAR)


def parse_code(code: str):
    ast = parser.parse(code)
    # print(ast)
    cprint(code, "yellow")
    cprint(json.dumps(asjson(ast), indent=2), "cyan")


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
3 + 5 * ( 10 - 20 )
(23)
86 + 84 + 87 / (96 - 46) / 59
((((49)))) + ((46))
76 + 18 + 4 - (98) - 7 / 15
(((73)))
(55) - (54) * 55 + 92 - 13 - ((36))
(78) - (7 / 56 * 33)
(81) - 18 * (((8)) * 59 - 14)
(((89)))
(59)
"""


def test_variable_declaration():
    ...
    # parse_code(var)
    # parse_code(const)
    # parse_code(enum)
    # parse_code(func)
    for line in expr.splitlines():
        parse_code(line)


if __name__ == "__main__":
    test_variable_declaration()
