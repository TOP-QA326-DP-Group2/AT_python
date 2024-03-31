def data_tyres_nums(data):
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['height_opt_num'], l['diameter_opt_num'],
                   l['season_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data

# Перед началом теста ОБЯЗАТЕЛЬНО проверить, что в адресе размещения тестовых данных
# указан Absolute path (полный путь к месту размещения файла)!!!
with open(r"D:\QA\Diplom\AT\test_framework\Tyres_ver_1.9_a (stable)\Cases\t_cases_tyres_v2.txt", "r", encoding="UTF-8") as file:
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
