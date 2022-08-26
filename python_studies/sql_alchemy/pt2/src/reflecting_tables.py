'''
Usually, instead of creating the tables via SqlAlchemy, we work with a db 
whose schema is already setted for us. Therefore, instead of manually create
the table objects, it's better to just reflect them from the database.  
'''

import json

from sqlalchemy import MetaData, Table
import db
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
metadata = MetaData()
cookies = Table('cookies', metadata, autoload=True, autoload_with=db_conn.engine)
users = Table('users', metadata, autoload=True, autoload_with=db_conn.engine)
line_items = Table('line_items', metadata, autoload=True, autoload_with=db_conn.engine)
orders = Table('orders', metadata, autoload=True, autoload_with=db_conn.engine)

metadata