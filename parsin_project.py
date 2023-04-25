import requests
from bs4 import BeautifulSoup

url = "https://allo.ua/ua/products/mobile/dir-asc/order-price/proizvoditel-samsung/"

response = requests.get(url)


sup = BeautifulSoup(response.text, "html.parser")

data = sup.find_all("div", class_="products-layout__item")
if data:
    for i in data:
        name_elem = i.find("a", class_="product-card__title")
        if name_elem:
            name = name_elem.text.strip()
        else:
            name = "Name not found"

        price_elem = i.find("div", class_="v-pb__cur")
        if price_elem:
            price = price_elem.text.strip()
        else:
            price = "Price not found"

        url_img_elem = i.find("img", class_="gallery__img")
        if url_img_elem:
            url_img = url_img_elem.get("src")
        else:
            url_img = "Image not found"

        print(name + '\n' + price + '\n' + url_img + '\n')
else:
    print("No data found")

    if name is not None and price is not None and url_img is not None:
        print(name + '\n' + price + '\n' + url_img + '\n')
    else:
        print("Some data not found")