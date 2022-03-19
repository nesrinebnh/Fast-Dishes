# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import imp
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class RecipescraperItem(scrapy.Item):
    # define the fields for your item here like:
    
    title = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    description = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    
    
    pass
