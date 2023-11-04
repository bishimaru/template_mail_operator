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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta
from sb_p_repost import pcmax_repost
from sb_h_repost_return_foot import sb_h_repost_returnfoot


def sb_h_all_do(return_foot_cnt):
  chara_order = [
    "アスカ", "彩香", "きりこ", "波留（はる）",  "りこ",  "ハル", "ゆかり", "すい"
  ]
  def timer(sec, functions):
    start_time = time.time() 
    for func in functions:
      func()
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    while elapsed_time < sec:
      time.sleep(5)
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      # print(elapsed_time)
  wait_cnt = 7200 / len(chara_order)
  start_one_rap_time = time.time() 

  for chara in chara_order:
    try:
      timer(wait_cnt, [lambda: pcmax_repost(chara), lambda: sb_h_repost_returnfoot(chara, return_foot_cnt)])
    except Exception as e:
      print(f"エラー{chara}")
      print(traceback.format_exc())
  elapsed_time = time.time() - start_one_rap_time  
  elapsed_timedelta = timedelta(seconds=elapsed_time)
  elapsed_time_formatted = str(elapsed_timedelta)
  print(f"<<<<<<<<<<<<<サイト回し一周タイム： {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
  if len(sys.argv) < 2:
    return_foot_cnt = 22
  elif len(sys.argv) >= 2:
    return_foot_cnt = int(sys.argv[1])
  sb_h_all_do(return_foot_cnt)