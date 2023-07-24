"""
VoxArticleScraper - A class for scraping and parsing article content from Vox.
"""
from __future__ import annotations

import re

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from news_api.Article import Article
from news_api.common.constants import BASE_URL
from news_api.common.log import get_logger

logger = get_logger(__name__)


class VoxArticleScraper:
    """
    A web scraper for Vox news articles.

    Attributes:
        base_url (str): The base URL of the Vox news website.
        articles_list (list[Article]): A list to store scraped Article objects.
        time_out (int) : request time out in seconds

    Methods:
        __init__(self) -> None:
            Initializes the VoxArticleScraper with the default base_url and sets up the HTTP adapter.

        get_articles(self) -> list[Article]:
            Scrapes the Vox website for article headlines and URLs, and populates the articles_list.
            Returns the list of Article objects.

        populate_articles(self) -> list[Article]:
            Populates additional attributes of Article objects by scraping individual article pages.
            Returns the updated articles_list.

        __get_label(self, label: Tag, Tag, article: Article) -> Union[str, None]:
            Helper method to extract and clean the article label from the HTML soup.

        __get_author_bio(self, about_the_author: Tag, article: Article) -> Union[str, None]:
            Helper method to extract and clean the author's biography from the HTML soup.
            Returns either the author's biography as a string or None if not found.

        __get_article_body(self, article_body: Tag) -> str:
            Helper method to extract and clean the article body text from the HTML soup.
            Removes any footer items and replaces multiple newlines with one newline.
        __get_article_datetime(self, article_datetime_string: Tag, article: Article) -> Union[str, None]:
            Helper method to extract return the article's datetime from the HTML soup.
            Returns either the article's datetime as a string or None if not found.
    """

    base_url: str = BASE_URL
    articles_list: list[Article] = []
    time_out: int = 30

    def __init__(self) -> None:
        """
        Initializes the VoxArticleScraper with the default base_url and sets up the HTTP adapter.
        """
        logger.info("initializing vox news scraper")
        # setup http adapter
        retry_strategy = Retry(total=5, status_forcelist=[429, 500, 502, 503, 504], backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)

    def get_articles(self) -> list[Article]:
        """
        Scrapes the Vox website for article headlines and URLs, and populates the articles_list.
        Returns the list of Article objects.

        Returns:
            list[Article]: The list of Article objects representing the scraped articles.
        """
        for i in range(1, 15):
            url = self.base_url + ("" if i == 1 else str(i))
            response = requests.get(url, timeout=self.time_out)
            soup = BeautifulSoup(response.content, "html.parser")
            entries = soup.find_all("div", class_="c-compact-river__entry")
            for entry in entries:
                text = entry.text.replace("\n", "")
                words = text.split()
                headline = " ".join(words)
                href = entry.find("a").get("href")
                self.articles_list.append(Article(headline, href))
        logger.debug("articles list len = %i", len(self.articles_list))
        return self.articles_list

    def populate_articles(self) -> list[Article]:
        """
        Populates additional attributes of Article objects by scraping individual article pages.
        Returns the updated articles_list.

        Returns:
            list[Article]: The list of Article objects with additional attributes populated.
        """
        logger.info("populating articles objects")
        for article in self.articles_list:
            logger.debug("getting article '%s'", article.headline)
            logger.debug("requesting url %s", article.url)
            response = requests.get(article.url, timeout=30)
            soup = BeautifulSoup(response.content, "html.parser")
            article_title = soup.find("h1", class_="c-page-title")
            # if the title isn't clear it's not an article but a collection of articles
            if not soup.find("h1", class_="c-page-title"):
                continue
            article.title = article_title.text
            article.label = self.__get_label(soup.find("div", class_="c-entry-group-labels"), article)
            article.subtitle = soup.find("p", class_="c-entry-summary p-dek").text
            article.author = soup.find("span", class_="c-byline__author-name").text
            article.about_the_author = self.__get_author_bio(
                soup.find("div", class_="c-short-author-bio-wrapper"), article
            )
            article.datetime_string = self.__get_article_datetime(soup.find("time", {"data-ui": "timestamp"}), article)
            article.article_body = self.__get_article_body(soup.find("div", class_="c-entry-content"))
        return self.articles_list

    def __get_label(self, label: Tag, article: Article) -> str | None:
        """
        Helper method to extract and clean the article label from the HTML soup.

        Args:
            label (Tag): The HTML tag containing the article label.
            article (Article): The Article object representing the article.

        Returns:
            Union[str, None]: The cleaned tag as a string, or None if not found.
        """
        if label:
            return " ".join(label.text.replace("\n", " ").replace("Filed under: ", "").split())
        logger.debug("no label found for article '%s', url:%s", article.headline, article.url)
        return None

    def __get_author_bio(self, about_the_author: Tag, article: Article) -> str | None:
        """
        Helper method to extract and clean the author's biography from the HTML soup.

        Args:
            about_the_author (Tag): The HTML tag containing the author's biography.
            article (Article): The Article object representing the article.

        Returns:
            Union[str, None]: The cleaned author's biography as a string, or None if not found.
        """
        if about_the_author:
            return " ".join(about_the_author.text.replace("\n", " ").split())
        logger.debug("no author bio found for article '%s', url:%s", article.headline, article.url)
        return None

    def __get_article_body(self, article_body: Tag) -> str:
        """
        Helper method to extract and clean the article body text from the HTML soup.
        Removes any footer items and replaces multiple newlines with one newline.

        Args:
            article_body (Tag): The HTML tag containing the article body.

        Returns:
            str: The cleaned article body text.
        """
        footer_item = article_body.find("div", class_="c-article-footer c-article-footer-cta")
        # Remove the footer_item from article_body
        if footer_item:
            footer_item.extract()
        # replace chained new lines with one new line
        return re.sub(r"\n+", "\n", article_body.text)

    def __get_article_datetime(self, article_datetime_string: Tag, article: Article) -> str | None:
        """
        Helper method to extracts datetime as string from the HTML soup.

        Args:
            article_datetime_string (Tag): The HTML tag containing the article's datetime.
            article (Article): The Article object representing the article.

        Returns:
            Union[str, None]: The datetime as a string, or None if not found.
        """
        if article_datetime_string:
            return str(article_datetime_string["datetime"])
        logger.debug("no datetime found for article '%s', url:%s", article.headline, article.url)
        return None
