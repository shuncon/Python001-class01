import  scrapy
import  logging

logger= logging.getLogger(())

class Maoyanspider(scrapy.Spider):
    name= 'maoyan'
    allowed_dimains = ['manyan.com']
    start_url = 'https://maoyan.com/films?showType=3'

    def parse(self,response):
        request_url= response.request.url
        #divs = response.xpath('//*[@class="movie-hover-title"][1]')
        divs  = response.xpath('//*[@class="movie-hover-info"][1]')
        print(divs)