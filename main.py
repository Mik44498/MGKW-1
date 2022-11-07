import csv
import re

with open('details.csv', 'r', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        asd=re.search(r'(?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})(,)?\s?',row[0])
        asd2=re.search(r'(?P<Year2>(\d{4}))?((,.)|(\s))(?P<col4pom>((vol.\s)|(S.)))?(?P<col4>\d)?(?P<col3pom>(nr\s)|(t.\s)|(No.\s))?(?P<col3>\d\d+)?(,\s?|\s)?(?P<col6>\d{3}\-\d{3})?',row[1])
        if asd:
            print("|Dane z kolumny 9:",asd.group('col9'),"|Dane z kolumny 8:",asd.group('col8'),"|Dane z kolumny 10:",asd.group('col10'))
        if asd2:
            print("|Dane z kolumny 4:", asd2.group('col4'),"|Dane z kolumny 3:", asd2.group('col3'),"|Dane z kolumny 6:", asd2.group('col6'))

# (?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})\,?\s?(?P<Year2>(\d{4}))?((,.)|(\s))(?P<col4pom>((vol.\s)|(S.)))?(?P<col4>\d)?(?P<col3pom>(nr\s)|(t.\s)|(No.\s))?(?P<col3>\d\d+)?(,\s?|\s)?(?P<col7>)