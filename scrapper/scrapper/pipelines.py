# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pdb
import pymongo

class clothingPipeline(object):
    collection_name = 'tops'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri='mongodb://127.0.0.1/Tailor',
            mongo_db='Tailor'
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        category = item['category']
        products = item['products']
        for pid, info in products:
            #Extract the variation data and then remove from original dict
            variations = [vari[1] for vari in info['colorImageSelectionData'].items()]
            del info['colorImageSelectionData']
            del info['classId']
            del info['bundleCatId']
            del info['defaultURL']
            del info['hasBundle']
            del info['contextRoot']
            del info['isHazMat']
            for variation in variations:
                entry = dict(info)
                entry['category'] = category
                entry['prd_id'] = pid
                del variation['imgViews']
                entry.update(variation)
                self.db[self.collection_name].insert(entry)
