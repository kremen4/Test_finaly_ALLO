import time
from inits.form_init import FormInit
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestFormInit:

    def test_open(self, driver):
        form_init = FormInit(driver, 'https://allo.ua/')
        driver.implicitly_wait(10)
        form_init.open()
        time.sleep(2)
        # вхід на сторінку для авторизації
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[1]/button').click()
        time.sleep(2)
        # спроба залогінитися без вводу номеру
        driver.find_element(By.CLASS_NAME, 'a-button__text').click()
        # Повідомлення про обовязкове заповнення поля
        warning = driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/div/form/div/span').text
        # Порівняння попереджувального запису  фронта з бекенд
        assert warning == "Це поле є обов'язковим для заповнення."

        # введення дійсного номеру але не зареєстрованого
        driver.find_element(By.NAME, 'telephone').send_keys("992331382", Keys.RETURN)
        time.sleep(3)
        # Повідомлення попереджувального тексту про не зареєстрований номер та рекомендація зареєструватися
        error = driver.find_element(By.CSS_SELECTOR,
        '#customer-popup-menu > div > div.auth__register > div.auth__contact > div.auth__text.auth__text--full-width')
        # Порівняння попереджувального повідомлення  фронта з бекенд
        assert "Цей номер телефону не зареєстрований.\nДля реєстрації введіть своє ім'я." in error.text

        # посилання інший спосіб входу( через e-mail)
        driver.find_element(By.CLASS_NAME, 'a-button__text').click()
        driver.refresh()
        # пробуємо залогінитися через вкладку "ввести e-mail , login"
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[1]/button').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/div/div[3]/button').click()

        # без вводу e-mail пробуємо увійти
        driver.find_element(By.CLASS_NAME, 'a-button__text').click()

        # Повідомлення що поля обовязкові для заповнення (e-mail, login)
        error = driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/form/div[1]/span')
        assert "Це поле є обов'язковим для заповнення" in error.text
        error = driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/form/div[2]/span')
        assert "Це поле є обов'язковим для заповнення" in error.text
        # в полі e-mail вводимо набір символів
        driver.find_element(By.CSS_SELECTOR, 'input[class*="a-input__field base-input').click()
        user_clear = driver.find_element(By.CSS_SELECTOR, 'input[class*="a-input__field base-input')
        user_clear.send_keys('1qaz-=+4', Keys.ENTER)
        # попередження "Введено некоректний email"
        error_mail = driver.find_element(By.CSS_SELECTOR, 'span[class*="a-input__message base-message is-error"]')
        assert 'Введено некоректний email' in error_mail.text
        time.sleep(2)
        # Видаляємо в полі всі символи
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        user_clear.send_keys(Keys.BACKSPACE)
        # вводимо валідний e-mail без пароля
        driver.find_element(By.CSS_SELECTOR, 'input[class*="a-input__field base-input').send_keys(
            'stanson1974@gmail.com', Keys.ENTER)
        time.sleep(3)

        # попередження про обовязковий ввод паролю
        new = driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/form/div[2]/span')
        assert "Це поле є обов'язковим для заповнення" in new.text
        # в поле пароль вводимо дані
        driver.find_element(By.NAME, 'password').click()
        driver.find_element(By.NAME, 'password').send_keys('123qaz', Keys.ENTER)

        # повідомлення про незареєстрований  e-mail
        text_error = driver.find_element(By.XPATH, '//*[@id="customer-popup-menu"]/div/div[2]/div[1]/div[2]/p[1]')
        assert 'Цей email не зареєстрований.' in text_error.text
        # закриття вікна
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]').click()
        # кнопка Каталог
        driver.find_element(By.CLASS_NAME, 'ct-button').click()

        # вибираємо вид товару (Повер банк)
        driver.find_element(By.XPATH, '//*[@id="js-menu-wrapper"]/div/ul/li[1]/div/mmc[1]/mms[2]/mmss/a[2]').click()

        # вибираємо ємність 20 000
        driver.find_element(By.CLASS_NAME, 'product-card__title').click()

        # натискаємо кнопку Купити
        driver.find_element(By.ID, "product-buy-button").click()
        time.sleep(2)
        # натискаємо оформити замовлення
        driver.find_element(By.CLASS_NAME, 'order-now').click()
        time.sleep(6)

        #  на сторінці оформлення замовлення, натискаємо "Вибрати доставку" без введення телеф. та імені
        # повинна бути інфа про обовязкове введення в поля
        driver.find_element(By.CLASS_NAME, 'a-button__text').click()
        time.sleep(3)
        # звіряємо попереджувальну інфу про необхідність заповнення обох  полів
        err = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div/div/form/div[1]/span')
        assert "Це поле є обов'язковим для заповнення." in err.text
        erro = driver.find_element(By.XPATH,
                                   '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div/div/form/div[2]/span')
        assert "Це поле є обов'язковим для заповнення." in erro.text
        #  перевіряємо поле введення міста та вводимо місто яке відсутнє в списку міст
        driver.find_element(By.XPATH,
                      '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div/div/form/div[3]/div/div').click()
        driver.find_element(By.XPATH,
                '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div/div/form/div[3]/div/div[2]/ul/li[2]').click()

        driver.find_element(By.NAME, 'cityAutocomplete').send_keys('Лондон', Keys.ENTER)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div').click()

        # Повідомлення про не обхідність введення коректної назви міста
        city = driver.find_element(By.CSS_SELECTOR, 'span[class*="a-autocomplete__message base-message is-error"]')
        assert "Будь ласка, перевірте правильність введеної назви міста." in city.text
        # переходимо на головну сторінку щоб перевірити нявність товару в кошику та зробити редагування(видалити)
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/div[1]/a/img').click()
        #заходимо в Кошик
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/div[1]/div[2]/div[4]/div[2]/button').click()
        time.sleep(3)
        # видаляємо товар
        driver.find_element(By.CSS_SELECTOR, 'svg[class*="vi i-shared vi__close remove"]').click()
        time.sleep(2)

        # підтвердження що Кошик порожній
        basket = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/div/div[1]/div/p[1]')
        assert 'Ваш кошик порожній.' in basket.text
        # закриваємо віконце Кошик порожній
        driver.find_element(By.CSS_SELECTOR, 'svg[class*="vi i-shared vi__close"]').click()

        #  щоб наступний елемент був видимий необхідно проскролити сторінку
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(5)
        # спроба зробити підписку без вводу e-mail
        driver.find_element(By.CSS_SELECTOR, 'button[class*="social-subscription__button"]').click()
        # попереджувальний текст про обовязкове заповнення поля( необхідно ввести e-mail)
        text_warning = driver.find_element(By.XPATH,
                        '//*[@id="__layout"]/div/div[2]/div[1]/div/div/div/div/div[2]/span/span/span')
        assert "Це поле є обов'язковим для заповнення." in text_warning.text

        # спроба підписатия при вводі не коректного e-mail
        driver.find_element(By.XPATH, '//*[@id="catalog-social-block-email"]').click()
        driver.find_element(By.XPATH, '//*[@id="catalog-social-block-email"]').send_keys('бразилія@бразилія')
        driver.find_element(By.CLASS_NAME, 'social-subscription__button').click()
        time.sleep(2)
        # повідомлення про некоректний e-mail
        mail_non = driver.find_element(By.CLASS_NAME, 'validation-text')
        assert 'Введено некоректний email' in mail_non.text
        # скролимо на верх сторінки
        driver.find_element(By.CSS_SELECTOR, 'svg[class*="vi i-shared vi__arrow"]').click()
        time.sleep(2)
        # провіряємо поле Пошук на ввод хаотичних елементів
        driver.find_element(By.ID, 'search-form__input').click()
        driver.find_element(By.ID, 'search-form__input').send_keys('=-23%qaz', Keys.RETURN)
        time.sleep(3)
        # завантажилася сторінка з відповіддю на введений текст
        field_search = driver.find_element(By.CSS_SELECTOR, 'span[class*="b-crumbs__link"]')
        assert "Результати пошуку для '=-23%qaz'. Знайдено товарів: 0" in field_search.text
        time.sleep(2)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)

   # def test_page(self, driver):
       # form_init = FormInit(driver, 'https://allo.ua/')
       # form_init.open()
      #  driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
       # time.sleep(3)

        # посилання Контакти
        driver.find_element(By.CSS_SELECTOR, 'a[href="https://allo.ua/ua/contact-us/"]').click()
        time.sleep(3)
         #  Натискаємо "Надіслати". В формі незаповнюємо нічого
        driver.find_element(By.XPATH,
                             '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div/div[2]/div/form/button').click()
        time.sleep(3)
        #Зявилося повідомлення про обовязкове заповнення полів( Ім"я, телефон або пошта, текст в полі Повідомлення)
        #Поле імя
        name = driver.find_element(By.CSS_SELECTOR, 'span[class*="validation-text"]')
        assert "Це поле є обов'язковим для заповнення." in name.text
        #Поле телефон або пошта
        mail_telef = driver.find_element(By.CSS_SELECTOR, 'label[class*="feedback__label"]')
        assert "Ел. пошта або телефон" in mail_telef.text
        # Повідомлення про обов. введення пошти або телефон
        telef_mail = driver.find_element(By.CSS_SELECTOR, 'span[class*="validation-text"]')
        assert "Це поле є обов'язковим для заповнення." in telef_mail.text
        # Поле Повідомлення
        massage = driver.find_element(By.XPATH,
            '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div/div[2]/div/form/div[4]/div/div[2]/span/span/span')
        assert "Будь-ласка, введіть своє повідомлення." in massage.text

        # Заповнюємо поля: І'мя, пошта, Повідомлення, в полі пошта вводимо некорекний mail
        driver.find_element(By.ID, 'feedback-name').send_keys('Стас')
        driver.find_element(By.ID, 'feedback-email').send_keys('Малага@Малага.Spain')
        driver.find_element(By.ID, 'feedback-message').send_keys('Вакансія')
        driver.find_element(By.XPATH,
                         '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div/div[2]/div/form/button').click()
        #Попереджувальне повідомлення про некоректний mail
        incorect_mail = driver.find_element(By.CSS_SELECTOR, 'span[class*="validation-text"]')
        assert 'Введено некоректний email' in incorect_mail.text

        #Переходимо на головну сторінку натиская логотип
        driver.find_element(By.CSS_SELECTOR, 'a[href="https://allo.ua/"]').click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)

        # Посилання подарунковий сертифікат
        driver.find_element(By.CSS_SELECTOR, 'a[href="https://allo.ua/ua/gift-certificates/"]').click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        # поле перевірка дії сертифіката натискаємо Перевірити без введення номеру
        driver.find_element(By.XPATH, '//*[@id="giftcard-widget"]/form/button').click()
        time.sleep(3)
        # Порівняння попереджувального тексту про обовязкове введення номеру
        name_certif = driver.find_element(By.XPATH, '//*[@id="giftcard-widget"]/form/div/span')
        assert "Це поле є обов'язковим для заповнення." in name_certif.text
        # вводимо рандомні числа
        driver.find_element(By.CSS_SELECTOR, 'input[class*="a-input__field base-input"]')\
                                                                             .send_keys("1258745851232", Keys.ENTER)
        time.sleep(5)
        number_non = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/section/div/p')
        assert 'Сертифікат 125-874-585-1232 не знайдено.' in number_non.text
        # закриваємо попереджувальне віконце
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]').click()

        #Внизу сторінки превіряємо  лого Алло, робимо клік (повині перейти  на головну сторінку)
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div[3]/div[2]/div[3]/a/img').click()
        # перевірка що знаходимся на головній сторінці
        header_page = driver.find_element(By.CLASS_NAME, 'ct-button')
        assert "Каталог" in header_page.text

        driver.quit()

































