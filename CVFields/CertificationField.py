from CVFields.Field import Field

__author__ = 'haojiang'

class CertificationField(Field):

    def __init__(self,title, issuedcompany, license, date):
        self.title = title
        self.company = issuedcompany
        self.license = license
        self.date = date
