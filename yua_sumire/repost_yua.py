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
  genre_flag_pcmax = setting.genre_flag_pcmax

  name = "ゆあ&すみれ"
  title = "六本木の高級デリ嬢2人組の専属セフレ募集"
  text = """掲示板見てくれてありがとうございます♫、
  六本木の高級デリヘルで現役キャストしてます『ゆあ』と『すみれ』です！

  お店の特別コースで私とすみれの3Pコースがあるんですけど、
  １回やってみたら二人ともそれにハマっちゃって笑

  私がSですみれがMなのでかなり楽しめると思うんですけど高級店の3Pだからか中々このコース選んでくれる人がいなくて（ ; ; ）

  私たち的にはもっと3Pを楽しみたいけど、相手がいないので
  じゃあ、このサイトでプライベートで長く関係を続けられる人を見つけよってなって、今お相手を探してるところです( ^ω^ )

  一応、高級店に在籍してるので二人とも夜の営みには自信ありです笑

  こんな私たちの専属のセフレになってくれる方で純粋にエッチを楽しみたい方ならどんな人でも大歓迎です！

  ご連絡お待ちしてます♡"""


  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.re_post(name, setting.yua_happy_windowhandle, driver, title, text, adult_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  try:
    pcmax.re_post(name, setting.yua_pcmax_windowhandle, driver)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True
if __name__ == '__main__':
  repost_happymail_pcmax()