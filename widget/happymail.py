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


def re_post(name, happy_windowhandle, driver, title, text):
  area_list = ["東京都", "千葉県", "埼玉県", "神奈川県"]
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(happy_windowhandle)
  wait_time = random.uniform(2, 3)
  # TOPに戻る
  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")

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
      # 都道府県を取得
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
      warning = driver.find_elements(By.CLASS_NAME, value="remodal-wrapper ")
      for w in warning:
         display_property = driver.execute_script("return window.getComputedStyle(arguments[0]).getPropertyValue('display');", w)
         if display_property == 'block':
            # ２時間経ってない場合は終了
            modal_text = w.find_element(By.CLASS_NAME, value="modal-content")
            if modal_text.text == "掲載から2時間以上経過していない為、再掲載できません":
               cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
               cancel.click()
               print(modal_text.text)
               driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
               return
            # リモーダルウィンドウを閉じる
            print("再投稿に失敗したので新規書き込みします")
            print("Element is displayed as block")
            print(title)
            cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
            cancel.click()
            time.sleep(wait_time)
            # 都道府県を取得
            area_text = driver.find_elements(By.CLASS_NAME, value="ds_write_bbs_status")
            area_text = area_text[i].text.replace(" ", "").replace("\n", "")
            for area in area_list:
              if area in area_text:
                #  掲示板をクリック
                nav_list = driver.find_element(By.ID, value='ds_nav')
                bulletin_board = nav_list.find_element(By.LINK_TEXT, "掲示板")
                bulletin_board.click()
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
                # 書き込みをクリック
                write = driver.find_element(By.CLASS_NAME, value="icon-header_kakikomi")
                write.click()
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
                # その他掲示板をクリック
                adult = driver.find_elements(By.CLASS_NAME, value="ds_link_tab_text")
                adult[1].click()
                time.sleep(1)
                # タイトルを書き込む
                input_title = driver.find_element(By.NAME, value="Subj")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", input_title)
                input_title.send_keys(title)
                time.sleep(1)
                # 本文を書き込む
                text_field = driver.find_element(By.ID, value="text-message")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_field)
                text_field.send_keys(text)
                time.sleep(1)
                # 書き込みエリアを選択
                select_area = driver.find_element(By.NAME, value="wrtarea")
                select = Select(select_area)
                select.select_by_visible_text(area)
                time.sleep(1)
                mail_rep =driver.find_element(By.NAME, value="Rep")
                select = Select(mail_rep)
                select.select_by_visible_text("10件")
                time.sleep(1)
                # 書き込む
                writing = driver.find_element(By.ID, value="billboard_submit")
                writing.click()
                select.select_by_visible_text("10件")
                time.sleep(1)
                # 書き込み成功画面の判定
                success = driver.find_elements(By.CLASS_NAME, value="ds_keijiban_finish")
                if len(success):
                  print(str(area) + "の書き込みに成功しました")
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
                else:
                  print(str(area) + "の書き込みに失敗しました")
                  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
                  return
      print(str(i + 1) + "件の書き込みに成功しました")
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
      driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
      

def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt):
    wait = WebDriverWait(driver, 15)
    driver.switch_to.window(happy_windowhandle)
    wait_time = random.uniform(2, 3)
    driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール足跡返し実行中...\" with title \"{}\"'".format(name))
    try:
      user_icon = 0
      for i in range(cnt):
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
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", f_user[user_icon])
        time.sleep(1)
        f_user[user_icon].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        m = driver.find_elements(By.XPATH, value="//*[@id='ds_main']/div/p")
        if len(m):
          print(m[0].text)
          if m[0].text == "プロフィール情報の取得に失敗しました":
             user_icon += 1
             continue
        # 自己紹介文に業者、通報が含まれているかチェック
        if len(driver.find_elements(By.CLASS_NAME, value="translate_body")):
          contains_violations = driver.find_element(By.CLASS_NAME, value="translate_body")
          driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", contains_violations)
          text = contains_violations.text.replace(" ", "").replace("\n", "")
          if '通報' in text or '業者' in text:
              print('自己紹介文に危険なワードが含まれていました')
              send_status = False
        # メッセージ履歴があるかチェック
        mail_field = driver.find_element(By.ID, value="ds_nav")
        mail_history = mail_field.find_element(By.ID, value="mail-history")
        display_value = mail_history.value_of_css_property("display")
        if display_value != "none":
            print('メール履歴があります')   
            send_status = False
        # メールするをクリック
        if send_status:
          print('send_status = ' + str(send_status) +  ' ~' + str(i) + "~")
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
  
