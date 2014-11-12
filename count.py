#!/bin/python
# This script prints the number of documents in the rt collection movies.

import pymongo

client = pymongo.MongoClient('da0.eecs.utk.edu')

db = client['rt']
movies = db.movies

print movies.count()

client.close()
