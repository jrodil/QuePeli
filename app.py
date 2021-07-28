import QuePeli as qp
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
        
        pelis = qp.getMovie(url)
        return render_template('index.html',pelis=pelis,error=error)


@app.route('/nolist',methods = ['POST','GET'])
def nolist():
    
    pelis = []
    error = ""

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        url = "https://www.imdb.com/list/ls055592025/"
        pelis = qp.getMovie(url)
        return render_template('index.html',pelis=pelis,error=error)


if __name__ == "__main__":
    app.run(debug=True)