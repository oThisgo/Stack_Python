from livro import Livro

class Pilha():
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, item):
        if not isinstance(item, Livro):
            raise TypeError("O item precisa ser uma instância da classe Livro.")
            
        item.proximo = self.topo
        self.topo = item
        self.tamanho += 1
        
    def remover(self):
        if self.topo is None:
            raise IndexError("A pilha está vazia. Não é possível remover nenhum item.")
        
        item_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return item_removido

    def imprimir(self):
        itens = []
        atual = self.topo
        while atual is not None:
            itens.append(str(atual))
            atual = atual.proximo
        
        for item in reversed(itens):
            print(item)