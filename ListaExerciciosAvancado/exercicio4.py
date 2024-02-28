import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            break
        elif abs(palpite - numero_secreto) <= 10:
            print("Você está quente!")
        elif abs(palpite - numero_secreto) <= 20:
            print("Você está morno.")
        else:
            print("Você está frio.")

# Exemplo de uso do jogo de adivinhação
jogo_adivinhacao()

import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potenciacao(a, b):
    return a ** b

def raiz_quadrada(a):
    return math.sqrt(a)

# Exemplo de uso da calculadora
print("Operações básicas:")
print("Soma:", soma(10, 5))
print("Subtração:", subtracao(10, 5))
print("Multiplicação:", multiplicacao(10, 5))
print("Divisão:", divisao(10, 5))

print("\nOperações avançadas:")
print("Potenciação:", potenciacao(2, 3))
print("Raiz Quadrada:", raiz_quadrada(9))
