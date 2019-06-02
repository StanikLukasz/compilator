class Node(object):
    def __init__(self):
        self.line = 0
        self.column = 0

class Integer(Node):
    def __init__(self, value):
        self.value = value

class Real(Node):
    def __init__(self, value):
        self.value = value

class Identifier(Node):
    def __init__(self, name, indicies=None):
        self.name = name
        self.indicies = indicies

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Program(Node):
    def __init__(self, instruction_lines):
        self.instruction_lines = instruction_lines

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

class Condition(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class String(Node):
    def __init__(self, content):
        self.content = content

class Assignment(Node):
    def __init__(self, op, identifier, expression):
        self.op = op
        self.identifier = identifier
        self.expression = expression

class Printing(Node):
    def __init__(self, array_line):
        self.array_line = array_line

class Returning(Node):
    def __init__(self, expression):
        self.expression = expression

class Range(Node):
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

class Continue(Node):
    def __init__(self):
        pass

class Break(Node):
    def __init__(self):
        pass

class Negation(Node):
    def __init__(self, expression):
        self.expression = expression

class Transposition(Node):
    def __init__(self, array):
        self.array = array





# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
