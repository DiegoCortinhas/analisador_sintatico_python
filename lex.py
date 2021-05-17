import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




def main():

    while True:
        try:
            valor_entrada1 = input('\nDigite o primeiro valor de entrada: ')
            valor_entrada2 = input('\nDigite o segundo valor de entrada: ')
            # Build the lexer
            lexer1 = lex.lex()
            lexer2 = lex.lex()
            lexer1.input(valor_entrada1)
            lexer2.input(valor_entrada2)
            token1 = lexer1.token()
            token2 = lexer2.token()

            if not token1 or not token2:
                break  # No more input
            # print(tok.type, tok.value, tok.lineno, tok.lexpos)
            print(token1.type, token1.value)
            print(token2.type, token2.value)

        except ValueError:
            print("Valor de entrada precisa ser um numero")
            continue
        except EOFError:
            break

        # data = '''
        #     3 + 4 * 10
        #       + -20 *2 p
        #     '''

    # Give the lexer some input
    #lexer.input(data)


def checa_maior(token1,token2):
    if token1>token2:
        return token1
    else:
        return token2

main()
'''
# Tokenize
while True:
    main
    tok = lexer.token()
    if not tok:
        break      # No more input
    #print(tok.type, tok.value, tok.lineno, tok.lexpos)
    print(tok.type, tok.value)
'''


