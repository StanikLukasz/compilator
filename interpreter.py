
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
    @when(AST.Assignment)
    def visit(self, node):
        pass

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



    @when(AST.BinOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        # try sth smarter than:
        # if(node.op=='+') return r1+r2
        # elsif(node.op=='-') ...
        # but do not use python eval

    @when(AST.Assignment)
    def visit(self, node):
        pass
    #
    #

    # simplistic while loop interpretation
    @when(AST.WhileInstr)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            r = node.body.accept(self)
        return r

