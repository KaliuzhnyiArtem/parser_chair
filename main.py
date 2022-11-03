from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_service = Service(executable_path='/Users/artem/desktop/Парсер/homeclub/chromedriver/chromedriver')
url = 'https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE'
driver = webdriver.Chrome(service=driver_service)


def write_data_in_file(article, availability_delivery, availability_poland, availability_lviv):
    # Записує отримані данні у файл homeclub.txt
    with open('homeclub.txt', 'a') as home_club_file:
        home_club_file.write(f'Артикуль: {article};\n'
                       f'Наявність для поставки: {availability_delivery};\n'
                       f'Прогноз наявності в Польщі: {availability_poland};\n'
                       f'Наявність у Львові: {availability_lviv}; ')


try:
    driver.get(url)
    time.sleep(3)
    datasite = driver.find_elements(By.XPATH, "//span[@class='value']")
    print('-'*20)
    write_data_in_file(article=datasite[2].text,
                       availability_delivery=datasite[3].text,
                       availability_poland=datasite[4].text,
                       availability_lviv=datasite[6].text,
                       )
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()









