#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import pandas as pd
import os

# Import the functions to test
from spotify_data import get_spotify_data
from spotify_hit_songs_visualizations import create_hit_song_visualizations


class TestGetData(unittest.TestCase):
    
    def test_get_spotify_data(self):
        # Test that the function returns a Pandas DataFrame
        df = get_spotify_data()
        self.assertIsInstance(df, pd.DataFrame)
        
        # Test that the DataFrame contains the expected columns
        expected_columns = ["playlist_name", "track_name", "track_album",
                            "track_artists", "track_release_date",
                            "track_length", "track_popularity", "track_explicit",
                            "track_markets", "track_album_type"]
        self.assertListEqual(list(df.columns), expected_columns)
        
        # Test that the DataFrame contains at least one row
        self.assertGreaterEqual(df.shape[0], 1)
        
        # Test that the DataFrame contains no null values
        self.assertFalse(df.isnull().values.any())
        
    def test_create_hit_song_visualizations(self):
        # Test that the function returns None
        df = pd.read_csv("data.csv")
        result = create_hit_song_visualizations(df)
        self.assertIsNone(result)
        
        # Test that the visualization files are created
        self.assertTrue(os.path.exists("top_artists.png"))
        self.assertTrue(os.path.exists("top_genres.png"))
        self.assertTrue(os.path.exists("acousticness.png"))
        self.assertTrue(os.path.exists("danceability.png"))
        self.assertTrue(os.path.exists("energy.png"))
        self.assertTrue(os.path.exists("instrumentalness.png"))
        self.assertTrue(os.path.exists("liveness.png"))
        self.assertTrue(os.path.exists("loudness.png"))
        self.assertTrue(os.path.exists("speechiness.png"))
        self.assertTrue(os.path.exists("tempo.png"))
        self.assertTrue(os.path.exists("valence.png"))


# Note: The unit tests assume that the working directory is set to the directory containing the Jupyter notebook and the two Python files (get_data.py and create_visualizations.py).
