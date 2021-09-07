import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print('Request response: ', page.status_code)
print('Web page html: ')
print( page.content)

