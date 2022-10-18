'''
It's possible to use the builtin fixtures to feed customized fixtures. In the code
below, follows a situation where a customized fixture that generates an instance 
of a database uses a builtin fixture to provide a temporary directory.
'''
import pytest
import cards
@pytest.fixture(scope="session")
def db(tmp_path_factory):
    """CardsDB object connected to a temporary database"""
    db_path = tmp_path_factory.mktemp("cards_db")
    db_ = cards.CardsDB(db_path)
    yield db_
    db_.close()