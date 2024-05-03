from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Settings.browser_params import driver
from Pages.disk_locators import *


class Disk:  # задаем класс, описывающий взаимодействие с элементами на странице
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

        # далее прописываем элементы, которые будем искать в выпадающих списках,
        # подставляя в элементы выпадающих списков индексы, считанные в файле "t_cases_disk.py"
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
        self.submit_button = driver.find_element(*button)

    # Методы класса - тут описываем функции, которые отвечают за механику
    # непосредственного взаимодействия с элементами страницы
    def find(self, args):                       # функция, которая возвращает найденный
        return self.driver.find_element(*args)  # на странице элемент (берет локатор элемента в "disk_locators.py")

    def test_click(self, element):      # функция через обращение к коду JS осуществляет нажатие на выпадающий список и
        return self.driver.execute_script("arguments[0].click();", element)  # отображение элементов выпадающего списка

    def wait_elem_loc(self, args):  # ожидание отображения элементов
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(args))

    # width:
    def select_width(self):  # поиск элемента с выпадающим списком
        return self.find(select_width)

    def select_width_options(self):             # поиск элементов, которые доступны
        return self.find(select_width_options)  # для нажатия (взаимодействия) в выпадающем списке

    def width_options_to_select_click(self):  # непосредственное нажатие на элемент выпадающего списка
        self.width_options_to_select.click()

    # diameter:  # аналогично элементам width
    def select_diameter(self):
        return self.find(select_diameter)

    def select_height_options(self):
        return self.find(select_diameter_options)

    def diameter_options_to_select_click(self):
        self.diameter_options_to_select.click()

    # pcd:  # аналогично элементам width
    def select_pcd(self):
        return self.find(select_pcd)

    def select_pcd_options(self):
        return self.find(select_pcd_options)

    def pcd_options_to_select_click(self):
        self.pcd_options_to_select.click()

    # et:  # аналогично элементам width
    def select_et(self):
        return self.find(select_et)

    def select_et_options(self):
        return self.find(select_et_options)

    def et_options_to_select_click(self):
        self.et_options_to_select.click()

    # dia:  # аналогично элементам width
    def select_dia(self):
        return self.find(select_dia)

    def select_dia_options(self):
        return self.find(select_dia_options)

    def dia_options_to_select_click(self):
        self.dia_options_to_select.click()

    # manufacturer:  # аналогично элементам width
    def select_manufacturer(self):
        return self.find(select_manufacturer)

    def select_manufacturer_options(self):
        return self.find(select_manufacturer_options)

    def manufacturer_options_to_select_click(self):
        self.manufacturer_options_to_select.click()

    # submit_button

    def submit_button_find(self):  # поиск кнопки подтверждения выбора
        return self.find(button)

    def submit_button_click(self):  # нажатие кнопки подтверждения выбора
        self.submit_button.click()
