"""
Module to visualize data
"""

import pandas as pd
import matplotlib.pyplot as plt


def create_visualizations(data_file, output_dir):
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

    print("\n")
    print("=" * 50)
    print("Plotting and Storing visualizations")
    print("=" * 50)

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
    plt.barh(top_artists.index, top_artists)
    plt.xlabel('Mean Popularity')
    plt.title('Top 10 Artists by Popularity')
    plt.savefig(output_dir + '/top_artists_by_popularity.png')
    plt.clf()

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
    plt.savefig(output_dir + '/release_date_distribution.png')
    plt.clf()

    # Create scatter plot
    plt.scatter(data['track_markets'], data['track_popularity'])
    plt.xlabel('Number of Available Markets')
    plt.ylabel('Popularity')
    plt.title('Number of Markets vs Popularity')
    plt.savefig(output_dir + '/markets_vs_popularity.png')
    plt.clf()
