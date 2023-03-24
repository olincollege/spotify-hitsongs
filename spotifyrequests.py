import base64
import spotifyrequests

# set up API endpoint and client credentials
url = 'https://accounts.spotify.com/api/token'
client_id = '<your_client_id>'
client_secret = '<your_client_secret>'

# encode client credentials as base64
credentials = f'{client_id}:{client_secret}'
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
response = spotifyrequests.post(url, headers=headers, data=data)

# check status code to ensure successful request
if response.status_code == 200:
    # extract access token from response
    access_token = response.json()['access_token']
    # do something with access token
    print(access_token)
else:
    # handle error
    print('Error:', response.status_code)