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
  name = "kumi"
  title = "リードします！楽しく会える人♪一般事務OLです。"
  text = """はじめまして！社会人二年目のくみです♪
最近、仕事と家の往復で忙しく過ごしている中で、せふれ探しにおいてちょっと困っているんです（ ; ; ）
職場での噂やトラブルは避けたいので、社会人になってそういう人の見つけ方がわからなくって、
友達がここでいい人見つけて、楽しそうなので登録しました♪率直に言って、えっちなことも大好きなので、新たな出会いを求めています。

せふれと聞くと都合の良い関係をイメージされるかもしれませんが、私はお互いに気を許し合えるパートナーとしての関係を築きたいと思っています。会っている時間は恋人同士のように甘え合える、心を通わせられる関係が理想です。
同じような気持ちを持っている方がいらっしゃいましたら、ぜひメッセージをいただけると嬉しいです！
よろしくお願いします♪"""



  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.re_post(name, setting.kumi_happy_windowhandle, driver, title, text, adult_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  try:
    pcmax.re_post(name, setting.kumi_pcmax_windowhandle, driver)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()