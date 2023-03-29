#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_api_keys import get_client_id, get_client_secret


# Set up the SpotiPy client with your Spotify app credentials
client_id = get_client_id()
client_secret = get_client_secret()
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Get a list of playlists in the Million Playlist Project
playlists = sp.user_playlists('spotify', limit=50)
# limit the number of playlists to

print("\nData")
print("=" * 50)

# List to store data
data = []

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
        track_artists = ', '.join([artist['name']
                                   for artist in track_data['artists']])
        track_release_date = track_data['album']['release_date']
        track_length = track_data['duration_ms']
        track_popularity = track_data['popularity']
        track_explicit = track_data['explicit']
        track_markets = len(track_data['available_markets'])
        track_album_type = track_data['album']['album_type']
        
        # Print the sample extracted data for the track
        print(f"Playlist: {playlist_name}")
        print(f"Track: {track_name}")
        print(f"Album: {track_album}")
        print(f"Artists: {track_artists}")
        print(f"Release Date: {track_release_date}")
        print(f"Length: {track_length} ms")
        print(f"Popularity: {track_popularity}")
        print(f"Explicit: {track_explicit}")
        print(f"Number of Available Markets: {track_markets}")
        print(f"Album Type: {track_album_type}")
        print("=" * 50)

        # Appending the list with track data
        data.append([playlist_name, track_name, track_album,
                    track_artists, track_release_date, track_length,
                    track_popularity, track_explicit, track_markets,
                    track_album_type])

# Converting list to Pandas DataFrame
data = pd.DataFrame(data)

# # Exporting track data into a csv file
# data.to_csv("data.csv",
#             header=["playlist_name", "track_name", "track_album",
#                     "track_artists", "track_release_date",
#                     "track_length", "track_popularity", "track_explicit",
#                     "track_markets", "track_album_type"],
#             index=False)

# Exporting track data into a csv file in the current directory
current_directory = os.getcwd()
data_file_path = os.path.join(current_directory, "data.csv")
data.to_csv(data_file_path,
            header=["playlist_name", "track_name", "track_album",
                    "track_artists", "track_release_date",
                    "track_length", "track_popularity", "track_explicit",
                    "track_markets", "track_album_type"],
            index=False)


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Create histogram
plt.hist(data['track_popularity'], bins=20)
plt.xlabel('Popularity')
plt.ylabel('Frequency')
plt.title('Popularity Distribution')
plt.show()


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Create scatter plot
plt.scatter(data['track_length'], data['track_popularity'])
plt.xlabel('Track Length (ms)')
plt.ylabel('Popularity')
plt.title('Track Length vs. Popularity')
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Group data by explicit content and calculate mean popularity
mean_popularity = data.groupby('track_explicit')['track_popularity'].mean()

# Create bar chart
plt.bar(mean_popularity.index.astype(str), mean_popularity)
plt.xlabel('Explicit Content')
plt.ylabel('Mean Popularity')
plt.title('Explicit Content vs. Popularity')
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Count number of albums in each type
album_counts = data['track_album_type'].value_counts()

# Create pie chart
plt.pie(album_counts, labels=album_counts.index, autopct='%1.1f%%')
plt.title('Album Type Distribution')
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Group data by artist and calculate mean popularity
mean_popularity = data.groupby('track_artists')['track_popularity'].mean()

# Sort by popularity and select top 10
top_artists = mean_popularity.sort_values(ascending=False).head(10)

# Create horizontal bar chart
plt.barh(top_artists.index, top_artists)
plt.xlabel('Mean Popularity')
plt.title('Top 10 Artists by Popularity')
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Convert release date to datetime and group by year/month
data['release_date'] = pd.to_datetime(data['track_release_date'])
data['year_month'] = data['release_date'].dt.to_period('M')
release_counts = data['year_month'].value_counts().sort_index()

# Create line chart
plt.plot(release_counts.index.astype(str), release_counts)
plt.xlabel('Year/Month')
plt.ylabel('Number of Hit Songs')
plt.title('Release Date Distribution')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Create box plot
plt.boxplot(data['track_markets'])
plt.ylabel('Number of Available Markets')
plt.title('Available Markets Distribution')
plt.show()

