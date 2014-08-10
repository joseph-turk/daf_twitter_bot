#!/usr/bin/python

import twitter
from OAuthSettings import settings
import MySQLdb

# set api variables from oauthsettings
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="dafbot", # your username
                     passwd="dafbot", # your password
                     db="daf") # name of the data base

# create cursor
cur = db.cursor()

# get a random row from the lyrics table
getRow = "SELECT content, contentID FROM lyrics_prod ORDER BY RAND() LIMIT 1"
cur.execute(getRow)

tweet = cur.fetchall()
tweetThis = tweet[0][0]
tweetID = tweet[0][1]
print tweetThis

# post to twitter
try:
  api = twitter.Api(
  consumer_key = consumer_key,
  consumer_secret = consumer_secret,
  access_token_key = access_token_key,
  access_token_secret = access_token_secret)

  status = api.PostUpdate(tweetThis)
  print 'post successful!'

except twitter.TwitterError:
  print 'error posting!'

# delete the row
deleteRow = "DELETE FROM lyrics_prod WHERE contentID=%s"%(tweetID)
cur.execute(deleteRow)
db.commit()
db.close()
