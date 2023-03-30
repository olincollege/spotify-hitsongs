"""
Module to visualize data
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_visualizations(data_file, output_dir):
    # pylint: disable=too-many-statements
    """
    Generates various visualizations based on hit song data and saves them to
    the specified output directory.

    Args:
        data_file (str): The path to the CSV file containing hit song data.
        output_dir (str): The path to the directory where the
            visualizations will be saved.

    Returns:
        None

    Example:
        create_visualizations('hit_songs.csv', 'visualization_outputs/')
    """
    # Load data
    data = pd.read_csv(data_file)

    # Create histogram
    plt.hist(data['track_popularity'], bins=20)
    plt.xlabel('Popularity')
    plt.ylabel('Number of songs')
    plt.title('Popularity Distribution (frequency)')
    plt.savefig(output_dir + '/popularity_distribution.png')
    plt.clf()

    # Create scatter plot
    plt.scatter(data['track_length'], data['track_popularity'])
    plt.xlabel('Track Length (ms)')
    plt.ylabel('Popularity')
    plt.title('Track Length vs. Popularity')
    plt.savefig(output_dir + '/length_vs_popularity.png')
    plt.clf()

    # Group data by explicit content and calculate mean popularity
    mean_popularity = data.groupby('track_explicit')['track_popularity'].mean()
    # Create bar chart
    plt.bar(mean_popularity.index.astype(str), mean_popularity)
    plt.xlabel('Explicit Content')
    plt.ylabel('Mean Popularity')
    plt.title('Explicit Content vs. Popularity')
    plt.savefig(output_dir + '/explicit_content_vs_popularity.png')
    plt.clf()

    # Group data by artist and calculate mean popularity
    mean_popularity = data.groupby('track_artists')['track_popularity'].mean()
    # Sort by popularity and select top 10
    top_artists = mean_popularity.sort_values(ascending=False).head(10)
    # Create horizontal bar chart
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(left=0.3, right=0.8)
    plt.barh(top_artists.index, top_artists)
    plt.xlabel('Mean Popularity')
    plt.ylabel('Artists')
    plt.title('Top 10 Artists by Popularity')
    plt.savefig(output_dir + '/top_artists_by_popularity.png')
    plt.clf()

    # Convert release date to datetime and filter data
    data['release_date'] = pd.to_datetime(data['track_release_date'])
    data = data[data['release_date'] >= '2010-01-01']
    # Group by year/month and count
    data['year_month'] = data['release_date'].dt.to_period('M')
    release_counts = data['year_month'].value_counts().sort_index()
    # Select 100 random values
    random_indices = np.random.choice(len(release_counts), size=100,
                                      replace=False)
    random_values = release_counts.iloc[random_indices].sort_values()
    # Create scatter plot
    plt.figure(figsize=(15, 6))
    plt.scatter(random_values.index.astype(str), random_values, alpha=0.5)
    plt.xlabel('Year/Month', fontsize=7)
    plt.ylabel('Number of Hit Songs')
    plt.title('Random Sample of Release Date Distribution after 01/2010')
    plt.xticks(rotation=90, fontsize=7)
    plt.savefig(output_dir + '/release_date_distribution.png')
    plt.clf()

    # Create scatter plot
    plt.scatter(data['track_markets'], data['track_popularity'])
    plt.xlabel('Number of Available Markets')
    plt.ylabel('Popularity')
    plt.title('Number of Markets vs Popularity')
    plt.savefig(output_dir + '/markets_vs_popularity.png')
    plt.clf()


create_visualizations('data.csv', 'figures')
