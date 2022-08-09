import itertools
import pandas as pd


df_dipr:pd.DataFrame = pd.read_pickle('./downloaded_data/DIPR_2021.pkl')
df_aliquotas:pd.DataFrame =pd.read_pickle('./downloaded_data/df_aliquotas.pkl')
df_dipr.reset_index(inplace=True, drop=True)
df_aliquotas.reset_index(inplace=True, drop=True)

def generate_control_data(cnpj:str, year:int, month:int):
    return [dict(nr_cnpj_entidade=cnpj, dt_ano=year, dt_mes=month_) 
            for month_ in range(1,month + 1)]

# creating an iterator with cnpjs
cnpj_iter = df_aliquotas.nr_cnpj_entidade.unique()
month = df_dipr.dt_mes.max()
year = df_dipr.dt_ano.max()

# creating the table to control cnpj, month and year   
fn = lambda arg: generate_control_data(arg,year,month)
list_df_control = list(map(fn,cnpj_iter))
df_data_control = pd.DataFrame(list(itertools.chain(*list_df_control)))

# grouping by data considering 'df_dipr', given 'nr_cnpj_entidade','dt_mes', 'dt_ano'
df_dipr_grouped = df_dipr.groupby(['nr_cnpj_entidade','dt_mes', 'dt_ano'],
                    as_index=False).count()[['nr_cnpj_entidade','dt_mes',
                    'dt_ano']]

# joining the tables
df_data_control=df_data_control.merge(df_dipr_grouped,how='left',indicator=True)

fn = lambda arg: False if(arg=='both') else True
df_data_control._merge = df_data_control._merge.apply(fn)
df_data_control.rename({'merge_':'nao_enviou'},inplace=True)
df_data_control.to_excel('./downloaded_data/controle_envios.xlsx')