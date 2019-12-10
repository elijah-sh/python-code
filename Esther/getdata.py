import json

import pymysql
import requests
#import pyoracle  # 引用模块cx_Oracle

host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'test'
c = 'utf8'
port = 3306
TABLE_NAME = 'snowman'
symbol = 'SZ002936'
def getBrand():

    zz = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=SZ002936&type=Q4&is_detail=true&count=6&timestamp="
    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=SZ002936&type=Q4&is_detail=true&count=6&timestamp=1819955200001"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xq_a_token.sig=ZvtaY2gpozjtDgM9XQBm-U6v7VE; xq_r_token=670668eda313118d7214487d800c21ad0202e141; xq_r_token.sig=nB5LZeMGKYGGQHzx5fGb8InoJlQ; xqat=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xqat.sig=HJXN1BVd98YfFXpmbPKXMmSNL60; u=971575639800540; device_id=078fc8a1158fb5f5fb3d6e42c8bc1c24; Hm_lvt_1db88642e346389874251b5a1eded6e3=1575639801; s=c214qyu0nd; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1575642250"
    }
    print(url)
    response = requests.get(zz, headers = headers )
    result = json.loads(response.text)
    datas = result['data']['list']
    #print(datas)
    quote_name = result['data']['quote_name']
    for data in datas :
        item_info = {}
        item_info['report_name'] = data['report_name']
        item_info['quote_name'] = quote_name
        item_info['symbol'] = symbol
        item_info['currency_funds'] =  data['currency_funds'][0]
        item_info['tradable_fnncl_assets'] = data['tradable_fnncl_assets'][0]
        item_info['ar_and_br'] = data['ar_and_br'][0]
        item_info['bills_receivable'] = data['bills_receivable'][0]
        item_info['pre_payment'] = data['pre_payment'][0]
        item_info['othr_receivables'] = data['othr_receivables'][0]
        item_info['othr_current_assets'] = data['othr_current_assets'][0]
        item_info['lt_equity_invest'] = data['lt_equity_invest'][0]
        item_info['fixed_asset_sum'] = data['fixed_asset_sum'][0]
        item_info['fixed_asset'] = data['fixed_asset'][0]
        item_info['intangible_assets'] = data['intangible_assets'][0]
        item_info['goodwill'] = data['goodwill'][0]
        item_info['lt_deferred_expense'] = data['lt_deferred_expense'][0]
        item_info['othr_noncurrent_assets'] = data['othr_noncurrent_assets'][0]
        item_info['total_noncurrent_assets'] = data['total_noncurrent_assets'][0]


        process_item(item_info)
        print(item_info)




def process_item(item):
    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)

    # 数据库游标
    cue = con.cursor()
    try:
        cue.execute("insert ignore into " +
                    TABLE_NAME +
                    "("
                     "quote_name,"
                    "symbol,"
                    "report_name,"
                    "currency_funds,"
                    "tradable_fnncl_assets,"
                    "ar_and_br,"
                    "bills_receivable,"
                    "pre_payment,"
                    "othr_receivables,"
                    "othr_current_assets,"
                    "lt_equity_invest,"
                    "fixed_asset_sum,"
                    "fixed_asset,"
                    "intangible_assets,"
                    "goodwill,"
                    "lt_deferred_expense,"
                    "othr_noncurrent_assets,"
                    "total_noncurrent_assets"
                    ") "
                    "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [
                        item['quote_name'],
                        item['symbol'],
                        item['report_name'],
                        item['currency_funds'],
                        item['tradable_fnncl_assets'],
                        item['ar_and_br'],
                        item['bills_receivable'],
                        item['pre_payment'],
                        item['othr_receivables'],
                        item['othr_current_assets'],
                        item['lt_equity_invest'],
                        item['fixed_asset_sum'],
                        item['fixed_asset'],
                        item['intangible_assets'],
                        item['goodwill'],
                        item['lt_deferred_expense'],
                        item['othr_noncurrent_assets'],
                        item['total_noncurrent_assets'],
                     ])
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()
    con.close()

if __name__ == '__main__':
    getBrand()
