#titles = response.xpath('//*/header/h4/a/text()').getall()
#descriptions = response.xpath('//*/li/article/div/p/text()').getall()
#urls = response.xpath('//*/header/h4/a/@href').getall()
#img_url = response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-4"]/div[@class="img-holder"]/img/@src').get()
#level = response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[2]/span[@class="text"]/text()').get()
#duration = response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[1]/span/text()[3]').get().replace(' mins ', '')

from gc import callbacks
import scrapy
from recipescraper.items import RecipescraperItem
from scrapy.loader import ItemLoader

class RecipeSpider(scrapy.Spider):
    name = 'recipe'
    start_urls = ['https://www.bbcgoodfoodme.com/collections/cheap-family-suppers/']
    
    def parse(self, response):
        
        for recipes in response.xpath('//*/div[@class="entry-content"]'):
            I = ItemLoader(item=RecipescraperItem(), selector=recipes)
            
            I.add_xpath('title', 'header/h4/a')
            I.add_xpath('description', 'p')
            I.add_xpath('url', 'header/h4/a/@href')
            url = recipes.xpath('header/h4/a/@href').getall()[0]
            print('=============================')
            print(url)
            print('==============================')
            #yield response.follow(author_url, self.parse_author, meta={'quote_item': quote_item})
            # yield I.load_item()
            recipeItem = I.load_item()
            yield response.follow(url, self.parseDetail, meta={'recipe_item': recipeItem})
            
        next_page = response.xpath('//*/main/div[@class="pagination"]/ol/li/a[@class="next"]/@href').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parseDetail(self, response):
        recipe_item = response.meta['recipe_item']
        loader = ItemLoader(item=recipe_item, response=response)
        # print('============================')
        # print('image url', response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-4"]/div[@class="img-holder"]/img/@src').get())
        # print('level', response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[2]/span[@class="text"]/text()').get())
        # print('duration', response.xpath('//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[1]/span/text()[3]').get())
        # print('===========================')
        loader.add_xpath('image_url', '//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-4"]/div[@class="img-holder"]/img/@src')
        loader.add_xpath('level', '//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[2]/span[@class="text"]')
        loader.add_xpath('duration','//*[@id="main"]/div[@class="recipe-head-container"]/div[@class="row remove_margin"]/div[@class="col-md-8"]/div[@class="preparation"]/ul/li[1]/span/text()[3]')
        yield loader.load_item()