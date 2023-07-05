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
  name = "めあり"
  title = "せふれ募集◎性欲強めでもいいですか？？"
  text = """掲示板見てくれて嬉しいです( ´∀｀)
  ホテルで働いている『めあり』って言います◯

  大学生の頃から続いていたせふれさんがいたんですけど、お互いの勤務場所が離れてしまって会えなくなっちゃって（ ;  ; ）

  今出会いって言ったら職場くらいなんですけど、同僚とかお客様とそういう関係はよくないかなって思ってるんです。。。

  だから職場外でせふれさんが欲しくてここに登録しました！！

  簡単に自己紹介します(*´∇｀*)
  ・めあり
  ・24歳/156cm/Dcup
  ・恥ずかしいんですけどかなり性欲強めです^^;
  お休みの日はいつもお家でドラマとか見ながらゴロゴロしてるんですけど、気づいたら1人でしちゃってたりもします(>_<)

  こんな私とせふれさんになりたいって思ってくれる人いたらメッセージお願いします！
  性欲強めで優しい方だと嬉しいです(*ﾟ▽ﾟ*)"""


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
    pcmax.re_post(name, p_w, driver)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True
if __name__ == '__main__':
  repost_happymail_pcmax()