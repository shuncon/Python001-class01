import requests
from  bs4 import BeautifulSoup as bs

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

header = {'user-agent' : user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header) 
bs_info = bs(response.text,'html.parser')


# 使用for方法来模拟浏览指针
for tags in bs_info.find_all('div',attrs={'class': 'hd'}):
    for atag in tags.find_all('a',):

        #获取所有链接
        print(atag.get('href'))
        获取电影名称
        print(atag.find('span',).text)
