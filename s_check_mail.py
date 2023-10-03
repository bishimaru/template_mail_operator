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
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import sqlite3
from datetime import timedelta

order_list = [
   ["あすか", "asuka414510@gmail.com"],
   ["彩香", "ayaka414510@gmail.com"],
   ["えりか", "k.erika414510@gmail.com"],
   ["きりこ", "kiriko414510@gmail.com"],
   ["めあり", "meari414510@gmail.com"],
   ["ももか", "momoka414510@gmail.com"],
   ["波留（はる）", "k.haru414510@gmail.com"], 
   ["波留（は...", ""],
   ["りこ", "riko414510@gmail.com"],
   ["りな", "k.rina414510@gmail.com"],
   ["ゆうこ", "yuko414510@gmail.com"], 
   ["ハル", "haruru414510@gmail.com"],
]
# order_list = [
# ["ゆうこ", "yuko414510@gmail.com"], 
# ]
def get_driver(debug):
    options = Options()
    
    if debug:
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument('--headless')
    else:
        # options.add_argument('--headless')
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=456,912")
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-cache")
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    # driver = func.get_debug_chromedriver()
    wait = WebDriverWait(driver, 15)
    return driver, wait

def check_mail():
  while True:
    
    for order_info in order_list:
        new_mail_list = []
        debug = False
        #  # ハッピーメール
        try:
            driver, wait = get_driver(debug)
            happymail_new = happymail.check_new_mail(driver, wait, order_info[0])
            if happymail_new:
                new_mail_list.append(happymail_new)
            # print(happymail_new)
            driver.quit()
        except Exception as e:
            print(f"<<<<<<<<<<メールチェックエラー：ハッピーメール{order_info[0]}>>>>>>>>>>>")
            print(traceback.format_exc())
            driver.quit()
        # # pcmax
        try:
            driver, wait = get_driver(debug)
            pcmax_new = pcmax.check_new_mail(driver, wait, order_info[0])
            # print(pcmax_new)
            if pcmax_new:
                new_mail_list.append(pcmax_new)
            driver.quit()
        except Exception as e:
            print(f"<<<<<<<<<<メールチェックエラー：pcmax{order_info[0]}>>>>>>>>>>>")
            print(traceback.format_exc())
            driver.quit()
        # gmail
        try:
            time.sleep(2)
            debug = True
            driver, wait = get_driver(debug)
            gmail_new = func.check_new_mail_gmail(driver, wait, order_info[1])
            if gmail_new:
                new_mail_list.append(gmail_new)
            # print(gmail_new)
            driver.quit()
        except Exception as e:
            print(f"<<<<<<<<<<メールチェックエラー：{order_info[1]}>>>>>>>>>>>")
            print(traceback.format_exc())
            driver.quit()
        
        # メール送信
        if len(new_mail_list) == 0:
            print(f'{order_info[0]}新着チェック完了手動メールなし')
            pass
        else:
            print(f'{order_info[0]}新着チェック完了手動メールあり')
            print(new_mail_list)
            mailaddress = 'kenta.bishi777@gmail.com'
            password = 'rjdzkswuhgfvslvd'
            text = ""
            subject = "新着メッセージ"
        
            for i in new_mail_list:
                text = text + i[0] + ",\n"
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
#    start_time = time.time() 
   check_mail()
#    elapsed_time = time.time() - start_time  # 経過時間を計算する
#    elapsed_timedelta = timedelta(seconds=elapsed_time)
#    elapsed_time_formatted = str(elapsed_timedelta)
#    print(f"<<<<<<<<<<<<<経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")