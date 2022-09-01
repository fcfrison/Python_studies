import boto3

import pandas as pd

from datetime import datetime
from io import BytesIO

def load_bucket(target_file:str,file_format:str,df:pd.DataFrame, 
                resource:str, target_bucket:str)->None:
    '''
    Function that gets a Pandas DataFrame as input and load it in a AWS S3 Bucket.

    Parameters
    ---------------------
        target_file
            A string with the name of the AWS S3 target file;
        file_format
            A string with the file format to be saved on the AWS resource;
        df 
            A Pandas DataFrame with the data to be uploaded;
        resource
            The name of the resource. For instance, 's3';
        target_bucket
            The name of the bucket on AWS S3 where the file will be saved;

    '''
    target_file_complete = target_file + file_format
    out_buffer = BytesIO() # Creating the output buffer.
    df.to_parquet(out_buffer,index=False)
    s3 = boto3.resource(f'{resource}')
    bucket_target = s3.Bucket(f'{target_bucket}') # Creating an instance 
                                                            # of a Bucket object. 
    bucket_target.put_object(Body=out_buffer.getvalue(),Key=target_file_complete)
