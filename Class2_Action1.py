import requests # 导入requests模块
import pandas as pd # 导入pandas模块
from bs4 import BeautifSoup # 导入BeautifSoup模块

# 请求URL并进行封装, 输入为URL地址，输出为soup结构

def get_page_content(request_url):
    # 得到页面内容
   headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
   html = requests.get(request_url, headers=headers, timeout=10) # 10秒内必须返回响应，否则会报错 一般为了避免再发出请求过程中出现异常而中断请求
   content = html.text
   # 通过content创建BeautifulSoup对象
   soup = BeautifulSoup(content, 'html.parser', from_encouding='utf-8') # 使用html.parser编码，解码中文网页
   return soup

# 分析当前页面的投诉
def analysis(soup):
  temp = soup.find('div', class_='tslb_b') # 查找标签div，只返回第一个匹配到的对象, 通过‘属性=值’的方法进行匹配, 匹配标签内属性使用BeautifulSoup自带的特别关键字class_, tslb_b为HTML内标签
  # 根据待提取的文本创建DataFrame
  df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datatime', 'status'])
  # 返回一个tr标签的列表, tr和td是HTMLde标签，tr代表行，td代表列
  tr_list = temp.find_all('tr') # 返回所有匹配到的结果
  for tr in tr_list:
    #提取汽车投诉信息
    temp={}
    td_list=tr.find_all('td')
    # 第一个tr没有td，其余都有八个td
      if len(td_list) > 0:
        # 解析各个字段的内容
        id, brand, car_model, type, desc, problem, datatime, status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
        # 将解析出的内容，放入到DataFrame当中
        temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], temp['datetime'], temp['status'] = id, brand, car_model, type, desc, problem, datetime, status
        df = df.append(temp, ignore_index=True)
  return df

# 进行多页分析

page_nume = 20
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'

# 创建DataFrame
result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datatime', 'status'])

# 针对每一页进行提取，分析

for i in range(page_num):
  request_url = base_url + str(i+1) + '.shtml' # 每次抓取时，给与新的url地址，规律为尾号+1
  soup = get_page_content(request_url)
  df = analysis(soup)
  print(df)
  result = result.append(df)
  
# 导出提取的数据到csv
result.to.csv('result.csv', index=False)

