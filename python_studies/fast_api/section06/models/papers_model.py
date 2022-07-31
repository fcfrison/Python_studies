from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings_

class PaperModel(settings_.DBBaseModel):
    __tablename__='papers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256))
    description = Column(String(256))
    url = Column(String(256))
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('UserModel',back_populates='papers',lazy='joined')
    