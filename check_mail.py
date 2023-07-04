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

def check_mail():
    window_handle_list= []
    dbpath = 'firstdb.db'
    conn = sqlite3.connect(dbpath)
    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()
    # データ検索
    cur.execute('SELECT window_handle FROM happymail')
    for row in cur:
        window_handle_list.append(row[0])  
    cur.execute('SELECT window_handle FROM pcmax')
    for row in cur:
        window_handle_list.append(row[0])  
    cur.execute('SELECT window_handle FROM gmail')
    for row in cur:
        window_handle_list.append(row[0])  
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("detach", True)
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)

    try:
      new_message_list = []
      for w_h in window_handle_list:
        new_message = mail_reception_check.mail_reception_check(
              w_h,
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

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  check_mail()