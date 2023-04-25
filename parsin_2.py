import time
import requests
from bs4 import BeautifulSoup

#Частина 6  якщо сторінок і товару на сайті дуже багато, то помістимо кількість в функцію  'def'
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

for card_url in get_url():            # Виконується кругова генерація отримання ссилок ,щоб не загромоджувати память ,
# З цієї точки починається генерація    # коли це буває при  створенні списку
    response = requests.get(card_url)
    time.sleep(3)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div',class_='card mt-4 my-4')
    name = data.find('h3',class_='card-title').text
    price = data.find('h4').text
    text = data.find('p',class_='card-text').text
    url_img ='https://scrapingclub.com'+ data.find('img',class_="card-img-top img-fluid").get('src') #отримання силки 'src' це атрибут тега img
    print(name + '\n', price + '\n', text+'\n', url_img)


# Частина 5
#list_card_url = []
#for count in range(1,8):
   # time.sleep(3)
    #response = requests.get(f'https://scrapingclub.com/exercise/list_basic/?page=(count)')
   # soup = BeautifulSoup(response.text, 'lxml')
    #data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')     # Отримання інфи по карточкам товарів
                                                                   #зі сторінки (9елем.)
   # for i in data:    #Циклом створюємо по кожному елементу посилання і передаємо в список (list_card_url)
      #  card_url ='https://scrapingclub.com'+ i.find('a').get('href')
      #  list_card_url.append(card_url)

#for card_url in list_card_url:  #Даним циклом проходимся по списку із силок(list_card_url) Опис товару що під фото
   # response = requests.get(card_url)  # тут робимо окремий запрос на кожен вид товару
   # soup = BeautifulSoup(response.text, 'lxml')
   # data = soup.find('div',class_='card mt-4 my-4')  # вся інфа по карті
   # name = data.find('h3',class_='card-title').text
   # price = data.find('h4').text
  #  text = data.find('p',class_='card-text').text
   # url_img ='https://scrapingclub.com'+ data.find('img',class_="card-img-top img-fluid").get('src') #отримання силки 'src' це атрибут тега img
   # print(name + '\n', price + '\n', text+'\n', url_img)


# Частина 4
#for count in range (1, 8):
   # time.sleep(3)
   # response = requests.get(f'https://scrapingclub.com/exercise/list_basic/?page=(count)')
    #soup = BeautifulSoup(response.text, 'lxml')
   # data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

   # for i in data:
      #  name = i.find('h4', class_='card-title').text
       # price = i.find('h5').text

      #  url_img ='https://scrapingclub.com' + i.find('img',class_='card-img-top img-fluid').get('src')
       # print(name + '\n',price +'\n',url_img)




#Частина 3 Дістаємо інфу ці всіх семи сторінок, для цього створюємо цикл з rangt та добавляємо f до url а також
#добавляємо  count
#for count in range (1, 8):
    #time.sleep(3)
    #response = requests.get(f'https://scrapingclub.com/exercise/list_basic/?page=(count)')
    #soup = BeautifulSoup(response.text, 'lxml')
   # data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    #for i in data:
       # name = i.find('h4', class_='card-title').text
      #  price = i.find('h5').text

      #  url_img ='https://scrapingclub.com' + i.find('img',class_='card-img-top img-fluid').get('src')
      #  print(name + '\n',price +'\n',url_img)



# Частина 2
#response = requests.get('https://scrapingclub.com/exercise/list_basic/?page=1')
#soup = BeautifulSoup(response.text, 'lxml')
#data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')   #Частина 2. Замінюємо find  на find_all
# та створюємо цикл for щоб дістати інфу по всім карточкам на першій сторінці( 9 елементів на сторінці)
#всього 7 сторінок
#for i in data: #Частина 2    Замінюємо soup на i
    #name = i.find('h4', class_='card-title').text
    #price = i.find('h5').text
              #Добавляємо 'https://scrapingclub.com' в перемінну,щоб отримати повноцінну ссилку
    #url_img ='https://scrapingclub.com' + i.find('img',class_='card-img-top img-fluid').get('src')
    #print(name + '\n',price +'\n',url_img)  # отримуємо назву ,ціну  та посилання на кожну карточку
#  В частині 2 було написано код для отримання інфи карточок товару з однієї сторінки (ст.1)


#Частина 1
#response = requests.get('https://scrapingclub.com/exercise/list_basic/?page=1')
#soup = BeautifulSoup(response.text, 'lxml')
#data = soup.find('div', class_='col-lg-4 col-md-6 mb-4')   # Отримання інфи по карточці товару

#Частина 1  Отримання інфи по одній картоці товару
#name =soup.find('h4', class_='card-title').text     # Отримання назви товару (Short Dress)
#price = soup.find('h5').text                        # Отримання ціни
#url_img =soup.find('img',class_='card-img-top img-fluid')  #Отримання посилання на товар (фото)




