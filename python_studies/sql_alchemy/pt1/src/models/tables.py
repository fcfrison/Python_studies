from sqlalchemy import Table, Column, Integer, Numeric, String, Boolean
from sqlalchemy import MetaData, CheckConstraint, ForeignKey, DateTime, Identity
from sqlalchemy.engine import Engine
from datetime import datetime
from sqlalchemy import DateTime



def create_tables(engine:Engine)->MetaData:
    '''
    Function that creates a finite number of tables.

    Parameters
    ----------------------
    engine\n
        An engine to connect to a database.
    
    Returns
    ----------------------
        An object from the class MetaData .
    '''
    metadata = MetaData() # a metadata object is necessary to tie together 
                      # the table object information

    cookies = Table('cookies', metadata,
                    Column('cookie_id', Integer(), Identity(start=1), primary_key=True),
                    Column('cookie_name', String(50), index=True),
                    Column('cookie_recipe_url', String(255)),
                    Column('cookie_sku', String(55)),
                    Column('quantity', Integer()),
                    Column('unit_cost', Numeric(12, 2)),
                    CheckConstraint('quantity >= 0', name='quantity_positive'), 
                    CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
                    )

    users = Table('users', metadata,
                    Column('user_id', Integer(), Identity(start=1),primary_key=True),
                    Column('customer_number', Integer(), autoincrement=True),
                    Column('username', String(15), nullable=False, unique=True),
                    Column('email_address', String(255), nullable=False),
                    Column('phone', String(20), nullable=False),
                    Column('password', String(25), nullable=False),
                    Column('created_on', DateTime(), default=datetime.now),
                    Column('updated_on', DateTime(), default=datetime.now, 
                            onupdate=datetime.now)
                    )

    orders = Table('orders', metadata,
                Column('order_id', Integer(), primary_key=True),
                Column('user_id', ForeignKey('users.user_id')), 
                Column('shipped', Boolean(), default=False)
                )

    line_items = Table('line_items', metadata,
                        Column('line_items_id', Integer(),Identity(start=1), 
                                primary_key=True),
                        Column('order_id', ForeignKey('orders.order_id')),
                        Column('cookie_id', ForeignKey('cookies.cookie_id')),
                        Column('quantity', Integer()),
                        Column('extended_cost', Numeric(12, 2))
                    )

    
    
    
    metadata.create_all(engine)
    return metadata
