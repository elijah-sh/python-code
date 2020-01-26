import json

import pymysql
import requests
import pyoracle  # 引用模块 cx_Oracle
import datetime
import  time
host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'test'
c = 'utf8'
port = 3306
TABLE_NAME = 'ESTHER_117'
# 流动负债合计 total_current_liab 流动资产合计	total_current_assets
def getBrand(symbol, company_name):
    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol="+symbol+"&type=Q4&is_detail=true&count=6&timestamp="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=c9d3b00a3bd89b210c0024ce7a2e049f437d4df3;"
    }
    response = requests.get(url, headers = headers )
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
        if data['report_name'] == '2014年报':
            item_info['total_current_assets'] =  data['total_current_assets'][0]
            item_info['total_current_liab'] =  data['total_current_liab'][0]
            pdata.append(data['total_current_assets'][0])
            pdata.append(data['total_current_liab'][0])
            print(item_info)
        if data['report_name'] == '2013年报':
            item_info['total_current_liab'] = data['total_current_liab'][0]
            pdata.append(data['total_current_liab'][0])
            print(item_info)
    return pdata;


def process_item():
    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
    # 数据库游标
    cue = con.cursor()
    try:

        # 查询数据
        query_sql = "select  ID,  HEBING,       DATA_ID,       COMPANY_NAME,       STOCK_CODE  " \
                    " from " + TABLE_NAME + "  where COMPANY_NAME is not null "

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

            update_sql = "update " + TABLE_NAME + "  set total_current_assets14=%s " \
                                                  ", total_current_liab14=%s " \
                                                  ", total_current_liab13=%s " \
                                                  ", DESCRIPTION=%s " \
                                                  " where ID=%s"

            data = ( pdata[1], pdata[2], pdata[3],pdata[0],i[0])

            try:
                #cue.execute(update_sql, data)
                print(data)
            except Exception as e:
                print('Insert error:', e)
                con.rollback()
            else:
                con.commit()
        print('共查询到：', cue.rowcount, '条数据。')

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
