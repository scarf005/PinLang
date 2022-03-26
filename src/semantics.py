from pathlib import Path
from pprint import pprint

import tatsu


class CalcSemantics(object):
    def number(self, ast):
        return int(ast)

    def addition(self, ast):
        return ast.left + ast.right

    def subtraction(self, ast):
        return ast.left - ast.right

    def multiplication(self, ast):
        return ast.left * ast.right

    def division(self, ast):
        return ast.left / ast.right


def parse_refactored():
    grammar = Path("src/resources/smol.ebnf").read_text()

    parser = tatsu.compile(grammar)
    ast = parser.parse("3 + 5 * ( 10 - 20 )", semantics=CalcSemantics())

    print("# REFACTORED SEMANTICS RESULT")
    pprint(ast, width=20, indent=4)
    print()


if __name__ == "__main__":
    parse_refactored()
