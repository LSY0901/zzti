# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   TitleSpider
  Description: 抓取校网学术动态
  Author:       Mr.Liu
  date:         2018/8/24
-----------------------------------------------
   Change Activity:
                2018/8/24:
-----------------------------------------------
"""
_author_ = 'Mr.Liu'
import scrapy
from zzti.items import ZztiItem
from scrapy.http import Request
import re
class TestSpider(scrapy.Spider):
       name = "zzti"
       allowed_domains = ["www.zzti.edu.cn"]
       start_urls = ["http://www.zzti.edu.cn/index/jxgz/31.htm"]
       # 主网页的标题
       def parse(self, response):
           m_title = '//a[@class="c67214"]/@title'
           m_href = '//a[@class="c67214"]/@href'
           m_datem = '//span[@class="timestyle67214"]/text()'
           m_last = '//a[@class="Next"]/@href'
           title = response.xpath(m_title).extract()
           hrefs  = response.xpath(m_href).extract()
           datem  = response.xpath(m_datem).extract()
           last = response.xpath(m_last).extract()
           for i in range(0, len(title)):
               item = ZztiItem()
               item['title'] = title[i]
               item['datem'] = datem[i]
               item['href'] = hrefs[i].replace('../..', 'www.zzti.edu.cn')
               href = 'http://www.zzti.edu.cn'+hrefs[i][5:]
               yield scrapy.Request(href, meta = {'item': item}, callback=self.parse_ser)
            # 读取下一页
           url = 'http://www.zzti.edu.cn/index/jxgz/' + last[0]
           yield scrapy.Request(url, callback=self.parse)
        # 读取子页内容
       def parse_ser(self, response):
           item = response.meta['item']
           m_content = '//div/div[@class="v_news_content"]//p/span/text()'
           content = response.xpath(m_content).extract()
           contents = ""
           for i in range(0, len(content)):
                contents +=content[i]
           item['content'] = contents
           yield item






