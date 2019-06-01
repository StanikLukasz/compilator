#object oriented version

import sys
import scanner # scanner.py is a file you create, (it is not an external library)


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = scanner.Scanner()
    lexer.build()


    # Give the lexer some input
    lexer.input(text)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        column = lexer.find_column(text,tok)
        print("(%d,%d): %s(%s)" %(tok.lineno, column, tok.type, tok.value))
