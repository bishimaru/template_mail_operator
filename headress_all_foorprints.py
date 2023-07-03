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
import h_footprints
import p_footprints
from datetime import timedelta



def headress_all_footprints(driver, wait):
  for i in range(9999):
    start_time = time.time() 
    h_footprints.happymail_footprints(driver, wait)
    p_footprints.pcmax_footprints(driver, wait)
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    # timedeltaオブジェクトを作成してフォーマットする
    elapsed_timedelta = timedelta(seconds=elapsed_time)
    elapsed_time_formatted = str(elapsed_timedelta)
    print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
    
  driver.quit()
  
if __name__ == '__main__':
  # if len(sys.argv) < 2:
  #   cnt = 20
  # else:
  #   cnt = int(sys.argv[1])
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  # options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  wait = WebDriverWait(driver, 15)

  headress_all_footprints(driver, wait)