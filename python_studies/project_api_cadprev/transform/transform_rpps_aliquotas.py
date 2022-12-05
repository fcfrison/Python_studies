from typing import List
import pandas as pd
import numpy as np

from decimal import Decimal
from datetime import datetime
from collections import namedtuple
import itertools

import datetime
import pandas as pd
import numpy as np
# suppress FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def normalize_date(date:str)->datetime.datetime:
    '''
    normalize_date
    ---------------
    normalize_date(date:str)

    Function that casts a string to timestamp and normalizes it, 
    meaning the time component of the date-time is converted to 
    midnight.

    parameters
    ---------------
        date: the string to be casted
    '''
    if(date is not np.nan):
        date = pd.to_datetime(date, errors = 'coerce') # if date is too big, 
        try:                                           # then 'coerce' it to datetime.
            date = date.normalize()
        except AttributeError:
            return date
    else:
        return date    
    return date



def insert_expected_final_ente(df:pd.DataFrame, 
                               now:datetime.datetime,
                               nr_cnpj_entidade:str,
                               no_sujeito_passivo:str):
    '''
    Description
    ----------------

    This function inserts the fields 'dt_final_esperada' and 
    'datas_invertidas'. The former contains data related to 
    the expected date given the field 'dt_inicio_vigencia' and
    the latter refers to the situation in which 
    'dt_inicio_vigencia'>'dt_fim_vigencia'".

    Parameters
    ----------------
        df
            DataFrame with data from the endpoint RPPS_ALIQUOTAS;
        now
            The date of data processing;
        nr_cnpj_entidade
            nr_cnpj_entidade is a string that identifies one municipality;
        no_sujeito_passivo
            no_sujeito_passivo is a category related to the kind of investiment;

    '''
    # Insert new columns.
    try:
        df.insert(loc=len(df.columns), column="dt_final_esperada",
                          value=pd.NaT) # create dt_final_esperada column 
        df.insert(loc=len(df.columns),column="datas_invertidas",value=np.nan)
    except ValueError:
        pass
    
    # Query data from 'Ente' or 'Ente-suplementar'.
    query_str = f"nr_cnpj_entidade == '{nr_cnpj_entidade}'" +\
        f" & no_sujeito_passivo =='{no_sujeito_passivo}'"
    selected_columns = ['dt_inicio_vigencia','dt_fim_vigencia','nr_cnpj_entidade']
    iterator = df.query(query_str)[selected_columns]\
        .sort_values(ascending=True, by='dt_inicio_vigencia')

    list_iter = list(iterator.itertuples()) # create iterator with namedtuple
    for index, nm_tuple in enumerate(list_iter):
        if(nm_tuple.dt_inicio_vigencia>nm_tuple.dt_fim_vigencia): # dates are inverted
            df['datas_invertidas'].loc[nm_tuple.Index] = True
            continue
        else: df['datas_invertidas'].loc[nm_tuple.Index] = False

        if(index==len(list_iter)-1 and nm_tuple.dt_inicio_vigencia<=now):# last element in the list
            df['dt_final_esperada'].loc[nm_tuple.Index] = now
        
        elif(index==len(list_iter)-1 and nm_tuple.dt_inicio_vigencia>now):
            df['dt_final_esperada'].loc[nm_tuple.Index] = nm_tuple.dt_inicio_vigencia
        
        else: # not the last element in the list
            if(nm_tuple.dt_inicio_vigencia == # if dates are repeated, search different date.
                list_iter[index+1].dt_inicio_vigencia):
                try:
                    list_iter[index+2]
                    sub_list = list_iter[index+2:]
                    for i,item in enumerate(sub_list):
                        if(item.dt_inicio_vigencia!=
                            nm_tuple.dt_inicio_vigencia):
                                df['dt_final_esperada'].loc[nm_tuple.Index] =  \
                                        item.dt_inicio_vigencia - \
                                        datetime.timedelta(seconds = 1) # the end of the day before
                                break
                        if(len(sub_list)==i+1):
                            raise IndexError
                except IndexError:
                    if(list_iter[len(list_iter)-1].dt_inicio_vigencia>=now):
                        df['dt_final_esperada'].loc[nm_tuple.Index] = \
                            list_iter[len(list_iter)-1].dt_inicio_vigencia
                    else:
                        df['dt_final_esperada'].loc[nm_tuple.Index] = now
            else:
                df['dt_final_esperada'].loc[nm_tuple.Index] = \
                        list_iter[index+1].dt_inicio_vigencia - \
                        datetime.timedelta(seconds = 1) # the end of the day before




def check_dt_differences(df:pd.DataFrame, 
                         nr_cnpj_entidade:str,
                         no_sujeito_passivo:str)->None:
    '''
    Description
    ----------------

    This function inserts the field 'dts_finais_diferentes', whose 
    purpose is to show if the values 'dt_fim_vigencia' and 
    'dt_final_esperada' are equal or not.
    The field previously mentioned is restricted by the condition 
    no_sujeito_passivo == 'Ente'.

    Parameters
    ----------------
        df:pd.DataFrame, 
        nr_cnpj_entidade:str
    '''
    try:
        df.insert(loc=len(df.columns), column="dts_finais_diferentes",value="DFI") # create dt_final_esperada column 
    except ValueError:
        pass
    iterator = df.query(f"nr_cnpj_entidade == '{nr_cnpj_entidade}' & "
                      + f"no_sujeito_passivo == '{no_sujeito_passivo}'").sort_values(
                            ascending=True, by='dt_inicio_vigencia')[:-1]\
                                .itertuples() 
    for nm_tuple in iterator:
        if (nm_tuple.dt_fim_vigencia.date() != 
            nm_tuple.dt_final_esperada.date()):
                
                df['dts_finais_diferentes'].loc[nm_tuple.Index]="DFD"

def normalizing_dates(df:pd.DataFrame,column_name:str)->pd.DataFrame:
    '''
    Description
    ----------------
    This function normalizes dates from a given column.

    Parameters
    ----------------
        df: a Pandas DataFrame;
        column_name: the name of the column to be normalized;
    
    Returns
    ----------------
        df: the transformed Pandas DataFrame;
    '''
    df[column_name] = df[column_name].map(normalize_date)
    return df

def create_cnpj_list(df:pd.DataFrame)->List[object]:
    unique_cnpj:np.ndarray = df_aliquota.nr_cnpj_entidade\
                                .unique() 
    # creating a class with 'nr_cnpj_entidade' and 'no_sujeito_passivo' attributes.
    CnpjNomeSujPass = namedtuple('CnpjNomeSujPass', 
                            'nr_cnpj_entidade  no_sujeito_passivo')
        
    # creating lists of objects of the class CnpjNomeSujPass.
    cnpj_nome_suj = [list(map(lambda arg: CnpjNomeSujPass(arg,nome_suj),
                        unique_cnpj)) for nome_suj in ['Ente','Ente-suplementar']]
    cnpj_nome_suj_unpack = list(itertools.chain(*cnpj_nome_suj))
    return cnpj_nome_suj_unpack

def aliquotas_rpps_transform(df_aliquota:pd.DataFrame,
                            now = datetime.datetime.now()):
    '''
    This function applies various transformations to the data downloaded
    from the endpoint ''
    '''
    selected_columns = ['nr_cnpj_entidade', 'no_ente','vl_aliquota',
                    'no_sujeito_passivo','dt_inicio_vigencia', 'dt_fim_vigencia']
    df_aliquota = df_aliquota[selected_columns] # filtering the fields of interest                

    df_aliquota.query("no_sujeito_passivo == 'Ente' | " +
                    "no_sujeito_passivo == 'Ente-suplementar' ",
                    inplace=True)
    df_aliquota.reset_index(inplace=True, drop=True)
    df_aliquota.vl_aliquota = df_aliquota.vl_aliquota\
                            .map(lambda arg: Decimal(arg)) # turning 'vl_aliquota' into Decimal
    # normalizing dates   
    df_aliquota = normalizing_dates(df_aliquota,'dt_inicio_vigencia')
    df_aliquota = normalizing_dates(df_aliquota,'dt_fim_vigencia')
    
    # droping na values from the field  'dt_inicio_vigencia'
    df_aliquota.dropna(axis=0,how='any',
                        subset='dt_inicio_vigencia',
                        inplace=True)
    '''
    unique_cnpj:np.ndarray = df_aliquota.nr_cnpj_entidade\
                                .unique() 

    # creating a class with 'nr_cnpj_entidade' and 'no_sujeito_passivo' attributes.
    CnpjNomeSujPass = namedtuple('CnpjNomeSujPass', 
                        'nr_cnpj_entidade  no_sujeito_passivo')
    
    # creating lists of objects of the class CnpjNomeSujPass.
    cnpj_nome_suj = [list(map(lambda arg: CnpjNomeSujPass(arg,nome_suj),
                    unique_cnpj)) for nome_suj in ['Ente','Ente-suplementar']]
    
    # unpacking two lists into another.
    cnpj_nome_suj_unpack = list(itertools.chain(*cnpj_nome_suj))
    '''

    cnpj_nome_suj_unpack = create_cnpj_list(df_aliquota)
    # inserting columns
    fn = lambda arg: insert_expected_final_ente(
                        df=df_aliquota,
                        now=now,
                        nr_cnpj_entidade=arg.nr_cnpj_entidade,
                        no_sujeito_passivo=arg.no_sujeito_passivo)
    list(map(fn,cnpj_nome_suj_unpack)) 
    
    # drop duplicates rows.
    df_aliquota.drop_duplicates(inplace=True, ignore_index=True) 

    dupl_iter = df_aliquota.duplicated(subset=['nr_cnpj_entidade', # checking for duplicated rows, 
                'no_sujeito_passivo','dt_inicio_vigencia'],        # given the field 'dt_inicio_vigencia'
                keep=False)
    fn = lambda arg: "D" if arg else "ND" # D - duplicada; ND - ñ dupli.
    dupl_iter_ = list(map(fn,dupl_iter))
    # insert the column 'dt_inicio_vigencia_duplicada'
    df_aliquota= df_aliquota.assign(dt_inicio_vigencia_duplicada=dupl_iter_) 

    # inserting column 'dts_finais_diferentes'
    fn = lambda arg: check_dt_differences(df=df_aliquota, 
                                          nr_cnpj_entidade=arg.nr_cnpj_entidade,
                                          no_sujeito_passivo=arg.no_sujeito_passivo)
    list(map(fn,cnpj_nome_suj_unpack)) 
    
    return df_aliquota

if(__name__=="__main__"):
    data_file_address = './data/df_aliquotas.pkl'
    df_aliquota:pd.DataFrame = pd.read_pickle(data_file_address)
    aliquotas_rpps_transform(df_aliquota)