import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        """
        Конструктор
        :param driver: WebDriver
        """
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
        """
        Клик по элементу
        :param element: элемент
        :return: None
        """
        element.click()

    def clear_input(self, locator):
        """
        Очистить поле ввода
        :param locator: путь к элементу
        :return: None
        """
        element = self.find_element(locator)
        len_input_text = len(element.get_attribute("value"))
        for index in range(len_input_text):
            element.send_keys("\b")

    def write_in_element(self, locator, words):
        """
        Заполнение поля ввода
        :param locator: путь к элементу
        :param words: строка
        :return: None
        """
        element = self.find_element(locator)
        element.send_keys(words)

    # ----------------------- ОЖИДАНИЯ -----------------------
    def wait(self, sec):
        """
        Ожидание через засыпания главного потока
        :param sec: секунды
        :return: None
        """
        time.sleep(sec)

    def wait_view_element(self, locator, time):
        """
        Ожидание появления элемента
        :param locator: путь к элементу
        :param time: время ожидания
        :return: False - элемент не появился True - элемент появился
        """
        element = False
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
        finally:
            return element

    # ----------------------- КЛАВИАТУРА -----------------------
    def enter_key(self, locator):
        """
        Нажать Enter в элементе
        :param locator: путь к элементу
        :return: None
        """
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