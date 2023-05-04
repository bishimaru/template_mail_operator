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


name = "rina"
happy_windowhandle = "504D4E1934235E88D40946D7223DA77A"
pcmax_windowhandle = "A8940E1D39C82A9733E8BCA8F7A8B9BF"


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:   
  happymail.re_post(name,happy_windowhandle, driver)
except Exception as e:
  print('777')
try:
  pcmax.re_post(name, pcmax_windowhandle, driver)
except Exception as e:
  print('777')
driver.quit()