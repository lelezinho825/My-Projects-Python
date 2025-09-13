# Cria a Classe para a calculadora
class Calculadora:
    # Faz as variaveis
    def __init__(self):
        self.conta = None
        self.result = False
        self.isResult = False

        #Verifica se tem um resultado
        if self.result != False:
            self.isResult = True
        else:
            self.isResult = False

    # Faz que calcule
    def calcular(self):
        print("Bem vindo a minha calculadora!")
        self.conta = input("Vc deseja fazer adição, subtração, multiplicação ou divisão? ")

        #Verifica o tipo de conta
        if self.conta == "adição":
            self.num1 = float(input("qual é o valor de x? "))
            self.num2 = float(input("qual é o valor de y? "))
            self.adi = self.num1 + self.num2
            print("o resultado da conta é: {}".format(self.adi))
            self.result = True
        elif self.conta == "subtração":
            self.n1 = float(input("qual é o valor de x? "))
            self.n2 = float(input("qual é o valor de y? "))
            self.subt = self.n1 - self.n2
            print("o resultado da conta é: {}".format(self.subt))
            self.result = True
        elif self.conta == "multiplicação":
            self.nu1 = float(input("qual é o valor de x? "))
            self.nu2 = float(input("qual é o valor de y? "))
            self.mult = self.nu1 * self.nu2
            print("o resultado da conta é: {}".format(self.mult))
            self.result = True
        elif self.conta == "divisão":
            self.nn1 = float(input("qual é o valor de x? "))
            self.nn2 = float(input("qual é o valor de y? "))
            self.div = self.nn1 / self.nn2
            print("o resultado da conta é: {}".format(self.div))
            self.result = True
        else:
            print("essa conta não pode ser executada")
            print("o resultado é: {}".format(self.isResult))

#Faz que a classe seja executada
classe = Calculadora()
classe.calcular()
