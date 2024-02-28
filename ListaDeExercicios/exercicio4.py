# Variáveis booleanas representando as condições climáticas
tem_sol = True
tem_chuva = False

# Estrutura condicional para decidir se é um dia agradável
if tem_sol and not tem_chuva:
    print("É um dia agradável!")
else:
    print("Não é um dia agradável.")

# Solicitando dois números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verificando se ambos os números são pares
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos os números são pares.")
else:
    print("Pelo menos um dos números não é par.")

# Lista de números
numeros = [3, 8, 11, 15, 24, 30, 33]

# Verificando quais números são múltiplos de 3 e ímpares
for numero in numeros:
    if numero % 3 == 0 and numero % 2 != 0:
        print(numero, "é múltiplo de 3 e ímpar.")

# Solicitando a idade ao usuário
idade = int(input("Digite sua idade: "))

# Verificando se a idade está dentro do intervalo especificado
if idade >= 18 and idade <= 65:
    print("Sua idade está dentro do intervalo de 18 a 65 anos.")
else:
    print("Sua idade não está dentro do intervalo de 18 a 65 anos.")
