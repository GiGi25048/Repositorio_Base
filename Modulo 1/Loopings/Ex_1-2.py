from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    
    return 'Olá Mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, me chamo Giovanna e faço curso de  Programação'

if __name__== '__main__':
    app.run(debug=True)