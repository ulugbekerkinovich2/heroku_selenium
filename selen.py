import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
# driver = webdriver.Chrome(executable_path="C:/Users/ulugbek/PycharmProjects/deploy_heroku_selenium/chromedriver")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print('ornatildi')
driver.get("https://www.lsgeotar.ru/pages/abc-pharma_tn.html")
time.sleep(15)
links = driver.find_elements(By.TAG_NAME, 'a')
# print("Opened database successfully")
list_links = []
my_links = []
ettdb_links = []
a = 0

for link in links:
    link_l = link.get_attribute('href')
    # print(link.get_attribute('href'), a)
    a += 1

    if 24 <= a < 57:
        my_links.append(link_l)

    if 59 <= a < 110:
        if a % 2 == 0:
            list_links.append(link_l)
print(list_links)

time.sleep(10)
driver.close()