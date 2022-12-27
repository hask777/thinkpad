import requests
import json
from bs4 import BeautifulSoup as bs

first_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
second_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
third_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6M30=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'

def get_first(url):
    # url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
    url = first_url
    response = requests.get(url).json()
    pages = response.get("pagination").get("pages")
    print(pages)


    with open(f'files/first.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

    url = second_url
    response = requests.get(url).json()
    pages = response.get("pagination").get("pages")
    print(pages)

    with open(f'files/second.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

    url = third_url
    response = requests.get(url).json()
    pages = response.get("pagination").get("pages")
    print(pages)

    with open(f'files/third.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

get_first(first_url)
get_first(second_url)
get_first(third_url)