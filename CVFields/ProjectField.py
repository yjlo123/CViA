__author__ = 'haojiang'


from CVFields.Field import Field

class ProjectField(Field):

    def __init__(self,title,date,des):
        self.title = title
        self.date = date
        self.description = des
