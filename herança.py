class InstrumentoEscrita:
    def __init__(self, material):
        self._material = material
    
    def escrever(self):
        print('Escrevendo...')

    def desenhar(self):
        print('Desenhando...')
    

#filho
class Lapis(InstrumentoEscrita):
    def __init__(self, grafite_n=0):
        super().__init__("grafite")
        self.grafite = grafite_n

class Caneta(InstrumentoEscrita):
    def __init__(self, cor_tinta):
        super().__init__('tinta')
        self._cor = cor_tinta

