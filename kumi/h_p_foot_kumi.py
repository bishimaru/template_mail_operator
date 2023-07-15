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
  name = "くみ"
  return_foot_message = """こんにちは！くみです♪
このサイトでせふれさん募集してます☆
先日、とっても可愛い水着を買いました✌︎('ω'✌︎ )その水着を見てもらいたくて、足跡をつけてくれた方に見せちゃいます♪

思わず「これを着て海やプールに行きたいな」という気分になるような水着で、デザインは大胆で、シンプルな柄がとても鮮やかで気に入っています♪


もし興味があって、私とメッセージ交換してもいいよと思ってくれたら、お返事をいただけるとうれしいです。楽しく会える人がいいです！
それでは、返信待ってますね。よろしくお願いします♪"""  
  relative_path = os.path.join(setting.BASE_DIR, setting.kumi_picture_path)
  h_return_foot_img = relative_path
  p_return_foot_img = "230614"
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", "くみ")
  p_w = func.get_windowhandle("pcmax", "くみ")

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