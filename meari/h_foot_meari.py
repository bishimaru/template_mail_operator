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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback

def h_foot(cnt):
  name = "めあり"
  relative_path = os.path.join(setting.BASE_DIR, setting.meari_picture_path)
  return_foot_img = relative_path
  
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
  h_w = func.get_windowhandle("happymail", name)
  try:   
    happymail.return_footpoint(name, h_w, driver, return_foot_message, cnt, return_foot_img)
    print('<<<<<<<<<<<<めあり　ハッピーメール足跡返し　完了>>>>>>>>>>>>>>')
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_foot(cnt)