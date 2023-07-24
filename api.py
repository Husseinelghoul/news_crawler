"""
A file to use only the API without going through the scraping and storing
"""
import flask

from news_api.common.constants import (
    DATABASE_NAME,
    FLASK_HOST,
    FLASK_PORT,
    MONGODB_CONNECTION_STRING,
)
from news_api.common.log import get_logger
from news_api.MongoClient import MongoClient

logger = get_logger(__name__)

logger.info("Initializing application")

# Initialize mongo client
mongo_client = MongoClient(MONGODB_CONNECTION_STRING, DATABASE_NAME, "articles")

# Initialize flask app
app = flask.Flask(__name__)
logger.info("API ready to go!")


# Defining flask function
@app.route("/articles/<keyword>", methods=["GET"])
def get_articles(keyword):
    """
    Flask method to search articles from mongoDB by keyword
    """
    results = mongo_client.search_articles(keyword)
    return results


app.run(host=FLASK_HOST, port=FLASK_PORT)

logger.info("program finished running successfully")
