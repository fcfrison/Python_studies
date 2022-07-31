from collections import namedtuple
import itertools
import numpy as np
import pandas as pd

from transform import *


#df_aliquota = pd.read_excel('./downloaded_data/ALIQUOTA_auricaba.xlsx')
df_aliquota = pd.read_excel('./downloaded_data/ALIQUOTAS.xlsx')
df_aliquota = df_aliquota[['nr_cnpj_entidade', 'no_ente','no_sujeito_passivo',
                           'dt_inicio_vigencia', 'dt_fim_vigencia']]
# we're interested only in 'Ente' and 'Ente-suplementar'.
df_aliquota = df_aliquota.query(
    "no_sujeito_passivo=='Ente' or no_sujeito_passivo=='Ente-suplementar'"
)
# normalizing dates.
df_aliquota.dt_inicio_vigencia = df_aliquota.dt_inicio_vigencia.map(normalize_date)
df_aliquota.dt_fim_vigencia = df_aliquota.dt_fim_vigencia.map(normalize_date)

# creating a class with 'nr_cnpj_entidade' and 'no_sujeito_passivo' attributes.
CnpjNomeSujPass = namedtuple('CnpjNomeSujPass', 'nr_cnpj_entidade  no_sujeito_passivo')
unique_cnpj:np.ndarray = df_aliquota.nr_cnpj_entidade.unique()

# creating lists of objects of the class CnpjNomeSujPass.
cnpj_nome_suj = [list(map(lambda arg: CnpjNomeSujPass(arg,nome_suj),unique_cnpj))
                for nome_suj in ['Ente','Ente-suplementar']]
# unpacking two lists into another.
cnpj_nome_suj_unpack = list(itertools.chain(*cnpj_nome_suj))

# creating the column 'dt_final_esperada'
fn = lambda arg: insert_expct_final(df_aliquota,arg.no_sujeito_passivo,arg.nr_cnpj_entidade)
list(map(fn,cnpj_nome_suj_unpack))
df_aliquota['datas_divergentes']=np.where(
            df_aliquota.dt_final_esperada!=
            df_aliquota.dt_fim_vigencia,True,False)
type(df_aliquota.iloc[6224].dt_fim_vigencia)
type(df_aliquota.iloc[6224].dt_final_esperada)
df_aliquota.to_excel('df_dt_final_esperada_2.xlsx')
'''
insert_expct_final(df_aliquota,"Ente","87297271000139")
print(df_aliquota.query("nr_cnpj_entidade == 1602258000120 & no_sujeito_passivo=='Ente'")[
                ['dt_inicio_vigencia','dt_final_esperada']].sort_values(ascending=True, 
                by='dt_inicio_vigencia'))
'''
### Problemas com pandas nat. É preciso converter ou de NaTType para 
# nat datetime, ou vice-versa.