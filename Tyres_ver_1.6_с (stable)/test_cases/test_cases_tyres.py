def data_tyres_nums(data):
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['height_opt_num'], l['diameter_opt_num'],
                   l['season_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


with open(r"test_cases/test_cases_tyres_v2.txt", "r", encoding="UTF-8") as file:  # работает при запуске тестов
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:
    try:
        test_case = {"width_opt_num": i[0], "height_opt_num": i[1], "diameter_opt_num": i[2], "season_opt_num": i[3],
                     "manufacturer_opt_num": i[4],
                     "expected_url": "https://miktyres.ru/articles/podbor_po_parametram/"}
        test_cases.append(test_case)
    except:
        pass
