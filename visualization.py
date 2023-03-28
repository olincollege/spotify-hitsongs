"""
Module to Plot and Visualize Data
"""
import pandas as pd
import matplotlib.pyplot as plt

from data import load_data, extract_column

# Load the Spotify data from csv file
spotify_data = load_data('data.csv')


#playlist_name = extract_column(spotify_data, 'playlist_name')
