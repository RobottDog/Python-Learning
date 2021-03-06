# -*- coding: utf-8 -*-

from scrapy import Request 
from scrapy.spiders import Spider
from DoubanTop250.items import Doubantop250Item as dbItem

class DoubanTop250Spider(Spider):
    name = 'douban'
    # start_urls = ["https://movie.douban.com/top250"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def start_requests(self):
        url = "https://movie.douban.com/top250"
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = dbItem()
        container = response.xpath('//ol[@class="grid_view"]/li')
        for movie in container:
            item["name"] = movie.xpath('.//div[@class="hd"]/a/span/text()').extract_first()
            item["ranking"] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item["score"] = movie.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            item["description"] = movie.xpath('.//span[@class="inq"]/text()').extract()[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = "https://movie.douban.com/top250" + next_url
            yield Request(next_url, headers=self.headers)