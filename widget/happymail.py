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
import setting
from selenium.webdriver.support.select import Select
import sqlite3
import re
from datetime import datetime, timedelta
import difflib
from selenium.common.exceptions import NoSuchElementException




# 警告画面
# b2_dialog_title
def catch_warning_screen(driver):
   warning = driver.find_elements(By.CLASS_NAME, value="warning screen")
   if len(warning):
      print(warning.text)
      return True
   else:
      return False

def re_post(name, happy_windowhandle, driver, title, post_text, adult_flag, genre_flag):
  area_list = ["東京都", "千葉県", "埼玉県", "神奈川県"]
  wait = WebDriverWait(driver, 15)
  if happy_windowhandle:
    driver.switch_to.window(happy_windowhandle)
  wait_time = random.uniform(2, 3)
  # TOPに戻る
  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
  driver.delete_cookie("outbrain_cid_fetch")
  if setting.mac_os:
    os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中...\" with title \"{}\"'".format(name))
  # 警告画面が出たらスキップ
  # ds_main_header_text
  warning = driver.find_elements(By.CLASS_NAME, value="ds_main_header_text")
  if warning:
     print("警告画面が出ました")
     return
  # print(777)
  # print(driver.get_cookies())
  # return
  # マイページをクリック
  nav_list = driver.find_element(By.ID, value='ds_nav')
  mypage = nav_list.find_element(By.LINK_TEXT, "マイページ")
  mypage.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(wait_time)
  # マイリストをクリック
  common_list = driver.find_element(By.CLASS_NAME, "ds_common_table")
  common_table = common_list.find_elements(By.CLASS_NAME, "ds_mypage_text")
  for common_table_elem in common_table:
     if "マイリスト" in common_table_elem.text:
        mylist = common_table_elem
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
  # ピュア掲示板かその他掲示板をクリック
  if adult_flag:
    link_tab = driver.find_elements(By.CLASS_NAME, "ds_link_tab_text")
    others_bulletin_board = link_tab[1]
    others_bulletin_board.click()
    time.sleep(1)
  else:
    print('ピュア掲示板')
    link_tab = driver.find_elements(By.CLASS_NAME, "ds_link_tab_text")
    others_bulletin_board = link_tab[0]
    others_bulletin_board.click()
    time.sleep(1)
  # ジャンル選択
  genre_dict = {0:"今すぐ会いたい", 1:"大人の出会い"}
  genre = driver.find_elements(By.CLASS_NAME, value="ds_bd_none")[1].text
  print("<<<再投稿する掲示板のジャンル取得>>>")
  print(genre)
  # 1日に書き込めるのは五回まで
  if genre != genre_dict[genre_flag]:
    print(f"{genre_dict[genre_flag]}にジャンル変更します")
    for i, kanto in enumerate(area_list):
      # 掲示板重複を削除する
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(2)
      area_texts = driver.find_elements(By.CLASS_NAME, value="ds_write_bbs_status")
      area_texts_list = []
      for area in area_texts:
        shaping_area = area.text.replace(" ", "").replace("\n", "")
        area_texts_list.append(shaping_area)
      area_cnt = 0
      list = []
      for area_text in area_texts_list:
        if area_text not in list:
            list.append(area_text)
            area_cnt += 1
        else:
            print("重複があった")
            duplication_area = driver.find_elements(By.CLASS_NAME, value="ds_round_btn_red")[area_cnt]
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", duplication_area)
            time.sleep(2)
            duplication_area.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(wait_time)
            delete = driver.find_element(By.CLASS_NAME, "modal-confirm")
            delete.click()
            time.sleep(2)

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
      # 書き込み上限に達したらスキップ
      adult = driver.find_elements(By.CLASS_NAME, value="remodal-wrapper")
      print(len(adult))
      if len(adult):
          print("24時間以内の掲示板書き込み回数の上限に達しています(1日5件まで)")
          cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
          cancel.click()
          driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
          continue
      # その他掲示板をクリック
      link_tab = driver.find_elements(By.CLASS_NAME, "ds_link_tab_text")
      others_bulletin_board = link_tab[1]
      others_bulletin_board.click()
      time.sleep(2)
      # ジャンルを選択
      select_genre = driver.find_element(By.ID, value="keijiban_adult_janl")
      select = Select(select_genre)
      select.select_by_visible_text(genre_dict[genre_flag])
      time.sleep(1)
      # タイトルを書き込む
      input_title = driver.find_element(By.NAME, value="Subj")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", input_title)
      input_title.send_keys(title)
      time.sleep(1)
      # 本文を書き込む
      text_field = driver.find_element(By.ID, value="text-message")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_field)
      text_field.send_keys(post_text)
      time.sleep(1)
      # 書き込みエリアを選択
      select_area = driver.find_element(By.NAME, value="wrtarea")
      select = Select(select_area)
      select.select_by_visible_text(kanto)
      time.sleep(1)
      mail_rep =driver.find_element(By.NAME, value="Rep")
      select = Select(mail_rep)
      select.select_by_visible_text("10件")
      time.sleep(1)
      # 書き込む
      writing = driver.find_element(By.ID, value="billboard_submit")
      writing.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      # 書き込み成功画面の判定
      success = driver.find_elements(By.CLASS_NAME, value="ds_keijiban_finish")
      if len(success):
        print(f"{name}: {i + 1} の書き込みに成功しました")
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
        print(str(i +1) + "の書き込みに失敗しました")
        driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
        
  else:
    # 再掲載をクリック
    for repost_cnt in range(4):
    # 掲示板重複を削除する
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(2)
      area_texts = driver.find_elements(By.CLASS_NAME, value="ds_write_bbs_status")
      area_texts_list = []
      for area in area_texts:
        area = area.text.replace(" ", "").replace("\n", "")
        area_texts_list.append(area)
      area_cnt = 0
      list = []
      for area_text in area_texts_list:
        if area_text not in list:
            list.append(area_text)
            area_cnt += 1
        else:
            print("重複があった")
            duplication_area = driver.find_elements(By.CLASS_NAME, value="ds_round_btn_red")[area_cnt]
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", duplication_area)
            time.sleep(2)
            duplication_area.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(wait_time)
            delete = driver.find_element(By.CLASS_NAME, "modal-confirm")
            delete.click()
            time.sleep(2)
      blue_round_buttons = driver.find_elements(By.CLASS_NAME, "ds_round_btn_blue2")
      blue_round_button = blue_round_buttons[repost_cnt]
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
      if len(warning):
          display_property = driver.execute_script("return window.getComputedStyle(arguments[0]).getPropertyValue('display');", warning[0])
          if display_property == 'block':
            # ２時間経ってない場合は終了
            modal_text = warning[0].find_element(By.CLASS_NAME, value="modal-content")
            if modal_text.text == "掲載から2時間以上経過していない為、再掲載できません":
                print("掲載から2時間以上経過していない為、再掲載できません")
                cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
                cancel.click()
                driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
                break
            # リモーダルウィンドウを閉じる
            print("再投稿に失敗したので新規書き込みします")
            print("Element is displayed as block")
            cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
            cancel.click()
            time.sleep(wait_time)
            # 都道府県を取得
            area_text = driver.find_elements(By.CLASS_NAME, value="ds_write_bbs_status")
            area_text = area_text[repost_cnt].text.replace(" ", "").replace("\n", "")
            for area in area_list:
              if area in area_text:
                #  掲示板をクリック
                nav_list = driver.find_element(By.ID, value='ds_nav')
                bulletin_board = nav_list.find_element(By.LINK_TEXT, "掲示板")
                bulletin_board.click()
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
                # 書き込みをクリック
                write = driver.find_element(By.CLASS_NAME, value="icon-kakikomi_float")
                # write = driver.find_element(By.CLASS_NAME, value="icon-header_kakikomi")
                write.click()
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
                # 書き込み上限に達したらスキップ
                adult = driver.find_elements(By.CLASS_NAME, value="remodal-wrapper")
                print(len(adult))
                if len(adult):
                    print("24時間以内の掲示板書き込み回数の上限に達しています(1日5件まで)")
                    cancel = driver.find_element(By.CLASS_NAME, value="modal-cancel")
                    cancel.click()
                    driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
                    continue
                # その他掲示板をクリック
                link_tab = driver.find_elements(By.CLASS_NAME, "ds_link_tab_text")
                others_bulletin_board = link_tab[1]
                others_bulletin_board.click()
                time.sleep(2)
                # タイトルを書き込む
                input_title = driver.find_element(By.NAME, value="Subj")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", input_title)
                input_title.send_keys(title)
                time.sleep(1)
                # 本文を書き込む
                text_field = driver.find_element(By.ID, value="text-message")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_field)
                text_field.send_keys(post_text)
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
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
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
                  for common_table_elem in common_table:
                     if common_table_elem.text == "マイリスト":  
                      mylist = common_table_elem
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
      print(str(repost_cnt + 1) + "件の書き込みに成功しました")
    if setting.mac_os:
        os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中に成功しました◎\" with title \"{}\"'".format(name))

def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt, return_foot_img):
    wait = WebDriverWait(driver, 15)
    if happy_windowhandle:
      driver.switch_to.window(happy_windowhandle)
    # wait_time = random.uniform(2, 3)
    wait_time = 2
    driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール足跡返し実行中...\" with title \"{}\"'".format(name))
    user_icon = 0
    foot_cnt = 1
    mail_icon_cnt = 0
    duplication_user = False
    user_name_list = []
    # 上から順番に足跡返し
    while cnt >= foot_cnt:
      warning = catch_warning_screen(driver) 
      if warning:
         break
      user_icon = 0
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
      send_status = True
      time.sleep(1)
      f_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
      while len(f_user) == 0:
         time.sleep(2)
         f_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
      name_field = f_user[user_icon].find_element(By.CLASS_NAME, value="ds_like_list_name")
      user_name = name_field.text
      mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
      user_age = f_user[user_icon].find_elements(By.CLASS_NAME, value="ds_like_list_age")
      if not len(user_age):
         send_status = False
      if user_age[0].text[:2] == "ナイ":
         print("年齢不詳")
         user_age = 31
      else:
        user_age = int(user_age[0].text[:2])
      if user_age >= 40:
        #  print(f'〜〜{user_age}代〜〜')
         # 実行確率（80%の場合）
         execution_probability = 0.20
         # ランダムな数値を生成し、実行確率と比較
         if random.random() < execution_probability:
            send_status = False
      # メールアイコンがあるかチェック
      # print(user_name_list)
      if len(mail_icon):
        send_status = False
        print('メールアイコンがあります')
        mail_icon_cnt += 1
        print(f'メールアイコンカウント{mail_icon_cnt}')
        # ユーザー名を取得

        # # メールアイコンが7つ続いたら終了
        if mail_icon_cnt == 7:
          ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
          top_link = ds_logo.find_element(By.TAG_NAME, value="a")
          top_link.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          print("メールアイコンが10続きました")
          return
      # ユーザー重複チェック
      while user_name in user_name_list:
          print('重複ユーザー')
          user_icon = user_icon + 1
          
          name_field = f_user[user_icon].find_element(By.CLASS_NAME, value="ds_like_list_name")
          user_name = name_field.text      
      # 足跡ユーザーをクリック
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", f_user[user_icon])
      time.sleep(1)
      if duplication_user:
        name_field = f_user[user_icon+1].find_element(By.CLASS_NAME, value="ds_like_list_name")
        user_name = name_field.text
        user_name_list.append(user_name) 

        f_user[user_icon+1].click()
      else:
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
        self_introduction_text = contains_violations.text.replace(" ", "").replace("\n", "")
        if '通報' in self_introduction_text or '業者' in self_introduction_text:
            print('自己紹介文に危険なワードが含まれていました')
            send_status = False
      # メッセージ履歴があるかチェック
      mail_field = driver.find_element(By.ID, value="ds_nav")
      mail_history = mail_field.find_element(By.ID, value="mail-history")
      display_value = mail_history.value_of_css_property("display")
      if display_value != "none":
          # print('メール履歴があります')
          # print(user_name)
          user_name_list.append(user_name) 
          send_status = False
          mail_icon_cnt += 1
      # メールするをクリック
      if send_status:
        print(f'{name}:足跡返し send_status = {str(send_status)} ~ {str(foot_cnt)} ~)')
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
        # 画像があれば送信
        if return_foot_img:
          img_conform = driver.find_element(By.ID, value="media-confirm")
          plus_icon = driver.find_element(By.CLASS_NAME, value="icon-message_plus")
          plus_icon.click()
          time.sleep(1)
          upload_file = driver.find_element(By.ID, "upload_file")
          upload_file.send_keys(return_foot_img)
          time.sleep(2)
          submit = driver.find_element(By.ID, value="submit_button")
          submit.click()
          while img_conform.is_displayed():
             time.sleep(2)
        foot_cnt += 1
        mail_icon_cnt = 0
        user_icon = 0
        # TOPに戻る
        driver.execute_script("window.scrollTo(0, 0);")
        ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", ds_logo)
        top_link = ds_logo.find_element(By.TAG_NAME, value="a")
        time.sleep(1)
        top_link.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
      else:
        user_name_list.append(user_name) 
        # TOPに戻る
        ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
        top_link = ds_logo.find_element(By.TAG_NAME, value="a")
        top_link.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール{}件の足跡返しに成功しました...\" with title \"{}\"'".format(foot_cnt, name))
  
def make_footprints(name, happymail_id, happymail_pass, driver, wait):
   driver.delete_all_cookies()
   driver.get("https://happymail.jp/login/")
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   wait_time = random.uniform(2, 5)
   time.sleep(wait_time)
   id_form = driver.find_element(By.ID, value="TelNo")
   id_form.send_keys(happymail_id)
   pass_form = driver.find_element(By.ID, value="TelPass")
   pass_form.send_keys(happymail_pass)
   time.sleep(wait_time)
   send_form = driver.find_element(By.ID, value="login_btn")
   send_form.click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(2)
   # プロフ検索をクリック
   nav_list = driver.find_element(By.ID, value='ds_nav')
   mypage = nav_list.find_element(By.LINK_TEXT, "プロフ検索")
   mypage.click()
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(wait_time)
   # 並びの表示を設定
   sort_order = driver.find_elements(By.ID, value="kind_select")
   select = Select(sort_order[0])
   select.select_by_visible_text("プロフ一覧")
   wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
   time.sleep(wait_time)
   no_history_user_list = []
   # ページの高さを取得
   last_height = driver.execute_script("return document.body.scrollHeight")
   while True:
    # ページの最後までスクロール
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # ページが完全に読み込まれるまで待機
    time.sleep(2)
    user_list = driver.find_elements(By.CLASS_NAME, value="ds_user_post_link_item_r")
    for user in user_list:
       user_class = user.get_attribute('class')
       if not "ds_ribbon" in user_class:
          # user_name = user.find_elements(By.CLASS_NAME, value="ds_post_body_name_small")
          user_link = user.find_elements(By.TAG_NAME, value="a")
          onclick_value = user_link[0].get_attribute('onclick')
          # 正規表現パターンを定義
          pattern = r'happymail\.co\.jp.*?idx=(\d+)'
          match = re.search(pattern, onclick_value)
          if match:
            result = match.group(0)
          no_history_user_list.append(result)
# https://happymail.jp/login/
    if len(no_history_user_list) > 33:
      print('ユーザー件数33　OVER')
      print(len(no_history_user_list))
      break
    # 新しい高さを取得
    new_height = driver.execute_script("return document.body.scrollHeight")
    # ページの高さが変わらなければ、すべての要素が読み込まれたことを意味する
    if new_height == last_height:
        break
    last_height = new_height
   for i, no_history_user in enumerate(no_history_user_list):
      driver.get(f"https://{no_history_user}")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      # userのidxを取得（タイプボタン取得のため）
      #  正規表現パターンを定義
      pattern = r'idx=(\d+)'
      # 正規表現でマッチングを行う
      matches = re.findall(pattern, no_history_user)
      # idxを目印にユーザーのディスプレイを取得
      inputs = driver.find_elements(By.NAME, value="idx")
      type_flag = False
      # タイプ
      # ランダムな数値を生成し、実行確率と比較
      # 実行確率
      execution_probability = 0.77
      if random.random() < execution_probability:
        for input in inputs:
          if input.get_attribute('value') == matches[0]:
            user_profile = input.find_element(By.XPATH, 'following-sibling::div[contains(@class, "ds_profile_picture")]')
            type_btn = user_profile.find_elements(By.CLASS_NAME, value="icon-type_off")
            type_btn[0].click()
            type_flag = True
            time.sleep(2)
      # いいね
      like_flag = False
      like = driver.find_elements(By.CLASS_NAME, value="icon-profile_like")
      like_icon = like[0].find_elements(By.CLASS_NAME, value="icon-on")
      if like_icon[0].is_displayed():
        # ランダムな数値を生成し、実行確率と比較
         # 実行確率
        execution_probability = 0.77
        if random.random() < execution_probability:
          like_flag = True
          like[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
          like_send = driver.find_elements(By.CLASS_NAME, value="modal-confirm")
          while not len(like_send):
            time.sleep(1)
            like_send = driver.find_elements(By.CLASS_NAME, value="modal-confirm")
          like_send[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
          like_cansel = driver.find_elements(By.CLASS_NAME, value="modal-cancel")
          like_cansel[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
      # driver.get("https://happymail.co.jp/sp/app/html/profile_list.php")
      # driver.back()
      print(f'{name}:足跡付け{i+1}件, いいね:{like_flag}、タイプ{type_flag}')
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      if i == 40:
         break
   driver.refresh()

def send_fst_message(name_list):
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  wait = WebDriverWait(driver, 15)
  wait_time = random.uniform(2, 3)

  try:
    for name in name_list:
      limit_cnt = 2
      if name == "えりか":
        limit_cnt = 3
      h_w = func.get_windowhandle("happymail", name)
      # print(name)
      dbpath = 'firstdb.db'
      conn = sqlite3.connect(dbpath)
      # SQLiteを操作するためのカーソルを作成
      cur = conn.cursor()
      # データ検索
      cur.execute('SELECT * FROM happymail WHERE name = ?', (name,))
      for row in cur:
          fst_message = row[6]
          fst_message_img = row[7]
      driver.switch_to.window(h_w)
      # TOPに戻る
      driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      # # プロフ検索をクリック
      nav_list = driver.find_element(By.ID, value='ds_nav')
      seach_profile = nav_list.find_element(By.LINK_TEXT, "プロフ検索")
      seach_profile.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      send_cnt = 0
      user_colum = 0
      # リモーダル画面が出たら閉じる
      remodal = driver.find_elements(By.CLASS_NAME, value="remodal-close")
      if len(remodal):
        print('リモーダル画面')
        remodal[0].click()
        time.sleep(wait_time)
      # 並びの表示を設定
      sort_order = driver.find_elements(By.ID, value="kind_select")
      select = Select(sort_order[0])
      select.select_by_visible_text("プロフ一覧")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      
      while send_cnt < limit_cnt:
        # ユーザーをクリック
        users = driver.find_elements(By.CLASS_NAME, value="ds_thum_contain")
        print('取得したユーザー数')
        print(len(users))
        styles = users[user_colum].get_attribute('style')
        # 画像なしのユーザーを探す
        while "noimage" not in styles:
          user_colum += 1
          print(user_colum)
          styles = users[user_colum].get_attribute('style')
          if user_colum == len(users):
             break
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", users[user_colum])
        users[user_colum].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        send_status = True
        m = driver.find_elements(By.XPATH, value="//*[@id='ds_main']/div/p")
        if len(m):
          print(m[0].text)
          if m[0].text == "プロフィール情報の取得に失敗しました":
              send_status = False
              user_colum += 1
        # 自己紹介文に業者、通報が含まれているかチェック
        if len(driver.find_elements(By.CLASS_NAME, value="translate_body")):
          contains_violations = driver.find_element(By.CLASS_NAME, value="translate_body")
          driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", contains_violations)
          self_introduction_text = contains_violations.text.replace(" ", "").replace("\n", "")
          if '通報' in self_introduction_text or '業者' in self_introduction_text:
              print('自己紹介文に危険なワードが含まれていました')
              send_status = False
              user_colum += 1
        # メッセージ履歴があるかチェック
        mail_field = driver.find_element(By.ID, value="ds_nav")
        mail_history = mail_field.find_element(By.ID, value="mail-history")
        display_value = mail_history.value_of_css_property("display")
        if display_value != "none":
            print('メール履歴があります')
            send_status = False
            user_colum += 1
        # メール送信
        if send_status:
          do_mail_icon = driver.find_elements(By.CLASS_NAME, value="ds_profile_target_btn")
          do_mail_icon[0].click()
          # 初めましてメッセージを入力
          text_area = driver.find_element(By.ID, value="text-message")
          text_area.send_keys(fst_message)
          # 送信
          send_mail = driver.find_element(By.ID, value="submitButton")
          send_mail.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          # 画像があれば送信
          if fst_message_img:
            img_conform = driver.find_element(By.ID, value="media-confirm")
            plus_icon = driver.find_element(By.CLASS_NAME, value="icon-message_plus")
            plus_icon.click()
            time.sleep(1)
            upload_file = driver.find_element(By.ID, "upload_file")
            upload_file.send_keys(fst_message_img)
            time.sleep(2)
            submit = driver.find_element(By.ID, value="submit_button")
            submit.click()
            while img_conform.is_displayed():
                time.sleep(2)
          send_cnt += 1
          user_colum += 1
          print(f"fst_message ~{send_cnt}~")
        driver.get("https://happymail.co.jp/sp/app/html/profile_list.php")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        # リモーダル画面が出たら閉じる
        remodal = driver.find_elements(By.CLASS_NAME, value="remodal-close")
        if len(remodal):
          print('リモーダル画面')
          remodal[0].click()
          time.sleep(wait_time)
    print("fstmail end")
    driver.quit()  
  except Exception as e:  
    print(traceback.format_exc())
    driver.quit()  

def check_new_mail(driver, wait, name):
  return_list = []
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT login_id, passward, fst_message, return_foot_message, conditions_message FROM happymail WHERE name = ?', (name,))
  login_id = None
  for row in cur:
      login_id = row[0]
      login_pass = row[1]
      fst_message = row[2]
      return_foot_message = row[3]
      conditions_message = row[4]   
  if not login_id:
    print(f"{name}のhappymailキャラ情報を取得できませんでした")
    return
  driver.delete_all_cookies()
  driver.get("https://happymail.jp/login/")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  wait_time = random.uniform(2, 5)
  time.sleep(wait_time)
  id_form = driver.find_element(By.ID, value="TelNo")
  id_form.send_keys(login_id)
  pass_form = driver.find_element(By.ID, value="TelPass")
  pass_form.send_keys(login_pass)
  time.sleep(wait_time)
  send_form = driver.find_element(By.ID, value="login_btn")
  send_form.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  remodal = driver.find_elements(By.CLASS_NAME,value="remodal-close")
  if len(remodal):
     remodal.click()
     time.sleep(1)
  warning = driver.find_elements(By.CLASS_NAME, value="information__dialog")
  if len(warning):
     return_list.append(f"{name},{login_id}:{login_pass} ハッピーメールに警告画面が出ている可能性があります")
     return return_list
  name_elem = ""
  try:
    name_elem = driver.find_element(By.CLASS_NAME, "ds_user_display_name")
  except NoSuchElementException:
      time.sleep(7)
      name_elem = driver.find_elements(By.CLASS_NAME, "ds_user_display_name")
      name_elem = name_elem[0]
      pass
  if not name_elem:
     return_list.append(f"{name},{login_id}:{login_pass} ハッピーメールに警告画面が出ている可能性があります.....")
     return return_list
  name = name_elem.text  
  message_icon_candidates = driver.find_elements(By.CLASS_NAME, value="ds_nav_item")
  message_icon = ""
  for message_icon_candidate in message_icon_candidates:
     if "メッセージ" in message_icon_candidate.text:
        message_icon = message_icon_candidate
  if message_icon:
    new_message = message_icon.find_elements(By.CLASS_NAME, value="ds_red_circle")
    
  else:
     print("message_iconが見つかりません")
     return
  # 新着があった
  if len(new_message):
     link = message_icon.find_elements(By.TAG_NAME, value="a")
     link[0].click()
     wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
     time.sleep(2)
     #  未読のみ表示
     only_new_message = driver.find_elements(By.CLASS_NAME, value="ds_message_tab_item")[1]
     only_new_message.click()
     time.sleep(1)
    
     new_mail = driver.find_elements(By.CLASS_NAME, value="ds_list_r_kidoku")  
     if not len(new_mail):
         list_load = driver.find_element(By.ID, value="load_bL")
         list_load.click()
         time.sleep(2)
     #新着がある間はループ  
     while len(new_mail):
        parent_element = new_mail[0].find_element(By.XPATH, value="..")
        next_element = parent_element.find_element(By.XPATH, value="following-sibling::*")
        date = next_element.find_elements(By.CLASS_NAME, value="ds_message_date")
        date_numbers = re.findall(r'\d+', date[0].text)
        arrival_datetime = datetime(int(datetime.now().year), int(date_numbers[0]), int(date_numbers[1]), int(date_numbers[2]), int(date_numbers[3])) 
        now = datetime.today()
        elapsed_time = now - arrival_datetime
        # print(f"メール到着からの経過時間{elapsed_time}")
        # 4分経過しているか
        if elapsed_time >= timedelta(minutes=4):
          # print("4分以上経過しています。")
          new_mail[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
          send_message = driver.find_elements(By.CLASS_NAME, value="message__block--send")          
          if len(send_message):
            send_text = send_message[-1].find_elements(By.CLASS_NAME, value="message__block__body__text")[0].text
            if not send_text:
                send_text = send_message[-2].find_elements(By.CLASS_NAME, value="message__block__body__text")[0].text
            # print(send_text)
            
            # print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")
            # if name == "りこ":
            print("<<<<<<<<<<<>>>>>>>>>>>>>")
            print(send_text)
            print("---------------------------------------")
            print(fst_message == send_text)
            print("---------------------------------------")
            print(return_foot_message == send_text)
            print("---------------------------------------")
            print("掲示板メッセージ" in send_text)

            if fst_message == send_text or return_foot_message == send_text or "掲示板メッセージ" in send_text:
                # print("やった")
                text_area = driver.find_element(By.ID, value="text-message")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_area)
                text_area.send_keys(conditions_message)
                # 送信
                send_mail = driver.find_element(By.ID, value="submitButton")
                send_mail.click()
                wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                time.sleep(wait_time)
            else:
              #  print('やり取りしてますん')
               user_name = driver.find_elements(By.CLASS_NAME, value="app__navbar__item--title")[0]
               user_name = user_name.text
               receive_contents = driver.find_elements(By.CLASS_NAME, value="message__block--receive")[-1]
              #  print(f"{user_name}:{receive_contents.text}")
               return_message = f"{name}happymail,{login_id}:{login_pass}\n{user_name}「{receive_contents.text}」"
               return_list.append(return_message)
          else:
            text_area = driver.find_element(By.ID, value="text-message")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_area)
            text_area.send_keys(fst_message)
            # 送信
            send_mail = driver.find_element(By.ID, value="submitButton")
            send_mail.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(wait_time)
        else:
           if len(return_list):
              return return_list
           else:
              return None
        driver.get("https://happymail.co.jp/sp/app/html/message_list.php")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(2)
        new_mail = driver.find_elements(By.CLASS_NAME, value="ds_list_r_kidoku")
  if len(return_list):
    return return_list
  else:
    return None
       
     
