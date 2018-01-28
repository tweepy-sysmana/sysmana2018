#obteniendo localizacion de los tweets
import tweepy
import codecs
from secret import *

api = init_twitter('sysmanapy')

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):			
		print('Autor: '+status.user.screen_name)
		print('Estado: \n'+status.text)
		if status.coordinates:
			print '\ncoords:'+ status.coordinates
		if status.place:
			print '\nplace:'+ status.place.full_name
		print("-"*10)

if __name__ == '__main__':

    #Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['probandoSysmana'])
