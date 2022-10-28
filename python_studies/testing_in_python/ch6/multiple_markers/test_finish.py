import pytest
from cards import Card
@pytest.mark.smoke #marking the entire class with the 'smoke' marker
class TestFinish:
    def test_finish_from_todo(self, cards_db):
        i = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"
    def test_finish_from_in_prog(self, cards_db):
        i = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"
