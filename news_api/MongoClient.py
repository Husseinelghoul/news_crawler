"""
MongoClient.py

This file contains the MongoClient class. The MongoClient class is responsible for connecting
to a MongoDB database and storing articles in the database.

Classes:
    MongoClient: The MongoClient class.

Functions:
    __init__: The constructor for the MongoClient class.
    insert_articles: The function that stores articles in the database.

"""

import pymongo

from news_api.Article import Article
from news_api.common.log import get_logger

logger = get_logger(__name__)


class MongoClient:
    """
    The MongoClient class.

    Attributes:
        connection_string: The connection string to the MongoDB database.
        client: The MongoClient object.
        database: The database object.
        collection: The collection object.

    Methods:
        __init__: The constructor for the MongoClient class.
        insert_articles: The function that stores articles in the database.

    """

    connection_string: str
    client: pymongo.mongo_client.MongoClient
    database: pymongo.database.Database
    collection: pymongo.collection.Collection

    def __init__(self, url: str, database: str, collection: str) -> None:
        """
        The constructor for the MongoClient class.

        Args:
            url: The connection string to the MongoDB database.
            database: The name of the database.
            collection: The name of the collection.

        """

        self.connection_string = url
        self.client = pymongo.MongoClient(url)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def insert_articles(self, articles: list[Article]) -> None:
        """
        The function that stores articles in the database. Taking into considerations
        articles that are already there

        Args:
            articles: The list of articles to be stored in the database.

        """

        # Loop through the list of articles
        for article in articles:
            # Check if the object already exists in the database
            document = self.collection.find_one({"id": article.id})
            # If the object does not exist, insert it into the database
            if document is None:
                logger.debug("inserting article id %s", article.id)
                self.collection.insert_one(article.__dict__)
            else:
                logger.debug("article id %s already present", article.id)
