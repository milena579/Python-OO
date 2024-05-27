#consiste em modificar o método herdado 
#Ex: abrir a janela de um carro: botão, abrir a janela de uma casa: manualmente
# a função de abrir a janela é a mesma, mas o método que se usa pra abrir é diferente 

class Personagem:
    _vida = 0
    _força = 0
    _inteligencia = 0
    _dinheiro_por_min_ = 0

    def __init__(self):
        self._vida = 100
        self._força = 10
        self._inteligencia = 10
        self._dinheiro_por_min_ = 10
        pass

    def getVida(self):
        return self._vida
    
    def Minerar(self):
        return self._força

class Goblin(Personagem):
    def __init__(self):
        super().__init__()
        self._força = 14
        self._inteligencia = 8
        self._dinheiro_por_min_ = 11

random = Personagem()
print(f'A vida de um personagem aleatório: {random.getVida()}')
print(f'A mineração de um personagem aleatório: {random.Minerar()}')
g = Goblin()
print(f'Vida de um Goblin: {g.getVida()}')
print(f'Mineração de um Goblin: {g.Minerar()}')