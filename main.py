import csv
import re

with open('details.csv', 'r', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        asd=re.search(r'(?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})(,)?\s?(?P<Year2>(\d{4}))?',row[0])
        if asd:
            print(asd.group('col9'),asd.group('col8'),asd.group('col10'))


# (?P<col9>\w*)\s\S(?P<col8>(\s\w*)*)\S\s(?P<col10>\d{4})\,?\s?(?P<Year2>(\d{4}))?((,.)|(\s))(?P<col4pom>((vol.\s)|(S.)))?(?P<col4>\d)?(?P<col3pom>(nr\s)|(t.\s)|(No.\s))?(?P<col3>\d\d+)?(,\s?|\s)?(?P<col7>)