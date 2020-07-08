import  time
import  random
import requests
from  fake_useragent import  UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer'  : 'https://shimo.im/login?from=home'
}

s = requests.Session()


login_url = 'https://shimo.im/login?from=home'
form_data = {
'ck' : '',
'name' : '1428834423@qq.com',
'password' : f'riadwkdm/text()',
'remeber' : 'flase',
'ticket' : ''
}

pre_login = 'https://shimo.im/dashboard/used'
pre_resp = s.get(pre_resp,headers=headers)

response = s.post(login_url,data=form_data,  headers=headers, cookies=s.cookies )