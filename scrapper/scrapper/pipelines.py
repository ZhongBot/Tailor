# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pdb
import pymongo

from scrapy import log
from scrapy.exceptions import DropItem
from scrapper.model.top import topItem
from scrapper.spiders.base import check_spider_pipeline
from scrapper.config.db_config import connect_to_mongo, disconnect_from_mongo

class americanEaglePipeline(object):
    collection_name = 'tops'

    def open_spider(self, spider):
        self.db = connect_to_mongo()

    def close_spider(self, spider):
        disconnect_from_mongo(self.db)

    @check_spider_pipeline
    def process_item(self, item, spider):
        category = item['category']
        products = item['products']
        img_url_template = "pics.ae.com/is/image/aeo/%s_of?fit=crop&wid=450&hei=504&qlt=50,0"
        entry = topItem()
        for pid, info in products:
        #Extract the variation data and then remove from original dict
            variations = [vari[1] for vari in info['colorImageSelectionData'].items()]
            entry.category = category
            entry.name = info.get('prdName')
            #entry.colors = []
            entry.brand = info.get('brandName')
            entry.full_price = info.get('listPrice')
            entry.discounted_price = info.get('salePrice')
            #entry.complexity =

            for variation in variations:
                cpid = variation.get('colorPrdId')
                entry.color_name = variation.get('colorName')
                entry.img_url = img_url_template % cpid
                entry.product_url = item.get('product_url').replace('category.jsp?', 'product_details.jsp?productId=%s&'%(cpid))
                self.db[self.collection_name].insert(entry.to_dict())

class hollisterPipeline(object):
    collection_name = 'tops'
    def open_spider(self, spider):
        self.db = connect_to_mongo()

    def close_spider(self, spider):
        disconnect_from_mongo(self.db)

    @check_spider_pipeline
    def process_item(self, item, spider):
        entry = topItem()
        for prod in item['products']:
            entry.category  = item['category']
            entry.name = prod.get('name')
            entry.brand = prod.get('brand')
            entry.full_price = prod.get('full_price')
            entry.discounted_price = prod.get('discounted_price')
            #entry.color_name =
            entry.img_url = prod.get('img_url')
            entry.product_url = prod.get('product_url')
            self.db[self.collection_name].insert(entry.to_dict())

class hmPipeline(object):
    collection_name = 'tops'

    def open_spider(self, spider):
        self.db = connect_to_mongo()

    def close_spider(self, spider):
        disconnect_from_mongo(self.db)

    @check_spider_pipeline
    def process_item(self, item, spider):
        entry = topItem()
        entry.category = item['category']
        entry.name = item['name']
        entry.brand = item['brand']
        entry.full_price = item['full_price']
        entry.img_url = item['img_url']
        entry.product_url = item['product_url']
        self.db[self.collection_name].insert(entry.to_dict())


class uniqloPipeline(object):
    collection_name = 'tops'

    def open_spider(self, spider):
        self.db = connect_to_mongo()

    def close_spider(self, spider):
        disconnect_from_mongo(self.db)

    @check_spider_pipeline
    def process_item(self, item, spider):
        entry = topItem()
        entry.category = item['category']
        entry.name = item['name']
        entry.brand = item['brand']
        entry.discounted_price = item['discounted_price']
        entry.img_url = item['img_url']
        entry.product_url = item['product_url']
        self.db[self.collection_name].insert(entry.to_dict())