from flask import Flask, render_template, request, redirect, url_for
from models import Biblioteca

app = Flask(__name__)
biblioteca = Biblioteca()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        isbn = request.form['isbn']
        biblioteca.cadastrar_livro(titulo, autor, isbn)
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/consulta', methods=['GET'])
def consulta():
    busca = request.args.get('busca', '')
    livros = biblioteca.consultar_livros(busca)
    return render_template('consulta.html', livros=livros)

@app.route('/emprestimo', methods=['GET', 'POST'])
def emprestimo():
    mensagem = ""
    if request.method == 'POST':
        livro_id = request.form['livro_id']
        usuario = request.form['usuario']
        
        if not livro_id:
            mensagem = "Por favor, selecione um livro válido."
        else:
            sucesso = biblioteca.emprestar_livro(int(livro_id), usuario)  # Passa o ID como inteiro
            if sucesso:
                mensagem = "Empréstimo realizado com sucesso!"
            else:
                mensagem = "Livro não disponível para empréstimo."
    
    livros_disponiveis = biblioteca.consultar_livros()  # Atualiza a lista de livros
    return render_template('emprestimo.html', livros=livros_disponiveis, mensagem=mensagem)

@app.route('/devolver', methods=['GET', 'POST'])
def devolver():
    mensagem = ""
    if request.method == 'POST':
        livro_id = request.form['livro_id']
        
        if not livro_id:
            mensagem = "Por favor, selecione um livro para devolver."
        else:
            sucesso = biblioteca.devolver_livro(int(livro_id))  # Passa o ID como inteiro
            if sucesso:
                mensagem = "Devolução realizada com sucesso!"
            else:
                mensagem = "Livro não encontrado ou não está emprestado."
    
    livros_emprestados = biblioteca.consultar_livros_emprestados()
    return render_template('devolver.html', livros=livros_emprestados, mensagem=mensagem)

@app.route('/livros-emprestados', methods=['GET'])
def livros_emprestados():
    livros_emprestados = biblioteca.consultar_livros_emprestados()
    return render_template('consultar_livros_emprestados.html', livros=livros_emprestados)

if __name__ == '__main__':
    app.run(debug=True)
