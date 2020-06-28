# -*- coding: utf-8 -*-
###第二阶段
import  scrapy
from items import  DoubansItem
from scrapy.selector import Selector

###第一阶段
# import scrapy
# from  bs4  import  BeautifulSoup as bfs
# from  items import DoubansItem


# class MoviesSpider(scrapy.Spider):
#     name = 'douban'
#     allowed_domains = ['douban.com']
#     start_urls = [#'http://douban.com/',
#     'https://movie.douban.com/top250'
#     ]



###第一阶段
    # #爬虫启动时，引起自动调用该方法，并且只会调用一次，用于生成初始化的请求对象(requests)
    # #start_requests()方法的要求start_urls列表中的URL并生成Requests对象，发送给引擎
    # #引擎再指挥其他组件向网站发送服务器请求，下载网页 
    # def start_requests(self):
    #     for i in range(0, 10):
    #         url = f'https://movie.douban.com/top250?start={i * 25}'
    #         yield  scrapy.Request(url=url, callback=self.parse)
    #         #url  请求访问的地址
    #         #callback 回调函数，引擎会将下载好的页面（reponse对象）发给该方法。执行数据解析
    #         #这里可以使用callback指定新的函数，不是用parse作为默认的回调参数


    # def parse(self, response):
    #     items = []
    #     soup = bfs(response.text, 'html.parser')
    #     title_list = soup.find_all('div', attrs={'class' : 'hd'})
    #     for i in range(len(title_list)):
    #         item = SpidersItem()
    #         title = title_list[i].find('a').find('span',).text
    #         link = title_list[i].find('a').qet('href')
    #         item['tetle'] = title
    #         item['link']  = link
    #         #items.append(item)
    #     #return items
    #         yield  scrapy.Request(url=link, meta={'item': item},callback=self.parse2)


    # def parse2(self, response):
    #     item = response.meta['item']
    #     soup = bfs(response.text,'html.parse')
    #     content = soup.find('div',attrs={'class' : 'related-info'}).get_text().strip()
    #     item['content'] =content
    #     yield item


###第二阶段 使用xpath


class MoviesSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = [#'http://douban.com/',
    'https://movie.douban.com/top250'
    ]

    def start_requests(self):
        i=0
        url = f'https://movie.douban.com/top250?start={i * 25}'
        yield  scrapy.Request(url=url,callback=self.parse,dont_filter=False)

    def parse(self,response):
        print(response.url)
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            title =movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            print('-----------')
            print('title')
            print('link')
            print('-------------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first().strip())
            print(link.extract_first().strip())

