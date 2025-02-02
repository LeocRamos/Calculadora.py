# -*- coding: utf-8 -*-
"""Projeto_Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q4_t98kvsQd4gaGLpfV3n3Fs5DhvW8gW

# Boas Vindas e armazenando valores.
"""

# Boas vindas ao usuário e solicitando 2 números para o calcúlos aritiméticos.

num1 = 0
num2 = 0

print("Olá caro usuário, seja bem vindo a calculadora!")
print("Para iniciarmos, digite um primeiro valor:")
num1 = int(input())
print("Agora digite um segundo valor:")
num2 = int(input())

"""# Opções de Calculos"""

# Serão disponibilizados 4 opções de calculos para o usuário, sendo eles soma, subtração, multiplicação e divisão.

opcao = 0

print("Agora selecione a operação que deseja realizar:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input())

"""### Loop para erros de digitação."""

# Vamos criar uma linha de loop caso o usuário digite o número errado.

while opcao < 1 or opcao > 4:
    print("Opção inválida. Por favor, selecione uma opção válida.")
    opcao = int(input())

"""# Calculo dos valores armazenados"""

# Agora iremos fazer o calcúlo conforme a opção selecionado pelo usuário.

if opcao == 1:
    soma = num1 + num2
    print("O resultado da soma é:", soma)

elif opcao == 2:
    subtracao = num1 - num2
    print("O resultado da subtração é:", subtracao)

elif opcao == 3:
    multiplicacao = num1 * num2
    print("O resultado da multiplicação é:", multiplicacao)

elif opcao == 4:
    divisao = num1 / num2
    print("O resultado da divisão é:", divisao)