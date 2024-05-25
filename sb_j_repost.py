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
from widget import  func, jmail
import sqlite3
from selenium.webdriver.chrome.service import Service
from datetime import timedelta

def jmail_repost():
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  wait = WebDriverWait(driver, 15)

  chara_order = [  
    "アスカ", "あやか", "いおり", "えりか", 
    "きりこ", "さな", "すい", "つむぎ", "なお", 
  ]
  chara_order = [  
    "つむぎ", "ハル",
  ]
  def timer(sec, functions):
    start_time = time.time() 
    for func in functions:
      repost_flag = func()    
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    while elapsed_time < sec:
      time.sleep(10)
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      # print(elapsed_time)
    return repost_flag
  
  wait_cnt = 7200 / len(chara_order)
  start_one_rap_time = time.time() 
  return_cnt_list = []

  for chara in chara_order:
    try:
      repost_flag = timer(wait_cnt, [lambda: jmail.re_post(driver, chara)])
      if repost_flag:
        return_cnt_list.append(f"{chara}:掲示板再投稿 True")
    except Exception as e:
      print(f"エラー{chara}")
      print(traceback.format_exc())
      # func.send_error(chara, traceback.format_exc())
  elapsed_time = time.time() - start_one_rap_time  
  elapsed_timedelta = timedelta(seconds=elapsed_time)
  elapsed_time_formatted = str(elapsed_timedelta)
  print(f"<<<<<<<<<<<<<サイト回し一周タイム： {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
  return_cnt_list.append(f"サイト回し一周タイム： {elapsed_time_formatted}")
  str_return_cnt_list = ", ".join(return_cnt_list)
  func.send_mail(str_return_cnt_list)
  # try:
  #   jmail.re_post(driver, name)
  #   driver.quit() 
  # except Exception as e:
  #   print(f"{name}:エラー")
  #   print(traceback.format_exc())
  #   driver.quit() 
  

if __name__ == '__main__':
  jmail_repost()
  