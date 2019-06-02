## Table of contents
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


## 0. Base Node class

class Node(object):
    def __init__(self):
        self.line = 0
        self.column = 0


## 1. Initial rules

class Program(Node):
    def __init__(self, instruction_lines):
        self.instruction_lines = instruction_lines

class Empty(Node):
    def __init__(self):
        pass


## 2. Statement types

class IfElse(Node):
    def __init__(self, condition, instruction_line, else_instruction=None):
        self.condition = condition
        self.instruction_line = instruction_line
        self.else_instruction = else_instruction

class WhileLoop(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class ForLoop(Node):
    def __init__(self, iterator, range, instruction):
        self.iterator = iterator
        self.range = range
        self.instruction = instruction

class CodeBlock(Node):
    def __init__(self, program):
        self.program = program

# 2.1 Condition statements
class Condition(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

# 2.2 Values range
class Range(Node):
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number


## 3. Instruction types

class Assignment(Node):
    def __init__(self, op, identifier, expression):
        self.op = op
        self.identifier = identifier
        self.expression = expression

class Print(Node):
    def __init__(self, array_line):
        self.array_line = array_line

class Continue(Node):
    def __init__(self):
        pass

class Break(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(self, expression):
        self.expression = expression

# 3.1 Assignment operators
# no AST classes for this part


## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
class Array(Node):
    def __init__(self, content):
        self.content = content

# 4.2 Array special functions
class Function(Node):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

# 4.3 Array transposition
class Transposition(Node):
    def __init__(self, argument):
        self.argument = argument

# 4.4 Unary negation
class Negation(Node):
    def __init__(self, expression):
        self.expression = expression

# 4.5 Binary expressions
class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
class String(Node):
    def __init__(self, content):
        self.content = content

class Identifier(Node):
    def __init__(self, name):
        self.name = name

class Reference(Node):
    def __init__(self, id, indicies):
        self.id = id
        self.indicies = indicies

class Integer(Node):
    def __init__(self, value):
        self.value = value

class Real(Node):
    def __init__(self, value):
        self.value = value


# X. Error raising

class Error(Node):
    def __init__(self):
        pass
