import datetime
import pandas as pd
import numpy as np

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
        date = pd.to_datetime(date, errors = 'coerce')
        try:
            date = date.normalize()
        except AttributeError:
            return date
    else:
        return date
    return date

def insert_expct_final( df:pd.DataFrame, 
                        no_sujeito_passivo:str,
                        nr_cnpj_entidade:str)->None:
    '''
    insert_expct_final
    ---------------
    insert_expct_final( df:pd.DataFrame, 
                        no_sujeito_passivo:str,
                        nr_cnpj_entidade:str)


    Function that creates the column dt_final_esperada
    and insert data into it, according to certain rules.

    parameters
    ---------------
        df: the DataFrame reference
        no_sujeito_passivo: the name of 'sujeito passivo'
        nr_cnpj_entidade: the 'cnpj' value of the rpps
    '''
    try:
        df.insert(len(df.columns),"dt_final_esperada",'') # create dt_final_esperada column 
        df.insert(len(df.columns),"datas_invertidas",'')
    except ValueError:
        pass
    iterator = df.query(f"nr_cnpj_entidade == {nr_cnpj_entidade} & " +
                        f"no_sujeito_passivo =='{no_sujeito_passivo}'")\
                        [['dt_inicio_vigencia','dt_fim_vigencia']].sort_values(ascending=True, 
                        by='dt_inicio_vigencia')
    list_iter = list(iterator.itertuples()) # create iterator with namedtuples
    try:
        for index,nm_tuple in enumerate(list_iter):
            if(nm_tuple.dt_inicio_vigencia>nm_tuple.dt_fim_vigencia): #dt_inicio_vigencia>dt_fim_vigencia then do nothing. 
                df['datas_invertidas'].loc[nm_tuple.Index] = True
            next_item_time = list_iter[index+1].dt_inicio_vigencia
            df["dt_final_esperada"].loc[nm_tuple.Index] = next_item_time - \
                                    datetime.timedelta(days = 1)
    except IndexError:
        df["dt_final_esperada"].loc[nm_tuple.Index] =pd.Nat ###é preciso criar um objeto to tipo pandas.Nat