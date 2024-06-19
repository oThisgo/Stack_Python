from livro import Livro

class Pilha():
    def __init__(self, topo, tamanho):
        self.itens = []
        self.topo = topo
        self.tamanho = tamanho

    def add(self, item = Livro()):
        self.itens.append(item)
        self.tamanho += 1
        

    def remover(self):
        if not self.itens:
            return
        else:
            self.itens.pop()

    def imprimir(self):
        return str(self.itens)

    
