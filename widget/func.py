import time
import sqlite3
import random
import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import setting
import traceback
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from widget import pcmax
from selenium.webdriver.support.select import Select
from datetime import timedelta

def timer(fnc, seconds, h_cnt, p_cnt):  
  start_time = time.time() 
  fnc(h_cnt, p_cnt)
  while True:
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    if elapsed_time >= seconds:
      start_time = time.time() 
      break
    else:
      time.sleep(10)
  return True

def get_windowhandle(site, name):
  # DB
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # データ検索
  # cur.execute('UPDATE happymail SET window_handle = ? WHERE name = ?', (mohu1, mohu2))
  if site == "happymail":
    cur.execute('SELECT window_handle FROM happymail WHERE name = ?', (name,))
  elif site == "pcmax":
    cur.execute('SELECT window_handle FROM pcmax WHERE name = ?', (name,))
  w_h = ""
  for row in cur:
    w_h = row[0]
  conn.close()
  return w_h

def send_conditional(user_name, user_address, mailaddress, password, text):
  subject = f'{user_name}さんですか？'
  text = text
  address_from = mailaddress
  address_to = user_address
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

def h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img):
  start_time = time.time() 
  wait = WebDriverWait(driver, 10)
  wait_time = random.uniform(1, 3)
  # wait_time = 2
  # ハッピーメールの足跡リストまで
  driver.switch_to.window(h_w)
  driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(wait_time)
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
  # 足跡ユーザーを取得
  happy_foot_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
  while len(happy_foot_user) == 0:
      time.sleep(2)
      happy_foot_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")  
  mail_icon_cnt = 0
  name_field = happy_foot_user[0].find_element(By.CLASS_NAME, value="ds_like_list_name")
  user_name = name_field.text
  mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
  mail_icon_cnt = 0
  while len(mail_icon):
    print('メールアイコンがあります')
    mail_icon_cnt += 1
    print(f'メールアイコンカウント{mail_icon_cnt}')
    name_field = happy_foot_user[mail_icon_cnt].find_element(By.CLASS_NAME, value="ds_like_list_name")
    user_name = name_field.text
    mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
    # # メールアイコンが7つ続いたら終了
    if mail_icon_cnt == 5:
      # ds_logo = driver.find_element(By.CLASS_NAME, value="ds_logo")
      # top_link = ds_logo.find_element(By.TAG_NAME, value="a")
      # top_link.click()
      # wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      # time.sleep(wait_time)
      print("メールアイコンが5続きました")
  # ユーザークリック
  happy_foot_user[mail_icon_cnt].click()

  # PCMAXの足跡リストまで
  if p_w:
    driver.switch_to.window(p_w)
    pcmax.login(driver, wait)
    # 新着メッセージの確認
    have_new_massage_users = []
    new_message = driver.find_element(By.CLASS_NAME, value="message")
    new_message.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    user_info = driver.find_elements(By.CLASS_NAME, value="user_info")
    # 新着ありのユーザーをリストに追加
    for usr_info in user_info:
      unread = usr_info.find_elements(By.CLASS_NAME, value="unread1")
      if len(unread):
        new_mail_pcmax_name = usr_info.find_element(By.CLASS_NAME, value="name").text
        if len(new_mail_pcmax_name) > 7:
          new_mail_pcmax_name = new_mail_pcmax_name[:7] + "…"
        have_new_massage_users.append(new_mail_pcmax_name)
    print("新着メッセージリスト")
    print(have_new_massage_users)
    driver.get("https://pcmax.jp/pcm/index.php")
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)
    # 右下のキャラ画像をクリック
    chara_img = driver.find_elements(By.XPATH, value="//*[@id='sp_footer']/a[5]")
    if len(chara_img):
      chara_img[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
    else: #番号確認画面
      return
    # //*[@id="contents"]/div[2]/div[2]/ul/li[5]/a
    # 足あとをクリック
    footpoint = driver.find_element(By.XPATH, value="//*[@id='contents']/div[2]/div[2]/ul/li[5]/a")
    footpoint.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    for i in range(3):
      # ページの最後までスクロール
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      # ページが完全に読み込まれるまで待機
      time.sleep(1)
    # ユーザーを取得
    user_list = driver.find_element(By.CLASS_NAME, value="list-content")
    div = user_list.find_elements(By.XPATH, value='./div')
    # ユーザーのlinkをリストに保存
    link_list = []
    user_cnt = 0
    # print(len(div))
    while user_cnt + 1 < len(div):
      # 新着リストの名前ならスキップ
      new_mail_name = div[user_cnt].find_element(By.CLASS_NAME, value="user-name")
      if new_mail_name.text in have_new_massage_users:
        user_cnt += 1
      else:
        a_tags = div[user_cnt].find_elements(By.TAG_NAME, value="a")
        # print("aタグの数：" + str(len(a_tags)))
        if len(a_tags) > 1:
          link = a_tags[1].get_attribute("href")
          # print(link)
          link_list.append(link)
        user_cnt += 1
  # メッセージを送信
  pcmax_return_message_cnt = 1
  pcmax_transmission_history = 0
  pcmax_send_flag = True
  foot_cnt = 0
  p_foot_cnt = 0
  p_send_cnt = 0
  while cnt > foot_cnt:
    # happymail
    driver.switch_to.window(h_w)
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    happy_send_status = True
    m = driver.find_elements(By.XPATH, value="//*[@id='ds_main']/div/p")
    if len(m):
      print(m[0].text)
      if m[0].text == "プロフィール情報の取得に失敗しました": 
          continue
    # 自己紹介文に業者、通報が含まれているかチェック
    if len(driver.find_elements(By.CLASS_NAME, value="translate_body")):
      contains_violations = driver.find_element(By.CLASS_NAME, value="translate_body")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", contains_violations)
      self_introduction_text = contains_violations.text.replace(" ", "").replace("\n", "")
      if '通報' in self_introduction_text or '業者' in self_introduction_text:
          print('ハッピーメール：自己紹介文に危険なワードが含まれていました')
          happy_send_status = False
    # メッセージ履歴があるかチェック
    mail_field = driver.find_element(By.ID, value="ds_nav")
    mail_history = mail_field.find_element(By.ID, value="mail-history")
    display_value = mail_history.value_of_css_property("display")
    if display_value != "none":
        print('ハッピーメール：メール履歴があります')
        # print(user_name)
        # user_name_list.append(user_name) 
        happy_send_status = False
        mail_icon_cnt += 1
    # メールするをクリック
    if happy_send_status:
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
      if h_return_foot_img:
        print('画像img')
        print(h_return_foot_img)
        img_conform = driver.find_element(By.ID, value="media-confirm")
        plus_icon = driver.find_element(By.CLASS_NAME, value="icon-message_plus")
        plus_icon.click()
        time.sleep(1)
        upload_file = driver.find_element(By.ID, "upload_file")
        upload_file.send_keys(h_return_foot_img)
        time.sleep(1)
        submit = driver.find_element(By.ID, value="submit_button")
        submit.click()
        while img_conform.is_displayed():
            time.sleep(1)
      foot_cnt += 1
      print(name + ':ハッピーメール：'  + str(foot_cnt) + "件送信")
      mail_icon_cnt = 0
      driver.get("https://happymail.co.jp/sp/app/html/ashiato.php")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      # https://happymail.co.jp/sp/app/html/ashiato.php
    else:
      driver.get("https://happymail.co.jp/sp/app/html/ashiato.php")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
    # 足跡ユーザーを取得
    time.sleep(1)
    happy_foot_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
    while len(happy_foot_user) == 0:
        time.sleep(1)
        happy_foot_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")    
    name_field = happy_foot_user[0].find_element(By.CLASS_NAME, value="ds_like_list_name")
    user_name = name_field.text
    mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
    while len(mail_icon):
      # print('ハッピーメール：メールアイコンがあります')
      mail_icon_cnt += 1
      # print(f'メールアイコンカウント{mail_icon_cnt}')
      name_field = happy_foot_user[mail_icon_cnt].find_element(By.CLASS_NAME, value="ds_like_list_name")
      user_name = name_field.text
      mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
      # # メールアイコンが7つ続いたら終了
      if mail_icon_cnt == 5:
        print("ハッピーメール：メールアイコンが5続きました")
    # ユーザークリック
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", happy_foot_user[mail_icon_cnt])
    time.sleep(1)
    happy_foot_user[mail_icon_cnt].click()

    # pcmax
    if p_w and pcmax_send_flag:
      transmission_history = 0
      driver.switch_to.window(p_w)
      time.sleep(1)
      driver.get(link_list[p_foot_cnt])
      time.sleep(wait_time)
      # お相手のご都合により表示できませんはスキップ
      main = driver.find_elements(By.TAG_NAME, value="main")
      if not len(main):
        p_foot_cnt += 1
        continue

      # 送信履歴が連続で続くと終了
      sent = driver.find_elements(By.XPATH, value="//*[@id='profile-box']/div/div[2]/p/a/span")
      if len(sent):
        pcmax_transmission_history += 1
        if pcmax_transmission_history == 5:
          pcmax_send_flag = False
        print('pcmax:送信履歴があります')
        print(f"送信履歴カウント：{pcmax_transmission_history}" )
        p_foot_cnt += 1
        time.sleep(1)
        continue
      # 自己紹介文をチェック
      self_introduction = driver.find_elements(By.XPATH, value="/html/body/main/div[4]/div/p")
      if len(self_introduction):
        self_introduction = self_introduction[0].text.replace(" ", "").replace("\n", "")
        if '通報' in self_introduction or '業者' in self_introduction:
          print('pcmax:自己紹介文に危険なワードが含まれていました')
          p_foot_cnt += 1
          continue
      # 残ポイントチェック
      point = driver.find_elements(By.ID, value="point")
      if len(point):
        point = point[0].find_element(By.TAG_NAME, value="span").text
        pattern = r'\d+'
        match = re.findall(pattern, point)
        if int(match[0]) > 1:
          maji_soushin = True
        else:
          maji_soushin = False
      else:
        time.sleep(wait_time)
        print(' 相手の都合により表示できません')
        p_foot_cnt += 1
        continue
      # メッセージをクリック
      message = driver.find_elements(By.ID, value="message1")
      if len(message):
        message[0].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)
      else:
        continue
      # 画像があれば送付
      if p_return_foot_img:
        picture_icon = driver.find_elements(By.CLASS_NAME, value="mail-menu-title")
        picture_icon[0].click()
        time.sleep(1)
        picture_select = driver.find_element(By.ID, "my_photo")
        select = Select(picture_select)
        select.select_by_visible_text(p_return_foot_img)
      # メッセージを入力
      text_area = driver.find_element(By.ID, value="mdc")
      text_area.send_keys(return_foot_message)
      time.sleep(1)
      p_foot_cnt += 1
      p_send_cnt += 1
      print("pcmax:マジ送信 " + str(maji_soushin) + " ~" + str(p_send_cnt) + "~")
      # メッセージを送信
      if maji_soushin:
        send = driver.find_element(By.CLASS_NAME, value="maji_send")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", send)
        send.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        send_link = driver.find_element(By.ID, value="link_OK")
        send_link.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # time.sleep(wait_time)
        pcmax_transmission_history = 0
      else:
        send = driver.find_element(By.ID, value="send_n")
        send.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # time.sleep(wait_time)
        # mail_history = 0
  # timedeltaオブジェクトを作成してフォーマットする
  elapsed_time = time.time() - start_time  # 経過時間を計算する
  elapsed_timedelta = timedelta(seconds=elapsed_time)
  elapsed_time_formatted = str(elapsed_timedelta)
  print(f"<<<<<<<<<<<<<h_p_foot 経過時間 {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
  print(f"pcmax足跡返し　{name}、{p_send_cnt}件")