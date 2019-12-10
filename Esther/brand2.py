import json

import pymysql
import requests
host = '127.0.0.1'
user = 'root'
psd = '123456'
db = 'test'
c = 'utf8'
port = 3306
TABLE_NAME = 'snowman'

def getBrand():
    url = 'https://fhs.jd.com/api/getattrinfo?sub=12477&md=1&fhc=pc&callback=jQuery7435860&my=list_brand'
    callback = 'jQuery7435860'
    result = requests.get(url).text[len(callback)+1:-1]
    result = json.loads(result)
    brands = result['brands']
    for brand in brands:
        item_info = {}
        item_info['big_circle'] = '美妆个护'
        item_info['middle_circle'] = '美妆'
        item_info['small_circle'] = '底妆'
        brand_name = brand['name']
        if '（' in str(brand_name):
            brand_name_cn = brand_name.split('（')[0]
            brand_name_en = brand_name.split('（')[1][:-1]
            item_info['brand_name_cn'] = brand_name_cn
            item_info['brand_name_en'] = brand_name_en
        elif (brand_name>= u'\u0041' and brand_name<=u'\u005a') or (brand_name >= u'\u0061'and brand_name<=u'\u007a'):
            item_info['brand_name_cn'] = None
            item_info['brand_name_en'] = brand_name
        else:
            item_info['brand_name_cn'] = brand_name
            item_info['brand_name_en'] = None
        item_info['brand_id'] = brand['id']
        item_info['source'] = 'jd'
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
                   # "(big_circle,middle_circle,small_circle,brand_id,brand_name_cn,brand_name_en,source) "
                     "(report_name,total_assets,total_liab,asset_liab_ratio,total_quity_atsopc,held_to_maturity_invest,interest_receivable) "

                    "values (%s,%s,%s,%s,%s,%s,%s)",
                    [item['big_circle'],item['middle_circle'],item['small_circle'],item['brand_id'],item['brand_name_cn'],item['brand_name_en'],item['source']])
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()
    con.close()

if __name__ == '__main__':
    getBrand()