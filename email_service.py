from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from itertools import cycle
import requests
import re
import os
import csv
# import pandas as pd
import json
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
# from fastapi import FastAPI, Query
def get_email(username,password):
    chrome_options=Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service, options=chrome_options)
    wait=WebDriverWait(driver,20)

    driver.get("https://provar.io/webmail")
    # time.sleep(20)
    username_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#user')))
    username_btn.send_keys(username)
    time.sleep(3)
    password_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#pass')))
    password_btn.send_keys(password)
    time.sleep(4)
    login=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#login_submit')))
    login.click()
    time.sleep(7)
    inbox_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#taskmenu .selected")))
    inbox_btn.click()
    time.sleep(3)
    first_message=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#rcmrowMw td.subject')))
    first_message.click()
    time.sleep(4)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#messagecontframe"))
    )

    driver.switch_to.frame(iframe)

    # Now find the message body
    message_raw = driver.find_element(By.XPATH, '//*[@id="messagebody"]')
    # print(message_raw.text)
    message= message_raw.text
    # print(message.text)
    driver.quit()
    return message


username="forward2@provar.io"
password='alaapassword'
message=get_email(username,password)
print(message)