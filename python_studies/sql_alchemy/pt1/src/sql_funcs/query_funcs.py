from typing import List
from sqlalchemy.sql import select
from sqlalchemy.engine.row import Row

from infra.db.improved_DAO import DataAcessLayer


def get_orders_by_customer(cust_name:str,dal:DataAcessLayer,shipped:bool=None,
                          details:bool=False)->List[Row]:
    '''
    Function that gets the customer name and returns the list of the orders
    related to him.
    '''
    columns = [dal.orders.c.order_id, dal.users.c.username, dal.users.c.phone]
    joins = dal.users.join(dal.orders)
    if details:
        columns.extend([dal.cookies.c.cookie_name,
                        dal.line_items.c.quantity,
                        dal.line_items.c.extended_cost])
        joins = joins.join(dal.line_items).join(dal.cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins).where(
        dal.users.c.username == cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(dal.orders.c.shipped == shipped)
    return dal.connection.execute(cust_orders).fetchall()