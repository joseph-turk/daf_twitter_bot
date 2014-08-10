#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="dafbot", # your username
                     passwd="dafbot", # your password
                     db="daf") # name of the data base

# create cursor
cur = db.cursor()

# get a random row from the lyrics table
getRow = "SELECT content, contentID FROM lyrics_test ORDER BY RAND() LIMIT 1"
cur.execute(getRow)

tweet = cur.fetchall()
tweetThis = tweet[0][0]
tweetID = tweet[0][1]
print tweetThis

# delete the row
deleteRow = "DELETE FROM lyrics_test WHERE contentID=%s"%(tweetID)
cur.execute(deleteRow)
db.commit()
db.close()
