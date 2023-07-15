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
from rina import all_do_rina, h_foot_rina, p_foot_rina, post_rina, h_p_foot_rina
from meari import all_do_meari, post_meari, h_p_foot_meari
from yua_sumire import all_do_yua_sumire
from erika import all_do_erika, post_erika, h_p_foot_erika
from yuria import all_do_yuria, post_yuria, h_p_foot_yuria
from maiko import all_do_maiko
from ayaka import all_do_ayaka, repost_ayaka, h_p_foot_ayaka
from misuzu import all_do_misuzu
from kiriko import all_do_kiriko, repost_kiriko, h_p_foot_kiriko
from kumi import all_do_kumi, h_p_foot_kumi, repost_kumi
from mizuki import repost_mizuki, h_p_foot_mizuki
from momoka import repost_momoka, h_p_foot_momoka
from riko import repost_riko, h_p_foot_riko
from yuko_yuki import repost_yuko_yuki, h_p_foot_yuko_yuki
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta
from check_mail import check_mail

if len(sys.argv) < 2:
  cnt = 20
elif len(sys.argv) == 2:
  cnt = int(sys.argv[1])

def timer(sec, functions, cnt):
  start_time = time.time() 
  for func in functions:
    func()
  elapsed_time = time.time() - start_time  # 経過時間を計算する
  while elapsed_time < sec:
    time.sleep(10)
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    print(elapsed_time)

sitemawashi_starttime = time.time() 

try:
  timer(600, [post_erika.repost_happymail_pcmax, check_mail])
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_kumi.repost_happymail_pcmax, check_mail, lambda: h_p_foot_erika.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [post_rina.repost_happymail_pcmax, check_mail, lambda: h_p_foot_kumi.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [post_meari.repost_happymail_pcmax, check_mail, lambda: h_p_foot_rina.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_kiriko.repost_happymail_pcmax, check_mail, lambda: h_p_foot_meari.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_ayaka.repost_happymail_pcmax, check_mail, lambda: h_p_foot_kiriko.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [post_yuria.repost_happymail_pcmax, check_mail, lambda: h_p_foot_ayaka.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_mizuki.repost_happymail_pcmax, check_mail, lambda: h_p_foot_yuria.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_momoka.repost_happymail_pcmax, check_mail, lambda: h_p_foot_mizuki.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  timer(600, [repost_riko.repost_happymail_pcmax, check_mail, lambda: h_p_foot_momoka.h_p_foot(cnt)], cnt)
except Exception as e:
  print(traceback.format_exc())

try:
  repost_yuko_yuki.repost_happymail_pcmax()
  check_mail()
  h_p_foot_riko.h_p_foot(cnt)
  h_p_foot_yuko_yuki.h_p_foot(cnt)
except Exception as e:
  print(traceback.format_exc())

elapsed_sitemawashi_time = time.time() - sitemawashi_starttime  # 経過時間を計算する
elapsed_sitemawashi_timedelta = timedelta(seconds=elapsed_sitemawashi_time)
elapsed_sitemawashi_time_formatted = str(elapsed_sitemawashi_timedelta)
print(f"<<<<<<<<<<<<<サイト回し一周タイム： {elapsed_sitemawashi_time_formatted}>>>>>>>>>>>>>>>>>>")




