from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('CSGO', 'FPS', 'PC')
jogo2 = Jogo('LOL', 'MOBA', 'PC')
jogo3 = Jogo('Valorant', 'FPS', 'PC')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ]) #configurando a rota para o metodo post.
# Tratar o dado do cliente ( recebendo o jogo novo e adicionando na lista)
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/') #redirecionamento de rota.


app.run(debug=True) #reload na aplicação com o debug.
