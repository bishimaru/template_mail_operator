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
from datetime import timedelta


def h_p_foot(cnt):
  name = "めあり"
  return_foot_message = """足跡ぺたぺたありがとうございますー！

旅館で働いているめありって言います( ´｡•ω•)ﾉ

前の彼とは遠距離になってしまって別れてしまってからあっちの方はしばらくご無沙汰していてます( ; ; )

それが原因か最近はカップルのお客さんとかの対応をすると色んな妄想とかをしてしまって、お家で1人でする頻度とかが増えてきて寂しいなって思っています。。。

男性は前の彼氏しか知らないけど、人生で1度くらいはセフさんとかも作ってみたいなって思ってサイトを始めてみました！！

私と長期的な関係を考えてみようかなって思ったらお返事貰えたら嬉しいです(*ˊᵕˋ*)"""  
  relative_path = os.path.join(setting.BASE_DIR, setting.meari_picture_path)
  h_return_foot_img = ""
  p_return_foot_img = "" #230704
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = ""

  try:   
    func.h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img)
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
  h_p_foot(cnt)