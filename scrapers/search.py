import requests
import json



def main():
    count = 0
    total = []
    with open('files/totals.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(len(data))

        for item in data:
            
            try:
                if 'ideapad' in item['subject']:
                    count += 1
                    print(item['subject'], item['ad_link'])
            except:
                continue

            # try:
            #     for i in item['ad_parameters']:
                    
            #         # if i['pl'] == 'Производитель':   
            #         #     print(i)

            #         if i['vl'] == 'HP':
            #             print(i)
            #             count += 1
            #             print(count)

            #             total.append(item)
                        
                
            # except:
            #     continue

    # with open('files/total.json', 'w', encoding='utf-8') as f:
    #     json.dump(total, f, ensure_ascii=False, indent=4)  
    # print('Done')  


if __name__ == "__main__":
    main()