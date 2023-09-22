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
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, mail_reception_check
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import sqlite3
from datetime import timedelta

# order_list = ["あすか", "彩香","えりか", "haru...", "haru","きりこ","めあり","ももか","ゆうこ", 
#                "りこ","りな","ハル", "波留（はる）" ]
order_list = ["めあり", ]

def get_driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=456,912")
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-cache")
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    # driver = func.get_debug_chromedriver()
    wait = WebDriverWait(driver, 15)
    return driver, wait

def check_mail():
  for order_name in order_list:
     # ハッピーメール
    driver, wait = get_driver()
    x = happymail.check_new_mail(driver, wait, order_name)
    print(1234)
    print(x)


if __name__ == '__main__':
   check_mail()