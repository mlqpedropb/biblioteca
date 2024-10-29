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
        if not self.livros[livro_id].emprestado:
            self.livros[livro_id].emprestado = True
            return True  # Empréstimo bem-sucedido
        return False  # Livro já está emprestado

    def devolver_livro(self, livro_id):
        if self.livros[livro_id].emprestado:
            self.livros[livro_id].emprestado = False
            return True  # Devolução bem-sucedida
        return False  # Livro não estava emprestado

    def consultar_livros_emprestados(self):
        return [livro for livro in self.livros if livro.emprestado]
