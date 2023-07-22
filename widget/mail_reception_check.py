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
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import pcmax
from selenium.common.exceptions import TimeoutException


def mail_reception_check(window_handle, driver, wait):
   try:
      new_mail = ""
      # print("window_handle")
      # print(window_handle)
      driver.switch_to.window(window_handle)
      try:
         url = WebDriverWait(driver, 10).until(lambda driver: driver.current_url)
         # url = driver.current_url
      except TimeoutException as e:
         print("TimeoutException")
         driver.refresh()
      # happymail
      if url.startswith("https://happymail.co.jp"):
         # TOPに戻る
         driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
         wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
         time.sleep(1)
         message_icon = driver.find_elements(By.CLASS_NAME, value="ds_nav_no_pickup")[2]
         name = driver.find_element(By.CLASS_NAME, "ds_user_display_name")
         name = name.text  
         new_message = message_icon.find_elements(By.CLASS_NAME, value="ds_red_circle")
         if len(new_message):
            new_mail = name+ " : ハッピーメール"
         # 足跡つける
         # wait_time = random.uniform(1, 4)
         # # プロフ検索をクリック
         # nav_list = driver.find_element(By.ID, value='ds_nav')
         # mypage = nav_list.find_element(By.LINK_TEXT, "プロフ検索")
         # mypage.click()
         # wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
         # time.sleep(wait_time)
         # for i in range(4):
         #    user_list = driver.find_elements(By.CLASS_NAME, value="profile_list_big_item")
         #    user = user_list[i].find_element(By.TAG_NAME, value="a")
         #    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", user)
         #    user.click()
         #    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
         #    print(f'{name}: ハッピーメール、足跡{i+1}件')
         #    time.sleep(wait_time)
         #    driver.back()
         #    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
         #    time.sleep(1)
      # pcmax
      elif url.startswith("https://pcmax.jp"):
         pcmax.login(driver, wait)
         name = driver.find_elements(By.CLASS_NAME, "p_img")
         if len(name):
            # 次の要素を取得
            next_element = name[0].find_element(By.XPATH, value="following-sibling::*[1]")
            name = next_element.text
            new_message = driver.find_elements(By.CLASS_NAME, value="message")[0]
            if new_message.text[:2] == "新着":
               new_mail = name + " : pcmax"
      # gmail
      elif url.startswith("https://mail.google.com"):
         try:
            driver.get("https://mail.google.com/mail/mu")
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(1)  
         except TimeoutException as e:
            print("TimeoutException")
            driver.refresh()
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
         if len(element):
            time.sleep(2)
            element = driver.find_elements(By.XPATH, value=xpath)
         address = element[0].text
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
   except Exception as e:
      print(traceback.format_exc())

   return new_mail