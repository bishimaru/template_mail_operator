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


name = "ゆりあ"
happy_windowhandle = "649D6CFA6496F61AB58D2762E7DC99B7"
pcmax_windowhandle = "F88DA50E170152B3DB70FADC8465375A"


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