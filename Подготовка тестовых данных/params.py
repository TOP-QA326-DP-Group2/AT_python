#----------------------------------------------------- Диски ---------------------------------------------------------#
#------------------------ Создаём переменную params, содержащую список с данными для проверки -------------------------#
with open("test_cases_disk.txt", "r", encoding="UTF-8") as file:
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))

#---------------------------------------------- Пример вывода данных --------------------------------------------------#
for pair in params:
    width = pair[0]
    diameter = pair[1]
    pcd = pair[2]
    et = pair[3]
    dia = pair[4]
    manufacturer = pair[5]
    print(f"width = {width}, diameter = {diameter}, pcd = {pcd}, et = {et}, dia = {dia}, manufacturer = {manufacturer}")

#---------------------------------------------- Пример параметризации -------------------------------------------------#
@pytest.mark.parametrize("input_data", params)
def test_test(driver, input_data):
    width = input_data[0]
    diameter = input_data[1]
    pcd = input_data[2]
    et = input_data[3]
    dia = input_data[4]
    manufacturer = input_data[5]

#------------------------------------------------------ Шины ----------------------------------------------------------#
with open("test_cases_tyres.txt", "r", encoding="UTF-8") as file:
    params = file.read()
    file.close()
params = params.split("\n")
params = list(map(lambda x: list(x.split("\t")), params))

#---------------------------------------------- Пример параметризации -------------------------------------------------#
@pytest.mark.parametrize("input_data", params)
def test_test(driver, input_data):
    width = input_data[0]
    height = input_data[1]
    diameter = input_data[2]
    season = input_data[3]
    manufacturer = input_data[4]