"""
article.py - Defines the Article class for representing news articles.
"""
import hashlib


class Article:
    """
    Represents a news article.

    Attributes:
        id (int): The unique identifier for the article, generated based on the hash of the URL.
        headline (str): The main headline of the article.
        url (str): The URL of the article.
        label (Optional[str]): The label/category of the article (default is None).
        title (Optional[str]): The title of the article (default is None).
        subtitle (Optional[str]): A subheading or additional information about the article (default is None).
        author (Optional[str]): The author of the article (default is None).
        about_the_author (Optional[str]): Information about the author's background and expertise (default is None).
        datetime_string (Optional[str]): The date and time of the article in string format (default is None).
        article_body (Optional[str]): The main content/body of the article (default is None).

    Methods:
        __init__(self, headline: str, url: str) -> None:
            Initializes an Article object with the provided headline and URL.
            The unique ID for the article is generated based on the hash of the URL.

        __str__(self) -> str:
            Returns the string representation of the Article object.
            The string representation is the headline of the article.

        __repr__(self) -> str:
            Returns the official string representation of the Article object.
            The official representation is the headline of the article.
    """

    def __init__(self, headline: str, url: str) -> None:
        """
        Initializes an Article object with the provided headline and URL.
        The unique ID for the article is generated based on the hash of the URL.

        Args:
            headline (str): The main headline of the article.
            url (str): The URL of the article.
        """
        hash_object = hashlib.sha1(url.encode("utf-8"))
        self.id = int(hash_object.hexdigest(), 16)
        self.headline = headline
        self.url = url

    def __str__(self) -> str:
        """
        Returns the string representation of the Article object.

        Returns:
            str: The headline of the article.
        """
        return self.headline

    def __repr__(self) -> str:
        """
        Returns the official string representation of the Article object.

        Returns:
            str: The headline of the article.
        """
        return self.headline
