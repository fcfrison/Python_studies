'''
This module purpose is to create some simple data access classes to 
make it easy the creation and management of a database connection. 
I also developed some methods for simple operations like insert data into a db, 
select data (given some parameters) from a db and count values from a column.
'''

import cx_Oracle

from collections import namedtuple, deque
from decimal import Decimal
from sqlalchemy import create_engine, desc
from sqlalchemy.sql import select, func
from sqlalchemy import Table, Column
from sqlalchemy.engine.cursor import BaseCursorResult
from sqlalchemy.exc import IntegrityError
from typing import List, Tuple

class DAO:
    def __init__(self, user:str, password:str,host:str,port:str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port



class OracleDAO(DAO):
    '''
    For the sake of simplicity, i created an specific Data Access Object for
    an Oracle Database. In a certain way, it goes against the principle of generalization
    that informs software that is based on ORM.
    '''
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
        
    
   
    def select_data(self, table:Table, type_result:str,*args,filter_clause:\
                    List[Tuple[str,str,Tuple]] = None, sel_columns:List[str]=None, 
                    order_by_column:List[str] = None, descending:bool=False, 
                    limit_rows:int = None):
        '''
        Method that selects data from a table given the desired type of return.

        Parameters
        ----------------------
            table\n 
                An object from the class Table

            type_result\n 
                A string type that must match the following words:
                    >> 'fetch_all': to use the 'fetchall' method from the SqlAlchemy library;
                    >> 'first': 'fetch_all': to use the 'first' method from the SqlAlchemy library;
                    >> 'fetch_one': to use the 'fetchone' method from the SqlAlchemy library;
                    >> 'scalar': to use the 'scalar' method from the SqlAlchemy library;
            
            filter_clause\n
                A list of tuples. The first element of the tuple is the name of the ClauseElement 
                method to be applied, the second name of the column and the third are the arguments 
                to be passed to the method. 
                For sake of simplicity, it were implemented only the methods 'like', 'between', 'distinct'.
            
            sel_column\n 
                A list of columns names to be returned;
            
            order_by_column\n 
                A list of columns names to order by;
        '''
        
        if(sel_columns): # if sel_columns, means there're selected columns
            columns_list = [self.search_column(table,column)
                                for column in sel_columns]
            sel = select(*columns_list)
        else: sel = select(table)

        if(filter_clause): # if filter_clause means there's a filter statement
            FilterObject = namedtuple("FilterObject",
                            ["method_name","column_object","tuple_arguments"])
            fn = lambda arg: FilterObject(arg[0],self.search_column(table,arg[1]),\
                                        arg[2])
            list_clauses = list(map(fn,filter_clause))
            for item in list_clauses: # implementing the methods 'like', 'between' and 'distinct'
                match(item.method_name):
                    case 'like':
                        sel = sel.where(item.column_object.like(*item.tuple_arguments))
                    case'between':
                        sel = sel.where(item.column_object.between(*item.tuple_arguments))
                    case'distinct':
                        sel = sel.distinct(item.column_object)

        if(order_by_column):
            order_by_list = [self.search_column(table,column)
                                for column in order_by_column]
            if(descending==True):
                order_by_list = [desc(*order_by_list)]
            sel = sel.order_by(*order_by_list)
        if(limit_rows):
            sel = sel.limit(limit_rows)
        result_proxy = self.connection.execute(sel)

        match(type_result): # selecting the type of result
            case 'fetch_all':
                return result_proxy.fetchall()
            case 'first':
                return result_proxy.first()
            case 'fetch_one':
                return result_proxy.fetchone()
            case 'scalar':
                return result_proxy.scalar()
            case _:
                raise AttributeError("'type_result' param must assume the values"+ 
                    " 'fetch_all', 'first', 'fetch_one' or 'scalar'.")
    
    def select_w_join(self,*_, sel_columns:List[Tuple[Table,str]],
                      join_list: List[Table], type_result:str,
                      where_params: dict = None):
        '''
        Method that query data from the database joining its tables. 

        Parameters
        ----------------------        
        sel_columns\n 
            A list of tuples. It tells the algorithm the columns of interest.
            The first element of the tuple is a sqlalchemy.Table object, while the second is the name of the column to be selected.\n
            Example \n
                sel_columns = [(orders,"order_id"),(users,"username"),(users,"phone"), (cookies, "cookie_name"),\n 
                (line_items,"quantity"), (line_items,"extended_cost")]\n\n
        
        join_list\n
            A list of sqlalchemy.Table objects. It tells what are the tables to be joined.\n
            Example \n
            join_list = [orders,users,line_items,cookies] \n\n
        
        
        type_result\n  
            A string type that must match the following words:\n
                >> 'fetch_all': to use the 'fetchall' method from the library SqlAlchemy ;\n
                >> 'first': 'fetch_all': to use the 'first' method from the library SqlAlchemy;\n
                >> 'fetch_one': to use the 'fetchone' method from the library SqlAlchemy;\n
                >> 'scalar': to use the 'scalar' method from the SqlAlchemy library;\n\n
        
        where_params\n
            A dictionary that informs the arguments that fill the 'where' clause.\n
            The dict must have these key-values pairs:
                >> table: an object from the sqlalchemy.Table class;\n
                >> column_name: a string with the column name;\n
                >> operator: a rule of comparision;\n
                >> comparation_value: the value to be compared;\n
            For the sake of simplicity, was implemented only the operators '==' and
            'like'.            

            Example
                where_params={
                    'table':users, 
                    'column_name':'username',
                    'operator':'==',
                    'comparation_value':'cookiemon'}

        
        '''
        fn = lambda arg: self.search_column(arg[0],arg[1])
        columns_list = list(map(fn,sel_columns))
        sel = select(columns_list)
        deque_join = deque(join_list)
        first_element = deque_join.popleft()
        
        while(deque_join):
            first_element = self.join_statements(first_element,deque_join.popleft())
        sel = sel.select_from(first_element)
        
        if(where_params):
            table = where_params['table']
            column = self.search_column(table,where_params['column_name'])
            operator = where_params['operator']
            match(operator):
                case 'like':
                    sel = sel.where(column.like(where_params['comparation_value']))
                case'==':
                    sel = sel.where(column==where_params['comparation_value'])
                case _ :
                    raise AttributeError('Wrong operator.')
        result_proxy = self.connection.execute(sel)    
        
        match(type_result): # selecting the type of result
            case 'fetch_all':
                return result_proxy.fetchall()
            case 'first':
                return result_proxy.first()
            case 'fetch_one':
                return result_proxy.fetchone()
            case 'scalar':
                return result_proxy.scalar()
            case _:
                raise ValueError("'type_result' param must assume the values"+ 
                    " 'fetch_all', 'first', 'fetch_one' or 'scalar'.")
    


    def join_statements(self,first_element,join_element):
        first_element = first_element.join(join_element)
        return first_element

    def sum_values(self,table_obj:Table,column_name:str)->int or float or Decimal:
        '''
        Method that sum the values of a given column. 

        Parameters
        ----------------------
        table_obj: an object from the class Table
        column_name: a string with a column name

        Output
        ----------------------
        rp.scalar(): a numeric value        
        '''
        column = self.search_column(table_obj,column_name)
        sel = select([func.sum(column)])
        rp = self.connection.execute(sel)
        return rp.scalar()

    def count_values(self, table_obj:Table,column_name:str,
                    label_column:str=None)->int:
        '''
        Method that count the instances of a given column. 

        Parameters
        ----------------------
        table_obj: an object from the class Table
        column_name: a string with a column name
        label_column: a string 

        Output
        ----------------------
        record[label_column]: the number of counted items       
        '''        
        column = self.search_column(table_obj,column_name)
        if(label_column):
            sel = select([func.count(column).label(label_column)])
        else:
            sel = select([func.count(column)])
        rp = self.connection.execute(sel)
        record = rp.first()
        return record[label_column]

    def search_column(self,table_obj:Table,column_name:str)->Column:
        '''
        Method that searches and returns a Table object, given a column name.

        Parameters
        ----------------------
        table_obj: an object from the class Table
        column_name: a string with a column name

        Returns
        ----------------------
        column: an object from the class Column
        '''
        for column in table_obj.c:
            if(column.name == column_name):
                return column

    def raw_sql(self, SQL:str,type_result:str):
        '''
        Method that queries against a table via a "raw sql" statement. 

        Parameters
        ----------------------
        SQL\n
            A string with a SQL statement.

        type_result\n  
            A string type that must match the following words:\n
                >> 'fetch_all': to use the 'fetchall' method from the library SqlAlchemy ;\n
                >> 'first': 'fetch_all': to use the 'first' method from the library SqlAlchemy;\n
                >> 'fetch_one': to use the 'fetchone' method from the library SqlAlchemy;\n
                >> 'scalar': to use the 'scalar' method from the SqlAlchemy library;\n\n
        
        Returns
        ----------------------
            A result proxy with the chosen type of result ('fetch_all', 'first', ...).
        
        '''
        try:
            transaction = self.connection.begin()
            result_proxy = self.connection.execute(SQL)
            transaction.commit()
            match(type_result): # selecting the type of result
                case 'fetch_all':
                    return result_proxy.fetchall()
                case 'first':
                    return result_proxy.first()
                case 'fetch_one':
                    return result_proxy.fetchone()
                case 'scalar':
                    return result_proxy.scalar()
                case _:
                    raise AttributeError("'type_result' param must assume the values"+ 
                        " 'fetch_all', 'first', 'fetch_one' or 'scalar'.")
        except Exception as e:
            raise e  

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

