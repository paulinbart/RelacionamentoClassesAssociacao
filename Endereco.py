class Endereco:

    def __init__(self):
      #usando o comando input para inserir valores nos atributos dentro do construtor
        self._logradouro=input("insira o nome da rua: ")
        self._cidade=input("insira o nome da sua cidade: ")
        self._estado=input("insira o nome do seu estado: ")

    def consultaLogradouro(self):
        print("rua: ",self._logradouro)
        print("cidade: ", self._cidade,"-",self._estado)
