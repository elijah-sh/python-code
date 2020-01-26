import xlrd


def read_input():
    workbook = xlrd.open_workbook('25.xls')  # (1)取得excel book对象
    s12 = workbook.sheet_by_name("Sheet1")  # (2)取得sheet对象
    rows = s12.nrows  # (3)获得总行数
    for r in range(0, rows):
        row = s12.row_values(r)  # (4)获取行数据
        print(row)


def read_input_ex():
    workbook = xlrd.open_workbook('25.xls')  # (1)取得excel book对象
    sheet = workbook.sheet_by_name("Sheet1")  # (2)取得sheet对象
    rows = sheet.nrows  # (3)获得总行数
    title = sheet.row_values(0)
    for r in range(1, rows):
        row = sheet.row_values(r)  # (4)获取行数据
        i = -1
        value = ''
        for t in title:
            i = i + 1
            value = value   + "  " +  t   + "：" +  str(row[i])
        print(value)


if __name__ == '__main__':
    read_input_ex()
