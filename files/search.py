import requests
import json

with open('page1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    for item in data['ads']:
    
        # print(item['ad_parameters'])
        # with open('item.json', 'w', encoding='utf-8') as f:
        #     json.dump(item, f, ensure_ascii=False, indent=4)

        for i in item['ad_parameters']:
            if 'Lenovo' in i['vl']:
                print(i['vl'])

# print(data)