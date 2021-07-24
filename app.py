from flask import Flask, render_template, request, redirect
from subprocess import run


app = Flask(__name__)


@app.route("/",methods = ['POST','GET'])
def index():
    
    error = ""


    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        url = request.form['url']
        if url == "":
            error = "La url está vacía!"
        cmd = run(['python', 'QuePeli.py',f'{url}'], capture_output=True)
        pelis = (cmd.stdout.decode('utf-8','replace')).split("\n")
        return render_template('index.html',pelis=pelis,error=error)


@app.route('/nolist',methods = ['POST','GET'])
def nolist():
    
    pelis = []
    error = ""

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        url = "https://www.imdb.com/list/ls006266261/"
        cmd = run(['python', 'QuePeli.py',url], capture_output=True)
        pelis = (cmd.stdout.decode('utf-8','replace')).split("\n")
        return render_template('index.html',pelis=pelis,error=error)


if __name__ == "__main__":
    app.run(debug=True)