from gc import callbacks
import scrapy
from recipescraper.items import CollectionItem
from scrapy.loader import ItemLoader




class CollectionSpider(scrapy.Spider):
    name = 'collection'
    start_urls = [
                  'https://www.bbcgoodfoodme.com/collections/',
                  ]
    
    def parse(self, response):
        for collection in response.xpath('//*[@id="main"]/div[1]/ul/li'):
            print(collection.xpath('div/a/@href').get())
            
            I = ItemLoader(item=CollectionItem(), selector=collection)
            I.add_xpath('url', 'div/a/@href')
            yield I.load_item()
        next_page = response.xpath('//*/main/div[@class="pagination"]/ol/li/a[@class="next"]/@href').get()
        
        if next_page is not None:
            print("url next",next_page)
            yield response.follow(next_page, callback=self.parse)
    
           
       
    