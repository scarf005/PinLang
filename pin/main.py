import json
from pathlib import Path
from pprint import pprint

from tatsu import parse
from tatsu.util import asjson

variable_declarations = [
    "let x = 1 // --> const int x = 1;"
    "let y: int = 2 // --> const int y = 2;"
    "let mut z = 3 // --> int z = 3;"
    "let xPtr = &x // --> const int* xPtr = &x;"
    "let yPtr: *int = &y // --> const int* yPtr = &y;"
    "let zPtr: *mut int = &z // --> int* zPtr = &mut z;"
]
variable_declarations_simple = [
    "let x = 1",
    "let y = 2",
]

grammar_text = (Path(__file__).parent / "grammar.tatsu").read_text()

test_cases = [
    "let a = 3\n",
    "let b : i32 = 4\n",
    "let mut y = 2\n",
    "let c = if true { 1 } else { 2 }\n",
    """
    let a = when 3 {
        1 -> 1,
        2 -> 2,
        else -> 3
    }
    """,
    # "let double = (i) -> {}\n",
    "let main = () -> {}\n",
]

for text in test_cases:
    ast = parse(grammar_text, text)
    # pprint(ast)
    print(json.dumps(asjson(ast), indent=2))
