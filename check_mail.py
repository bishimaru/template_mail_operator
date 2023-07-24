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
from widget import pcmax, happymail, mail_reception_check
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import sqlite3
from datetime import timedelta

order_list = ["えりか", "くみ", "りな", "めあり", "きりこ", "彩香", "ハル", "ゆりあ", "みづき", "ももか",  "りこ", "ゆうこ", "まいこ", "みすず"]

def check_mail():
    print('checkkumaiiiil')
    return
    window_handle_list= []
    window_handle_order_list= []
    dbpath = 'firstdb.db'
    conn = sqlite3.connect(dbpath)
    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()
    # 順番
    # データ検索
    cur.execute('SELECT window_handle,name FROM happymail')
    for row in cur:
        window_handle_list.append(row)  
    cur.execute('SELECT window_handle,name FROM pcmax')
    for row in cur:
        window_handle_list.append(row)  
    cur.execute('SELECT window_handle,name FROM gmail')
    for row in cur:
        window_handle_list.append(row)  
    # 順番入れ替え
    for order_name in order_list:
       for window_handle in window_handle_list:
          chara_name = window_handle[1]
          if chara_name == order_name:
             if window_handle != None:
              window_handle_order_list.append(window_handle)
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("detach", True)
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 7)
    for i in range(1):
      # start_time = time.time() 
      try:
        new_message_list = []
        for w_h in window_handle_order_list:
          if w_h[0]:
            new_message = mail_reception_check.mail_reception_check(
                  w_h[0],
                  driver, wait
                )
            if new_message:
              new_message_list.append(new_message)
        driver.quit()
      except Exception as e:
        print(traceback.format_exc())
        driver.quit()
      # メール送信
      mailaddress = 'kenta.bishi777@gmail.com'
      password = 'rjdzkswuhgfvslvd'
      text = ""
      if len(new_message_list) == 0:
        subject = "新着はありません"
        text = ""
      else:
        subject = "新着メッセージ"
        for i in new_message_list:
          text = text + i + ",\n"
      address_from = 'kenta.bishi777@gmail.com'
      address_to = 'bidato@wanko.be'
      smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
      smtpobj.starttls()
      smtpobj.login(mailaddress, password)
      msg = MIMEText(text)
      msg['Subject'] = subject
      msg['From'] = address_from
      msg['To'] = address_to
      msg['Date'] = formatdate()
      smtpobj.send_message(msg)
      smtpobj.close()

      # elapsed_time = time.time() - start_time  # 経過時間を計算する
      # elapsed_timedelta = timedelta(seconds=elapsed_time)
      # elapsed_time_formatted = str(elapsed_timedelta)
      # print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  check_mail()