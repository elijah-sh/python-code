import requests

def getBrand():
    url = "https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=OC430247&type=Q4&is_detail=true&count=5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie":"xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2;"
    }
    response = requests.get(url, headers = headers )
    print(response.text)

if __name__ == '__main__':
    getBrand()