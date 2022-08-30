from datetime import datetime, timedelta
import pandas as pd

def transform(df_all:pd.DataFrame)->pd.DataFrame:
    '''
    This function is a quick and dirty solution to trasform the data returned
    from the function 'extract.py'.
    '''
    # Getting the opening price by day
    df_all['opening_price'] = df_all.sort_values(by=['Time']).\
        groupby(['ISIN', 'Date'])['StartPrice'].transform('first')

    # Getting the opening price by day
    df_all['closing_price'] = df_all.sort_values(by=['Time']).\
        groupby(['ISIN', 'Date'])['StartPrice'].transform('last')
    # Aggregate data some values
    df_all = df_all.groupby(['ISIN', 'Date'],as_index=False).agg(
        opening_price_eur=('opening_price','min'), 
        closing_price_eur=('closing_price','min'),
        minimum_price_eur=('MinPrice','min'),
        maximum_price_eur=('MaxPrice','max'),
        daily_traded_volume = ('TradedVolume','sum'))
    # Groupy by type of asset (or 'ISIN') and get the value from the day before.
    df_all['prev_closing_price'] = df_all.sort_values(by=['Date'])\
        .groupby(['ISIN'])['closing_price_eur'].shift(1)
    # Calculate the percentage variation of price from one day to another
    df_all['change_prev_closing'] = (df_all['closing_price_eur']- df_all['prev_closing_price'])\
                                    /df_all['prev_closing_price']
    df_all.drop(columns=['prev_closing_price'], inplace=True)
    return df_all