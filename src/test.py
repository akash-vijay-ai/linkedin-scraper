from scraper import LinkedinScraper
import requests
from lxml.html import fromstring

url = "https://www.linkedin.com/posts/nehageo_internship-designintern-figma-activity-7222580242261979136-pAYx?utm_source=share&utm_medium=member_desktop"

response = requests.get(url)

with open("test.html", "wb") as f:
    f.write(response.content)

scraper =  LinkedinScraper(response_text=response.text, url=url)

print(scraper.extract_data())
