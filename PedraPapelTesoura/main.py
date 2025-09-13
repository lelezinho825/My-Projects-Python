from random import choice

# Cria a classe para o jogo
class Ppt:
    # Cria as variaveis
    def __init__(self):
        self.user = None
        self.comp = None
        self.jogad = None

    # Faz que o player possa jogar
    def jogar(self):
        print("0: Pedra")
        print("1: Papel")
        print("2: Tesoura")
        print("="*5, "Jogar", "="*5)
        self.pergunta = int(input("Qual vai ser sua jogada? "))
        self.comp_jogadas = [0, 1, 2]
        self.jogada = choice(self.comp_jogadas)

        # Tranforma o __init__
        self.user = self.pergunta
        self.comp = self.jogada

        # Verifica se GANHOU, PERDOU ou deu EMPATE
        if self.user == 0 and self.comp == 2 or self.user == 2 and self.comp == 1 or self.user == 1 and self.comp == 0:
            self.jogad = "GANHOU"
        elif self.user == 2 and self.comp == 0 or self.user == 1 and self.comp == 2 or self.user == 0 and self.comp == 1:
            self.jogad = "PERDEU"
        elif self.user == self.comp:
            self.jogad = "EMPATE"
        else:
            print("vc tem que digitar 0,1 ou 2")
        
        # Mostra como foi o seu jogo
        print(self.jogad)

# Faz que a classe seja executada
classe = Ppt()
classe.jogar()
