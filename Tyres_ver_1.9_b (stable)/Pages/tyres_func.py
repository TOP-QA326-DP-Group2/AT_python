from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Settings.browser_params import driver
from Pages.tyres_locators import *


class TyresFunc:
    # Атрибуты
    def __init__(self, driver, width_opt_num, height_opt_num, diameter_opt_num, season_opt_num,
                 manufacturer_opt_num):
        self.driver = driver
        self.width_opt_num = width_opt_num
        self.height_opt_num = height_opt_num
        self.diameter_opt_num = diameter_opt_num
        self.season_opt_num = season_opt_num
        self.manufacturer_opt_num = manufacturer_opt_num

        self.width_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')
        self.height_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div/div/ul/li[{height_opt_num}]')
        self.diameter_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div/div/ul/li[{diameter_opt_num}]')
        self.season_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div/div/ul/li[{season_opt_num}]')
        self.manufacturer_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div/div/ul/li[{manufacturer_opt_num}]')
        self.submit_button = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[7]/div/input')

    # Методы
    def find(self, args):
        return self.driver.find_element(*args)

    def test_click(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def wait_elem_loc(self, args):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(args))

    # width:
    def select_width(self):
        return self.find(select_width)

    def select_width_options(self):
        return self.find(select_width_options)

    def width_options_to_select_click(self):
        self.width_options_to_select.click()

    # height:
    def select_height(self):
        return self.find(select_height)

    def select_height_options(self):
        return self.find(select_height_options)

    def height_options_to_select_click(self):
        self.height_options_to_select.click()

    # diameter:
    def select_diameter(self):
        return self.find(select_diameter)

    def select_diameter_options(self):
        return self.find(select_diameter_options)

    def diameter_options_to_select_click(self):
        self.diameter_options_to_select.click()

    # season:
    def select_season(self):
        return self.find(select_season)

    def select_season_options(self):
        return self.find(select_season_options)

    def season_options_to_select_click(self):
        self.season_options_to_select.click()

    # manufacturer:
    def select_manufacturer(self):
        return self.find(select_manufacturer)

    def select_manufacturer_options(self):
        return self.find(select_manufacturer_options)

    def manufacturer_options_to_select_click(self):
        self.manufacturer_options_to_select.click()

    # submit_button

    def submit_button_find(self):
        return self.find(button)

    def submit_button_click(self):
        self.submit_button.click()
