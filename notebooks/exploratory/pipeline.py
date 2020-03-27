import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.impute import MissingIndicator, SimpleImputer

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import SelectFromModel

# plot_confusion_matrix is a handy visual tool, added in the latest version of scikit-learn
# if you are running an older version, comment out this line and just use confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from imblearn.pipeline import Pipeline


def encode_artist_name(x):
    '''
    This is a helper function for load_and_format_x_y()
    This function takes in a dataframe of x predictors. 
    Initiates a OneHotEncoder with handle_unknown="ignore" to 
    compensate for unseen artists in new data, 
    And returns the dataframe with the artist column encoded.
    '''
    # initiate OHE
    ohe = OneHotEncoder(categories="auto", handle_unknown="ignore")
    # dataframe of just encoded columns, using x_train index as it's index to ensure rows line up
    ohe.fit(x[['artist_name']])
    artist_dummies = pd.DataFrame(ohe.transform(x[['artist_name']]).todense(), columns=ohe.get_feature_names(), index=x.index)
    # concat encoded columns to x
    concatted_x = pd.concat([x, artist_dummies], axis=1)
    #add column names
    concatted_x.columns = list(x.columns) + list(artist_dummies)
    concatted_x = concatted_x.drop('artist_name', axis=1)
    return concatted_x

def load_and_format_x_y():
    '''
    This is a helper function for format_data_for_model()
    This function takes in a raw data frame, 
    Formats data, 
    And returns X and y pandas dataframes
    '''
    # load data into dataframe
    df = pd.read_csv('../../Data/music_subset.csv')
    # drop extra axis column from csv file
    df = df.drop('Unnamed: 0', axis=1).set_index('track_id')
    # remove songs in 'classic pop and rock' genre
    df = df[df['genre'] != 'classic pop and rock']
    # split data into X and y dataframes
    X = df.drop('genre', axis=1)
    y = df['genre']
    # encode artist column in X
    X = encode_artist_name(X)
    
    return X, y

def format_data_for_model():
    '''
    This function takes in a dataframe, 
    Removes unwanted columns and the 'classic pop and rock', 
    Genre because of it's size and ambiguity, 
    Performs a train test split, 
    Initates a SMOTE object and uses it to generate data points in the 
    test data in order to balance class sizes, 
    And returns resampled train X and y sets and test X and y sets 
    formatted to train model
    '''
    #format raw dataframe
    X, y = load_and_format_x_y()
    
    # train test split data with stratify to create class 
    # equality between train and test data
    x_train, x_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=2020, test_size=0.01006711409) # test_size=0.01006711409 
    # drop title column (string, useless category)
    x_test = x_test.drop('title', axis=1)
    x_train = x_train.drop('title', axis=1)
    
    
    return x_train, y_train, x_test, y_test

def pass_pipeline(X, y):
    '''
    This function runs the pipeline including
    SMOTE and RFC with specified parameters on the 
    input data, and instantiates a pipeline that can 
    can then be used to fit new training data or predict on
    test data.
    '''
    
    pipe = Pipeline(steps=[
    ('smote', SMOTE()),
    ('model', RandomForestClassifier(n_jobs=-1, max_features=8, random_state=2020))
    ])
    
    return pipe.fit(X, y)