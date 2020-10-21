import pandas as pd
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt
import seaborn as sns
import os

from env import host, username, password
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler

def clean_zillow_data():
    # Drop any duplicates in data
    df.drop_duplicates(inplace=True)
    # Drop unnecessary columns
    df = df.drop(columns=cols_to_drop)
    df = prepare.data_prep(df,cols_to_remove=['id', 'parcelid','buildingqualitytypeid','calculatedbathnbr','finishedsquarefeet12','fullbathcnt', 'heatingorsystemtypeid','propertycountylandusecode',
    'propertylandusetypeid', 'propertyzoningdesc', 'rawcensustractandblock', 'regionidcity', 'regionidcounty', 'regionidzip', 'roomcnt', 'unitcnt', 'censustractandblock'],
    prop_required_column=.6,
    prop_required_row=.75)

    # Specific removal of outliers
    df = df[((df.bathroomcnt <= 7) & (df.bedroomcnt <= 7) & 
         (df.bathroomcnt > 0) & 
         (df.bedroomcnt > 0) & 
         (df.calculatedfinishedsquarefeet < 7000))]
    return df

def prep_zillow_data():
    df = clean_data()
    train_validate, test = train_test_split(df, test_size=.3, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.2, random_state=123)

    # Split into X variables and y target
    # X is every column except logerror
    X_train = train.drop('logerror',axis=1)
    # y is only log error, [[]] to keep as df and not series
    y_train = train[['logerror']]

    # Repeat for validate and test
    X_validate = validate.drop('logerror',axis=1)
    y_validate = validate[['logerror']]

    X_test = test.drop('logerror',axis=1)
    y_test = test[['logerror']]

    return train, validate, test

def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75): 
    df = remove_columns(df, cols_to_remove)  # Removes Specified Columns
    df = handle_missing_values(df, prop_required_column, prop_required_row) # Removes Specified Rows
    df.dropna(inplace=True) # Drops all Null Values From Dataframe
    return df

def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df