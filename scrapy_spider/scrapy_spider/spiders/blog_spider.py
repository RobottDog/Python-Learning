from scrapy.spiders import Spider

class BlogSpider(Spider):
    name = 'robottdog'
    start_urls = ['http://robottdog.com']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title)