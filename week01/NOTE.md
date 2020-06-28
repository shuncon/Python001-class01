# 学习笔记:
## 1.文件名不能和库名相同

## 2.第三方包
### requests
     属于第三方包，需要使用pip安装 或者通过其他虚拟环境工具安装：pipenv conda


## 3. 浏览器ua头部信息：

### UA配置
   user_agent = '输入当前浏览器ua信息，可通过此网站快速获取：http://service.spiritsoft.cn/ua.html'

### header语句
```
header = {'user-agent' : user_agent}
```

## 4. get和post、cookie
```
get 属于向服务器请求数据（请求网页信息）
post 属于向服务器提交数据（如用户登录，用户填写评论并提交）
cookie 属于服务器验证客户端信息（用户密码登录）

```

## 5.scrapy框架
```
1.使用scrapy生成项目
    scrapy startproject name

2. 初始化项目文件
    scrapy genspider douban  douban.com
``` 