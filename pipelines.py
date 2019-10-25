# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs      #开发包，文件的编码，避免编码的繁杂工作
import json
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class MysqlPipeline(object):  #connenct('host','user','password','dbname'
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '密码', 'article_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
           insert into douban_spider(title, em, img, comment)
           VALUES (%s, %s, %s, %s)
        """ #execute-commit 同步操作，execute不操作完，就不会网commit去
        self.cursor.execute(insert_sql, (item["title"], item["em"], item["img"], item["comment"]))
        self.conn.commit()

