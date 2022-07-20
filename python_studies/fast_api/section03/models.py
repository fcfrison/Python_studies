'''
Creating basic models.
'''

from typing import Optional # Optional is used when a default value is defined

from pydantic import BaseModel

class Curso(BaseModel):
    id:Optional[int]=None #'id' is a integer or none
    title:str
    lectures:int
    duration:int

