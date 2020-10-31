from ply import yacc
from A3lex import tokens, lexer

symbol_table = dict()

def p_prog(_):
    "prog : stmt_list"
    pass

def p_stmt_list(_):
    """
    stmt_list : stmt stmt_list
              | empty
    """
    pass

def p_print_stmt(p):
    "stmt : PRINT exp ';'"
    print("> {}".format(p[2]))
    
def p_store_stmt(p):
    "stmt : STORE NAME exp ';'"
    symbol_table[p[2]] = p[3]

def p_plus_exp(p):
    """
    exp : '+' exp exp
    """
    p[0] = p[2] + p[3]

def p_minus_exp(p):
    """
    exp : '-' exp exp
    """
    p[0] = p[2] - p[3]
    
def p_mult_exp(p):
    """
    exp : '*' exp exp
    """
    p[0] = p[2] * p[3]
    
def p_div_exp(p):
    """
    exp : '/' exp exp
    """
    p[0] = p[2] // p[3]
    p[0] = int(p[0])

def p_paren_exp(p):
    """
    exp : '(' exp ')'
    """
    p[0] = p[2]

def p_var_exp(p):
    "exp : var"
    p[0] = p[1]
    
def p_num_exp(p):
    "exp : num"
    p[0] = p[1]

def p_var(p):
    "var : NAME"
    p[0] = symbol_table.get(p[1], 0)

def p_num(p):
    "num : NUMBER"
    p[0] = p[1]

def p_empty(p):
    "empty :"
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc(debug=False, tabmodule='exp1parsetab')