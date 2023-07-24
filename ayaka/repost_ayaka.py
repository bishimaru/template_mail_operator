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
title = "子供のお世話も大人のお世話も得意です♡"
text = """掲示板見てくれてありがとうございます♪
都内で保育士のお仕事をしています( ´∀｀)

普段から世話焼きの方であるので子供のお世話するのは全然苦じゃないし、笑顔を見てるとハッピーな気持ちにもなれるし私には天職だと思ってますd(￣ ￣)

でも女性の多い職場だから全然出会いはなくてそこだけが不満です（ ;  ; ）
同僚の子がここでせふれさんを作ったって自慢していて、それなら私もって思ってせふれ探しを始めました！！

Profile
・あやか/24歳/Dcup
・スマホゲームにハマっていて、時間ある時はついついぽちぽちしちゃいます笑
・甘えられるのも好きだけど甘えるのも大好きな寂しがり屋です(>_<)

年齢とか気にしないんですけど、会ってる時はまったりと楽しい時間を過ごせたらって思ってるのでよろしくお願いします！！
気になったら連絡もらえると喜びます( ´∀｀)"""

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