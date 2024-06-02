from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import widget.pcmax 
import widget.mail_reception_check
import time
import sqlite3
from selenium.common.exceptions import TimeoutException


check_character_list = [
  "アスカ", "きりこ"
]

options = Options()
# options.add_argument('--headless')
profile_path = "/Users/yamamotokenta/Library/Application Support/Google/Chrome/Profile 13"
options.add_argument(f"user-data-dir={profile_path}")
# options.add_experimental_option("debuggerAddress", "localhost:9222")
options.add_experimental_option("detach", True)


# options.add_argument("--no-sandbox")
# options.add_argument("--remote-debugging-port=9222")
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)



# ウィンドウハンドルを取得
window_handles = driver.window_handles
# ウィンドウハンドルを表示
print(window_handles)
time.sleep(1000)
# 例としてGoogleにアクセス

# ページタイトルを表示
# print(driver.title)

# 操作終了後にブラウザを閉じる
driver.quit()

# for window_handle in window_handles:
#   widget.mail_reception_check.mail_reception_check(window_handle, driver, wait)



  