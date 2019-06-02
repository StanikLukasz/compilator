
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



    @on('node')
    def visit(self, node):
        pass

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

