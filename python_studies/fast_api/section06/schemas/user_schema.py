from typing import List, Optional, Union
from pydantic import BaseModel as SCBaseModel, EmailStr

from .papers_schema import PaperSchema

class UserSchemaBase(SCBaseModel):
    '''
    Base class to deal with the user's data.
    '''
    id: Union[int,None]
    name: str
    last_name: str
    email:EmailStr
    is_admin:bool = False

    class Config:
        '''
        This class is used to provide configurations to Pydantic. Pydantic's 
        orm_mode will tell the Pydantic model to read the data even if it 
        is not a dict, but an ORM model.
        '''
        orm_mode = True

class UserSchemaCreate(UserSchemaBase):
    '''
    This class is used in the creation of an user.
    '''
    password: str

class UserSchemaPapers(UserSchemaBase):
    papers:Optional[List[PaperSchema]]

class UserSchemaUpdate(UserSchemaBase):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_admin: Optional[bool]
