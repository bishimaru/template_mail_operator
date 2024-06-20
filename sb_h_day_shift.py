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
import sqlite3



def sb_h_all_do(return_foot_cnt):
  
  dbpath = setting.db
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT name, login_id, passward FROM happymail')
  chara_order = []
  for row in cur:
      # print(row[0])
      chara_order.append(row[0])
      # if row[0] in foot_order_list:
      #   happy_user_list.append(row)
  # print(chara_order)

  def timer(sec, functions):
    start_time = time.time() 
    for func in functions:
      try:
        return_func = func()
      except Exception as e:
        print(e)
        return_func = 0
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    while elapsed_time < sec:
      time.sleep(5)
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      # print(elapsed_time)
    return return_func
  
  wait_cnt = 7200 / len(chara_order)
  start_one_rap_time = time.time() 
  return_cnt_list = []

  for chara in chara_order:
    
    try:
      # return_func = timer(wait_cnt, [lambda: pcmax_repost(chara), lambda: sb_h_repost_returnfoot(chara, return_foot_cnt)])
      return_func = timer(wait_cnt, [ lambda: sb_h_repost_returnfoot(chara, return_foot_cnt)])
      if return_func is not None:
        return_cnt_list.append(f"{chara}:足跡返し {return_func}件")
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

if __name__ == '__main__':
  if len(sys.argv) < 2:
    return_foot_cnt = 18
  elif len(sys.argv) >= 2:
    return_foot_cnt = int(sys.argv[1])
  sb_h_all_do(return_foot_cnt)