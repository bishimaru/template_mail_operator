from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from widget import pcmax, happymail, func
import sqlite3
from selenium.webdriver.chrome.service import Service
from datetime import timedelta

def pcmax_footprints(driver, wait):
  # 地域選択（3つまで選択可能）
  select_areas = [
    "東京都",
    # "千葉県",
    "埼玉県",
    "神奈川県",
    # "静岡県",
    # "新潟県",
    # "山梨県",
    # "長野県",
    # "茨城県",
    # "栃木県",
    # "群馬県",
  ]

  # 年齢選択（最小18歳、最高60以上）
  youngest_age = "19"
  oldest_age = "31"

  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT name, login_id, passward FROM pcmax')
  pcmax_user_list = []
  foot_order_list = [
     "アスカ", "あやか", "いおり","えりか", "きりこ", "さな", "すい", "つむぎ", 
     "なお", "めあり","ハル", "はづき", "りな", "りこ", "ゆうな", "ゆっこ", "ゆかり", 
     
      
  ]
  # foot_order_list = ["彩香",]

  for row in cur:
      if row[0] in foot_order_list:
        pcmax_user_list.append(row)
  for i in range(9999):
    start_time = time.time() 
    for user_list in pcmax_user_list:
        try:
          pcmax.make_footprints(user_list[0], user_list[1], user_list[2], driver, wait, select_areas, youngest_age, oldest_age,)
        except Exception as e:
          print(f"{user_list[0]}:エラー")
          print(traceback.format_exc())
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    elapsed_timedelta = timedelta(seconds=elapsed_time)
    elapsed_time_formatted = str(elapsed_timedelta)
    print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
    # 50足後付け,約6分
    # １キャラ12000 ６キャラ2000 12キャラ 1000
    
if __name__ == '__main__':
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  # options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  service = Service(executable_path="./chromedriver")

  driver = webdriver.Chrome(service=service, options=options)
  # driver = func.get_debug_chromedriver()
  wait = WebDriverWait(driver, 15)

  pcmax_footprints(driver, wait,)
      