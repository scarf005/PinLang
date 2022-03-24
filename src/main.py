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


def parse_codes(codes: list[str]):
    for code in codes:
        parse_code(code)


var = """u: u16 = 3
x: int
y := 1
z: i32, y: i8
"""

const = """X :: 3
Y :: 4
Z :: 3, Y :: 4
"""


def test_variable_declaration():
    parse_codes([var, const])


if __name__ == "__main__":
    test_variable_declaration()
