import sys
import scanner
import parser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example2_3.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = scanner.Scanner()
    lexer.build()

    parser = parser.parser
    text = file.read()
    try:
        parser.parse(text, lexer=lexer)
    except ValueError as e:
        print(e)
