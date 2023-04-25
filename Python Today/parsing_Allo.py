import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"  
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
        "cache-control": "max-age=0",
        "user - agent": "Mozilla / 5.0(Linux;  Android 6.0; Nexus 5 Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 109.0 .0 .0Mobile Safari / 537.36"
    }

    response = requests.get(url=url, headers=headers)

    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(response.text)




def main():
    get_data("https://allo.ua/ua/products/mobile/dir-asc/order-price/proizvoditel-samsung/")




if __name__ == '__main__':
    main()









#url = "https://allo.ua/ua/products/mobile/dir-asc/order-price/proizvoditel-samsung/"

#response = requests.get(url)

#sup = BeautifulSoup(response.text, "html.parser")
# print(sup)

# вибраний виробник Samsung
#data = sup.find_all("div", class_="products-layout__item")
#print(data)