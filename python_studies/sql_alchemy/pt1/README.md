# Sql Alchemy small development

📜 Description
This is a small project whose purpose is to understand the SqlAlchemy Core
(from the Python library SqlAlchemy) and its functionalities. My goal here 
is to develop some ideas related to how to structure files and directories
in a proper way, as well as set the needed configurations to interact with an 
Oracle database. 
As a result, i was able to insert into and select data from an Oracle database
using SqlAlchemy. It was also developed a module of testing.

## 📈 File structure and descriprion

* `/documentation`
    * Contains the database schema;
* `/logs`
    * Directory for log files;
* `/src/infra/db`
    * Package that contains the necessary classes and modules to interact with
    an Oracle database;
* `/src/models`
    * Package destined for the database schema modeling;
* `/src/sql_funcs`
    * Package with some functions for querying against a database;
* `/src/test`
    * Package related to testing;
* `/src/basic_development_sqlalchemy.py`
    * Script that connect and interact with the database;
* `/src/improved_dev_sqlalchemy.py`
    * Script that also connect and interact with the database. The difference between
    this file and the one before is the classes used to establish the interaction 
    with the database. 


