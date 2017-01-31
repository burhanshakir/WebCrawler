import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://thenewboston.com/forum/category.php?id=10&orderby=recent&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all('a', {'class': 'user-name'}):
            href = link.get('href')
            user = link.string
            # print(href)
            # print(user)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.find_all('td', {'class': 'second-column'}):
        print(item_name.string)
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)

trade_spider(1)