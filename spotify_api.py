import requests
import spotipy

CLIENT_ID = "086effcb4fbf4677a205517773c4e019"
CLIENT_SECRET = "38664d62b6a74d1682ccddee8e17a36b"

#authenticating 

AUTH_URL = "https://accounts.spotify.com/api/token"

auth_response = requests.post(AUTH_URL,{
  
  "grant_type": "client_credentials",
  "client_id" : CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  
})

#print(auth_response.status_code)

auth_response_data = auth_response.json()

#print(auth_response_data)

access_token = auth_response_data['access_token']

headers = {

'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL ='https://api.spotify.com/v1/'

artist_id = '2gzWmhOZhDN6gXL49JW9qj'

response = requests.get(BASE_URL + "artists/" + artist_id, headers = headers)
print(response.json())

