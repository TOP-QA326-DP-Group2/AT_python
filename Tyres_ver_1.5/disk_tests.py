import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# #  headless режим, добавляем from 'selenium.webdriver.chrome.options import Option'
# @pytest.fixture()
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     base_url = "https://miktyres.ru/articles/podbor_diski/"
#     driver.get(base_url)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver

#  обычный режим, убираем from 'selenium.webdriver.chrome.options import Option'
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    base_url = "https://miktyres.ru/articles/podbor_po_parametram/"
    driver.get(base_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver


def data_diski_nums(data):
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'],
                   l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


# with open(r"test_cases_disk_v2.txt", "r", encoding="UTF-8") as file: #работает при запуске testing_data.py
with open(r"pages\test_cases_disk_v2.txt", "r", encoding="UTF-8") as file:  # работает при запуске тестов
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:
    try:
        test_case = {"width_opt_num": i[0], "diameter_opt_num": i[1], "pcd_opt_num": i[2], "et_opt_num": i[3],
                     "dia_opt_num": i[4], "manufacturer_opt_num": i[5],
                     "expected_url": "https://miktyres.ru/articles/podbor_po_parametram/"}
        test_cases.append(test_case)
    except:
        pass


@pytest.mark.parametrize('width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url', data_diski_nums(test_cases))
def test_disks(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url):
    current_url = driver.current_url
    # width
    select_width = driver.find_element(By.XPATH, "//div[@id='column-left']/div/div[2]/div[3]/div/div")
    driver.execute_script("arguments[0].click();", select_width)
    select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_width_options))  # Ожидаем, пока опции выпадающего списка загрузятся
    width_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')  #  подставляем переменную с номером элемента выпадающего списка
    width_options_to_select.click()

    # diameter
    select_diameter = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div')
    driver.execute_script("arguments[0].click();", select_diameter)
    select_diameter_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_diameter_options))
    diameter_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul/li[{diameter_opt_num}]')
    diameter_options_to_select.click()

    # pcd
    select_pcd = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div')
    driver.execute_script("arguments[0].click();", select_pcd)
    select_pcd_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_pcd_options))
    pcd_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul/li[{pcd_opt_num}]')
    pcd_options_to_select.click()

    # et
    select_et = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div')
    driver.execute_script("arguments[0].click();", select_et)
    select_et_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_et_options))
    et_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul/li[{et_opt_num}]')
    et_options_to_select.click()

    # dia
    select_dia = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div')
    driver.execute_script("arguments[0].click();", select_dia)
    select_dia_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_dia_options))
    dia_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul/li[{dia_opt_num}]')
    dia_options_to_select.click()

    # manufacturer
    select_manufacturer = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div')
    driver.execute_script("arguments[0].click();", select_manufacturer)
    select_manufacturer_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_manufacturer_options))
    manufacturer_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul/li[{manufacturer_opt_num}]')
    manufacturer_options_to_select.click()

    button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[7]/div/input')))  # Ожидаем, пока кнопка станет кликабельной
    button.click()  # После выполнения всех действий закрываем браузер
    driver.quit()

    assert ec.url_changes(current_url)
