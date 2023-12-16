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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta
import sqlite3

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
    
    return driver

def sb_h_registration(name): 
  
  driver = get_driver()

  
  
  try:
     happymail.re_registration(name, driver)
  except Exception as e:
    
    print(traceback.format_exc())
    func.send_error(f"{name}", traceback.format_exc())
  driver.quit()


if __name__ == '__main__':
  if len(sys.argv) > 1:
    name = str(sys.argv[1])
    
  sb_h_registration(name)

  