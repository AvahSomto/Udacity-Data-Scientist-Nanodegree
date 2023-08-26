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
    row = dis_categories.iloc[0]

    # Apply a lambda function to create new column names
    dis_category_colnames = row.apply(lambda x: x.str[:-2]).values.tolist()
    # rename the columns of 'categories'
    dis_categories.columns = dis_category_colnames

    # Assuming 'df' is your DataFrame
    # Iterate through each column in the DataFrame
    # Check if the column is of type 'object' (i.e., string)
    # and the category columns in 'df' should only contain the last character of each string
    for column in dis_categories:
    # Iterate through each element in the collection.
    # For each element, retrieve the last character of the string.
    # Assign the last character as the new value for that element.
        dis_categories[column] = dis_categories[column].astype(str).str[-1]

    # Type casting
    dis_categories[column] = dis_categories[column].astype(int)

    # Substituting 2s for 1s
    dis_categories['related'] = dis_categories['related'].replace(to_replace=2, value=1)

    # Assuming the original categories column is named 'categories'
    df.drop('categories', axis=1, inplace=True)
    # Merging the old and new dataframe using concatenation
    df = pd.concat([df, dis_categories], axis=1)
    # drop duplicates
    df.drop_duplicates(inplace=True)
    return df
    
def save_data(df, database_filepath):
    """df will be stored in a SQLite database."""
    engine = create_engine(f'sqlite:///{database_filepath}')
    df.to_sql('SELECT * from disaster_messages', con=engine, index=False, if_exists='replace')


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
