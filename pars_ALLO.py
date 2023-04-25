import requests
from bs4 import BeautifulSoup

url = "https://allo.ua/ua/products/mobile/dir-asc/order-price/proizvoditel-samsung/"

response = requests.get(url)


with open('result.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
soup = BeautifulSoup(response.text, "html.parser")


# вибраний виробник Samsung( з data і буде братися вся інфа)
data = soup.find_all("div", class_="product-card")
# витягуємо ссилки, ціну, назви на моделі(1 сторінка)
for i in data:
    samsung = i.find("a").get("href")
    price = i.find("div", class_="v-pb__cur").text
    name = i.find("a", class_="product-card__title").text
    print(samsung, price, name)

#print(data)







#name = data.find("a", class_="product-card__title").text

#price = data.find("div", class_="v-pb__cur").text

#url_img = data.find("img", class_="gallery__img").get("src")?

#print(name + '\n' + price + '\n' + url_img + '\n')
