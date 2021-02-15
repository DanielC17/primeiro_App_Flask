from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista = ['CSGO', 'Valorant', 'LOL']
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
