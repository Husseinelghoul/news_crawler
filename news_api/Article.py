"""
article.py - Defines the Article class for representing news articles.
"""
from __future__ import annotations

import hashlib


class Article:
    """
    Represents a news article.

    Attributes:
        id (str): The unique identifier for the article, generated based on the hash of the URL.
        headline (str): The main headline of the article.
        url (str): The URL of the article.
        label (str | None): The label/category of the article (default is None).
        title (str | None): The title of the article (default is None).
        subtitle (str | None): A subheading or additional information about the article (default is None).
        author (str | None): The author of the article (default is None).
        about_the_author (str | None): Information about the author's background and expertise (default is None).
        datetime_string (str | None): The date and time of the article in string format (default is None).
        article_body (str | None): The main content/body of the article (default is None).

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

    id: str
    headline: str
    url: str
    label: str | None
    title: str | None
    subtitle: str | None
    author: str | None
    about_the_author: str | None
    datetime_string: str | None
    article_body: str | None

    def __init__(self, headline: str, url: str) -> None:
        """
        Initializes an Article object with the provided headline and URL.
        The unique ID for the article is generated based on the hash of the URL.

        Args:
            headline (str): The main headline of the article.
            url (str): The URL of the article.
        """
        hash_object = hashlib.sha1(url.encode("utf-8"))
        self.id = str(hash_object.hexdigest())
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
