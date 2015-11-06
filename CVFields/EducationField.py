__author__ = 'haojiang'

from Field import Field

class EducationField(Field):

    def __init__(self,university,degree,major):
        self.university = university
        self.degree = degree
        self.major = major