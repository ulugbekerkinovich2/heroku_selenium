import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

API_TOKEN = '2090467761:AAHh3xty_m8W7TuiIGs_49zUUJM22pLUdbk'

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
# time.sleep(15)
links = driver.find_elements(By.TAG_NAME, 'a')
# print("Opened database successfully")
list_links = []
my_links = []
ettdb_links = []
a = 0
user = 935920479
for link in links:
    link_l = link.get_attribute('href')
    print(link.get_attribute('href'), a)

    if 24 <= a < 57:
        my_links.append(link_l)
        print('1', link_l)
        requests.get(
            url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={link_l}")
        time.sleep(3)

    if 59 <= a < 110:
        if a % 2 == 0:
            list_links.append(link_l)
            print('2', link_l)
            requests.get(
                url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={link_l}")
            time.sleep(3)
    a += 1
print(list_links)

# time.sleep(10)

driver.close()
