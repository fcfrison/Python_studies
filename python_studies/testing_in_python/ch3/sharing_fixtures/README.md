## Description
Instead of keeping the fixture code in the same file that the test functions, it's 
possible to create it's own file. In `conftest.py`, the scope of the fixture is 
setted as "session" and it's used by the tests in the `test_count.py` file.