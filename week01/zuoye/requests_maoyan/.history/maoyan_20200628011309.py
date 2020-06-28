#-*-conding：utf-8 -*-

import requests
import  lxml

from  bs4 import BeautifulSoup as bfs

user_agent= {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

"Cookie": '__mta=143555850.1593182389402.1593186588642.1593186951752.13; _lxsdk_cuid=172f111f51562-0c65d9babc0209-3a65460c-1fa400-172f111f516c8; uuid_n_v=v1; uuid=E1D4A130B7BA11EAB4E28FB161D5B82BB28615396FEA473FAA79466FF93A0ADC; _lxsdk=E1D4A130B7BA11EAB4E28FB161D5B82BB28615396FEA473FAA79466FF93A0ADC; mojo-uuid=8bd33533b8dd1a759d17cadf1be0eefb; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=0d6a79576c8af13e864ce4bc16256224b781a4cddb5105facfa01b80cc9314b6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593182389,1593186370,1593276349; mojo-session-id={"id":"e7c501439a3b4a3b79e13dd84a3f3791","time":1593276349044}; mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593276558; __mta=143555850.1593182389402.1593186951752.1593276557953.14; _lxsdk_s=172f6abba85-f3d-41e-9d2%7C%7C6'}

# header = {'user-agent' : user_agent}

myurl = 'https://maoyan.com/films?showType=3'

header = {}
header ['user-agent'] = user_agent
response = requests.get(myurl,headers=header)

# selector = lxml.etree.HTML(response.text)

bs_info = bfs(response.text,'html.parser')

for tags in bs_info.find_all('div', arrts={'class':'movie-item-title'}):
    for ttags in tags.find_all('p' ,arrts={'class' : 'name'}):
        for atag in ttags.find_all('a',):
            print (atag.get('href'))
            print (atag.get('titile'))
