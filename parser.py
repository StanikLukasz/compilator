#!/usr/bin/python

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
    ("left", '+', '-', "DOTADD", "DOTSUB"),
    ("left", '*', '/', "DOTMUL", "DOTDIV"),
    ("nonassoc", "'")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, s.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instruction_lines
               | empty"""
    p[0] = AST.Program(p[1])

def p_empty(p):
    """empty : """
    #todo what type

def p_instructions(p):
    """instruction_lines : instruction_lines instruction_line
                         | instruction_line"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_instruction_line(p):
    """instruction_line : instruction ';'
                        | if_else
                        | while_loop
                        | for_loop
                        | code_block"""
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
    """for_loop : FOR ID '=' range instruction_line"""

def p_code_block(p):
    """code_block : '{' program '}' """

def p_instruction(p):
    """instruction : assignment
                   | printing
                   | CONTINUE
                   | BREAK
                   | returning"""
    p[0] = p[1]


# INSTRUCTION TYPES

def p_assignment(p):
    """assignment : identifier assignment_op expression"""
    p[0] = AST.Assignment(p[2], p[1], p[3])

def p_printing(p):
    """printing : PRINT array_line"""

def p_returning(p):
    """returning : RETURN expression"""


# ASSIGNMENT OPEARATORS

def p_assignment_op(p):
    """assignment_op : '='
                     | ADDASSIGN
                     | SUBASSIGN
                     | MULASSIGN
                     | DIVASSIGN"""


# CONDITION FOR "WHILE" AND "IF" CONSTRUCTIONS

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
    p[0] = AST.String(p[1])


# NEEDED FOR LOOPS AND "IF" STATEMENT

def p_range(p):
    """range : id_or_number ':' id_or_number""" # what about strings?


# EXPRESSION DEFINITION

def p_expression(p):
    """expression : expression_binary
                  | array
                  | elementary
                  | array_special
                  | negation
                  | transposition
                  | expression_group"""
    p[0] = p[1]


# ARRAY DEFINITION

def p_array(p):
    """array : '[' array_lines ']' """

def p_array_lines(p):
    """array_lines : array_lines ';' array_line
                   | array_line"""

def p_array_line(p):
    """array_line : array_line ',' expression
                  | expression"""


# ARRAY SPECIAL

def p_array_special(p):
    """array_special : ZEROS array_special_specifier
                     | ONES array_special_specifier
                     | EYE array_special_specifier """

def p_array_special_specifier(p):
    """array_special_specifier : '(' id_or_number ')'"""

def p_transposition(p):
    """transposition : ID "'"
                     | array "'" """


# NEGATION

def p_negation(p):
    """negation : '-' expression"""


# ELEMTARY TYPES

def p_elementary(p):
    """elementary : id_or_number
                  | STRING"""
    p[0] = AST.String(p[1])

def p_id_or_number(p):
    """id_or_number : identifier
                    | number"""
    p[0] = p[1]

def p_identifier(p):
    """identifier : ID '[' array_line ']'
                  | ID"""
    if len(p) == 2:
        p[0] = p[1]

def p_number(p):
    """number : INTNUM
              | REALNUM"""


# BINARY EXPRESSIONS

def p_expression_binary(p):
    """expression_binary : normal_binary_expression
                         | dot_binary_expression"""

def p_normal_binary_expression(p):
    """normal_binary_expression : add_expression
                                | sub_expression
                                | mul_expression
                                | div_expression"""

def p_dot_binary_expression(p):
    """dot_binary_expression : dot_add_expression
                             | dot_sub_expression
                             | dot_mul_expression
                             | dot_div_expression"""

def p_add_expression(p):
    """add_expression : expression '+' expression"""

def p_sub_expression(p):
    """sub_expression : expression '-' expression"""

def p_mul_expression(p):
    """mul_expression : expression '*' expression"""

def p_div_expression(p):
    """div_expression : expression '/' expression"""

def p_dot_add_expression(p):
    """dot_add_expression : expression DOTADD expression"""

def p_dot_sub_expression(p):
    """dot_sub_expression : expression DOTSUB expression"""

def p_dot_mul_expression(p):
    """dot_mul_expression : expression DOTMUL expression"""

def p_dot_div_expression(p):
    """dot_div_expression : expression DOTDIV expression"""

# PARENTHESIS

def p_expression_group(p):
    """expression_group : '(' expression ')' """

parser = yacc.yacc()
