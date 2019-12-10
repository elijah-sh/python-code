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

def getBrand():
    # url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=OC430247&type=Q4&is_detail=true&count=5"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    #     "Cookie":"xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2;"
    # }

    # 2014
    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=OC430247&type=Q4&is_detail=true&count=5&timestamp=1419955200001"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xq_a_token.sig=ZvtaY2gpozjtDgM9XQBm-U6v7VE; xq_r_token=670668eda313118d7214487d800c21ad0202e141; xq_r_token.sig=nB5LZeMGKYGGQHzx5fGb8InoJlQ; xqat=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xqat.sig=HJXN1BVd98YfFXpmbPKXMmSNL60; u=971575639800540; device_id=078fc8a1158fb5f5fb3d6e42c8bc1c24; Hm_lvt_1db88642e346389874251b5a1eded6e3=1575639801; s=c214qyu0nd; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1575642250"
    }

    response = requests.get(url, headers = headers )
    result = json.loads(response.text)
    datas = result['data']['list']
    for data in datas :
        item_info = {}
        item_info['report_name'] = data['report_name']
        item_info['quote_name'] = data['report_name']
        item_info['symbol'] = 'OC430247'
        item_info['currency_funds'] = data['currency_funds'][0]
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

        # item_info['total_assets'] = data['total_assets'][0]
        # item_info['total_liab'] = data['total_liab'][0]
        # item_info['asset_liab_ratio'] = data['asset_liab_ratio'][0]
        # item_info['total_quity_atsopc'] = data['total_quity_atsopc'][0]
        # item_info['tradable_fnncl_assets'] = data['tradable_fnncl_assets'][0]
        # item_info['interest_receivable'] = data['interest_receivable'][0]
        #
        # item_info['saleable_finacial_assets'] = data['saleable_finacial_assets'][0]
        # item_info['held_to_maturity_invest'] = data['held_to_maturity_invest'][0]
        #
        # item_info['fixed_asset'] = data['fixed_asset'][0]
        # item_info['intangible_assets'] = data['intangible_assets'][0]
        # item_info['construction_in_process'] = data['construction_in_process'][0]
        # item_info['dt_assets'] = data['dt_assets'][0]
        # item_info['tradable_fnncl_liab'] = data['tradable_fnncl_liab'][0]
        #
        # item_info['payroll_payable'] = data['payroll_payable'][0]
        # item_info['tax_payable'] = data['tax_payable'][0]
        # item_info['estimated_liab'] = data['estimated_liab'][0]
        # item_info['dt_liab'] = data['dt_liab'][0]
        # item_info['bond_payable'] = data['bond_payable'][0]
        # item_info['shares'] = data['shares'][0]
        # item_info['capital_reserve'] = data['capital_reserve'][0]
        #
        # item_info['payroll_payable'] = data['payroll_payable'][0]
        # item_info['tax_payable'] = data['tax_payable'][0]
        # item_info['estimated_liab'] = data['estimated_liab'][0]
        # item_info['dt_liab'] = data['dt_liab'][0]
        # item_info['bond_payable'] = data['bond_payable'][0]
        # item_info['shares'] = data['shares'][0]
        # item_info['capital_reserve'] = data['capital_reserve'][0]
        #
        # item_info['earned_surplus'] = data['earned_surplus'][0]
        # item_info['undstrbtd_profit'] = data['undstrbtd_profit'][0]
        # item_info['minority_equity'] = data['minority_equity'][0]
        # item_info['total_holders_equity'] = data['total_holders_equity'][0]
        # item_info['lt_equity_invest'] = data['lt_equity_invest'][0]
        # item_info['derivative_fnncl_liab'] = data['derivative_fnncl_liab'][0]
        # item_info['general_risk_provision'] = data['general_risk_provision'][0]
        #
        # item_info['frgn_currency_convert_diff'] = data['frgn_currency_convert_diff'][0]
        # item_info['goodwill'] = data['goodwill'][0]
        # item_info['invest_property'] = data['invest_property'][0]
        # item_info['interest_payable'] = data['interest_payable'][0]
        # item_info['treasury_stock'] = data['treasury_stock'][0]
        # item_info['othr_compre_income'] = data['othr_compre_income'][0]
        # item_info['othr_equity_instruments'] = data['othr_equity_instruments'][0]
        #
        # item_info['currency_funds'] = data['currency_funds'][0]
        # item_info['bills_receivable'] = data['bills_receivable'][0]
        # item_info['account_receivable'] = data['account_receivable'][0]
        # item_info['pre_payment'] = data['pre_payment'][0]
        # item_info['dividend_receivable'] = data['dividend_receivable'][0]
        # item_info['othr_receivables'] = data['othr_receivables'][0]
        # item_info['inventory'] = data['inventory'][0]
        #
        # item_info['nca_due_within_one_year'] = data['nca_due_within_one_year'][0]
        # item_info['othr_current_assets'] = data['othr_current_assets'][0]
        # item_info['current_assets_si'] = data['current_assets_si'][0]
        # item_info['total_current_assets'] = data['total_current_assets'][0]
        # item_info['lt_receivable'] = data['lt_receivable'][0]
        # item_info['dev_expenditure'] = data['dev_expenditure'][0]
        # item_info['lt_deferred_expense'] = data['lt_deferred_expense'][0]

        process_item(item_info)
        print(item_info)
    #conn=cx_Oracle.connect(‘用户名/密码@主机ip地址：端口号/Service Name（SID)')
    # conn = cx_Oracle.connect('boot/boot@47.102.111.109:16021/XE')  # 连接数据库
    # c = conn.cursor()  # 获取cursor
    # x = c.execute('select sysdate from dual')  # 使用cursor进行各种操作
    # x.fetchone()
    # c.close()  # 关闭cursor
    # conn.close()  # 关闭连接




def process_item(item):
    # 数据库连接
   # con = pymysql.connect(host="localhost", user="root", passwd=123456, db="test", charset="utf8", port=3306)
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)

    # 数据库游标
    cue = con.cursor()
    try:
        cue.execute("insert ignore into " +
                    TABLE_NAME +
                    "(report_name,"
                    "total_assets,"
                    "total_liab,"
                    "asset_liab_ratio,"
                    "total_quity_atsopc,"
                    "tradable_fnncl_assets,"
                    "interest_receivable"
                    ") "
                    "values (%s,%s,%s,%s,%s,%s,%s)",
                    [item['report_name'],
                     item['total_assets'],
                     item['total_liab'],
                     item['asset_liab_ratio'],
                     item['total_quity_atsopc'],
                     item['tradable_fnncl_assets'],
                     item['interest_receivable']
                     ])
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()
    con.close()

if __name__ == '__main__':
    getBrand()
