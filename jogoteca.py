from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Inicio')
def ola():
    jogos = ['The sims', 'Valorant', 'Crash']
    return render_template('lista.html', titulo='Jogos')


app.run()