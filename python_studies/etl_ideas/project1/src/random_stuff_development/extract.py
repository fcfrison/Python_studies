'''
Module for simple development. The goal here is to download csv files from an 
AWS S3 bucket. It's a quick and dirty solution for extracting, transform and
load the data. 

'''
import boto3
import pandas as pd


from boto3.resources.factory import ServiceResource
from datetime import datetime, timedelta
from io import StringIO
import warnings
warnings.filterwarnings("ignore")

def extract(start_date:str, bucket_name:str, resource:str)->pd.DataFrame:
    '''
    Quick and dirty solution to extract data from a AWS S3 bucket.
    '''
    date_format = '%Y-%m-%d'
    day_before =  datetime.strptime(start_date,date_format).date() - timedelta(days=1)
    selected_columns = ['ISIN','Date', 'Time', 'StartPrice', 'MaxPrice', 'MinPrice',
            'EndPrice', 'TradedVolume', 'NumberOfTrades']
    s3:ServiceResource = boto3.resource(f'{resource}') # create an instance of service resource


    bucket = s3.Bucket(f'{bucket_name}') # Specifying the chosen bucket
    objects = [obj for obj in bucket.objects.all() if datetime.strptime(obj.key.\
                split('/')[0],date_format).date()>=day_before]

    csv_obj = bucket.Object(key=objects[0].key).get()\
        .get('Body').read().decode('utf-8')


    data = StringIO(csv_obj) # buffering the downloaded data
    df_all = pd.read_csv(data, delimiter=',') # creating an instance of a DataFrame class
    for obj in objects:
        csv_obj = bucket.Object(key=obj.key).get()\
            .get('Body').read().decode('utf-8')
        data = StringIO(csv_obj)
        df_all = df_all.append(
            pd.read_csv(data, delimiter=','),
            ignore_index=True
        )
    # Selecting some columns
    df_all = df_all[selected_columns]
    df_all.reset_index(drop=True,inplace=True)
    df_all.dropna(inplace=True)
    return df_all

if(__name__=='__main__'):
    extract(start_date='2022-08-30', resource='s3', bucket_name='xetra-1234')
