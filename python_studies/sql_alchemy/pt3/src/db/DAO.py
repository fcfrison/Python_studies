'''
This module purpose is to create some simple data access classes to 
make it easy the creation and management of a database connection. 
I also developed some methods for simple operations like insert data into a db, 
select data (given some parameters) from a db and count values from a column.
'''

import cx_Oracle
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List

from .variables import *


class DAO:
    '''
    For the sake of simplicity, i created an specific Data Access Object for
    an Oracle Database. In a certain way, it goes against the principle of generalization
    that informs software that is based on ORM.
    '''
    def __init__(self, user:str, password:str,host:str,port:str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port



class OracleDAO(DAO):
    def __init__(self, user:str, password:str,host:str,port:str,
                       service:str = None, sid:str = None):
        super().__init__(user, password,host,port)
        self.service = service
        self.sid = sid
        self.engine = None
        self.connection = None
        
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self,*arg):
        engine = create_engine(self.create_conn_string(),
                               pool_recycle=10,
                               pool_size=50,
                               echo=True)
        self._engine = engine

    
    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self,*arg):
        self._connection = self.engine.connect() 
    
    def create_conn_string(self)->str:
        '''
        Method that generates a string to connect with an Oracle database.

        Returns
        ----------------------
            A string with the required configuration to connect with a database.
        '''
        if(self.service and not self.sid):
            preq = cx_Oracle.makedsn(self.host, self.port, service_name = self.service)
        elif(self.sid  and not self.service):
            preq = cx_Oracle.makedsn(self.host, self.port, sid = self.sid)
        else:
            raise Exception("Problems with 'service'or 'sid' fields.")
        return f'oracle://{self.user}:{self.password}@{preq}'

    
    def __repr__(self):
        '''
        The way the implementation of this method is done is just for
        development purposes.

        '''
        return self.create_conn_string()


def init_oracle(config_file:dict, key_name:str):
        '''
        Function that sets up cx_oracle with the Oracle's Instant Client driver 
        location.

        parameters
        ----------
        config_file:json
            A json file with the Oracle data base information.
        
        key_name:str
            The key name in the json file that indicates the location
            of the Oracle's Instant Client driver.

        '''
        orcl_conf=config_file[key_name]
        cx_Oracle.init_oracle_client(lib_dir=orcl_conf)

with open(CONFIG_FILE_LOCATION, encoding='utf-8') as file:
    data:dict = json.load(file)
    init_oracle(config_file=data,key_name='instant_client_dir')
    db_conn = OracleDAO(
        user = data.get("ouser"),
        password = data.get('opass'),
        host = data.get('servidor'),
        port = data.get('porta'),
        sid = data.get('servico')
    )

Session = sessionmaker(bind=db_conn.engine) # creating a Session object.
session = Session() # this session is used to interact with the db.