from templates.user_pages.page import Class
import pytest

@pytest.mark.parametrize("words", [
        "QA",
        "QC",
        "Putin"
])
def test_zen_yandex(browser, words):
    test = Class(browser)
    test.site("https://zen.yandex.ru/")
    test.search_with_fixture(words)
    test.get_tab("Видео")
