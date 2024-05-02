from selenium.webdriver.common.by import By

# disk
# width
select_width = (By.XPATH, "//div[@id='column-left']/div/div[2]/div[3]/div/div")
select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[1]/div/div/ul')

# diameter
select_diameter = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div')
select_diameter_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[2]/div/div/ul')

# pcd
select_pcd = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div')
select_pcd_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[3]/div/div/ul')

# et
select_et = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div')
select_et_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[4]/div/div/ul')

# dia
select_dia = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div')
select_dia_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[5]/div/div/ul')

# manufacturer
select_manufacturer = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div')
select_manufacturer_options = (By.XPATH, '//*[@id="column-left"]/div/div[2]/div[3]/div[6]/div/div/ul')
