from bs4 import BeautifulSoup
import bs4
import requests
import beautifulsoup4
res = requests.get('https://gitee.com/maxiaoqian')
# 如果不指定parser，会有警告，使用默认的html.parser，不同的系统解析可能会有差异
soup = BeautifulSoup(res.text, 'html.parser')

# 获取操作tag， <class 'bs4.element.Tag'>
# 返回：
'''
  <div class="follow-num" id="followers-number">
  42
  </div>
'''
tag = soup.find('div', attrs={'id': 'followers-number'})              # 查找树
# tag = soup.find_all('div', attrs={'id': 'followers-number'})[0]
# tag = soup.select_one('div#followers-number')                   # css selector方式
# tag = soup.select('div#followers-number')[0]

# 返回tag的内容: tag.text 或者 tag.get_text()
print(tag.get_text().strip())    # 移除内容字符串中前后的空格，返回: '42'