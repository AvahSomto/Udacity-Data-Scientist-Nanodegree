# import libraries
import re
import sys
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

nltk.download(['punkt', 'wordnet'])


def load_data(database_filepath):
    """
    Loading the data from the SQLite database.
    
    Parameters:
    database_filepath: Filepath to the database
    
    Returns:
    X: Feature variable
    y: Target variable
    """
    # load data from database 
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table("disaster_messages", con=engine)
    df = pd.read_sql("SELECT * from disaster_messages",con=engine)
    X = df['message']
    y = df.iloc[:, 4:]
    return X,y


def tokenize(disaster_text):
   """
   Tokenizes and lemmatizes text.
    
   Parameters:
   text: Text to be tokenized
    
   Returns:
   clean_tokens: Returns cleaned tokens 
   """
   tokens = word_tokenize(disaster_text)
   lemmatizer = WordNetLemmatizer()

   clean_tokens=[]
   for tok in tokens:
       clean_tok = lemmatizer.lemmatize(tok).lower().strip()
       clean_tokens.append(clean_tok)

   return clean_tokens



def build_model():
    """
    Classifier building and model tuning using GridSearchCV.
    
    Returns:
    cv: Cross-validation
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    parameters = {
        'clf__estimator__n_estimators' : [50, 150]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv



from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluating the model performance and returning various evaluation metrics.

    Parameters:
    model: classifier
    X_test: test dataset
    y_test: test data labels in X_test

    Returns:
    Dictionary containing evaluation metrics
    """
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    classification_rep = classification_report(y_test, y_pred)

    evaluation_metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'classification_report': classification_rep
    }

    return evaluation_metrics

    y_pred = model.predict(X_test)
    for index, column in enumerate(y_test):
        print(column, classification_report(y_test[column], y_pred[:, index]))




def save_model(model, model_filepath):
    """Export the final model using Joblib."""
    joblib.dump(model, model_filepath)




def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, y = load_data(database_filepath)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
#%%
