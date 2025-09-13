from random import *

# Cria a classe para o policial
class Policial:
    # Cria as variaveis
    def __init__(self):
        self.trabalho = "Policial"
        self.cliente = None
        self.clientes = []

    # Faz a função dos policiais
    def politica(self):
        print("seu trabalho é {}".format(self.trabalho))
        print("verifique se as identidades dos clientes estão batendo")
        self.começar = input("======Começar o Trabalho?====== ")

        # Verifica se vai começar
        if self.começar == "não":
            print("vc esta demitido")
        elif self.começar == "sim":
            self.nomes = ["João", "Maria", "Bernardo", "Claudia", "Sandra", "Luiz", "Marcelo"]
            self.nome = choice(self.nomes)
            self.pode = [False, True]
            self.pode_passar = choice(self.pode)
            print("======Identidades======")
            print("Nome: {}".format(self.nome))
            print("Idade: {}".format(randint(18, 80)))
            print("Trabalho: {}".format("Aposentado"))
            self.verificar = input("Esse cliente pode passar? ")

            # Verifica se pode passar
            if self.verificar == "sim" and self.pode_passar == True or self.verificar == "não" and self.pode_passar == False:
                print("Vc consegiu!!")
            elif self.verificar == "não" and self.pode_passar == True or self.verificar == "sim" and self.pode_passar == False:
                print("Vc perdeu")
            else:
                print("Não conseguimos saber se pode passar")
        else:
            print("não sabemos o que o senhor quer dizer")

        # Transforma as variaveis
        self.cliente = self.nome
        self.clientes.append(self.cliente)

# Faz que a classe seja executada
classe = Policial()
classe.politica()
