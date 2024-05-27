# import math
# import datetime

# # # #! main

# class Conta:
#     _saldo = None
#     _conta = None
#     _agencia = None
#     _dono = None
#     _taxa_saque = None
#     _pagamentos_recebidos = []
#     _pagamentos_efetuados = []

# def __init__(self, agencia, conta, dono, saldo_inicial, taxa_de_saque):
#     self._saldo = saldo_inicial
#     self._conta = conta
#     self._agencia = agencia
#     self._dono = dono
#     self._taxa_saque = taxa_de_saque
    
# def consultar_saldo(self):
#     return self._saldo
    
# def receber_pagamento(self, quantidade):
#     print('este tipo de conta não recebe pagamento')        

# def emitir_extrato(self):
#     print("extrato emitido")

# class ContaComTransferencia(Conta):
#     def __init__(self, agencia, conta, dono, saldo_inicial, taxa_de_saque):
#         super().__init__(agencia, conta, dono, saldo_inicial, taxa_de_saque)

#     _taxa_pix = None
#     _taxa_ted = None

#     def Transferencia(self, tipo, quantidade):
#         match tipo:
#             case 'pix':
#                 self._saldo -= quantidade + (quantidade * self._taxa_pix)
#                 self._pagamentos_efetuados.append({
#                     "data": datetime.datetime.now(),
#                     "quantidade": quantidade
#                 })
#             case 'ted':
#                 self._saldo -= quantidade + (quantidade * self._taxa_ted)
#                 self._pagamentos_efetuados.append({
#                     "data": datetime.datetime.now(),
#                     "quantidade": quantidade
#                 })



# # # #! child  

# class ContaSalario(Conta):
#     __limite_saque = None
#     __limite_saque_inicial = None
#     __limite_emitir_extrato = None

#     def __init__(self, agencia, conta, dono, saldo_inicial, limite_saque = 5, limite_extrato = 2):
#         super().__init__(agencia, conta, dono, saldo_inicial, 0.01)
#         self.__limite_saque = limite_saque
#         self.__limite_saque_inicial = limite_saque
#         self.__limite_emitir_extrato = limite_extrato


#     def saque(self, quantidade):
#         if self.__limite_saque >= 0:
#             self._saldo -= quantidade - (quantidade * self._taxa_saque)
#             self._pagamentos_efetuados.append({
#                 "data": datetime.datetime.now(),
#                 "quantidade": quantidade
#             })
#         else:
#             print("Voce já atingiu o limite de saque por mes")

#     def resetar_limite_saque(self):
#         self.__limite_saque = self.__limite_saque_inicial

#     def emitir_extrato(self):
#         if self.__limite_emitir_extrato > 0:
#             print("Recebidos:\n")
#             for i in self._pagamentos_recebidos:
#                 print(i)
#             print("Efetuados:\n")
#             for i in self._pagamentos_efetuados:
#                 print(i)
#         else:
#             print("Voce ja atingiu o limite de emissão de extrato este mês")

#     def getSaldo(self):
#         return self._saldo

#     def setSaldo(self, value):
#         self._saldo = value

#     def receber_pagamento(self, quantidade):
#         self._pagamentos_recebidos.append({
#                 "data": datetime.datetime.now(),
#                 "quantidade": quantidade
#             })
#         # self._saldo += quantidade
#         saldo = self.getSaldo()
#         novo_saldo = saldo + quantidade
#         self.setSaldo(novo_saldo)

# class ContaCorrente(ContaComTransferencia):
#     _limite_credito = None

#     def __init__(self, agencia, conta, dono, saldo_inicial, limite_inicial = 100.0):
#         super().__init__(agencia, conta, dono, saldo_inicial, 0.025)
#         self._limite_credito = limite_inicial
    
#     def pagar_conta(self, quantidade):
#         self._saldo -= quantidade
#         self._pagamentos_efetuados.append({
#             'data':datetime.datetime.now(),
#             'quantidade': quantidade
#         })

# class ContaPoupanca(ContaComTransferencia):
#     __rendimento = None

#     def __init__(self, agencia, conta, dono, saldo_inicial, taxa_de_saque, rendimento = 0.02):
#         super().__init__(agencia, conta, dono, saldo_inicial, taxa_de_saque)
#         self.__rendimento = rendimento

#     def fazer_aplicacao(self, quantidade):
#         self._saldo += quantidade

#     def efetuar_rendimento(self):
#         self._saldo += self._saldo * self.__rendimento


# salario  = ContaSalario(123, 33244, 'nycollas sobolevski', 1000)
# corrente = ContaCorrente(123, 54354, 'nycollas sobolevski', 0)
# poupanca = ContaPoupanca(123, 55646, 'nycollas sobolevski', 100, 0.02)

# salarioseminit = ContaSalario()

# salario.receber_pagamento(1200)
# salario.receber_pagamento(1200)
# print(salario.consultar_saldo())

# diaatual = datetime.datetime.now()



# #! getter/setter

class Conta:
    def __init__(self, saldo, nome):
        self.__saldo = saldo
        self.__nome = nome

    def get_saldo( self ):
        return self.__saldo

    def set_saldo( self, value ):
        self.__saldo = value
    
    def get_nome( self ):
        return self.__nome

    def set_nome( self, value ):
        self.__nome = value

conta = Conta(1200, '')

# # com erro
# # print(conta.__saldo)
# # conta.__saldo = 3000


# #forma correta
conta.set_saldo(3000)
print(conta.get_saldo())
