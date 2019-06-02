#!/usr/bin/python

import AST


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

# 0. Base Node class

    def visit_Node(self, node):
        pass


## 1. Initial rules

    def visit_Program(self, node):
        pass

    def visit_Empty(self, node):
        pass


## 2. Statement types

    def visit_IfElse(self, node):
        pass

    def visit_WhileLoop(self, node):
        pass

    def visit_ForLoop(self, node):
        pass

    def visit_CodeBlock(self, node):
        pass

# 2.1 Condition statements
    def visit_Condition(self, node):
        pass

# 2.2 Values range
    def visit_Range(self, node):
        pass


## 3. Instruction types

    def visit_Assignment(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_Continue(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Return(self, node):
        pass

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
        pass

# 4.5 Binary expressions
    def visit_BinExpr(self, node):
        # alternative usage,
        # requires definition of accept method in class Node
        type1 = self.visit(node.left)  # type1 = node.left.accept(self)
        type2 = self.visit(node.right)  # type2 = node.right.accept(self)
        op = node.op
        # ...
        #

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
