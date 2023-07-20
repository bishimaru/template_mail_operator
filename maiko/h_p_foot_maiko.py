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
  name = "まいこ"
  return_foot_message = """足跡ありがとうございます！！

大学4年生の麻衣子です。

声優になる夢が捨てきれず、夢を追いかけることにしたんですが、家族に反対されて、彼氏にも捨てられちゃいました...

不安だけど決めたことだし、絶対頑張って見返してやります！

どんな役でもできるように、ここではもっとHな経験をして上手な演技をしたいので、sexパートナーを募集します....( *｀ω´)
たくさんエロい声を出したいし、男性の感じている声も大好きなのでいっぱい気持ちよくしたいです！

会ってる時は恋人みたいにお互いを思いやれる、そして私の「夢」を応援してくれるsexパートナーになってくれませんか？"""  
  h_return_foot_img = ""
  p_return_foot_img = ""
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", "まいこ")
  p_w = func.get_windowhandle("pcmax", "まいこ")

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