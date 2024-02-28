def eh_palindromo(string):
    # Removendo espaços em branco e convertendo para minúsculas
    string = string.replace(" ", "").lower()
    # Verificando se a string é igual à sua inversa
    return string == string[::-1]

# Exemplo de uso da função
string = "arara"
print(eh_palindromo(string))  # Saída: True

def palavra_mais_longa(frase):
    # Dividindo a frase em palavras
    palavras = frase.split()
    # Encontrando a palavra mais longa
    palavra_mais_longa = max(palavras, key=len)
    return palavra_mais_longa

# Solicitando a frase ao usuário
frase = input("Digite uma frase: ")

# Chamando a função e imprimindo a palavra mais longa
print("A palavra mais longa na frase é:", palavra_mais_longa(frase))
