def data_disk_nums(data):  # задаем функцию, которая будет передавать
                           # тестовые параметры для подстановки в методы классов
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'],
                   l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data

# Перед началом теста ОБЯЗАТЕЛЬНО проверить, что в адресе размещения тестовых данных
# указан Absolute path (полный путь к месту размещения файла)!!!
with open(r"D:\QA\Diplom\AT\test_framework\Tyres_ver_1.9_a (stable)\Cases\t_cases_disk_v2.txt",
          "r", encoding="UTF-8") as file:  # читаем тестовые данные из файла
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:  # исключаем первую строку файла с названием столбцов
    try:
        test_case = {"width_opt_num": i[0], "diameter_opt_num": i[1], "pcd_opt_num": i[2], "et_opt_num": i[3],
                     "dia_opt_num": i[4], "manufacturer_opt_num": i[5],
                     "expected_url": "https://miktyres.ru/articles/podbor_po_parametram/"}
                    #  назначаем переменным индексы считываемых данных списков, expected_url - задаем ожидаемый URL
                    #  expected_url при успешном тесте изменяется
        test_cases.append(test_case)
    except:
        pass
