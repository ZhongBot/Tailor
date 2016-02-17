import scrapy
import pdb
import re, json

from scrapper.pipelines import *

class americanEagleSpider(scrapy.Spider):
    name = 'american_eagle_spider'
    allowed_domains = ["ae.com"]
    start_urls = [
        "https://www.ae.com/web/browse/category.jsp?catId=cat10025&navdetail=mega:men:c2:p1"
    ]
    pipeline = set([
        americanEaglePipeline
    ])    

    def parse(self, response):
        # Extract the subcategory names and link from the male top page
        res = response.css('.navHeader').css('.menu')[0]
        links = res.css('a::attr(href)').extract()
        categories = res.css('span::text').extract()
        for i, link in enumerate(links):
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_category)
            request.meta['category'] = categories[i]
            yield request

    def parse_category(self, response):
        category = response.meta['category']
        res = response.css('.navHeader').css('.menu')[0]
        detail = res.css('.%s'%(category))
        sub_cat_links = detail.css('a::attr(href)').extract()
        sub_categories = detail.css('span::text').extract()
        for i, sl in enumerate(sub_cat_links):
            url = response.urljoin(sl)
            request = scrapy.Request(url, callback=self.parse_detailed_category)
            request.meta['category'] = [category, sub_categories[i]]
            yield request

    def parse_detailed_category(self, response):
        data_json = re.search('category_json = ({.*})', response.body).group(1)
        data = json.loads(data_json)
        #Image can be retrieved by using colorPrdId such as '2154_9171_767' and going to pics.ae.com/is/image/aeo/{{colorPrdId}}_of?fit=crop&wid=450&hei=504&qlt=50,0
        res = dict()
        res['category'] = response.meta['category']
        res['products'] = data['availablePrds'].items()
        res['product_url'] = response.url
        yield res
