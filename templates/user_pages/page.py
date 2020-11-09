from selenium.webdriver.common.by import By
from module.core.pageobject.PageObject import BasePageObject
from module.core.pageobject.PageObject import Locators

import allure

class Class(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LOCATORS_DICT
        self.locators["search_input"] = (By.CLASS_NAME, "zen-ui-search__input")
        self.locators["tab_container"] = (By.CLASS_NAME, "search-tabs-view__item-container")
        self.locators["tab_item"] = (By.CLASS_NAME, "search-tabs-view__item")

    @allure.feature("Open website")
    @allure.story("Открытие сайта")
    @allure.epic("critical")
    def site(self, url):
        with allure.step(f"Открыли сайт {url}"):
            self.open_website(url)

    @allure.feature("Search in website")
    @allure.story("Использование поисковой строки на сайте")
    def search(self, words):
        with allure.step(f"Поиск по слову '{words}'"):
            self.write_in_element(self.locators["search_input"], words)
            self.enter_key(self.locators["search_input"])
            self.wait(2)

    @allure.feature("Search in website (fixture)")
    @allure.story("Использование поисковой строки на сайте (fixture)")
    def search_with_fixture(self, words):
        with allure.step(f"Поиск по слову '{words}'"):
            self.write_in_element(self.locators["search_input"], words)
            self.enter_key(self.locators["search_input"])
            self.wait(2)

    @allure.feature("Get tab")
    @allure.story("Премещение по табам")
    def get_tab(self, name):
        with allure.step("Поиск элемента по локатору"):
            tab_items = self.find_elements(self.locators["tab_container"])

        with allure.step(f"Определение нужного таба '{name}'"):
            for index in range(len(tab_items)):
                if (self.find_element(self.locators["tab_item"], tab_items[index]).text == name):
                    self.click_element(tab_items[index])
                    break
            self.wait(2)

        with allure.step("Очистка строки поиска"):
            self.clear_input(self.locators["search_input"])