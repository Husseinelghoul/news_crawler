import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

response = requests.get("https://www.vox.com/unexplainable/2023/7/15/23793840/chat-gpt-ai-science-mystery-unexplainable-podcast")
soup = BeautifulSoup(response.content, "html.parser")
label = soup.find("div", class_="c-entry-group-labels")
breakpoint()