import unittest
from tkinter.filedialog import askopenfilename
import main
from main import regsearch


class MyTestCase(unittest.TestCase):
    def test_col10(self):
        column10 = r'(?P<col10>\d{4})'
        g10 = 'col10'
        filename = askopenfilename()
        x = main.values(filename,9)
        y = main.regsearch(filename,column10,0,g10)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("Publisher year: znaleziono ", tmp, " dopasowań\n")

    def test_col9(self):
        column9 = r'(?P<col9>\w*(\s\w*)?|W*|Cz\S\w+)\s\:'
        g9 = 'col9'
        filename = askopenfilename()
        x = main.values(filename,8)
        y = main.regsearch(filename,column9,0,g9)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("Publisher location: znaleziono ", tmp, " dopasowań\n")
    def test_col8(self):
        column8 = r'(\w+\s\:\s)(?P<col8>(\w+\s)*\w*),'
        g8 = 'col8'
        filename = askopenfilename()
        x = main.values(filename,7)
        y = main.regsearch(filename,column8,0,g8)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("Publisher name: znaleziono ", tmp, " dopasowań\n")
    def test_col6(self):
        filename = askopenfilename()
        column6 = r'((s.\s)|S.\s)(?P<col6>\d+\-\d+)'
        g6 = 'col6'
        x = main.values(filename,5)
        y = main.regsearch(filename,column6,1,g6)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("Pages in range: znaleziono ", tmp, " dopasowań\n")
    def test_col5(self):
        filename = askopenfilename()
        column5 = r'((nr\sart.\s))(?P<col5>\w\d+)'
        g5 = 'col5'
        x = main.values(filename,4)
        y = main.regsearch(filename,column5,1,g5)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("Article no: znaleziono ", tmp, " dopasowań\n")
    def test_col4(self):
        filename = askopenfilename()
        column4 = r'((vol.\s)|(t.\s)|Vol.\s)(?P<col4>\d+)'
        g4 = 'col4'
        x = main.values(filename,3)
        y = main.regsearch(filename,column4,1,g4)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i],y[i])
                tmp += 1
            except:
                 tmp -= 1
        print("Vol: znaleziono ",tmp," dopasowań\n")
    def test_col3(self):
        filename = askopenfilename()
        column3 = r'((iss.\s)|(nr\s)|(No.)|(num.)|(no.))\s?,?(no.)?(?P<col3>\d+)'
        g3 = 'col3'
        x = main.values(filename,2)
        y = main.regsearch(filename,column3,1,g3)
        tmp = 0
        for i in range(len(y)):
            try:
                self.assertEqual(*x[i], y[i])
                tmp += 1
            except:
                tmp -= 1
        print("No: znaleziono ", tmp, " dopasowań\n")
if __name__ == '__main__':
    unittest.main()

