#importando a classe endereço
from Endereco import *
class Pessoa:
    def __init__(self):
        self._nome=input("insira o nome do cliente: ")
        self._numero=input("insira o telefone do cliente: ")
        #chamando o construtor da classe endereço
        self._endereco= Endereco()

    def consultaEndereco(self):
        return self._endereco
        
    def consultaNome(self):
        return self._nome



