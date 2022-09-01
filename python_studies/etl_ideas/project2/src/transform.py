from datetime import datetime, timedelta
from select import select
from typing import List
import pandas as pd

def select_and_clean(df:pd.DataFrame,selected_columns:List[str])->pd.DataFrame:
    '''
    Function that gets a Pandas DataFrame as input and select some columns.
    '''
    # Selecting some columns
    df = df[selected_columns]
    df.reset_index(drop=True,inplace=True)
    df.dropna(inplace=True)
    return df

def transform_report_1(df:pd.DataFrame):
    '''
    Function that takes a Pandas DataFrame as input and transform it
    considering some rules.
    '''
    # Getting the opening price by day
    df['opening_price'] = df.sort_values(by=['Time']).\
        groupby(['ISIN', 'Date'])['StartPrice'].transform('first')

    # Getting the opening price by day
    df['closing_price'] = df.sort_values(by=['Time']).\
        groupby(['ISIN', 'Date'])['StartPrice'].transform('last')
    # Aggregate data some values
    df = df.groupby(['ISIN', 'Date'],as_index=False).agg(
        opening_price_eur=('opening_price','min'), 
        closing_price_eur=('closing_price','min'),
        minimum_price_eur=('MinPrice','min'),
        maximum_price_eur=('MaxPrice','max'),
        daily_traded_volume = ('TradedVolume','sum'))
    # Groupy by type of asset (or 'ISIN') and get the value from the day before.
    df['prev_closing_price'] = df.sort_values(by=['Date'])\
        .groupby(['ISIN'])['closing_price_eur'].shift(1)
    # Calculate the percentage variation of price from one day to another
    df['change_prev_closing'] = (df['closing_price_eur']- df['prev_closing_price'])\
                                    /df['prev_closing_price']
    df.drop(columns=['prev_closing_price'], inplace=True)
    return df
    
def transform(df_all:pd.DataFrame)->pd.DataFrame:
    '''
    This function is a quick and dirty solution to trasform the data returned
    from the function 'extract.py'.
    '''
    selected_columns = ['ISIN','Date', 'Time', 'StartPrice', 'MaxPrice', 'MinPrice',
            'EndPrice', 'TradedVolume', 'NumberOfTrades']
    df_all = select_and_clean(df_all,selected_columns)
    df_all = transform_report_1(df_all)
    return df_all