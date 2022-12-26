import requests
import json
# import lxml
from bs4 import BeautifulSoup as bs

def get_data():

    query = 'nb~lenovo'
    response = requests.get(f'https://www.kufar.by/l/r~gomelskaya-obl/noutbuki').text

    items_arr = []
    links = []

    soup = bs(response)
    items = soup.find_all('a', class_='styles_wrapper__pb4qU')
    for item in items:
        link = item.get('href')
        # links.append(link)
        # for l in links:
        #     # print(l)
        #     item_url = requests.get(l).text
        #     soup = bs(item_url, 'lxml')
        #     date = soup.find('span', class_="styles_brief_wrapper__date__FfOke")
        #     print(date)

        try:
            image = item.find('img', class_='styles_image--blur__6MsOZ').get('data-src')
        except:
            image = None
        title = item.find('h3', class_='styles_title__wj__Y').text
        try:
            price = item.find('p', class_='styles_price__x_wGw').text
        except:
            price = None
        params = item.find('p', class_='styles_parameters__baZ7_ styles_ellipsis__3MoMa').text
        try:
            div = item.find('div', class_='styles_bottom__bottom__PzqJt')
            city = item.find('div', class_='styles_bottom__bottom__PzqJt').find('p').text
        except:
            city = None
        try:
            time = item.find('div', class_='styles_bottom__bottom__PzqJt').find('span')
        except:
            time = None
    
        # print(div)

        items_arr.append({
            'link': link,
            'image': image,
            'title': title,
            'price': price,
            'params': params,
            'city': city,
            # 'time': time
            
        })

    with open('thinkpad_gomel.json', 'w', encoding='utf-8') as f:
        json.dump(items_arr, f, indent=4, ensure_ascii=False)

def main():
    get_data()

if __name__ == "__main__":
    main()