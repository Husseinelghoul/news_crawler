#  News Crawler

The News Crawler is a sophisticated application designed to extract news articles from the [Vox news website](vox.com/news) using the powerful web scraping library, [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). The application performs data cleansing on the obtained articles to extract relevant information such as theheadline, URL, label, title, subtitle, author, author bio, datetime, and article body. By removing ads, footers, and unnecessary HTML elements, the data is made easily readable.

The primary objective of this application is to store the cleansed news data into a hosted [MongoDB](https://www.mongodb.com/cloud/atlas/register) database, enabling seamless search and retrieval operations. In addition to the database functionality, the application also deploys an API that provides users with convenient access to the content stored within the MongoDB database. Users can perform keyword-based searches, and if the provided keyword matches any headlines, the relevant articles will be returned through the API.

## Project Composition

The Vox News Crawler is composed of three essential parts:

1. **BeautifulSoup Scraper**: This module, located at [GitHub link](https://github.com/Husseinelghoul/news_crawler/blob/master/news_api/VoxArticleScraper.py), is responsible for crawling the Vox news website using beautifulsoup4 to extract the desired news articles.

2. **Mongo DB Database**: The MongoDB database module, accessible at [GitHub link](https://github.com/Husseinelghoul/news_crawler/blob/master/news_api/MongoClient.py), manages the storage of cleansed news data retrieved by the scraper.

3. **API**: The API module, located at [GitHub link](https://github.com/Husseinelghoul/news_crawler/blob/master/api.py), facilitates searching through the MongoDB database and presenting the results to users.

## How to Run the Application

To utilize the News Crawler and access the news articles from the Vox website, follow these steps:

1. Clone the repository to your local machine using the following command:
   ```
   git clone git@github.com:Husseinelghoul/news_crawler.git
   ```

2. Install the required dependencies by executing the following command:
   ```
   pip install -r requirements.txt
   ```

3. Create a MongoDB database and obtain the connection URL.

4. Create a new file named `.env` based on the provided `.env.example`, and populate it with the required configuration settings.

5. Choose one of the following options to run the application:

   a. To run the entire process, including firing up the scraper, loading data into the database, and running the API, execute the following command:
      ```
      python -m news_crawler
      ```

   b. If you have already populated the database and only want to run the API, use the following command:
      ```
      python api.py
      ```

6. To search for articles based on a specific keyword, use [Postman](https://www.postman.com) or any other API platform. Send a GET request to the API with the following URL, replacing `<host>` with `localhost` and `<port-number>` with `5500` to use the default configurations. Additionally, replace `<keyword>` with a keyword of your choice:
   ```
   GET http://<host>:<port-number>/articles/<keyword>
   ```

By following these steps, you will be able to efficiently utilize the  News Crawler to access and search for the latest news articles from Vox.com, all powered by the robustness of beautifulsoup4 and MongoDB.
## Linting and Typing
This project uses [flake8](https://www.flake8rules.com), [pylint](https://pylint.pycqa.org/en/latest/) and [black](https://github.com/psf/black) to check the code base against coding style ([PEP8](https://peps.python.org/pep-0008/)) , and [mypy](https://mypy-lang.org) which is a static type checker for Python.
To check the typing and linting use the following commands:
**Typing**
```
python -m mypy news_api --no-namespace-packages
```
**Linting**
black
```
black  --check  news_api
```
flake8
```
flake8p news_api
```
pylint
```
pylint news_api
```
## Areas of Improvements
We could use [Selenium](https://selenium-python.readthedocs.io/index.html) to click on the `Load More` button to scrape the data from the [monthly archive](https://www.vox.com/archives/2023/4) instead of the [recent archives](https://www.vox.com/news).

## Potential Issues
* Using `5000` port on mac wouldn’t work because of [this issue](https://medium.com/pythonistas/port-5000-already-in-use-macos-monterey-issue-d86b02edd36c)
* MongoDB [certificate verify failed: unable to get local issuer certificate](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)
