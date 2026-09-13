class Token:
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

# Tabela de símbolos usando um dicionário nativo do Python
tabela_simbolos = {}

# Preenchendo a tabela com as palavras reservadas da TABELA 2
palavras_reservadas = [
    "inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", 
    "fimse", "faca-ate", "fimfaca", "fim", "inteiro", "literal", "real"
]

for palavra in palavras_reservadas:
    # A regra exige que classe, lexema e tipo sejam a própria palavra
    tabela_simbolos[palavra] = Token(palavra, palavra, palavra)

linha_atual = 1
coluna_atual = 1
posicao = 0
codigo_fonte = ""

def ERROR(token_erro):
    # Imprime a mensagem padronizada exigida pelo documento
    print(f"ERRO - Caractere inválido na linguagem, linha {linha_atual}, coluna {coluna_atual}")

def SCANNER():
    global posicao, linha_atual, coluna_atual, codigo_fonte
    estado = 0
    lexema = ""

    while posicao < len(codigo_fonte):
        c = codigo_fonte[posicao]

        if c == '\n':
            linha_atual += 1
            coluna_atual = 0

        if estado == 0:
            if c.isspace():
                posicao += 1
                coluna_atual += 1
                continue

            if c in "+-*/":
                estado = 16
                lexema += c
                posicao += 1
                coluna_atual += 1
                

            if c == '(':
                estado = 17
                lexema += c
                posicao += 1
                coluna_atual += 1
                continue

            if c == ')':
                estado = 18
                lexema += c
                posicao += 1
                coluna_atual += 1
                

            if c == ',':
                estado = 19
                lexema += c
                posicao += 1
                coluna_atual += 1
                

            if c == ';':
                estado = 21
                lexema += c
                posicao += 1
                coluna_atual += 1
                

            if c == '<':
                estado = 20
                lexema += c
                posicao += 1
                coluna_atual += 1
                continue

            if c in ">=": # >=
                estado = 23
                lexema += c
                posicao += 1
                coluna_atual += 1

        elif estado == 20:
            if c == '-': # <- 
                estado = 22
                lexema += c
                posicao += 1
                coluna_atual += 1
                continue

            elif c == '=' or c == '>': # <= ou <>
                estado = 15
                lexema += c
                posicao += 1
                coluna_atual += 1
                continue

            else:
                return Token("OPR", lexema, "NULO")

        elif estado == 23:
            if c in "=": # >= ou ==
                estado = 24
                lexema += c
                posicao += 1
                coluna_atual += 1
                continue

            else: # > ou =
                return Token("OPR", lexema, "NULO")

        elif estado == 24:
            return Token("OPR", lexema, "NULO")

        elif estado == 16:
            return Token("OPM", lexema, "NULO")

        elif estado == 17:
            return Token("AB_P", lexema, "NULO")

        elif estado == 18:
            return Token("FC_P", lexema, "NULO")

        elif estado == 19:
            return Token("VIR", lexema, "NULO")

        elif estado == 21:
            return Token("PT_V", lexema, "NULO")

        elif estado == 22:
            return Token("RCB", lexema, "NULO")
            


