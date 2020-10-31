from ply import yacc
from ulisp_lex import tokens, lexer
    
def p_prog(_):
    """
    prog : sexp prog
    """
    global count
    count += 1
    pass
    
def p_prog_empty(_):
    'prog : empty'
    pass
    
def p_sexp(_):
    """
    sexp : '(' exp ')'
        | var
        | num
    """
    pass
    
def p_exp(_):
    """    
    exp : '+' sexp sexp
        | '-' sexp sexp
        | '*' sexp sexp
        | '/' sexp sexp
        | 's' var sexp
        | 'p' sexp
    """
    pass
        
def p_var(_):
    """
    var : 'x'
        | 'y'
        | 'z'
    """
    pass
        
def p_num(_):
    """
    num : '0'
        | '1'
        | '2'
        | '3'
        | '4'
        | '5'
        | '6'
        | '7'
        | '8'
        | '9'
    """
    pass

def p_empty(p):
    'empty :'
    print("count = {}".format(count))
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc(debug=False,tabmodule='exp0parsetab')