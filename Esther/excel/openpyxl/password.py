import xlrd
import pandas as pd
import xlwings as xw

PATH = '23.xlsx'
wb = xw.Book(PATH)
sheet = wb.sheets['sample']

df = sheet['A1:C4'].options(pd.DataFrame, index=False, header=True).value
df