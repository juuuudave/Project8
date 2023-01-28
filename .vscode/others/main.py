import requests
import scrapy

# url de la page visé
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# print le code html source
print(page.content)
