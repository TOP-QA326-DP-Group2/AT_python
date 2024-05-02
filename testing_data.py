def data_diski_nums(data):
    for i, l in enumerate(data):
        data[i] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'], l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data

# with open(r"test_cases_disk.txt", "r", encoding="UTF-8") as file: #работает при запуске testing_data.py
with open(r"pages\test_cases_disk.txt", "r", encoding="UTF-8") as file: #работает при запуске тестов
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params:
    test_case={}
    test_case["width_opt_num"] = i[0]
    test_case["diameter_opt_num"] = i[1]
    test_case["pcd_opt_num"] = i[2]
    test_case["et_opt_num"] = i[3]
    test_case["dia_opt_num"] = i[4]
    test_case["manufacturer_opt_num"] = i[5]
    test_case["expected_url"] = "https://miktyres.ru/articles/podbor_diski/"
    test_cases.append(test_case)

# test_cases = [
#     {
#         "width_opt_num": "10",
#         "diameter_opt_num": "10",
#         "pcd_opt_num": "10",
#         "et_opt_num": "10",
#         "dia_opt_num": "10",
#         "manufacturer_opt_num": "10",
#         "expected_url": "https://miktyres.ru/articles/podbor_diski/"
#     },
#     {
#         "width_opt_num": "2",
#         "diameter_opt_num": "2",
#         "pcd_opt_num": "2",
#         "et_opt_num": "2",
#         "dia_opt_num": "2",
#         "manufacturer_opt_num": "2",
#         "expected_url": "https://miktyres.ru/articles/podbor_diski/"
#     },
# ]