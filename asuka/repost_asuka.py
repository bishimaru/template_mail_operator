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

name = "あすか"
title = "3人でエッチを楽しめる方探してます♪"
text = """初めまして( ＾∀＾)
あすかです！友達のゆかとセフレさん探しの為に始めてみました♪♪

2人とも都内のメンズ専門の脱毛サロンで働いてるんですけど、VIOの脱毛専門で施術中にエッチな気分になっちゃてるちょっと変態な2人組です(⸝⸝⸝´꒳`⸝⸝⸝)ﾃﾚｯ

私もゆかもちょっと刺激が欲しいなって思ってて、、
折角セフレさんになってもらうなら3人でエッチを楽しめる人を探してます！

3Pとかに興味ある方は連絡くださいね♪♪
因みに、2人ともエッチで人懐っこい性格なので会って損はしないと思います♪笑"""

def repost_happymail_pcmax():
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", "あすか")
  p_w = func.get_windowhandle("pcmax", "あすか")
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