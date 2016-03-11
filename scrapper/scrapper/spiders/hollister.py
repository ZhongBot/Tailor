import scrapy
import re, json
import pdb

from scrapper.pipelines import *

class hollisterSpider(scrapy.Spider):
    name = 'hollister_spider'
    allow_domains = ["hollisterco.ca/shop/ca"]
    start_urls = [
        "http://www.hollisterco.ca/shop/ca/guys-tops"        
    ]
    
    pipeline = set([
        hollisterPipeline
    ])
    
    def parse(self, response):
        # Extract the subcategory names and link from the male top page
        res = response.css('.current').css('ul').css('li')
        for sub_cat in res:
            link = sub_cat.css('a::attr(href)').extract()[0]
            category = sub_cat.css('a::text').extract()[0]
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_category)
            request.meta['category'] = [category]
            yield request

    def parse_category(self, response):
        res = response.css('.selected')
        #Holister's website has two types of subcategories, one which has a further list of subcategory
        #the other does not. If len(res) > 1 means there is no sub category
        sub_category = res.css('.tertiary')
        if sub_category and not sub_category.css('li').css('.current'):
            res = sub_category.css('li')
            for sub_cat in res:
                link = sub_cat.css('a::attr(href)').extract()[0]
                category = sub_cat.css('a::text').extract()[0]
                url = response.urljoin(link)
                request = scrapy.Request(url, callback=self.parse_category)
                request.meta['category'] = response.meta['category'] + [category]
                yield request
        #Retrieve the products
        res = response.css('.grid-product')
        
        result_dict = dict()
        result_dict['category'] = response.meta['category']
        result_dict['products'] = []       

        for product in res:
            product_dict = dict()
            product_info = product.css('.grid-product__info')
            product_dict['name'] = product_info.css('.grid-product__name::text').extract()[0]
            product_dict['brand'] = 'hollister'
            product_dict['product_url'] = product_info.css('.grid-product__name').css('a::attr(href)').extract()[0]
            product_dict['img_url'] = product.css('img::attr(src)').extract()[0]
            product_dict['full_price'] = get_price(product.css('.product-price-v2__price--list::text').extract())
            product_dict['discounted_price'] = get_price(product.css('.product-price-v2__price--offer::text').extract())
            #product_dict['complexity']
            #product_dict['color_name']
            #product_dict['colors']
            #product_dict['category']
            result_dict['products'].append(product_dict)
        yield result_dict

def get_price(raw_price):
    if len(raw_price) == 0:
        return ''
    res = raw_price[0].strip()
    return res.replace(u'\xa0', u' ')

