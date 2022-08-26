'''
This module is a simple development based on the book 'Essential SQLAlchemy' 
by Jason Myers and Rick Copeland.
It's purpose is just to explore and understand the Python library SqlAlchemy.
'''

import json
import logging
from datetime import datetime

import infra
import models


logging.basicConfig(filename=f'logs/{datetime.now().strftime("%d%m%y%H%M%S")}.log', encoding='utf-8', level=logging.ERROR)
# https://sqlserverguides.com/connect-to-oracle-database-using-python/
try:
    with open('../config_sqlalchemy_.json', encoding='utf-8') as file:
        data:dict = json.load(file)
        infra.init_oracle(config_file=data,key_name='instant_client_dir')
        db_conn = infra.OracleDAO(
            user = data.get("ouser"),
            password = data.get('opass'),
            host = data.get('servidor'),
            port = data.get('porta'),
            sid = data.get('servico')
        )

    #creating the tables
    metadata = models.create_tables(db_conn.engine)
    cookies, users, orders, line_items = metadata.sorted_tables

    # data to be inserted in the database
    inventory_list = [
        {   'cookie_name': 'white chocolate',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'WC01',
            'quantity': 50,
            'unit_cost': 0.75
        },
        {
            
            'cookie_name': 'vanilla sky',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'VSY01',
            'quantity': 200,
            'unit_cost': 0.35
        },
        {
            
            'cookie_name': 'chocolate night',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'VSY01',
            'quantity': 150,
            'unit_cost': 1.35
        }
    ]
    # inserting data on the cookies table
    db_conn.insert_data(cookies,inventory_list)

    # more data to be inserted
    customer_list = [
        {
        'username': 'cookiemon',
        'email_address': 'mon@cookie.com',
        'phone': '111-111-1111',
        'password': 'password'},
        {
        'username': 'cakeeater',
        'email_address': 'cakeeater@cake.com',
        'phone': '222-222-2222',
        'password': 'password'
        },
        {
        'username': 'pieguy',
        'email_address': 'guy@pie.com',
        'phone': '333-333-3333',
        'password': 'password'
        }
    ]

    db_conn.insert_data(users,customer_list)

    # more data to be inserted
    orders_data = [
        {
        'user_id':1,
        'order_id':1
        },
        {
        'user_id':2,
        'order_id':2
        }    
    ]
    db_conn.insert_data(orders,orders_data)

    # more data to be inserted

    order_items = [
        {
            'order_id': 1,
            'cookie_id': 1,
            'quantity': 2,
            'extended_cost': 1.00
        },
        {
            'order_id': 1,
            'cookie_id': 3,
            'quantity': 12,
            'extended_cost': 3.00
        },
        {
            'order_id': 2,
            'cookie_id': 1,
            'quantity': 24,
            'extended_cost': 12.00
        },
        {
            'order_id': 2,
            'cookie_id': 2,
            'quantity': 6,
            'extended_cost': 6.00
        }
    ]

    db_conn.insert_data(line_items,order_items)

    # selecting data from the database
    result = db_conn.select_data(cookies,'fetch_all',sel_columns=['cookie_name','cookie_sku'],
                                order_by_column=['cookie_name'], descending=True,
                                limit_rows=2)
    sum_quantity = db_conn.sum_values(cookies,"quantity")
    count_column = db_conn.count_values(cookies,"cookie_recipe_url","count_urls")

    # selecting more data from the db, given some conditions
    result = db_conn.select_data(cookies,'fetch_all',\
        filter_clause=[
            ("like","cookie_name",("%chocolate%",)),
            ("between","unit_cost",(0,1))
            ])
    result = db_conn.select_data(cookies,'fetch_all',sel_columns=['cookie_recipe_url'],
        filter_clause=[
            ("distinct","cookie_recipe_url",(None,)),
            ])
    result = db_conn.select_w_join(sel_columns = [(orders,"order_id"),(users,"username"),
                        (users,"phone"), (cookies, "cookie_name"), (line_items,"quantity"), 
                        (line_items,"extended_cost")], 
                                join_list= [orders,users,line_items,cookies],
                                where_params={'table':users, 'column_name':'username',
                        'operator':'==','comparation_value':'cookiemon'}, 
                        type_result = 'fetch_all')
    # testing the raw_sql module
    result = db_conn.raw_sql(
        """
        SELECT 
            a.username, 
            b.cookie_name,
            c.quantity
        FROM users a
        JOIN orders w
            ON a.user_id = w.user_id
        JOIN line_items c
            ON w.order_id = c.order_id
        JOIN cookies b
            ON b.cookie_id = c.cookie_id
        """, 
        type_result = 'fetch_all')
except Exception as e:
    logging.error(e)
    raise e