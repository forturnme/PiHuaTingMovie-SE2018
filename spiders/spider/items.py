# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    name = scrapy.Field()
    # 序号
    # ind = scrapy.Field()
    # 年份
    year = scrapy.Field()
    # 月份
    month = scrapy.Field()
    # 日子
    day = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演，多个
    actor = scrapy.Field()
    # 主题
    genre = scrapy.Field()
    # 票房
    boxing = scrapy.Field()
    pass
