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
  title = "元銀座ホステスです。気軽に連絡ください♪"
  text = """掲示板見てくれてありがとうございます♪

都内在住でリモートで働いているみすずです( *｀ω´)
今の仕事を働き出して３ヶ月が経つんですけど、仕事にもなれてきて特に不自由なく
過ごせてます♪

でも１つだけ悩みがあって、出会いがないことです...ずっと家にいて家族以外と喋ることがない日もしばしば。。。まだ25歳だしこのまま歳をとっていくのはなんだか悲しいです。

だから思い切ってサイトに登録してみました！！昔、銀座でホステスをやっていたことがプチ自慢です笑　
せっかくなので年上も年下も、容姿とかも特に気にせず絡んでいきたいんですけど、ぶっちゃけあっちの方も欲求溜まっています。一人でするのも飽きたので、生身の男性と触れ合いたいです(๑>◡<๑)

良かったらメッセージください♪"""

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

if __name__ == '__main__':
  repost_happymail_pcmax()