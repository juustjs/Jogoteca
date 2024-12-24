#importando o Flask 
#importando render template para gerenciar o front com html
from flask import Flask, render_template

#criando uma classe 
class Jogo:
    def __init__(self,nome,categoria,console):
        self._nome = nome
        self._categoria = categoria
        self._console = console
        
#chamando a aplicação
app = Flask(__name__)

#criando rota inicio
@app.route('/Inicio')
def ola():
    jogo1 = Jogo('The Sims', 'Sandbox', 'pc')
    jogo2 = Jogo('valorant','Tiro','xbox')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'Ps5')
    
    lista =[jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo ='Jogos', jogos=lista)

#rodando a aplicação
app.run() 