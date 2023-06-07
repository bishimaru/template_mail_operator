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

def re_post(name, happy_windowhandle, driver, title, post_text, adult_flag):
  area_list = ["東京都", "千葉県", "埼玉県", "神奈川県"]
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(happy_windowhandle)
  wait_time = random.uniform(2, 3)
  # TOPに戻る
  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
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
  
  # 再掲載をクリック
  for repost_cnt in range(4):
  # 掲示板重複を削除する
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    area_texts = driver.find_elements(By.CLASS_NAME, value="ds_write_bbs_status")
    print(len(area_texts))
    area_texts_list = []
    for area in area_texts:
      area = area.text.replace(" ", "").replace("\n", "")
      area_texts_list.append(area)
    area_cnt = 0
    list = []
    print(area_texts_list)
    for area_text in area_texts_list:
      print(area_text)
      print(area_cnt)
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
    print(777)
    print(repost_cnt)
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
    print('<<<<<remodalの数>>>>>>')
    print(len(warning))
    if len(warning):
        print(666)
        print(repost_cnt)
        display_property = driver.execute_script("return window.getComputedStyle(arguments[0]).getPropertyValue('display');", warning[0])
        if display_property == 'block':
          # ２時間経ってない場合は終了
          print(999)
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
          print("取得した都道府県の数")
          print(len(area_text))
          area_text = area_text[repost_cnt].text.replace(" ", "").replace("\n", "")
          print('<<<<<<<<<<整形する前の都道府県>>>>>>>>>>>>')
          print(area_text)
          for area in area_list:
            if area in area_text:
              print('<<<<<<<<<都道府県>>>>>>>>')
              print(area)
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
              print(len(title))
              time.sleep(1)
              # 本文を書き込む
              text_field = driver.find_element(By.ID, value="text-message")
              driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_field)
              text_field.send_keys(post_text)
              print(len(post_text))
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
              print(555)
              print(len(success))
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

# def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt, return_foot_img):
def return_footpoint(name, happy_windowhandle, driver, return_foot_message, cnt):
    wait = WebDriverWait(driver, 15)
    driver.switch_to.window(happy_windowhandle)
    wait_time = random.uniform(2, 3)
    driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール足跡返し実行中...\" with title \"{}\"'".format(name))
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
      time.sleep(1)
      f_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
      while len(f_user) == 0:
         time.sleep(2)
         f_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
      name_field = f_user[user_icon].find_element(By.CLASS_NAME, value="ds_like_list_name")
      mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
      print(888)
      print(len(mail_icon))
      while len(mail_icon):
        print('メールアイコンがあります')
        user_icon += 1
        name_field = f_user[user_icon].find_element(By.CLASS_NAME, value="ds_like_list_name")
        print(777)
        print(user_icon)
        mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
        # メールアイコンが3つ続いたら終了
        if user_icon == 3:
          ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
          top_link = ds_logo.find_element(By.TAG_NAME, value="a")
          top_link.click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          return
        # send_status = False
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
          send_status = False
      # メールするをクリック
      if send_status:
        print('send_status = ' + str(send_status) +  ' ~' + str(i + 1) + "~")
        send_mail = mail_field.find_element(By.CLASS_NAME, value="ds_profile_target_btn")
        send_mail.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
        # 足跡返しを入力
        text_area = driver.find_element(By.ID, value="text-message")
        text_area.send_keys(return_foot_message)
        # 画像があれば送信
        # ダイヤログを操作する
        # plus_icon = driver.find_element(By.CLASS_NAME, value="icon-message_plus")
        # plus_icon.click()
        # time.sleep(2)
        # upload_icon = driver.find_element(By.CLASS_NAME, value="upload_picture")
        # driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", upload_icon)
        # upload_icon.click()
        # time.sleep(2)
        # # upload_input = driver.find_element(By.ID, value="upload_file")
        # # upload_input.send_keys(return_foot_img)
        # return

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
    if setting.mac_os:
       os.system("osascript -e 'beep' -e 'display notification \"ハッピーメール{}件の足跡返しに成功しました...\" with title \"{}\"'".format(i + 1, name))
  
