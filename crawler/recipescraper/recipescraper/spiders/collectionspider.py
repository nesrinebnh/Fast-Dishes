from gc import callbacks
import scrapy
from recipescraper.items import CollectionItem
from scrapy.loader import ItemLoader
import mysql.connector

def getCollectionUrls():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="scrapy_recipes"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM collections")

    myresult = mycursor.fetchall()

    l = []
    for x in myresult:
        l.append(x[1])
    
    return l

class CollectionSpider(scrapy.Spider):
    name = 'collection'
    start_urls = getCollectionUrls()
    
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
    
           
       
    