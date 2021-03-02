from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'DKS'


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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo') # novo é meu caminho a seguir depois de login
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])  # configurando a rota para o metodo post.
# Tratar os dados dos clientes ( recebendo o jogo de NOVO e adicionando na lista)
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')  # redirecionamento de rota.


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)  # adicionando rota para o formulario de login



@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'senhaMestra' == request.form['senha']:  # verificando os dados (senha) passados pelo formulario .
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' Logou com sucesso!') #passando mensagem de verificação de login
        proxima_pagina = request.form['proxima']
        return redirect('/'.format(proxima_pagina))
    else:
        flash(request.form['usuario'] + " Nome ou senha invalidos")
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')


app.run(debug=True)  # reload na aplicação com o debug.
