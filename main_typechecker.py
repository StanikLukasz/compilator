import sys
import ply.yacc as yacc
import scanner
import parser
import treeprinter
import typechecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example4_1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = scanner.Scanner()
    lexer.build()

    parser = parser.parser
    text = file.read()

    ast = parser.parse(text, lexer=lexer)




    # Below code shows how to use visitor
# typeChecker = TypeChecker()
# typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
