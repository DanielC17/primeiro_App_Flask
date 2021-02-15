from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self._nome = nome
        self._categoria = categoria
        self._plataforma = plataforma



@app.route('/inicio')
def ola():

    jogo1 = Jogo('CSGO', 'FPS', 'PC')
    jogo2 = Jogo('LOL', 'MOBA', 'PC')
    jogo3 = Jogo('Valorant', 'FPS', 'PC')
    lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


app.run()
