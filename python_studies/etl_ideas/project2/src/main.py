

import os

from datetime import datetime

from extract import extract
from transform import transform
from load import load_bucket
def main():
    # basic configuration
    date_format = "%Y-%m-%d"
    source_bucket = 'xetra-1234'
    target_bucket = os.getenv("AWS_BUCKET_NAME")
    resource_name = 's3'
    target_file = 'xetra_daily_report' + datetime.today().strftime("%Y%m%d_%H%M%S")
    file_format = '.parquet'
    # extract data
    df_all = extract(start_date=datetime.today().strftime(date_format), 
                    resource=resource_name, bucket_name=source_bucket)
    # transform data
    df_all = transform(df_all)
    
    # load data
    load_bucket(target_file,file_format, df=df_all, resource=resource_name,
                target_bucket=target_bucket)
    print("File loaded.")

if(__name__=="__main__"):
    main()
