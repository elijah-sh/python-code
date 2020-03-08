import json
#import ssl
#import urllib3.contrib.pyopenssl
import requests
#字符串格式
def get_student_info(studentNum):
    #requests.packages.urllib3.disable_warnings()
   # context = ssl._create_unverified_context()

    print(studentNum)
    requests.get('https://pypi.org/simple/pip/', verify=False)
    r = requests.get('https://www.12306.cn', verify=False, headers={'Connection':'close'})

    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session();
    s.keep_alive = False

    print(r.status_code)
    s_url = "https://teacher.yhkdz.cn/StudentInfo/StudentList";
    data = {"classid": 131}

    header  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "techerClient=platform=1&SchoolID=67&SchoolName=%e8%a5%84%e5%9f%8e%e5%8e%bf%e5%ae%9e%e9%aa%8c%e9%ab%98%e4%b8%ad&SchoolFlag=xiangchengshiyan&openid=&Username=13733734302&IPAddress=tGt5URfb8ZUzHGqPOUF2kQ==&LoginName=d3g6DD8nF/w=&DatabasePass=SG4mbANR95Q=&ConnectionName=BhdA2yeowXXJBcpceT6y9NblJtVuc+VW"
    }

    response = requests.post(s_url, json=json.dumps(data), headers =header, verify=False)
    print(response.status_code)
    #

    result = json.loads(response.text)
   # # datas = result['data']['list']
    print(result)



if __name__ == '__main__':
    # getBrand()
    get_student_info(10553)
