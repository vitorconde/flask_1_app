from flask import Flask, render_template

app = Flask(__name__)

class Jogos():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogos('Super Mario', 'Ação', 'SNES')
    jogo2 = Jogos('Pokemon Gold', 'RPG', 'GBA')
    jogo3 = Jogos('Mortal Kombat', 'Luta', 'SNES')
    lista=[jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()