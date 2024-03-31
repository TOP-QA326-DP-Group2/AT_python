import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# #  headless режим, добавляем from 'selenium.webdriver.chrome.options import Option'
@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    base_url = "https://miktyres.ru/articles/podbor_diski/"
    driver.get(base_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

#  обычный режим, убираем from 'selenium.webdriver.chrome.options import Option'
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     base_url = "https://miktyres.ru/articles/podbor_po_parametram/"
#     driver.get(base_url)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver
