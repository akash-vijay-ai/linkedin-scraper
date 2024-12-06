from scraper import LinkedinScraper
import requests
from lxml.html import fromstring

url = "https://www.linkedin.com/posts/poonam-soni-9255931b2_jobpreparation-remotejobs-websites-activity-7270398477816205312-o4ql?utm_source=share&utm_medium=member_desktop"

response = requests.get(url)

with open("test.html", "wb") as f:
    f.write(response.content)

scraper =  LinkedinScraper(response_text=response.text, url=url)

print(scraper.extract_data())
