from pytwitter import Api
api = Api(bearer_token="Your bearer token")

api = Api(consumer_key="consumer key",consumer_secret="consumer secret",oauth_flow=True)
# get url for user to authorize
api.get_authorize_url()
# copy the response url
api.generate_access_token("https://localhost/?oauth_token=oauth_token&oauth_verifier=oauth_verifier")
{'oauth_token': 'oauth_token',
 'oauth_token_secret': 'oauth_token_secret',
 'user_id': '123456',
 'screen_name': 'screen name'}
