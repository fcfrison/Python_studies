import os

CONFIG_FILE_LOCATION = r'C:\location\to\the\config_file\config_sqlalchemy_.json'


def get_parent_directory(current_work_dir:str)->str:
    '''
    Function that generates the absolute path of a given current working directory.

    Parameters
    -------------------------
        current_work_dir\n
            The child directory whose parent is to be known
    
    Returns
    -------------------------
        abs_path_par_dir\n
            A string with the parent directory.
    '''
    par_dir = os.pardir
    abs_path_par_dir = os.path.abspath(os.path.join(current_work_dir,par_dir))
    return abs_path_par_dir

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
