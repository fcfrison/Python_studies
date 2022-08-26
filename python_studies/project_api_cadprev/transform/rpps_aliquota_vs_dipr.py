from collections import namedtuple
from decimal import Decimal
import numpy as np
import pandas as pd

# suppress FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def create_table_percent(df:pd.DataFrame)->pd.DataFrame:
    '''
    Description
    ---------------------------
    This function creates a table that contains a column with the 
    field 'perc_56_19', that represents the resulting 'vl_rubrica' 
    considering the division between 'id_rubrica'=56 and 'id_rubrica'=19.

    Parameters
    ---------------------------
        df: pd.DataFrame

    Output
    ---------------------------
        df_DIPR_grouped_final pd.DataFrame
    '''
    df_DIPR_copy = df.copy()
    cnpj_iterator = df_DIPR_copy.nr_cnpj_entidade.unique()
    # grouping by considering 'nr_cnpj_entidade','dt_mes', 'dt_ano','id_rubrica'
    df_DIPR_grouped = df_DIPR_copy.groupby(['nr_cnpj_entidade','dt_mes', 
                        'dt_ano','id_rubrica'], as_index=False).sum()[
                            ['nr_cnpj_entidade','dt_mes','dt_ano',
                            'id_rubrica','vl_rubrica']]
    df_DIPR_grouped_final = pd.DataFrame()
    for cnpj in cnpj_iterator:
        # selecting id_rubrica=='56' | id_rubrica=='19' given a cnpj
        df_DIPR_grouped_query = df_DIPR_grouped.query(
                            f"nr_cnpj_entidade == '{cnpj}' & " +
                            "(id_rubrica=='56' | id_rubrica=='19')")
        
        # making two new columns considering the values of 'id_rubrica'
        df_DIPR_grouped_query = pd.pivot_table(df_DIPR_grouped_query, 
                            index=['nr_cnpj_entidade','dt_mes', 'dt_ano'],
                            columns=['id_rubrica'], values='vl_rubrica')\
                                .reset_index()
        df_DIPR_grouped_query.rename(columns={'19':"rubrica_19", 
                        '56':"rubrica_56"},inplace=True)
        
        # dividing one column by another
        df_DIPR_grouped_query['perc_56_19'] = df_DIPR_grouped_query['rubrica_56']\
            .div(df_DIPR_grouped_query['rubrica_19'].values)

        if(df_DIPR_grouped_final.empty):
            df_DIPR_grouped_final = df_DIPR_grouped_query
        else:
            df_DIPR_grouped_final= pd.concat([df_DIPR_grouped_final,df_DIPR_grouped_query],
                       ignore_index=True)
    return df_DIPR_grouped_final



def find_time_interval(df_aliquotas:pd.DataFrame,nm_tuple:namedtuple)->pd.Series:
    '''
    Description
    ---------------------------
    This function finds the interval by which a specific 'date' belongs to. 
    The 'dates' field comes from the table 'df_DIPR_grouped' and is related
    to a transaction date.
    
    Parameters
    ---------------------------
        df_aliquotas: a DataFrame with data from the endpoint RPPS_ALIQUOTAS;
        nm_tuple: an object with the attribute 'dates'. This information comes 
                from the endpoint DIPR

    Output
    ---------------------------
        An object from the type pd.Series with boolean values.
    '''
    return df_aliquotas.apply(lambda arg: True \
        if (arg.dt_inicio_vigencia<=nm_tuple.dates and \
            nm_tuple.dates<arg.dt_final_esperada) \
                else False, axis=1)


def get_aliquotas(df_aliquotas:pd.DataFrame,
                  df_DIPR_grouped:pd.DataFrame,
                  cnpj:str)->None:
    '''
    Description
    ---------------------------
    This function finds the correct "aliquota" given a specific 'cnpj', a month
    and a year. It inserts some columns in the 'df_DIPR_grouped' Dataframe.

    Parameters 
    ---------------------------
    df_aliquotas:pd.DataFrame,
    df_DIPR_grouped:pd.DataFrame,
    cnpj:str
    '''
    
    aliquotas_columns = ['vl_aliquota','datas_invertidas','dt_inicio_vigencia_duplicada',
                         'dts_finais_diferentes'] # list of columns of interest   
    new_columns_ente =  ['aliquota_ente','datas_invertidas_ente','dt_duplicada_ente',
                        'problema_dt_final_ente'] # list of new columns
    new_columns_ente_suplem =  ['aliquota_suplem','datas_invertidas_suplem',
                                'dt_duplicada_suplem','problema_dt_final_suplem'] # list of new columns

    dipr_iter = list(df_DIPR_grouped.query( # list of items in DIPR, given a cnpj
                    f"nr_cnpj_entidade == '{cnpj}'").itertuples())

    # df_aliquotas_ente is a table with data related to the category 'Ente'. 
    df_aliquotas_ente = df_aliquotas.query(f"nr_cnpj_entidade == '{cnpj}' & "+
                                            "no_sujeito_passivo == 'Ente'")
    df_aliquotas_ente_supl = df_aliquotas.query(f"nr_cnpj_entidade == '{cnpj}' & "+
                                            "no_sujeito_passivo == 'Ente-suplementar'")
    for nm_tuple in dipr_iter:
        # updating the DIPR table with new data. 
        if(not df_aliquotas_ente.empty):
            intervals_ente = find_time_interval(df_aliquotas_ente,nm_tuple)
            
            df_DIPR_grouped.loc[nm_tuple.Index,new_columns_ente] = \
                tuple(df_aliquotas_ente[intervals_ente][aliquotas_columns]\
                    .iloc[0])
        if(not df_aliquotas_ente_supl.empty): # no rows for a cnpj
            intervals_suplementar = find_time_interval(df_aliquotas_ente_supl,nm_tuple)
            if(intervals_suplementar.any()): # at least one true value
                df_DIPR_grouped.loc[nm_tuple.Index,new_columns_ente_suplem] = \
                    tuple(df_aliquotas_ente_supl[intervals_suplementar][aliquotas_columns]\
                        .iloc[0])
            else: # for now, do nothing...
                pass


def rpps_aliquota_vs_dipr(df_DIPR:pd.DataFrame,
                          df_aliquotas:pd.DataFrame)->pd.DataFrame:
    '''
    Concept
    ----------------------
    This function works with the Pandas Dataframe generated from the endpoint 
    'DIPR' and groups it by the fields 'nr_cnpj_entidade','dt_mes', 'dt_ano' 
    and 'id_rubrica'. For each row in the dataframe grouped by the above mentioned
    fields, it finds the correct 'aliquota' (given the month and year related 
    to each row). 
    The function output is a Pandas Dataframe with a comparation between the 
    expected 'aliquota' and the calculated 'aliquota'.

    Parameters  
    ----------------------
        df_DIPR:pd.DataFrame
        df_aliquotas:pd.DataFrame
    
    Output
    ----------------------
        df_DIPR_grouped: pd.DataFrame
    '''
    # despite the fact that'vl_rubrica' is a monetary value, it'll be treated as float.
    df_DIPR = df_DIPR.astype(dict(vl_rubrica='float',
                                id_rubrica='str'))
    # creating a table with a new field
    df_DIPR_grouped = create_table_percent(df=df_DIPR)

    # insert the column 'dates'
    fn = lambda arg: pd.to_datetime(pd.Period(f'{arg.dt_mes}-1-{arg.dt_ano}',freq='M')\
        .end_time.date()) # get the last day of the month
    list_dates = list(map(fn,df_DIPR_grouped.itertuples()))
    
    # create column 'dates'
    df_DIPR_grouped = df_DIPR_grouped.assign(dates=list_dates)

    list(map(lambda cnpj: get_aliquotas(df_aliquotas,df_DIPR_grouped,cnpj),
        df_DIPR_grouped.nr_cnpj_entidade.unique()))

    df_DIPR_grouped.aliquota_suplem.fillna(value=Decimal(0.0),inplace=True)

    df_DIPR_grouped['montante_aliquotas'] = \
        df_DIPR_grouped[['aliquota_ente','aliquota_suplem']]\
            .sum(axis=1)

    df_DIPR_grouped.perc_56_19 = (df_DIPR_grouped.perc_56_19 * 100).round(2)

    # comparing two columns
    conditions = [df_DIPR_grouped.perc_56_19 >= df_DIPR_grouped.montante_aliquotas, 
                df_DIPR_grouped.perc_56_19 < df_DIPR_grouped.montante_aliquotas] 
    choices = [False,True]
    
    # creating new column with compared values
    df_DIPR_grouped['irregularidade'] = np.select(conditions,choices)
    return df_DIPR_grouped

if(__name__=='__main__'):
    df_DIPR:pd.DataFrame = pd.read_pickle('./downloaded_data/DIPR_2021.pkl')
    df_aliquotas:pd.DataFrame = pd.read_pickle('./downloaded_data/df_aliquota_transformed.pkl')
    rpps_aliquota_vs_dipr(df_DIPR,df_aliquotas)
