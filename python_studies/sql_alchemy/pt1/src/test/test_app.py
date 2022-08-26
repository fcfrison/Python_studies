''''
This module is designed for testing with a database. 
'''

import unittest
import json
import logging
from datetime import datetime
import sys
import os
from test_funcs_variables import *

sys.path.append(get_parent_directory(os.getcwd()))


import infra.db.improved_DAO
from sql_funcs import get_orders_by_customer

logging.basicConfig(filename=f'test_logs/{datetime.now().strftime("%d%m%y%H%M%S")}.log', encoding='utf-8', level=logging.ERROR)

def insert_data()->bool|Exception:
    '''
    Function that inserts the toy data in db . 

    Returns
    ----------------
        True if the data was correctly inserted; 
        Exception if the data was not inserted;
    '''
    try:
        with open(CONFIG_FILE_LOCATION, encoding='utf-8') as file:
            data:dict = json.load(file)
            db_conn = infra.DataAcessLayer(
                user = data.get("ouser"),
                password = data.get('opass'),
                host = data.get('servidor'),
                port = data.get('porta'),
                sid = data.get('servico')
            )            
    except Exception as e:
        logging.error(e)
        raise e
    db_conn.insert_data(db_conn.cookies,inventory_list)
    db_conn.insert_data(db_conn.users,customer_list)
    db_conn.insert_data(db_conn.orders,orders_data)
    db_conn.insert_data(db_conn.line_items,inventory_list)
    return True
if(not insert_data()):
    raise Exception("The data for the testing was not inserted.")

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  
        try:
            with open(CONFIG_FILE_LOCATION, encoding='utf-8') as file:
                data:dict = json.load(file)
                db_conn = infra.DataAcessLayer(
                    user = data.get("ouser"),
                    password = data.get('opass'),
                    host = data.get('servidor'),
                    port = data.get('porta'),
                    sid = data.get('servico')
                )            
        except Exception as e:
            logging.error(e)
            raise e
        return db_conn

    def test_orders_by_customer_blank(self):
        results = get_orders_by_customer('',dal=TestApp.setUpClass())
        self.assertEqual(results, [])
    def test_orders_by_customer_blank_shipped(self):
        results = get_orders_by_customer('',dal=TestApp.setUpClass(), shipped=True)
        self.assertEqual(results, [])
    def test_orders_by_customer_blank_notshipped(self):
        results = get_orders_by_customer('',dal=TestApp.setUpClass(), shipped=False)
        self.assertEqual(results, [])
    def test_orders_by_customer_blank_details(self):
        results = get_orders_by_customer('', dal=TestApp.setUpClass(),details=True)
        self.assertEqual(results, [])
    def test_orders_by_customer_blank_shipped_details(self):
        results = get_orders_by_customer('',dal=TestApp.setUpClass(), 
                                            details=True, shipped=True)
        self.assertEqual(results, [])
    def test_orders_by_customer(self):
        expected_results = [(1, u'cookiemon', u'111-111-1111')]
        results = get_orders_by_customer('cookiemon',dal=TestApp.setUpClass())
        self.assertEqual(results, expected_results)
    def test_orders_by_customer_shipped_only(self):
        results = get_orders_by_customer('cookiemon', shipped=True,dal=TestApp.setUpClass())
        self.assertEqual(results, [])
    def test_orders_by_customer_unshipped_only(self):
        expected_results = [(1, u'cookiemon', u'111-111-1111')]
        results = get_orders_by_customer('cookiemon', shipped=False,dal=TestApp.setUpClass())
        self.assertEqual(results, expected_results)

