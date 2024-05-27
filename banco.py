#agencia = int(input('Digite o número sua agência: '))
import time
class Conta():
    def __init__(self, agencia, dono, saldo:int):
        self.agencia = agencia
        self.dono = dono
        self.saldo = saldo
    
class contaCorrente(Conta):
    def __init__(self, agencia, dono, saldo):
        super().__init__( agencia, dono, saldo)

    def enviarPix(self,chavePix, valorPix:int):
        self.chavePix = chavePix
        self.valorPix = valorPix

        if valorPix <= self.saldo:
            print('Transferência realizada com sucesso!')
            time.sleep(1)
            saldoAtual = self.saldo - valorPix
            print(f'Seu saldo atual é R${saldoAtual}')

        else: 
            print('Saldo insuficente!')
            print(f'Saldo atual: {self.saldo}\n Valor da tranferência: {self.valorPix}')
    
    def saque(self, valorSaque):
        self.valorSaque = valorSaque
        
        if valorSaque <= self.saldo:
            print('Saque realizado com sucesso!')
            time.sleep(2)
            print('Operação encerrada')
        else:
            print('Saldo insuficente!')
            time.sleep(2)
            print('Operação encerrada')
    
        
class contaPoupança(Conta):
    def __init__(self, agencia, dono, saldo, idadeSaque):
        self.idadeSaque = idadeSaque
        super().__init__(agencia, dono, saldo)
    
    def enviarPix(self, chavePix, valorPix):
        self.chavePix = chavePix
        self.valorPix = valorPix

        if valorPix <= self.saldo:
            time.sleep(3)
            print('Transferência realizada com sucesso!')
            print(f'Seu salfo atual é R${self.saldo}')
        else: 
            print('Saldo insuficente!')
            print(f'Saldo atual: {self.saldo}\n Valor da tranferência: {self.valorPix}')
    
    def saque(self, valorSaque):
        self.valorSaque = valorSaque
        
        if self.idadeSaque >= 18:
            if valorSaque <= self.saldo:
                print('Saque realizado com sucesso!')
                time.sleep(2)
                print('Operação encerrada')
            else:
                print('Saldo insuficente!')
                time.sleep(2)
                print('Operação encerrada')
        else:
            print('Sua idade ainda não é permitida para saque!')
        
class contaSalário(Conta):
    def __init__(self, agencia, dono, saldo:int):
        super().__init__( agencia, dono, saldo)

    def saque(self, valorSaque:int):
        self.valorSaque = valorSaque
        
        if valorSaque <= self.saldo:
            print('Saque realizado com sucesso!')
            time.sleep(2)
            print('Operação encerrada')
        else:
            print('Saldo insuficente!')
            time.sleep(2)
            print('Operação encerrada')

#conta1 =  contaCorrente('32132',"Milena Calegari", 1000)
conta2 =  contaSalário('32132', "Guilherme", 2000)
#conta1.enviarPix('mile@gmail.com', 150)
conta2.saque(3000)


