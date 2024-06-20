import time
import sqlite3
import random
import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import traceback
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from selenium.webdriver.common.by import By
from widget import pcmax
from selenium.webdriver.support.select import Select
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as G_options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import setting


def get_driver():
    options = G_options()
    options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=456,912")
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-cache")
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)
    return driver, wait

def get_firefox_driver():
  options = Options()
  # Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7
  user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7"
  profile = webdriver.FirefoxProfile()
  profile.set_preference("general.useragent.override", user_agent)
  options.profile = profile
  # options.add_argument('--headless')
  options.add_argument('--width=456')
  options.add_argument('--height=912')
  driver = webdriver.Firefox(options=options, )
  # driver.set_window_size(456, 912)
  return driver

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
  dbpath = setting.db
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

def send_conditional(user_name, user_address, mailaddress, password, text, site):
  subject = f'{site}でやり取りしてた{user_name}さんでしょうか？'
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

def send_error(chara, error_message):
  print("エラー送信＞＞＞＜＜＜＜＜＜＜")
  print(f"{chara}  :  {error_message}")
  mailaddress = 'kenta.bishi777@gmail.com'
  password = 'rjdzkswuhgfvslvd'
  text = f"キャラ名:{chara} \n {error_message}"
  subject = "サイト回しエラーメッセージ"
  address_from = 'kenta.bishi777@gmail.com'
  # address_to = "ryapya694@ruru.be"
  address_to = "gifopeho@kmail.li"
  smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpobj.starttls()
  smtpobj.login(mailaddress, password)
  msg = MIMEText(text)
  msg['Subject'] = subject
  msg['From'] = address_from
  msg['To'] = address_to
  msg['Date'] = formatdate()
  try:
    smtpobj.send_message(msg)
  except smtplib.SMTPDataError as e:
    print(f"SMTPDataError: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")
  
  smtpobj.close()

def send_mail(message):
  mailaddress = 'kenta.bishi777@gmail.com'
  password = 'rjdzkswuhgfvslvd'
  text = message
  subject = "ハッピーメールサイト回し件数"
  address_from = 'kenta.bishi777@gmail.com'
  # address_to = "ryapya694@ruru.be"
  address_to = "gifopeho@kmail.li"
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
  history_user_list = []
  p_w = ""
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
  if len(mail_icon):
    if not user_name in history_user_list:
        print(777)
        print(history_user_list)
        mail_icon_cnt = 0
        history_user_list.append(user_name)
        happy_foot_user[0].click()
    else:
      print(666)
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
  else:
    happy_foot_user[0].click()

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
    while user_cnt + 1 < len(div) - 1:
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
    # print(888)
    # print(user_name)
    # print(history_user_list)
    mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
    if len(mail_icon):
      while len(mail_icon):
        if not user_name in history_user_list:
          print(777)
          mail_icon_cnt = 0
          history_user_list.append(user_name)
          happy_foot_user[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
          driver.get("https://happymail.co.jp/sp/app/html/ashiato.php")
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(wait_time)
          happy_foot_user = driver.find_elements(By.CLASS_NAME, value="ds_post_head_main_info")
          name_field = happy_foot_user[0].find_element(By.CLASS_NAME, value="ds_like_list_name")
          mail_icon = name_field.find_elements(By.TAG_NAME, value="img")
        else:
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
    else:
      happy_foot_user[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)


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

def get_debug_chromedriver():
  # options = Options()
  # options.add_argument("start-maximized")
  # options.add_argument("enable-automation")
  # options.add_argument("--disable-infobars")
  # options.add_argument("--dns-prefetch-disable")
  # options.add_argument('--disable-extensions')
  # options.add_argument("--disable-dev-shm-usage")
  # options.add_argument("--disable-browser-side-navigation")
  # options.add_argument("--disable-gpu")
  # options.add_argument('--ignore-certificate-errors')
  # options.add_argument('--ignore-ssl-errors')
  # prefs = {"profile.default_content_setting_values.notifications" : 2}
  # options.add_experimental_option("prefs",prefs)
  # options.add_argument("--headless=new")
  # # options.add_argument('--headless')
  # options.add_argument("--no-sandbox")
  # options.add_argument("--remote-debugging-port=9222")
  # options.add_experimental_option("detach", True)
  # service = Service(executable_path="./chromedriver")
  # driver = webdriver.Chrome(service=service, options=options)
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  service = Service(executable_path="../chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  wait = WebDriverWait(driver, 15)

  return driver

def check_new_mail_gmail(driver, wait, name, mail_address):
  if not mail_address:
    return None
  return_list = []
  dbpath = setting.db
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT window_Handle FROM gmail WHERE mail_address = ?', (mail_address,))
  w_h = ""
  for row in cur:
      w_h = row[0]
  if not w_h:
    return None
  cur.execute('SELECT login_id, passward FROM pcmax WHERE name = ?', (name,))
  login_id = ""
  passward = ""
  for row in cur:
    login_id = row[0]
    passward = row[1]
  try:
      driver.switch_to.window(w_h)
      time.sleep(2)
      driver.get("https://mail.google.com/mail/mu")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)  
  except TimeoutException as e:
      print("TimeoutException")
      driver.refresh()
  except Exception as e:
      print(f"<<<<<<<<<<エラー：{mail_address}>>>>>>>>>>>")
      print(traceback.format_exc())
      driver.quit()
  # メニューをクリック
  # カスタム属性の値を持つ要素をXPathで検索
  custom_value = "メニュー"
  xpath = f"//*[@aria-label='{custom_value}']"
  element = driver.find_elements(By.XPATH, value=xpath)
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2) 
  element[0].click()
  time.sleep(1) 
  custom_value = "toggleaccountscallout+21"
  xpath = f"//*[@data-control-type='{custom_value}']"
  element = driver.find_elements(By.XPATH, value=xpath)
  if len(element):
      time.sleep(2)
      element = driver.find_elements(By.XPATH, value=xpath)
  address = element[0].text
  # メインボックスのチェック
  menuitem_element = driver.find_elements(By.XPATH, '//*[@role="menuitem"]')
  main_box = menuitem_element[0]
  main_box.click()
  time.sleep(1)
  emails = driver.find_elements(By.XPATH, value='//*[@role="listitem"]')
  for email in emails:
    new_email = email.find_elements(By.TAG_NAME, value="b")
    if len(new_email):
      child_elements = email.find_elements(By.CLASS_NAME, value="Rk")
      if child_elements[0].text:  # テキストが空でない場合
          # print(f"この子要素にテキストが含まれています: {child_elements[0].text}")
          return_list.append(f"{address},{login_id}:{passward}\n「{child_elements[0].text}」")
      email.click()
      time.sleep(2)
      driver.back()
      time.sleep(1)
    else:
      continue
      
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
  emails = driver.find_elements(By.XPATH, value='//*[@role="listitem"]')
  for email in emails:
    new_email = email.find_elements(By.TAG_NAME, value="b")
    if len(new_email):
      child_elements = email.find_elements(By.CLASS_NAME, value="Rk")
      if child_elements[0].text:  # テキストが空でない場合
          # print(f"この子要素にテキストが含まれています: {child_elements[0].text}")
          return_list.append(f"{address}:迷惑フォルダ,{login_id}:{passward}\n「{child_elements[0].text}」")
      email.click()
      time.sleep(2)
      driver.back()
      time.sleep(1)
    else:
      continue
  custom_value = "メニュー"
  xpath = f"//*[@aria-label='{custom_value}']"
  element = driver.find_elements(By.XPATH, value=xpath)
  element[0].click()
  # window_handles = driver.window_handles
  # for window_handle in window_handles:
  #   driver.switch_to.window(window_handle)
  #   current_url = driver.current_url
  #   if current_url.startswith("https://mail.google.com/mail/mu"):
  #       print("URLがhttps://mail.google.com/mail/muから始まります。")
  #   else:
  #       print("URLがhttps://mail.google.com/mail/muから始まりません。")
  if len(return_list):
    return return_list
  else:
    return None
