from typing import List
from sqlalchemy.orm import sessionmaker
from models import *
def insert_data(session:sessionmaker,data:List[Cookie|User|Order|LineItem]):
    '''
    Function that inserts data in the database. 

    Parameters
    ----------------
        session\n
            A session related to SqlAlchemy that allows interact with the db.
        data\n
            A list of objects of the class declarative_base, from SqlAlchemy.
    
    
    '''
    session.bulk_save_objects(data)
    session.commit()
