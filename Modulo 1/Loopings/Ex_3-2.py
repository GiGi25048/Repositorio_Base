from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    lista= ['Beatriz','Ygona','Agatha Nunes', 'Paulo','Jhonny','Agnaldo', 'Anielly','Theo','Roberto Carlos','Levina']
    return render_template('ex_3-2.html', Lista = lista)







if __name__== '__main__':
    app.run(debug=True)