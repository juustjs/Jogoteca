#importando o Flask 
#importando render template para gerenciar com html
#importando o redirect para redirecionar rotas
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

#criando uma classe 
class Jogo:
    def __init__(self,nome,categoria,console):
        self._nome = nome
        self._categoria = categoria
        self._console = console

jogo1 = Jogo('The Sims', 'Sandbox', 'pc')
jogo2 = Jogo('valorant','Tiro','xbox')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'Ps5')
    
lista =[jogo1, jogo2, jogo3]
        
#chamando a aplicação
app = Flask(__name__)

#criando rota inicio
@app.route('/')
def index():
    return render_template('lista.html', titulo ='Jogos', jogos=lista)

#criando uma nova rota para cadastrar jogos direto no html
@app.route('/cadastro')
def cadastro():
    return render_template('novo.html', titulo='Cadastrar Novo Jogo')

#criando uma nova rota request para receber os dados cadastrados vindo do html
@app.route('/criar', methods=['POST',])
def criar ():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo =  Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

#rodando a aplicação
#ativando o debug
app.run(debug=True) 