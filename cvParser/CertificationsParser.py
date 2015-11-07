import FieldFactory
__author__ = 'haojiang'

class Certifications:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseCertifications(self,text):
        monthlist = ["January","February","March","April","May","June","July","August"
                     ,"September","October","November","December"]
        textList = text.splitlines()
        result = []
        for i in range(0,len(textList),2):
            # print textList[i+1].split()
            title = textList[i]
            company = ""
            license = ""
            date = ""
            nextline = textList[i+1].split()
            if len(nextline) > 2:
                companyIndex = len(nextline)
                licenseIndex = len(nextline)
                for k in range(0,len(nextline)):
                    if nextline[k] == "License":
                        companyIndex = k - 1
                    if nextline[k] in monthlist:
                        licenseIndex = k - 1
                    if k < companyIndex:
                        company = company + " " + nextline[k]
                    elif k > licenseIndex:
                        date = date + " " + nextline[k]
                    else:
                        license = license + " " + nextline[k]

            result.append(self.factory.produce("certifications",title.strip(),company.strip(),license.strip(),date.strip()))
        return result