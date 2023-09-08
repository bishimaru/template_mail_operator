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

# order_list = ["あすか", "彩香","えりか", "haru...", "haru","きりこ","めあり","ももか","ゆうこ", 
#                "りこ","りな","ハル",  ]


def check_mail():
    chara_info_dic = {"まいこ":{}, "みづき":{}}

    dbpath = 'firstdb.db'
    conn = sqlite3.connect(dbpath)
    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()
    # 順番
    # データ検索
    # データ検索
    for chara_name in chara_info_dic.keys():
      cur.execute('SELECT * FROM pcmax WHERE name = ?', (chara_name,))
      for row in cur:
          # print("キャラ情報")
          # print(row)
          chara_info_dic[chara_name]["p_login_id"] = row[2]
          chara_info_dic[chara_name]["p_login_pass"] = row[3]
    print(777)
    print(chara_info_dic)
    return
          
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
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
              if new_message[:3] == "エラー":
                error_w_h = new_message[3:]
                cur.execute('SELECT name FROM pcmax WHERE window_Handle = ?', (error_w_h,))
                for row in cur:
                    if row:
                      error_message = f"{row[0]} pcmax 取得失敗"
                      new_message_list.append(error_message)
                cur.execute('SELECT name FROM gmail WHERE window_Handle = ?', (error_w_h,))
                for row in cur:
                    if row:
                      error_message = f"{row[0]} gmail 取得失敗"
                      new_message_list.append(error_message)
                cur.execute('SELECT name FROM happymail WHERE window_Handle = ?', (error_w_h,))
                for row in cur:
                    if row:
                      error_message = f"{row[0]} happymail 取得失敗"
                      new_message_list.append(error_message)
              else:  
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