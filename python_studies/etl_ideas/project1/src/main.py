

import os

from datetime import datetime

from extract import extract
from transform import transform
from load import load_bucket
def main():
    date_format = "%Y-%m-%d"
    source_bucket = 'xetra-1234'
    resource_name = 's3'

    df_all = extract(start_date=datetime.today().strftime(date_format), 
                    resource=resource_name, bucket_name=source_bucket)

    df_all = transform(df_all)
    name_of_file = 'xetra_daily_report' + datetime.today().strftime("%Y%m%d_%H%M%S") +\
                    '.parquet'
    load_bucket(name_of_file=name_of_file, df=df_all, resource=resource_name, 
                    bucktet_name=os.getenv("AWS_BUCKET_NAME"))
    print("File loaded.")

if(__name__=="__main__"):
    main()
