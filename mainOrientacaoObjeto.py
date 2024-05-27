class Casa:
    def __init__(self, area, cor, rua):
        self._area = area
        self._cor = cor
        self._ = rua
        self._luzes_ligadas = False
    
    def __del__(self):
        pass
    
    def ligar_luzes(self):
        print('luzes ligadas')
    def desligar_luzes(self):
        print('luzes desligadas')

    def trancar_portas(self):
        print('Portas trancadas')
    def destrancar_portas(self):
        print('Portas destrancadas')

    @staticmethod
    def cortar_energia():
        Casa.energia = False

    @staticmethod
    def ligar_energia():
        Casa.energia = True
casa_joao = Casa(120, 'azul', 'juscelino k')
    # casa_maeia = Casa()
    # casa_verde = Casa()