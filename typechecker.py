#!/usr/bin/python

import AST
import symboltable

from copy import deepcopy

class Vector(object):
    def __init__(self, size):
        self.size = size

bin_op_result = dict()

for op in ['+', '-', '/', '*', '+=', '-=', '*=', '/=']:
    bin_op_result[(op, AST.Integer, AST.Integer)] = AST.Integer
    bin_op_result[(op, AST.Real, AST.Real)] = AST.Real
    bin_op_result[(op, AST.Integer, AST.Real)] = AST.Real
    bin_op_result[(op, AST.Real, AST.Integer)] = AST.Real

for op in ['>', '<', '==', '!=', '>=', '<=']:
    bin_op_result[(op, AST.Integer, AST.Integer)] = AST.Integer
    bin_op_result[(op, AST.Real, AST.Real)] = AST.Integer
    bin_op_result[(op, AST.Integer, AST.Real)] = AST.Integer
    bin_op_result[(op, AST.Real, AST.Integer)] = AST.Integer

for op in ['.+', '.-', './', '.*']:
    bin_op_result[(op, AST.Array, AST.Array)] = AST.Array

    bin_op_result[('*', AST.Array, AST.Array)] = AST.Array
    bin_op_result[('/', AST.Array, AST.Array)] = AST.Array
    bin_op_result[('*=', AST.Array, AST.Array)] = AST.Array
    bin_op_result[('/=', AST.Array, AST.Array)] = AST.Array
    bin_op_result[('*', AST.Integer, AST.Array)] = AST.Array
    bin_op_result[('*', AST.Array, AST.Integer)] = AST.Array
    bin_op_result[('*', AST.Real, AST.Array)] = AST.Array
    bin_op_result[('*', AST.Array, AST.Real)] = AST.Array
    bin_op_result[('/', AST.Array, AST.Integer)] = AST.Array
    bin_op_result[('/', AST.Array, AST.Real)] = AST.Array


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
        _id = node.identifier
        _value = node.expression
        _op = node.op
        if not isinstance(_id, AST.Variable):
            print('Semantic error at line {}: Cannot assign to something what is not a variable'.format(node.line))
            try:
                _id = self.visit(_id)
            except:
                _id = None
        try:
            _value = self.visit(_value)
        except TypeError:
            #print("DEBUG: TypeError raised while visiting _value".format(node.line))
            return
        if _value == None:
            print("Pan Koloczek")
        if isinstance(_value, AST.Variable):
            if _value.name not in self.scope.symbols.keys():
                print('Semantic error at line {}: Identifier/Reference used before initialization'.format(node.line))
                return
        if isinstance(_id, AST.Variable) and isinstance(_value, AST.Value):
                self.scope.put(_id.name, _value)
               # print('DEBUG: self.scope.put({},{})'.format(_id.name, _value))
        elif isinstance(_id, AST.Variable) and isinstance(_value, AST.Array):
                self.scope.put(_id.name, _value)
               # print('DEBUG: self.scope.put({},{})'.format(_id.name, _value))

    def visit_Print(self, node):
        self.visit(node.array_line)

    def visit_Continue(self, node):
        scopes = self.get_scopes()
        if 'WhileLoop' not in scopes and 'ForLoop' not in scopes:
            print('Semantic error at line {}: Continue not in WhileLoop or ForLoop scope'.format(node.line))

    def visit_Break(self, node):
        scopes = self.get_scopes()
        if 'WhileLoop' not in scopes and 'ForLoop' not in scopes:
            print('Semantic error at line {}: Break not in WhileLoop or ForLoop scope'.format(node.line))

    def visit_Return(self, node):
        scopes = self.get_scopes()
        if 'Program' not in scopes:
            print('Semantic error at line {}: Return not in Program scope'.format(node.line))

# 3.1 Assignment operators
# no AST classes for this part


## 4. Expressions

# 4.1 Array definition (and array lines used in other structures)
    def visit_Array(self, node): #todo: check if we don't have unassigned variables inside
        row_size = len(node.content[0])
        for vector in node.content[1:]:
            if len(vector) != row_size:
                print('Semantic error at line {}: Incompatible row sizes in array'.format(node.line))
                raise TypeError
        return node

# 4.2 Array special functions
    def visit_Function(self, node):
        rows = node.arguments[0].value
        if len(node.arguments) == 2:
            columns = node.arguments[1].value
        else:
            columns = rows
        row = [AST.Integer(None)] * columns
        array = [row] * rows
        if (node.name == "zeros"):
            # print("DEBUG: created an array of zeros [{},{}]".format(rows, columns))
            return AST.Array(array, rows, columns)
        if (node.name == "ones"):
            # print("DEBUG: created an array of ones [{},{}]".format(rows, columns))
            return AST.Array(array, rows, columns)
        if (node.name == "eye"):
            # print("DEBUG: created an eye array [{},{}]".format(rows, columns))
            return AST.Array(array, rows, columns)
        print('Semantic error at line {}: Unknown function used'.format(node.line))

# 4.3 Array transposition
    def visit_Transposition(self, node):
        argument = node.argument
        argument = self.visit(argument)
        if not isinstance(argument, AST.Array): #todo and not isinstance(_expression, AST.Array):
            print('Semantic error at line {}: Cannot transpose anything else than array'.format(node.line))
            raise TypeError
        argument.rows, argument.columns = argument.columns, argument.rows
        return node.argument

# 4.4 Unary negation
    def visit_Negation(self, node):
        _expression = node.expression
        self.visit(_expression)
        if not isinstance(_expression, AST.Number): #todo and not isinstance(_expression, AST.Array):
            print('Semantic error at line {}:s Cannot negate anything else than number'.format(node.line))
            raise TypeError
        node.expression.value = -node.expression.value
        return node.expression

# 4.5 Binary expressions
    def visit_BinExpr(self, node): #todo: dzielenie przez zero
        result = {}
        left = self.visit(node.left)
        right = self.visit(node.right)
        left_type = type(left)
        right_type = type(right)
        op = node.op
        # print("DEBUG: ", left_type, op, right_type)
        op_left_right = (op, left_type, right_type)
        if op_left_right not in bin_op_result.keys():
            print('Semantic error at line {}: Operation {} not supported between operands of types {} and {}'.format(node.line, op, left_type, right_type))
            raise TypeError
        elif left_type == AST.Array and right_type == AST.Array:
            if op in ('.+', '.-', '.*', './'):
                if left.rows != right.rows or left.columns != right.columns:
                    print('Semantic error at line {}: Operation {} needs arrays of the same sizes. Given array 1: [{}x{}], array 2: [{}x{}]'.format(node.line, op, left.rows, left.columns, right.rows, right.columns))
                    raise TypeError
                return AST.Array(None, left.rows, right.rows)
            if op == '*':
                if left.columns != right.rows:
                    print('Semantic error at line {}: Operation {} needs arrays sizes [axb] and [bxc]. Given array 1: [{}x{}], array 2: [{}x{}]'.format(node.line, op, left.rows, left.columns, right.rows, right.columns))
                    raise TypeError
                return AST.Array(None, left.rows, right.columns)
        elif left_type == AST.Array and right_type in (AST.Integer, AST.Real):
            return AST.Array(None, left.rows, left.columns)
        elif left_type in (AST.Integer, AST.Real) and right_type == AST.Array:
            return AST.Array(None, right.rows, right.columns)
        else:
            result_type = bin_op_result[op_left_right]
            if result_type == AST.Integer:
                return AST.Integer(None)
            elif result_type == AST.Real:
                return AST.Real(None)


# 4.6 Expressions in parenthesis
# no AST classes for this part

# 4.7 Elementary types
    def visit_String(self, node):
        return node

    def visit_Identifier(self, node):
        variable = self.scope.symbols.get(node.name)
        return variable

    def visit_Reference(self, node):
        for index in node.indicies:
            self.visit(index)
        variable = self.scope.symbols.get(node.name)
        if not variable:
            print('Semantic error at line {}: Identifier/Reference used before initialization'.format(node.line))
            raise TypeError

        if not isinstance(variable, AST.Array):
            print('Semantic error at line {}: Referenced to something what is not an array'.format(node.line))
            raise TypeError

        array_depth = 0
        array = deepcopy(variable)
        while isinstance(array.content, list):
            array.content = array.content[0]
            array_depth = array_depth + 1

        if len(node.indicies) == 1:
            if variable.rows != 1:
                print('Semantic error at line {}: Referenced to a {}-dimensional array with {} indicies'.format(node.line, array_depth, len(node.indicies)))
                raise TypeError
            try:
                row_vector = variable.content[0]
                referenced_element = row_vector[node.indicies[0].value]
                return referenced_element
            except IndexError:
                print('Semantic error at line {}: Referenced index {} of an array of size {}'.format(node.line, node.indicies[0].value, variable.columns))
                raise TypeError
        elif len(node.indicies) == 2 and node.indicies[0] != 0:
            if variable.rows < 2:
                print('Semantic error at line {}: Referenced to a {}-dimensional array with {} indicies'.format(node.line, array_depth, len(node.indicies)))
                raise TypeError
            try:
                row_vector = variable.content[node.indicies[0].value]
                referenced_element = row_vector[node.indicies[1].value]
                return referenced_element
            except IndexError:
                print('Semantic error at line {}: Referenced index [{},{}] of an array of size [{},{}]'.format(node.line, node.indicies[0].value, node.indicies[1].value, variable.rows, variable.columns))
                raise TypeError
        elif len(node.indicies) != array_depth:
            print('Semantic error at line {}: Referenced to a {}-dimensional array with {} indicies'.format(node.line, array_depth, len(node.indicies)))
            raise TypeError

    def visit_Integer(self, node):
        return node

    def visit_Real(self, node):
        return node


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
