from pathlib import Path

GRAMMAR = Path("src/resources/grammar.ebnf").read_text()
import json

import tatsu
from tatsu import parse
from tatsu.util import asjson

# model = tatsu.compile(GRAMMAR)
# code = tatsu.to_python_sourcecode(GRAMMAR)
# print(code)
code = "3 + 5 * ( 10 - 20 )"
# code = "x : int = 3"
ast = parse(GRAMMAR, code)
print(asjson(ast))
# print(json.dumps(asjson(ast), indent=2))
