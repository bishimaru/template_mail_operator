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
from widget import pcmax, happymail
from selenium.webdriver.support.ui import WebDriverWait
import setting


name = "ゆあ&すみれ"
happy_windowhandle = "B6A833C61FC9E66870AD876B6221DD30"
pcmax_windowhandle = "236654B90E86E9FEC6C48964CD1D1FAB"


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:   
  happymail.re_post(name, setting.yua_happy_windowhandle, driver)
except Exception as e:
  print('777')
try:
  pcmax.re_post(name, setting.yua_pcmax_windowhandle, driver)
except Exception as e:
  print('777')
driver.quit()