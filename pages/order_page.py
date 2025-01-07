import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/')  # декоратор
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Заполняем форму Для кого самокат и нажимаем Далее')
    def fill_for_who_form(
            self,
            name,
            sure_name,
            address_name,
            metro_name_locator,
            phone_number,

    ):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURE_NAME_INPUT).send_keys(sure_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address_name)
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()
        self.driver.find_element(*metro_name_locator).click()
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone_number)
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(OrderPageLocators.INPUT_DATE)
        )

    @allure.step('Заполняем форму Про аренду и нажимаем Заказать')
    def fill_about_rent_form(
            self,
            date_selector_locator,
            rent_period_locator,
            color_locator,
            comment_text

    ):
        self.driver.find_element(*OrderPageLocators.INPUT_DATE).click()
        self.driver.find_element(*date_selector_locator).click()
        self.driver.find_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        self.driver.find_element(*rent_period_locator).click()
        self.driver.find_element(*color_locator).click()
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment_text)
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(OrderPageLocators.BUTTON_ACCEPTION_POP_UP_YES)
        )
        self.driver.find_element(*OrderPageLocators.BUTTON_ACCEPTION_POP_UP_YES).click()

        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(OrderPageLocators.BUTTON_SHOW_STATUS)
        )
        self.driver.find_element(*OrderPageLocators.BUTTON_SHOW_STATUS).click()

    @allure.step('Нажимаем кнопку Самокат в хэдере')
    def click_scooter_button(self):
        self.driver.find_element(*MainPageLocators.SCOOTER_BUTTON).click()
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(MainPageLocators.TEXT_ABOUT_SCOOTER)
        )


