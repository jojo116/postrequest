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

print(auth_response.status_code)