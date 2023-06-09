# Disaster Response Pipeline Project

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

### Project Motivation
I analyzed disaster datasets from [Figure Eight](https://appen.com/) and used it to build a model 
for an API that classifies disaster messages. 
I created a machine learning pipeline to categorize real messages sent during disaster events so 
that the messages could be channeled to the appropriate disaster relief agency. 
This project includes a web app where an emergency worker can input a new message and get classification 
results in several categories. This web app will also display visualizations of the data.

## Installation <a name="installation"></a>

The libaries used for this project is python 3.7 and above, pandas, numpy, matplotlib, pickle, re, nltk, sklearn, etc 
and the platform was Jupyter Notebook.  
The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, I was interestested in classifying diaster messages so as that
1. Different NGOs can easily respond to their specific disaster focus.
2. An API that classifies diasater messages can be created and used to rescue millions of lives.


### Instructions to Interact With this Project:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
      `python process_data.py messages.csv categories.csv DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
      `python train_classifier.py DisasterResponse.db classifier.pkl`

2. Run the following command in the app's directory to run your web app.
   `python run.py`

3. Go to http://0.0.0.0:3001/


## File Descriptions <a name="files"></a>
The app folder contains:
1. A template.
2. A master.html which is also the main page of the web app.
3. A go.html which is also the classification result page of the web app.
4. A run.py which is the flask file that runs the web app.

The data folder contains:
1. A disaster categories csv file.
2. A disaster messages csv file.
3. A process data python file.
4. Finally a disaster response database file.

The models folder contains
1. A training classifier python file.

There are two Jupyter Notebooks used to create the Diasaster response webapp. They are:
1. ETL(Extract, Transform, Load) Pipeline.
2. Machine Learning (ML) Pipeline

1. ETL Pipeline
   It has a process data python file that loads in the datasets, merges the datasets, 
   clean and store the datasets in an SQLite database.

2. ML Pipeline
   It has a custom transformer python file. The basic work done here is load data from the database,
   performing train-test split, building a model, training and tuning the model and exporting 
   the model as a pickle file.

How to interact with the Flask Web App
First run the following commands in the project's root directory to set up the database and model
To run ETL pipeline that cleans data and stores in database
`python process_data.py messages.csv categories.csv DisasterResponse.db`
To run ML pipeline that trains classifier and saves
`python train_classifier.py DisasterResponse.db model.pkl`

Secondly run the following command in the app's directory to run your web app.
`python run.py`

Then go to http://0.0.0.0:3001/ to view the Flask Web App.

### Results.
I created an ETL pipeline to read data from two csv files, clean data, process data, transform data 
and save data into a SQLite database.
I created a machine learning pipeline to train a multi-output classifier on the various categories in the dataset. 
I also improved the model by adding the starting verb extractor to the TF-IDF transformer
I created a Flask app to show data visualization and classify any message that users would enter on the web page

### Licensing, Authors, Acknowledgements, etc.
Thanks to Figure Eight for the datasets provoided and Udacity for the Starter code and 
workspace provided to build the web app.