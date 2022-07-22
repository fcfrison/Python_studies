'''
For each model created, it will be necessary a file with the related schema.
The 'schema' is almost a mirror from the relative 'model'. While the 'schema'
is related to Pydantic, the 'model' is its equivalent, but related to SQLAlchemy. 

'''

from typing import Union
from pydantic import BaseModel as SCBaseModel

class CourseSchema(SCBaseModel):
    id : Union[int,None] # is the same that Optional[int]
    title: str
    lectures : int
    total_hours : int

    class Config:
        '''
        Class is used to provide configurations to Pydantic. Pydantic's 
        orm_mode will tell the Pydantic model to read the data even if it 
        is not a dict, but an ORM model.
        '''
        orm_model = True
