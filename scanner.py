import ply.lex as lex

class Scanner:
    literals = [
    '+', '-', '*', '/', # 1. operatory binarne
    '(', ')', '{', '}', '[', ']', # 5. nawiasy
    ':', "'", ',', ';', # 6, 7, 8
    '=', # 3a. operatory przypisania
    '<', '>' ] # 4a. operatory relacyjne

    tokens = (
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', # 2. macierzowe operatory binarne
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN', # 3b. operatory przypisania
    'LEQ', 'GEQ', 'NEQ', 'EQ', # 4b. operatory relacyjne
    'IF', 'ELSE', 'FOR', 'WHILE', # 9. if, else, for, while
    'BREAK', 'CONTINUE', 'RETURN', # 10. break, continue, return
    'EYE', 'ZEROS', 'ONES', # 11. eye, zeros, ones
    'PRINT', # 12. print
    'ID', 'INTNUM', 'REALNUM', 'STRING', # 13, 14, 15, 16
    #'LEFT_SPAR', 'RIGHT_SPAR' # 5b. nawiasy
    )

    reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
    }

    t_ignore    = ' '

    t_DOTADD    = r'\.\+'
    t_DOTSUB    = r'\.\-'
    t_DOTMUL    = r'\.\*'
    t_DOTDIV    = r'\./'

    t_ADDASSIGN = r'\+='
    t_SUBASSIGN = r'\-='
    t_MULASSIGN = r'\*='
    t_DIVASSIGN = r'/='

    t_LEQ       = r'<='
    t_GEQ       = r'>='
    t_NEQ       = r'!='
    t_EQ        = r'=='

    # t_LEFT_SPAR = r'\['
    # t_RIGHT_SPAR = r'\]'

    def t_COMMENT(self,t):
        r'\#.*'
        pass

    def t_REALNUM(self,t):
        r'[-+]?(((\d+\.\d*)|(\d*\.\d+))([eE][-+]?\d+)?|\d+[eE][-+]?\d+)'
        t.value = float(t.value)
        return t

    def t_INTNUM(self,t):
        r'[-+]?\d+'
        t.value = int(t.value)
        return t

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    def t_STRING(self,t):
        r'".+"' # nie przewidujemy stringów w pojedynczym cudzysłowie, bo byłby konflikt z transpozycją
        return t

    def t_error(self,t):
        print("Line %d: illegal character '%s'" %(t.lineno, t.value[0]))
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, text):
        self.lexer.input(text)
        return

    def token(self):
        return self.lexer.token()

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
