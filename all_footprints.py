from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import widget.pcmax 
import time
import random
import widget.mail_reception_check
import traceback
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import setting
import sys


window_handle_list = [
      #  setting.erika_gmail_windowhandle, setting.erika_happy_windowhandle, setting.erika_pcmax_windowhandle,
       setting.rina_pcmax_windowhandle,
      #  setting.kumi_gmail_windowhandle, setting.kumi_happy_windowhandle, setting.kumi_pcmax_windowhandle, 
      #  setting.meari_happy_windowhandle, setting.meari_gmail_windowhandle, setting.meari_pcmax_windowhandle,
      #  setting.yuria_happy_windowhandle, setting.yuria_pcmax_windowhandle, setting.yuria_gmail_windowhandle, 
      #  setting.kiriko_gmail_windowhandle, setting.kiriko_happy_windowhandle, setting.kiriko_pcmax_windowhandle,
      #  setting.ayaka_gmail_windowhandle, setting.ayaka_happy_windowhandle, setting.ayaka_pcmax_windowhandle,
      #  setting.misuzu_happy_windowhandle,
       
      #  setting.maiko_gmail_windowhandle, setting.maiko_happy_windowhandle, setting.maiko_pcmax_windowhandle,
    ]
send_mail = True
if len(sys.argv) == 2:
  send_mail = False
new_message_list = []
dev_cnt = 0
start_time = time.time() 

for x in range(9999):
  for window_cnt in range(len(window_handle_list)):
      options = Options()
      options.add_argument('--headless')
      options.add_argument("--no-sandbox")
      options.add_argument("--remote-debugging-port=9222")
      options.add_experimental_option("detach", True)
      # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
      service = Service(executable_path="./chromedriver")
      driver = webdriver.Chrome(service=service, options=options)
      wait = WebDriverWait(driver, 15)
      driver.switch_to.window(window_handle_list[window_cnt])
      url = driver.current_url
      if url.startswith("https://happymail.co.jp"):
          try:
            happy_foot_cnt = 3
            happy_wait_time = random.uniform(2, 5)
            # TOPに戻る
            if url != "https://happymail.co.jp/sp/app/html/mbmenu.php":
              driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
              time.sleep(happy_wait_time)  
            # プロフ検索をクリック
            nav_list = driver.find_element(By.ID, value='ds_nav')
            mypage = nav_list.find_element(By.LINK_TEXT, "プロフ検索")
            mypage.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(2)
            for h_f_cnt in range(happy_foot_cnt):
              user_list = driver.find_elements(By.CLASS_NAME, value="profile_list_big_item")
              user = user_list[h_f_cnt].find_element(By.TAG_NAME, value="a")
              driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", user)
              user.click()
              wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
              print(f'ハッピーメール、足跡{h_f_cnt+1}件')
              time.sleep(happy_wait_time)
              driver.back()
              wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
              time.sleep(2)
            
            new_message = widget.mail_reception_check.mail_reception_check(
                  window_handle_list[window_cnt],
                  driver, wait
                )
            if new_message:
              new_message_list.append(new_message)
            print(new_message_list)
          except Exception as e:
            print(traceback.format_exc()) 
      elif url.startswith("https://pcmax.jp"):
          try:
            pcmax_foot_cnt = 4
            pcmax_wait_time = random.uniform(2, 5)
            widget.pcmax.login(driver, wait)
            print(666)
            #プロフ検索をクリック
            footer_icons = driver.find_element(By.ID, value="sp_footer")
            search_profile = footer_icons.find_element(By.XPATH, value="./*[1]")
            search_profile.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(1)
            user_list = driver.find_element(By.CLASS_NAME, value="content_inner")
            users = user_list.find_elements(By.XPATH, value='./div')
            print(len(users))
            link_list = []
            for user_cnt in range(pcmax_foot_cnt):
              user_id = users[user_cnt].get_attribute("id")
              if user_id == "loading":
                print('id=loading')
                while user_id != "loading":
                  time.sleep(2)
                  user_id = users[user_cnt].get_attribute("id")
              link = "https://pcmax.jp/mobile/profile_detail.php?user_id=" + user_id + "&search=prof&condition=648ac5f23df62&page=1&sort=&stmp_counter=13&js=1"
              link_list.append(link)
            for i, link_url in enumerate(link_list):
              print(f"足ペタ件数: {i + 1}")
              print(link_url)
              driver.get(link_url)
              time.sleep(pcmax_wait_time) 
            new_message = widget.mail_reception_check.mail_reception_check(
                  window_handle_list[window_cnt],
                  driver, wait
                )
            if new_message:
              new_message_list.append(new_message)
            print(new_message_list)  
          except Exception as e:
            print(traceback.format_exc()) 

      elif url.startswith("https://mail.google.com"):
          try:
            driver.get("https://mail.google.com/mail/mu")
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(1)  
            new_mail = ""
            # メニューをクリック
            # カスタム属性の値を持つ要素をXPathで検索
            custom_value = "メニュー"
            xpath = f"//*[@aria-label='{custom_value}']"
            element = driver.find_elements(By.XPATH, value=xpath)
            element[0].click()
            time.sleep(1) 
            custom_value = "toggleaccountscallout+20"
            xpath = f"//*[@data-control-type='{custom_value}']"
            element = driver.find_elements(By.XPATH, value=xpath)
            address = element[0].text
            time.sleep(1) 
            # メインボックスのチェック
            main_box = driver.find_elements(By.CLASS_NAME, value="Hd")
            main_box[0].click()
            email_list = driver.find_element(By.CLASS_NAME, value="Ik")
            # 最初の子要素を取得
            latest_email = email_list.find_element(By.XPATH, value="./*[1]")
            latest_new_email_address = latest_email.find_elements(By.TAG_NAME, value="b")
            time.sleep(1) 
            if len(latest_new_email_address):
              new_mail = address
            # 迷惑メールフォルダーをチェック
            custom_value = "メニュー"
            xpath = f"//*[@aria-label='{custom_value}']"
            element = driver.find_elements(By.XPATH, value=xpath)
            element[0].click()
            time.sleep(2) 
            menu_list = driver.find_elements(By.XPATH, value="//*[@role='menuitem']")
            spam = menu_list[-1]
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", spam)
            spam.click()
            time.sleep(1) 
            email_list = driver.find_element(By.CLASS_NAME, value="Ik")
            latest_email = email_list.find_element(By.XPATH, value="./*[1]")
            latest_new_spam = latest_email.find_elements(By.TAG_NAME, value="b")
            time.sleep(1) 
            if len(latest_new_spam):
              new_mail = new_mail + ", " + address + ":迷惑フォルダ"
            custom_value = "メニュー"
            xpath = f"//*[@aria-label='{custom_value}']"
            element = driver.find_elements(By.XPATH, value=xpath)
            element[0].click()
            if new_mail:
              new_message_list.append(new_mail)
          except Exception as e:
            print(traceback.format_exc()) 
      # dev_cnt += 1
      # if dev_cnt == 4:
      #     break
  elapsed_time = time.time() - start_time  # 経過時間を計算する
  print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>')
  print(elapsed_time)
  driver.quit()
  # メール送信
  if send_mail:
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