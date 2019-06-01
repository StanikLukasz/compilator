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
        self.instruction.printTree(indent + 1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        TreePrinter.printIndented('FOR', indent)
        self.iterator.printTree(indent + 1)
        self.range.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.CodeBlock)
    def printTree(self, indent=0):
        TreePrinter.printIndented('{', indent)
        self.program.printTree(indent + 1)
        TreePrinter.printIndented('}', indent)


    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        #TreePrinter.printIndented(self.op, indent)
        self.op.printTree(indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.content, indent)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.idetifier.printTree(indent + 1)
        self.expresion.printTree(indent + 1)

    @addToClass(AST.Printing)
    def printTree(self, indent=0):
        TreePrinter.printIndented('PRINT', indent)
        self.array_line.printTree(indent + 1)

    @addToClass(AST.Returning)
    def printTree(self, indent=0):
        TreePrinter.printIndented('RETURN', indent)
        self.expression.printTree(indent + 1)



    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body



    # define printTree for other classes
    # ...
