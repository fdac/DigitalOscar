#!/usr/bin/python

# This script returns a projection from the MongoDB collection movies in the database rt on the server DA0.EECS.UTK.EDU. 
# Its output is intended to be redirected to a file. 

import pymongo

client = pymongo.MongoClient('da0.eecs.utk.edu')

db = client['rt']

print "Title"

for it in db.movies.find({}, {'title':1}): #[:100]: #Used to limit return values. 
  
  movieTitle = it['title']

  print movieTitle

client.close()
