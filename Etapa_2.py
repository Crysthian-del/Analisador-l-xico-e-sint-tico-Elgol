import ply.yacc as yacc
import ply.lex as lex

# =========================
# PALAVRAS RESERVADAS
# =========================

reservadas = {
    'elgio': 'ELGIO',
    'numero': 'NUMERO_TIPO',
    'NADA': 'NADA',
    'NEG': 'NEG',
    'EXP': 'EXP',
    'enquanto': 'ENQUANTO',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'para': 'PARA',
    'inicio': 'INICIO',
    'fim': 'FIM',
    'maior': 'MAIOR',
    'menor': 'MENOR',
    'igual': 'IGUAL',
    'diferente': 'DIFERENTE',
    'migual': 'MIGUAL',
    'Migual': 'MIGUAL2'
}

# =========================
# TOKENS
# =========================

tokens = [
    'IDENTIFICADOR',
    'FUNCAO',
    'NUMERO',

    'IGUAL_OP',
    'MOD',
    'MAIS',
    'MENOS',
    'DIV',
    'MULT',

    'LPAREN',
    'RPAREN',
    'PONTO',
    'VIRGULA'
] + list(reservadas.values())

# =========================
# OPERADORES E SIMBOLOS
# =========================

t_IGUAL_OP = r'='
t_MOD = r'%'
t_MAIS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_MULT = r'x'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PONTO = r'\.'
t_VIRGULA = r','

# =========================
# IGNORAR ESPAÇOS
# =========================

t_ignore = ' \t'

# =========================
# COMENTÁRIOS
# =========================

def t_COMENTARIO(t):
    r'\*.*'
    pass

# =========================
# IDENTIFICADORES E RESERVADAS
# =========================

def t_FUNCAO(t):
    r'_[A-Z][a-zA-Z]{2,}[a-z]'
    return t

def t_IDENTIFICADOR(t):
    r'[A-Za-z]+'

    # Palavras reservadas
    if t.value in reservadas:
        t.type = reservadas[t.value]
        return t

    # Identificadores válidos do Elgol
    if len(t.value) >= 4 and t.value[0].isupper() and t.value[-1].islower():
        return t

    print(f"Erro léxico: token inválido '{t.value}'")

def t_PALAVRA_INVALIDA(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    print(f"Erro léxico: token inválido '{t.value}'")
    
# =========================
# NÚMEROS
# =========================

def t_NUMERO(t):
    r'[1-9][0-9]*'
    return t

# =========================
# QUEBRA DE LINHA
# =========================

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# =========================
# ERROS
# =========================

def t_error(t):
    print(f"Erro léxico: caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# =========================
# BUILD DO LEXER
# =========================

lexer = lex.lex()

# =========================
# REGRAS SINTÁTICAS
# =========================

def p_programa(p):
    '''
    programa : lista_comandos
    '''

def p_lista_comandos(p):
    '''
    lista_comandos : comando
                   | comando lista_comandos
    '''

def p_comando_declaracao(p):
    '''
    comando : NUMERO_TIPO IDENTIFICADOR PONTO
    '''

def p_comando_atribuicao(p):
    '''
    comando : IDENTIFICADOR IGUAL_OP valor PONTO
    '''

def p_comando_neg(p):
    '''
    comando : NEG IDENTIFICADOR PONTO
    '''

def p_valor_numero(p):
    '''
    valor : NUMERO
    '''

def p_valor_identificador(p):
    '''
    valor : IDENTIFICADOR
    '''

def p_valor_nada(p):
    '''
    valor : NADA
    '''

def p_valor_expressao(p):
    '''
    valor : valor MAIS valor
          | valor MENOS valor
          | valor MULT valor
          | valor DIV valor
          | valor MOD valor
          | valor EXP valor
    '''

def p_error(p):
    if p:
        print(f"Erro sintático próximo de '{p.value}'")
    else:
        print("Erro sintático no final do arquivo")

parser = yacc.yacc()

# =========================
# TESTE
# =========================

codigo = """
numero Teste .

NEG Teste .
"""

resultado = parser.parse(codigo)

print("Análise sintática concluída.")
