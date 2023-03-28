# spotify-hitsongs

Sparsh Gupta and Sohum Kothavade

## Project Description

In this project, we explore how certain non-musical factors, for example, release date of songs, album, etc. are correlated to the 'popularity' of a song and how these factors affect the successfulness of a song.

For understanding this project thouroughly, please access the computational essay `spotify-hitsongs.ipynb` inculded in this repository.

## Dependencies

|  Package  |      Uses       |
|-----------|-----------------|
| Matplotlib| Visualization   |
| Pandas    | Data Processing |
| Requests  | web API         |
| SpotiPy   | Spotify API     |

 The dependencies are present in `requirements.txt` and can be installed using the following in terminal:
 
 ```
 pip install -r requirements.txt
 ```
 
## Data

The data used in this study is from Spotify's ['The Million Playlist'](https://research.atspotify.com/2020/09/the-million-playlist-dataset-remastered/) dataset. We obtained the data used in this study from Spotify's API which gives us access to a million playlists of songs consisting of more than a hundred million songs/tracks.

We obtain the web API access keys which includes `CLIENT_ID` and `CLIENT_SECRET` from [Spotify Developer Tools](https://developer.spotify.com) by creating a developer account and a project.

The sample extracted data output can be seen below:

![](samplespotifydata.png)

## Data Extraction

We used the module `spotifydata.py` to extract data from Spotify's web API. Please refer to this module for detailed instructions to extract and process spotify API data.

We first set up the SPotiPy client using our Spotify API access credentials:
```
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```

Then, using the SpotiPy client, we get a list of playlists from Spotify's data:
```
playlists = sp.user_playlists('spotify', limit=50)
```

## Data Processing

Using Pandas, we process the dataset accessed through the API and store it to the csv file `data.csv`

## Visualization
