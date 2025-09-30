from flask import Flask, render_template, request, redirect, url_for
from controller import StreamingController

app = Flask(__name__)
controller = StreamingController()

# Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if controller.login(usuario, senha):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro="Usuário ou senha incorretos!")
    return render_template('login.html', erro=None)

# Página principal
@app.route('/index')
def index():
    disponiveis = controller.listar_disponiveis()
    destaque = controller.listar_destaque()
    return render_template('index.html', disponiveis=disponiveis, destaque=destaque)

# Adicionar mídia
@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form['titulo']
    genero = request.form['genero']
    avaliacao = request.form['avaliacao']
    ano = request.form['ano']
    idioma = request.form['idioma']
    controller.adicionar_midia(titulo, genero, avaliacao, ano, idioma)
    return redirect(url_for('index'))

# Destacar mídia
@app.route('/destacar/<int:indice>')
def destacar(indice):
    controller.destacar_midia(indice)
    return redirect(url_for('index'))

# Excluir mídia do destaque
@app.route('/excluir/<int:indice>')
def excluir(indice):
    controller.excluir_midia(indice)
    return redirect(url_for('index'))

# Remover mídia
@app.route('/remover/<int:indice>')
def remover(indice):
    controller.remover_midia(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
