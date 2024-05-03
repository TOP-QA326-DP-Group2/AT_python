import pytest
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# #  headless режим, раскомментируем строку: from 'selenium.webdriver.chrome.options import Option'
# @pytest.fixture()
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     base_url = "https://miktyres.ru/buy/"
#     driver.get(base_url)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver

#  обычный режим с отображением открываемых окон браузера,
#  комментируем строку: from 'selenium.webdriver.chrome.options import Option'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    base_url = "https://miktyres.ru/buy/"
    driver.get(base_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
