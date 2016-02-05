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
    description = scrapy.Field()
    product_url = scrapy.Field()
    img_url = scrapy.Field()
    brand = scrapy.Field()

    #These fields should be put into the db manually. One entry per brand.
    #fit_neck = scrapy.Field()
    #fit_chest = scrapy.Field()
    #fit_arm = scrapy.Field()

    #Not sure if needed
    gender = scrapy.Field()
    cotton = scrapy.Field()

    #Different types of shirts
    #t_shirt    
    #graphic_tee
    #long_sleeve
    #polo
    #dress_shirt
    shirt_type = scrapy.Field()    

    #Attributes to be provided from image rec
    #colours = scrapy.Field()
    #complexity = scrapy.Field()
