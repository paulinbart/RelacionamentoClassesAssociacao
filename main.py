#Classe principal, vamos instanciar os objetos aqui

#importando as classes que vamos utilizar diretamente
from Compra import Compra
from Pessoa import Pessoa
from Produto import Produto

#criando um objeto pessoa
pessoa=Pessoa()
#criando um objeto produto
produto=Produto()
#criando um objeto compra
compra1=Compra()
#chamando o método comprar, que precisa como parâmetro uma pessoa e um produto
compra1.comprar(pessoa,produto)
#exibindo o verificar compra da nossa compra1
print(compra1.verificarCompra())