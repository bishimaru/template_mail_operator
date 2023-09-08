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
  name = "めあり"
  title = "せふれ募集◎性欲強めでもいいですか？？"
  text = """掲示板見てくれて嬉しいです( ´∀｀)
旅館で働いている『めあり』って言いますー！

中学生の頃から付き合っていた男の子が居て、関係性も悪く無かったんですけどお互いに社会人になってからは転勤とかで遠距離恋愛になってしまって( ; ; )

今出会いって言ったら職場くらいなんですけど、同僚とかお客様とそういう関係はよくないかなって思ってるんです。。。

1人としか付き合ったり体の関係とかも持ったことがないし、私もフリーなので人生で1度くらいはセフさんみたいな人が欲しいなって思ってサイトに登録しました(*ˊᵕˋ*)੭

profile
・めあり
・24歳/156cm/Dcup


お休みの日はいつもお家でドラマとか見ながらゴロゴロしてるんですけど、気づいたら1人でしちゃってたりもします(>_<)

こんな私とせふれさんになりたいって思ってくれる人いたらメッセージお願いします！
"""


  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)
  print(777)
  print(text)
  return
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