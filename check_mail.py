from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, mail_reception_check
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback


def check_mail():
    name = "えりか"
    print(5656)
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("detach", True)
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
      mail_reception_check.mail_reception_check(
            setting.erika_happy_windowhandle,
            setting.erika_pcmax_windowhandle,
            setting.erika_gmail_windowhandle,
            driver,
            name
          )
    except Exception as e:
      print(traceback.format_exc())
      driver.quit()
    


if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  check_mail()