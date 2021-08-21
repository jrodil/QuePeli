from bs4 import BeautifulSoup
import json, requests, re, time

def fetchLists():

	iTime = time.perf_counter()


	f = open('lists.json')
	data = json.load(f)

	for l in data['lists']:
		response = requests.get(l['url'])	
		soup = BeautifulSoup(response.content,'html.parser')
		movies = soup.findAll('div',attrs='lister-item mode-detail')

		movieIds = []
		for i in range(len(movies)):
			movieId = str(re.search("[^tt]\d*",str(movies[i].div['data-tconst'])).group(0))
			movieIds.append(movieId)

		l['movies'] = movieIds


	finalJson = json.dumps(data)
	with open('lists.json','w') as out:
		out.write(finalJson)


	fTime = time.perf_counter()

	print(f"Fetched all lists in {fTime - iTime:0.4f} seconds!")
	


fetchLists()