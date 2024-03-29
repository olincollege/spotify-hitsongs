"""
Module for Data Extraction using Spotify API and Data Processing
"""
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_data(client_id, client_secret):
    # pylint: disable-msg=too-many-locals
    """
    Extracts data for each track from 50 playlists of the
    Million Playlist Project on Spotify,
    using the Spotify API and the provided client ID and secret.

    Parameters:
        client_id (str): The client ID for the Spotify API
            authentication.
        client_secret (str): The client secret for the Spotify API
            authentication.

    Returns:
        pandas.DataFrame: A DataFrame containing the extracted track data,
            with the following columns:
        - playlist_name: The name of the playlist the track belongs to.
        - track_name: The name of the track.
        - track_album: The name of the album the track belongs to.
        - track_artists: A comma-separated string with the names of the artists
            who performed the track.
        - track_release_date: The release date of the album the track belongs
            to, in YYYY-MM-DD format.
        - track_length: The length of the track, in milliseconds.
        - track_popularity: The popularity of the track, on a scale
            from 0 to 100.
        - track_explicit: A boolean indicating whether the track has
            explicit lyrics.
        - track_markets: The number of markets where the track is available.
        - track_album_type: The type of album the track belongs to
            (album, single, compilation, etc.).
    """
    # Authenticate with Spotify API
    auth_manager = SpotifyClientCredentials(client_id=client_id,
                                            client_secret=client_secret)
    sp = spotipy.Spotify(  # pylint: disable=invalid-name
        auth_manager=auth_manager)

    # List to store data
    data = []

    # Get a list of playlists in the Million Playlist Project
    playlists = sp.user_playlists('spotify', limit=50)
    # limit the number of playlists to 50

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
            try:
                track_id = track['track']['id']
            except TypeError:
                continue
            track_name = track['track']['name']

            # Get additional track data
            track_data = sp.track(track_id)
            track_album = track_data['album']['name']
            track_artists = ', '.join(  # pylint: disable=invalid-name
                [artist['name']
                 for artist in track_data['artists']])
            track_release_date = track_data['album']['release_date']
            track_length = track_data['duration_ms']
            track_popularity = track_data['popularity']
            track_explicit = track_data['explicit']
            track_markets = len(track_data['available_markets'])
            track_album_type = track_data['album']['album_type']

            # Appending the list with track data
            data.append([playlist_name, track_name, track_album,
                         track_artists, track_release_date, track_length,
                         track_popularity, track_explicit, track_markets,
                         track_album_type])

    # Converting list to Pandas DataFrame
    data = pd.DataFrame(data)

    # Exporting track data into a csv file
    data.to_csv("data.csv",
                header=["playlist_name", "track_name", "track_album",
                        "track_artists", "track_release_date",
                        "track_length", "track_popularity", "track_explicit",
                        "track_markets", "track_album_type"],
                index=False)

    return data
