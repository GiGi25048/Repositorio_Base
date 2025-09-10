from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    
    return 'Olá Mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, me chamo Giovanna e faço curso de  Programação'



@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome},Boa tarde!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}'



if __name__== '__main__':
    app.run(debug=True)