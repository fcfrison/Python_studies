

import os

from datetime import datetime

from extract import extract, return_date_list, update_meta_file
from transform import transform
from load import load_bucket
def main(min_day:str):
    # basic configuration
    source_bucket = 'xetra-1234'
    target_bucket = os.getenv("AWS_BUCKET_NAME")
    resource_name = 's3'
    target_file = 'xetra_daily_report' + datetime.today().strftime("%Y%m%d_%H%M%S")
    file_format = '.parquet'
    today = '2022-09-13'
    meta_key ='meta_file.csv' 

    # extract data
    extract_date, date_list = return_date_list(min_day,today,target_bucket,resource_name,meta_key)
    df_all = extract(start_date=extract_date, resource=resource_name, 
                     bucket_name=source_bucket)
    # transform data
    df_all = transform(df_all)
    
    # load data
    load_bucket(target_file,file_format, df=df_all, resource=resource_name,
                target_bucket=target_bucket)
    update_meta_file(target_bucket,meta_key,resource_name,date_list)
    
    print("File loaded.")

if(__name__=="__main__"):
    date_format = "%Y-%m-%d"
    min_day = datetime.today().strftime(date_format)
    main(min_day = '2022-09-11')
