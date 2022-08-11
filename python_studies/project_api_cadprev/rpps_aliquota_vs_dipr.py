import pandas as pd

def create_table_percent(df:pd.DataFrame)->pd.DataFrame:
    '''
    This function creates a table that contains a column with the 
    field 'perc_56_19', that represents the resulting 'vl_rubrica' 
    considering the division between 'id_rubrica'=56 and 'id_rubrica'=19.
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

df_DIPR:pd.DataFrame = pd.read_pickle('./downloaded_data/DIPR_2021.pkl')
df_aliquotas:pd.DataFrame = pd.read_pickle('./downloaded_data/df_aliquota_transformed.pkl')

# despite the fact that'vl_rubrica' is a monetary value, it'll treated as float.
df_DIPR = df_DIPR.astype(dict(vl_rubrica='float128',
                              id_rubrica='str'))
# creating table with 
df_DIPR_grouped = create_table_percent(df=df_DIPR)

# insert the column 'dates'
fn = lambda arg: pd.Period(f'{arg.dt_mes}-1-{arg.dt_ano}',freq='M')\
    .end_time.date() # get the last day of the month
list_dates = list(map(fn,df_DIPR_grouped.itertuples()))
df_DIPR_grouped = df_DIPR_grouped.assign(dates=list_dates)



# -----------------------------------------------------------------------------------------
df_DIPR_grouped['dates'] = pd.to_datetime(df_DIPR_grouped['dates']).dt.date
df_aliquotas['dt_inicio_vigencia'] = pd.to_datetime(df_aliquotas['dt_inicio_vigencia']).dt.date
df_aliquotas['dt_fim_vigencia'] = pd.to_datetime(df_aliquotas['dt_fim_vigencia']).dt.date
#----------------------------------------------------------------
df_aliquotas_teste = df_aliquotas.query("nr_cnpj_entidade == '97320030000117' & "+
                   "no_sujeito_passivo == 'Ente'")

dipr_iter = list(df_DIPR_grouped.query("nr_cnpj_entidade == '97320030000117'").itertuples())

x = df_aliquotas_teste.apply(lambda arg: True if (arg.dt_inicio_vigencia<=dipr_iter[0].dates and \
    dipr_iter[0].dates<arg.dt_fim_vigencia) else False, axis=1)
df_aliquotas_teste[x]

#geeksforgeeks.org/how-to-compare-two-columns-in-pandas/
