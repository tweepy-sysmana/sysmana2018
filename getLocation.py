#!/usr/bin/env python
# -*- coding: utf-8 -*-

#obtenemos la localizacion de los tweets que recoja nuestro filtro
import tweepy
import codecs
from secret import *

api = init_twitter('sysmanapy')

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):		#recogemos todos los tweets que contengan el filtro indicado
		print('Autor: '+status.user.screen_name)
		print('Estado: \n'+status.text)
		if status.coordinates:  #si puede extraer las coordenadas, las muestra
			print '\ncoords:'+ status.coordinates
		if status.place:  #si puede extraer el lugar, lo muestra
			print '\nplace:'+ status.place.full_name
		print("-"*10)

if __name__ == '__main__':

    #Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['sysmana2018'])
