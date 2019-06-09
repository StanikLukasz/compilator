
import AST
import symboltable
from memory import *
import exceptions
from visit import *
import sys
from exceptions import *
import operator
import numpy as np
from copy import deepcopy

sys.setrecursionlimit(10000)

class Interpreter(object):

    def custom_matrix_division(self, left, right):
        return []

    bin_op_function = dict()

    number_comparison_operations = {
        "<" : operator.lt,
        ">": operator.gt,
        "<=": operator.le,
        ">=": operator.ge,
        "==": operator.eq,
        "!=": operator.ne
    }

    number_binary_operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    element_wise_matrix_binary_operations = {
        ".+": np.add,
        ".-": np.subtract,
        ".*": np.multiply,
        "./": np.divide,
    }

    comparison_operations = {
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
        "!=": operator.ne
    }

    unary_operations = {
        "-": operator.neg,
        "'": np.transpose
    }

    functions = {
        'EYE': np.eye,
        'ZEROS': np.zeros,
        'ONES': np.ones
    }

    for op in ['+', '-', '/', '*']:
        bin_op_function[(op, int, int)] = number_binary_operations[op]
        bin_op_function[(op, float, float)] = number_binary_operations[op]
        bin_op_function[(op, int, float)] = number_binary_operations[op]
        bin_op_function[(op, float, int)] = number_binary_operations[op]

    bin_op_function[('/', int, int)] = operator.floordiv

    for op in ['.+', '.-', './', '.*']:
        bin_op_function[(op, list, list)] = element_wise_matrix_binary_operations[op]

    bin_op_function[('*', list, list)] = np.matmul
    bin_op_function[('/', list, list)] = custom_matrix_division
    bin_op_function[('*', int, list)] = np.multiply
    bin_op_function[('*', list, int)] = np.multiply
    bin_op_function[('*', float, list)] = np.multiply
    bin_op_function[('*', list, float)] = np.multiply
    bin_op_function[('/', list, int)] = np.divide
    bin_op_function[('/', list, float)] = np.divide

    def __init__(self):
        self.memory_stack = MemoryStack()

    def check_condition(self, op, left, right):
        comparing_function = self.number_comparison_operations[op]
        return comparing_function(left, right)

# 0. Base Node class

    @on('node')
    def visit(self, node):
        pass

## 1. Initial rules

    @when(AST.Program)
    def visit(self, node):
        #self.visit(node.instruction_lines) - just out of curiosity... why doesn't it want to work
        for instruction in node.instruction_lines:
            instruction.accept(self)


## 2. Statement types

    @when(AST.IfElse)
    def visit(self, node):
        if node.condition.accept(self):
            node.instruction_line.accept(self)
        else:
            if node.else_instruction:
                node.else_instruction.accept(self)

    @when(AST.WhileLoop)
    def visit(self, node):
        while node.condition.accept(self):
            try:
                node.instruction.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break

    @when(AST.ForLoop)
    def visit(self, node):
        for iterator in node.range.accept(self):
            self.memory_stack.insert(node.iterator.name, iterator) #to check
            try:
                node.instruction.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break

    @when(AST.CodeBlock)
    def visit(self, node):
        node.program.accept(self)

# 2.1 Condition statements
    @when(AST.Condition)
    def visit(self, node):
        op = node.op
        left = node.left.accept(self)
        right = node.right.accept(self)
        return self.check_condition(op, left, right)

# 2.2 Values range
    @when(AST.Range)
    def visit(self, node):
        start = node.start_number.accept(self)
        end = node.end_number.accept(self)
        return range(start, end+1)

## 3. Instruction types

    @when(AST.Assignment)
    def visit(self, node):
        right = 0
        left = node.identifier
        if node.op == "=":
            right = node.expression.accept(self)
        elif node.op == "+=":
            right = operator.add(node.identifier.accept(self), node.expression.accept(self))
        elif node.op == "*=":
            right = operator.mul(node.identifier.accept(self), node.expression.accept(self))
        elif node.op == "/=":
            right = operator.truediv(node.identifier.accept(self), node.expression.accept(self))
        elif node.op == "-=":
            right = operator.sub(node.identifier.accept(self), node.expression.accept(self))
        self.memory_stack.insert(left.name, right)

    @when(AST.Print)
    def visit(self, node):
        for element in node.array_line:
            print(element.accept(self))

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.expression.accept(self))

# 3.1 Assignment operators
# no AST classes for this part

## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
    @when(AST.Array)  #TODO
    def visit(self, node):
        array = deepcopy(node.content)
        for row in range(node.rows):
            for column in range(node.columns):
                array[row][column] = array[row][column].accept(self)
        return array

# 4.2 Array special functions
    @when(AST.Function)
    def visit(self, node):
        rows = node.arguments[0].accept(self)
        if len(node.arguments) == 2:
            columns = node.arguments[1].accept(self)
        else:
            columns = rows
        if node.name == "zeros":
            return np.zeros((rows, columns))
        if node.name == "ones":
            return np.ones((rows, columns))
        if node.name == "eye":
            return np.eye(rows)


# 4.3 Array transposition
    @when(AST.Transposition)
    def visit(self, node):
        array =  node.argument.accept(self)
        return np.transpose(array)

# 4.4 Unary negation
    @when(AST.Negation)
    def visit(self, node):
        value = node.expression.accept(self)
        return operator.neg(value)

# 4.5 Binary expressions
    @when(AST.BinExpr)  #TODO
    def visit(self, node):
        op = node.op
        left = node.left.accept(self)
        right = node.right.accept(self)
        left_type = type(left)
        # print("DEBUG:", left_type)
        right_type = type(right)
        # print("DEBUG:", right_type)
        expr_function = self.bin_op_function[(op, left_type, right_type)]
        return expr_function(left, right)

# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.Identifier)
    def visit(self, node):
        name = node.name
        return self.memory_stack.get(name)

    @when(AST.Reference)
    def visit(self, node):
        var = self.memory_stack.get(node.name)
        indicies = node.indicies #doesn't it affect node.indicies itself? even if it does... it's correct
        if len(indicies) == 1: #we don't want it to return the whole vector... or... we might want... but it's a work for TODO
            indicies.append(indicies[0])
            indicies[0] = AST.Integer(0)
        for index in node.indicies:
            var = var[index.accept(self)]
        return var

    @when(AST.Integer)
    def visit(self, node):
        return node.value

    @when(AST.Real)
    def visit(self, node):
        return node.value

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
