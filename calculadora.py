import math

class Calculadora:
    def __init__(self, numero):
       self.numero = numero

    def Soma(self):
       return self.numero + self.numero
        
    def Subtraçao(self):
        return self.numero - self.numero
        
    def Divisao(self):
        return self.numero / self.numero
    
    def Multiplicacao(self):
        return self.numero * self.numero

    def Resultados(self):
        print(f'A soma dos números é: {self.Soma()}')
        print(f'A subtração dos números é: {self.Subtraçao()}')
        print(f'A divisão dos números é: {self.Divisao()}')
        print(f'A multiplicação dos números é: {self.Multiplicacao()}')

class calculadoraCientifica(Calculadora):
    def __init__(self):
        super().__init__ = self.numero
    
    def Raiz(self):
        return math.sqrt(self.numero)

    def Fatorial(self):
        return math.factorial(self.numero)
    
    def Sen(self):
        return math.sin(self.numero)
    
    def Cos(self):
        return math.cos(self.numero)

    def Tang(self):
        return math.tan(self.numero)
    
    def Log(self):
        return math.log(self.numero)

    def Resultados(self):
        super().Resultados()
        print(f'A raiz quadrada é: {self.Raiz()}')
        print(f'O fatorial é: {self.Fatorial()}')
        print(f'O seno é: {self.Sen()}')
        print(f'O cosseno é: {self.Cos()}')
        print(f'A tangente é: {self.Tang()} ')
        print(f'O log é: {self.Log()}')
        

print('1 - Calculadora Simples\n2 - Calculadora Científica')
modeloCal = int(input(f'Escolha uma opção de calculadora:'))

calculadoraSimples = Calculadora()
cientifica = calculadoraCientifica()

if modeloCal == 1:
    calculadoraSimples.Resultados()
else: 
    cientifica.Resultados()
