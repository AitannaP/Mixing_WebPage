# get token

import requests
import json

# Replace with your actual client id and secret
client_id = "8bba093121064231a91f19d7ec70757b"
client_secret = "enter secret"

# Endpoint for Spotify token access
token_url = "https://accounts.spotify.com/api/token"

# Request body parameters
payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

# Set headers for content type
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Send POST request for access token
response = requests.post(token_url, headers=headers, data=payload)

# Check for successful response (200 OK)
if response.status_code == 200:
    # Parse the JSON response to get access token
    data = response.json()
    access_token = data["access_token"]
    print("Successfully obtained access token:", access_token)
    
    # Use the access token for further Spotify API calls here...
    
else:
    print("Error obtaining access token:", response.status_code, response.text)


#search for single based onSpotify ID

search_artist_name = input('Please type you song you want to search?\n')
search_song_name = input('Please type you artist you want to search?\n')


secret = '899584a8168442cda47824803bfde729'
client_id = '8bba093121064231a91f19d7ec70757b'
api_auth = 'https://accounts.spotify.com/api/token'
album_url = 'https://api.spotify.com/v1/albums/'
search_url = f'https://api.spotify.com/v1/search?q=remaster%2520track%3A{search_song_name}%2520artist%3A{search_artist_name}&type=track&limit=1'
track_url = "https://api.spotify.com/v1/me/shows?offset=0&limit=20"
token= access_token
single = 'https://api.spotify.com/v1/audio-analysis/11dFghVXANMlKmJXsNCbNl' # with key and tempo

headers = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'secret': secret
}

h = {
    'Authorization': f'Bearer {token}' 
}



#search song 
session = requests.Session()
search_res = session.get(search_url, headers=h)
result = search_res.text

spotify_song_id = search_res.json()
spotify_song_id = spotify_song_id['tracks']['items'][0]['id']



#search for single based onSpotify ID
single_url = f'https://api.spotify.com/v1/audio-analysis/{spotify_song_id}' # with key and tempo

headers = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'secret': secret
}

h = {
    'Authorization': f'Bearer {token}',
    "Content-Type": "application/json" 

}
session = requests.Session()
search_res = session.get(single_url, headers=h)

result = search_res.text
song_audio_analysis = search_res.json()
data = song_audio_analysis


final = { 'spotify_song_id': spotify_song_id,
    'time_signature': data['track']['time_signature'],
    'key' : data['track']['key'],
    'mode' : data['track']['mode'],
    'tempo' : data['track']['tempo'],
    'artist': search_artist_name, 
    'song': search_song_name
    
    }
with open("output.json", "w") as f:
     # Write the result to the file
     json.dump(final, f, indent=4) 



