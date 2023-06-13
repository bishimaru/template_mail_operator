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
import setting
from selenium.webdriver.support.select import Select
from tkinter import filedialog
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import pcmax

def mail_reception_check(window_handle, driver, wait):
    new_mail = ""
    driver.switch_to.window(window_handle)
    wait_time = random.uniform(2, 3)
    url = driver.current_url
    # happymail
    if url.startswith("https://happymail.co.jp"):
      # TOPに戻る
      driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
      message_icon = driver.find_elements(By.CLASS_NAME, value="ds_nav_no_pickup")[2]
      name = driver.find_element(By.CLASS_NAME, "ds_user_display_name")      
      new_message = message_icon.find_elements(By.CLASS_NAME, value="ds_red_circle")
      if len(new_message):
          print(name.text + " :newmessage")
          new_mail = name.text + " : ハッピーメール"
    # pcmax
    elif url.startswith("https://pcmax.jp"):
      pcmax.login(driver, wait)
      name = driver.find_elements(By.CLASS_NAME, "p_img")
      if len(name):
          # 次の要素を取得
          next_element = name[0].find_element(By.XPATH, value="following-sibling::*[1]")
          name = next_element.text
          print(name)
          new_message = driver.find_elements(By.CLASS_NAME, value="message")[0]
          print(new_message.text)
          if new_message.text[:2] == "新着":
            print('新着')
            new_mail = name + " : pcmax"
    # gmail
    elif url.startswith("https://mail.google.com"):
        driver.get("https://mail.google.com/mail/mu")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)  
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
        print(address)

        # メインボックスのチェック
        main_box = driver.find_elements(By.CLASS_NAME, value="Hd")
        main_box[0].click()
        email_list = driver.find_element(By.CLASS_NAME, value="Ik")
        # 最初の子要素を取得
        latest_email = email_list.find_element(By.XPATH, value="./*[1]")
        print(latest_email)
        latest_new_email_address = latest_email.find_elements(By.TAG_NAME, value="b")
        print(len(latest_new_email_address))
        time.sleep(1) 
        if len(latest_new_email_address):
           print('newmessage')
           new_mail = address + " : メールボックス"
        
        # 迷惑メールフォルダーをチェック
        custom_value = "メニュー"
        xpath = f"//*[@aria-label='{custom_value}']"
        element = driver.find_elements(By.XPATH, value=xpath)
        element[0].click()
        time.sleep(1) 
        menu_list = driver.find_elements(By.XPATH, value="//*[@role='menuitem']")
        print(len(menu_list))
        spam = menu_list[-1]
        spam.click()
        time.sleep(1) 
        email_list = driver.find_element(By.CLASS_NAME, value="Ik")
        latest_email = email_list.find_element(By.XPATH, value="./*[1]")
        print(latest_email)
        latest_new_spam = latest_email.find_elements(By.TAG_NAME, value="b")
        print(len(latest_new_spam))
        time.sleep(1) 
        if len(latest_new_spam):
           print('new spammessage')
           new_mail = new_mail + ", " + address + " : 迷惑メール"
        custom_value = "メニュー"
        xpath = f"//*[@aria-label='{custom_value}']"
        element = driver.find_elements(By.XPATH, value=xpath)
        element[0].click()

    return new_mail