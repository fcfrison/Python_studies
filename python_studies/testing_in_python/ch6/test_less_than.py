'''
The code below presents a situation where we mark a test with the purpose of
skip it (mainly because the feature it tests still has not been developed).
'''
from cards import Card
import pytest
@pytest.mark.skip(reason="Card doesn't support < comparison yet")
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2
def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
