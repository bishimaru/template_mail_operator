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
  name = "misuzu"
  return_foot_img = ""
  return_foot_message = """足跡からきました♪
銀座のホステスをしていましたが、現在は家事手伝いしてます。

働いていた時は寧な接客や美しさなど求められるものが多くプレッシャーが凄くって...
今は普通の生活をしてますが、反動で遊びたくて登録しちゃいました( *｀ω´)

ホステスの時に、信頼関係を築いた方と関係を持ったこともあったんですけど、セックスは乱暴で全く相性が合わなくて、思い切って体の関係から始めるのもありかなぁなんて思ってます。どっちかというとせめられたい人の方がいいかもです♪

こんな私とやり取りしてもいいよって思ってくれたらメッセージください！"""
  
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.return_footpoint(name, setting.misuzu_happy_windowhandle, driver, return_foot_message, cnt, return_foot_img)
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