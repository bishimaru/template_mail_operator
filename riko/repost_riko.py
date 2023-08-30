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
  name = "りこ"
  title = "失恋の寂しさを埋めれる相手を探してます◎"
  text = """投稿見てくれてありがとうございます♪
りこって言います♪( ´θ｀)ノ
都内で駆け出しのOLをしています！

大学生の時まで付き合っていた彼氏がいたのですが、就職のタイミングで遠距離になってしまって自然消滅してしましました(>_<)
その寂しさを紛らわしたくてお仕事に熱中してたんですが、最近は少し慣れてきたこともあり寂しさが溢れてきて。。。

基本職場とお家の往復ばかりで出会いは職場くらいだし、新米で職場で波立てたくないってのもあるのでここで新しい出会いを探そうと思って始めました！！！

少し自己紹介書いておきますね(^ ^)
◎りこ/24歳/153cm/Ecup
◎大学時代はバドミントンサークルに入っていて、今でも体動かすのが大好きです(*´∇｀*)
◎動物が大好きでペットを飼うのが目標です！

見た目とか年齢とか関係なくフィーリング合う人と会えたらって思っているので、興味持ってくれたら連絡もらえると喜びます♪"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  # driver = func.get_debug_chromedriver()
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)

  try:   
    happymail.re_post(name, h_w, driver, title, text, adult_flag, genre_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, p_w, driver, genre_flag_pcmax)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()

if __name__ == '__main__':
  repost_happymail_pcmax()