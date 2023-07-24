"""
The brain of the program, where the magic happens
"""
from news_api.common.constants import DATABASE_NAME, MONGODB_CONNECTION_STRING
from news_api.common.log import get_logger
from news_api.MongoClient import MongoClient
from news_api.VoxArticleScraper import VoxArticleScraper

logger = get_logger(__name__)

logger.info("Initializing application")
my_scraper = VoxArticleScraper()
# Get articles list from archive
articles_list = my_scraper.get_articles()
# Populate articles objects with propper attributes
articles = my_scraper.populate_articles()
# Initialize mongo client
mongo_client = MongoClient(MONGODB_CONNECTION_STRING, DATABASE_NAME, "articles")
# Insert new articles
mongo_client.insert_articles(articles)
logger.info("program finished running successfully")
