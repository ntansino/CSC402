from ply import lex

reserved = {
    'push' : 'PUSHNUM',
    'push' : 'PUSHNAME',
    'pop' : 'POP',
    'print' : 'PRINT',
    'store' : 'STORE',
    'ask' : 'ASK',
    'dup' : 'DUP',
    'add' : 'ADD',
    'sub' : 'SUB',
    'mul' : 'MUL',
    'div' : 'DIV',
    'equ' : 'EQU',
    'leq' : 'LEQ',
    'jumpT' : 'JUMPT',
    'jumpF' : 'JUMPF',
    'jump'  : 'JUMP',
    'stop'  : 'STOP',
    'noop'  : 'NOOP'
}

literals = [':',';','+','-','*','/','(',')']

tokens = ['NAME','NUMBER','MSG','LABEL'] + list(reserved.values())

t_ignore = ' \t'

def t_NAME(t):
    r'[a-zA-Z_$][a-zA-Z_$0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n'
    pass

def t_COMMENT(t):
    r'//.*'
    pass

def t_MSG(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t
    
def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)