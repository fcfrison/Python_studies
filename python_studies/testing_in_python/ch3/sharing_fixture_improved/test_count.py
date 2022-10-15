'''
Testing the function 'count'. 
In the scenario presented by the code below, the fixture is external to 
the test functions file.
'''

import cards

def test_empty(cards_db):
    assert cards_db.count() == 0
def test_two(cards_db):# The same fixture can be used many times.
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2