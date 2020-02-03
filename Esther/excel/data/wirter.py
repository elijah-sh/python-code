import xlrd
import xlsxwriter
import pymysql
import csv

host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'news_data'
c = 'utf8'
port = 3306
TABLE_NAME = 'EXCEL_ROW_DATA'

WORK_BOOK_NAME = 'D:/tmp/data/武汉进出人员统计-税务组.xlsx'
SHEET_NAME = '武汉进出人员-报账'

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
        data.append(edata)
    return  data


def wirter():
    workbook = xlsxwriter.Workbook('D:/tmp/data/test4.xlsx') # 建立文件
    worksheet = workbook.add_worksheet() # 建立sheet
    # 行
    for row in range(0,10):
        # 列
        for col in range(0,10):
            if row == 0 or col == 0 or row > col:
                continue
            else:
                worksheet.write(row,col,' '  + str(row) + ' *  '  + str(col) +  ' = ' + str(row*col) )#向第二行第二例写入guoshun
    workbook.close()




def process_item():
    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
    # 数据库游标
    cue = con.cursor()
    try:

        # 查询数据
        query_sql = "select  EXCEL_ROW_DATA_ID, " \
                       " WORK_BOOK_NAME,  SHEET_NAME, FIRST_ROW_FLAG, " \
                     "COLUMN_A,  COLUMN_B, COLUMN_C, COLUMN_D,  COLUMN_E," \
                     "COLUMN_F, COLUMN_G, COLUMN_H, COLUMN_I, COLUMN_J, " \
                     "COLUMN_K, COLUMN_L, COLUMN_M, COLUMN_N, COLUMN_O, " \
                     "COLUMN_P, COLUMN_Q, COLUMN_R, COLUMN_S,  COLUMN_T, " \
                     "COLUMN_U, COLUMN_V, COLUMN_W, COLUMN_X, COLUMN_Y, COLUMN_Z" \
                    " FROM " + TABLE_NAME + "  where 1=1 and SHEET_NAME = 'Sheet1'"

        cue.execute(query_sql)  # 执行sql
        workbook = xlsxwriter.Workbook('D:/tmp/data/test5.xlsx')  # 建立文件
        worksheet = workbook.add_worksheet()  # 建立sheet
        # 查询所有数据，返回结果默认以元组形式，所以可以进行迭代处理
        row = 1
        for i in cue.fetchall():
           # print(i)
            col = 0
            if i[3] == 'Y':
                for d in i:
                    worksheet.write(0, col, d)
                    col = col + 1
                continue
            for d in i:
                worksheet.write(row, col, d)
                col = col + 1
            row = row + 1
        workbook.close()


    except Exception as e:
        print('query error:', e)
        con.rollback()
    else:
        con.commit()
    cue.close()  # 关闭游标

def writer_csv():

    data = read_input_ex();
    print("====")
    print(data)
    with open('D:/tmp/data/data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        spamwriter = csv.writer(csvfile)
        for d in data:
            spamwriter.writerow(d)

if __name__ == '__main__':
    writer_csv()
