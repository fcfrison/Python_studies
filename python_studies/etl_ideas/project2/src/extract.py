'''
Module for simple development. The goal here is to download csv files from an 
AWS S3 bucket. It's a quick and dirty solution for extracting, transform and
load the data. 

'''
import boto3
import pandas as pd

from boto3.resources.factory import ServiceResource
from boto3.resources import factory
from datetime import datetime, timedelta
from io import StringIO
import warnings
warnings.filterwarnings("ignore")

def read_csv_obj(bucket,obj,decoding)->pd.DataFrame:
    '''
    Function that gets an specific S3 Bucket object and returns a 
    Pandas DataFrame. 
    '''
    csv_obj = bucket.Object(key=obj.key).get()\
            .get('Body').read().decode(decoding)
    data = StringIO(csv_obj)
    return pd.read_csv(data, delimiter=',')

def csv_to_df(bucket:ServiceResource,date_format:str, 
              day_before:datetime, decoding:str='utf-8', 
              delimiter:str=',')->pd.DataFrame:
    '''
    Function that downloads all csv files in a specific AWS S3 bucket and transform
    it to a Pandas DataFrame. All csv files that were created after the 'day before' 
    will be downloaded.

    Parameters
    ---------------------
        bucket
            An instance of a S3 bucket;
        date_format
            The reference day;
        day_before
            The day before the reference day;
    
    Output
    ---------------------
        df_all
            A Pandas DataFrame with the selected data.

    '''
    objects = [obj for obj in bucket.objects.all() if datetime.strptime(obj.key.\
                split('/')[0],date_format).date()>=day_before]

    csv_obj = bucket.Object(key=objects[0].key).get()\
        .get('Body').read().decode(decoding)


    data = StringIO(csv_obj) # buffering the downloaded data
    df_all = pd.read_csv(data, delimiter=delimiter) # creating an instance of a DataFrame class
    for obj in objects:
        df_all = df_all.append(read_csv_obj(bucket,obj,decoding),ignore_index=True)
    return df_all

def extract(start_date:str, bucket_name:str, resource:str)->pd.DataFrame:
    '''
    Quick and dirty solution to extract data from a AWS S3 bucket.
    '''
    date_format = '%Y-%m-%d'
    day_before =  datetime.strptime(start_date,date_format).date()\
         - timedelta(days=1)
    
    
    s3:ServiceResource = boto3.resource(f'{resource}') # create an instance of service resource

    bucket = s3.Bucket(f'{bucket_name}') # Specifying the chosen bucket
    df_all = csv_to_df(bucket,date_format,day_before)
    return df_all

if(__name__=='__main__'):
    extract(start_date='2022-08-30', resource='s3', bucket_name='xetra-1234')
