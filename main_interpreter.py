import sys
import scanner
import parser
import treeprinter
import typechecker
import interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example5_1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = scanner.Scanner()
    lexer.build()

    parser = parser.Parser(lexer)
    parser.build()

    text = file.read()

    typeChecker = typechecker.TypeChecker()

    try:
        ast = parser.parse(text, lexer=lexer)
    except:
        print("Syntax error(s) occured")
    else:
        return_code = typeChecker.visit(ast)
        if return_code == 0:
            ast.accept(interpreter.Interpreter())
        else:
            print("Semantic errors occured ({} error(s))".format(return_code))


    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())
