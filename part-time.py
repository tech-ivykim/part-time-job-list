import requests
from bs4 import BeautifulSoup

all_url = "http://www.alba.co.kr/"
all_page = requests.get(all_url)
all_soup = BeautifulSoup(all_page.text, "html.parser")

print(all_soup)