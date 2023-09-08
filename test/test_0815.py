from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sqlite3
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback




dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# profile_path = '/Users/yamamotokenta/Library/Application Support/Google/Chrome'
# erika_profile = "Profile 39"
# kumi_profile = "Profile 38"
# asuka_profile = "Profile 54"
# rina_profile = "Profile 35"
# meari_profile = "Profile 40"
# riko_profile = "Profile 46"
# haru_profile = "Profile 45"
# ayaka_profile = "Profile 53"
# kiriko_profile = "Profile 52"
# yuko_profile = "Profile 47"
# momoka_profile = "Profile 44"
# yuria_profile = "Profile 42"
# maiko_profile = "Profile 5"
# haru2_profile = "Profile 55"
# yua_profile = 'Default' 
# mizuki_profile = "Profile 43"

characters = {
   "ももか":{},
   "きりこ":{},
}
# データ検索
for chara_name in characters:
  cur.execute('SELECT * FROM pcmax WHERE name = ?', (chara_name,))
  for row in cur:
      # print("キャラ情報")
      # print(row)
      characters[chara_name]["login_id"] = row[2]
      characters[chara_name]["login_pass"] = row[3]
      characters[chara_name]["fst_message"] = row[5]
      characters[chara_name]["fst_message_img"] = row[6]
      characters[chara_name]["second_message"] = row[9]
      
      
print(characters)

# ドライバ設定
def chrome():
  profile_path = '/Users/yamamotokenta/Library/Application Support/Google/Chrome'
  options = Options()
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  # options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  options.add_experimental_option("detach", True)
  options.add_argument("--incognito")  # シークレットモードを有効にするオプション
  # options.add_argument("--disable-cache")
  # options.add_argument('--lang=ja')
  # options.add_argument('--user-data-dir=' + profile_path)
  # options.add_argument(f'--profile-directory={chara_profile}')
  # options.add_argument(f'--remote-debugging-port={port}')
  # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

  # options.add_argument('--headless')
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  return driver

try:
    # ログイン
    for chara_name, chara_info in characters.items():
      driver = chrome()
      wait = WebDriverWait(driver, 15)
      try:
        driver.delete_all_cookies()
        driver.get("https://pcmax.jp/pcm/file.php?f=login_form")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      except TimeoutException as e:
        print("TimeoutException")
        driver.refresh()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(2)
      id_form = driver.find_element(By.ID, value="login_id")
      id_form.send_keys(chara_info["login_id"])
      pass_form = driver.find_element(By.ID, value="login_pw")
      pass_form.send_keys(chara_info["login_pass"])
      time.sleep(1)
      send_form = driver.find_element(By.NAME, value="login")
      send_form.click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(3)
      # 利用制限中
      suspend = driver.find_elements(By.CLASS_NAME, value="suspend-title")
      if len(suspend):
        print(f'{chara_name} 利用制限中です')

      characters[chara_name]["driver"] = driver
    # プロフ検索
    for chara_name, chara_info in characters.items():
      driver = chara_info["driver"]
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
       
       

    print(777)
   



      

except Exception as e:
    print(traceback.format_exc())

    # driver.close()
    # driver.quit()