import boto3

import pandas as pd

from datetime import datetime
from io import BytesIO

def load_bucket(name_of_file:str, df:pd.DataFrame, resource:str, bucktet_name)->bool:
    
    name_of_file = 'xetra_daily_report' + datetime.today().strftime("%Y%m%d_%H%M%S") + \
            '.parquet'
    out_buffer = BytesIO() # Creating the output buffer.
    df.to_parquet(out_buffer,index=False)
    s3 = boto3.resource(f'{resource}')
    bucket_target = s3.Bucket(f'{bucktet_name}') # Creating an instance 
                                                            # of a Bucket object. 
    bucket_target.put_object(Body=out_buffer.getvalue(),Key=name_of_file)
