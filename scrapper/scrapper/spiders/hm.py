import scrapy
import re, json
import pdb

from scrapper.pipelines import *

class hmSpider(scrapy.Spider):
    name = 'hm_spider'
    allow_domains = ["http://www.hm.com/ca/"]
    start_urls = [
        "http://www.hm.com/ca/subdepartment/MEN?Nr=4294927065#Nr=4294927065",
        "http://www.hm.com/ca/subdepartment/MEN?Nr=4294927065#Nr=4294956362"
    ]

    pipeline = set([
        hmPipeline
    ])

    def parse(self, response):
        item_list = response.css('.products')[0].css('.has-secondary-image')
        for item in item_list:
            link = item.css('a::attr(href)').extract()[0]
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_item)
            yield request


    def parse_item(self, response):
        product_dict = dict()
        product_dict['category'] = response.css('.breadcrumbs').css('a::text').extract()[3]
        product_dict['name'] = response.css('h1')[1].css('h1::text').extract()[0].strip()
        product_dict['brand'] = 'H&M'
        product_dict['product_url'] = response.url
        product_dict['img_url'] = response.css('img::attr(src)').extract()[3]
        product_dict['full_price'] = response.css('.price').css('span')[1].css('.actual-price::text').extract()
        yield product_dict

