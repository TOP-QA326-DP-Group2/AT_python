from Settings.browser_params import *  # подключаем настройки WebdDiver и браузера
from Cases.t_cases_disk import *  # подключаем тест-кейсы (наборы тестовых данных)
from Pages.disk_func import *  # подключаем классы и методы взаимодействия с элементами страницы


@pytest.mark.parametrize("""width_opt_num, diameter_opt_num, pcd_opt_num,
                        et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url""", data_disk_nums(test_cases))
# прописываем параметризацию теста, описываем откуда будем брать тестовые данные и функцию,
# которая предоставит переменные для подстановки данных и поиска элементов для выбора
def test_disk(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num,
              dia_opt_num, manufacturer_opt_num, expected_url):
    # тест, в котором помимо тестовых данных будем проверять, изменился ли "expected_url"

    test = DiskFunc(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num,
                    dia_opt_num, manufacturer_opt_num)
    # обращаемся к классу, который описывает механизмы взаимодействия с элементами страницы

    test.test_click(test.select_width())  # кликаем на выпадающем меню
    test.wait_elem_loc(select_width_options)  # ждем, пока все элементы выпадающего меню будут доступны для выбора
    test.width_options_to_select_click()  # кликаем на нужном элементе списка в выпадающем
                                          # меню согласно индекса данного элемента (индекс берем из тест-кейсов)

    test.test_click(test.select_diameter())
    test.wait_elem_loc(select_diameter_options)
    test.diameter_options_to_select_click()

    test.test_click(test.select_diameter())
    test.wait_elem_loc(select_diameter_options)
    test.diameter_options_to_select_click()

    test.test_click(test.select_pcd())
    test.wait_elem_loc(select_pcd_options)
    test.pcd_options_to_select_click()

    test.test_click(test.select_et())
    test.wait_elem_loc(select_et_options)
    test.et_options_to_select_click()

    test.test_click(test.select_dia())
    test.wait_elem_loc(select_dia_options)
    test.dia_options_to_select_click()

    test.test_click(test.select_manufacturer())
    test.wait_elem_loc(select_manufacturer_options)
    test.manufacturer_options_to_select_click()

    test.wait_elem_loc(button)
    test.submit_button_click()

    assert ec.url_changes(expected_url)  # проверяем, что ожидаемый результат (expected_url - страница подбора) -
                                         # изменился после подстановки тестовых данных и нажатия кнопки подтверждения

    driver.quit()
