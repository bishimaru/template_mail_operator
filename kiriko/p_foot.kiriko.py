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

def p_foot(cnt):
  name = "きりこ"

  return_foot_message = """はじめまして(*'ω'*)
某企業のカーディーラーの受付嬢として働いている『きりこ』です(*´ω｀)
　
今お仕事とか出会いで悩んでることがあって......
営業の人とかお客さんをおもてなしするのが仕事なんですけど
「接客マナー」とか「気配り」をすごい求められる職業ですっごいストレスがたまっちゃうんです(´;ω;｀)

休みの日でも営業の人から連絡きたりもするし、そんな仕事だけの毎日から解放されたくて.....
ついでにあっちのほうもご無沙汰だしストレスと欲求不満を解消できるセフレさんを探そうと思ってサイトをはじめてみました(@_@。

普段は気配りとかして相手に尽くすようなお仕事をしてるんですけど実は私Sなんです(#^^#)

なので少しMっけのある男性のほうが相性いいかもです(*´ω｀)"""
  
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    pcmax.return_footpoint(name, setting.kiriko_pcmax_windowhandle, driver, return_foot_message, cnt)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  p_foot(cnt)