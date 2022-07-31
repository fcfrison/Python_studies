from typing import Union
from pydantic import BaseModel as SCBaseModel, HttpUrl

class PaperSchema(SCBaseModel):
    id: Union[int,None] = None
    title: str
    description:str
    url: HttpUrl
    user_id: int


    class Config:
        '''
        This class is used to provide configurations to Pydantic. Pydantic's 
        orm_mode will tell the Pydantic model to read the data even if it 
        is not a dict, but an ORM model.
        '''
        orm_mode = True