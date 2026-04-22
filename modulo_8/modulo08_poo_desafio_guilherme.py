'''

Criar um Sistema de Biblioteca

class Livro

    (produtos)
    livros, periodicos, jornais, maps, gibi/mangás

class Biblioteca (main)

    (processos/serviços) 
    ler, emprestar, devolver, pesquisar
'''

class Livros:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [status]"
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def emprestar_livro(self, titulo_procurado):
        for livro in self.livros:
            if livro.titulo == titulo_procurado:
                livro.disponivel = False
                print(f"Emprestimo '{livro.titulo}' realizado!")
            else:
                print(f"O livro'{livro.titulo}' já está ocupado.")
            return
        print("Livro não encontrado no acervo.")
