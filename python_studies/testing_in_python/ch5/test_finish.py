'''
The code below presents a situation where the 'finish' method is tested without
any kind of parametrization.
'''
from cards import Card

def test_finish_from_in_prog(cards_db): # it's used the 'cards_db' fixture
    index = cards_db.add_card(Card("second edition", state="in prog")) #index point to a integer
    cards_db.finish(index) #'finish' updates the state attribute to "done"
    card = cards_db.get_card(index)
    assert card.state == "done"
def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card("write a book", state="done"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card("create a course", state="todo"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

