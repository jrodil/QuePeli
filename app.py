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
        
        pelis = qp.getMovies(url)
        return render_template('index.html',pelis=pelis,error=error)


@app.route('/nolist',methods = ['POST','GET'])
def nolist():
    
    pelis = []
    error = ""
    url = ""

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        genre = request.form['genre']


        if genre == "1":
            url = "https://www.imdb.com/list/ls055592025/"
        elif genre == "2":
            url = "https://www.imdb.com/list/ls009668579/"
        elif genre == "3":
            url = "https://www.imdb.com/list/ls051840406/"
        elif genre == "4":
            url = "https://www.imdb.com/list/ls009668747/"
        elif genre == "5":
            url = "https://www.imdb.com/list/ls009668711/"
        elif genre == "6":
            url = "https://www.imdb.com/list/ls009669258/"
        elif genre == "7":
            url = "https://www.imdb.com/list/ls049309814/"
        elif genre == "8":
            url = "https://www.imdb.com/list/ls000485502/"
        elif genre == "9":
            url = "https://www.imdb.com/list/ls009668082/"
        elif genre == "10":
            url = "https://www.imdb.com/list/ls009668314/"
        pelis = qp.getMovies(url)
        return render_template('index.html',pelis=pelis,error=error)


if __name__ == "__main__":
    app.run(debug=True)