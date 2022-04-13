# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from recipescraper.models import Recipe, db_connect, create_table 


class RecipescraperPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save recipes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        recipe = Recipe()
        recipe.title = item["title"]
        recipe.description = item['description']
        recipe.url = item['url']
        recipe.image_url = item['image_url']
        recipe.level = item['level']
        recipe.duration = item['duration']
      

        try:
            session.add(recipe)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item