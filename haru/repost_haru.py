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
  genre_flag_pcmax = setting.genre_flag_pcmax
  name = "ハル"
  title = "現役AV女優◎MM号に出演したのが自慢♪"
  text = """掲示板見てくれてありがとうございます♪
AV女優をしているハルです♪( ´▽｀)
一応MM号にも出たことあるのが自慢です！！笑

プライベートでの出会いが無いし寂しがりやなので
同じ事務所の女優さんに教えてもらって初めてみました◎
好きなタイプは優しくて穏やかな人です(^ ^)
こういう出会いなので、見た目とか年齢は気にせずに
やり取りした時のフィーリングで探してみようと思ってます♪
良かったらメッセージください♡

〜profile〜
・21歳
・156cm/45kg/Fカップ
・食べることとえっちなことが大好きです！笑"""

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
  try:
    pcmax.re_post(name, p_w, driver, genre_flag_pcmax)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  repost_happymail_pcmax()