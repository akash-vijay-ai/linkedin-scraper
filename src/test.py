from scraper import LinkedinScraper
import requests
from lxml.html import fromstring

url = "https://www.linkedin.com/pulse/how-publish-content-linkedin-pulse-hamza-sarfraz/"

response = requests.get(url)

scraper =  LinkedinScraper(response_text=response.text, url=url)

print(scraper.extract_data())
