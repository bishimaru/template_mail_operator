from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from widget import pcmax, happymail, func

options = Options()
options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=456,912")
# options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
options.add_argument("--disable-cache")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)
# えりか 18819944 1112
  # りな　19052443　2083
  # メアリ　19208796 9438
  # "ゆりあ", 19208867, 5742
  # あやか　18821722　1112
  # 霧子　19137736 7324
  # くみ　19137965  6385
  # 麻衣子　19020699　6842
user_lists = [
    # ["えりか", "09040563832", 7896],
    ["りな", 50023189077, 8198],
    ["めあり","09053232087", 1452],
    ["ゆりあ", 50071405699, 3787],
    ["あやか", 50096816478, 1448],
    ["みすず", "08095350044", 2358],
    ["きりこ", 50090427757, 2966],
    ["くみ", "09022346299", 4512],
    ["まいこ", 50018666325, 1625],
]
for user_list in user_lists:
    try:
       happymail.make_footprints(user_list[0], user_list[1], user_list[2], driver, wait)
    except Exception as e:
      print(traceback.format_exc())
    