from doc_converter import DocConcerter

__author__ = 'haojiang'


class Parser:
    def __init__(self):
        self.Summary = ""
        self.Experience = ""
        self.Publications = ""
        self.Project = ""
        self.Language = ""
        self.Skill = ""
        self.Education = ""
        self.i=0
    def IsKeyWord(self,word):
        return word == "Summary" or word == "Experience" or word == "Publications" or \
               word == "Projects" or word == "Languages" or word == "Education" or \
               word == "Skills & Expertise"

    def ConstructStr(self,textList):
        result = ""
        word = textList[self.i+1]
        while(self.IsKeyWord(word) is False or self.i<len(textList) is False):
            self.i=self.i+1
            if word != "" and word[:4] !="Page":
                if result is "":
                    result = result+word
                else:
                    result = result+"\n"+word
            word = textList[self.i+1]
        return result

    # When it is the final filed(Education), terminate it when the page ends
    def ConstructFinalStr(self,textList):
        result = ""
        word = textList[self.i+1]
        while(self.IsKeyWord(word) is False or self.i<len(textList) is False):
            self.i=self.i+1
            if word != "":
                if result is "":
                    result = result+word
                else:
                    result = result+"\n"+word
            word = textList[self.i+1]
            if( word[:4] =="Page"):
                break;
        return result

    def AnylyseText(self,text):
        textList = text.splitlines()
        while (self.i<len(textList)):
            word = textList[self.i]
            if self.IsKeyWord(word):
                if word == 'Summary':
                    self.Summary = self.ConstructStr(textList)
                elif word == 'Experience':
                    self.Experience = self.ConstructStr(textList)
                elif word == 'Publications':
                    self.Publications = self.ConstructStr(textList)
                elif word == 'Projects':
                    self.Project = self.ConstructStr(textList)
                elif word == 'Languages':
                    self.Language = self.ConstructStr(textList)
                elif word == 'Skills & Expertise':
                    self.Skill = self.ConstructStr(textList)
                elif word == 'Education':
                    self.Education = self.ConstructFinalStr(textList)
            self.i = self.i + 1

if __name__ == "__main__":
    converter = DocConverter()
    CV_Text = converter.documentToText("/Users/haojiang/Desktop/CViA/cv/DesmondLim.pdf")
    P = Parser()
    P.AnylyseText(CV_Text)
    result = P.__dict__
    del result["i"]
    print result
