import openpyxl
import pymysql
import numpy as np
import pandas as pd
from .models import UndergraduateInfo, UndergraduateOtherInfo

import matplotlib.pyplot as plt
import numpy as np

def save_undergraduateinfo():
    filepath = r'C:\Users\60557\Desktop\2017级本科生信息.xlsx'
    # data = pd.read_excel(filepath, sheet_name='sheet1')
    excel = openpyxl.load_workbook(filepath)
    sheet = excel['sheet1']
    data = sheet['A1': 'O2']
    for a in data:
        print()
        for b in a:
            print(b.value, end=' ')
    # print(data.value)
    student = UndergraduateInfo()
    data = student.objects.all()
    for i in data:
        print(i)


def A():
    students = UndergraduateOtherInfo()

    students_c_chinese = np.mean(list(students.objects.filter(registeredResidence='0').values('gkChinese')))
    print(students_c_chinese)

if __name__ == '__main__':
    # save_undergraduateinfo()
    A()