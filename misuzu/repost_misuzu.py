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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback

def repost_happymail_pcmax():
  adult_flag = True
  genre_flag = setting.genre_flag
  name = "みすず"
  title = "元銀座ホステス/今は家事手伝いです。。"
  text = """目に留めていただきありがとうございます♪

以前は銀座のホステスとして働いていましたが、今は家事手伝いをしているみすずです( ´∀｀)

ホステスの仕事では、接客や外見への要求が多く、プレッシャーも大きかったんです(>_<)
なので、現在はその反動で普通の生活を楽しんでます♪

ホステスの時に、信頼関係を築いた方と関係を持ったこともあったんですけど、セックスは乱暴で相性が合わなくって、なので思い切って体の関係から始めてみるのもアリかなぁと思っています( ´θ｀)ノ

どっちかというとせめられたい人の方が相性いいかもです！
良かったらメッセージ待ってます(๑>◡<๑)
"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)

  try:   
    happymail.re_post(name, h_w, driver, title, text, adult_flag, genre_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, p_w, driver)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()