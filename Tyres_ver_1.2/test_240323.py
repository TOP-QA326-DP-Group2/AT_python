import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from pages.testing_data import *


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    current_url = "https://miktyres.ru/articles/podbor_diski/"
    driver.get(current_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver


@pytest.mark.parametrize('width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url', data_diski_nums(test_cases))
def test_message_page(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url):
    current_url = driver.current_url
    # width
    select_width = driver.find_element(By.XPATH, "//div[@id='column-left']/div/div[2]/div[3]/div/div")
    driver.execute_script("arguments[0].click();", select_width)
    select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_width_options))  # Ожидаем, пока опции выпадающего списка загрузятся
    width_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')  #  подставляем переменную с номером элемента выпадающего списка
    width_options_to_select.click()

    # diameter
    select_diameter = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div')
    driver.execute_script("arguments[0].click();", select_diameter)
    select_diameter_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_diameter_options))
    diameter_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul/li[{diameter_opt_num}]')
    diameter_options_to_select.click()

    # pcd
    select_pcd = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div')
    driver.execute_script("arguments[0].click();", select_pcd)
    select_pcd_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_pcd_options))
    pcd_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul/li[{pcd_opt_num}]')
    pcd_options_to_select.click()

    # et
    select_et = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div')
    driver.execute_script("arguments[0].click();", select_et)
    select_et_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_et_options))
    et_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul/li[{et_opt_num}]')
    et_options_to_select.click()

    # dia
    select_dia = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div')
    driver.execute_script("arguments[0].click();", select_dia)
    select_dia_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_dia_options))
    dia_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul/li[{dia_opt_num}]')
    dia_options_to_select.click()

    # manufacturer
    select_manufacturer = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div')
    driver.execute_script("arguments[0].click();", select_manufacturer)
    select_manufacturer_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_manufacturer_options))
    manufacturer_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul/li[{manufacturer_opt_num}]')
    manufacturer_options_to_select.click()

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[7]/div/input')))  # Ожидаем, пока кнопка станет кликабельной
    button.click()  # После выполнения всех действий закрываем браузер
    time.sleep(5)
    driver.quit()

    assert ec.url_changes(current_url)
