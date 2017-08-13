#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser
import sys

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
        
def prop_loader(prop_file):
    cp = configparser.RawConfigParser()
    cp.read(prop_file)

    global access_token, access_token_secret, consumer_key, consumer_secret, filter_words, output_file
    
    access_token = cp.get('main_section', 'access_token')
    access_token_secret = cp.get('main_section', 'access_token_secret')
    consumer_key = cp.get('main_section', 'consumer_key')
    consumer_secret = cp.get('main_section', 'consumer_secret')
    filter_words = cp.get('main_section', 'filter_words')
    output_file = cp.get('main_section','output_file')
    


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    prop_loader('settings.properties.txt')
    sys.stdout = open(output_file, 'w+')
    l = StdOutListener()
    auth = OAuthHandler('**', '**')
    auth.set_access_token('**', '**')
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['cindy'])
    #target.write("\n")  
