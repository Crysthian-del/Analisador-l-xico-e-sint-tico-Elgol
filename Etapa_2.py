import ply.lex as lex

# =========================
# Palavras reservadas
# =========================
reserved = {
    'elgio': 'ELGIO',
    'numero': 'NUMERO',
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
    'Migual': 'MIGUAL'
}

# =========================
# Tokens
# =========================
tokens = [
    'ID',
    'FUNC_ID',
    'NUM',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'EQUAL',
    'LPAREN', 'RPAREN',
    'DOT'
] + list(reserved.values())

# =========================
# Operadores e símbolos
# =========================
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'x'
t_DIVIDE = r'/'
t_MOD    = r'%'
t_EQUAL  = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT    = r'\.'

# =========================
# Ignorar espaços
# =========================
t_ignore = ' \t'

# =========================
# Comentários (* até fim da linha)
# =========================
def t_COMMENT(t):
    r'\*.*'
    pass

# =========================
# Funções (ANTES do ID!)
# =========================
def t_FUNC_ID(t):
    r'_[A-Z][a-zA-Z]{2,}[a-z]'
    return t

# =========================
# Identificadores e reservadas
# =========================
def t_ID(t):
    r'[A-Z][a-zA-Z]{2,}[a-z]'
    
    # Se for palavra reservada, troca o tipo
    t.type = reserved.get(t.value, 'ID')
    return t

# =========================
# Número válido
# =========================
def t_NUM(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t

# =========================
# Detectar número inválido (ex: 034)
# =========================
def t_NUM_INVALID(t):
    r'0[0-9]+'
    print(f"Erro léxico: número inválido '{t.value}' (não pode começar com 0)")

# =========================
# Quebra de linha
# =========================
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# =========================
# Erro geral
# =========================
def t_error(t):
    print(f"Erro léxico: caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# =========================
# Criar lexer
# =========================
lexer = lex.lex()

# =========================
# TESTE
# =========================
data = '''
* Exemplo Elgol
numero Teste .
Teste = 34 .
NEG Teste .
Teste = 034 .
_TesteFunc (Teste) .
'''

lexer.input(data)

for tok in lexer:
    print(tok)

input("Pressione Enter para sair...")
