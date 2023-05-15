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

def h_foot(cnt):
  name = "ゆあ&すみれ"
  return_foot_message = """足跡ありがとうございます！
  六本木の高級デリヘルに勤めてます『ゆあ』と『すみれ』です♪( ´θ｀)ノ
  気になってご連絡しちゃいました！

  お店で私たち２人の3Pコースがあるんですけど、
  2人とも３Pに目覚めちゃって笑

  プライベートでも3Pを楽しみたいので、私たち2人の夜の専属パートナーを探しているところなんです♫

  ちょっと変わった内容なんですけど、そういう関係に興味あったりしませんか？？"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.return_footpoint(name, setting.yua_happy_windowhandle, driver, return_foot_message, cnt)
    print('<<<<<<<<<<<<ゆあ、すみれ　ハッピーメール足跡返し　完了>>>>>>>>>>>>>>')

  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('message:' + e.message)
    print('e自身:' + str(e))
  driver.quit()
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_foot(cnt)