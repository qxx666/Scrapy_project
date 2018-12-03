# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    positionType = scrapy.Field()
    positionNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()
