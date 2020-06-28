import  sys, time
import  os

os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

from scrapy import  cmdline

cmdline.execute("scrapy runspider douban".split())