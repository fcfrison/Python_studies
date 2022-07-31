from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings_

class UserModel(settings_.DBBaseModel):
    '''
    Class that represents the 'users' table.
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    is_admin = Column(Boolean,default=False)
    papers = relationship(
        "PaperModel",
        cascade="all, delete-orphan",
        back_populates="creator",
        uselist=True,
        lazy="joined"
    )