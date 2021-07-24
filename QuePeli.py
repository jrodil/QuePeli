import requests, sys, re
from random import *
from bs4 import BeautifulSoup




p = 1
name = []
year = []
scrap = True

listID = str(re.search("ls\d*",sys.argv[1]).group(0))


while scrap == True: #if there's movies
	

	
	url = 'https://www.imdb.com/list/' + listID +'?page='+str(p)
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	movie_name = soup.findAll('div',attrs={'class':'lister-item-content'}) 
	movie_year = soup.findAll('span',attrs={'class':'lister-item-year text-muted unbold'})
	x = 0


	for i in range(0,len(movie_name)): #gets every movie data
		if(len(movie_name) != 0): #if not empty page
			n = movie_name[i].h3.a.text
			y = movie_year[i].text
			name.append(n)
			year.append(y)
			x += 1


	if x < 100: #if last page
		scrap = False
	else:
		p += 1






movies = []
for x in range (0,3):
	i = randint(0,len(name)) #gets random movie
	movies.append(i)


for i in range (0,len(movies)):
	print(name[movies[i]] + " - " + year[movies[i]])






