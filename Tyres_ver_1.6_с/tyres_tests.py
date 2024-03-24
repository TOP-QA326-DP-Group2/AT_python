from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser_test_params import *
from tests_data.test_cases import *


@pytest.mark.parametrize('width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num, expected_url', data_tyres_nums(test_cases))
def test_tyres(driver, width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num, expected_url):

    current_url = driver.current_url

    # width
    select_width = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div')
    driver.execute_script("arguments[0].click();", select_width)
    select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul')
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(select_width_options))
    width_options_to_select = driver.find_element(By.XPATH, f'//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')
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

    # submit_button
    button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[6]/div/input')))
    button.click()
    driver.quit()

    assert ec.url_changes(current_url)


