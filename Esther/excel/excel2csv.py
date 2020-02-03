import xlrd
import csv

def read_input_ex():
    workbook = xlrd.open_workbook('D:/tmp/data/141.xls')  # (1)取得excel book对象
    sheet = workbook.sheet_by_name("许昌-列车离鄂")  # (2)取得sheet对象
    rows = sheet.nrows  # (3)获得总行数
    title = sheet.row_values(0)
    data = []
    for r in range(1, rows):
        edata = []
        row = sheet.row_values(r)  # (4)获取行数据
        i = -1
        for t in title:
            i = i + 1
            edata.append(t)
            edata.append(row[i])
        print(edata)
        data.append(row)
    return  data

def writer_csv():

    data = read_input_ex();
    with open('D:/tmp/data/data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        spamwriter = csv.writer(csvfile)
        for d in data:
            spamwriter.writerow(d)

if __name__ == '__main__':
    writer_csv()