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
  name = "波留（はる）"
  title = "都内OLはる/恋人みたいなセフさん"
  text = """はじめまして。
都内の会社でおもちゃの商品企画をしているはるです！

女子校出身で大学も美大で、職場も女性ばかりで出会いがなく、始めました...

好きなことは映画を見ること、ゲームをすること、本を読むことです。めちゃくちゃインドア派です。

ゲームは仕事でも関わりがあるのでよくやります！
今はポケモン、スプラトゥーンをしています。

彼氏とかも居ないので休みの日は1人えっちばかりです(´；ω；｀)

ゲームとかも一緒に出来て
一緒にいて気負わない恋人みたいなセフさんが作れたらいいなと思っています(๑>◡<๑)"""

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

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  repost_happymail_pcmax()