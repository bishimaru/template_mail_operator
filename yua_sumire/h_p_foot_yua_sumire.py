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
from datetime import timedelta


def h_p_foot(cnt):
  name = "ゆあ"
  return_foot_message = """足跡ありがとうございます！
六本木の高級デリヘルに勤めてます『ゆあ』と『すみれ』です♪( ´θ｀)ノ
気になってご連絡しちゃいました！

お店で私たち２人の3Pコースがあるんですけど、
2人とも３Pに目覚めちゃって笑

プライベートでも3Pを楽しみたいので、私たち2人の夜の専属パートナーを探しているところなんです♫

ちょっと変わった内容なんですけど、そういう関係に興味あったりしませんか？？"""
  relative_path = os.path.join(setting.BASE_DIR, setting.yua_sumire_picture_path)
  h_return_foot_img = relative_path
  p_return_foot_img = "230409"
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
    func.h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img)
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
  h_p_foot(cnt)