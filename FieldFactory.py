__author__ = 'haojiang'

from CVFields import EducationField
from CVFields import ExperienceField
from CVFields import LanguageField
from CVFields import Skill_ExpertiseField
from CVFields import VolunteerField
from CVFields import InterestsField
from CVFields import CertificationField
from CVFields import ProjectField
from CVFields import PublicationField

class FieldFacory:
    def __init__(self):
        pass

    def produceEdu(self,university,degree,major):
       return EducationField.EducationField(university,degree,major).__dict__

    def produceExp(self,title,period,description,company):
        return ExperienceField.ExperienceField(title,period,description,company).__dict__

    def produceLanguage(self,textList):
        return LanguageField.LanguageField(textList).__dict__["language"]

    def produceSkill(self,textList):
        return Skill_ExpertiseField.Skill_ExpertiseField(textList).__dict__["skill"]

    def produceVolunteerExp(self,title,period,description):
        return VolunteerField.VolunteerExpField(title,period,description).__dict__

    def produceInterest(self,textList):
        return InterestsField.InterestsField(textList).__dict__["interest"]

    def produceCertifications(self,title,company,license,date):
        return CertificationField.CertificationField(title,company,license,date).__dict__

    def produceProjects(self,title,date,description):
        return ProjectField.ProjectField(title,date,description).__dict__

    def produce(self,*args):
        fieldName = args[0]
        if fieldName == "exp":
            title = args[1]
            period = args[2]
            description = args[3]
            company = args[4]
            return self.produceExp(title,period,description,company)
        elif fieldName == "edu":
            university = args[1]
            degree = args[2]
            major = args[3]
            return self.produceEdu(university,degree,major)
        elif fieldName == "projects":
            title = args[1]
            date = args[2]
            description = args[3]
            return self.produceProjects(title,date,description)
        elif fieldName == "language":
            return self.produceLanguage(args[1])
        elif fieldName == "skill":
            return self.produceSkill(args[1])
        elif fieldName == "volunteerexp":
            title = args[1]
            period = args[2]
            description = args[3]
            return self.produceVolunteerExp(title,period,description)
        elif fieldName == "interest":
            return self.produceInterest(args[1])
        elif fieldName == "certifications":
            title = args[1]
            company = args[2]
            license = args[3]
            date = args[4]
            return self.produceCertifications(title,company,license,date)
