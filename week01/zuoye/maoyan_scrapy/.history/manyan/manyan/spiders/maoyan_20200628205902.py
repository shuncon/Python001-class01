import  scrapy

class Maoyanspider(scrapy.Spider):
    name= 'maoyan'
    allowed_dimains = ['manyan.com']
    start_url = ''