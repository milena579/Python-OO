class Casa: 
    def __init__(self):
        self.public = 'public'
        self.__Pi = 3.141526

    def get_pi(self):
        return self.__Pi
    
    def piv2(self):
        return self.__Pi * 2
casinha = Casa()
casinha.public = 'uma string'
print(casinha.piv2())