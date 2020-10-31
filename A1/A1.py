"""
Grammar Extended w/ Lookahead Sets:

prog : {(, x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9} sexp prog
    | {""} ""

sexp : {(} ’(’ exp ’)’
    | {x,y,z} var
    | {0,1,2,3,4,5,6,7,8,9} num

exp : {+} ’+’ sexp sexp
    | {-} ’-’ sexp sexp
    | {*} ’*’ sexp sexp
    | {/} ’/’ sexp sexp
    | {s} ’s’ var sexp
    | {p} ’p’ sexp

var : {x} ’x’ | {y} ’y’ | {z} ’z’

num : {0} ’0’ | {1} ’1’ | {2} ’2’ | {3} ’3’ | {4} ’4’ | {5} ’5’ | {6} ’6’ | {7} ’7’ | {8} ’8’ | {9} ’9’

"""

from grammar_stuff import InputStream

I = None

def set_stream(input_stream):
    global I
    I = input_stream

def prog():
    sym = I.pointer()
    if sym in ['(', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        sexp()
        prog()
        #I.match(')') commented this out because it was giving me errors
    elif sym == "":
        pass
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def sexp():
    sym = I.pointer()
    if sym == '(':
        I.next()
        exp()
        # might need to I.match(')') here
        I.match(')')
    elif sym in ['x', 'y', 'z']:
        var()
    elif sym in ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']:
        num()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def exp():
    sym = I.pointer()
    if sym == '+':
        I.next()
        sexp()
        sexp()
    elif sym == '-':
        I.next()
        sexp()
        sexp()
    elif sym == '*':
        I.next()
        sexp()
        sexp()
    elif sym == '/':
        I.next()
        sexp()
        sexp()
    elif sym == 's':
        I.next()
        var()
        sexp()
    elif sym == 'p':
        I.next()
        sexp()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def var():
    sym = I.pointer()
    if sym == 'x':
        I.next()
    elif sym == 'y':
        I.next()
    elif sym == 'z':
        I.next()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def num():
    sym = I.pointer()
    if sym in ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']:
        I.next()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))
    

    
#example test case

#I = InputStream(['(', 'p','(', '+', '(', '*', '3', '2', ')', '1', ')', ')'])
#I = InputStream(['(', 's', 'x', '1', ')'])
#prog()

