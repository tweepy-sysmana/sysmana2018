import tweepy
#Authentication keys

credentials ={
	
	'nieves': {

		'consumer_key' : '',

		'consumer_secret' : '',

		'access_token' : '-',

		'access_token_secret' : ''
	},

	'pablo': {
	
		'consumer_key' : '',

		'consumer_secret' : '',

		'access_token' : '-',

		'access_token_secret' : ''
	},
	
	'sysmanapy': {
	
		'consumer_key' : '',

		'consumer_secret' : '',

		'access_token' : '-',

		'access_token_secret' : ''
	}
}

def init_twitter(u):
	auth = tweepy.OAuthHandler(credentials[u]['consumer_key'], credentials[u]['consumer_secret'])
	auth.set_access_token(credentials[u]['access_token'], credentials[u]['access_token_secret'])
	return tweepy.API(auth)
