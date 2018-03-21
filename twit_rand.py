#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv

#Variables that contains the user credentials to access Twitter API 
access_token = "3632658623-IFtneiy2z5Wwt5RJOsEsCVQx29MQQ6iuBmAJyVC"
access_token_secret = "sVc8z8hAvV3Q6VYWiAnEcRRnTCIEddrXXZi8ic0GbJIju"
consumer_key = "2X5YHHy3hXOnGqViXnlFMKHZM"
consumer_secret = "1VKgqnkngGUavNXJ3zdeQvG4BaH9CQoZBbedl6YSxvKXq5uINE"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, api=None, limit=1):
        super(StdOutListener, self).__init__()
        self.limit = limit
        self.i = 0
        self.tweets = [0] * self.limit

    def on_status(self, status):
        self.tweets[self.i] = status.text
        self.i += 1

        if(self.i < self.limit):
            return True
        else:
            return False

    def on_error(self, status):
        print (status)

#finds the total ascci value of the tweet
def getAggregateASCII(tweets):

    randomNumbers = [0] * len(tweets)

    for i in range(0, len(tweets)):
        for j in range(0, len(tweets[i])):
            randomNumbers[i] += ord((tweets[i])[j])

    return randomNumbers

#saves the random numbers to a csv file
def writeToCSV(randomNumbers):
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(randomNumbers)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    listener = StdOutListener(auth, 100)#fetches 100 tweets
    stream = Stream(auth, listener)

    stream.sample()

    tweets = listener.tweets
    writeToCSV(getAggregateASCII(tweets))

