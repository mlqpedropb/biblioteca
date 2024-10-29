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
    busca = request.args.get('busca')
    livros = biblioteca.consultar_livros(busca)
    return render_template('consulta.html', livros=livros)

@app.route('/emprestimo', methods=['POST'])
def emprestimo():
    livro_id = request.form['livro_id']
    usuario = request.form['usuario']
    biblioteca.emprestar_livro(livro_id, usuario)
    return redirect(url_for('index'))

@app.route('/devolver', methods=['GET', 'POST'])
def devolver():
    if request.method == 'POST':
        # Lógica para processar a devolução do livro
        pass
    return render_template('devolver.html')


if __name__ == '__main__':
    app.run(debug=True)
