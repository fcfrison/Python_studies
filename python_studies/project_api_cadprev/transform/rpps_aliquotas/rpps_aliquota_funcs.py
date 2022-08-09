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
    description
    ----------------

    This function inserts the fields 'dt_final_esperada' and 
    'datas_invertidas'. The former contains data related to 
    the expected date given the field 'dt_inicio_vigencia' and
    the latter refers to the situation in which 
    'dt_inicio_vigencia'>'dt_fim_vigencia'.
    It only applies to "no_sujeito_passivo =='Ente'".

    parameters
    ----------------
        df:pd.DataFrame, 
        now:datetime.datetime,
        nr_cnpj_entidade:str
    '''
    # Insert new columns.
    try:
        df.insert(loc=len(df.columns), column="dt_final_esperada",
                          value=pd.NaT) # create dt_final_esperada column 
        df.insert(loc=len(df.columns),column="datas_invertidas",value=np.nan)
    except ValueError:
        pass
    
    # Query data from 'Ente'
    iterator = df.query(f"nr_cnpj_entidade == '{nr_cnpj_entidade}'" +
                        f"& no_sujeito_passivo =='{no_sujeito_passivo}'")\
                        [['dt_inicio_vigencia','dt_fim_vigencia','nr_cnpj_entidade']]\
                        .sort_values(ascending=True, by='dt_inicio_vigencia')

    list_iter = list(iterator.itertuples()) # create iterator with namedtuple
    for index, nm_tuple in enumerate(list_iter):
        if(nm_tuple.dt_inicio_vigencia>nm_tuple.dt_fim_vigencia): # dates are inverted
                df['datas_invertidas'].loc[nm_tuple.Index] = True
        
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


def insert_expected_final_ente_suplem(df:pd.DataFrame, 
                                      nr_cnpj_entidade:str,
                                      now:datetime.datetime)->None:
    '''
    description
    ----------------

    This function inserts the fields 'dt_final_esperada_suplement' and 
    'datas_invertidas'. The former contains data related to 
    the expected date given the field 'dt_inicio_vigencia' and
    the latter refers to the situation in which 
    'dt_inicio_vigencia'>'dt_fim_vigencia'.
    It only applies to "no_sujeito_passivo =='Ente-suplementar'".

    parameters
    ----------------
        df:pd.DataFrame, 
        now:datetime.datetime,
        nr_cnpj_entidade:str
    '''
    
    try:
        df.insert(loc=len(df.columns), column="dt_final_esperada_suplement",
                          value=pd.NaT) # create dt_final_esperada column 
    except ValueError:
        pass
    iterator = df.query(f"nr_cnpj_entidade == '{nr_cnpj_entidade}'" +
                        f"& no_sujeito_passivo =='Ente-suplementar'")\
                        [['dt_inicio_vigencia','dt_fim_vigencia','nr_cnpj_entidade']]\
                        .sort_values(ascending=True, by='dt_inicio_vigencia')
    list_iter = list(iterator.itertuples())
    for index, nm_tuple in enumerate(list_iter):
        if(nm_tuple.dt_inicio_vigencia>nm_tuple.dt_fim_vigencia): # dates are inverted
                df['datas_invertidas'].loc[nm_tuple.Index] = True
        
        if(isinstance(nm_tuple.dt_fim_vigencia, 
                pd._libs.tslibs.nattype.NaTType)): # there's no dt_fim_vigencia
            
            if(index==len(list_iter)-1): # if item in the last position
                
                if(nm_tuple.dt_inicio_vigencia>=now): 
                    df['dt_final_esperada_suplement']\
                        .loc[nm_tuple.Index] = \
                            nm_tuple.dt_inicio_vigencia
                else:
                    df['dt_final_esperada_suplement']\
                        .loc[nm_tuple.Index] = now
            
            else: # null item is not in the last position 
                if(list_iter[index+1].dt_inicio_vigencia == # if dt_inicio_vigencia from next item
                    nm_tuple.dt_inicio_vigencia):           # in list is equal, search different item
                    try:
                        list_iter[index+2] #check if index is one position before the last.
                        sub_list = list_iter[index+2:] # create a sub list
                        for i,item in enumerate(sub_list):
                            if(item.dt_inicio_vigencia!=
                                nm_tuple.dt_inicio_vigencia):
                                df['dt_final_esperada_suplement'].loc[nm_tuple.Index] =  \
                                        item.dt_inicio_vigencia - \
                                        datetime.timedelta(seconds = 1) # the end of the day before
                                break
                            if(len(sub_list)==i+1): # if iteration ends, then no different 
                                raise IndexError    # dt_inicio_vigencia was found
                    except IndexError:
                        if(list_iter[len(list_iter)-1].dt_inicio_vigencia>=now):
                            df['dt_final_esperada_suplement'].loc[nm_tuple.Index] = \
                                list_iter[len(list_iter)-1].dt_inicio_vigencia
                        else:
                            df['dt_final_esperada_suplement'].loc[nm_tuple.Index] = now
                else: # if dt_fim_vigencia is null and there's dt_inicio_vigencia
                      # on the next item in the list.
                    df['dt_final_esperada_suplement'].loc[nm_tuple.Index] = \
                        df['dt_inicio_vigencia'].loc[nm_tuple.Index+1] - \
                            datetime.timedelta(seconds = 1)
        else:
            df['dt_final_esperada_suplement']\
                        .loc[nm_tuple.Index] = \
                            nm_tuple.dt_fim_vigencia

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
        if nm_tuple.dt_fim_vigencia.date() != \
            nm_tuple.dt_final_esperada.date():
                df['dts_finais_diferentes'].loc[nm_tuple.Index]="DFD"