'''
Instead of keeping the fixture code in the same file that the test file, it's 
possible to create it's own file. Note that the scope of the fixture is setted as 
"session".
'''

from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest
@pytest.fixture(scope="session")
def cards_db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()
