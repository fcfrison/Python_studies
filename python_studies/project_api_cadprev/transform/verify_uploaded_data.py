import itertools
from typing import List
import pandas as pd

def generate_control_data(cnpj:str, year:int, month:int)->List[dict]:
    """
    This function purpose is to generate a list of dictionary. 
    Each dictionary is composed by the keys 'nr_cnpj_entidade', 
    'dt_ano' and 'dt_mes'.

    Parameters
    -----------------------
        cnpj:str 
        year:int
        month:int
    
    Output
    -----------------------
        List[dict]
    """
    return [dict(nr_cnpj_entidade=cnpj, dt_ano=year, dt_mes=month_) 
                for month_ in range(1,month + 1)]

def verify_uploaded_data(df_dipr: pd.DataFrame,
                      df_aliquota:pd.DataFrame)->None:
    '''
    This function purpose is to verify whether a munipacility
    that has a RPPS related to it has uploaded or not the RPPS 
    information given an specific month and year.
    A '.xlsx' file is generated.

    Parameters
    -----------------------
        df_dipr: pd.DataFrame
        df_aliquota:pd.DataFrame
    '''
    
    df_DIPR = df_dipr.copy()
    df_aliquotas = df_aliquota.copy()
    df_DIPR.reset_index(inplace=True, drop=True)
    df_aliquotas.reset_index(inplace=True, drop=True)

    # creating an iterator with cnpjs
    cnpj_iter = df_aliquotas.nr_cnpj_entidade.unique()
    month = df_DIPR.dt_mes.max()
    year = df_DIPR.dt_ano.max()

    # creating the table to control cnpj, month and year   
    fn = lambda arg: generate_control_data(arg,year,month)
    list_df_control = list(map(fn,cnpj_iter))
    df_data_control = pd.DataFrame(list(itertools.chain(*list_df_control)))

    # grouping by data considering 'df_DIPR', given 'nr_cnpj_entidade','dt_mes', 'dt_ano'
    df_DIPR_grouped = df_DIPR.groupby(['nr_cnpj_entidade','dt_mes', 'dt_ano'],
                        as_index=False).count()[['nr_cnpj_entidade','dt_mes',
                        'dt_ano']]

    # joining the tables
    df_data_control=df_data_control.merge(df_DIPR_grouped,how='left',indicator=True)

    fn = lambda arg: False if(arg=='both') else True
    df_data_control._merge = df_data_control._merge.apply(fn)
    df_data_control.rename(columns={'_merge':'nao_enviou'},inplace=True)
    df_data_control.to_excel('./downloaded_data/controle_envios.xlsx')

if(__name__=='__main__'):
    df_DIPR:pd.DataFrame = pd.read_pickle('./downloaded_data/DIPR_2021.pkl')
    df_aliquotas:pd.DataFrame =pd.read_pickle('./downloaded_data/df_aliquotas.pkl')
    verify_uploaded_data(df_DIPR,df_aliquotas)