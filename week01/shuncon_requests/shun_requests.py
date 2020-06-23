import  requests

#查看浏览器UA:http://service.spiritsoft.cn/ua.html
user_agent ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

header= {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

#定义输出为文本
print (response.text)

print (f'返回状态码: {response.status_code}')