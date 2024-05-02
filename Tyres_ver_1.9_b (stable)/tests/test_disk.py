from Settings.browser_params import *
from Cases.t_cases_disk import *
from Pages.disk_func import *


@pytest.mark.parametrize("""width_opt_num, diameter_opt_num, pcd_opt_num,
                        et_opt_num, dia_opt_num, manufacturer_opt_num, expected_url""", data_disk_nums(test_cases))
def test_disk(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num,
              dia_opt_num, manufacturer_opt_num, expected_url):

    test = DiskFunc(driver, width_opt_num, diameter_opt_num, pcd_opt_num, et_opt_num,
                    dia_opt_num, manufacturer_opt_num)

    test.test_click(test.select_width())
    test.wait_elem_loc(select_width_options)
    test.width_options_to_select_click()

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

    assert ec.url_changes(expected_url)

    driver.quit()
