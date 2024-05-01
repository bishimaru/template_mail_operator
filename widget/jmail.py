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
import traceback
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func
from selenium.webdriver.support.select import Select
import sqlite3
import re
from datetime import datetime, timedelta
import difflib
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def login_jmail(driver, wait, name):
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT login_id, login_passward FROM jmail WHERE name = ?', (name,))
  for row in cur:
      login_id = row[0]
      login_pass = row[1]
      # post_title = row[2]
      # post_contents = row[3] 
  print(f"{row[0]}  {row[1]}")
  driver.delete_all_cookies()
  # https://mintj.com/msm/login/?adv=___36h1tmot02r12l8kxdtxx0b3z
  driver.get("https://mintj.com/msm/login/")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  wait_time = random.uniform(3, 6)
  time.sleep(2)
  id_form = driver.find_element(By.ID, value="loginid")
  id_form.send_keys(login_id)
  pass_form = driver.find_element(By.ID, value="pwd")
  pass_form.send_keys(login_pass)
  time.sleep(1)
  send_form = driver.find_element(By.ID, value="B1login")
  try:
    send_form.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)
  except TimeoutException as e:
    print("TimeoutException")
    driver.refresh()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    id_form = driver.find_element(By.ID, value="loginid")
    id_form.send_keys(login_id)
    pass_form = driver.find_element(By.ID, value="pwd")
    pass_form.send_keys(login_pass)
    time.sleep(1)
    send_form = driver.find_element(By.ID, value="B1login")
    send_form.click()

def re_post(driver, name):
   wait = WebDriverWait(driver, 15)
   login_jmail(driver, wait, name)
  # メニューをクリック
   menu_icon = driver.find_elements(By.CLASS_NAME, value="menu-off")
   menu_icon[0].click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(2)
