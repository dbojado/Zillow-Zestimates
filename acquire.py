import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from env import host, username, password

###################### Acquire Zillow Home Data ########################

def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'


def zillow_data():
# 260: residential general
# 261: single family residential
# 263: mobile home
# 264: townhouse
# 266: condominium 
# 279: inferred single family residential
    '''
    This function reads the mall customer data from the Codeup db into a df, 
    write it to a csv file, and returns the df.
    '''
    sql_query = '''
    SELECT *
    FROM properties_2017 as prop
    JOIN predictions_2017 as pred ON pred.id = prop.id
    WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);
    '''
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_home.csv')
    return df


def get_zillow_data(cached=False):
    '''
    This function reads in mall customer data from Codeup database if cached == False
    or if cached == True reads in mall customer df from a csv file, returns df
    '''
    if cached or os.path.isfile('zillow_home.csv') == False:
        df = zillow_data()
    else:
        df = pd.read_csv('zillow_home.csv', index_col=0)
    return df


def zillow_data_with_joins():
    '''
    This function reads the mall customer data from the Codeup db into a df, 
    write it to a csv file, and returns the df.
    '''
    sql_query = '''
    SELECT *
    FROM properties_2017 as prop
    JOIN predictions_2017 as pred ON pred.id = prop.id
    LEFT JOIN zillow.airconditioningtype ac USING(airconditioningtypeid)
    LEFT JOIN zillow.architecturalstyletype arch USING(architecturalstyletypeid)
    LEFT JOIN zillow.buildingclasstype bldg USING(buildingclasstypeid)
    LEFT JOIN zillow.heatingorsystemtype heat USING(heatingorsystemtypeid)
    LEFT JOIN zillow.propertylandusetype land USING(propertylandusetypeid)
    LEFT JOIN zillow.storytype stories USING(storytypeid)
    LEFT JOIN zillow.typeconstructiontype const USING(typeconstructiontypeid)
    WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);
    '''
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_home.csv')
    return df
