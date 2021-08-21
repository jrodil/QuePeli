import QuePeli as qp
from flask import Flask, render_template, request, redirect, url_for, json
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
                pelis = qp.getMovies(url,['imdb',None])
                
            


        if "nolist" in request.form:
            genre = request.form['genre']

            f = open('lists.json')
            data = json.load(f)
            movies = data['lists'][int(genre) - 1]['movies'] 




            pelis = qp.getMovies(None,['json',movies])

        return render_template('movies.html',pelis=pelis,error=error)



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
