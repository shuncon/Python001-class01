from  urllib import  request
import  urllib.request

# get方法
resp = request.urlopen('http://httpbin.org/get')
print (resp.read().decode())

#post方法
resps = request.urlopen('http://httpbin.org/post',data=b'key=value',timeout=10)
print (resps.read().decode())

#cookie
from  http import  cookiejar
# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建一个cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建opener对象
opener = request.build_opener(hanler)