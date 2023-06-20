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

def repost_happymail_pcmax():
  adult_flag = True
  name = "misuzu"
  title = "体の関係から始めるのってなしですか？"
  text = """目に留めていただき、ありがとうございます。

以前は銀座のホステスとして働いていましたが、今は家事手伝いをしているみすずと申します。

ホステスの仕事では、接客や外見への要求が多く、プレッシャーも大きかったんです(>_<)なので、現在はその反動で普通の生活を楽しむことにしています♪

ホステスの時に、信頼関係を築いた方と関係を持ったこともあったんですけど、セックスは乱暴で相性が合わないこともあって、なので思い切って体の関係から始めてみるのもアリかなぁと思っています( ´θ｀)ノ

こんな私に興味を持っていただけたら、メッセージください！

"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.re_post(name, setting.misuzu_happy_windowhandle, driver, title, text, adult_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, setting.rina_pcmax_windowhandle, driver)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()