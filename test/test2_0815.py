from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sqlite3

chara_list = ["まいこ", "ゆりあ"]

dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# データ検索
for chara_name in chara_list:
  cur.execute('SELECT * FROM pcmax WHERE name = ?', (chara_name,))
  for row in cur:
      print("キャラ情報")
      print(row)
      login_id = row[2]
      login_pass = row[3]
      fst_message = row[5]
      fst_message_img = row[6]
             
# 各インスタンス用のポート番号
port_numbers = [9515, 9516]  # 例として2つのポート番号を指定

# ChromeDriverオプションの設定
chrome_options = webdriver.ChromeOptions()

# インスタンスごとに異なるポート番号を指定してChromeDriverを起動
drivers = []
for port in port_numbers:
    
    chrome_options.add_argument(f'--remote-debugging-port={port}')  # ポート番号を設定
    driver = webdriver.Chrome(options=chrome_options)
    drivers.append(driver)

# 各ドライバーでウェブページを開くなどの操作を行う
for idx, driver in enumerate(drivers):
    driver.get("https://www.google.com")
    print(f"Driver {idx + 1} Title:", driver.title)

# ドライバーをクローズ
for driver in drivers:
    driver.quit()






