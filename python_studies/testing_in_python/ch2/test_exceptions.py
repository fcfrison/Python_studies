'''
Sometimes, we expect that a exception will be raised if an specific circumstance
happens.
'''
import pytest
import cards
def test_no_path_raises():
    with pytest.raises(TypeError): # we expect that a TypeError exception will be raised.
        cards.CardsDB()
def test_raises_with_info():
    match_regex = "missing 1 .* positional argument" # it's possible to check if the 
                                                    # message of the raised exception is  
                                                    # correct
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()
def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
        expected = "missing 1 required positional argument"
    assert expected in str(exc_info.value)
