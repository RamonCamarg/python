import math

# Coeficientes da equação quadrática
a = 1
b = -3
c = 2

# Calculando o discriminante
delta = b**2 - 4*a*c

# Verificando o número de raízes reais
if delta > 0:
    # Duas raízes reais distintas
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
elif delta == 0:
    # Uma raiz real (raiz dupla)
    x = -b / (2*a)
    print("A raiz da equação é:", x)
else:
    # Não há raízes reais
    print("A equação não possui raízes reais.")

# Solicitando o valor em dólares e a taxa de conversão
valor_dolares = float(input("Digite o valor em dólares: "))
taxa_euro = float(input("Digite a taxa de conversão para euros: "))
taxa_libra = float(input("Digite a taxa de conversão para libras: "))

# Convertendo para euros e libras
valor_euro = valor_dolares * taxa_euro
valor_libra = valor_dolares * taxa_libra

# Imprimindo os resultados
print("O valor em euros é:", valor_euro)
print("O valor em libras é:", valor_libra)
