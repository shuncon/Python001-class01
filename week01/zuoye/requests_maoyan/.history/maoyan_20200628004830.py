#-*-conding：utf-8 -*-

import requests
import  lxml
from  bs4 import BeautifulSoup as bfs

user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# header = {'user-agent' : user_agent}

myurl = 'https://maoyan.com/films?showType=3'

header = {}
header ['user-agent'] = user_agent
response = requests.get(myurl,headers=header)

# selector = lxml.etree.HTML(response.text)

bs_info = bfs(response.text,'html.parser')