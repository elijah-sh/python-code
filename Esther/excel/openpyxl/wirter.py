#读取带有标题的Excel


import xlrd

def read_input_ex():
    workbook = xlrd.open_workbook('141.xls')  # (1)取得excel book对象
    sheet = workbook.sheet_by_name("许昌-列车离鄂")  # (2)取得sheet对象
    rows = sheet.nrows  # (3)获得总行数
    title = sheet.row_values(0)
    for r in range(1, rows):
        edata = []
        row = sheet.row_values(r)  # (4)获取行数据
        i = -1
        for t in title:
            i = i + 1
            edata.append(t)
            edata.append(row[i])
        print(edata)

if __name__ == '__main__':
    read_input_ex()
