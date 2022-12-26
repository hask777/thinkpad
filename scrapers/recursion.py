import requests
import json
from bs4 import BeautifulSoup as bs

main_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'

def get_first():
    url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
    response = requests.get(url).json()
    pages = response.get("pagination").get("pages")
    print(pages)


    with open(f'files/main.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)


def data_get(url):
    totals = []

    response = requests.get(url).json()

    pages = response.get("pagination").get("pages")[3].get("num")
    token = response.get("pagination").get("pages")[2].get("token")

    #  we need function thst get url and return the nxt page token
    #  then we add this token to the url, to get ne token
    def get_token(token):
        next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
        pagination = next_page.get("pagination").get("pages")
        print(pagination)

        for page in pagination:
            if page["label"] == 'self':
                num = page["num"]
            # print(page['label'])
            if page['label'] == 'next':
                token = page['token']
                

                next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
                totals.append(next_page)

                with open(f'files/page{num}.json', 'w', encoding='utf-8') as f:
                    json.dump(next_page, f, indent=4, ensure_ascii=False)

        return get_token(token) 

    get_token(token)

def main():
    get_first()
    # data_get(main_url)

if __name__ == '__main__':
    main()