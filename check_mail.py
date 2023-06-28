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

def check_mail():
    window_handle_list = [
       setting.erika_gmail_windowhandle, setting.erika_happy_windowhandle, setting.erika_pcmax_windowhandle,
       setting.rina_gmail_windowhandle, setting.rina_happy_windowhandle, setting.rina_pcmax_windowhandle,
       setting.meari_gmail_windowhandle, 
       setting.meari_pcmax_windowhandle,
       setting.yuria_happy_windowhandle, setting.yuria_pcmax_windowhandle, setting.yuria_gmail_windowhandle, 
       setting.ayaka_gmail_windowhandle, setting.ayaka_happy_windowhandle, setting.ayaka_pcmax_windowhandle,
       setting.misuzu_happy_windowhandle,
       setting.kiriko_gmail_windowhandle, setting.kiriko_happy_windowhandle, setting.kiriko_pcmax_windowhandle,
       setting.kumi_gmail_windowhandle, setting.kumi_happy_windowhandle, setting.kumi_pcmax_windowhandle, 
       setting.maiko_gmail_windowhandle, setting.maiko_happy_windowhandle, setting.maiko_pcmax_windowhandle,
    ]
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
      print(new_message_list)
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
    # address_to = 'kenta.bishi777@gmail.com'
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