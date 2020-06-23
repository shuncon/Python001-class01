import requests

import lxml.etree

##重点 ： 使用xpath

#电影详细页面
url = 'https://movie.douban.com/subject/1292052/'

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

#声明为字典，使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url,headers=header)



# xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')

#上映日期
plan_date =selector.xpath( '//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

#电影评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'电影评分：{rating}')

mylist = [film_name,plan_date,rating]

import pandas as  pd

movie1 = pd.DataFrame(data = mylist)

#windows需要使用GBK字符集
#指定路径：./week01/shuncon_requests/movie.csv
movie1.to_csv('./week01/shuncon_requests/shun_lxml.csv', encoding='utf8', index=False, header=False)