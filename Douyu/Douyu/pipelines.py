# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  scrapy.pipelines.images import ImagesPipeline
import  scrapy


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['image_link']
        yield scrapy.Request(image_link)
    #
    # def process_item(self, item, spider):
    #     return item
