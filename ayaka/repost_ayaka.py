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

adult_flag = True
genre_flag = setting.genre_flag
genre_flag_pcmax = setting.genre_flag_pcmax

name = "あやか"
title = "乃木坂オタな保育士と友達以上の関係"
text = """初めまして、あやかです。
アプリ入れるのやめたつもりが、なぜか入っていたので、この際やってしまおうと始めました...笑

あ、自己紹介が遅れました。
普段は都内の幼稚園で保育士として働いています〜！

子供が大好きでもちもちしてます(ﾉ)`∨´(ヾ)

お仕事とかは充実しているんですが、仕事柄なんですが出会いとかは全然なくて...泣

でもまだ結婚願望とかはあまり無いので趣味とかも一緒に楽しめる恋人未満、友達以上のような人を探しています！

乃木坂がすごく好きでLIVEは月に1回は必ず行ったりします！！

【趣味】
乃木坂46
日向坂
名探偵コナン
料理すること"""

def repost_happymail_pcmax():
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", "彩香")
  p_w = func.get_windowhandle("pcmax", "彩香")
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