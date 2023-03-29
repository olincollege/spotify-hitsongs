# Import the functions to test
from spotifydata import get_spotify_data
from visualization import create_visualizations

# Import Spotify API keys functions
from spotify_api_keys import get_client_id, get_client_secret

print("\n")
print("=" * 50)
print("Obtaining API Keys")
print("=" * 50)

# Get API keys
CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()

# Get Spotify Data and save data into csv file
data = get_spotify_data(CLIENT_ID, CLIENT_SECRET)

# Create visualizations from csv file
create_visualizations('data.csv', 'figures')

print("\n")
print("=" * 50)
print("Everything successfully executed!")
print("=" * 50)
