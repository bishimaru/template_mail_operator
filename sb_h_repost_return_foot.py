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
from datetime import timedelta
import sqlite3

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=456,912")
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-cache")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    
    wait = WebDriverWait(driver, 15)
    return driver, wait

def sb_h_repost_returnfoot(name, cnt): 
  dbpath = setting.db
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT login_id, passward, post_title, post_contents, return_foot_message, mail_img, fst_message FROM happymail WHERE name = ?', (name,))
  login_id = ""
  for row in cur:
      login_id = row[0]
      login_pass = row[1]
      post_title = row[2]
      post_contents = row[3]
      return_foot_message = row[4]
      if row[5]:
        return_foot_img =  setting.BASE_DIR + row[5]
        if setting.mac_mini_bishi:
          return_foot_img = return_foot_img.replace("mail_tool", "mail_operator")
      else:
         return_foot_img = ""
      fst_message = row[6]
  if not login_id:
    return
  adult_flag = True
  genre_flag = setting.genre_flag
  happy_windowhandle = ""
  driver, wait = get_driver()

  driver.delete_all_cookies()
  driver.get("https://happymail.jp/login/")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  wait_time = random.uniform(2, 5)
  time.sleep(2)
  id_form = driver.find_element(By.ID, value="TelNo")
  id_form.send_keys(login_id)
  pass_form = driver.find_element(By.ID, value="TelPass")
  pass_form.send_keys(login_pass)
  time.sleep(1)
  send_form = driver.find_element(By.ID, value="login_btn")
  send_form.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  return_foot_cnt = 0
  try:
    happymail.re_post(name, happy_windowhandle, driver, post_title, post_contents, adult_flag, genre_flag)
  except Exception as e:
    print(f"ハッピーメール掲示板エラー{name}")
    print(traceback.format_exc())
    func.send_error(f"ハッピーメール掲示板エラー{name}", traceback.format_exc())
  time.sleep(2)
  try:
    return_foot_cnt = happymail.return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt, return_foot_img, fst_message)
  except Exception as e:
    print(f"足跡返しエラー{name}")
    print(traceback.format_exc())
    func.send_error(f"足跡返しエラー{name}", traceback.format_exc())
  driver.quit()
  return return_foot_cnt


if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    name = str(sys.argv[1])
    cnt = int(sys.argv[2])
    # matching_cnt = int(sys.argv[3])
    # type_cnt = int(sys.argv[4])
  # sb_h_repost_returnfoot(name, cnt, matching_cnt, type_cnt)
    sb_h_repost_returnfoot(name, cnt)


  