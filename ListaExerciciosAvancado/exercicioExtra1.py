class TabuleiroDamas:
    def __init__(self):
        self.tabuleiro = [[0]*8 for _ in range(8)]  # Inicializa o tabuleiro vazio
        self.jogador_atual = 1  # Define o jogador atual (1 ou 2)

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(linha)

    def movimento_legal(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        # Implemente a lógica para verificar se o movimento é legal
        # Aqui, você precisará verificar se a peça pode se mover para a posição de destino de acordo com as regras do jogo
        # Por exemplo, verifique se a peça está na posição de origem, se a posição de destino está vazia, etc.
        return True  # Temporariamente, sempre retorna True para simplificar o exemplo

    def mover_peca(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.movimento_legal(linha_origem, coluna_origem, linha_destino, coluna_destino):
            # Realiza o movimento da peça
            self.tabuleiro[linha_destino][coluna_destino] = self.tabuleiro[linha_origem][coluna_origem]
            self.tabuleiro[linha_origem][coluna_origem] = 0
            self.jogador_atual = 3 - self.jogador_atual  # Alterna para o próximo jogador (1 -> 2, 2 -> 1)
            return True
        else:
            print("Movimento ilegal!")
            return False

# Exemplo de uso do jogo de damas
tabuleiro = TabuleiroDamas()
tabuleiro.imprimir_tabuleiro()

while True:
    # Aqui você pode solicitar ao jogador que insira sua jogada
    # Por exemplo, solicitar a linha e coluna de origem e a linha e coluna de destino da peça
    linha_origem = int(input("Digite a linha de origem da peça: "))
    coluna_origem = int(input("Digite a coluna de origem da peça: "))
    linha_destino = int(input("Digite a linha de destino da peça: "))
    coluna_destino = int(input("Digite a coluna de destino da peça: "))

    if tabuleiro.mover_peca(linha_origem, coluna_origem, linha_destino, coluna_destino):
        tabuleiro.imprimir_tabuleiro()

    # Aqui você pode adicionar condições de vitória ou empate e encerrar o jogo quando necessário
