import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://pikabu.ru/tag/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%8E%D0%BC%D0%BE%D1%80/best?n=4"

response = requests.get(URL_TEMPLATE)

soup = bs(response.text, "lxml")

data = soup.find('article', class_='story story_exp-unit story_exp-unit_c')

name = data.find('h2', class_='story__title-link story__title-link_visited')

print(data)