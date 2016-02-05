# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class menTop(scrapy.Item):
    #Attributes to scrap
    name = scrapy.Field()
    price = scrapy.Field()
    fit_neck = scrapy.Field()
    fit_chest = scrapy.Field()
    fit_arm = scrapy.Field()

    #Not sure if needed
    gender = scrapy.Field()
    cotton = scrapy.Field()

    #Boolean fields indicating if the shirt belongs in the category
    t_shirt = scrapy.Field()    
    graphic_tee = scrapy.Field()
    long_sleeve = scrapy.Field()
    polo = scrapy.Field()
    dress_shirt = scrapy.Field()    

    #Attributes to be provided from image rec
    #colours = scrapy.Field()
    #complexity = scrapy.Field()
