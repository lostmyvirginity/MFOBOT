from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import os
import time
import random

service = Service("C:\\Users\\Jan.Dabrowski\\Desktop\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 

driver = webdriver.Chrome(service = service, options= options)

nazwa = ''
haslo = ''

def dol():
    ActionChains(driver).key_down(Keys.ARROW_DOWN) \
                        .pause(random.uniform(0.1, 0.7)) \
                        .key_up(Keys.ARROW_DOWN) \
                        .perform()


def lewo():
    ActionChains(driver).key_down(Keys.ARROW_LEFT) \
                        .pause(random.uniform(0.1, 0.7)) \
                        .key_up(Keys.ARROW_LEFT) \
                        .perform()


def gora():
    ActionChains(driver).key_down(Keys.ARROW_UP) \
                        .pause(random.uniform(0.1, 0.7)) \
                        .key_up(Keys.ARROW_UP) \
                        .perform()


def prawo():
    ActionChains(driver).key_down(Keys.ARROW_RIGHT) \
                        .pause(random.uniform(0.1, 0.7))\
                        .key_up(Keys.ARROW_RIGHT) \
                        .perform()
    

def main():
    global mfoid
    driver.find_element(By.NAME, value ="login").send_keys(nazwa)
    driver.find_element(By.NAME, value = "password").send_keys(haslo)
    driver.find_element(By.CLASS_NAME, value = 'submit').click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, value = 'button-text').click()
    time.sleep(3)
    driver.get_cookies()
    mfoid = driver.find_element(By.CLASS_NAME, value = 'TopPanel').get_attribute('id')
    playerid = driver.find_element(By.CLASS_NAME, value = 'PlayerInfo').get_attribute('id')
    potionsid = driver.find_element(By.XPATH, value = '//*[@class="WidgetBox LayoutBox2 ItemsWidget-cnt panel"]').get_attribute('id')
    punktyruchu = driver.find_element(By.XPATH, value = '//*[@id="' + mfoid + '_energy"]').get_attribute('innerText')
    obecnezycie = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_HP"]').get_attribute('current')
    maxzycie = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_HP"]').get_attribute('max')
    obecnamana = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_MP"]').get_attribute('current')
    maxmana = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_MP"]').get_attribute('max')
    obecnyexp = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_progress"]').get_attribute('current')
    lvlup = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_progress"]').get_attribute('max')

    os.system('cls')
    
    print("Punkty doswiadczenia: ", obecnyexp, "/", lvlup, '\n\n\n\n')
    time.sleep(3)

    ruch = [prawo, lewo]
    #ruch = [gora,dol, prawo, lewo]
    if int(obecnezycie) < 1400:
        driver.find_element(By.XPATH, value = '//*[@id="' + potionsid + '_widget_heal"]/div[1]/div[2]/div[2]/div[2]').click()
        time.sleep(2)
    if int(obecnamana) < 30:
        driver.find_element(By.XPATH, value = '//*[@id="' + potionsid + '_widget_heal"]/div[1]/div[3]/div[2]/div[2]').click()
        time.sleep(2)
    while True:
        punktyruchu = driver.find_element(By.XPATH, value = '//*[@id="' + mfoid + '_energy"]').get_attribute('innerText')
        obecnezycie = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_HP"]').get_attribute('current')
        obecnamana = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_MP"]').get_attribute('current')
        if int(obecnezycie) < 1400:
            driver.find_element(By.XPATH, value = '//*[@id="' + potionsid + '_widget_heal"]/div[1]/div[2]/div[2]/div[2]').click()
            time.sleep(2)
        if int(obecnamana) < 30:
            driver.find_element(By.XPATH, value = '//*[@id="' + potionsid + '_widget_heal"]/div[1]/div[3]/div[2]/div[2]').click()
            time.sleep(2)
        while int(obecnezycie) >= 1400 and int(obecnamana) >= 30:
            punktyruchu = driver.find_element(By.XPATH, value = '//*[@id="' + mfoid + '_energy"]').get_attribute('innerText')
            obecnezycie = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_HP"]').get_attribute('current')
            obecnamana = driver.find_element(By.XPATH, value = '//*[@id="' + playerid + '_MP"]').get_attribute('current')
            random.choice(ruch)()
            print('Twoje punkty ruchu', punktyruchu, '\n', 'Życie:', str(obecnezycie) + '/' + str(maxzycie), '\n', 'Mana:', str(obecnamana) + '/' + str(maxmana))

        if int(punktyruchu) == 0 or int(obecnezycie) == 1:
            break
    time.sleep(3)
    os.system('cls')
    print("Punkty doswiadczenia: ", obecnyexp, "/", lvlup)


driver.get('https://mfo3.pl')
if __name__ == '__main__':
    main()
    driver.quit()
