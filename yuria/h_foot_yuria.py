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
import traceback

def h_foot(cnt):
  name = "ゆりあ"
  return_foot_message = """足跡からです！ゆりあって言います♪
  都内で不動産関係のOLをしています！

  仕事に少し慣れてきたこともあり、仕事終わりにお家に帰ると人肌恋しさを感じるようになってきました(>_<)
  いっぱいいちゃいちゃできるようなせふれさんとここで出会えたらいいなって思ってます( ´ ▽ ` )

  同じように人肌恋しいって感じたことありませんか？？
  """
  
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.return_footpoint(name, setting.yuria_happy_windowhandle, driver, return_foot_message, cnt)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_foot(cnt)