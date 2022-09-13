'''
Module for simple development. The goal here is to download csv files from an 
AWS S3 bucket. It's a quick and dirty solution for extracting, transform and
load the data. 

'''
import boto3
import pandas as pd
from collections import namedtuple
from boto3.resources.factory import ServiceResource
from boto3.resources import factory
from datetime import date, datetime, timedelta
from io import BytesIO, StringIO
from typing import List

import warnings
warnings.filterwarnings("ignore")

def read_csv_obj(bucket,obj,decoding:str='utf-8')->pd.DataFrame:
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
    Function that downloads all 'csv' files in a specific AWS S3 bucket and transform
    it to a Pandas DataFrame. All 'csv' files that were created after the 'day before' 
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
    Quick and dirty solution to extract data from an AWS S3 bucket.
    '''
    date_format = '%Y-%m-%d'
    day_before =  datetime.strptime(start_date,date_format).date()\
         - timedelta(days=1)
    
    
    s3:ServiceResource = boto3.resource(f'{resource}') # create an instance of service resource

    bucket = s3.Bucket(f'{bucket_name}') # Specifying the chosen bucket
    df_all = csv_to_df(bucket,date_format,day_before)
    return df_all

def return_date_list(arg_date:str, today_date:str, bucket_name:str, resource:str,
              meta_key:str,date_format:str= "%Y-%m-%d")->List[date]:
    '''
    Function that takes 'arg_date' as the first day of the range of dates to be 
    considered and 'today_date' as the last one.

    Parameters
    ---------------------
        arg_date
            A string with the first day of the range of dates to be considered;
        today_date
            A string with the last day of the range of dates to be considered;
        date_format
            The format used for the dates.
    
    Output
    ---------------------
        return_list
            A list of dates.
    '''
    min_date = datetime.strptime(arg_date,date_format).date() - timedelta(days=1)
    today = datetime.strptime(today_date,date_format).date()
    try:
        return_list =  [
            (min_date + timedelta(days=x)) 
            for x in range(0,(today-min_date).days + 1)
        ]
        df_meta, bucket = read_meta_data(bucket_name, resource,meta_key)
        src_dates = set(pd.to_datetime(df_meta['source_date']).dt.date)
        dates_missing = set(return_list[1:] ) - src_dates
        if(dates_missing):
            min_date = min(set(return_list[1:]) - src_dates) - timedelta(days=1)
            return_dates = [date.strftime(date_format) for date in return_list if date>=min_date]
            return_min_date = (min_date + timedelta(days=1)).strftime(date_format)
        else:
            return_dates = []
            return_min_date = datetime(2200,1,1).date()
    except bucket.session.client('s3').exceptions.NoSuchKey:
        return_dates = [(min_date + timedelta(days=x)).strftime(date_format) 
                    for x in range(0, (today-min_date).days) + 1]
        return_min_date = arg_date
    

    return return_min_date, return_dates

def read_meta_data(bucket_name:str, resource:str,meta_key:str)->pd.DataFrame:
    '''
    Function that read the metadata table and return a Pandas DataFrame from it.

    Parameters
    --------------------- 
        bucket_name
            A string with the name of the S3 Bucket where the 'metadata.csv' file
            can be found.

    '''
    Obj = namedtuple('Obj',['key'])
    obj = Obj(meta_key)
    s3:ServiceResource = boto3.resource(f'{resource}') # create an instance of service resource
    bucket = s3.Bucket(f'{bucket_name}') # Specifying the chosen bucket
    df_meta = read_csv_obj(bucket,obj)
    return df_meta, bucket

def write_df_to_s3_csv(bucket_name:str,resource:str,df:pd.DataFrame, key)->bool:
    s3:ServiceResource = boto3.resource(f'{resource}')
    bucket = s3.Bucket(f'{bucket_name}')
    out_buffer = StringIO()
    df.to_csv(out_buffer,index=False)
    bucket.put_object(Body=out_buffer.getvalue(),Key=key)
    return True

def update_meta_file(bucket_name:str, meta_key:str, resource:str, extract_date_list:List):
    df_new = pd.DataFrame(columns=['source_date',' datetime_of_processing'])
    df_new['source_date'] = extract_date_list
    df_new[' datetime_of_processing'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    df_old, _ = read_meta_data(bucket_name,resource,meta_key)
    df_all = pd.concat([df_old,df_new])
    write_df_to_s3_csv(bucket_name,resource,df_all,meta_key)


if(__name__=='__main__'):
    extract(start_date='2022-08-30', resource='s3', bucket_name='xetra-1234')
