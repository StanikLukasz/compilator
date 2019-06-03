import sys
import ply.yacc as yacc
import scanner
import parser
import treeprinter
import typechecker
import interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = scanner.Scanner()
    lexer.build()

    parser = parser.parser
    text = file.read()

    typeChecker = typechecker.TypeChecker()

    try:
        ast = parser.parse(text, lexer=lexer)
        typeChecker.visit(ast)
    except ValueError as e:
         print(e)

    # ast.accept(Interpreter())
    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())

