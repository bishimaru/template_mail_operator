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
import re
from selenium.common.exceptions import TimeoutException
import sqlite3
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func


def send_fst_mail(name, login_id, login_pass, fst_message, fst_message_img, second_message, maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort_list):
  options = Options()
  # options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  # driver = func.get_firefox_driver()
  wait = WebDriverWait(driver, 15)
  try:
    driver.delete_all_cookies()
    driver.get("https://pcmax.jp/pcm/file.php?f=login_form")
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  except TimeoutException as e:
    print("TimeoutException")
    driver.refresh()
  wait_time = random.uniform(6, 8)
  time.sleep(2)
  id_form = driver.find_element(By.ID, value="login_id")
  id_form.send_keys(login_id)
  pass_form = driver.find_element(By.ID, value="login_pw")
  pass_form.send_keys(login_pass)
  time.sleep(1)
  send_form = driver.find_element(By.NAME, value="login")
  send_form.click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(3)
  try:
    send_cnt = 1
    while True:
      # if second_message:
      #   print("新着チェック")
      #   # 新着があるかチェック
      #   new_message_elem = driver.find_elements(By.CLASS_NAME, value="message")
      #   if len(new_message_elem):
      #     new_message = new_message_elem[0]
      #   else:
      #     new_message = ""
      #     print('新着メール取得に失敗しました')
      #   if new_message:
      #     if new_message.text[:2] == "新着":
      #       print('新着があります')
      #       message = driver.find_elements(By.CLASS_NAME, value="message")[0]
      #       message.click()
      #       wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      #       time.sleep(2)
      #       while True:
      #         # メッセージ一覧を取得
      #         message_list = driver.find_elements(By.CLASS_NAME, value="receive_user")
      #         new_mail_link_list = []
      #         for msg_elem in message_list:
      #           new = msg_elem.find_elements(By.CLASS_NAME, value="unread1")
      #           if new:
      #             arrival_date = msg_elem.find_elements(By.CLASS_NAME, value="date")
      #             date_numbers = re.findall(r'\d+', arrival_date[0].text)
      #             # datetime型を作成
      #             arrival_datetime = datetime(int(date_numbers[0]), int(date_numbers[1]), int(date_numbers[2]), int(date_numbers[3]), int(date_numbers[4])) 
      #             now = datetime.today()
      #             elapsed_time = now - arrival_datetime
      #             print(f"メール到着からの経過時間{elapsed_time}")
      #             if elapsed_time >= timedelta(minutes=4):
      #               print("4分以上経過しています。")
      #               # リンクリストを作る
      #               # https://pcmax.jp/mobile/mail_recive_detail.php?mail_id=1141727044&user_id=19560947
      #               # user_id取得
      #               user_photo = msg_elem.find_element(By.CLASS_NAME, value="user_photo")
      #               user_link = user_photo.find_element(By.TAG_NAME, value="a").get_attribute("href")
      #               # user_id=以降の文字列を取得
      #               start_index = user_link.find("user_id=")
      #               if start_index != -1:
      #                   user_id = user_link[start_index + len("user_id="):]
      #                   # print("取得した文字列:", user_id)
      #               else:
      #                   print("user_idが見つかりませんでした。")
      #               # mail_id取得
      #               mail_id = msg_elem.find_element(By.TAG_NAME, value="input").get_attribute("value")
      #               new_mail_link = "https://pcmax.jp/mobile/mail_recive_detail.php?mail_id=" + str(mail_id) + "&user_id=" + str(user_id)
                    
      #               # print(new_mail_link)
      #               new_mail_link_list.append(new_mail_link)

      #         for new_mail_user in new_mail_link_list:
      #           driver.get(new_mail_user)
      #           wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      #           time.sleep(2)
      #           # やり取りがないか
      #           all_mail = driver.find_elements(By.ID, value="all_mail")
      #           if len(all_mail):
      #             all_mail[0].click()
      #             time.sleep(1)
      #             sent_by_me = driver.find_elements(By.CLASS_NAME, value="right_balloon_w")
      #             sent_by_me_maji = driver.find_elements(By.CLASS_NAME, value="right_balloon-maji")
      #           else:
      #             sent_by_me = driver.find_elements(By.CLASS_NAME, value="right_balloon_w")
      #             sent_by_me_maji = driver.find_elements(By.CLASS_NAME, value="right_balloon-maji")
      #           no_history_second_mail = True
      #           # メッセージ送信一件だけ
      #           if len(sent_by_me) == 1 and len(sent_by_me_maji) == 0:
      #             sent_by_me_list = []
      #             for sent_list in sent_by_me:
      #               sent_by_me_list.append(sent_list)
      #             for send_my_text in sent_by_me_list:
      #               # print("<<<<<<<<<<<<<<履歴>>>>>>>>>>>>>>>>>>")
      #               # print(send_my_text.text)
      #               # print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")
      #               # print("<<<<<<<<<<<<<<second_mail>>>>>>>>>>>>>>>>>>")
      #               # print(second_message)
      #               # print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")
      #               if send_my_text.text == second_message:
      #                 print("second_mail履歴あり")
      #                 no_history_second_mail = False
      #             # secondメッセージを入力
      #             if no_history_second_mail:
      #               text_area = driver.find_element(By.ID, value="mdc")
      #               text_area.send_keys(second_message)
      #               time.sleep(4)
      #               send = driver.find_element(By.ID, value="send_n")
      #               send.click()
      #               wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      #               time.sleep(wait_time)
      #         driver.get("https://pcmax.jp/pcm/index.php")
      #         wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      #         time.sleep(2)
      #         print("新着チェック終了")
      #         break
      # 利用制限中
      suspend = driver.find_elements(By.CLASS_NAME, value="suspend-title")
      if len(suspend):
        print(f'{name}利用制限中です')  
        driver.quit()
        return
      #プロフ検索をクリック
      footer_icons = driver.find_element(By.ID, value="sp_footer")
      search_profile = footer_icons.find_element(By.XPATH, value="./*[1]")
      search_profile.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(3)
      # 検索条件を設定
      search_elem = driver.find_element(By.ID, value="search1")
      search_elem.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
      # 地域選択
      select_area = driver.find_elements(By.CLASS_NAME, value="pref-select-link")
      if len(select_area):
        select_link = select_area[0].find_elements(By.TAG_NAME, value="a")
        select_link[0].click()
      else:
        # 都道府県の変更、リセット
        reset_area = driver.find_elements(By.CLASS_NAME, value="reference_btn")
        reset_area[0].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        reset_area_orange = driver.find_elements(By.CLASS_NAME, value="btn-orange")
        reset_area_orange[0].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        ok_button = driver.find_element(By.ID, value="link_OK")
        ok_button.click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        select_area = driver.find_elements(By.CLASS_NAME, value="pref-select-link")
        # たまにエラー
        select_area_cnt = 0
        while not len(select_area):
          time.sleep(1)
          print("select_areaが取得できません")
          select_area = driver.find_elements(By.CLASS_NAME, value="pref-select-link")
          select_area_cnt += 1
          if select_area_cnt == 10:
            break

        select_link = select_area[0].find_elements(By.TAG_NAME, value="a")
        select_link[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
      area_id_dict = {"静岡県":27, "新潟県":13, "山梨県":17, "長野県":18, "茨城県":19, "栃木県":20, "群馬県":21, "東京都":22, "神奈川県":23, "埼玉県":24, "千葉県":25}
      area_ids = []
      for select_area in select_areas:
        if area_id_dict.get(select_area):
          area_ids.append(area_id_dict.get(select_area))
      for area_id in area_ids:
        if 19 <= area_id <= 25:
          region = driver.find_elements(By.CLASS_NAME, value="select-details-area")[1]
        elif 13 <= area_id <= 18:
          region = driver.find_elements(By.CLASS_NAME, value="select-details-area")[2]
        elif 26 <= area_id <= 29:
          region = driver.find_elements(By.CLASS_NAME, value="select-details-area")[4]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", region)
        check = region.find_elements(By.ID, value=int(area_id))
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check[0])
      save_area = driver.find_elements(By.NAME, value="change")
      time.sleep(1)
      save_area[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
      # 年齢
      if youngest_age:
        if 17 < int(youngest_age) < 59:
          str_youngest_age = youngest_age + "歳"
        elif 60 <= int(youngest_age):
          str_youngest_age = "60歳以上"
        from_age = driver.find_element(By.NAME, value="from_age")
        select_from_age = Select(from_age)
        select_from_age.select_by_visible_text(str_youngest_age)
        time.sleep(1)
      else:
        youngest_age = ""
      if oldest_age:
        if 17 < int(oldest_age) < 59:
          str_oldest_age = oldest_age + "歳"
        elif 60 <= int(oldest_age):
          str_oldest_age = "60歳以上" 
        to_age = driver.find_element(By.ID, "to_age")
        select = Select(to_age)
        select.select_by_visible_text(str_oldest_age)
        time.sleep(1)
      else:
        youngest_age = ""
      # ページの高さを取得
      last_height = driver.execute_script("return document.body.scrollHeight")
      while True:
        # ページの最後までスクロール
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # ページが完全に読み込まれるまで待機
        time.sleep(2)
        # 新しい高さを取得
        new_height = driver.execute_script("return document.body.scrollHeight")
        # ページの高さが変わらなければ、すべての要素が読み込まれたことを意味する
        if new_height == last_height:
            break
        last_height = new_height
      # 履歴あり、なしの設定
      mail_history = driver.find_elements(By.CLASS_NAME, value="thumbnail-c")
      check_flag = driver.find_element(By.ID, value="opt3") 
      is_checked = check_flag.is_selected()
      while not is_checked:
          mail_history[2].click()
          time.sleep(1)
          is_checked = check_flag.is_selected()

      enter_button = driver.find_elements(By.ID, value="search1")
      enter_button[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

      # ユーザーリスト並び替え設定
      user_sort = driver.find_element(By.ID, "sort2")
      select = Select(user_sort)
      select.select_by_visible_text(user_sort_list[0])
      time.sleep(1)
      # ユーザーを取得
      user_list = driver.find_element(By.CLASS_NAME, value="content_inner")
      users = user_list.find_elements(By.XPATH, value='./div')
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
          # print('ユーザー件数200　OVER')
          break
        # 新しい高さを取得
        new_height = driver.execute_script("return document.body.scrollHeight")
        # ページの高さが変わらなければ、すべての要素が読み込まれたことを意味する
        if new_height == last_height:
            break
        last_height = new_height
      # ユーザーのhrefを取得
      user_cnt = 1
      link_list = []
      for user_cnt in range(len(users)):
        # 実行確率（80%の場合）
        execution_probability = 0.80
        # ランダムな数値を生成し、実行確率と比較
        if random.random() < execution_probability:
          user_id = users[user_cnt].get_attribute("id")
          if user_id == "loading":
            # print('id=loading')
            while user_id != "loading":
              time.sleep(2)
              user_id = users[user_cnt].get_attribute("id")
          link = "https://pcmax.jp/mobile/profile_detail.php?user_id=" + user_id + "&search=prof&condition=648ac5f23df62&page=1&sort=&stmp_counter=13&js=1"
          random_index = random.randint(0, len(link_list))
          link_list.insert(random_index, link)

      # print(f'リンクリストの数{len(link_list)}')
      # メール送信
      for idx, link_url in enumerate(link_list, 1):
        send_status = True
        driver.get(link_url)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        # 名前を取得
        user_name = driver.find_elements(By.CLASS_NAME, value="page_title")
        if len(user_name):
          user_name = user_name[0].text
        else:
          user_name = ""
        # 年齢,活動地域を取得
        profile_data = driver.find_elements(By.CLASS_NAME, value="data")
        span_cnt = 0
        while not len(profile_data):
          time.sleep(1)
          profile_data = driver.find_elements(By.CLASS_NAME, value="data")
          span_cnt += 1
          if span_cnt == 10:
            print("年齢と活動地域の取得に失敗しました")
            break
        if not len(profile_data):
          user_age = ""
          area_of_activity = ""
        else:
          span_elem = profile_data[0].find_elements(By.TAG_NAME, value="span")
          span_elem_list = []
          for span in span_elem:
            span_elem_list.append(span)
          for i in span_elem_list:
            if i.text == "送信歴あり":
              print(f"{name}:送信歴ありのためスキップ")
              send_status = False
              send_cnt += 1
              break
          user_age = span_elem[0].text
          area_of_activity = span_elem[1].text
        # 自己紹介文をチェック
        
        self_introduction = driver.find_elements(By.XPATH, value="/html/body/main/div[4]/div/p")
        if len(self_introduction):
          self_introduction = self_introduction[0].text.replace(" ", "").replace("\n", "")
          for ng_word in ng_words:
            if ng_word in self_introduction:
              print('自己紹介文に危険なワードが含まれていました')
              time.sleep(wait_time)
              send_status = False
              continue
            if send_status == False:
              break
        # 残ポイントチェック
        if maji_soushin:
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
        
        # メッセージを送信
        if send_status:
          # メッセージをクリック
          message = driver.find_elements(By.ID, value="message1")
          if len(message):
            message[0].click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(3)
          else:
            continue
          # 画像があれば送付
          if fst_message_img:
            picture_icon = driver.find_elements(By.CLASS_NAME, value="mail-menu-title")
            picture_icon[0].click()
            time.sleep(1)
            picture_select = driver.find_element(By.ID, "my_photo")
            select = Select(picture_select)
            select.select_by_visible_text(fst_message_img)
          # メッセージを入力
          text_area = driver.find_element(By.ID, value="mdc")
          text_area.send_keys(fst_message)
          time.sleep(4)
        
          if maji_soushin:
            send = driver.find_elements(By.CLASS_NAME, value="maji_send")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", send[0])
            send[0].click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(1)
            send_link = driver.find_element(By.ID, value="link_OK")
            send_link.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(wait_time)
          else:
            send = driver.find_element(By.ID, value="send_n")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", send)
            send.click()
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            time.sleep(wait_time)
          time.sleep(wait_time)
          print(str(name) + ": pcmax、マジ送信 " + str(maji_soushin) + " ~" + str(send_cnt) + "~ " + str(user_age) + " " + str(area_of_activity) + " " + str(user_name))
          send_cnt += 1
        if send_cnt == limit_send_cnt + 1:
          driver.quit()
          print(f"<<<<<<<<<<<{name}、送信数{send_cnt - 1}件:上限に達しました>>>>>>>>>>>>>>")
          break
      try:
        driver.get("https://pcmax.jp/pcm/index.php")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(wait_time)
      except TimeoutException as e:
        print("TimeoutException")
        driver.refresh()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(2)
      

  # 何らかの処理
  except KeyboardInterrupt:
    print("Ctl + c")
    driver.quit()  
  except Exception:
    print("警告画面、何らかのエラー")
    driver.quit()  