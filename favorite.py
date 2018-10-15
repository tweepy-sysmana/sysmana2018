#Manda un fav a los tweets que contengan el patron
import tweepy
import codecs
from secret import *

api = init_twitter('sysmanapy')

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
	    print('Autor: '+status.user.screen_name)
	    print('Estado: \n'+status.text)
	    print("-"*10)

	    api.create_favorite(status.id);
	    api.update_status("Genial! soy el script de @nievesborrero y @PabloLeonPsi, encantado @",in_reply_to_status_id=status.id);
