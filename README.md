This project generates a random tweet from a database of Doubles as a Frisbee lyrics.

getLyricsTest.py queries the test database and deletes the selected lyrics after printing, but does not post a tweet.
getLyrics.py queries the production database, tweets the selected lyrics, and then deletes the selected lyrics.

Note: these scripts are written to pull data from my local mySQL database. You'll need to connect them to your own database. Similarly, the OAuth settings for connecting to my Twitter app are not included here. You'll need to supply your own OAuthSettings.py file with a settings object.
