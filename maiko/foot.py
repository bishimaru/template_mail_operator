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


name = "麻衣子"
happy_windowhandle = "C66F326AF9E31926A7727A6D79DCBA68"
pcmax_windowhandle = "090F734C2A64AF735B51D15B0901F802"
return_foot_message = """足跡ありがとうございます！！
声優志望の女子大生『麻衣子』です♪

ここではセックスパートナーを探してます！
エロいのキャラの声もやりたい♪

セフレというとサバサバしててやり捨てされるのが嫌なので、たくさんいちゃいちゃできて何回も会える人がいいです。
なのでセックスパートナーさん募集♪

もし同じ気持ちだったらメッセージもらいたいです！"""

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