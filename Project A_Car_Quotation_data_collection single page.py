import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
# 请求URL

url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8' 
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=100)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

# 分析当前页面的报价
def analysis(soup):
        temp = soup.find('div', class_='search-result-list')
        #创建DataFrame
        df = pd.DataFrame(columns=['name', 'lowP', 'HighP', 'picURL'])
        a_list = temp.find_all('a')
        for a in a_list:
            #解析各个字段的内容
            temp =  {}
            print(a_list)
            name = a.find(class_= "cx-name text-hover").text
            Price = a.find(class_="cx-price").text
            lowP = re.split('[-]', Price)[0]+'万'
            HighP = re.split('[-]', Price)[-1]
            picURL = 'http:'+ a.find('img').get('src')
            # 放到DataFrame中
            temp['name'], temp['lowP'], temp['HighP'], temp['picURL'] = name, lowP, HighP, picURL
            df = df.append(temp, ignore_index=True)
        return df

result = analysis(soup)
print(result)

# 导出提取的数据到csv
result.to_csv('result.csv', index=False)
