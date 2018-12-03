# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    baseurl = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseurl + str(offset)]

    def parse(self, response):
        item = TencentItem()
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = "https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract()[0]
            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = ""
            item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]
            yield item

        # if self.offset < 3574:
        #     self.offset += 10
        #     url = self.baseurl + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)
        if not len(response.xpath("//a[@class='noactive' and @id ='next']")):
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("http://hr.tencent.com/" + url, callback=self.parse)
