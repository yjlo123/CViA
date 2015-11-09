__author__ = 'haojiang'

from CVFields.Field import Field

class ExperienceField(Field):

    def __init__(self,title,period,description,company):
        self.title = title
        self.period = period
        self.description = description
        self.company = company