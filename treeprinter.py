from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @classmethod
    def printIndented(cls, string, level):
        print ("|   " * level + string)

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)

    @addToClass(AST.Real)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        for instruction in self.instruction_lines:
            instruction.printTree(indent)

    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):
        TreePrinter.printIndented('WHILE', indent)
        self.condition.printTree(indent + 1)
        #TreePrinter.printIndented('THEN', indent)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        TreePrinter.printIndented('FOR', indent)
        self.iterator.printTree(indent + 1)
        self.range.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        TreePrinter.printIndented('IF', indent)
        self.condition.printTree(indent + 1)
        #TreePrinter.printIndented('THEN', indent)
        self.instruction_line.printTree(indent + 1)
        if self.else_instruction:
            #TreePrinter.printIndented('ELSE', indent)
            self.else_instruction.printTree(indent + 1)

    @addToClass(AST.CodeBlock)
    def printTree(self, indent=0):
        TreePrinter.printIndented('{', indent)
        self.program.printTree(indent + 1)
        TreePrinter.printIndented('}', indent)


    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.content, indent)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.identifier.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        TreePrinter.printIndented('PRINT', indent)
        for expression in self.array_line:
            expression.printTree(indent + 1)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        TreePrinter.printIndented('RETURN', indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Empty)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        TreePrinter.printIndented('RANGE', indent)
        self.start_number.printTree(indent + 1)
        self.end_number.printTree(indent + 1)

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        TreePrinter.printIndented('CONTINUE', indent)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        TreePrinter.printIndented('BREAK', indent)

    @addToClass(AST.Identifier)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.name, indent) #todo: indicies

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.name, indent)
        for argument in self.arguments:
            argument.printTree(indent + 1)

    @addToClass(AST.Negation)
    def printTree(self, indent=0):
        TreePrinter.printIndented('NEGATION', indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        TreePrinter.printIndented('TRANSPOSITION', indent)
        #TreePrinter.printIndented(self.argument, indent + 1)
        self.argument.printTree(indent + 1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Array)
    def printTree(self, indent=0):
        TreePrinter.printIndented('ARRAY', indent)
        for vector in self.content:
            TreePrinter.printIndented('VECTOR', indent + 1)
            for element in vector:
                element.printTree(indent + 2)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body



    # define printTree for other classes
    # ...
