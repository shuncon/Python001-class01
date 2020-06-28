import  scrapy

class Maoyanspider(scrapy.Spider):
    name= 'maoyan'
    allowed_dimains = ['manyan.com']
    start_url = 'https://maoyan.com/films?showType=3'

    def parse(self,response):
        request_url= response.request.url