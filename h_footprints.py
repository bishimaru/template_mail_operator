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

def happymail_footprints(driver, wait):
  user_lists = [
   ["くみ", "09022346299", 4512],
    ["えりか", "09040563832", 7896],
    ["りな", "08082181793", 1020],
    ["めあり","07026122542", 5461],
     ["きりこ", "08022257429", 1159],
    ["ゆりあ", 50071405699, 3787],
    ["あやか", 50096816478, 1448],
    ["みすず", "08095063912", 3576],
  ]
  
  for user_list in user_lists:
      try:
        happymail.make_footprints(user_list[0], user_list[1], user_list[2], driver, wait)
      except Exception as e:
        print(traceback.format_exc())

if __name__ == '__main__':
  # if len(sys.argv) < 2:
  #   cnt = 20
  # else:
  #   cnt = int(sys.argv[1])
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

  happymail_footprints(driver, wait)
      