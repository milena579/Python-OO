import math

# class Calculadora:

#     def __init__(self):
#         pass


#     @staticmethod
#     def Sum(numberA, numberB):
#         return numberA + numberB
#     @staticmethod
#     def Sub(numberA, numberB):
#         return numberA - numberB
#     @staticmethod
#     def Div(numberA, numberB):
#         return numberA / numberB
#     @staticmethod
#     def Mult(numberA, numberB):
#         return numberA * numberB
    
# class Cientifica(Calculadora):
    
#     def __init__(self) -> None:
#         super().__init__()

#     def Exp(self, numberA, exponential):
#         return numberA ** exponential
#     def Mod(self, numberA, mod):
#         return numberA % mod
#     def sqr(self, number):
#         return number ** 2
#     def sqrt(self, number):
#         return math.sqrt(number)
    

class Calculator: 
    _numberA = 0
    _numberB = 0
    def __init__(self, A, B):
        self._numberA = A
        self._numberB = B

    def Sum(self):
        return self._numberA + self._numberB
    def Sub(self):
        return self._numberA - self._numberB

    def ViewResults(self):
        print(f"Resultado Soma     : {self.Sum()}")
        print(f"Resultado Subtração: {self.Sub()}")

class Cientific(Calculator):
    def __init__(self, A, B):
        super().__init__(A, B)
    
    def Sum(self):
        return self._numberA + 2

    def Sqrt(self):
        return math.sqrt(self._numberA)
    def Sqr(self):
        return self._numberA ** 2
    
    def ViewResults(self):
        super().ViewResults()
        print(f"Soma dois numeros  : {super().Sum()}")
        print(f"SQRT               : {self.Sqrt()}")
        print(f"SQR                : {self.Sqr()}")

c = Calculator(10,7)
c.ViewResults()
print('\n\n\n')
s = Cientific(10,7)
s.ViewResults()
    