import requests
import json
from bs4 import BeautifulSoup as bs

def get_data():

    query = 'nb~lenovo'
    response = requests.get(f'https://www.kufar.by/l/r~gomelskaya-obl/noutbuki').text

    with open('page.html', 'w', encoding='utf-8') as f:
        f.write(response)

    urls = []
    links = []

    soup = bs(response, 'html.parser')
    pages = soup.find_all('a', class_="styles_link__KajLs")
    print(pages)

def main():
        get_data()

if __name__ == '__main__':
    main()