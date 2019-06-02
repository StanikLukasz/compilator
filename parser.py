#!/usr/bin/python

## Table of contents
#
# Error handling
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
# Parser building

import scanner
import ply.yacc as yacc
import AST

s = scanner.Scanner()

literals = s.literals
tokens = list(s.tokens) + literals

precedence = (
    ("left", "IF"),
    ("left", "ELSE"),
    ("nonassoc", '=', "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
    ("nonassoc", '<', '>', "EQ", "NEQ", "LEQ", "GEQ"),
    ("left", 'PLUS', 'MINUS', "DOTADD", "DOTSUB"),
    ("left", '*', '/', "DOTMUL", "DOTDIV"),
    ("nonassoc", "'")
)

# Error handling
def p_error(p):
    if p:
        raise ValueError("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, s.find_tok_column(p), p.type, p.value))
    else:
        raise EOFError("Unexpected end of input")


## 1. Initial rules
def p_program(p):
    """program : instruction_lines
               | empty"""
    p[0] = AST.Program(p[1])

def p_empty(p):
    """empty : """
    p[0] = AST.Empty()

def p_instructions(p):
    """instruction_lines : instruction_lines instruction_line
                         | instruction_line"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


## 2. Statement types
def p_instruction_line(p):
    """instruction_line : if_else
                        | while_loop
                        | for_loop
                        | code_block
                        | instruction ';'"""
    p[0] = p[1]

def p_if_else(p):
    """if_else : IF condition instruction_line
               | IF condition instruction_line ELSE instruction_line"""
    if len(p) == 4:
        p[0] = AST.IfElse(p[2], p[3])
    else:
        p[0] = AST.IfElse(p[2], p[3], p[5])

def p_while_loop(p):
    """while_loop : WHILE condition instruction_line"""
    p[0] = AST.WhileLoop(p[2], p[3])

def p_for_loop(p):
    """for_loop : FOR identifier '=' range instruction_line"""
    p[0] = AST.ForLoop(p[2], p[4], p[5])

def p_code_block(p):
    """code_block : '{' program '}' """
    p[0] = AST.CodeBlock(p[2])

# 2.1 Condition statements
def p_condition(p):
    """condition : '(' bool_expression ')'"""
    p[0] = p[2]

def p_bool_expression(p):
    """bool_expression : expression comparison_op expression"""
    p[0] = AST.Condition(p[2], p[1], p[3])

def p_comparison_op(p):
    """comparison_op : '<'
                     | '>'
                     | EQ
                     | NEQ
                     | GEQ
                     | LEQ"""
    p[0] = p[1]

# 2.2 Values range
def p_range(p):
    """range : id_or_number ':' id_or_number"""
    p[0] = AST.Range(p[1], p[3])


## 3. Instruction types

def p_instruction(p):
    """instruction : assignment
                   | printing
                   | continue_statement
                   | break_statement
                   | returning"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : identifier assignment_op expression"""
    p[0] = AST.Assignment(p[2], p[1], p[3])

def p_printing(p):
    """printing : PRINT array_line"""
    p[0] = AST.Print(p[2])

def p_continue_statement(p):
    """continue_statement : CONTINUE"""
    p[0] = AST.Continue()

def p_break_statement(p):
    """break_statement : BREAK"""
    p[0] = AST.Break()

def p_returning(p):
    """returning : RETURN expression"""
    p[0] = AST.Return(p[2])

# 3.1 Assignment operators
def p_assignment_op(p):
    """assignment_op : '='
                     | ADDASSIGN
                     | SUBASSIGN
                     | MULASSIGN
                     | DIVASSIGN"""
    p[0] = p[1]


## 4. Expressions

def p_expression(p):
    """expression : expression_binary
                  | array
                  | array_special
                  | transposition
                  | negation
                  | expression_group
                  | elementary"""
    p[0] = p[1]


# 4.1 Array definition (and array lines used in other structures)
def p_array(p):
    """array : '[' array_lines ']' """
    p[0] = AST.Array(p[2])

def p_array_lines(p):
    """array_lines : array_lines ';' array_line
                   | array_line"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_array_line(p):
    """array_line : array_line ',' expression
                  | expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# 4.2 Array special functions
def p_array_special(p):
    """array_special : ZEROS array_special_specifier
                     | ONES array_special_specifier
                     | EYE array_special_specifier """
    p[0] = AST.Function(p[1], p[2])

def p_array_special_specifier(p):
    """array_special_specifier : '(' id_or_number ')'
                               | '(' id_or_number ',' id_or_number ')'"""
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2], p[4]]

# 4.3 Array transposition
def p_transposition(p):
    """transposition : identifier "'"
                     | array "'" """
    p[0] = AST.Transposition(p[1])

# 4.4 Unary negation
def p_negation(p):
    """negation : MINUS expression"""
    p[0] = AST.Negation(p[2])

# 4.5 Binary expressions
def p_expression_binary(p):
    """expression_binary : normal_binary_expression
                         | dot_binary_expression"""
    p[0] = p[1]

def p_normal_binary_expression(p):
    """normal_binary_expression : add_expression
                                | sub_expression
                                | mul_expression
                                | div_expression"""
    p[0] = p[1]

def p_dot_binary_expression(p):
    """dot_binary_expression : dot_add_expression
                             | dot_sub_expression
                             | dot_mul_expression
                             | dot_div_expression"""
    p[0] = p[1]

def p_add_expression(p):
    """add_expression : expression PLUS expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_sub_expression(p):
    """sub_expression : expression MINUS expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_mul_expression(p):
    """mul_expression : expression '*' expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_div_expression(p):
    """div_expression : expression '/' expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_dot_add_expression(p):
    """dot_add_expression : expression DOTADD expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_dot_sub_expression(p):
    """dot_sub_expression : expression DOTSUB expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_dot_mul_expression(p):
    """dot_mul_expression : expression DOTMUL expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_dot_div_expression(p):
    """dot_div_expression : expression DOTDIV expression"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

# 4.6 Expressions in parenthesis
def p_expression_group(p):
    """expression_group : '(' expression ')' """
    p[0] = p[1]

# 4.7 Elementary types
def p_elementary(p):
    """elementary : id_or_number
                  | text"""
    p[0] = p[1]

def p_text(p):
    """text : STRING"""
    p[0] = AST.String(p[1])

def p_id_or_number(p):
    """id_or_number : identifier
                    | number"""
    p[0] = p[1]

def p_identifier(p):
    """identifier : ID '[' array_line ']'
                  | ID"""
    if len(p) == 2:
        p[0] = AST.Identifier(p[1])
    else:
        p[0] = AST.Reference(p[1], p[3])

def p_number(p):
    """number : integer
              | real"""
    p[0] = p[1]

def p_integer(p):
    """integer : INTNUM"""
    p[0] = AST.Integer(p[1])

def p_real(p):
    """real : REALNUM"""
    p[0] = AST.Real(p[1])

# Parser building
parser = yacc.yacc()
