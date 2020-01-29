#读取并存入数据库

import xlrd
import pymysql

host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'news_data'
c = 'utf8'
port = 3306
TABLE_NAME = 'EXCEL_ROW_DATA'

WORK_BOOK_NAME = 'D:/tmp/data/25.xls'
SHEET_NAME = 'Sheet1'

def read_input_ex():
    workbook = xlrd.open_workbook(WORK_BOOK_NAME)  # (1)取得excel book对象
    sheet = workbook.sheet_by_name(SHEET_NAME)  # (2)取得sheet对象
    rows = sheet.nrows  # (3)获得总行数

    for r in range(0, rows):
        edata = []
        edata.append(WORK_BOOK_NAME)
        edata.append(SHEET_NAME)
        if r == 0 :
            edata.append('Y')
        else:
            edata.append('N')
        row = sheet.row_values(r)  # (4)获取行数据

        # rows的长度sheet._dimncols
        for t in range(0, sheet._dimncols):
            edata.append(row[t])

        if sheet._dimncols < 26:
            for t in range(0, 26 - sheet._dimncols):
                edata.append("")

        print(edata)
        process_item(edata)



def process_item(item):

    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
    # 数据库游标
    cue = con.cursor()


    insert_sql = " INSERT IGNORE INTO EXCEL_ROW_DATA  ( " \
                 " WORK_BOOK_NAME,  SHEET_NAME, FIRST_ROW_FLAG, " \
                 "COLUMN_A,  COLUMN_B, COLUMN_C, COLUMN_D,  COLUMN_E," \
                 "COLUMN_F, COLUMN_G, COLUMN_H, COLUMN_I, COLUMN_J, " \
                 "COLUMN_K, COLUMN_L, COLUMN_M, COLUMN_N, COLUMN_O, " \
                 "COLUMN_P, COLUMN_Q, COLUMN_R, COLUMN_S,  COLUMN_T, " \
                 "COLUMN_U, COLUMN_V, COLUMN_W, COLUMN_X, COLUMN_Y, COLUMN_Z" \
                 ") VALUE (" \
                 "%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s )"
    print(insert_sql, item)

    try:
        cue.execute(insert_sql,item)
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()

    cue.close()  # 关闭游标


if __name__ == '__main__':
    read_input_ex()
