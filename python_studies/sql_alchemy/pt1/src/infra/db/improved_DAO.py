'''
This module purpose is to create some simple data access classes to 
make it easy the creation and management of a database connection. 
I also developed some methods for simple operations like insert data into a db, 
select data (given some parameters) from a db and count values from a column.
'''

from typing import List
from sqlalchemy.engine.cursor import BaseCursorResult
from sqlalchemy.exc import IntegrityError
import cx_Oracle

from sqlalchemy import create_engine

from models import *

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

class DataAcessLayer(OracleDAO):
    def __init__(self,user:str, password:str,host:str,port:str,
                       service:str = None, sid:str = None):
        super().__init__(user, password,host,port,service, sid)
        self.metadata = create_tables(self.engine)
        self.cookies, self.users, self.orders, self.line_items = self.metadata.sorted_tables

    def insert_data(self, table:Table, values_:List[dict])->BaseCursorResult:
        '''
        Method that insert data into a table. 

        Parameters
        ----------------------
            table\n 
                An object from the class Table. It tells what is table the data will
                be inserted on.
            
            values_\n 
                A list with dictionaries with the data to be inserted.
        
        Returns
        ----------------------
            connection.execute(ins,values_)

        '''

        try:
            ins = table.insert()
            transaction = self.connection.begin() # starting a transaction
            result = self.connection.execute(ins,values_)
            transaction.commit()
            return result
        except IntegrityError as error:
            transaction.rollback()
            raise error
        

        