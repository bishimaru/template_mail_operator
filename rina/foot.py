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
return_foot_message = """はじめまして、りなです。
私のプロフィールを見てくださって、ありがとうございます！

私は趣味でゲームや映画、お酒を楽しんだりしています(*'▽'*)
まだ20代のうちに楽しみたいと思って、恋人というより長期的なせふれ関係になれる人を探しています♪
でもいきなりそんな関係になるのは難しいと思うので、ゆっくり信頼関係を深められたらと思いますm(_ _)m

もしせふれさんを探していたらメッセージもらえると嬉しいです！"""

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
  print('=== エラー内容 ===')
  print(traceback.format_exc())
  print('type:' + str(type(e)))
  print('args:' + str(e.args))
  print('message:' + e.message)
  print('e自身:' + str(e))
driver.quit()