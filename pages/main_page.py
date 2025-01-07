import allure
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import MainPageConstants
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/')  # декоратор
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Нажимаем на вопрос и получаем ответ')
    def get_faq_text(self, question_locator, answer_locator):
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(question_locator)
        )

        faq_button = self.driver.find_element(*question_locator)

        self.driver.execute_script("arguments[0].scrollIntoView();", faq_button)

        WebDriverWait(self.driver, timeout=3).until(
            EC.element_to_be_clickable(question_locator)
        )

        self.driver.execute_script("arguments[0].click();", faq_button)

        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(answer_locator)
        )

        faq_text_element = self.driver.find_element(*answer_locator)
        return faq_text_element.text

    @allure.step('Нажимаем на вопрос и получаем ответ')
    def order_click(self, order_locator):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()

        order_button = self.driver.find_element(*order_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(order_locator)
        )

        self.driver.find_element(*order_locator).click()

        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        )

    @allure.step('Нажимаем кнопку Яндекс в хэдере')
    def click_yandex_button(self):
        self.driver.find_element(*MainPageLocators.YANDEX_BUTTON).click()

        url = MainPageConstants.DZEN_URL
        response = requests.get(url)
        assert (response.status_code, 200)



