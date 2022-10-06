
class Compra:
    def __init__(self):
        #objeto da classe pessoa
        self._pessoa=None
        #objeto da classe produto
        self._produto=None

    #método para adicionar quem fez a Compra e qual foi o produto
    def comprar(self,pessoa, produto):
        self._pessoa=pessoa
        self._produto=produto

    #método que retorna a compra
    def verificarCompra(self):
        return self._pessoa._nome+" comprou "+self._produto._nome

