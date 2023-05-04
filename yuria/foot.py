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
return_foot_message = """足跡からです！ゆりあって言います♪
都内で不動産関係のOLをしています！

仕事に少し慣れてきたこともあり、仕事終わりにお家に帰ると人肌恋しさを感じるようになってきました(>_<)
いっぱいいちゃいちゃできるようなせふれさんとここで出会えたらいいなって思ってます( ´ ▽ ` )

同じように人肌恋しいって感じたことありませんか？？
"""

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