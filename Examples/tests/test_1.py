from templates.user_pages.page import Class

def test_zen_yandex(browser):
    test = Class(browser)
    test.site("https://zen.yandex.ru/")
    test.search("python")
    test.get_tab("Статьи")
