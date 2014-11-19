#!/usr/bin/python

# This script prints a 2-column table from the collection movies in the database rt on the server DA0.EECS.UTK.EDU.
# The first column is the Rotten Tomatoes ID and the second is the Rotten Tomatoes synopsis. 
# Its output is intended to be redirected to a file. 

import pymongo

client = pymongo.MongoClient('da0.eecs.utk.edu')

db = client['rt']

print 'RTID\tSynopsis\n'

for it in db.movies.find({}, {'id':1, 'synopsis':1, '_id':0}): #[:10]: #Used to limit return values. 
  
  rtId = it['id']

  if 'synopsis' in it.keys():
    synopsis = it['synopsis']
    if synopsis == '': 
      synopsis = 'NA'
  else: synopsis = 'NA'

  print rtId + '\t' + synopsis

client.close()
