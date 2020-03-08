import json

import requests

def getBrand():
    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=OC430247&type=Q4&is_detail=true&count=6&timestamp=1819955200001"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=bc5da084cb40a795bbfb99a06aaa3e070dc180d2 ;"
    }
    response = requests.get(url, headers = headers )
    result = json.loads(response.text)
    print(result)

if __name__ == '__main__':
    getBrand()