import QuePeli as qp
from flask import Flask, render_template, request, redirect, url_for
from subprocess import run


app = Flask(__name__)


@app.route("/",methods = ['POST','GET'])
def movies():
    
    error = ""
    pelis = []


    if request.method == 'GET':
        return render_template('index.html',pelis=pelis)
    
    if request.method == 'POST':

        if "list" in request.form:
            url = request.form['url']
            if url == "":
                error = "La url está vacía!"
            else: 
                pelis = qp.getMovies(url)
                
            

            return render_template('movies.html',pelis=pelis,error=error)

        if "nolist" in request.form:
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
            elif genre == "11":
                url = "https://www.imdb.com/list/ls000071646/"
            pelis = qp.getMovies(url)

            return render_template('movies.html',pelis=pelis,error=error)



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
