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
from widget import pcmax, happymail
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback

def p_foot(cnt):
  name = "めあり"
  return_foot_message = """足跡ありがとうございます！
  ホテルで働いている『めあり』って言います◯

  前のせふれさんが職場が遠くなって会えなくなってしまったので、新しいせふれさんを探していますm(_ _)m

  性欲強めな私とのせふれ関係に興味ありませんか？？"""
  
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    pcmax.return_footpoint(name, setting.meari_pcmax_windowhandle, driver, return_foot_message, cnt)
    print('<<<<<<<<<<<<めあり　pcmax足跡返し　完了>>>>>>>>>>>>>>')
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('message:' + e.message)
    print('e自身:' + str(e))
  driver.quit()
  return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  p_foot(cnt)