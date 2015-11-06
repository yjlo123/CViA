__author__ = 'haojiang'

from Field import Field

class VolunteerExpField(Field):

    def __init__(self,title,period,description):
        self.title = title
        self.period = period
        self.description = description