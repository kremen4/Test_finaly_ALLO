import time
import requests
from bs4 import BeautifulSoup



#Частина 7
def get_url():
    for count in range(1,8):
        time.sleep(3)
        response = requests.get(f'https://scrapingclub.com/exercise/list_basic/?page=(count)')
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')     # Отримання інфи по карточкам товарів
                                                                         #зі сторінки (9елем.)
        for i in data:    #Циклом створюємо по кожному елементу посилання і передаємо в список (list_card_url)
            card_url ='https://scrapingclub.com'+ i.find('a').get('href')
            yield card_url

def array():

  for card_url in get_url():
    response = requests.get(card_url)
    time.sleep(3)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div',class_='card mt-4 my-4')
    name = data.find('h3',class_='card-title').text
    price = data.find('h4').text
    text = data.find('p',class_='card-text').text
    url_img ='https://scrapingclub.com'+ data.find('img',class_="card-img-top img-fluid").get('src') #отримання силки 'src' це атрибут тега img
    yield name, price, text, url_img    # Створемо кортеж







#2
    #for i in data:                                              # Отримання назви товару (Short Dress)
        #name = i.find('h4', class_='card-title').text
        #print(name)
        #price = i.find('h5').text                                 # Отримання ціни
       # url_img ='https://scrapingclub.com' + i.find('img',class_='card-img-top img-fluid').get('src')
       # print(name, price, url_img)                              #Отримання посилання на товар (фото)


