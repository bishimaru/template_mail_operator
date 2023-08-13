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
from selenium.webdriver.common.by import By
from datetime import timedelta


def h_p_foot(cnt):
  name = "haru"
  h_return_foot_img = ""
  p_return_foot_img = ""

  return_foot_message = """いきなりのメッセージ失礼します！

都内の会社でおもちゃの商品企画をしているはるです〜！

女子校出身で大学も美大で、職場も女性ばかりで出会いがなく、始めました...

好きなことは映画を見ること、ゲームをすること、本を読むことです。めちゃくちゃインドア派です。

ゲームは仕事でも関わりがあるのでよくやります！
今はポケモン、スプラトゥーンをしています。

ゲームとかばかりしていてしばらくは彼氏とかも居ないのであっちの方はソロプレイばかりです(´；ω；｀)

なのでゲームとかも一緒に出来て一緒にいて気負わない恋人みたいなセフさんが作れたらいいなと思っています(๑>◡<๑)

私との関係を前向きに考えて貰えるならお返事貰えたら嬉しいです♪"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)

  # start_time = time.time() 
  try:   
    func.h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())

  # timedeltaオブジェクトを作成してフォーマットする
  # elapsed_time = time.time() - start_time  # 経過時間を計算する
  # elapsed_timedelta = timedelta(seconds=elapsed_time)
  # elapsed_time_formatted = str(elapsed_timedelta)
  # print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
  driver.quit()
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_p_foot(cnt)