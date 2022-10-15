'''
Testing the function 'count'. 
It's possible to use a fixture to initialize a db connection and then close it. 
In the script below, it's used the default scope for the fixture: the function
scope. It means that everytime we call the fixture within a test function, 
a new instance of the 'db' is created. 
Here, the fixture is initialized once (and not one time for every test function). 

'''
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards

@pytest.fixture(scope='module')
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # create a Path object
        db = cards.CardsDB(db_path) # create a CardsDb instance
        yield db # returns the db instance
        db.close()
def test_empty(cards_db):
    assert cards_db.count() == 0
def test_two(cards_db):# The same fixture can be used many times.
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2