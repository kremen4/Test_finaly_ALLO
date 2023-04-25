import time
import requests
from bs4 import BeautifulSoup






response = requests.get('https://scrapingclub.com/exercise/list_basic/?page=1')
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')   # Отримання інфи по карточці товару
#print(data)
#Частина 1  Отримання інфи по одній картоці товару
name =soup.find('h4', class_='card-title').text     # Отримання назви товару (Short Dress)
price = soup.find('h5').text    # Отримання ціни
url_img =soup.find('img',class_='card-img-top img-fluid')  #Отримання посилання на товар (фото)
print(name, price)
#print()
