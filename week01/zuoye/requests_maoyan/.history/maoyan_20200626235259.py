#-*-conding：utf-8 -*-

import requests
import  lxml
from  bs4 import BeautifulSoup as bfs

user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# header = {'user-agent' : user_agent}

myurl = 'https://maoyan.com/films/1222268'，
'https://maoyan.com/films/1217023',

header = {}
header ['user-agent'] = user_agent
response = requests.get(myurl,herders=harder)

selector = 

# response = requests.get(myurl, headers=header)
# # print (response.text)

# # print (f'返回状态码: {response.status.code}')