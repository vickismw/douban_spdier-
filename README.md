# douban_spdier-
top250 next_pag获取
# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 允许下载的域名
    allowed_domains = ['movie.douban.com']
    # 配置下载的首地址
    start_urls = ['http://movie.douban.com/top250']
    # 下载完毕之后的解析方法 (parse在源码中支持yield)

    def parse(self, response):
        # print(response.text)
        html = etree.HTML(response.text)
        # 首先通过xpath获取ol
        li_list = html.xpath("//ol[@class='grid_view']/li")
        for li in li_list:
            item = DoubanItem()
            # em = title = img = comment
            item['em'] = li.xpath(".//em/text()")[0]
            item['title'] = li.xpath(".//span[@class='title']/text()")[0]
            item['img'] = li.xpath(".//img/@src")[0]
            item['comment'] = li.xpath(".//div[@class='star']/span/text()")[-1]
            # yield返回当前电影的数据
            yield item
        try:
            # 获取后页超链接的值 （xpath返回的是list）
            next_page = html.xpath("//span[@class='next']/a/@href")[0]
            # 手动发送请求,让爬虫去解析下一页的数据 (ajax)
            yield scrapy.Request(url = 'http://movie.douban.com/top250' + next_page,callback=self.parse)
        except:
            print('下载完毕.......')


＃在scrapy框架下在新建main.py表，配置获取douban_spider内容

from scrapy.cmdline import execute

execute("spider crawl douban_spider".split(' '))
