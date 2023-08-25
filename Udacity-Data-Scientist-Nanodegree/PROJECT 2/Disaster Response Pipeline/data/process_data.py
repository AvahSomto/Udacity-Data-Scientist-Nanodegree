import sys
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine


import pandas as pd

def load_data(messages_filepath, categories_filepath):
    """
    Loads and merges datasets from two filepaths.

    Parameters:
    messages_filepath (str): Path to the messages CSV file.
    categories_filepath (str): Path to the categories CSV file.

    Returns:
    df (pd.DataFrame): Merged dataframe containing messages and categories.

    Raises:
    FileNotFoundError: If either of the input filepaths does not exist.
    ValueError: If the input filepaths are not in the correct format.

    """
    try:
        # Validate filepaths
        if not (messages_filepath.endswith('.csv') and categories_filepath.endswith('.csv')):
            raise ValueError("Filepaths must be in CSV format.")

        # Load datasets
        messages = pd.read_csv(messages_filepath)
        categories = pd.read_csv(categories_filepath)

        # Merge datasets
        df = pd.merge(messages, categories, on='id')

        return df

    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please provide valid filepaths.")

def load_and_merge_datasets(messages_filepath, categories_filepath):
    # Load datasets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # Merge datasets on common id and assign to df
    df = pd.merge(messages, categories, on='id', how='outer')

    return df



def clean_dataframe(df) -> pd.DataFrame:
    """
    Cleans the dataframe by performing specific cleaning operations.

    Parameters:
    df: pd.DataFrame
        The input DataFrame to be cleaned.

    Returns:
    pd.DataFrame
        The cleaned DataFrame.
    """
    # create a dataframe of the 36 individual category columns
    dis_categories = df["categories"].str.split(';', expand=True)
    # select first row of the categories dataframe
    row = dis_categories[0:1]
    # apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    # to create new column names for categories
    dis_category_colnames = row.apply(lambda x: x.str[:-2]).values.tolist()
    # rename the columns of 'categories'
    dis_categories.columns = dis_category_colnames
    
    # iterate through the category columns in df to keep only the
    # last character of the string 
    for column in dis_categories:
        # set each value to be the last character of the string
        dis_categories[column] = dis_categories[column].astype(str).str[-1]
        # convert column from string to numeric
        dis_categories[column] = dis_categories[column].astype(int)
    # replace 2s with 1s in related column
    dis_categories['related'] = dis_categories['related'].replace(to_replace=2, value=1)

    # drop the original categories column from `df`
    df.drop('categories', axis=1, inplace=True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, dis_categories], axis=1)
    # drop duplicates
    df.drop_duplicates(inplace=True)
    return df
    
def save_data(df, database_filepath):
    """Stores df in a SQLite database."""
    engine = create_engine(f'sqlite:///{database_filepath}')
    df.to_sql('disaster_messages', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_dataframe(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
#%%
