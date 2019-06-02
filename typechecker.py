#!/usr/bin/python

import AST
import symboltable

class Vector(object):
    def __init__(self, size):
        self.size = size

op_and_type_map = dict()

for op in ['+', '-', '/', '*', '+=', '-=', '*=', '/=']:
    op_and_type_map[(op, 'int', 'int')] = 'int'
    op_and_type_map[(op, 'float', 'float')] = 'float'
    op_and_type_map[(op, 'int', 'float')] = 'float'
    op_and_type_map[(op, 'float', 'int')] = 'float'

for op in ['>', '<', '==', '!=', '>=', '<=']:
    op_and_type_map[(op, 'int', 'int')] = 'int'
    op_and_type_map[(op, 'float', 'float')] = 'int'
    op_and_type_map[(op, 'int', 'float')] = 'int'
    op_and_type_map[(op, 'float', 'int')] = 'int'

for op in ['.+', '.-', './', '.*']:
    op_and_type_map[(op, Vector.__name__, Vector.__name__)] = Vector.__name__



class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit) # visitor = self.method - default = self.generic_visit
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.scope = symboltable.SymbolTable(None, "Main")

# 0. Base Node class

    def visit_Node(self, node):
        pass


## 1. Initial rules

    def visit_Program(self, node):
        self.visit(node.instruction_lines)

    def visit_Empty(self, node):
        pass


## 2. Statement types

    def visit_IfElse(self, node):
        self.visit(node.condition)
        self.scope = self.scope.push_scope('If')
        self.visit(node.instruction_line)
        self.scope = self.scope.pop_scope()
        if node.else_instruction:
            self.scope = self.scope.push_scope('Else')
            self.visit(node.else_instruction)
            self.scope = self.scope.pop_scope()

    def visit_WhileLoop(self, node):
        self.visit(node.condition)
        self.scope = self.scope.push_scope('WhileLoop')
        self.visit(node.instruction)
        self.scope = self.scope.pop_scope()

    def visit_ForLoop(self, node):
        range = self.visit(node.range)
        self.scope = self.scope.push_scope('ForLoop')
        self.scope.put(node.iterator, range)
        self.visit(node.instruction)
        self.scope = self.scope.pop_scope()

    def visit_CodeBlock(self, node):
        self.scope = self.scope.push_scope('CodeBlock')
        self.visit(node.program)
        self.scope = self.scope.pop_scope()

# 2.1 Condition statements
    def visit_Condition(self, node):
        pass

# 2.2 Values range
    def visit_Range(self, node):
        start_number = self.visit(node.start_number)
        end_number = self.visit(node.end_number)

        if start_number >= end_number:
            print('cos wyebalo w reange parameter')
        return start_number


## 3. Instruction types

    def visit_Assignment(self, node):
        _left = node.identifier
        _right = node.expression
        _op = node.op
        if isinstance(_right, AST.Identifier):
            if _right.name not in self.scope.symbols.keys():
                print('niezainicjalizowany Identifier')
        elif isinstance(_right, AST.Reference):
            if _right.id not in self.scope.symbols.keys():
                print('niezainicjalizowany Reference')
        else:
            print(_left)
            self.scope.symbols[_left] = _right

    def visit_Print(self, node):
        self.visit(node.array_line)

    def visit_Continue(self, node):
        scopes = self.get_scopes()
        if 'WhileLoop' not in scopes and 'ForLoop' not in scopes:
            print('Continue not in WhileLoop or ForLoop scope')

    def visit_Break(self, node):
        scopes = self.get_scopes()
        if 'WhileLoop' not in scopes and 'ForLoop' not in scopes:
            print('Break not in WhileLoop or ForLoop scope')

    def visit_Return(self, node):
        scopes = self.get_scopes()
        if 'Program' not in scopes:
            print('Return not in Program scope')

# 3.1 Assignment operators
# no AST classes for this part


## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
    def visit_Array(self, node):
        pass

# 4.2 Array special functions
    def visit_Function(self, node):
        pass

# 4.3 Array transposition
    def visit_Transposition(self, node):
        pass

# 4.4 Unary negation
    def visit_Negation(self, node):
        return node.expression

# 4.5 Binary expressions
    def visit_BinExpr(self, node):
        result = {}
        right = self.visit(node.left)  # type1 = node.left.accept(self)
        left = self.visit(node.right)  # type2 = node.right.accept(self)
        right_type = right.get('type')
        left_type = left.get('type')
        op = node.op
        key = (op, left_type, right_type)
        if key not in op_and_type_map.key():
            print('niewspierana operacja badz typ')
        elif left_type is 'Vector' and right_type is 'Vector':
            dim1 = right.get('size')
            dim2 = left.get('size')
            if dim1 and dim2:
                if len(dim1) is not len(dim2):
                   print('ew')
                elif op is './' or op is '.*':
                    if dim1[1] is not dim2[0]:
                        print('incompatibile dims')
                    else:
                        result['size'] = [dim1[0], dim2[1]]
                else:
                    if not dim1 == dim2:
                        print('incompatibile dims')
            else:
                print("incompatible types line")
        else:
            result['type'] = op_and_type_map[(op, left_type, right_type)]
        return result

# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
    def visit_String(self, node):
        pass

    def visit_Identifier(self, node):
        pass

    def visit_Reference(self, node):
        pass

    def visit_Integer(self, node):
        pass

    def visit_Real(self, node):
        pass


# X. Error raising

    def visit_Error(self, node):
        pass

    def get_scopes(self):
        scopes = []
        parent = self.scope
        while parent:
            scopes.append(parent.name)
            parent = parent.parent
        return scopes
