"""
Module containing functions for Data Processing
"""
import pandas as pd


def load_data(filename):
    """
    Function to load data from a csv file

    Args:
        filename: A string with filename and .csv extension

    Returns:
        A Pandas DataFrame of the csv file
    """
    data = pd.read_csv(str(filename))
    print(data.head())
    return data


def extract_column(data, column):
    """
    Function to extract the desired column from a Pandas DataFrame.

    Args:
        data: A Pandas DataFrame
        column: A string containing the name of the desired column

    Returns:
        The extracted column of data
    """
    column = data[str(column)]
    print(column.head())
    return column
