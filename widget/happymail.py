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


def re_post(name, happy_windowhandle, driver):
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(happy_windowhandle)
  wait_time = random.uniform(2, 3)
  try:
    if setting.mac_os:
      os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中...\" with title \"{}\"'".format(name))
    # マイページをクリック
    nav_list = driver.find_element(By.ID, value='ds_nav')
    mypage = nav_list.find_element(By.LINK_TEXT, "マイページ")
    mypage.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    # マイリストをクリック
    common_list = driver.find_element(By.CLASS_NAME, "ds_common_table")
    common_table = common_list.find_elements(By.CLASS_NAME, "ds_mypage_text")
    mylist = common_table[5]
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", mylist)
    time.sleep(wait_time)
    mylist.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    # 掲示板履歴をクリック
    menu_list = driver.find_element(By.CLASS_NAME, "ds_menu_link_list")
    menu_link = menu_list.find_elements(By.CLASS_NAME, "ds_next_arrow")
    bulletin_board_history = menu_link[5]
    bulletin_board_history.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    # その他掲示板をクリック
    link_tab = driver.find_elements(By.CLASS_NAME, "ds_link_tab_text")
    others_bulletin_board = link_tab[1]
    others_bulletin_board.click()
    time.sleep(1)

    # 再掲載をクリック
    for i in range(4):
      blue_round_buttons = driver.find_elements(By.CLASS_NAME, "ds_round_btn_blue2")
      blue_round_button = blue_round_buttons[i]
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", blue_round_button)
      time.sleep(wait_time)
      driver.execute_script('arguments[0].click();', blue_round_button)
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      # 再掲載する
      re_posting = driver.find_element(By.CLASS_NAME, "modal-confirm")
      re_posting.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      # id=modalの要素が出たら失敗 class=remodal-wrapperが4つともdiplay:noneなら成功
    if setting.mac_os:
       os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中に成功しました◎\" with title \"{}\"'".format(name))

  except Exception as e:
      if setting.mac_os:
         os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中に失敗しました...\" with title \"{}\"'".format(name))
      print('=== エラー内容 ===')
      print(traceback.format_exc())
      print('type:' + str(type(e)))
      print('args:' + str(e.args))
      print('message:' + e.message)
      print('e自身:' + str(e))

def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt):
    wait = WebDriverWait(driver, 15)
    driver.switch_to.window(happy_windowhandle)
    wait_time = random.uniform(2, 3)
    # TOPに戻る
    ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
    top_link = ds_logo.find_element(By.TAG_NAME, value="a")
    top_link.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール足跡返し実行中...\" with title \"{}\"'".format(name))
    try:
      i = 1
      for i in range(1):
        # マイページをクリック
        nav_list = driver.find_element(By.ID, value='ds_nav')
        mypage = nav_list.find_element(By.LINK_TEXT, "マイページ")
        mypage.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        # 足あとをクリック
        return_footpoint = driver.find_element(By.CLASS_NAME, value="icon-ico_footprint")
        return_footpoint.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)      
        # メールアイコンがあるかチェック
        send_status = True
        f_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
        name_field = f_user[0].find_element(By.CLASS_NAME, value="ds_like_list_name")
        if len(name_field.find_elements(By.TAG_NAME, value="img")):
          print('メールアイコンがあります')
          send_status = False
        # 足跡ユーザーをクリック
        f_user[0].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        # 自己紹介文に業者、通報が含まれているかチェック
        if len(driver.find_elements(By.CLASS_NAME, value="translate_body")):
          print("自己紹介文がありました")
          contains_violations = driver.find_element(By.CLASS_NAME, value="translate_body")
          driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", contains_violations)
          text = contains_violations.text.replace(" ", "").replace("\n", "")
          dev_list = []
          if '通報' in test_text or '業者' in text:
              print('自己紹介文に危険なワードが含まれていました')
              dev_list.append(text)
              send_status = False
        # メッセージ履歴があるかチェック
        mail_field = driver.find_element(By.ID, value="ds_nav")
        mail_history = mail_field.find_element(By.ID, value="mail-history")
        display_value = mail_history.value_of_css_property("display")
        if display_value != "none":
            print('メール履歴があります')   
            send_status = False
        # メールするをクリック
        print('send_status = ' + str(send_status) +  ' ~' + str(i) + "~")
        if send_status:
          send_mail = mail_field.find_element(By.CLASS_NAME, value="ds_profile_target_btn")
          send_mail.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          # 足跡返しを入力
          text_area = driver.find_element(By.ID, value="text-message")
          text_area.send_keys(return_foot_message)
          # 送信
          send_mail = driver.find_element(By.ID, value="submitButton")
          send_mail.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          # TOPに戻る
          ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
          top_link = ds_logo.find_element(By.TAG_NAME, value="a")
          top_link.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          cnt += 1
        else:
          # TOPに戻る
          ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
          top_link = ds_logo.find_element(By.TAG_NAME, value="a")
          top_link.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
    except Exception as e:
      if setting.mac_os:
         os.system("osascript -e 'display notification \"ハッピーメール{}件目の足跡返しに失敗しました...\" with title \"{}\"'".format(i, name))
      print('=== エラー内容 ===')
      print(traceback.format_exc())
      print('type:' + str(type(e)))
      print('args:' + str(e.args))
      print('message:' + e.message)
      print('e自身:' + str(e))
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール{}件の足跡返しに成功しました...\" with title \"{}\"'".format(i, name))
    print(dev_list)
  
