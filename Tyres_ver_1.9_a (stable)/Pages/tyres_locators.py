from selenium.webdriver.common.by import By

# tyres
# width
select_width = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div')
select_width_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[1]/div/div/ul')

# height
select_height = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div')
select_height_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[2]/div/div/ul')

# diameter
select_diameter = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div')
select_diameter_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[3]/div/div/ul')

# season
select_season = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div')
select_season_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[4]/div/div/ul')

# manufacturer
select_manufacturer = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div')
select_manufacturer_options = (By.XPATH, '//*[@id="column-left"]/div/div[1]/div[3]/div[5]/div/div/ul')
