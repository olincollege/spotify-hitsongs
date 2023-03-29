#!/usr/bin/env python
# coding: utf-8

import unittest
import pandas as pd
import os

# Import the functions to test
from spotifydata import get_spotify_data
from visualization import create_visualizations

# Import API keys functions
from spotify_api_keys import get_client_id, get_client_secret

CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()


class TestGetData(unittest.TestCase):
    
    def test_get_spotify_data(self):
        """
        Unit test function for the get_spotify_data function.

        This function tests that the get_spotify_data function returns a
        Pandas DataFrame with the expected columns,
        contains at least one row, and contains no null values.
        """
        # Test that the function returns a Pandas DataFrame
        df = get_spotify_data(CLIENT_ID, CLIENT_SECRET)
        self.assertIsInstance(df, pd.DataFrame)
        
        # Test that the DataFrame contains the expected columns
        expected_columns = ["playlist_name", "track_name", "track_album",
                            "track_artists", "track_release_date",
                            "track_length", "track_popularity",
                            "track_explicit", "track_markets"]
        self.assertListEqual(list(df.columns), expected_columns)
        
        # Test that the DataFrame contains at least one row
        self.assertGreaterEqual(df.shape[0], 1)
        
        # Test that the DataFrame contains no null values
        self.assertFalse(df.isnull().values.any())

    def test_create_hit_song_visualization(self):
        """
            Test function for create_visualizations
        """
        # Test that the function returns None
        data_file = "data.csv"
        output_dir = "figures"
        result = create_visualizations(data_file, output_dir)
        self.assertIsNone(result)

        # Test that the visualization files are created
        self.assertTrue(
            os.path.exists(output_dir + "/popularity_distribution.png"))
        self.assertTrue(
            os.path.exists(output_dir + "/length_vs_popularity.png"))
        self.assertTrue(
            os.path.exists(output_dir + "/explicit_content_vs_popularity.png"))
        self.assertTrue(
            os.path.exists(output_dir + "/top_artists_by_popularity.png"))
        self.assertTrue(
            os.path.exists(output_dir + "/release_date_distribution.png"))
        self.assertTrue(
            os.path.exists(output_dir + "/available_markets_distribution.png"))
