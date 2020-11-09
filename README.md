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

### Часть 3 - установка проекта (примеры для PyCharm)
1. Скачать проект 
> git clone https://github.com/nu11try/AndroFrame.git
2. Открыть среду разработку (IDE)
3. Создать новый проект (**File** -> **New Project** -> **Pure Python**)
4. Открыть проект в проводнике (**ПКМ** -> **Show in Explorer**)
5. Скопировать в проект все из клонированного репозитория

### Часть 4 - структура framework
+ **Module** - папка, в которой собраны все модули framework
   1. **Core** - ядровая папка framework
     1. **BasePage** - папка со стандартным шаблоном объекта BasePage.py
       1. **BasePage.py** - файл стандартного шаблона объекта
     2. **PageObject** - папка со стандартным шаблоном страницы PageObject.py
       1. **PageObject.py** - файл стандартного шаблона страницы
   2. **Result** - папка с пезультатами для Allure
   3. **Templates** - папка для пользовательских шаблонов
     1. **User_pages** - папка для пользовательских шаблонов страницы
   4. **Tests** - папка для хранения тестов (**ВНИМАНИЕ!** В папке должен присутствовать пустой файл \__init__.py)
   5. **Conftest.py** - файл для конфигурации PyTest (содержит необходимые fixture)
   6. **Create_allure_report.cmd** - файл для запуска построения отчета Allure
