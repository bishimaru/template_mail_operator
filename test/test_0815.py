from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


options = Options()

profile_path = '/Users/yamamotokenta/Library/Application Support/Google/Chrome'
erika_profile = "Profile 39"
kumi_profile = "Profile 38"
asuka_profile = "Profile 54"
rina_profile = "Profile 35"
meari_profile = "Profile 40"
riko_profile = "Profile 46"
haru_profile = "Profile 45"
ayaka_profile = "Profile 53"
kiriko_profile = "Profile 52"
yuko_profile = "Profile 47"
momoka_profile = "Profile 44"
yuria_profile = "Profile 42"
maiko_profile = "Profile 5"
haru2_profile = "Profile 55"
yua_profile = 'Default' 
mizuki_profile = "Profile 43"

chara_profiles = [
  maiko_profile,
  yuria_profile,
]

# ドライバ設定
def chrome(chara_profile):
  profile_path = '/Users/yamamotokenta/Library/Application Support/Google/Chrome'
  options = Options()
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  options.add_argument('--lang=ja')
  options.add_argument('--user-data-dir=' + profile_path)
  options.add_argument(f'--profile-directory={chara_profile}')
  # options.add_argument('--headless')
  # Selenium実行後もChromeを開いたままにする
  # options.add_experimental_option('detach', True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  return driver

try:
    drivers = []
    for chara_profile in chara_profiles:
      driver = chrome(chara_profile)
      drivers.append(driver)
      wait = WebDriverWait(driver, 15)
      driver.get("https://pcmax.jp/")
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(1)
    print(777)
    print(len(drivers))


      

except Exception as e:
    print(e)

    # driver.close()
    # driver.quit()