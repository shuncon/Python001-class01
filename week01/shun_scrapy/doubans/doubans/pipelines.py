# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubansPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item,spider):
        title = item ['title']
        link = item['link']
        content = item['content']
        output = f'|{title}|\t|{link}|\t|{content}|\n\n'
        with  open('./doubanmovie.txt', 'a+', encoding='utf-8' ) as article:
            article.write(output)
            article.close()
        return item
