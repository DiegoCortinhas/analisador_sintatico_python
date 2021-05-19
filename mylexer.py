import math
import ply.lex as lex
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from pip._vendor.distlib.compat import raw_input


# Lista com os nomes das tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ELEVATE',
    'PERCENTAGE',
    'FAT',
    'SQRT',
    'LOG'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ELEVATE = r'\^'
t_PERCENTAGE = r'\%'
t_FAT = r'\!'
t_SQRT = r'\√'
t_LOG = r'\&'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Definir os numeros das linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Funcao para ignorar espaços
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Caractere não suportado pela gramatica. '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_elevate(p):
    'expression : expression ELEVATE term'
    p[0] = p[1] ** p[3]


def p_term_percentage(p):
    'term : term PERCENTAGE term'
    p[0] = p[1]/100 * p[3]

def p_term_fat(p):
    'term : term FAT'
    p[0] = math.factorial(p[1])

def p_term_sqrt(p):
    'term : SQRT term'
    p[0] = math.sqrt(p[2])

def p_term_log(p):
    'term : LOG term'
    p[0] = round(math.log(p[2],10),2)

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

#Main
while True:
    try:
        print('Digite a operação desejada:')
        s = raw_input('\ncalculadora > ')
        if s == 'exit':
            print("Saindo da calculadora.")
            break
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

# fazer relatorio - com as percepçoes, duvidas e dificuldades