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

import requests
import json
import pymysql

class mysql_conn(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self):
        #t
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, database='test')
        self.cursor = self.db.cursor()
    # 执行modify(修改)相关的操作
    def execute_modify_mysql(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()

# 使用抓包工具分析发送数据请求到json格式的cookie数据，这是此次动态抓取的重点
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xq_a_token.sig=ZvtaY2gpozjtDgM9XQBm-U6v7VE; xq_r_token=670668eda313118d7214487d800c21ad0202e141; xq_r_token.sig=nB5LZeMGKYGGQHzx5fGb8InoJlQ; xqat=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xqat.sig=HJXN1BVd98YfFXpmbPKXMmSNL60; u=971575639800540; device_id=078fc8a1158fb5f5fb3d6e42c8bc1c24; Hm_lvt_1db88642e346389874251b5a1eded6e3=1575639801; s=c214qyu0nd; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1575642250"
    }
url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=111'

response = requests.get(url,headers=headers)

res_dict = json.loads(response.text)

list_lsit = res_dict['list']

db ={}
for list_item_dict in list_lsit:
    data_dict = json.loads(list_item_dict['data'])

    db['id'] = data_dict['id']
    db['title'] = data_dict['title']
    db['description'] = data_dict['description']
    db['target'] = data_dict['target']
    try:
        sql = 'insert into xueqiu (uid,title,description,target) values ("{id}","{title}","{description}","{traget}")'.fromart(**db)
        mc = mysql_conn()
        mc.execute_modify_mysql(sql)
    except:
        pass



