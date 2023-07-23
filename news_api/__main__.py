from news_api.common.log import get_logger
from news_api.VoxArticleScraper import VoxArticleScraper

logger = get_logger(__name__)

logger.info("initializing application")
my_scraper = VoxArticleScraper()
# getting articles list from archive
articles_list = my_scraper.get_articles()
# populating articles objects with propper attributes
articles = my_scraper.populate_articles()
logger.info("program finished running successfully")
