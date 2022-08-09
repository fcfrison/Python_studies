import pandas as pd
import numpy as np

from decimal import Decimal
from datetime import datetime
from collections import namedtuple
import itertools

from transform.rpps_aliquotas import (normalize_date,insert_expected_final_ente,
                       insert_expected_final_ente_suplem,
                       check_dt_differences)

def aliquotas_rpps_transform(df_aliquota:pd.DataFrame,
                            now = datetime.now()):
    '''
    This function applies various transform the data downloaded
    from the endpoint ''
    '''
    df_aliquota = df_aliquota[ # filtering the fields of interest
                    ['nr_cnpj_entidade', 'no_ente','vl_aliquota',
                    'no_sujeito_passivo','dt_inicio_vigencia', 'dt_fim_vigencia']]   

    df_aliquota.query("no_sujeito_passivo == 'Ente' | " +
                    "no_sujeito_passivo == 'Ente-suplementar' ",
                    inplace=True)
    df_aliquota.reset_index(inplace=True, drop=True)
    df_aliquota.vl_aliquota = df_aliquota.vl_aliquota\
                            .map(lambda arg: Decimal(arg)) # turning 'vl_aliquota' into Decimal
    # normalizing dates
    df_aliquota.dt_inicio_vigencia = df_aliquota.dt_inicio_vigencia\
                                        .map(normalize_date)
    df_aliquota.dt_fim_vigencia = df_aliquota.dt_fim_vigencia\
                                        .map(normalize_date)

    # droping na values from the field  'dt_inicio_vigencia'
    df_aliquota.dropna(axis=0,how='any',
                        subset='dt_inicio_vigencia',
                        inplace=True)

    unique_cnpj:np.ndarray = df_aliquota.nr_cnpj_entidade\
                                .unique() 

    # creating a class with 'nr_cnpj_entidade' and 'no_sujeito_passivo' attributes.
    CnpjNomeSujPass = namedtuple('CnpjNomeSujPass', 
                        'nr_cnpj_entidade  no_sujeito_passivo')
    
    # creating lists of objects of the class CnpjNomeSujPass.
    cnpj_nome_suj = [list(map(lambda arg: CnpjNomeSujPass(arg,nome_suj),
                        unique_cnpj))
                for nome_suj in ['Ente','Ente-suplementar']]
    
    # unpacking two lists into another.
    cnpj_nome_suj_unpack = list(itertools.chain(*cnpj_nome_suj))

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
    df_aliquota:pd.DataFrame = pd.read_pickle('./downloaded_data/df_aliquotas.pkl')