'''
Creating basic models.
'''

from typing import Optional # Optional is used when a default value is defined

from pydantic import BaseModel, validator

class Course(BaseModel):
    id:Optional[int]=None #'id' is a integer or none
    title:str
    lectures:int
    duration:int

    @validator('title') # validating the title
    def validate_title(cls,value:str):
        '''
        This function validates the attribute 'title'. It's related to the 
        situation where it's necessary to insert new data or update existing
        data.
        '''
        title_words = value.split()
        if len(title_words)<3:
            raise ValueError('The title must contains at least 3 words.')
        return value
