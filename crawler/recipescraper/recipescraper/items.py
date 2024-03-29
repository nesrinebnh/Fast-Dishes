# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import imp
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def parse_Level(level):
    level = level.replace(' mins ', '')
    duration  = level
    if 'hrs' in level:
        l = level.split('hrs')
        print("\n\nlist", l)
        l = [element for element in l if element and element != ' ']
        l = [int(element.strip()) for element in l]
        
        print("\n\n")
        if len(l) == 2:
            duration = l[0]*60 + l[1]
        elif len(l) == 1:
            duration  = l[0]*60
    return str(duration)

def parseSpecial(text):
    text = text.replace('\u2018', "'")
    text = text.replace("\u2019", "'")
    text = text.replace("&amp;", "&")
    text = text.replace("\u2013", "-")
    return text

class RecipescraperItem(scrapy.Item):
    # define the fields for your item here like:
    
    title = scrapy.Field(input_processor = MapCompose(remove_tags,parseSpecial), output_processor=TakeFirst())
    description = scrapy.Field(input_processor = MapCompose(remove_tags,parseSpecial), output_processor=TakeFirst())
    url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    image_url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    level= scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    duration = scrapy.Field(input_processor = MapCompose(remove_tags, parse_Level), output_processor=TakeFirst())
    
class CollectionItem(scrapy.Item):
    url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())