import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Set up the SpotiPy client with your Spotify app credentials
client_id = 'c913bd156c9545639e236dc3a0fcefeb'
client_secret = '508070c5f0614300bd7aed6b163e73d6'
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Get a list of playlists in the Million Playlist Project
playlists = sp.user_playlists('spotify', limit=1)
# limit the number of playlists to


# Iterate over each playlist and extract data for each track in the playlist
for playlist in playlists['items']:
    # Get the playlist ID and name
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    
    # Get the tracks in the playlist
    tracks = sp.playlist_items(playlist_id)['items']
    
    # Iterate over each track and extract data
    for track in tracks:
        # Get the track ID and name
        track_id = track['track']['id']
        track_name = track['track']['name']
        
        # Get additional track data
        track_data = sp.track(track_id)
        track_album = track_data['album']['name']
        track_artists = ', '.join([artist['name']
                                   for artist in track_data['artists']])
        track_release_date = track_data['album']['release_date']
        track_length = track_data['duration_ms']
        track_popularity = track_data['popularity']
        
        # Print the sample extracted data for the track
        print("\nData")
        print("=" * 50)
        print(f"Playlist: {playlist_name}")
        print(f"Track: {track_name}")
        print(f"Album: {track_album}")
        print(f"Artists: {track_artists}")
        print(f"Release Date: {track_release_date}")
        print(f"Length: {track_length} ms")
        print(f"Popularity: {track_popularity}")
        print("=" * 50)
