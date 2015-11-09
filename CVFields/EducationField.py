__author__ = 'haojiang'

from CVFields.Field import Field

class EducationField(Field):

    def __init__(self,university,degree,major):
        self.university = university
        self.degree = degree
        self.major = major