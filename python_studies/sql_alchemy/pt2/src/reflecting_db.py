'''
This module creates a table object via the process of reflect the whole
database for a given configuration.
'''
import json

import db
import models
from db.variables import CONFIG_FILE_LOCATION

with open(CONFIG_FILE_LOCATION, encoding='utf-8') as file:
    data:dict = json.load(file)
    db.init_oracle(config_file=data,key_name='instant_client_dir')
    db_conn = db.OracleDAO(
        user = data.get("ouser"),
        password = data.get('opass'),
        host = data.get('servidor'),
        port = data.get('porta'),
        sid = data.get('servico')
    )
tables = models.Tables(db_conn)
