from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/morpion.html')
def morpion():
    return render_template('morpion.html')

@app.route('/echec.html')
def echec():
    return render_template('echec.html')

if __name__ == '__main__':
    app.run(debug=True)