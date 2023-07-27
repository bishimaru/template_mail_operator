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

  name = "ゆうこ"
  title = "美容師2人組@３Pできる共用のせふ募集！"
  text = """◎profile◎
『ゆうこ』
25歳/154cm/Ecup
おしゃべり上手でいつも元気だねって言われます(o^^o)

『ゆき』
25歳/156cm/Dcup
普段はアニメ好きの陰キャです笑
天然でおっとりしてるって言われます◯

初めまして！
2人とも都内で美容師として働いてます(*´∇｀*)

率直に3Pできるせふれさん欲しくて登録しました笑
以前お家で一緒に遊んでるときにせふれさんから連絡あって、好奇心でそのまま呼んで3Pしてからはまっちゃいました(●´ω｀●)

その方は転勤で会えなくなっちゃって、、、
代わりに性欲いっぱいで私たちの共用のせふれさんになってくれる人を大募集です！！
3P初心者の人も私たちの虜にしちゃうんで、興味あったらぜひ連絡欲しいです♪"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)
  # p_w = ""

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
  repost_happymail_pcmax()