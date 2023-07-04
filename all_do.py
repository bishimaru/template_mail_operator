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
from rina import all_do_rina, h_foot_rina, p_foot_rina, post_rina
from meari import all_do_meari
from yua_sumire import all_do_yua_sumire
from erika import all_do_erika
from yuria import all_do_yuria
from maiko import all_do_maiko
from ayaka import all_do_ayaka
from misuzu import all_do_misuzu
from kiriko import all_do_kiriko
from kumi import all_do_kumi
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta

if len(sys.argv) < 2:
  h_cnt = 20
  p_cnt = 20
elif len(sys.argv) == 2:
  h_cnt = int(sys.argv[1])
  p_cnt = 20
else:
  h_cnt = int(sys.argv[1])
  p_cnt = int(sys.argv[2])

start_time = time.time() 
try:
  func.timer(all_do_kumi.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
try:
  func.timer(all_do_erika.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
try:
  func.timer(all_do_rina.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
try:
  func.timer(all_do_meari.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
try:
  func.timer(all_do_kiriko.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
try:
  func.timer(all_do_ayaka.do_post_foot, 799, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
# try:
#   func.timer(all_do_yuria.do_post_foot, 799, h_cnt, p_cnt)
# except Exception as e:
#   print(traceback.format_exc())
try:
  func.timer(all_do_misuzu.do_post_foot, 900, h_cnt, p_cnt)
except Exception as e:
  print(traceback.format_exc())
elapsed_time = time.time() - start_time  # 経過時間を計算する
# timedeltaオブジェクトを作成してフォーマットする
elapsed_timedelta = timedelta(seconds=elapsed_time)
elapsed_time_formatted = str(elapsed_timedelta)
print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")


# try:
#   func.timer(all_do_maiko.do_post_foot, 799, h_cnt, p_cnt)
# except Exception as e:
#   print(traceback.format_exc())

# try:
#   func.timer(all_do_yua_sumire.do_post_foot, 1200, h_cnt, p_cnt)
# except Exception as e:
#   print(traceback.format_exc())


