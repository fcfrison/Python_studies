from sqlalchemy import Table, MetaData
from db import OracleDAO

class Tables:
    '''
    Class created to store the database tables configurations. 
    '''
    def __init__(self, db_conn):
        self.metadata = db_conn # the metadata is a property
        self.users:Table = self.metadata.tables['users'] # 'users' is a reference to a Table object.
        self.cookies:Table = self.metadata.tables['cookies']
        self.orders:Table = self.metadata.tables['orders']
        self.line_items:Table = self.metadata.tables['line_items']
    
    @property
    def metadata(self):
        return self._metadata
    @metadata.setter
    def metadata(self, db_conn:OracleDAO):
        metadata = MetaData()
        metadata.reflect(bind=db_conn.engine)
        self._metadata = metadata
