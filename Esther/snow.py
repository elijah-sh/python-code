import json

import pymysql
import requests
#import pyoracle  # 引用模块cx_Oracle
import datetime
import  time
host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'test'
c = 'utf8'
port = 3306
TABLE_NAME = 'snow'
symbol = 'SZ002936'
def getBrand(symbol, company_name):
    cash_flow = "https://stock.xueqiu.com/v5/stock/finance/cn/cash_flow.json?symbol="+symbol+"&type=Q4&is_detail=true&count=6&timestamp="

    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol="+symbol+"&type=Q4&is_detail=true&count=6&timestamp=1819955200001"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=c9d3b00a3bd89b210c0024ce7a2e049f437d4df3;"
    }
    response = requests.get(cash_flow, headers = headers )
    result = json.loads(response.text)
    datas = result['data']['list']
    quote_name = result['data']['quote_name']
    if  quote_name != company_name:
        return
    pdata = []
    pdata.append(quote_name)

    for data in datas :
        item_info = {}
        item_info['report_name'] = data['report_name']
        #item_info['total_assets'] =  data['total_assets'][0]
        item_info['net_increase_in_cce'] =  data['net_increase_in_cce'][0]
        # net_increase_in_cce
        pdata.append(data['net_increase_in_cce'][0])
        print(item_info)
    return pdata;


def process_item():
    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
    # 数据库游标
    cue = con.cursor()
    try:
       # cue.execute("select * from " + TABLE_NAME + "  where COMPANY_NAME is not null and STOCK_CODE is not null")

        # 查询数据
        query_sql = "select  ID,  HEBING,       DATA_ID,       COMPANY_NAME,       STOCK_CODE, " \
                    "   ASSETS_TOTAL18, ASSETS_TOTAL17, ASSETS_TOTAL16, ASSETS_TOTAL15,  ASSETS_TOTAL14, ASSETS_TOTAL13,   " \
                    "    CASH_FLOW18,    CASH_FLOW17,   CASH_FLOW16,   CASH_FLOW15,   CASH_FLOW14,    CASH_FLOW13,   " \
                    "    DESCRIPTION,       CREATE_DATE,       LAST_UP_DATE " \
                    " from " + TABLE_NAME + "  where COMPANY_NAME is not null and STOCK_CODE  is not null "



        cue.execute(query_sql)  # 执行sql

        # 查询所有数据，返回结果默认以元组形式，所以可以进行迭代处理
        for i in cue.fetchall():
            s = i[2].split('.')
            sc = s[1] + s[0]
            pdata = getBrand(sc,i[3])
            print(i[3])  # 公司
            print(sc)  # 股票
            print(pdata)  # 股票
            if pdata == None:
                continue
            as_update_sql = "update " + TABLE_NAME + "  set ASSETS_TOTAL18=%s " \
                                             ", ASSETS_TOTAL17=%s, ASSETS_TOTAL16=%s, ASSETS_TOTAL15=%s" \
                                             ", ASSETS_TOTAL14=%s, ASSETS_TOTAL13=%s" \
                                              ", DESCRIPTION=%s " \
                                              ", STOCK_CODE=%s " \
                                             " where ID=%s"
            update_sql = "update " + TABLE_NAME + "  set CASH_FLOW18=%s " \
                                                  ", CASH_FLOW17=%s, CASH_FLOW16=%s, CASH_FLOW15=%s" \
                                                  ", CASH_FLOW14=%s, CASH_FLOW13=%s, DESCRIPTION=%s " \
                                                  " where ID=%s"
            pdta1 = ''
            if len(pdata) < 7:
                pdta1 = 'None'
            else:
                pdta1 = pdata[6]

            pdta2 = ''
            if len(pdata) < 6:
                pdta2 = 'None'
            else:
                pdta2 = pdata[5]
            data = (pdata[1], pdata[2], pdata[3], pdata[4], pdta2, pdta1,sc,i[0])

            try:
                cue.execute(update_sql, data)
                print(data)
            except Exception as e:
                print('Insert error:', e)
                con.rollback()
            else:
                con.commit()
        print('共查询到：', cue.rowcount, '条数据。')

        # # 获取第一行数据
        # result_1 = cue.fetchone()
        # print(result_1)
        # print(result_1[0])
        # print(result_1[1])
        # print(result_1[2])
        # print(result_1[3])
        # print(result_1[4])
        # pdata = getBrand((result_1[4]), result_1[3])
        # print(pdata)
        # print(pdata[0])
        # print(pdata[1])
        update_sql = "update " + TABLE_NAME + "  set CASH_FLOW18=%s " \
                                               ", CASH_FLOW17=%s, CASH_FLOW16=%s, CASH_FLOW15=%s" \
                                               ", CASH_FLOW14=%s, CASH_FLOW13=%s, DESCRIPTION=%s " \
                                              " where ID=%s"

    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()

    cue.close()  # 关闭游标
    con.close()

if __name__ == '__main__':
    # getBrand()
    process_item()
