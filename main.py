import csv
import re
from tkinter.filedialog import askopenfilename

def regsearch(fname,regexpression,rownumber):
    matcharray = []
    with open(fname, 'r', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            column1=re.search(regexpression,row[rownumber])
            if column1:
                x = column1.group('col8')
                matcharray.append(x)
    print(matcharray)


if __name__ == "__main__":
    filename = askopenfilename()
    column10 = r'(?P<col10>\d{4})'
    column9 = r'(?P<col9>\w*)\s\S\s'
    column8 = r'(\w{1,10}\s\:\s)(?P<col8>(\w+\s)*\w*,)'
    column6 = r'((s.\s)|S.\s)(?P<col5>\d+\-\d+)'
    column5 = r'((nr\sart.\s))(?P<col5>\w\d+)'
    column4 = r'((vol.\s)|(t.\s))(?P<col4>\d+)'
    column3 = r'((iss.\s)|(nr\s)|(No.)|(num.)|(no.))(?P<col3>\d+)'
    c10 = regsearch(filename,column10,0)
    c9 = regsearch(filename,column10,0)
    c8 = regsearch(filename,column10,0)
    c6= regsearch(filename,column10,1)
    c5 = regsearch(filename,column10,1)
    c4 = regsearch(filename,column10,1)
    c3 = regsearch(filename,column10,1)












    # (?P<Year2>(\d{4}))?((,.)|(\s))?(?P<col4pom>((vol.\s)?|(S.)?))?\s?(?P<col4>\d{1,3})?(?P<col3pom>(nr\s)?|(t.\s)?|(No.\s)?)?(?P<col3>\d)?(,?\s?|\s)?\w+?\S?\s?(?P<col6>(\d{1,4}\-\d{1,4}))?(art. )?(?P<col5>\w\d{5})?
    # (?P<Year2>(\d{4}))?((,.)|(\s))?(?P<col4pom>((vol.\s)?|(S.)?))?\s?(?P<col4>\d)?(?P<col3pom>(nr\s)?|(t.\s)?|(No.\s)?)?(?P<col3>\d\d+)?(,?\s?|\s)?\w+?\S?\s?(?P<col6>(\d{1,4}\-\d{1,4}))?(art. )?(?P<col5>\w\d{5})?
    # (?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})(,)?\s?