import FieldFactory
__author__ = 'haojiang'

class ProjectsParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseProjects(self,text):
        textList = text.splitlines()
        keyIndex = []
        result = []
        for i in range(0,len(textList)):
            if "Members:" in textList[i]:
                keyIndex.append(i)

        for i in range(0,len(keyIndex)):
            theIndex = keyIndex[i]

            # Is not the last one
            if i != len(keyIndex) - 1:
                title = textList[theIndex-2]
                date = textList[theIndex-1]
                description = ""
                start = theIndex + 1
                end = keyIndex[i+1]
                for k in range(start,end):
                    description = description + textList[k]
            # Is the last one
            else:
                title = textList[theIndex-2]
                date = textList[theIndex-1]
                description = ""
                if theIndex + 1 < len(textList):
                    start = theIndex + 1
                    end = len(textList) - 1
                    for k in range(start,end):
                        description = description + textList[k]

            result.append(self.factory.produce("projects",title.strip(),date.strip(),description.strip()))

        return result