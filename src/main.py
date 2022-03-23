from pathlib import Path

GRAMMAR = Path("src/resources/declaration.ebnf").read_text()
import json

import tatsu
from tatsu import parse
from tatsu.util import asjson

# model = tatsu.compile(GRAMMAR)
# code = tatsu.to_python_sourcecode(GRAMMAR)
# print(code)
# code = "안녕"
codes = ["x:", "x : i8"]
# code = "3 + 5 * ( 10 - 20 )"
parser = tatsu.compile(GRAMMAR)
for code in codes:
    ast = parser.parse(code)
    print(json.dumps(asjson(ast), indent=2))
