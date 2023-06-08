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
  return_foot_message = """初めまして。
足跡からプロフィール拝見させて頂きました、みすずです。

元銀座のホステスをしていた経験がありますが、現在は家事手伝いをしながら新たな出会いを求めてます！

人生にはいろんな経験がありますよね(>_<)
銀座でいろんなお客様と出会って、同僚からイジメも受けて、今までの経験から、普段の生活のありがたみを知って普通の生活の道を歩みたいと思っています。

優しい男性との出会いを探しています。お互いを支え合い、温かな生活を築けたらいいなと思っています。
初めはメッセージからお話しして仲良くなれたら嬉しいです。
よろしくお願いします。"""
  
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