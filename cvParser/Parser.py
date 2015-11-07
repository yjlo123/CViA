import unicodedata
import doc_converter
import ExpParser
import LanguageParser
import SkillParser
import EduParser
import VolunteerExpParser
import InterestsParser
import PublicationsParser
import ProjectsParser
import CertificationsParser
import re
import unicodedata
__author__ = 'haojiang'


class Parser:

    def __init__(self):
        self.summary = ""
        self.experience = ""
        self.expParser = ExpParser.ExpParser()
        self.publications = ""
        self.publicationsParser = PublicationsParser.PublicationsParser()
        self.project = ""
        self.projectParser = ProjectsParser.ProjectsParser()
        self.language = ""
        self.languageParser = LanguageParser.LanguageParser()
        self.skill = ""
        self.skillParser = SkillParser.SkillParser()
        self.education = ""
        self.eduParser = EduParser.EduParser()
        self.volunteerexperience=""
        self.volunteerexperienceParser = VolunteerExpParser.VolunteerExpParser()
        self.interest = ""
        self.interestParser = InterestsParser.InterestParser()
        self.certifications = ""
        self.certificationsParser = CertificationsParser.Certifications()
        self.i=0
        self.keywords = ["Summary","Experience","Publications",
                         "Projects","Languages","Education",
                         "Skills & Expertise","Volunteer Experience","Certifications",
                         "Interests","\x0cInterests"]

    def IsKeyWord(self,word):
        return word in self.keywords

    def ConstructStr(self,textList):
        result = ""
        word = textList[self.i+1]
        while(self.IsKeyWord(word) is False or self.i<len(textList) is False):
            self.i+=1
            if word[:4] !="Page":
                if result is "":
                    result = result+word
                else:
                    result = result+"\n"+word
            if self.i==len(textList)-1:
                break
            else:
                word = textList[self.i+1]
        return result



    def AnalyseText(self,text):
        if isinstance(text, unicode):
            text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
        textList = text.splitlines()

        for i in range(len(textList)-1,0,-1):
            list = textList[i].split()
            if len(list) > 3:
                if list[0] == "Contact" and list[len(list)-1] == "LinkedIn":
                    textList = textList[:i-5]
                    break

        for i in range(0,len(textList)):
            textList[i] = textList[i].strip() # Trim
        textList = filter(None,textList)  # Remove ['']

        while (self.i<len(textList)):
            word = textList[self.i]
            #print word
            if self.IsKeyWord(word):
                if word == 'summary':
                    self.summary = self.ConstructStr(textList)
                elif word == 'Experience':
                    Expstr = self.ConstructStr(textList)
                    self.experience = self.expParser.ParseExp(Expstr)
                    #print self.experience
                elif word == 'Publications':
                    self.publications = self.ConstructStr(textList)
                elif word == 'Certifications':
                    Certificationsstr = self.ConstructStr(textList)
                    self.certifications = self.certificationsParser.ParseCertifications(Certificationsstr)
                    #print self.certifications
                elif word == 'Projects':
                    Projectstr = self.ConstructStr(textList)
                    self.project = self.projectParser.ParseProjects(Projectstr)
                    print self.project
                elif word == 'Languages':
                    Languagestr = self.ConstructStr(textList)
                    self.language = self.languageParser.ParseLanguage(Languagestr)
                    #print self.language
                elif word == 'Skills & Expertise':
                    Skillstr = self.ConstructStr(textList)
                    self.skill = self.skillParser.ParseSkill(Skillstr)
                    #print self.skill
                elif word == 'Education':
                    Edustr = self.ConstructStr(textList)
                    self.education = self.eduParser.ParseEdu(Edustr)
                    #print self.education
                elif word == 'Volunteer Experience':
                    VolunteerExpstr = self.ConstructStr(textList)
                    self.volunteerexperience = self.volunteerexperienceParser.ParseVolunteerExp(VolunteerExpstr)
                    #print self.volunteerexperience
                elif word == '\x0cInterests' or word == 'Interests':
                    Intereststr = self.ConstructStr(textList)
                    self.interest = self.interestParser.ParseInterest(Intereststr)
                    #print self.interest
            self.i = self.i + 1

    def convertToObj(self,text):
        self.AnalyseText(text)
        res = self.__dict__
        del res["i"]
        del res["expParser"]
        del res["skillParser"]
        del res["languageParser"]
        del res["eduParser"]
        del res["publicationsParser"]
        del res["projectParser"]
        del res["certificationsParser"]
        del res["interestParser"]
        del res["volunteerexperienceParser"]
        del res["keywords"]
        return res

if __name__ == "__main__":

    converter = doc_converter.DocConverter()
    CV_Text = converter.documentToText("/Users/haojiang/Desktop/CViA/cv/DonnabelleEmbodo.pdf")
    P = Parser()
    P.convertToObj(CV_Text)

    # result = P.__dict__
    # del result["i"]
    # print result["Experience"].splitlines()

    # f = FieldFactory.FieldFacory()
    # edu = f.produceEdu()
    # print edu.__dict__
    # print edu.GetScore()
    # print re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', "May 2010 ") !=[]
    # str = 'September 2015  -  Present (2 months)'
    # print str.split("(")[0].split("-")[1].split()
    # print str.split("(")[0].split("-")[0].split()
    # print str.split("(")[0].split("-")[1] == "  Present "
    # first = str.split("(")[0].split("-")[0]
    # second = str.split("(")[0].split("-")[1]
    # print first
    # print second
    # print re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}', first) !=[] and \
    #                (re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}', second) !=[] or second =="  Present ")
