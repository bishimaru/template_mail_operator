from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import setting
import re
from selenium.common.exceptions import TimeoutException


genre_dic = {0:"スグ会いたい", 1:"スグじゃないけど"}
post_area_tokyo = ["千代田区", "中央区", "港区", "新宿区", "文京区", "台東区",
                   "品川区", "目黒区", "大田区", "世田谷区", "渋谷区", "中野区",
                   "杉並区", "豊島区", "北区", "荒川区", "板橋区", "練馬区",
                   "立川市", "武蔵野市", "三鷹市", "府中市", "西東京市", "国分寺市",
                   "狛江市", "調布市"]
post_area_kanagawa = ["横浜市鶴見区", "横浜市神奈川区", "横浜市西区", "横浜市中区", "横浜市南区", "横浜市保土ｹ谷区", 
                      "横浜市磯子区", "横浜市金沢区", "横浜市港北区", "横浜市戸塚区", "横浜市港南区", "横浜市旭区",
                      "横浜市緑区", "横浜市瀬谷区", "横浜市栄区", "横浜市泉区", "横浜市青葉区", "横浜市都筑区", 
                      "川崎市川崎区", "川崎市幸区", "川崎市中原区", "川崎市高津区", "川崎市多摩区", "川崎市宮前区", 
                      "川崎市麻生区",]
post_area_saitama = ["さいたま市西区", "さいたま市北区", "さいたま市大宮区", "さいたま市見沼区", "さいたま市中央区",
                      "さいたま市桜区", "さいたま市浦和区", "さいたま市南区", "さいたま市緑区", "さいたま市岩槻区",
                      "川口市", "戸田市", "和光市",]
post_area_chiba = ["千葉市中央区", "千葉市花見川区", "千葉市稲毛区", "千葉市若葉区",
                    "千葉市緑区", "千葉市美浜区", "市川市", "船橋市",]

post_area_dic = {"東京都":post_area_tokyo, "神奈川県":post_area_kanagawa, "埼玉県":post_area_saitama, "千葉県":post_area_chiba}
# detail_post_area_list = [post_area_tokyo, post_area_kanagawa, post_area_saitama, post_area_chiba]

def login(driver, wait):
  try:
    driver.refresh()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)
    url = driver.current_url
    if url != "https://pcmax.jp/pcm/index.php":
      driver.get("https://pcmax.jp/pcm/index.php")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    login = driver.find_elements(By.CLASS_NAME, value="login")
    if len(login):    
      login[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
      submit = driver.find_element(By.NAME, value="login")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", submit)
      submit.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
  except TimeoutException as e:
    print("TimeoutException")
    driver.refresh()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    return login(driver, wait)
    
def re_post(name, pcmax_windowhandle, driver, genre_flag):
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(pcmax_windowhandle)
  wait_time = random.uniform(3, 4)
  login(driver, wait)
  if setting.mac_os:
    os.system("osascript -e 'display notification \"PCMAX掲示板再投稿中...\" with title \"{}\"'".format(name))
  # MENUをクリック
  menu = driver.find_element(By.ID, value='sp_nav')
  menu.click()
  time.sleep(wait_time)
  # 掲示板履歴をクリック　
  bulletin_board_history = driver.find_element(By.CLASS_NAME, value="nav-content-list")
  bulletin_board_history = bulletin_board_history.find_elements(By.TAG_NAME, value="dd")
  for i in bulletin_board_history:
    if i.text == "投稿履歴・編集":
      bulletin_board_history = i.find_element(By.TAG_NAME, value="a")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", bulletin_board_history)
      bulletin_board_history.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      break
  #掲示板4つ再投稿
  link_list = []
  copies = driver.find_elements(By.CLASS_NAME, value="copy_title")
  if not len(copies):
    return
  for i in range(len(copies)):
    copy = copies[i].find_elements(By.TAG_NAME, value="a")
    for a_element in copy:
      link_text = a_element.text
      if link_text == "コピーする":
        link = a_element.get_attribute("href")
        link_list.append(link)
  for i in link_list:
    driver.get(i)
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    detail_selected = driver.find_element(By.XPATH, value="/html/body/form/div[2]/div[3]/div[2]")
    detail_selected = detail_selected.text.replace(' ', '')
    # 前回の都道府県を取得
    last_area = driver.find_element(By.XPATH, value="/html/body/form/div[2]/div[2]/div[2]")
    last_area = last_area.text.replace(' ', '').replace('"', '')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(last_area)
    print("前回の詳細地域 ~" + str(detail_selected) + "~" )
    # 編集するをクリック 
    edit_post = driver.find_element(By.ID, value="alink")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", edit_post)
    time.sleep(1)
    edit_post.click()
    wait = WebDriverWait(driver, 15)
    time.sleep(wait_time)
    # ジャンルを選択
    select_genre = driver.find_element(By.ID, value="selectb")
    select = Select(select_genre)
    select.select_by_visible_text(genre_dic[genre_flag])
    time.sleep(1)

    # 投稿地域を選択
    area = driver.find_element(By.ID, "prech")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", area)
    time.sleep(1)
    select = Select(area)
    select.select_by_visible_text(last_area)
    time.sleep(1)
    # 詳細地域を選択
    detailed_area = driver.find_element(By.NAME, value="city_id")
    select = Select(detailed_area)
    try:
      post_area_dic[last_area].remove(detail_selected)
    except ValueError:
      pass
    detail_area = random.choice(post_area_dic[last_area])
    print('今回の詳細地域 ~' + str(detail_area) + "~")
    select.select_by_visible_text(detail_area)
    time.sleep(1)
    # メール受付数を変更
    mail_reception = driver.find_element(By.NAME, "max_reception_count")
    select = Select(mail_reception)
    select.select_by_visible_text("5通")
    time.sleep(1)
    # 掲示板に書く 
    write_bulletin_board = driver.find_element(By.ID, value="bbs_write_btn")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", write_bulletin_board)
    write_bulletin_board.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    # 利用制限チェック
    usage_limit = driver.find_elements(By.CLASS_NAME, value="white_box")
    if len(usage_limit):
      print("利用制限画面が出ました")
      # time.sleep(2)
      # driver.get("https://pcmax.jp/pcm/index.php")
      return
    # 掲示板投稿履歴をクリック
    bulletin_board_history = driver.find_element(By.XPATH, value="//*[@id='wrap']/div[2]/table/tbody/tr/td[3]/a")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", bulletin_board_history)
    bulletin_board_history.click()
    time.sleep(1)
  if setting.mac_os:
    os.system("osascript -e 'beep' -e 'display notification \"PCMAX掲示板再投稿に成功しました◎\" with title \"{}\"'".format(name))
  driver.get("https://pcmax.jp/pcm/index.php")
  
def return_footpoint(name, pcmax_windowhandle, driver, return_foot_message, cnt, return_foot_img):
  if cnt == 0:
    return
  wait = WebDriverWait(driver, 15)
  driver.switch_to.window(pcmax_windowhandle)
  wait_time = random.uniform(2, 3)
  time.sleep(1)
  login(driver, wait)
  # 新着メッセージの確認
  have_new_massage_users = []
  new_message = driver.find_element(By.CLASS_NAME, value="message")
  new_message.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(wait_time)
  user_info = driver.find_elements(By.CLASS_NAME, value="user_info")
  print(len(user_info))
  # 新着ありのユーザーをリストに追加
  for usr_info in user_info:
    unread = usr_info.find_elements(By.CLASS_NAME, value="unread1")
    if len(unread):
      name = usr_info.find_element(By.CLASS_NAME, value="name").text
      if len(name) > 7:
        name = name[:7] + "…"
      have_new_massage_users.append(name)
  print("新着メッセージリスト")
  print(have_new_massage_users)
  driver.get("https://pcmax.jp/pcm/index.php")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  # 右下のキャラ画像をクリック
  chara_img = driver.find_element(By.XPATH, value="//*[@id='sp_footer']/a[5]")
  chara_img.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(wait_time)
  # //*[@id="contents"]/div[2]/div[2]/ul/li[5]/a
  # 足あとをクリック
  footpoint = driver.find_element(By.XPATH, value="//*[@id='contents']/div[2]/div[2]/ul/li[5]/a")
  footpoint.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(wait_time)
  # ページの高さを取得
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
    # ページの最後までスクロール
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # ページが完全に読み込まれるまで待機
    time.sleep(1)
    # 新しい高さを取得
    new_height = driver.execute_script("return document.body.scrollHeight")
    # ページの高さが変わらなければ、すべての要素が読み込まれたことを意味する
    if new_height == last_height:
        break
    last_height = new_height
  # ユーザーを取得
  user_list = driver.find_element(By.CLASS_NAME, value="list-content")
  div = user_list.find_elements(By.XPATH, value='./div')
  # リンクを取得
  user_cnt = 1
  mail_history = 0
  send_count = 0
  link_list = []
  while user_cnt <= 40:
    # 新着リストの名前ならスキップ
    name = div[user_cnt].find_element(By.CLASS_NAME, value="user-name")
    if name.text in have_new_massage_users:
      user_cnt += 1
    else:
      a_tags = div[user_cnt].find_elements(By.TAG_NAME, value="a")
      # print("aタグの数：" + str(len(a_tags)))
      if len(a_tags) > 1:
        link = a_tags[1].get_attribute("href")
        # print(link)
        link_list.append(link)
      user_cnt += 1
  for i in link_list:
    if mail_history == 7:
      break
    driver.get(i)
    # //*[@id="profile-box"]/div/div[2]/p/a/span
    sent = driver.find_elements(By.XPATH, value="//*[@id='profile-box']/div/div[2]/p/a/span")
    if len(sent):
      print('送信履歴があります')
      time.sleep(2)
      mail_history += 1
      continue  
    # 自己紹介文をチェック
    self_introduction = driver.find_elements(By.XPATH, value="/html/body/main/div[4]/div/p")
    if len(self_introduction):
      self_introduction = self_introduction[0].text.replace(" ", "").replace("\n", "")
      if '通報' in self_introduction or '業者' in self_introduction:
        print('自己紹介文に危険なワードが含まれていました')
        time.sleep(wait_time)
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
      continue
    time.sleep(1)
    # メッセージをクリック
    message = driver.find_elements(By.ID, value="message1")
    if len(message):
      message[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(3)
    else:
      continue
    # 画像があれば送付
    if return_foot_img:
      picture_icon = driver.find_elements(By.CLASS_NAME, value="mail-menu-title")
      picture_icon[0].click()
      time.sleep(1)
      picture_select = driver.find_element(By.ID, "my_photo")
      select = Select(picture_select)
      select.select_by_visible_text(return_foot_img)
      
    # メッセージを入力
    text_area = driver.find_element(By.ID, value="mdc")
    text_area.send_keys(return_foot_message)
    time.sleep(4)
    print("マジ送信 " + str(maji_soushin) + " ~" + str(send_count + 1) + "~")
    # メッセージを送信
    if maji_soushin:
      send = driver.find_element(By.CLASS_NAME, value="maji_send")
      send.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
      send_link = driver.find_element(By.ID, value="link_OK")
      send_link.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      send_count += 1
      mail_history = 0
      
    else:
      send = driver.find_element(By.ID, value="send_n")
      send.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(wait_time)
      send_count += 1
      mail_history = 0

    if send_count == cnt:
      break
  driver.get("https://pcmax.jp/pcm/index.php")
def make_footprints(name, pcmax_id, pcmax_pass, driver, wait):
  driver.delete_all_cookies()
  driver.get("https://pcmax.jp/pcm/file.php?f=login_form")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  wait_time = random.uniform(2, 9)
  time.sleep(wait_time)
  id_form = driver.find_element(By.ID, value="login_id")
  id_form.send_keys(pcmax_id)
  pass_form = driver.find_element(By.ID, value="login_pw")
  pass_form.send_keys(pcmax_pass)
  time.sleep(1)
  send_form = driver.find_element(By.NAME, value="login")
  send_form.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(1)
  #プロフ検索をクリック
  footer_icons = driver.find_element(By.ID, value="sp_footer")
  search_profile = footer_icons.find_element(By.XPATH, value="./*[1]")
  search_profile.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(1)
  # ページの高さを取得
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
    # ページの最後までスクロール
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # ページが完全に読み込まれるまで待機
    time.sleep(2)
    user_list = driver.find_element(By.CLASS_NAME, value="content_inner")
    users = user_list.find_elements(By.XPATH, value='./div')
    # print(len(users))
    if len(users) > 200:
      #  print('ユーザー件数200　OVER')
       break
    # 新しい高さを取得
    new_height = driver.execute_script("return document.body.scrollHeight")
    # ページの高さが変わらなければ、すべての要素が読み込まれたことを意味する
    if new_height == last_height:
        break
    last_height = new_height
  # https://pcmax.jp/mobile/profile_detail.php?user_id=" + user_id + "&search=prof&condition=648ac5f23df62&page=1&sort=&stmp_counter=13&js=1
  # リンクを取得
  user_cnt = 1
  link_list = []
  for user_cnt in range(len(users)):
    # 実行確率（80%の場合）
    execution_probability = 0.80
    # ランダムな数値を生成し、実行確率と比較
    if random.random() < execution_probability:
      user_id = users[user_cnt].get_attribute("id")
      if user_id == "loading":
        print('id=loading')
        while user_id != "loading":
          time.sleep(2)
          user_id = users[user_cnt].get_attribute("id")
      link = "https://pcmax.jp/mobile/profile_detail.php?user_id=" + user_id + "&search=prof&condition=648ac5f23df62&page=1&sort=&stmp_counter=13&js=1"
      link_list.append(link)
    # else:
      #  print('無双RUSH終了')
  print(f"ユーザー件数：{len(link_list)}")
  for i, link_url in enumerate(link_list):

      print(f"{name}: pcmax、足ペタ件数: {i + 1}")
      driver.get(link_url)
      time.sleep(wait_time)
      if i == 42:
         break
  driver.refresh()
  

