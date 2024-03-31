from Settings.browser_params import *
from Cases.t_cases_tyres import *
from Pages.tyres_func import *


@pytest.mark.parametrize("""width_opt_num, height_opt_num, diameter_opt_num,
                            season_opt_num, manufacturer_opt_num, expected_url""", data_tyres_nums(test_cases))
def test_tyres(driver, width_opt_num, height_opt_num, diameter_opt_num,
               season_opt_num, manufacturer_opt_num, expected_url):

    test = TyresFunc(driver, width_opt_num, height_opt_num, diameter_opt_num, season_opt_num, manufacturer_opt_num)

    test.test_click(test.select_width())
    test.wait_elem_loc(select_width_options)
    test.width_options_to_select_click()

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

    button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[7]/div/input')))
    button.click()

    assert ec.url_changes(expected_url)

    driver.quit()
