from ply import yacc
from A4lex import tokens, lexer
from exp1bytecode_interp_state import state

def p_prog(_):
    '''
    prog : instr_list
    '''
    pass

def p_instr_list(_):
    '''
    instr_list : labeled_instr instr_list
              | empty
    '''
    pass

def p_labeled_instr(p):
    '''
    labeled_instr : label_def instr
    '''
    # if label exists record it in the label table
    if p[1]:
        state.label_table[p[1]] = state.instr_ix
    # append instr to program
    state.program.append(p[2])
    state.instr_ix += 1

def p_label_def(p):
    '''
    label_def : NAME ':' 
              | empty
    '''
    p[0] = p[1]

def p_instr(p):
    '''
    instr : PUSH NUMBER ';'
          | PUSH NAME ';'
          | POP ';'
          | PRINT MSG ';'
          | STORE NAME exp ';'
          | ASK MSG ';'
          | DUP ';'
          | ADD ';'
          | SUB ';'
          | MUL ';'
          | DIV ';'
          | EQU ';'
          | LEQ ';'
          | JUMPT exp label ';'
          | JUMPF exp label ';'
          | JUMP label ';'
          | STOP ';'
          | NOOP ';'
    '''
    # for each instr assemble the appropriate tuple
    if p[1] == 'push' and p[2].isnumeric():
        p[0] = ('push', p[2])
        
    elif p[1] == 'push' and p[2].isalpha():
        p[0] = ('push', p[2])
        
    elif p[1] == 'pop':
        p[0] = ('pop', p[2])
        
    elif p[1] == 'print':
        p[0] = ('print', p[2])
        
    elif p[1] == 'store':
        p[0] = ('store', p[2], p[3])
        
    elif p[1] == 'ask':
        p[0] = ('ask', p[2])
        
    elif p[1] == ('dup'):
        p[0] = ('dup', p[2])
        
    elif p[1] == 'add':
        p[0] = ('add', p[2])
        
    elif p[1] == 'sub':
        p[0] = ('sub', p[2])
        
    elif p[1] == 'mul':
        p[0] = ('mul', p[2])
        
    elif p[1] == 'div':
        p[0] = ('div', p[2])
        
    elif p[1] == 'equ':
        p[0] = ('equ', p[2])
        
    elif p[1] == 'leq':
        p[0] = ('leq', p[2])
        
    elif p[1] == 'jumpT':
        p[0] = ('jumpT', p[2], p[3])
        
    elif p[1] == 'jumpF':
        p[0] = ('jumpF', p[2], p[3])
        
    elif p[1] == 'jump':
        p[0] = ('jump', p[2])
        
    elif p[1] == 'stop':
        p[0] = ('stop',)
        
    elif p[1] == 'noop':
        p[0] = ('noop',)
        
    else:
        raise ValueError("Unexpected instr value: %s" % p[1])

def p_label(p):
    '''
        label : NAME
        '''
    p[0] = p[1]

def p_bin_exp(p):
    '''
    exp : '+' exp exp
        | '-' exp exp
        | '*' exp exp
        | '/' exp exp
    '''
    p[0] = (p[1], p[2], p[3])
    
def p_uminus_exp(p):
    '''
    exp : '-' exp
    '''
    p[0] = ('UMINUS', p[2])
    
# don't think we need this
def p_not_exp(p):
    '''
    exp : '!' exp
    '''
    p[0] = ('!', p[2])
    
def p_paren_exp(p):
    '''
    exp : '(' exp ')'
    '''
    # parens are not necessary in trees
    p[0] = p[2]
    
def p_var_exp(p):
    '''
    exp : NAME
    '''
    p[0] = ('NAME', p[1])

def p_number_exp(p):
    '''
    exp : NUMBER
    '''
    p[0] = ('NUMBER', int(p[1]))

def p_empty(p):
    '''
    empty :
    '''
    p[0] = ''

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc(debug=False, tabmodule='exp1bytecodeparsetab')