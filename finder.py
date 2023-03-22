# import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
from selenium import webdriver
import multiprocessing
import multiprocessing.connection
import time
import sys
import random
from datetime import datetime

import os

if __name__ == "__main__":

    # clients = [
    #     {  # 4000
    #         "username": "meriemkhaalef@gmail.com",
    #         "password": "7el9ouma",

    #     },
    # ]

    file = "./Sport.wav"
    
    trouv=0

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.studefi.fr/main.php#listRes")

    while trouv == 0:
        try:
            time.sleep(5)
            browser.refresh()
            time.sleep(10)

            # browser.execute_script("window.scrollTo(0, 70)")
            
            try:
                disponibles = list(browser.find_elements(
                    By.XPATH,
                    f"//img[@src = 'images/map/marker-residence_logements_disponibles.png']",
                ))
                if len(disponibles) > 1:
                    os.system("paplay " + file)
            except:
                time.sleep(5)
        except:
            continue
