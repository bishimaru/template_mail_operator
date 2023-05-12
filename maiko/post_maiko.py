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

def repost_happymail_pcmax():
  name = "麻衣子"
  title = "声優志望女子大生◎Hなキャラを演じたい！ワンナイトは×"
  text = """『声優志望の女子大生です！』

  初めまして！大学4年生で、将来は声優になることが夢です(๑>◡<๑)

  特にエロ系のアニメやゲームが好きで、エロいキャラクターの声を担当して、自分もそんなキャラクターを演じられるようになりたいです。

  もっとHな経験をして上手な演技をしたいので、セックスパートナーを募集します....( *｀ω´)
  たくさんエロい声を出したいし、男性の感じている声も大好きなのでいっぱい気持ちよくしたいです( ✌︎'ω')✌︎

  でも単に練習するっていうわけじゃなくて、会ってる時は恋人みたいにお互いを思いやれる関係がいいです◎
  そんなパートナーになれる関係でもいいよって人はメッセージください！

  いい出会いがあるといいな(๑>◡<๑)"""


  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.re_post(name, setting.maiko_happy_windowhandle, driver, title, text)
  except Exception as e:
    print('777')
  # try:
  #   pcmax.re_post(name, setting.maiko_pcmax_windowhandle, driver)
  # except Exception as e:
  #   print('777')
  driver.quit()
  return True

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  repost_happymail_pcmax()