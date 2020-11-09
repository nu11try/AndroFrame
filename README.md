# AndroFrame
Python framework for UI testing

# Начало
#### Стек
* **Python** (https://www.python.org/)
* **Selenium** (https://www.selenium.dev/)
* **PyTest** (https://docs.pytest.org/en/stable/)
* **Allure** (http://allure.qatools.ru/)
* **Webdriver Manager** (https://github.com/SergeyPirogov/webdriver_manager)
* **Scoop** (https://scoop.sh/)

# Старт
### Часть 1 - установка Python
1. Перейти на сайт **Python**
2. Скачать последнюю версию
3. Установить **Pyhton** с выбором опции для прописывания пути в **PATH**

### Часть 2 - установка необходимых модулей
1. Открыть PowerShell
2. Выполнить команду
> Set-ExecutionPolicy RemoteSigned -scope CurrentUser
3. Выполнить команду
> iwr -useb get.scoop.sh | iex
2. Установить **PyTest** 
> pip install pytest
3. Установить **Selenium** 
> pip install selenium
4. Установить **Webdriver Manager** 
> pip install webdriver_manager
5. Установить **Allure** 
> scoop install allure

### Часть 3 - структура framework
+ **Module** - папка, в которой собраны все модули framework
   + **Core** - ядровая папка framework
     + **BasePage** - папка со стандартным шаблоном объекта BasePage.py
       + **BasePage.py** - файл стандартного шаблона объекта
     + **PageObject** - папка со стандартным шаблоном страницы PageObject.py
       + **PageObject.py** - файл стандартного шаблона страницы
   + **Result** - папка с пезультатами для Allure
   + **Templates** - папка для пользовательских шаблонов
     + **User_objects** - папка для пользовательских шаблонов объектов
     + **User_pages** - папка для пользовательских шаблонов страницы
   + **Tests** - папка для хранения тестов (**ВНИМАНИЕ!** В папке должен присутствовать пустой файл \__init__.py)
   + **Conftest.py** - файл для конфигурации PyTest (содержит необходимые fixture)
   + **Create_allure_report.cmd** - файл для запуска построения отчета Allure

### Часть 4 - установка проекта (примеры для PyCharm)
1. Клонировать репозиторий 
> git clone https://github.com/nu11try/AndroFrame.git
2. Открыть среду разработку (IDE)
3. Создать новый проект (**File** -> **New Project** -> **Pure Python**)
4. Открыть проект в проводнике (**ПКМ** -> **Show in Explorer**)
5. Скопировать в проект все из клонированного репозитория

### Часть 5 - Настройка и написание тестов
1. Создать свой шаблон строки
2. Выполнить подключение библиотек
```pyhton
from selenium.webdriver.common.by import By
from module.core.pageobject.PageObject import BasePageObject
from module.core.pageobject.PageObject import Locators

import allure
```
3. Создать свой файл для шаблона страницы с наследованием класса стандартного шаблона страницы
```pyhton
class Class(BasePageObject):
```
4. В конструкторе созданного класса инициализировать словать локаторов
```pyhton
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LOCATORS_DICT
```
5. В словарь локаторов добавить необходимые локаторы (пример)
```pyhton
    self.locators["test"] = (By.CLASS_NAME, "test")
    self.locators["test"] = (By.ID, "test")
    self.locators["test"] = (By.XPATH, "test")
    self.locators["test"] = (By.LINK_TEXT, "test")
    self.locators["test"] = (By.PARTIAL_LINK_TEXT, "test")
    self.locators["test"] = (By.NAME, "test")
    self.locators["test"] = (By.TAG_NAME, "test")
    self.locators["test"] = (By.CSS_SELECTOR, "test")
```
6. Написать необходимые функции, помечая декораторами (пример) (описание см. ниже)
```pyhton
@allure.feature("Open website")
@allure.story("Открытие сайта")
```
7. Шаги функции помечать декораторами 
```pyhton
with allure.step("Test"):
   code
```
если необходимо указать в шаг переменные, то
```pyhton
with allure.step(f"Test '{name}'"):
   code
```
8. Создать файл с тестом
9. Подключить свой шаблон страницы
```pyhton
from templates.user_pages.НАЗВАНИЕ ШАБЛОНА import НАЗВАНИЕ КЛАССА
```
10. Создать функции тестирование, с параметром browser (перед названием указывать test_) (пример)
```pyhton
def test_zen_yandex(browser):
```
11. Написать тест!

### Часть 6 - запуск тестов
1. Открыть терминал IDE
2. Если необходимо запустить все тесты
> pytest --alluredir results
3. Если необходимо запустить кокретные тесты
> pytest --alluredir results [*название теста*.py]

### Часть 7 - построение отчета Allure
1. Открыть PowerShell
2. Выполнить команду 
> .\create_allure_report.cmd

# Использование своего BasePage
1. Создать свой файл в user_objects
2. Наследовать базовый шаблон объекта
```pyhton
class КЛАСС(BasePage):
```
3. Создать свой файл для шаблона страницы с наследованием класса созданного шаблона объекта
```pyhton
from templates.user_objects.ШАБЛОН import КЛАСС

class КЛАСС(КЛАСС ОБЪЕКТА):
```
4. В тестах использовать созданный шаблон страницы с наследуемым шаблоном объекта

# Описание fixture
В разработке...

# Тестирование API
В разработке...
