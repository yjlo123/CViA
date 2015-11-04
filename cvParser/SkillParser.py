import FieldFactory
from CVFields import Skill_ExpertiseField
__author__ = 'haojiang'



class SkillParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseSkill(self,text):
        textList = text.splitlines()
        return Skill_ExpertiseField.Skill_ExpertiseField(textList).__dict__["skill"]
