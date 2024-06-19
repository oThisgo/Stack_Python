from livro import Livro
from pilha import Pilha

pilha = Pilha()
    
livro1 = Livro("It - A Coisa", "Stephen King", 1103)
livro2 = Livro("O Senhor Dos Anéis: A Sociedade Do Anel", "J. R. R. Tolkien", 576)
livro3 = Livro("Jogos Vorazes", "Suzanne Collins", 400)
    
pilha.add(livro1)
pilha.add(livro2)
pilha.add(livro3)
    
print("Pilha após adicionar livros:")
pilha.imprimir()
    
livro_removido = pilha.remover()
print(f"\nLivro removido: {livro_removido}")
    
print("\nPilha após remover um livro:")
pilha.imprimir()