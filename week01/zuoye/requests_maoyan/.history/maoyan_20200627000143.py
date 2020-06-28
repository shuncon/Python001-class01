#-*-conding：utf-8 -*-

import requests
import  lxml
from  bs4 import BeautifulSoup as bfs

user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# header = {'user-agent' : user_agent}

myurl = 'https://maoyan.com/films/1222268',
'https://maoyan.com/films/1217023',

header = {}
header ['user-agent'] = user_agent
response = requests.get(myurl,headers=header)

selector = lxml.etree.HTML(response.text)

#电影名称
dy_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
print(f'电影名称：{dy_name}')
# response = requests.get(myurl, headers=header)
# # print (response.text)

# # print (f'返回状态码: {response.status.code}')