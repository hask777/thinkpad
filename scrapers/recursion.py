import requests
import json
from bs4 import BeautifulSoup as bs

first_url = 'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d'

def data_get(url):
    response = requests.get(url).json()
    pagination = response.get("pagination").get("pages")
    count = 2
    totals = []

    for page in pagination:
        if page["label"] == 'self':
            num = page["num"]
            response = requests.get(url).json()
            for item in response['ads']:
                totals.append(item)

            # with open(f'files/page{num}.json', 'w', encoding='utf-8') as f:
            #     json.dump(response, f, indent=4, ensure_ascii=False)
            
        if page['label'] == 'next':
            token = page['token']
            print(token)

    next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
    pages = next_page.get("pagination").get("pages")[3]["num"]
    print(pages)
    for item in next_page['ads']:
        totals.append(item)

    # with open(f'files/page{count}.json', 'w', encoding='utf-8') as f:
    #     json.dump(next_page, f, indent=4, ensure_ascii=False)


    def get_token(token, count):
        print(token)
        count += 1
        next_page = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
        pagination = next_page.get("pagination").get("pages")
        for item in next_page['ads']:
            totals.append(item)

        # with open(f'files/page{count}.json', 'w', encoding='utf-8') as f:
        #     json.dump(next_page, f, indent=4, ensure_ascii=False)
        # print(pagination)

        for page in pagination:

            if page['label'] == 'next':
                token = page['token']
           
            next_pages = requests.get(f'https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?cat=16040&cursor={token}&lang=ru&prn=16000&rgn=2&size=42&sort=lst.d').json()
            totals.append(next_pages['ads'])
            for item in next_pages['ads']:
                 totals.append(item)

            # with open(f'files/page{count}.json', 'w', encoding='utf-8') as f:
            #     json.dump(next_pages, f, indent=4, ensure_ascii=False)

        with open(f'files/totals.json', 'w', encoding='utf-8') as f:
            json.dump(totals, f, indent=4, ensure_ascii=False)

  
        if count == pages + 1:
            return

        return get_token(token, count) 

    get_token(token, count)

def main():
    data_get(first_url)
    # data_get(second_url)
    # data_get(third_url)

if __name__ == '__main__':
    main()