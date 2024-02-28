import random

# Definindo as perguntas e respostas
perguntas_respostas = {
    "Qual é a capital da França?": ["a) Lodres", "b) Paris", "c) Roma", "d) Berlim"],
    "Quem escreveu 'A Divina Comédia'?": ["a) Victor Hugo", "b) William Shakespeare", "c) Franz Kafka", "d) Dante Alighieri"],
    "Qual é o maior oceano do mundo?": ["a) Oceano Indico", "b) Oceano Atlântico", "c) Oceano Pacífico", "d) Oceano Ártico"],
    "Qual é a moeda oficial do Japão?": ["a) Won", "b) Dólar", "c) Euro", "d) Yen"],
    "Quem foi o primeiro presidente dos Estados Unidos?": ["a) George Washington", "b) Abraham Lincoln", "c) Thomas Jefferson", "d) John Adams"],
    "Qual é o símbolo químico do ouro?": ["a) Ag", "b) Au", "c) Fe", "d) Cu"],
    "Qual é o país com maior área territorial do mundo?": ["a) Canadá", "b) China", "c) Estados Unidos", "d) Rússia"],
    "Quem pintou a Mona Lisa?": ["a) Pablo Picasso", "b) Leonardo da Vinci", "c) Vincent van Gogh", "d) Michelangelo"],
    "Qual é a maior cadeia montanhosa do mundo?": ["a) Himalaias", "b) Montanhas Rochosas", "c) Alpes", "d) Andes"],
    "Quantos continentes existem?": ["a) 4", "b) 5", "c) 6", "d) 7"],
    "Qual é a montanha mais alta do mundo?": ["a) Monte Everest", "b) Monte Kilimanjaro", "c) Monte Fuji", "d) Monte Aconcágua"],
    "Quem foi o primeiro presidente do Brasil?": ["a) Tancredo Neves", "b) Getúlio Vargas", "c) Juscelino Kubitschek", "d) Deodoro da Fonseca"],
    "Qual é o maior rio do mundo em volume de água?": ["a) Rio Nilo", "b) Rio Amazonas", "c) Rio Yangtzé", "d) Rio Mississipi"],
    "Quem é o autor de 'Cem Anos de Solidão'?": ["a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Pablo Neruda", "d) Jorge Luis Borges"],
    "Qual é o metal mais abundante na crosta terrestre?": ["a) Cobre", "b) Ferro", "c)Alumínio", "d) Ouro"]
}

# Função para apresentar a pergunta e opções de resposta
def apresentar_pergunta(pergunta, opcoes):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    resposta = input("Escolha a opção correta (a, b, c ou d): ")
    return resposta.lower()

# Função para verificar se a resposta está correta
def verificar_resposta(pergunta, resposta):
    respostas_corretas = {
        "Qual é a capital da França?": "b",
        "Quem escreveu 'A Divina Comédia'?": "d",
        "Qual é o maior oceano do mundo?": "c",
        "Qual é a moeda oficial do Japão?": "d",
        "Quem foi o primeiro presidente dos Estados Unidos?": "a",
        "Qual é o símbolo químico do ouro?": "b",
        "Qual é o país com maior área territorial do mundo?": "d",
        "Quem pintou a Mona Lisa?": "b",
        "Qual é a maior cadeia montanhosa do mundo?": "a",
        "Quantos continentes existem?": "d",
        "Qual é a montanha mais alta do mundo?": "a",
        "Quem foi o primeiro presidente do Brasil?": "d",
        "Qual é o maior rio do mundo em volume de água?": "b",
        "Quem é o autor de 'Cem Anos de Solidão'?": "a",
        "Qual é o metal mais abundante na crosta terrestre?": "c"
    }
    if resposta == respostas_corretas[pergunta]:
        return True
    else:
        return False

# Função principal do jogo
def q_q_s_m():
    pontuacao = 0
    perguntas = list(perguntas_respostas.keys())
    random.shuffle(perguntas)  # Embaralhar as perguntas

    for pergunta in perguntas:
        opcoes = perguntas_respostas[pergunta]
        resposta = apresentar_pergunta(pergunta, opcoes)
        if verificar_resposta(pergunta, resposta):
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print("Resposta incorreta!\n")
            break  # Encerra o jogo se a resposta estiver errada

    print(f"Fim do jogo! Sua pontuação final é: {pontuacao}")

# Chamando a função principal para iniciar o jogo
q_q_s_m()
