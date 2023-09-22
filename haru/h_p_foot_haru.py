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
import sqlite3

def h_p_foot(cnt):
  name = "ハル"
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT return_foot_message, mail_img FROM happymail WHERE name = ?', (name,))
  for row in cur:
      return_foot_message = row[0]
      h_return_foot_img = row[1]  
  p_return_foot_img = ""
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