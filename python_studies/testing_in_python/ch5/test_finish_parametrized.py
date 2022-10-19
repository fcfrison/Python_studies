'''
Instead of writing multiple test functions to provide different inputs for the
test, a better approach is to parametrize the test function. The code below 
presents this approach. Here, we are testing the same as 'test_finish.py', but
with just one test function, and not 3.
'''
import pytest
from cards import Card
@pytest.mark.parametrize(
    ["start_summary", "start_state"], # here is the of the test function parameters
    [
    ("write a book", "done"), # 'start_summary' points to the first element of the tuple, and 'start_state' to the second
    ("second edition", "in prog"),
    ("create a course", "todo"),
    ],
)
def test_finish(cards_db, start_summary, start_state): # cards_db is a fixture
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
