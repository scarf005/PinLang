import tatsu

from codegen import PostfixCodeGenerator


def parse_and_translate():
    with open("calc_model.ebnf") as f:
        grammar = f.read()

    parser = tatsu.compile(grammar, asmodel=True)
    model = parser.parse("3 + 5 * ( 10 - 20 )")

    postfix = PostfixCodeGenerator().render(model)

    print("# TRANSLATED TO POSTFIX")
    print(postfix)


if __name__ == "__main__":
    parse_and_translate()
