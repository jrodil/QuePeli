import requests, sys, re
from random import *
from bs4 import BeautifulSoup


def getMovie(listURL):


	p = 1

	movies = {
		
	}

	name = []
	year = []

	scrap = True

	listID = str(re.search("ls\d*",listURL).group(0))


	while scrap == True: #if there's movies
		

		url = 'https://www.imdb.com/list/' + listID +'?page='+str(p)
		response = requests.get(url)
		soup = BeautifulSoup(response.content, 'html.parser')
		movie_name = soup.findAll('div',attrs={'class':'lister-item-content'}) 
		movie_year = soup.findAll('span',attrs={'class':'lister-item-year text-muted unbold'})
		movie_poster = soup.findAll('div',attrs={'class':'lister-item-image ribbonize'})
		nMovies = soup.findAll('span',attrs={'class':'pagination-range'})

		try: #if < 100 movies doesn't find regex
			nMovies = str(re.search("of.*",str(nMovies)).group(0))
			nMovies = nMovies[3:]
		except:
			None

		x = 0



		for i in range(0,len(movie_name)): #gets every movie data
			if(len(movie_name) != 0): #if not empty page
				n = movie_name[i].h3.a.text
				y = movie_year[i].text
				m = movie_poster[i].a.img['loadlate']
				movies[i] = [n,y,m]
				x += 1

		if x < 100 or (x == 100 and len(name) == nMovies): #if last page
			scrap = False
		else:
			p += 1





	ranmovies = []
	for x in range (0,3):
		i = randint(0,len(movies)) #gets random movie
		ranmovies.append(movies[i])


	return ranmovies






