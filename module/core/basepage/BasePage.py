import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # ----------------------- ПОИСК ЭЛЕМЕНТОВ -----------------------
    def find_element(self, locator, element=None, time=10):
        """
        ПОИСК ЭЛЕМЕНТА ПО ЛОКАТОРУ
        :param element:
        :param locator: локатор поиска
        :param time: время ожидания
        :return: элемент
        """
        if element == None:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Не могу найти элемент по локатору {locator}")
        else:
            return WebDriverWait(element, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не могу найти элемент по локатору {locator}")

    def find_elements(self, locator, time=10):
        """
        ПОИСК ЭЛЕМЕНТОВ ПО ЛОКАТОРУ
        :param locator: локатор поиска
        :param time: время ожидания
        :return: список элементов
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не могу найти элементы по локатору {locator}")

    # ----------------------- ДЕЙСТВИЯ НАД ЭЛЕМЕНТАМИ -----------------------
    def click_element(self, element):
        element.click()

    def clear_input(self, locator):
        element = self.find_element(locator)
        len_input_text = len(element.get_attribute("value"))
        for index in range(len_input_text):
            element.send_keys("\b")

    def write_in_element(self, locator, words):
        element = self.find_element(locator)
        element.send_keys(words)

    # ----------------------- ОЖИДАНИЯ -----------------------
    def wait(self, sec):
        time.sleep(sec)

    def wait_view_element(self, locator, time):
        element = False
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
        finally:
            return element

    # ----------------------- КЛАВИАТУРА -----------------------
    def enter_key(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    # ----------------------- ПРОЧЕЕ -----------------------
    def open_website(self, url):
        """
        ОТРЫТИЕ URL САЙТА
        :param url: url
        :return: объект открытой страницы
        """
        return self.driver.get(url)