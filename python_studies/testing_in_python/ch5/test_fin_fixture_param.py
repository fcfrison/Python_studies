'''
In 'test_finish_parametrized.py', the different inputs were passed as parameters
of the test function. It's also possible to passed it as arguments of a fixture.
'''
import pytest
from cards import Card
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    '''
    Fixture that just returns one by one the elements of 'params'.
    '''
    return request.param
def test_finish(cards_db, start_state):
    '''
    The test_finish function has two fixtures as its parameters. 
    The parameter 'start_state' points to the elements of the list in 'params', 
    inside the start_state fixture.
    '''
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"