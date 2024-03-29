"""
Module to authorize user to access Spotify web API account
"""
import base64
import requests
from spotify_api_keys import get_client_id, get_client_secret

# set up API endpoint and client credentials
URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()

# encode client credentials as base64
credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# set up headers and data for token request
headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'client_credentials'
}

# send POST request to /token endpoint
response = requests.post(URL, headers=headers, data=data, timeout=100)

# check status code to ensure successful request
if response.status_code == 200:
    # extract access token from response
    access_token = response.json()['access_token']
    # print access token
    print("Access token: ", access_token)
else:
    # handle error
    print('Error:', response.status_code)
