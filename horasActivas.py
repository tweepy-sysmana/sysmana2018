#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Devuelve una estimacion en base a 200 tweets de las horas a las que suele conectarse un usuario
import tweepy, codecs, sys
from secret import *

api = init_twitter('sysmanapy');

manana = tarde = noche = 0


def horas(user):
	for tweets in api.user_timeline(screen_name=user, count=200): # Recorremos el timeline del usuario.
		global manana
		global tarde
		global noche
		dateTime = str(tweets.created_at) # Recogemos la fecha
		array = dateTime.split()
		time = array[1].split(":")
		if(int(time[0])<14):
			manana+=1
		else:
			if(int(time[0])>20):
				noche+=1
			else:
				tarde+=1
	manana = manana/2
	tarde = tarde/2
	noche = noche/2


if __name__ == '__main__':
	horas(user)
	print("--Estadística de twiteo de "+user+"--")
	print('madrugando: '+str(manana)+"%")
	print('tarde: '+str(tarde)+"%")
	print('trasnochando: '+str(noche)+"%")
