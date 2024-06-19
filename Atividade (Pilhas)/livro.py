from pilha import Pilha

class Livro():
    def __init__(self, titulo, autor, paginas, proximo):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.proximo = proximo

    def __str__(self):
        return f"""
        Título: {self.titulo}
        Autor: {self.autor}
        Páginas: {self.paginas}
        """

    def getNext(self, topo):
        self.proximo = topo - 1

    
    

