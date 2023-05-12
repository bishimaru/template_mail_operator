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
import traceback
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail
from selenium.webdriver.support.ui import WebDriverWait
import setting

def h_foot(cnt):
  name = "rina"
  return_foot_message = """はじめまして、りなです。
  私のプロフィールを見てくださって、ありがとうございます！

  私は趣味でゲームや映画、お酒を楽しんだりしています(*'▽'*)
  まだ20代のうちに楽しみたいと思って、恋人というより長期的なせふれ関係になれる人を探しています♪
  でもいきなりそんな関係になるのは難しいと思うので、ゆっくり信頼関係を深められたらと思いますm(_ _)m

  もしせふれさんを探していたらメッセージもらえると嬉しいです！"""
  
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.return_footpoint(name, setting.rina_happy_windowhandle, driver, return_foot_message, cnt)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('message:' + e.message)
    print('e自身:' + str(e))
  driver.quit()
  return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_foot(cnt)