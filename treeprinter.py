## Table of contents
#
# @addToClass decorator
# printIndented function
#
# 0. Base Node class
# 1. Initial rules
# 2. Statement types
#   2.1 Condition statements
#   2.2 Values range
# 3. Instruction types
#   3.1 Assignment operators
# 4. Expressions
#   4.1 Array definition (and array line used in other structures)
#   4.2 Array special functions
#   4.3 Array transposition
#   4.4 Unary negation
#   4.5 Binary expressions
#   4.6 Expressions in parenthesis
#   4.7 Elementary types
# X. Error raising

from __future__ import print_function
import AST

# @addToClass decorator definition
def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

# The only funtion that really does the printing
    @classmethod
    def printIndented(cls, string, level):
        print ("|  " * level + string)

## 0. Base Node class

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

## 1. Initial rules

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        for instruction in self.instruction_lines:
            instruction.printTree(indent)

    @addToClass(AST.Empty)
    def printTree(self, indent=0):
        pass


## 2. Statement types

    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        TreePrinter.printIndented('IF', indent)
        self.condition.printTree(indent + 1)
        #TreePrinter.printIndented('THEN', indent)
        self.instruction_line.printTree(indent + 1)
        if self.else_instruction:
            #TreePrinter.printIndented('ELSE', indent)
            self.else_instruction.printTree(indent + 1)

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

    @addToClass(AST.CodeBlock)
    def printTree(self, indent=0):
        TreePrinter.printIndented('{', indent)
        self.program.printTree(indent + 1)
        TreePrinter.printIndented('}', indent)

# 2.1 Condition statements
    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

# 2.2 Values range
    @addToClass(AST.Range)
    def printTree(self, indent=0):
        TreePrinter.printIndented('RANGE', indent)
        self.start_number.printTree(indent + 1)
        self.end_number.printTree(indent + 1)


## 3. Instruction types

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

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        TreePrinter.printIndented('CONTINUE', indent)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        TreePrinter.printIndented('BREAK', indent)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        TreePrinter.printIndented('RETURN', indent)
        self.expression.printTree(indent + 1)

# 3.1 Assignment operators
# no AST classes for this part


## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
    @addToClass(AST.Array)
    def printTree(self, indent=0):
        for vector in self.content:
            TreePrinter.printIndented('VECTOR', indent)
            for element in vector:
                element.printTree(indent + 1)

# 4.2 Array special functions
    @addToClass(AST.Function)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.name, indent)
        for argument in self.arguments:
            argument.printTree(indent + 1)

# 4.3 Array transposition
    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        TreePrinter.printIndented('TRANSPOSITION', indent)
        self.argument.printTree(indent + 1)

# 4.4 Unary negation
    @addToClass(AST.Negation)
    def printTree(self, indent=0):
        TreePrinter.printIndented('NEGATION', indent)
        self.expression.printTree(indent + 1)

# 4.5 Binary expressions
    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
    @addToClass(AST.String)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.content, indent)

    @addToClass(AST.Identifier)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.name, indent)

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        TreePrinter.printIndented('REF', indent)
        TreePrinter.printIndented(self.id, indent + 1)
        for index in self.indicies:
            index.printTree(indent + 1)

    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)

    @addToClass(AST.Real)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)


# X. Error raising

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
