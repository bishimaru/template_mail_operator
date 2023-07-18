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

def pcmax_footprints(driver, wait):
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT name, login_id, passward FROM pcmax')
  pcmax_user_list = []
  foot_order_list = ["めあり","きりこ","彩香","ゆりあ", "ももか", "ハル"]
  for row in cur:
      # print(row[0])
      if row[0] in foot_order_list:
        pcmax_user_list.append(row)

  for user_list in pcmax_user_list:
      try:
        pcmax.make_footprints(user_list[0], user_list[1], user_list[2], driver, wait)
      except Exception as e:
        print(traceback.format_exc())

if __name__ == '__main__':
  # if len(sys.argv) < 2:
  #   cnt = 20
  # else:
  #   cnt = int(sys.argv[1])
  options = Options()
  # options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  # options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  wait = WebDriverWait(driver, 15)
  
  pcmax_footprints(driver, wait)