from A3gram import parser

def A3_interp(input_stream = None):
    'A driver for our LR Exp1 interpreter.'
    
    if not input_stream:
        input_stream = input("exp1 > ")
    
    parser.parse(input_stream)
