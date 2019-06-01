class Node(object):
    def __init__(self):
        self.line = 0
        self.column = 0

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name):
        self.name = name

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
    def __init__(self, condition, instruction_line):
        self.condition = condition
        self.instruction = instruction_line

class Condition(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
