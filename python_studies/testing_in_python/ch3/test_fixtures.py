'''
Here, we have the simplest development of a fixture. What is a fixture, after all?
"Fixtures are functions that are run by pytest before (and sometimes after) the 
actual test functions. The code in the fixture can do whatever you want it to. 
You can use fixtures to get a data set for the tests to work on. You can use 
fixtures to get a system into a known state before running a test. Fixtures are 
also used to get data ready for multiple tests."

'''
import pytest
@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42
def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42

