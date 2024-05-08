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


def login_jmail(driver, wait, login_id, login_pass):
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
   dbpath = 'firstdb.db'
   conn = sqlite3.connect(dbpath)
   # # SQLiteを操作するためのカーソルを作成
   cur = conn.cursor()
  # # 順番
  # # データ検索  
   cur.execute('SELECT * FROM jmail WHERE name = ?', (name,))
   for row in cur:
      # print(6666)
      # print(row)
      login_id = row[2]
      login_pass = row[3]
      post_title = row[4]
      post_content = row[5]
   login_jmail(driver, wait, login_id, login_pass)
  # メニューをクリック
   menu_icon = driver.find_elements(By.CLASS_NAME, value="menu-off")
   menu_icon[0].click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(2)
  #  アダルト掲示板をクリック
   menu = driver.find_elements(By.CLASS_NAME, value="iconMenu")
   adult_post_menus = menu[0].find_elements(By.TAG_NAME, value="p")
   adult_post_menu = adult_post_menus[0].find_elements(By.XPATH, "//*[contains(text(), 'アダルト掲示板')]")
   adult_post_menu_link = adult_post_menu[0].find_element(By.XPATH, "./.")
  #  adult_post_menu_link.click()
   driver.get(adult_post_menu_link.get_attribute("href"))
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(2)
  #  投稿をクリック　color_variations_03
   post_icon = driver.find_elements(By.CLASS_NAME, value="color_variations_03")
   post_icon[0].click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(2)
  #  コーナーを選択
   corner_select = driver.find_elements(By.NAME, value="CornerId")
   select = Select(corner_select[0])
   select.select_by_visible_text("今すぐあそぼっ")
   time.sleep(1)
  #  件名を入力
   post_title_input = driver.find_elements(By.NAME, value="Subj")
   post_title_input[0].clear()
   post_title_input[0].send_keys(post_title)
   time.sleep(1)
  #  メッセージを入力
   post_content_input = driver.find_elements(By.NAME, value="Comment")
   post_content_input[0].clear()
   post_content_input[0].send_keys(post_content)
   time.sleep(1)
  #  メール受信数を選択　Number of emails received
   select_recieve_number = driver.find_elements(By.NAME, value="ResMaxCount")
   driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", select_recieve_number[0])
   select = Select(select_recieve_number[0])
   select.select_by_visible_text("5件")
   time.sleep(1)
  #  書き込む
   write_button = driver.find_elements(By.NAME, value="Bw")
   write_button[0].click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(1)

def check_new_mail(driver, wait, name):
  return_list = []
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT login_id, login_passward, fst_message, return_foot_message, second_message FROM jmail WHERE name = ?', (name,))
  login_id = None
  for row in cur:
    print(row)
    login_id = row[0]
    login_pass = row[1]
    fst_message = row[2]
    return_foot_message = row[3]
    second_message = row[4]
  if login_id == None or login_id == "":
    print(f"{name}のjmailキャラ情報を取得できませんでした")
    return 1, 0
  login_jmail(driver, wait, login_id, login_pass)
  # メールアイコンをクリック
  mail_icon = driver.find_elements(By.CLASS_NAME, value="mail-off")
  link = mail_icon[0].find_element(By.XPATH, "./..")
  driver.get(link.get_attribute("href"))
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  interacting_user_list = []
  interacting_users = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")
  # 未読以外でNEWのアイコンも存在してそう
  if "未読" in interacting_users[0].text:
  # deug
  # if 1== 1:
    print(777)
    # 時間を取得　align_right
    parent_usr_info = interacting_users[0].find_element(By.XPATH, "./..")
    parent_usr_info = parent_usr_info.find_element(By.XPATH, "./..")
    next_element = parent_usr_info.find_element(By.XPATH, value="following-sibling::*[1]")
    print(next_element.text)
    current_year = datetime.now().year
    date_string = f"{current_year} {next_element.text}"
    date_format = "%Y %m/%d %H:%M" 
    date_object = datetime.strptime(date_string, date_format)
    now = datetime.today()
    
    elapsed_time = now - date_object
    print(interacting_users[0].text)
    print(f"メール到着からの経過時間{elapsed_time}")
    if elapsed_time >= timedelta(minutes=4):
      print("4分以上経過しています。")
      # リンクを取得
      link_element = interacting_users[0].find_element(By.XPATH, "./..")
      print(666)
      print(link_element.get_attribute("href"))
      print(link_element.tag_name)
      driver.get(link_element.get_attribute("href"))
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)
      # 相手からのメッセージが何通目か確認する
      # mohumohu

      # 返信するをクリック
      res_do = driver.find_elements(By.CLASS_NAME, value="color_variations_05")
      res_do[1].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(10)
      # メッセージを入力　name=comment
      text_area = driver.find_elements(By.NAME, value="comment")
      text_area[0].send_keys(fst_message)
      time.sleep(6)
      # 画像があれば送信
      # 7777777777777
      send_button = driver.find_elements(By.NAME, value="sendbutton")
      send_button[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(20)


      


  return 1, 0

   

   
   
