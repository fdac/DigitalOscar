#!/usr/bin/python

# This script returns a projection from the MongoDB collection movies in the database rt on the server DA0.EECS.UTK.EDU. 
# Its output is intended to be redirected to a file. 

import pymongo

client = pymongo.MongoClient('da0.eecs.utk.edu')

db = client['rt']

print "RTID\tTitle\tCritics_Score\tAudience_Score\tCritics_Rating\tAudience_Rating\tTheater_Release_Date\t"+\
      "Cast_One_Name\tCast_One_Id\tCast_Two_Name\tCast_Two_Id\tCast_Three_Name\tCast_Three_Id\tCast_Four_Name\tCast_Four_Id\tCast_Five_Name\tCast_Five_Id\n"

for it in db.movies.find({}, {'id':1, 'title':1, 'ratings':1, 'critics_consensus':1, 'release_dates':1, 'abridged_cast':1, '_id':0}): #[:100]: Used to limit return values. 
  
  rtId = it['id']
  movieTitle = it['title']

  if 'critics_score' in it['ratings'].keys():
    critics_score = str(it['ratings']['critics_score'])
  else: critics_score = 'NA'

  if 'audience_score' in it['ratings'].keys():
    audience_score = str(it['ratings']['audience_score'])
  else: audience_score = 'NA'
  
  if 'critics_rating' in it['ratings'].keys():
    critics_rating = it['ratings']['critics_rating']
  else: critics_rating = 'NA'
  
  if 'audience_rating' in it['ratings'].keys():
    audience_rating = it['ratings']['audience_rating']
  else: audience_rating = 'NA'
  
  if 'release_dates' in it.keys() and 'theater' in it['release_dates'].keys():
    theater_release_date = it['release_dates']['theater']
  else: theater_release_date = 'NA'

  if 'abridged_cast' in it.keys(): 
    nCast = len(it['abridged_cast'])
    if nCast >= 1: 
      cast_one_name = it['abridged_cast'][0]['name']
      cast_one_id = str(it['abridged_cast'][0]['id'])
    else: 
      cast_one_name = 'NA'
      cast_one_id = 'NA'
    if nCast >= 2: 
      cast_two_name = it['abridged_cast'][1]['name']
      cast_two_id = str(it['abridged_cast'][1]['id'])
    else: 
      cast_two_name = 'NA'
      cast_two_id = 'NA'
    if nCast >= 3: 
      cast_three_name = it['abridged_cast'][2]['name']
      cast_three_id = str(it['abridged_cast'][2]['id'])
    else: 
      cast_three_name = 'NA'
      cast_three_id = 'NA'
    if nCast >= 4: 
      cast_four_name = it['abridged_cast'][3]['name']
      cast_four_id = str(it['abridged_cast'][3]['id'])
    else: 
      cast_four_name = 'NA'
      cast_four_id = 'NA'
    if nCast >= 5: 
      cast_five_name = it['abridged_cast'][4]['name']
      cast_five_id = str(it['abridged_cast'][4]['id'])
    else: 
      cast_five_name = 'NA'
      cast_five_id = 'NA'
  else: 
    cast_one_name = 'NA'
    cast_one_id = 'NA'
    cast_two_name = 'NA'
    cast_two_id = 'NA'
    cast_three_name = 'NA'
    cast_three_id = 'NA'
    cast_four_name = 'NA'
    cast_four_id = 'NA'
    cast_five_name = 'NA'
    cast_five_id = 'NA'
      
  print rtId +'\t'+ \
    movieTitle +'\t'+ \
    critics_score +'\t'+ \
    audience_score +'\t'+\
    critics_rating +'\t'+\
    audience_rating +'\t'+\
    theater_release_date +'\t'+\
    cast_one_name +'\t'+\
    cast_one_id +'\t'+\
    cast_two_name +'\t'+\
    cast_two_id +'\t'+\
    cast_three_name +'\t'+\
    cast_three_id +'\t'+\
    cast_four_name +'\t'+\
    cast_four_id +'\t'+\
    cast_five_name +'\t'+\
    cast_five_id +'\t'

client.close()
