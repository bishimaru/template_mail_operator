from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
import traceback
import setting
from selenium.webdriver.support.select import Select
from tkinter import filedialog

def mail_reception_check(happy_window_handle, pcmax_window_handle, gmail_window_handle, driver):
    print(2525)
    driver.switch_to.window(happy_window_handle)
    wait_time = random.uniform(2, 3)
    # TOPに戻る
    driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
    message_icon = driver.find_elements(By.CLASS_NAME, value="ds_nav_no_pickup")[2]
    new_message = message_icon.find_elements(By.CLASS_NAME, value="ds_red_circle")
    if len(new_message):
        print("newmessage")
    driver.quit()