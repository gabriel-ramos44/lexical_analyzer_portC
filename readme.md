# Analisador Léxico em Python

Este é um projeto de analisador léxico em Python que reconhece tokens com base em padrões definidos para uma linguagem de programação específica. O analisador léxico é a parte inicial de um projeto para a matéria de Compiladores.

## O que foi feito

- O projeto inclui um analisador léxico funcional que pode ser utilizado para dividir o código-fonte em tokens reconhecidos.

- A lista de tokens é definida na variável `list_tokens`, onde cada token é associado a um padrão regular.

- O programa lê arquivos de código-fonte com extensão '.portc' da pasta atual, permite que o usuário escolha um arquivo para processar e gera um arquivo de saída com os tokens reconhecidos.

## O que será melhorado

- **Gerar uma lista de tokens de acordo com a gramática:** Atualmente, os tokens são gerados com base em padrões regulares, mas pode ser útil definir tokens de acordo com a gramática da linguagem.

- **Diferenciar entre tipos de variáveis:** Atualmente, os tipos de variáveis são reconhecidos, mas não são diferenciados na saída. Seria útil identificar se uma variável é do tipo "int", "flut", etc.

- **Sinalizar a linha do erro:** Se houver um caractere ilegal ou um token não reconhecido, seria útil sinalizar a linha do erro para facilitar a depuração.

- **Reconhecer o token exatamente como o símbolo terminal:** Atualmente, os tokens são gerados com base em padrões regulares, mas pode ser útil definir tokens de acordo com a gramática da linguagem, em vez de exibir tipos de token como "OPERACAO_ES" deve ser exibido de acordo com a gramática por exemplo "LEIA" ou "ESCREVA.". Ou seja,justar os padrões de token para corresponder exatamente à gramática da linguagem.