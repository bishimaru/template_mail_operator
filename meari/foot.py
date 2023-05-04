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


name = "めあり"
happy_windowhandle = "124D67E48565CA12094A6FCC4604EE5E"
pcmax_windowhandle = "DD43F375299CCBDA554874BE608F2198"
return_foot_message = """足跡ありがとうございます！
ホテルで働いている『めあり』って言います◯

前のせふれさんが職場が遠くなって会えなくなってしまったので、新しいせふれさんを探していますm(_ _)m

性欲強めな私とのせふれ関係に興味ありませんか？？"""

if len(sys.argv) < 2:
  cnt = 20
else:
  cnt = int(sys.argv[1])
options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:   
  happymail.return_footpoint(name,happy_windowhandle, driver, return_foot_message, cnt)
except Exception as e:
  print('error')
driver.quit()