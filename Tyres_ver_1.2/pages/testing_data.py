def data_diski_nums(data):
    for i, l in enumerate(data):
        data[i] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'], l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


test_cases = [
    {
        "width_opt_num": "10",
        "diameter_opt_num": "10",
        "pcd_opt_num": "10",
        "et_opt_num": "10",
        "dia_opt_num": "10",
        "manufacturer_opt_num": "10",
        "expected_url": "https://miktyres.ru/articles/podbor_diski/"
    },
    {
        "width_opt_num": "2",
        "diameter_opt_num": "2",
        "pcd_opt_num": "2",
        "et_opt_num": "2",
        "dia_opt_num": "2",
        "manufacturer_opt_num": "2",
        "expected_url": "https://miktyres.ru/articles/podbor_diski/"
    },
]