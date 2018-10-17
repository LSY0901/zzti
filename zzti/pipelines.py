# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class ZztiPipeline(object):
    def __init__(self):
       dispatcher.connect(self.spider_opened, signals.spider_opened)
       dispatcher.connect(self.spider_closed, signals.spider_opened)

    def process_item(self, item, spider):
        self.conn = pymysql.connect(host='127.0.0.1', user='root',
                                    password='', db='zzti', port=3306)
        self.cursor = self.conn.cursor()

        title = item.get('title')
        href = item.get('href')
        content = item.get('content')
        sql = 'insert into m_zzti (title,href,content) VALUES (%s,%s,%s)'

        self.cursor.execute(sql, (title,href,content))
        self.conn.commit()
        print('操作成功！')
        return item

    def close_spider(self, spider):
        # 关闭资源
        self.cursor.close()
        self.conn.close()

    def spider_opened(self, spider):
        print('**********open')

    def spider_closed(self, spider):
        print('**********close')
