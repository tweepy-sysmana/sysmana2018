#
# Escucha en tiempo real y almacena los tweets en un fichero de texto
#
import tweepy
import codecs
from secret import *

api = init_twitter('sysmanapy') #### PASO 1 (Pasamos por parámetro el usuario del cual cogerá las credenciales en el fichero secret)

class MyStreamListener(tweepy.StreamListener): #### PASO 2

	#cada vez que se publica un estado
	def on_status(self, status):	#### PASO 6	Cada vez que se reciba un tweet con el filtro indicado, extraemos sus datos
		autor = status.user.screen_name
		print('Autor: '+autor)
		print('Idioma: '+status.lang)
		print('Estado: \n'+status.text)

		api.create_favorite(status.id); # Damos like y retweet
		api.update_status("Genial! soy el script de @nievesborrero y @PabloLeonPsi, encantado "+ autor , in_reply_to_status_id=status.id);

		print("-"*10)

		# Almacenamos en un documento
		with codecs.open("streamSearch.txt", "a", "utf-8") as myfile:
			myfile.write('Autor: '+status.user.screen_name+'\n')
			myfile.write('Estado: \n'+status.text+'\n')
			myfile.write('\n-----\n')


if __name__ == '__main__':

