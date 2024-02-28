def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [numero for numero in lista if eh_primo(numero)]

# Exemplo de uso da função
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = numeros_primos(numeros)
print("Números primos na lista:", primos)

fila = []

def adicionar_cliente(cliente):
    fila.append(cliente)
    print(f"Cliente '{cliente}' adicionado à fila.")

def remover_cliente():
    if fila:
        cliente_removido = fila.pop(0)
        print(f"Cliente '{cliente_removido}' removido da fila.")
    else:
        print("Fila vazia. Nenhum cliente para remover.")

def mostrar_posicao_cliente(cliente):
    if cliente in fila:
        posicao = fila.index(cliente) + 1
        print(f"O cliente '{cliente}' está na posição {posicao} na fila.")
    else:
        print(f"O cliente '{cliente}' não está na fila.")

# Exemplo de uso do programa
adicionar_cliente("João")
adicionar_cliente("Maria")
adicionar_cliente("Pedro")
mostrar_posicao_cliente("Maria")
remover_cliente()
mostrar_posicao_cliente("Maria")
remover_cliente()
remover_cliente()
remover_cliente()
