from lib2to3.pgen2 import grammar
from pathlib import Path
from pprint import pprint

import tatsu
from tatsu.ast import AST


class CalcBasicSemantics(object):
    def number(self, ast):
        return int(ast)

    def term(self, ast):
        if not isinstance(ast, AST):
            return ast
        elif ast.op == "*":
            return ast.left * ast.right
        elif ast.op == "/":
            return ast.left / ast.right
        else:
            raise Exception("Unknown operator", ast.op)

    def expression(self, ast):
        if not isinstance(ast, AST):
            return ast
        elif ast.op == "+":
            return ast.left + ast.right
        elif ast.op == "-":
            return ast.left - ast.right
        else:
            raise Exception("Unknown operator", ast.op)


def parse_with_basic_semantics():
    grammar = Path("src/resources/smol.ebnf").read_text()

    parser = tatsu.compile(grammar)
    ast = parser.parse("3 + 5 * ( 10 - 20 )", semantics=CalcBasicSemantics())

    print("# BASIC SEMANTICS RESULT")
    pprint(ast, width=20, indent=4)


if __name__ == "__main__":
    parse_with_basic_semantics()
