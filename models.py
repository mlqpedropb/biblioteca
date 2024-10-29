class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False

class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, titulo, autor, isbn):
        novo_livro = Livro(titulo, autor, isbn)
        self.livros.append(novo_livro)

    def consultar_livros(self, busca=None):
        if busca:
            return [livro for livro in self.livros if busca.lower() in livro.titulo.lower() or busca.lower() in livro.autor.lower()]
        return self.livros

    def emprestar_livro(self, livro_id, usuario):
        if not self.livros[int(livro_id)].emprestado:
            self.livros[int(livro_id)].emprestado = True
            # Aqui você poderia adicionar lógica para registrar o usuário que fez o empréstimo

    def devolver_livro(self, livro_id):
        self.livros[int(livro_id)].emprestado = False
