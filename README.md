This is a random number generator that uses a stream of tweets as it's source of entropy. It uses tweepy
to access tweets using the Twitter streaming API which provides a reasonably high rate of tweets. It
then takes the total ascii value of the charatcers in these tweets to generate a random number. Random
as far as the specific set of characters a random human tweets at a random time are random. It is however
not a partcularly fast method of obtaining random numbers, but it is free and requires no equipment other
than a computer and an internet connection.
