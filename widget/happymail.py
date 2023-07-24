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

def re_post(name, happy_windowhandle, driver, title, post_text, adult_flag, genre_flag):
  area_list = ["東京都", "千葉県", "埼玉県", "神奈川県"]
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(happy_windowhandle)
  wait_time = random.uniform(2, 3)
  # TOPに戻る
  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
  if setting.mac_os:
    os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中...\" with title \"{}\"'".format(name))
  # 警告画面が出たらスキップ
  # ds_main_header_text
  warning = driver.find_elements(By.CLASS_NAME, value="ds_main_header_text")
  if warning:
     print("警告画面が出ました")
     return
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
  if genre != genre_dict[genre_flag]:
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
      print(str(repost_cnt + 1) + "件の書き込みに成功しました")
    if setting.mac_os:
        os.system("osascript -e 'display notification \"ハッピーメール掲示板再投稿中に成功しました◎\" with title \"{}\"'".format(name))

def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt, return_foot_img):
    wait = WebDriverWait(driver, 15)
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
      user_age = f_user[user_icon].find_element(By.CLASS_NAME, value="ds_like_list_age")
      if user_age.text[:2] == "ナイ":
         print("年齢不詳")
         user_age = 31
      else:
        user_age = int(user_age.text[:2])
      if user_age >= 40:
         print(f'〜〜{user_age}代〜〜')
         # 実行確率（80%の場合）
         execution_probability = 0.20
         # ランダムな数値を生成し、実行確率と比較
         if random.random() < execution_probability:
            send_status = False
      # メールアイコンがあるかチェック
      print(user_name_list)
      if len(mail_icon):
        send_status = False
        print('メールアイコンがあります')
        mail_icon_cnt += 1
        print(f'メールアイコンカウント{mail_icon_cnt}')
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
          print('メール履歴があります')
          print(user_name)
          user_name_list.append(user_name) 
          send_status = False
          mail_icon_cnt += 1
      # メールするをクリック
      if send_status:
        print('send_status = ' + str(send_status) +  ' ~' + str(foot_cnt) + "~")
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
   wait_time = random.uniform(2, 4)
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
  
   for i in range(21):
      print(777)
      user_list = driver.find_elements(By.CLASS_NAME, value="profile_list_big_item")
      user = user_list[i].find_element(By.TAG_NAME, value="a")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", user)
      user.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      print(666)
      # いいね
      like_flag = False
      like = driver.find_elements(By.CLASS_NAME, value="icon-profile_like")
      like_icon = like[0].find_elements(By.CLASS_NAME, value="icon-on")
      if like_icon[0].is_displayed():
        # ランダムな数値を生成し、実行確率と比較
         # 実行確率
        execution_probability = 0.30
        if random.random() < execution_probability:
          print(555)
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
      print(444)
      driver.get("https://happymail.co.jp/sp/app/html/profile_list.php")
      # driver.back()
      print(f'{name}: ハッピーメール、足跡{i+1}件, いいね:{like_flag}')
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      
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
      # print(777)
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
  
