# Disaster Response Pipeline Project

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libaries used for this project is python 3.7 and above, pandas, numpy, matplotlib, pickle, re, nltk, sklearn, sys,
sqlalchemy, sqlite3 and the platform was DataSpell.  The code should run with no issues using 
Python versions 3.*.

## Project Motivation<a name="motivation"></a>

In this project, I applied data engineering skills to analyze disaster data from [Appen](https://appen.com/)
(formally Figure 8) to 
build a model for an API that classifies disaster messages.
I used a data set containing real messages that were sent during disaster events. I created a machine learning pipeline
to categorize these events so that a emergency worker can send these messages to an appropriate disaster relief agency.
In this project I included a web app where an emergency worker can input a new message and get classification results
in several categories. The web app will also display visualizations of the data.
Below are a few screenshots of the web app.

![Disaster Response Project image.jpg](Disaster%20Response%20Project%20image.jpg)


![Disaster Response Project active image.jpg](Disaster%20Response%20Project%20active%20image.jpg)


## File Descriptions <a name="files"></a>

There are three components for this project.

1. ETL Pipeline
   In a Python script, process_data.py, write a data cleaning pipeline that:

   Loads the messages and categories datasets
   Merges the two datasets
   Cleans the data
   Stores it in a SQLite database

2. ML Pipeline
   In a Python script, train_classifier.py, write a machine learning pipeline that:

   Loads data from the SQLite database
   Splits the dataset into training and test sets
   Builds a text processing and machine learning pipeline
   Trains and tunes a model using GridSearchCV
   Outputs results on the test set
   Exports the final model as a pickle file

3. Flask Web App

   File paths were modified for database and model as needed and data visualizations using Plotly 
   was added in the web app.

## Results<a name="results"></a>

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
      `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
      `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

(base) PS C:\Users\Just Me\Downloads\Disaster Response Pipeline> cd app
(base) PS C:\Users\Just Me\Downloads\Disaster Response Pipeline\app> python run.py
* Serving Flask app 'run'
* Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:3000
* Running on http://11.243.53.195:3000                                                                               
  Press CTRL+C to quit


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Thanks to Figure 8 for the data. Thanks to Udacity for the starter code and workspace provided.