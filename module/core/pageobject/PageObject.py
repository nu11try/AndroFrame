from module.core.basepage.BasePage import BasePage

class Locators:
    LOCATORS_DICT = {}

class BasePageObject(BasePage):

    def exit(self):
        exit(0)