import json
import ssl
import http.cookiejar
import urllib.request
import os
import json
import re


#引入模块ssl取消全局验证
ssl._create_default_https_context = ssl._create_unverified_context
headers = [('Accept', 'application/json, text/plain, */*'),('Accept-Language', 'zh-CN,zh;q=0.9'),
('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'),
('Origin', 'https://xueqiu.com')]           
#path = 'C:\\Users\\hq\\Desktop\\'
path = 'D:\\tmp\\data\\'
cj = 0

def getOpener():
    global cj
    filename = 'cookie_xueqiu.txt'   
    cj = http.cookiejar.MozillaCookieJar(filename)
    # 从文件中读取cookie内容到变量  
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来  
    # ignore_expires的意思是如果过期了也照样保存  
    # 如果存在，则读取主要COOKIE  
    if os.path.exists(filename): 
        cj.load(filename, ignore_discard=True, ignore_expires=True)  

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = headers
    return opener

#获得Url对应网页中内容
def getContent(url):
    request = urllib.request.Request(url)
    response = opener.open(request)
    content = response.read()
    content = content.decode('utf-8')
    cj.save(ignore_discard=True, ignore_expires=True)
    return content

#获得公司股票代号
def getCode(company):
    #对汉字进行编码
    company = urllib.parse.quote(company)
    url = "https://xueqiu.com/stock/search.json?code="+str(company)+"&size=3&page=1"
    content = getContent(url)
    content = json.loads(content)
    return content['stocks'][0]['code']

#查看是cn还是hk
def getRegion(code):
    url = "https://xueqiu.com/snowman/S/"+code+"/detail"
    content = getContent(url)
    region = re.compile(r'"region":"(.*?)","status"')
    region = region.findall(content);
    return region
    

#资产负债表（资产合计）
#返回列表
def getData(url,type):
    content = getContent(url)
    content = json.loads(content)
    data = []
    p = content['data']['list']
    for i in range(len(p)):
        data.append(p[i][type][0])
    return data;

#四舍五入保留两位小数
def get_two_float(f_str):
    f_str = str(f_str + 0.005)
    a, b, c = f_str.partition('.')
    c = (c + '00')[:2]
    return ".".join([a,c])

def solve(company):
    code = getCode(company)
    print(code)
    region = getRegion(code)
    print(region)
    region = region[0].lower()

    #资产负债表中数据来源的网址
    url_ZCZFB_1 = 'https://stock.xueqiu.com/v5/stock/finance/'+region+'/balance.json?symbol='+code+'&type=Q4&is_detail=true&count=5&timestamp='
    url_ZCZFB_2 = 'https://stock.xueqiu.com/v5/stock/finance/'+region+'/balance.json?symbol='+code+'&type=Q4&is_detail=true&count=5&timestamp=1419955200001'
    #现金流量表中数据来源的网址
    url_XJLLB_1 = 'https://stock.xueqiu.com/v5/stock/finance/'+region+'/cash_flow.json?symbol='+code+'&type=Q4&is_detail=true&count=5&timestamp='
    url_XJLLB_2 = 'https://stock.xueqiu.com/v5/stock/finance/'+region+'/cash_flow.json?symbol='+code+'&type=Q4&is_detail=true&count=5&timestamp=1419955200001'

    data_ZCZFB = ""
    data_XJLLB = ""

    if region == "cn":
        #资产负债表2014-2018
        data_ZCZFB = getData(url_ZCZFB_1,"total_assets")
        #资产负债表2010-2014
        data_ZCZFB += getData(url_ZCZFB_2,"total_assets")
        #去掉重复的2014年
        del data_ZCZFB[4]

        #现金流量表2014-2018
        data_XJLLB = getData(url_XJLLB_1,"cash_paid_for_assets")
        #现金流量表2010-2014
        data_XJLLB += getData(url_XJLLB_2, "cash_paid_for_assets")
        #去掉重复的2014年
        del data_XJLLB[4]

        print(data_XJLLB)
        print(data_ZCZFB)
    elif region == "hk":
         #资产负债表2014-2018
        data_ZCZFB = getData(url_ZCZFB_1,"ta")
        #资产负债表2010-2014
        data_ZCZFB += getData(url_ZCZFB_2,"ta")
        #去掉重复的2014年
        del data_ZCZFB[4]

    """
        #现金流量表2014-2018
        data_XJLLB = getData(url_XJLLB_1,"cash_paid_for_assets")
        #现金流量表2010-2014
        data_XJLLB += getData(url_XJLLB_2, "cash_paid_for_assets")
        #去掉重复的2014年
        del data_XJLLB[4]
    """
    #把数据存入文件中
    with open("data/"+company + ".txt", "w") as file:

        for i in range(2018,2012,-1):
            file.write("\t" + str(i))
        file.write("\n")
        
        file.write("总资产:")
        for i in data_ZCZFB[:6]:
            file.write(" " + get_two_float(i/10000) + "万")
        file.write("\n")
        file.write("购建固定资产、无形资产和其他长期资产支付的现金:")
        for i in data_XJLLB[:6]:
            file.write(" " + get_two_float(i/10000) + "万")
        


        
opener = getOpener()
#判断data文件夹是否存在，如果不存在则创建
if not os.path.exists("data"):
    os.mkdir("data")


    
        
    








# 单进程
if __name__ == '__main__':

    # 需要爬取的企业的名字放入name列表中
    name = ["九易庄宸"]
    for i in name:
        solve(i)
