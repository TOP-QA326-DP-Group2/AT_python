from Settings.browser_params import *  # подключаем настройки WebdDiver и браузера
from Cases.t_cases_tyres import *  # подключаем тест-кейсы (наборы тестовых данных)
from Pages.tyres_func import *  # подключаем классы и методы взаимодействия с элементами страницы


@pytest.mark.parametrize("""width_opt_num, height_opt_num, diameter_opt_num,
                            season_opt_num, manufacturer_opt_num, expected_url""", data_tyres_nums(test_cases))
# прописываем параметризацию теста, описываем откуда будем брать тестовые данные и функцию,
# которая предоставит переменные для подстановки данных и поиска элементов для выбора
def test_tyres(driver, width_opt_num, height_opt_num, diameter_opt_num,
               season_opt_num, manufacturer_opt_num, expected_url):
    # тест, в котором помимо тестовых данных будем проверять, изменился ли "expected_url"

    test = Tyres(driver, width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num)
    # обращаемся к классу, в котором описаны элементы фильтра подбора

    test.test_click(test.select_width())  # кликаем на выпадающем меню
    test.wait_elem_loc(select_width_options)  # ждем, пока все элементы выпадающего меню будут доступны для выбора
    test.width_options_to_select_click()  # кликаем на нужном элементе списка в выпадающем
                                          # меню согласно индекса данного элемента (индекс берем из тест-кейсов)
    test.test_click(test.select_height())
    test.wait_elem_loc(select_height_options)
    test.height_options_to_select_click()

    test.test_click(test.select_diameter())
    test.wait_elem_loc(select_diameter_options)
    test.diameter_options_to_select_click()

    test.test_click(test.select_season())
    test.wait_elem_loc(select_season_options)
    test.season_options_to_select_click()

    test.test_click(test.select_manufacturer())
    test.wait_elem_loc(select_manufacturer_options)
    test.manufacturer_options_to_select_click()

    test.wait_elem_loc(button)
    test.submit_button_click()

    # assert #1 проверяет, что ожидаемый результат (expected_url - страница подбора)
    # изменился после подстановки тестовых данных и нажатия кнопки подтверждения
    # assert #2 проверяет, что на экране отображается надпись с выбранными параметрами фильтра
    assert ec.url_changes(expected_url)
    assert ec.presence_of_element_located(title)

    driver.quit()
