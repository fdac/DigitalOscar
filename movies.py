#!/usr/bin/python

import json, pymongo, time, urllib2

BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json'
PAGE_LIMIT = '50'	# 50 is the API maximum. 
API_KEY = '8undyqmz5dwuc785mbbhsh6v'

def getMovies(q): 
  # Retrieve the current page and store it in a Python dictionary. The purpose of this call is to get the total number of movies for the given search parameter. 
  response = urllib2.urlopen(BASE_URL+'?apikey='+API_KEY+'&page=1&page_limit='+PAGE_LIMIT+'&q='+q).read()
  respDict = json.loads(response)
  
  totalMovies = respDict['total']
  if totalMovies == 0: 
    return
  elif totalMovies % 50 == 0: 
    nPages = totalMovies / 50
  else: 
    nPages = totalMovies / 50 + 1
  if nPages > 25: 
    nPages = 25		# The RT API does not permit the page argument to exceed 25. :(

  # Set up a loop that will iterate through nPages pages. The page argument must be a positive integer, so we start with 1. 
  for page in range(1, nPages+1): 
    response = urllib2.urlopen(BASE_URL+'?apikey='+API_KEY+'&page='+str(page)+'&page_limit='+PAGE_LIMIT+'&q='+q).read()
    respDict = json.loads(response)

    recordCount = len(respDict['movies'])	# recordCount is usually but not always 50.

    for j in range(0, recordCount):
      # Get the id and title for the current movie record.
      movieId = respDict['movies'][j]['id']
      movieTitle = respDict['movies'][j]['title']
      searchObj = {}
      searchObj['id'] = movieId
      result = movies.find(searchObj)
      if result.count() == 0: 
        print 'INSERTING (from page '+str(page)+' [q='+q+']) ' + movieId + ':\t' + movieTitle
        movies.insert(respDict['movies'][j])
      #else:
        #print 'Page '+ str(i) + ': ' + movieTitle + ' is already in the collection movies.'

    time.sleep(2)

  return
  # End of function getMovies(str q).

client = pymongo.MongoClient('da0.eecs.utk.edu')

# Get a reference to the Mongo database we will be using. It is named rt. 
db = client['rt']
movies = db.movies

for a in letters: 
  for b in letters: 
    getMovies(a+b)

client.close()
