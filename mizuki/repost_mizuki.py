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

def repost_happymail_pcmax():
  adult_flag = True
  genre_flag = setting.genre_flag
  name = "みづき"
  title = "SはサービスのSです♪せふれさん(^ ^)"
  text = """はじめまして、美月（みづき）と言います。
脱毛サロンのエステティシャンをしています。

おっとりとした性格で、癒し系だねとよく言われます。。
でも本当は優しく責めるのが好きで...VIOの施術をしている時に我慢している男の人を見てこっそり興奮してます(ノД`)

もちろん仕事は仕事としてちゃんとやるし、クレームとかはもらったことないですが、施術が終わって頑張った後のお客様を見てるとつい「ヨシヨシ」したくなっちゃいます・・・実際はお疲れ様でしたと言うだけですが笑

このままだと仕事に支障が出ちゃいそうなので、プライベートで会えるせふれさん探してます(>_<)
あ◯こを攻めたり、ヨシヨシできる人がいいかも笑

せふれ探してて、こう言うものありかな？って思ってくれたらメッセージしてみて下さいヽ(^o^)"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)

  try:   
    happymail.re_post(name, h_w, driver, title, text, adult_flag, genre_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, p_w, driver)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()