
import AST
import symboltable
from memory import *
import exceptions
from visit import *
import sys

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
    def visit_Program(self, node):
        self.visit(node.instruction_lines)

    def visit_Empty(self, node):
        pass

## 2. Statement types

    @when(AST.IfElse)
    def visit_IfElse(self, node):
        if node.condition.accept(self):
            return node.instruction_line.accept(self)
        else:
            if node.else_instruction(self):
                return node.instruction_line.accept(self)

    @when(AST.WhileLoop)
    def visit_WhileLoop(self, node):
        result = None
        while node.cond.accept(self):
            result = node.instruction.accept(self)
        return result

    @when(AST.ForLoop)
    def visit_ForLoop(self, node):
        result = None
        for iterator in node.range.accept(self):
            self.memory_stack.insert((node.iterator, iterator))
            result = node.instruction.accept(self)
        return result

    @when(AST.CodeBlock)
    def visit_CodeBlock(self, node):
        self.visit(node.program)






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

