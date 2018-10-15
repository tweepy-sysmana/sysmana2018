# -*- coding: utf-8 -*-
import logging

import tweepy


class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		logging.info('Autor: '+status.user.screen_name)
		logging.info('Estado: \n'+status.text)

		if status.coordinates:
			logging.info('\ncoords: {}'.format(status.coordinates))

		if status.place:
			logging.info('\nplace: {}'.format(status.place.full_name))
