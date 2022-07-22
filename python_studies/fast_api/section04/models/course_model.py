'''
This module defines the models used in the project developed in section04.
'''

from core.configs import settings_

from sqlalchemy import Column, Integer, String

class CourseModel(settings_.DBBaseModel):
    __tablename__ = 'courses'

    id : int = Column(Integer, primary_key=True,autoincrement=True)
    title : str = Column(String(100))
    lectures : str = Column(Integer)
    total_hours : int = Column(Integer)
