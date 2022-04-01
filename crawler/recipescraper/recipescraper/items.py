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
    l = level.split('hrs')
    l = [int(element.strip()) for element in l]
    duration  = level
    if len(l) > 0:
        duration = l[0]*60 + l[1]
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