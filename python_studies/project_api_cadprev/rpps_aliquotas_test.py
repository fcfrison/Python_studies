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

pd.set_option('expand_frame_repr',False,'display.max_row',None)
#df_aliquota = pd.read_excel('./downloaded_data/ALIQUOTA_auricaba.xlsx')
df_aliquota = pd.read_excel('./downloaded_data/ALIQUOTAS.xlsx')
df_aliquota = df_aliquota[['nr_cnpj_entidade', 'no_ente','no_sujeito_passivo',
                           'dt_inicio_vigencia', 'dt_fim_vigencia']]

df_aliquota.dt_inicio_vigencia = df_aliquota.dt_inicio_vigencia.map(normalize_date)
df_aliquota.dt_fim_vigencia = df_aliquota.dt_fim_vigencia.map(normalize_date)


df_aliquota.query("dt_inicio_vigencia >dt_fim_vigencia")[['dt_inicio_vigencia','dt_fim_vigencia']]
df_aliquota.query("no_sujeito_passivo == 'Ente'").dt_inicio_vigencia.sort_values(ascending=True)

iterator = df_aliquota.query("nr_cnpj_entidade == 87297271000139 & no_sujeito_passivo=='Ente'")[
                  ['dt_inicio_vigencia']].sort_values(ascending=True, 
                  by='dt_inicio_vigencia')
type(iterator)
iterator.loc[339]
for item in iterator:
    print(item)
df_aliquota.no_sujeito_passivo.unique()

df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
for item in df.iterrows():
    print(type(item))
iterator.iloc[5]
iterator.size
lista = list(iterator.itertuples())


    
    