def data_disk_nums(data):
    for k, l in enumerate(data):
        data[k] = (l['width_opt_num'], l['diameter_opt_num'], l['pcd_opt_num'],
                   l['et_opt_num'], l['dia_opt_num'], l['manufacturer_opt_num'], l['expected_url'])
    return data


with open(r"Cases/t_cases_disk_v2.txt", "r", encoding="UTF-8") as file:
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))
test_cases = []
for i in params[1:]:
    try:
        test_case = {"width_opt_num": i[0], "diameter_opt_num": i[1], "pcd_opt_num": i[2], "et_opt_num": i[3],
                     "dia_opt_num": i[4], "manufacturer_opt_num": i[5],
                     "expected_url": "https://miktyres.ru/articles/podbor_po_parametram/"}
        test_cases.append(test_case)
    except:
        pass
