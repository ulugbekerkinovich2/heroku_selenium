import os
import time

import requests
from django.db import connection
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.db import connection

from test import telebots


def selenium_upload1():
    # API_TOKEN = '2090467761:AAHh3xty_m8W7TuiIGs_49zUUJM22pLUdbk'
    cursor = connection.cursor()
    time.sleep(2)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    # driver = webdriver.Chrome(executable_path="C:/Users/ulugbek/PycharmProjects/deploy_heroku_selenium/chromedriver")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print('ornatildi')
    cursor.execute("SELECT FROM link")
    all_data = cursor.fetchalL()
    print(all_data)
    print(all_data[0][-1])
    # driver.get(f"{all_data[0][-1]}")
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
            # requests.get(
            #     url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={link_l}")
            telebots(link_l)
            time.sleep(3)
            cursor.execute("INSERT INTO  link  (link) VALUES (%s)", link_l)

            if 59 <= a < 110:
                if a % 2 == 0:
                    list_links.append(link_l)
                    print('2', link_l)
                    # requests.get(
                    #     url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={link_l}")
                    telebots(link_l)
                    time.sleep(3)
                    cursor.execute("INSERT INTO  link  (link) VALUES (%s)", link_l)
            a += 1
            print(list_links)

            # time.sleep(10)

            driver.close()


selenium_upload1()
