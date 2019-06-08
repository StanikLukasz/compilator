
import AST
import symboltable
from memory import *
import exceptions
from visit import *
import sys
from exceptions import *
import operator
import numpy as np

sys.setrecursionlimit(10000)

class Interpreter(object):

    def __init__(self):
        self.memory_stack = MemoryStack()

        self.binary_operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            ".+": operator.add,
            ".-": operator.sub,
            ".*": np.multiply,
            "./": np.divide,
            "<" : operator.lt,
            ">": operator.gt,
            "<=": operator.le,
            ">=": operator.ge,
            "==": operator.eq,
            "!=": operator.ne,
        }

        self.unary_operations = {
            "-": operator.neg,
            "'": np.transpose,
        }

        self.functions = {
            'EYE': np.eye,
            'ZEROS': np.zeros,
            'ONES': np.ones,
        }

# 0. Base Node class

    @on('node')
    def visit(self, node):
        pass

## 1. Initial rules

    @when(AST.Program)
    def visit(self, node):
        self.visit(node.instruction_lines)

    def visit(self, node):
        pass

## 2. Statement types

    @when(AST.IfElse)
    def visit(self, node):
        if node.condition.accept(self):
            return node.instruction_line.accept(self)
        else:
            if node.else_instruction(self):
                return node.instruction_line.accept(self)

    @when(AST.WhileLoop)
    def visit(self, node):
        result = None
        while node.cond.accept(self):
            result = node.instruction.accept(self)
        return result

    @when(AST.ForLoop)
    def visit(self, node):
        result = None
        for iterator in node.range.accept(self):
            self.memory_stack.insert((node.iterator, iterator))
            result = node.instruction.accept(self)
        return result

    @when(AST.CodeBlock)
    def visit(self, node):
        self.visit(node.program)

# 2.1 Condition statements
    @when(AST.Condition)
    def visit(self, node):
        pass

# 2.2 Values range
    @when(AST.Range)
    def visit(self, node):
        start = node.start_number.accept(self)
        end = node.end_number.accept(self)

        if type(start) == str:
            start = self.memory_stack.get(start)
        if type(end) == str:
            end = self.memory_stack.get(end)

        return range(start, end)

## 3. Instruction types

    # TODO
    # tutaj nei rozumiem zbytnio wszystkiego
    @when(AST.Assignment)
    def visit(self, node):
        right = None
        left = node.left if isinstance(node.left, AST.Variable) else node.left.value
        if node.op == "=":
            right = node.right.accept(self)
        elif node.op == "+=":
            right = operator.add(right, node.right.accept(self))
        elif node.op == "*=":
            right = node.right.accept(self)
            right = operator.mul(right, node.right.accept(self))
        elif node.op == "/=":
            right = node.right.accept(self)
            right = operator.truediv(right, node.right.accept(self))
        elif node.op == "-=":
            right = node.right.accept(self)
            right = operator.sub(right, node.right.accept(self))

        if isinstance(node.left, AST.Variable):
            variable = self.memory_stack.get(left.variable)
            where = left.key.accept(self)
            access = variable
            for iterator in where[:-1]:
                access = access[iterator]
            access[-1] = right
            self.memory_stack.insert((left.variable, variable))
        else:
            self.memory_stack.insert(left, right)


    @when(AST.Print)
    def visit(self, node):
        for iterator in node.array_line:
            print(iterator.accept(self))

    @when(AST.Condition)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.result.accept(self))

# 3.1 Assignment operators
# no AST classes for this part

## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
    @when(AST.Array)  #TODO
    def visit(self, node):
        pass

# 4.2 Array special functions
    @when(AST.Function)  #TODO
    def visit(self, node):
        pass

# 4.3 Array transposition
    @when(AST.Transposition)
    def visit(self, node):
        r = node.operand.accept(self)
        return np.transpose(r)

# 4.4 Unary negation
    @when(AST.Negation)
    def visit(self, node):
        r = node.operand.accept(self)
        return node.operand.neg(r)

# 4.5 Binary expressions
    @when(AST.BinExpr)  #TODO
    def visit(self, node):
        pass

# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
    @when(AST.String)  #TODO
    def visit(self, node):
        pass

    @when(AST.Identifier)  #TODO
    def visit(self, node):
        pass

    @when(AST.Reference)  #TODO
    def visit(self, node):
        pass

    @when(AST.Integer)  #TODO
    def visit(self, node):
        pass

    @when(AST.Real)  #TODO
    def visit(self, node):
        pass

# X. Error raising

    @when(AST.Error)
    def visit(self, node):
        pass


    def get_scopes(self):
        scopes = []
        parent = self.scope
        while parent:
            scopes.append(parent.name)
            parent = parent.parent
        return scopes