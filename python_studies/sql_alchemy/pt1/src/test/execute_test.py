'''
This module purpose is to facilitate the execution of the module test_app.py.
'''

import os

# when executing the test from the root of the project, then utilize this  
# approach.
os.system(r"cd src\test & python -m unittest test_app")

# when executing the test from directory where is located the test_app.py module, 
# then utilize this approach.
#os.system(r"cd.. & cd.. & cd lib\alchemy_venv\Scripts & activate &" +
#        r" cd.. & cd.. & cd.. & cd src\test & python -m unittest test_app")