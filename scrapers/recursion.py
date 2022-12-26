import requests
import json
from bs4 import BeautifulSoup as bs

main_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'

def data_get(url):
    response = requests.get(url).json()
    totals = []
    pages = response.get("pagination").get("pages")[3].get("num")
    token = response.get("pagination").get("pages")[2].get("token")
    print(token)

    url = f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'
    count = 0

    #  we need function thst get url and return the nxt page token
    #  then we add this token to the url, to get ne token
    def get_token(token, count):
        count += 1
        next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
        pagination = next_page.get("pagination").get("pages")

        for page in pagination:
            # print(page['label'])
            if page['label'] == 'next':
                token = page['token']
                print(token)

                next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
                totals.append(next_page)

                with open(f'files/page{count}.json', 'w', encoding='utf-8') as f:
                    json.dump(next_page, f, indent=4, ensure_ascii=False)

                if token is None:
                    return  

        return get_token(token, count) 

    get_token(token, count)

def main():
    data_get(main_url)

if __name__ == '__main__':
    main()