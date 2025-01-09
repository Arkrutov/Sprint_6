from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCORDION_QUESTION_0 = (By.XPATH, "//div[@id='accordion__heading-0']") #первая кнопка FAQ
    ACCORDION_ANSWER_0 = (By.XPATH, "//div[@id='accordion__panel-0']//p")  #первый ответ FAQ
    ACCORDION_QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-1']") #вторая кнопка FAQ
    ACCORDION_ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-1']//p")  #второй ответ FAQ
    ACCORDION_QUESTION_2 = (By.XPATH, "//div[@id='accordion__heading-2']") #третья кнопка FAQ
    ACCORDION_ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-2']//p")  #третий ответ FAQ
    ACCORDION_QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-3']") #четвертая кнопка FAQ
    ACCORDION_ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-3']//p")  #четвертый ответ FAQ
    ACCORDION_QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-4']") #пятая кнопка FAQ
    ACCORDION_ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-4']//p")  #пятый ответ FAQ
    ACCORDION_QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-5']") #шестая кнопка FAQ
    ACCORDION_ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-5']//p")  #шестая ответ FAQ
    ACCORDION_QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-6']") #седьмая кнопка FAQ
    ACCORDION_ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-6']//p")  #седьмой ответ FAQ
    ACCORDION_QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-7']") #восьмая кнопка FAQ
    ACCORDION_ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-7']//p")  #восьмой ответ FAQ
    YANDEX_BUTTON = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")  #Кнопка яндекс в хэдере
    BUTTON_ORDER_IN_HEADER = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")  #Кнопка заказать в хэдере
    BUTTON_ORDER_IN_CENTER = (By.XPATH, "(//button[contains(., 'Заказать')])[2]")  #Кнопка заказать в хэдере
    TEXT_ABOUT_SCOOTER = (By.XPATH, "//div[text()='Привезём его прямо к вашей двери,']")  #Текст на главной
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")  # кнопка куки нотификейшен

