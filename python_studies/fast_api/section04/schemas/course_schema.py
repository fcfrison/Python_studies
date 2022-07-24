'''
For each model created, it will be necessary a file with the related schema.
The 'schema' is almost a mirror from the relative 'model'. While the 'schema'
is related to Pydantic, the 'model' is its equivalent, but related to SQLAlchemy. 
In other words, the file 'course_model.py' is concerned with the database configuration, 
while the file 'course_schema.py' is concerned with the information that is received and
sent by the API.
'''

from typing import Union
from pydantic import BaseModel as SCBaseModel

class CourseSchema(SCBaseModel):
    id_ : Union[int,None] # is the same as Optional[int]
    title: str
    lectures : int
    total_hours : int

    class Config:
        '''
        This class is used to provide configurations to Pydantic. Pydantic's 
        orm_mode will tell the Pydantic model to read the data even if it 
        is not a dict, but an ORM model.
        '''
        orm_mode = True
