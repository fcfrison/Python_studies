# Sql Alchemy small development

## 📜 Description
This is a small project whose purpose is to understand the SqlAlchemy Core
(from the Python library SqlAlchemy) dinamics and its functionalities. My goal here  is to develop some ideas related to how to structure files and directories in a proper way, as well as set the needed configurations to interact with an Oracle database. 

Usually, instead of creating the tables via SqlAlchemy, we work with a db 
whose schema is already setted for us. Therefore, instead of manually create
the table objects, it's better to just reflect them from the database. This 
process is called 'reflection' and was it developed in ``reflecting_db.py``. 

## 📈 File structure and descriprion

* `/src/db`
    * Package that contains the necessary classes and modules to interact with
    an Oracle database;
* `/src/models`
    * Package destined for the database schema modeling;
* `/src/reflecting_db.py`
    * Code that connect and interact with the database;
