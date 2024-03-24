import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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


def data_tyres_nums(data):
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['height_opt_num'], l['diameter_opt_num'],
                   l['season_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


# with open(r"test_cases_tyres_v2.txt", "r", encoding="UTF-8") as file: #работает при запуске testing_data.py
with open(r"pages\test_cases_tyres_v2.txt", "r", encoding="UTF-8") as file:  # работает при запуске тестов
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:
    try:
        test_case = {"width_opt_num": i[0], "height_opt_num": i[1], "diameter_opt_num": i[2], "season_opt_num": i[3],
                     "manufacturer_opt_num": i[4],
                     "expected_url": "https://miktyres.ru/articles/podbor_po_parametram/"}
        test_cases.append(test_case)
    except:
        pass


@pytest.mark.parametrize('width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num, expected_url', data_tyres_nums(test_cases))
def test_tyres(driver, width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num, expected_url):

    current_url = driver.current_url

    # width
    select_width = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div')
    driver.execute_script("arguments[0].click();", select_width)
    select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_width_options))  # Ожидаем, пока опции выпадающего списка загрузятся
    width_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')  #  подставляем переменную с номером элемента выпадающего списка
    width_options_to_select.click()

    # height
    select_height = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div')
    driver.execute_script("arguments[0].click();", select_height)
    select_height_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_height_options))
    height_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div/div/ul/li[{height_opt_num}]')
    height_options_to_select.click()

    # diameter
    select_diameter = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div')
    driver.execute_script("arguments[0].click();", select_diameter)
    select_diameter_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_diameter_options))
    diameter_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div/div/ul/li[{diameter_opt_num}]')
    diameter_options_to_select.click()

    # season
    select_season = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div')
    driver.execute_script("arguments[0].click();", select_season)
    select_season_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_season_options))
    season_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div/div/ul/li[{season_opt_num}]')
    season_options_to_select.click()

    # manufacturer
    select_manufacturer = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div')
    driver.execute_script("arguments[0].click();", select_manufacturer)
    select_manufacturer_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_manufacturer_options))
    manufacturer_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div/div/ul/li[{manufacturer_opt_num}]')
    manufacturer_options_to_select.click()

    # submit_button - NOT DONE
    button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[6]/div/input')))
    button.click()  # После выполнения всех действий закрываем браузер
    driver.quit()

    assert ec.url_changes(current_url)
