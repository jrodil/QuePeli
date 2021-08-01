import requests, sys, re, imdb, os
from random import *
from bs4 import BeautifulSoup


def getMovies(listURL):


	p = 1
	movies_id = []
	scrap = True
	listID = str(re.search("ls\d*",listURL).group(0))

	while scrap == True: #if there's movies
		

		list_url = 'https://www.imdb.com/list/' + listID +'?page='+str(p)
		response = requests.get(list_url)
		soup = BeautifulSoup(response.content, 'html.parser')
		list_movies = soup.findAll('div',attrs='lister-item mode-detail')
		nMovies = soup.findAll('span',attrs={'class':'pagination-range'})

		try: #if < 100 movies won't find regex
			nMovies = str(re.search("of.*",str(nMovies)).group(0))
			nMovies = nMovies[3:]
		except:
			None

		x = 0
		
		for i in range(0,len(list_movies)): #gets every movie data
			if(len(list_movies) != 0): #if not empty page
				id = ""
				id = str(re.search("[^tt]\d*",str(list_movies[i].div['data-tconst'])).group(0))
				movies_id.append(id)
				x += 1

		if x < 100 or (x == 100 and len(movies_id) == nMovies): #if last page
			scrap = False
		else:
			p += 1





	ranmovies = []
	repeated = True
	ranids = []
	for x in range (0,3): #get random movies
		repeated = True
		while repeated == True:
			i = randint(0,(len(movies_id)-1)) 
			if i not in ranids:
				ranids.append(i)
				print(i)
				repeated = False

		info = getMovieInfo(movies_id[i])
		movie = []
		movie.append(info['title'])
		movie.append(info['year'])
		movie.append(depixelCover(info['cover url']))
		movie.append(str(re.search("[^:]*",info['plot'][0])[0]))
		movie.append(info['genres'])

		director = info['director']
		movie.append(director[0]['name'])

		stars = []
		cast = info['cast']
		for r in range(0,3): #gets top 3 stars
			stars.append(cast[r]['name'])
		movie.append(stars)


		ranmovies.append(movie)


	return ranmovies






def getMovieInfo(id):

	ia = imdb.IMDb()
	return ia.get_movie(id)


def depixelCover(url): #to get hq cover
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url













