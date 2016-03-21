import scrapy
import re, json
import pdb

from scrapper.pipelines import *

class uniqloSpider(scrapy.Spider):
    name = 'uniqlo_spider'
    allow_domains = ["http://www.uniqlo.com/us/"]
    start_urls = [
        "http://www.uniqlo.com/us/men/dress-shirts.html"
    ]

    pipeline = set([
        uniqloPipeline
    ])

    def parse(self, response):
        item_list = response.css('.product-tile-component')
        for item in item_list:
            link = item.css('a::attr(href)').extract()[0]
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_item)
            yield request


    def parse_item(self, response):
        product_dict = dict()
        product_dict['category'] = response.css('.breadcrumb-item')[2].css('a::text').extract()
        product_dict['name'] = response.css('.pdp-title-rating').css('h1::text').extract()
        product_dict['brand'] = 'Uniqlo'
        product_dict['product_url'] = response.url
        product_dict['img_url'] = response.css('.pdp-image-main-image').css('img::attr(src)').extract()[0]
        product_dict['discounted_price'] = response.css('.pdp-price-current')[0].css('p::text').extract()

        yield product_dict