"""
The code below shows how to mark tests that are expected to fail. 
"""
import pytest
from cards import Card,__version__
from packaging import version
@pytest.mark.xfail( # This test will run and is expected to fail.
    version.parse(__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
    )
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2
@pytest.mark.xfail(reason="XPASS demo") # this test is expected to fail, and if it passes, 
def test_xpass():                       # pytest will mark it as XPASSED, condidering the 
    c1 = Card("a task")                 # the parameter 'strict' is setted to 'False'
    c2 = Card("a task")
    assert c1 == c2
@pytest.mark.xfail(reason="strict demo", strict=True) # If this test passes, pytest will return the
def test_xfail_strict():                              # message of FAIL, cause the parameter 'strict'
    c1 = Card("a task")                               # is setted to 'True'
    c2 = Card("a task")
    assert c1 == c2
