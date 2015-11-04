
import doc_converter
import ExpParser
import LanguageParser
import SkillParser
__author__ = 'haojiang'


class Parser:

    def __init__(self):
        self.summary = ""
        self.experience = ""
        self.expParser = ExpParser.ExpParser()
        self.peublications = ""
        self.project = ""
        self.language = ""
        self.languageParser = LanguageParser.LanguageParser()
        self.skill = ""
        self.skillParser = SkillParser.SkillParser()
        self.education = ""
        self.i=0

    def IsKeyWord(self,word):
        return word == "summary" or word == "experience" or word == "publications" or \
               word == "projects" or word == "languages" or word == "education" or \
               word == "skills & expertise" or word == "volunteer experience" or \
               word == "certifications" or word == "interests"

    def ConstructStr(self,textList):
        result = ""
        word = textList[self.i+1]
        while(self.IsKeyWord(word) is False or self.i<len(textList) is False):
            self.i+=1
            if word[:4] !="page":
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
        textList = text.splitlines()
        lastPageIndex = len(textList)-1
        PageChecker = 2
        while(lastPageIndex>0):
            if textList[lastPageIndex][:4] == "page":
                PageChecker -=1 ;
            if PageChecker == 0:
                break
            lastPageIndex -=1;
        textList = textList[:lastPageIndex]
        while (self.i<len(textList)):
            word = textList[self.i]
            if self.IsKeyWord(word):
                if word == 'summary':
                    self.summary = self.ConstructStr(textList)
                elif word == 'experience':
                    Expstr = self.ConstructStr(textList)
                    self.experience = self.expParser.ParseExp(Expstr)
                    print self.experience
                elif word == 'publications':
                    self.publications = self.ConstructStr(textList)
                elif word == 'projects':
                    self.project = self.ConstructStr(textList)
                elif word == 'languages':
                    Languagestr = self.ConstructStr(textList)
                    self.language = self.languageParser.ParseLanguage(Languagestr)
                elif word == 'skills & expertise':
                    Skillstr = self.ConstructStr(textList)
                    self.skill = self.skillParser.ParseSkill(Skillstr)
                elif word == 'education':
                    self.education = self.ConstructStr(textList)
            self.i = self.i + 1

    def convertToObj(self,text):
        text = text.lower()
        self.AnalyseText(text)
        res = self.__dict__
        del res["i"]
        del res["expParser"]
        del res["skillParser"]
        del res["languageParser"]
        return res

if __name__ == "__main__":

    converter = doc_converter.DocConverter()
    CV_Text = converter.documentToText("/Users/haojiang/Desktop/CViA/cv/DonnabelleEmbodo.pdf")
    P = Parser()
    P.AnalyseText(CV_Text.lower())

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
