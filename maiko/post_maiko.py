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
import sqlite3

def repost_happymail_pcmax():
  adult_flag = True
  genre_flag = setting.genre_flag
  genre_flag_pcmax = setting.genre_flag_pcmax
  name = "まいこ"
  title = "声優志望◎Hなキャラを演じたい！"
  text = """初めまして！22才で、声優目指して上京してきた麻衣子です。

声優としてはまだ駆け出しですが、夢を追いかけることができて楽しいです♪

でも親には反対されちゃって、理解してもらえなくて(;o;)
不安なのですが、自分で決めたことだしやるしかないと思って頑張ります！

どんな役でも頑張りたいので、ここではもっとHな経験をして上手な演技をしたいので、セックスパートナーを募集します....( *｀ω´)
たくさんエロい声を出したいし、男性の感じている声も大好きなのでいっぱい気持ちよくしたいです( ✌︎'ω')✌︎
でも単に練習するっていうわけじゃなくて、会ってる時は恋人みたいにお互いを思いやれる、そして私の「夢」を応援してくれる人がいいです◎

そんなパートナーになれるよって人はメッセージください！"""
  h_w = func.get_windowhandle("happymail", "まいこ")
  p_w = func.get_windowhandle("pcmax", "まいこ")
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  
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