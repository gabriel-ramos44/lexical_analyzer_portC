# ANALISADOR LEXICO
# GABRIEL RAMOS
# LUCAS BECKER

import os
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Lista de padrões e tipos de tokens correspondentes
list_tokens = [
    (r'\s+', 'WHITESPACE'),
    (r'\bprograma\b|\bfimprograma\b', 'PALAVRA_RESERVADA'),  # Palavras reservadas 'programa' e 'fimprograma'
    (r'\bse\b|\bfimse\b|\bpara\b|\benquanto\b', 'ESTRUTURA'),  # Palavras reservadas de estruturas condicionais e de loop
    (r'\bleia\b|\bescreva\b', 'OPERACAO_ES'),  # Palavras reservadas para operações de entrada e saída
    (r'\binteiro\b|\bflut\b|\bchar\b|\btexto\b', 'TIPO_VARIAVEL'),  # Palavras reservadas para tipos de variáveis
    (r'[a-zA-Z]+(?![a-zA-Z])', 'VARIAVEL'),  # Nomes de variáveis
    (r'[-+]?\d*\.\d+|\d+', 'NUMERO'),  # Números inteiros e de ponto flutuante
    (r'"(\\.|[^"])*"', 'TEXTO'),  # String (texto)
    (r',', 'VIRGULA'),  # Vírgula
    (r'{', 'ABRE_BLOCO'),  # Delimitador de bloco de abertura
    (r'}', 'FECHA_BLOCO'),  # Delimitador de bloco de fechamento
    (r';', 'DELIMITADOR_COMANDO'),  # Delimitadores de comandos
    (r'&&', 'ELOG'),  # Lógico AND
    (r'\|\|', 'OULOG'),  # Lógico OR
    (r'!', 'NEGACAO'),  # Negação
    (r'>|<|==|>=|<=', 'RELACIONAL'),  # Operadores relacionais
    (r'\*|/|\+|-|\^', 'ARITMETICO'),  # Operadores aritméticos
    (r'=', 'ATRIBUICAO'),  # Operador de atribuição
    (r'\(', 'ABRE_PARENTESES'),  # Parênteses de abertura
    (r'\)', 'FECHA_PARENTESES'),  # Parênteses de fechamento
    (r'\{', 'ABRE_CHAVES'),  # Chave de abertura
    (r'\}', 'FECHA_CHAVES'),  # Chave de fechamento
]

def tokenize(code):
    tokens = []
    i = 0
    while i < len(code):
        match = None
        for pattern, type in list_tokens:
            regex = re.compile(pattern)
            match = regex.match(code, i)
            if match:
                value = match.group(0)
                if type != 'WHITESPACE':
                    tokens.append(Token(type, value))
                i += len(value)
                break
        if not match:
            raise Exception(f"Caractere ilegal: {code[i]}")
            i += 1
    return tokens

def main():
    # Listar os arquivos com a extensão .portc na pasta atual
    files = [f for f in os.listdir('.') if f.endswith('.portc')]

    if not files:
        print("Nenhum arquivo .portc encontrado na pasta atual.")
        return

    print("Arquivos .portc disponíveis:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    choice = int(input("Escolha o número do arquivo que deseja processar: "))

    if 1 <= choice <= len(files):
        input_file_name = files[choice - 1]
        output_file_name = f"tokens_{os.path.splitext(input_file_name)[0]}.txt"

        with open(input_file_name, 'r') as input_file:
            code = input_file.read()

        # Tokenizar o código
        tokens = tokenize(code)

        with open(output_file_name, 'w') as output_file:
            for token in tokens:
                output_file.write(f"Tipo: {token.type}, Valor: {token.value}\n")

        print(f"Tokens do arquivo '{input_file_name}' escritos em '{output_file_name}'.")

    else:
        print("Escolha inválida. Por favor, escolha um número de arquivo válido.")

if __name__ == "__main__":
    main()