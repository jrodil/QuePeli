import requests, sys, re, imdb, os, time
from random import *
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait




responses = []


def getMovies(listURL,src):


	movies_id = []
	listType = None


	if src[0] == 'imdb':


		try: #gets list type
			listID = str(re.search("ls\d*",listURL).group(0))
			listType = "list"
		except:
			try: 
				listID = str(re.search("/user/ur\d*/watchlist",listURL).group(0))
				listType = "watchlist"
			except:
				None
			


		if listType == "watchlist": #gets list-type id from an html tag
			response = requests.get(listURL)
			soup = BeautifulSoup(response.content, 'html.parser')
			url = soup.findAll('meta',attrs={'property':'pageId'})[0]['content']
			listID = str(re.search("ls\d*",url).group(0))


		list_url = 'https://www.imdb.com/list/' + listID
		list_pages = getPages(list_url) #gets every page of the list



		with ThreadPoolExecutor(max_workers=len(list_pages)) as pool:
			for i in range(len(list_pages)):
				future = pool.submit(makeRequest,list_pages[i])
			future.result()
			pool.shutdown(wait=True)	







		list_movies = [] #get movies
		for i in range(len(list_pages)):
			soup = BeautifulSoup(responses[i],'html.parser')
			list_movies = list_movies + soup.findAll('div',attrs='lister-item mode-detail')


		

		for i in range(0,len(list_movies)): #gets every movie ID
			id = ""
			id = str(re.search("[^tt]\d*",str(list_movies[i].div['data-tconst'])).group(0))
			movies_id.append(id)

	elif src[0] == 'json':
		movies_id = src[1]




	ranmovies = []
	repeated = True
	ranids = []
	for x in range (0,3): #get random movies
		repeated = True
		while repeated == True:
			i = randint(0,(len(movies_id)-1)) 
			if i not in ranids:
				ranids.append(i)
				repeated = False





	global ranMovieUrl,ranMovieInfo
	ranMovieInfo = []
	ranMovieUrl = []
	with ThreadPoolExecutor(max_workers=len(movies_id)) as pool: #multithread IMDbPy requests
		for i in range(len(ranids)):
			future = pool.submit(getMovieInfo,movies_id[ranids[i]])
		future.result()
		pool.shutdown(wait=True)

	

	for i in range(3):
		
		movie = []
		movie.append(ranMovieInfo[i]['title'])
		movie.append(ranMovieInfo[i]['year'])
		movie.append(depixelCover(ranMovieInfo[i]['cover url']))

		try:
			movie.append(str(re.search("[^:]*",ranMovieInfo[i]['plot'][0])[0]))
		except:
			movie.append(" ")

		movie.append(ranMovieInfo[i]['genres'])

		director = ranMovieInfo[i]['director']
		movie.append(director[0]['name'])

		stars = []
		cast = ranMovieInfo[i]['cast']
		for r in range(0,3): #gets top 3 stars
			stars.append(cast[r]['name'])
		movie.append(stars)

		movie.append(ranMovieUrl[i])


		ranmovies.append(movie)


	return ranmovies







def getPages(listURL):


	urls = []
	response = requests.get(listURL)
	soup = BeautifulSoup(response.content, 'html.parser')

	try:
		soup = soup.findAll('span',attrs={'class':'pagination-range'})
		nMovies = str(re.search("of \d+",str(soup[0])).group(0))
		nMovies = nMovies.split(" ")
		nMovies = nMovies[1]
		nPages = int(nMovies) / 100 

		if nPages % 1 != 0:
			nPages = int(nPages) + 1
		else:
			nPages = int(nPages)

		for i in range(nPages):
			urls.append(listURL+"?page="+str(i + 1))

	except: 
		urls.append(listURL)

	return urls





def makeRequest(listURL):
	result = requests.get(listURL)
	responses.append(result.content)
	return None


def getMovieInfo(id):
	ia = imdb.IMDb()
	movie = ia.get_movie(id)
	URL = ia.get_imdbURL(movie)
	ranMovieInfo.append(movie)
	ranMovieUrl.append(URL)
	return None




def depixelCover(url): #to get hq cover
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url













