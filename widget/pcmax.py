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

def re_post(name, maiko_pcmax, driver):
  wait = WebDriverWait(driver, 15)
  handle_array = driver.window_handles
  driver.switch_to.window(maiko_pcmax)
  wait_time = random.uniform(3, 4)
  try:
    if setting.mac_os:
      os.system("osascript -e 'display notification \"PCMAX掲示板再投稿中...\" with title \"{}\"'".format(name))
    # MENUをクリック
    menu = driver.find_element(By.ID, value='sp_nav')
    menu.click()
    time.sleep(wait_time)
    # 掲示板履歴をクリック　
    bulletin_board_history = driver.find_element(By.XPATH, value="//*[@id='nav-content']/dl/dd[17]/a")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", bulletin_board_history)
    time.sleep(wait_time)
    bulletin_board_history.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(wait_time)
    #掲示板4つ再投稿
    link_list = []
    copies = driver.find_elements(By.CLASS_NAME, value="copy_title")
    for i in range(len(copies)):
      copy = copies[i].find_elements(By.TAG_NAME, value="a")
      link = copy[1].get_attribute("href")
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
      # 編集するをクリック 
      edit_post = driver.find_element(By.ID, value="alink")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", edit_post)
      time.sleep(1)
      edit_post.click()
      wait = WebDriverWait(driver, 15)
      time.sleep(wait_time)
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
      print('詳細地域のリスト')
      print(post_area_dic[last_area])
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
      # 掲示板投稿履歴をクリック
      bulletin_board_history = driver.find_element(By.XPATH, value="//*[@id='wrap']/div[2]/table/tbody/tr/td[3]/a")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", bulletin_board_history)
      bulletin_board_history.click()
      time.sleep(1)
    if setting.mac_os:
      os.system("osascript -e 'beep' -e 'display notification \"PCMAX掲示板再投稿に成功しました◎\" with title \"{}\"'".format(name))

  except Exception as e:
      if setting.mac_os:
        os.system("osascript -e 'display notification \"PCMAX掲示板再投稿中に失敗しました...\" with title \"{}\"'".format(name))
      print('=== エラー内容 ===')
      print(traceback.format_exc())
      print('type:' + str(type(e)))
      print('args:' + str(e.args))
      print('message:' + e.message)
      print('e自身:' + str(e))
  
def return_footpoint(name, pcmax_windowhandle, driver, return_foot_message, cnt):
  wait = WebDriverWait(driver, 15)
  driver.switch_to.window(pcmax_windowhandle)
  wait_time = random.uniform(2, 3)
  driver.get("https://pcmax.jp/pcm/index.php")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(1)
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
  print(len(div))
  # リンクを取得
  cnt = 1
  link_list = []
  while cnt <= 30:
    # link = div[cnt].find_elements(By.TAG_NAME, value="a")[1].get_attribute("href")
    a_tags = div[cnt].find_elements(By.TAG_NAME, value="a")
    print("aタグの数：" + str(len(a_tags)))
    if len(a_tags):
      link = a_tags[1].get_attribute("href")
      print(link)
      link_list.append(link)
    cnt += 1
  for i in link_list:
    driver.get(i)
    # //*[@id="profile-box"]/div/div[2]/p/a/span
    sent = driver.find_elements(By.XPATH, value="//*[@id='profile-box']/div/div[2]/p/a/span")
    if len(sent):
      print('送信履歴があります')
      continue
    print("うひょひょ")
  

