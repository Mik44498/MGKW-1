import csv
import re
from tkinter.filedialog import askopenfilename

def regsearch(fname,regexpression,rownumber,grname):
    matcharray = []
    with open(fname, 'r', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            column1=re.search(regexpression,row[rownumber])
            if column1:
                x = column1.group(grname)
                matcharray.append(x)
            else:
                matcharray.append("")
    return matcharray

def values(fname,colnumber):
    with open(fname, 'r', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        column = [colnumber]
        contentlist = []
        for row in rows:
            content = list(row[i] for i in column)
            contentlist.append(content)
    return contentlist


if __name__ == "__main__":
    filename = askopenfilename()
    column10 = r'(?P<col10>\d{4})'
    g10 = 'col10'
    column9 = r'(?P<col9>\w*(\s\w*)?|W*|Cz\S\w+)\s\:'
    g9 = 'col9'
    column8 = r'(\w+\s\:\s)(?P<col8>(\w+\s)*\w*),'
    g8 = 'col8'
    column6 = r'((s.\s)|S.\s)(?P<col6>\d+\-\d+)'
    g6 = 'col6'
    column5 = r'((nr\sart.\s))(?P<col5>\w\d+)'
    g5 = 'col5'
    column4 = r'((vol.\s)|(t.\s)|Vol.\s)(?P<col4>\d+)'
    g4 = 'col4'
    column3 = r'((iss.\s)|(nr\s)|(No.)|(num.)|(no.))\s?,?(no.)?(?P<col3>\d+)'
    g3 = 'col3'
    c10 = regsearch(filename,column10,0,g10)
    c9 = regsearch(filename,column9,0,g9)
    c8 = regsearch(filename,column8,0,g8)
    c6 = regsearch(filename,column6,1,g6)
    c5 = regsearch(filename,column5,1,g5)
    c4 = regsearch(filename,column4,1,g4)
    c3 = regsearch(filename,column3,1,g3)



    # (?P<Year2>(\d{4}))?((,.)|(\s))?(?P<col4pom>((vol.\s)?|(S.)?))?\s?(?P<col4>\d{1,3})?(?P<col3pom>(nr\s)?|(t.\s)?|(No.\s)?)?(?P<col3>\d)?(,?\s?|\s)?\w+?\S?\s?(?P<col6>(\d{1,4}\-\d{1,4}))?(art. )?(?P<col5>\w\d{5})?
    # (?P<Year2>(\d{4}))?((,.)|(\s))?(?P<col4pom>((vol.\s)?|(S.)?))?\s?(?P<col4>\d)?(?P<col3pom>(nr\s)?|(t.\s)?|(No.\s)?)?(?P<col3>\d\d+)?(,?\s?|\s)?\w+?\S?\s?(?P<col6>(\d{1,4}\-\d{1,4}))?(art. )?(?P<col5>\w\d{5})?
    # (?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})(,)?\s?