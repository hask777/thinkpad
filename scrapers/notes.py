import requests
import json
from bs4 import BeautifulSoup as bs

def get_data():
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=utf-8'}
    url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
    response = requests.get(url,  headers=headers).text

    arr = json.loads(response)

    with open('files/page.json', 'w', encoding='utf-8') as f:
        json.dump(arr, f, indent=4, ensure_ascii=False)

    with open('files/page.json', 'r', encoding='utf-8')  as f:
        items = json.load(f) 

    print(items["pagination"]["pages"][0])
    print(items["pagination"]["pages"][1])
    print(items["pagination"]["pages"][2]["token"])
    print(items["pagination"]["pages"][3]["num"])

    for i in range(1, items["pagination"]["pages"][3]["num"] + 1):
        token = items["pagination"]["pages"][2]["token"]
        url = f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'

        page_url = requests.get(url)
        print(url)

    # for item in items:
    #     print(item)

    urls = []
    links = []

    soup = bs(response, 'html.parser')
    pages = soup.find_all('a', class_="styles_link__KajLs")
    print(pages)

def main():
        get_data()

if __name__ == '__main__':
    main()