class Casa:
    def __init__(self, area, cor, rua, nome = None ):
        self._area = area
        self._cor = cor
        self._rua = rua
        self._nome = nome
       
    def mostrar(self):
        print(f'{self._area}, {self._cor}, {self._rua}, {self._nome}')

cadastro = Casa('1231', 'laranja', 'sete de setembro',)
cadastro.mostrar()

        