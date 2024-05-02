import os


def data_disk_nums(data):  # задаем функцию, которая будет передавать
                           # тестовые параметры для подстановки в методы классов
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'],
                   l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 't_cases_disk_low_data.txt')
with open(file_path, "r", encoding="UTF-8") as file:  # читаем тестовые данные из файла
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:  # исключаем первую строку файла с названием столбцов
    try:
        test_case = {"width_opt_num": i[0], "diameter_opt_num": i[1], "pcd_opt_num": i[2], "et_opt_num": i[3],
                     "dia_opt_num": i[4], "manufacturer_opt_num": i[5],
                     "expected_url": "https://miktyres.ru/buy/"}
                    #  назначаем переменным индексы считываемых данных списков, expected_url - задаем ожидаемый URL
                    #  expected_url при успешном тесте изменяется
        test_cases.append(test_case)
    except:
        pass
