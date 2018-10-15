import tweepy
#Authentication keys

# credentials ={

# 	'nieves': {

# 		'consumer_key' : '',

# 		'consumer_secret' : '',

# 		'access_token' : '-',

# 		'access_token_secret' : ''
# 	},

# 	'pablo': {

# 		'consumer_key' : '',

# 		'consumer_secret' : '',

# 		'access_token' : '-',

# 		'access_token_secret' : ''
# 	},

# 	'sysmanapy': {

# 		'consumer_key' : '',

# 		'consumer_secret' : '',

# 		'access_token' : '-',

# 		'access_token_secret' : ''
# 	}
# }

class TwitterAuthApi:
	def __init__(self, credentials):
		self.credentials = credentials

	def get_user_api(self, username):
		auth = tweepy.OAuthHandler(
			self.credentials[u]['consumer_key'],
			self.credentials[u]['consumer_secret'])
		auth.set_access_token(
			self.credentials[u]['access_token'],
			self.credentials[u]['access_token_secret'])

		return tweepy.API(auth)
