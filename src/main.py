from pathlib import Path

GRAMMAR = Path("src/resources/pin.ebnf").read_text()
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
    print(json.dumps(asjson(ast), indent=2))


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


def test_variable_declaration():
    ...
    # parse_code(var)
    # parse_code(const)
    # parse_code(enum)
    parse_code(func)


if __name__ == "__main__":
    test_variable_declaration()
