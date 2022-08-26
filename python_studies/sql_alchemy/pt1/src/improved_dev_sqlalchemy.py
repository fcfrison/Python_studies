import json
import logging
from datetime import datetime

import infra
import sql_funcs


logging.basicConfig(filename=f'logs/{datetime.now().strftime("%d%m%y%H%M%S")}.log', encoding='utf-8', level=logging.ERROR)
# https://sqlserverguides.com/connect-to-oracle-database-using-python/
try:
    with open('../config_sqlalchemy_.json', encoding='utf-8') as file:
        data:dict = json.load(file)
        infra.init_oracle(config_file=data,key_name='instant_client_dir')
        db_conn = infra.DataAcessLayer(
            user = data.get("ouser"),
            password = data.get('opass'),
            host = data.get('servidor'),
            port = data.get('porta'),
            sid = data.get('servico')
        )
    orders = sql_funcs.get_orders_by_customer(dal= db_conn,cust_name="")
    
except Exception as e:
    logging.error(e)
    raise e
