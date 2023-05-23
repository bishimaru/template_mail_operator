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

def repost_happymail_pcmax():
  name = "ゆりあ"
  title = "仕事終わりの人肌恋しさ共感できませんか？不動産OLしてます☆"
  text = """投稿見てくれて嬉しいです(^ ^)
  不動産の営業をしている『ゆりあ』って言います♪

  最初はなかなか慣れない仕事に休みの日やお家に帰ってからも悩まされていたのですが、最近ようやく時間に余裕が出てきました！
  そうなるとふとした瞬間に人肌恋しさが襲ってくるようになってきて(;o;)

  慣れてきたとはいえまだお仕事に集中したい気持ちがあるので、お互いのプライベートに干渉しないで人肌恋しさを埋め合えるような関係が理想です♪

  いっぱいいちゃいちゃできるようなせふれさんとここで出会えたらいいなって思ってます(*^▽^*)
  多くは望まないんですけどフィーリングが合えば嬉しいです！

  ☆プロフィール
  ・ゆりあ/24歳/Dcup
  ・最近朝活をしようと思って、ちゃんと朝ごはんを自分で作るようにしています♪"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  try:   
    happymail.re_post(name, setting.yuria_happy_windowhandle, driver, title, text)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, setting.yuria_pcmax_windowhandle, driver)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()