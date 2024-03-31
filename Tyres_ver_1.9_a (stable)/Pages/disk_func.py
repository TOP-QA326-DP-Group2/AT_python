from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Settings.browser_params import driver
from Pages.disk_locators import *


class DiskFunc:
    # Атрибуты
    def __init__(self, driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num, dia_opt_num,
                 manufacturer_opt_num):
        self.driver = driver
        self.width_opt_num = width_opt_num
        self.diameter_opt_num = diameter_opt_num
        self.pcd_opt_num = pcd_opt_num
        self.et_opt_num = et_opt_num
        self.dia_opt_num = dia_opt_num
        self.manufacturer_opt_num = manufacturer_opt_num

        self.width_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul/li[{width_opt_num}]')
        self.diameter_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul/li[{diameter_opt_num}]')
        self.pcd_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul/li[{pcd_opt_num}]')
        self.et_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul/li[{et_opt_num}]')
        self.dia_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul/li[{dia_opt_num}]')
        self.manufacturer_options_to_select = driver.find_element(By.XPATH,
                            f'//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul/li[{manufacturer_opt_num}]')

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

    # diameter:
    def select_diameter(self):
        return self.find(select_diameter)

    def select_height_options(self):
        return self.find(select_diameter_options)

    def diameter_options_to_select_click(self):
        self.diameter_options_to_select.click()

    # pcd:
    def select_pcd(self):
        return self.find(select_pcd)

    def select_pcd_options(self):
        return self.find(select_pcd_options)

    def pcd_options_to_select_click(self):
        self.pcd_options_to_select.click()

    # et:
    def select_et(self):
        return self.find(select_et)

    def select_et_options(self):
        return self.find(select_et_options)

    def et_options_to_select_click(self):
        self.et_options_to_select.click()

    # dia:
    def select_dia(self):
        return self.find(select_dia)

    def select_dia_options(self):
        return self.find(select_dia_options)

    def dia_options_to_select_click(self):
        self.dia_options_to_select.click()

    # manufacturer:
    def select_manufacturer(self):
        return self.find(select_manufacturer)

    def select_manufacturer_options(self):
        return self.find(select_manufacturer_options)

    def manufacturer_options_to_select_click(self):
        self.manufacturer_options_to_select.click()
