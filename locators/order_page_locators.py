from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") #инпут Имя
    SURE_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # инпут Фамилия
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # инпут Адрес
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # инпут Метро
    METRO_ROKOSOVSKI_SELECTOR = (By.XPATH, "(//div[text()='Бульвар Рокоссовского'])[1]")  # инпут Метро Бульвар Рокоссовского
    METRO_CHERKIZOVSKAYA_SELECTOR = (By.XPATH, "(//div[text()='Черкизовская'])[1]")  # инпут Метро Черкизовская
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # инпут телефон
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")  # кнопка Далее
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # инпут Когда привезти самокат
    SELECTOR_DATE_ONE = (By.XPATH, "//div[@aria-label='Choose пятница, 31-е января 2025 г.']")  # селектор даты
    SELECTOR_DATE_TWO = (By.XPATH, "//div[@aria-label='Choose суббота, 1-е февраля 2025 г.']")  # селектор даты
    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")  # инпут Срок аренды
    SELECTOR_RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[text()='сутки']")  # селектор срока аренды на сутки
    SELECTOR_RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")  # селектор срока аренды на двое суток
    SELECTOR_COLOR_BLACK = (By.XPATH, "//input[@id='black']")  # селектор цвета самоката черный
    SELECTOR_COLOR_GREY = (By.XPATH, "//input[@id='grey']")  # селектор цвета самоката серый
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # инпут комментарий
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")  # кнопка заказать
    BUTTON_ACCEPTION_POP_UP_YES = (By.XPATH, "//button[text()='Да']")  # кнопка Да на поп-апе подтверждения заказа
    BUTTON_SHOW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")  # кнопка Посмотреть статус
    SCOOTER_BUTTON = (By.XPATH, "//a[(@href= '/')]")  # Кнопка самокат в хэдере
