import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print('Request response: ', page.status_code)
print('Web page html: ')
print( page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print('Soup : ', soup.prettify())
print('Children : ', list(soup.children))